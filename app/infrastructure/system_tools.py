from pathlib import Path
import shutil


class SystemTools:
    """
    Utility methods for discovering external tools.
    """

    @staticmethod
    def find_ffmpeg() -> str | None:
        return shutil.which("ffmpeg")

    @staticmethod
    def find_deno() -> str | None:

        deno = shutil.which("deno")
        if deno:
            return deno

        winget_packages = (
            Path.home()
            / "AppData"
            / "Local"
            / "Microsoft"
            / "WinGet"
            / "Packages"
        )

        if winget_packages.exists():
            for exe in winget_packages.rglob("deno.exe"):
                return str(exe)

        return None