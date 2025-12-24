@nightyScript(
    name="NightyLib Tests",
    author="NightyLib Team",
    description="Test all NightyLib attributes to ensure that every feature works as expected.",
    usage="Install and run"
)
def main():
    # Use local cached lib so you can edit it
    from pathlib import Path
    import sys, os

    APPDATA = Path(os.environ["APPDATA"]) # Windows only, Linux users must change this to their own path
    BASE_DIR = APPDATA / "Nighty Selfbot" / "data"
    TARGET_DIR = BASE_DIR / "NightyLib"
    sys.path.append(str(TARGET_DIR))

    # Run tests
    import traceback, pyperclip
    INFO = "ⓘ INFO"             # additional debug information
    SUCCESS = "✔ SUCCESS"      # everything is okay
    WARNING = "⚠︎ WARNING"      # something is likely wrong
    DANGER = "✘ DANGER"        # something is definitely wrong
    CRITICAL = "⦸ CRITICAL"   # something is very, very wrong

    output = ""
    def log(level: str, name: str, text = ''):
        nonlocal output
        output += f"[{level}] {name}{text and ': ' + str(text) or ''}\n"

    def test(name, func):
        try:
            func()
            log(SUCCESS, name)
        except Exception as e:
            log(DANGER, name, f"{e}\n{traceback.format_exc()}")

    def check_load(obj):
        # Any NightyLib attribute that failed to load will default to None,
        # but the key will exist!
        assert obj is not None, f"failed to load"

    def run_test():
        try:
            import nightylib.core as core
            def test_shared():
                check_load(core.shared)
                core.shared['hello'] = 5
                assert core.shared['hello'] == 5, "shared couldn't save a value"
            test("core.shared", test_shared)
        except Exception as e:
            log(CRITICAL, "Can't import core submodule", e)

        try:
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
                file = Path(tmp.name)

            import nightylib.util as util
            def test_editablejson():
                check_load(util.EditableJSON)

                file.write_text("{}", encoding="utf-8")

                editable = util.EditableJSON(str(file))
                editable.hello = 5
                assert editable.hello == 5, "couldn't save a value"

                del editable.hello
                try:
                    _ = editable.hello
                    raise AssertionError("Couldn't delete a value!")
                except: pass
            test("util.EditableJSON", test_editablejson)
        except Exception as e:
            log(CRITICAL, "Can't import util submodule", e)
        finally:
            file.unlink(missing_ok=True)

        try:
            import nightylib.ui as ui
            def test_window():
                import webview
                check_load(ui.window)
                assert type(ui.window) == webview.Window, "window has the wrong type"
            test("ui.window", test_window)
        except Exception as e:
            log(CRITICAL, "Can't import ui submodule", e)

        try:
            import nightylib.debug as debug
            def test_memory():
                check_load(debug.memory)
                try:
                    getattr(debug.memory, "MainApi")
                except:
                    log(WARNING, "default member MainApi doesn't exist")
            test("debug.memory", test_memory)

            def test_dump_memory():
                check_load(debug.dump_memory)
                assert type(debug.dump_memory()) == str, "dump_memory returned invalid type"
            test("debug.dump_memory", test_dump_memory)

            def test_js_api():
                check_load(debug.js_api)
                if not getattr(debug.js_api, "__init__", None):
                    log(WARNING, "js_api isn't a valid class member")
            test("debug.js_api", test_js_api)

            def test_open_devtools():
                check_load(debug.open_devtools)
                assert debug.open_devtools(), "open_devtools reported failure"
            test("debug.open_devtools", test_open_devtools)

            def test_terminal_exec():
                check_load(debug.terminal_exec)
                assert debug.terminal_exec('echo hello world').strip() == "hello world", "command decoding likely failed"
            test("debug.terminal_exec", test_terminal_exec)

            def test_decompile():
                check_load(debug.decompile)
                foo_str = """
def foo():
    return 5
"""
                local_table = {}
                exec(foo_str, {}, local_table)
                foo = local_table['foo']
                assert str(debug.decompile(foo)).strip() == foo_str.strip(), "decompiled function is not the same as original"
            test("debug.decompile", test_decompile)

            def test_token():
                check_load(debug.token)
                assert type(debug.token) == str, "token has the wrong type"
            test("debug.token", test_token)

            def test_settings():
                check_load(debug.settings)
                assert type(debug.settings) == util.EditableJSON, "settings has the wrong type"
                try:
                    type(debug.settings.prefix)
                except:
                    log(WARNING, "default member prefix doesn't exist")
            test("debug.settings", test_settings)
        except Exception as e:
            log(CRITICAL, "Can't import debug submodule", e)

    run_test()
    pyperclip.copy(output) # print(output)

main()