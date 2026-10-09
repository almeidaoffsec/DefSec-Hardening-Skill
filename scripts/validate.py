#!/usr/bin/env python3
"""Verifica estrutura e referências locais; não avalia comportamento do modelo."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]\n]+\]\(([^\s)]+)\)")
FIELDS = (
    "PLAYBOOKS",
    "INPUT",
    "EXPECTED OBSERVATIONS",
    "EXPECTED STATE UPDATE",
    "EXPECTED PRIORITY",
    "EXPECTED NEXT OBJECTIVE",
    "UNWANTED BEHAVIOR",
)


def main():
    errors = []
    documents = {}
    targets = {}
    files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        documents[relative] = text
        targets[relative] = set()
        if not text.strip():
            errors.append(f"{relative}: arquivo vazio")
        if not text.endswith("\n"):
            errors.append(f"{relative}: falta newline final")
        fence = None
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{relative}:{number}: whitespace no fim da linha")
            marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if marker:
                token, suffix = marker.groups()
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                    fence = None
                continue
            if fence:
                continue
            for link in LINK.findall(line):
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(ROOT):
                    errors.append(f"{relative}:{number}: link fora do repositório: {link}")
                elif not target.is_file():
                    errors.append(f"{relative}:{number}: arquivo de link ausente: {link}")
                else:
                    targets[relative].add(target.relative_to(ROOT).as_posix())
        if fence:
            errors.append(f"{relative}: bloco de código não fechado")

    for required in ("SKILL.md", "README.md", "AGENTS.md", "TESTS.md", "VALIDATION.md", "Roadmap.md"):
        if required not in documents:
            errors.append(f"arquivo obrigatório ausente: {required}")

    # O formato local usa somente name/description, strings JSON entre aspas
    # (subconjunto de YAML). Isto não pretende ser um parser YAML genérico.
    skill = documents.get("SKILL.md", "")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    values = {}
    if not frontmatter:
        errors.append("SKILL.md: frontmatter ausente ou delimitadores inválidos")
    else:
        for line in frontmatter.group(1).splitlines():
            key, separator, value = line.partition(":")
            try:
                if not separator or key in values or key not in ("name", "description"):
                    raise ValueError
                decoded = json.loads(value.strip())
                if not isinstance(decoded, str) or not decoded.strip():
                    raise ValueError
                values[key] = decoded
            except ValueError:
                errors.append(f"SKILL.md: campo inválido no formato local: {line}")
        for key in ("name", "description"):
            if key not in values:
                errors.append(f"SKILL.md: campo obrigatório ausente: {key}")

    operational = {name for name in documents if name.startswith(("playbooks/", "templates/", "references/"))}
    for name in sorted(operational - targets.get("SKILL.md", set())):
        errors.append(f"SKILL.md: arquivo operacional sem referência direta: {name}")

    tests = documents.get("TESTS.md", "")
    scenarios = list(re.finditer(r"^### ([TM]\d{2}) — .+$", tests, re.MULTILINE))
    seen = set()
    covered = set()
    for index, match in enumerate(scenarios):
        scenario_id = match.group(1)
        if scenario_id in seen:
            errors.append(f"TESTS.md: ID duplicado: {scenario_id}")
        seen.add(scenario_id)
        end = scenarios[index + 1].start() if index + 1 < len(scenarios) else len(tests)
        body = tests[match.end():end]
        for field in FIELDS:
            entries = re.findall(rf"^- {re.escape(field)}: (.+)$", body, re.MULTILINE)
            if len(entries) != 1:
                errors.append(f"TESTS.md/{scenario_id}: esperado um campo {field}")
            if field == "PLAYBOOKS" and entries:
                routed = {link for link in LINK.findall(entries[0]) if link.startswith("playbooks/")}
                if not routed:
                    errors.append(f"TESTS.md/{scenario_id}: nenhum playbook relacionado")
                covered.update(routed)
    if not scenarios or not any(key.startswith("M") for key in seen):
        errors.append("TESTS.md: faltam cenários ou cenário multi-turn")
    playbooks = {name for name in operational if name.startswith("playbooks/")}
    for name in sorted(playbooks - covered):
        errors.append(f"TESTS.md: playbook sem cenário associado: {name}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(documents)} documentos, {len(playbooks)} playbooks, {len(scenarios)} cenários estruturados.")
    print("Links locais, frontmatter restrito, blocos e cobertura declarada verificados; comportamento não executado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
