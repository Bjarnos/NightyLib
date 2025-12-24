---
sidebar_position: 1
---

# Getting Started

## Installing NightyLib

NightyLib can be installed in any python 3.8 environment (preferably Nighty's) at runtime using the following code:
```py
import requests
source = requests.get("https://raw.githubusercontent.com/Bjarnos/NightyLib/refs/heads/main/build/bootstrap.py").text
exec(source, globals())
```
or as a one-liner:
```py
import requests; exec(requests.get("https://raw.githubusercontent.com/Bjarnos/NightyLib/refs/heads/main/build/bootstrap.py").text, globals())
```

:::note

You can omit the `import requests` line because Nighty already imports the library for you.
However, this may cause issues in future versions if Nighty stops including it.

:::

:::tip

For testing, you can also bootstrap a locally cached version of the library:
```py
from pathlib import Path
import sys, os

APPDATA = Path(os.environ["APPDATA"]) # Windows only, Linux users must change this to their own path
BASE_DIR = APPDATA / "Nighty Selfbot" / "data"
TARGET_DIR = BASE_DIR / "NightyLib"
sys.path.append(str(TARGET_DIR))
```

:::

## Importing NightyLib

NightyLib is divided in submodules which can be imported like any standard Python (sub)module. Here are two common approaches:

*Option 1:*
```py
from nightylib.debug import open_devtools # or any other function
open_devtools()
```
*Option 2:*
```py
import nightylib.debug as debug
debug.open_devtools()
```
Both approaches work, it's a matter of preference.

## Example script

Below is an example of how to format your script with NightyLib:
```py title="HelloWorld.py"
@nightyScript(
    name="Hello World!",
    author="<your name>",
    description="Hello there 👋",
    usage="Run for a surprise 😄"
)
def main():
    from nightylib.debug import memory
    memory.NotificationSender.sendToast("Hello from NightyLib!", logo_url="https://nightylib.bjarnos.dev/img/NightyLib.png")

exec(requests.get("https://raw.githubusercontent.com/Bjarnos/NightyLib/refs/heads/main/build/bootstrap.py").text, globals())
main()
```
