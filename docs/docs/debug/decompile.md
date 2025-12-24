---
sidebar_position: 3
---

# Decompile

Attributes related to decompiling Python objects.

:::warning

"Attempting to reverse-engineer, decompile, or modify the software" goes against [Nighty's ToS](https://nighty.one/terms-of-service).
<br></br>**Use at your own risk!** Never share scripts that use these attributes publicly.

:::

## decompile
<p style={{ color: 'gray', marginBottom: '1%' }}>2.0.0</p>
```py
def nightylib.debug.decompile(obj: Any) -> Union[Suite, PyStatement]
```
A powerful function that allows you to decompile code objects back to source code, potentially bypassing restrictions imposed by PyArmor. It accepts a module, a function, a code object, or a string pointing to a `.py` or `.pyc` file as input.

The source code can be found [here](https://github.com/greyblue9/unpyc37-3.10)

```py title="Example: decompile a function"
from nightylib.debug import decompile
def foo(x): return x
print(str(decompile(foo)).strip())
```
```txt title="Output"
def foo(x):
    return x
```

:::tip

You can also import `decompile` directly from the original library:
```py
from unpyc3 import decompile
```

:::
