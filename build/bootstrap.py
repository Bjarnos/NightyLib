from pathlib import Path
import sys, struct, platform, shutil, zipfile
import tempfile, urllib.request, os

version = sys.version_info
if version[0] != 3 or version[1] != 8:
    raise RuntimeError("NightyLib is only supported on Python 3.8!")

if struct.calcsize("P") * 8 == 32:
    raise RuntimeError("NightyLib doesn't work on 32-bit Python!")

arch = platform.machine().lower()
if sys.platform.startswith("win"):
    if arch == "amd64":
        APPDATA = Path(os.environ["APPDATA"])
    else:
        raise RuntimeError(f"NightyLib doesn't support Windows architecture: {arch}")
else:
    if arch == "x86_64":
        APPDATA = "" # wait for Linux release before we know this
        raise RuntimeError(f"NightyLib support for Linux is WIP!")
    elif arch == "arm64" or arch == "aarch64":
        raise RuntimeError(f"NightyLib support for Linux ARM64 is WIP!")
    else:
        raise RuntimeError(f"NightyLib doesn't support Linux architecture: {arch}")
    
BASE_DIR = APPDATA / "Nighty Selfbot" / "data"
TARGET_DIR = BASE_DIR / "NightyLib"
LOCAL_VERSION_FILE = TARGET_DIR / "version.txt"

VERSION_URL = "https://raw.githubusercontent.com/Bjarnos/NightyLib/refs/heads/main/build/version.txt"
ZIP_URL = "https://github.com/Bjarnos/NightyLib/archive/refs/heads/main.zip"

def read_local_version():
    try:
        return LOCAL_VERSION_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None


def read_remote_version():
    with urllib.request.urlopen(VERSION_URL) as response:
        return response.read().decode("utf-8").strip()

def download():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        zip_path = tmpdir / "nightylib.zip"

        urllib.request.urlretrieve(ZIP_URL, zip_path)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmpdir)

        extracted_root = tmpdir / "NightyLib-main"
        build_dir = extracted_root / "build"

        if TARGET_DIR.exists():
            shutil.rmtree(TARGET_DIR)

        BASE_DIR.mkdir(parents=True, exist_ok=True)

        shutil.move(str(build_dir), str(TARGET_DIR))

def install():
    if str(TARGET_DIR) not in sys.path:
        sys.path.append(str(TARGET_DIR))

local_version = read_local_version()
remote_version = read_remote_version()
if local_version != remote_version:
    download()
    
install()