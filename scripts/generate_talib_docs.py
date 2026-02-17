from pathlib import Path

import talib
from talib import abstract


def _format_params(params):
    if not params:
        return "{}"
    parts = []
    for k, v in params.items():
        if isinstance(v, str):
            parts.append(f"\"{k}\": \"{v}\"")
        else:
            parts.append(f"\"{k}\": {v}")
    return "{" + ", ".join(parts) + "}"


def _format_desc(desc):
    if not desc:
        return "-"
    return desc.replace("\n", " ").strip()


def _collect_by_group():
    groups = {}
    for group_name, func_names in talib.get_function_groups().items():
        entries = []
        for name in func_names:
            f = abstract.Function(name)
            entries.append(
                {
                    "name": name,
                    "desc": _format_desc(f.info.get("display_name")),
                    "params": f.parameters or {},
                }
            )
        groups[group_name] = sorted(entries, key=lambda x: x["name"])
    return groups


def main():
    groups = _collect_by_group()

    lines = []
    lines.append("# Indicator Groups")
    lines.append("")
    for group_name in groups.keys():
        lines.append(f"- {group_name}")
    lines.append("")

    for group_name, entries in groups.items():
        lines.append(f"## {group_name}")
        lines.append("")
        lines.append("| Type | Description | Code Line |")
        lines.append("|---|---|---|")
        for e in entries:
            params = _format_params(e["params"])
            code_line = f"\"{e['name']}\": {params}"
            lines.append(f"| `{e['name']}` | {e['desc']} | `{code_line}` |")
        lines.append("")

    output_path = Path("docs/talib_functions.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
