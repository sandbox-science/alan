from typing import Optional, List, Tuple

def make_embed(
    description: str,
    title: Optional[str] = None,
    field: Optional[str] = None,
) -> str:
    """
    Create a Markdown-styled embed message.

    Args:
        description: Main content of the embed.
        title: Optional title for the embed.
        fields: Optional list of (name, value) tuples for extra fields.

    Returns:
        A formatted Markdown string.
    """
    title_text  = f"## {title}"       if title  else ""
    field_text = f"### {field}" if field else ""

    lines = """
---

{title}
{description}
{field}

---
"""

    return lines.format(
        title       = title_text,
        description = description,
        field      = field_text
    ).strip()
