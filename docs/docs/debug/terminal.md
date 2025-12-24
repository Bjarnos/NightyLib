---
sidebar_position: 4
---

# Terminal

Attributes related to the cross-platform terminal.

## terminal_exec
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
def nightylib.debug.terminal_exec(cmd: str) -> str
```
A potentially dangerous function that executes the given command in the operating system’s native terminal and returns the decoded output.
The command is executed in a background thread, so the user is unlikely to notice it running.

:::info

If the input command is provided as bytes, the return value will also be bytes.

:::