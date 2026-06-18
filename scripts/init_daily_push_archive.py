#!/usr/bin/env python3
"""每日 AI 行业学习推送归档生成器。

读取 data/daily_pushes.json，为每条推送生成独立的 Markdown 页面到
daily-pushes/ 目录，并生成带链接索引的 daily-pushes/README.md。

脚本是幂等的：重复运行会覆盖生成文件，不会产生重复内容。

用法:
    python scripts/init_daily_push_archive.py
"""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "daily_pushes.json"
ARCHIVE_DIR = REPO_ROOT / "daily-pushes"

GENERATED_NOTICE = (
    "> 本归档由应用内每日学习推送记录自动生成，请勿手动编辑生成文件。\n"
    "> 如需重建，请运行 `python scripts/init_daily_push_archive.py`。"
)


def load_data() -> dict:
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def render_page(push: dict) -> str:
    """渲染单条推送为带 YAML frontmatter 的 Markdown 页面。"""
    tags = push.get("tags", [])
    sources = push.get("sources", [])

    lines: list[str] = []
    # YAML frontmatter
    lines.append("---")
    lines.append(f"title: {json.dumps(push['title'], ensure_ascii=False)}")
    lines.append(f"day: {json.dumps(push['day_label'], ensure_ascii=False)}")
    lines.append(f"date: {push['date']}")
    lines.append(f"time: {push['time']}")
    lines.append("timezone: Asia/Shanghai")
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {json.dumps(tag, ensure_ascii=False)}")
    lines.append("---")
    lines.append("")

    lines.append(f"# {push['title']}")
    lines.append("")
    lines.append(
        f"**{push['day_label']}** ｜ {push['date']} {push['time']}（Asia/Shanghai）"
    )
    lines.append("")
    if tags:
        lines.append("标签：" + " ".join(f"`{t}`" for t in tags))
        lines.append("")

    notice = push.get("notice", "").strip()
    if notice:
        lines.append(f"> 说明：{notice}")
        lines.append("")

    for section in push.get("sections", []):
        lines.append(f"## {section['heading']}")
        lines.append("")
        lines.append(section["body"].rstrip())
        lines.append("")

    if sources:
        lines.append("## 来源链接")
        lines.append("")
        for src in sources:
            lines.append(f"- [{src['label']}]({src['url']})")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("[返回归档索引](README.md) ｜ [返回仓库首页](../README.md)")
    lines.append("")

    return "\n".join(lines)


def render_index(data: dict) -> str:
    meta = data.get("meta", {})
    pushes = data.get("pushes", [])

    lines: list[str] = []
    lines.append(f"# {meta.get('title', '每日 AI 行业学习推送归档')}")
    lines.append("")
    lines.append(GENERATED_NOTICE)
    lines.append("")
    desc = meta.get("description", "").strip()
    if desc:
        lines.append(desc)
        lines.append("")

    lines.append("## 推送索引")
    lines.append("")
    lines.append("| Day | 时间 | 主题 | 标签 | 链接 |")
    lines.append("|---|---|---|---|---|")
    for push in pushes:
        tags = "、".join(push.get("tags", []))
        when = f"{push['date']} {push['time']}"
        title = push["title"].replace("|", "\\|")
        link = f"[{title}]({push['slug']}.md)"
        lines.append(
            f"| {push['day_label']} | {when} | {title} | {tags} | {link} |"
        )
    lines.append("")

    lines.append("## 说明")
    lines.append("")
    lines.append(
        "- 时间均为 Asia/Shanghai 时区。"
    )
    lines.append(
        "- 每篇页面保留学习笔记的原始结构（为什么今天要懂它 / 一句话解释 / 核心概念 / 术语卡片 / 今日行动建议等），并附来源链接。"
    )
    lines.append(
        "- 部分早期推送引用了未来日期的材料或存在同日选题重复，相关情况已在对应页面顶部以“说明”标注，未做静默改写。"
    )
    lines.append("")
    lines.append("[返回仓库首页](../README.md)")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    data = load_data()
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    written = []
    for push in data.get("pushes", []):
        page_path = ARCHIVE_DIR / f"{push['slug']}.md"
        page_path.write_text(render_page(push), encoding="utf-8")
        written.append(page_path.name)

    index_path = ARCHIVE_DIR / "README.md"
    index_path.write_text(render_index(data), encoding="utf-8")
    written.append(index_path.name)

    print(f"已生成 {len(written)} 个文件到 {ARCHIVE_DIR.relative_to(REPO_ROOT)}/：")
    for name in written:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
