---
sidebar_position: 1
---

# Files

Attributes related to parsing and editing files.

## EditableJSON
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
class nightylib.util.EditableJSON(path: str, data: Optional[dict[str, Any]] = None)
```
This class allows you to dynamically edit JSON files during runtime.

```py title="Example: create a new JSON file and edit it"
from nightylib.util import EditableJSON
from pathlib import Path

downloads = Path.home() / "Downloads"

file = downloads / "example.json"
with open(file, "w", encoding="utf-8") as f:
    f.write("{}")

editable = EditableJSON(str(file))
editable.hello = "Hi!"
print(editable.hello)

del editable.hello
```