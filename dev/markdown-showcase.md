# Markdown showcase

This local paste exercises the parts of Markdown that should be easy to read in pb.

## Status table

| Service | Owner | Status | Notes |
| --- | :--- | :---: | --- |
| Renderer | Web Platform | Ready | Supports headings, tables, and code. |
| Mobile layout | Web Platform | In progress | Wide tables should scroll without widening page. |
| Documentation | Everyone | Planned | Links, lists, and callouts should be clear at a glance. |

## Code and callouts

> A blockquote should look distinct without overpowering the document.

```python
def render_markdown(source: bytes) -> str:
    """Render Markdown content for a paste preview."""
    return source.decode("utf-8")
```

Use inline code such as `pb/r/<id>.md` when describing a URL.

## Lists

1. Create or update this paste with the seed script.
2. Open the stable rendered URL.
3. Refresh the page after changing renderer styles.

- Nested content should remain readable.
  - Links such as [pb](http://localhost:10002/) need a clear visual treatment.
  - Long words and wide table cells must not break the page layout.

---

The source of this showcase lives in `dev/markdown-showcase.md`.
