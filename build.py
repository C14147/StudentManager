# Student Manager Build Script
import subprocess


__version__ = "1.0.0"
software_version = "1.0.0"


def installPkg(pkg: str):
    p = subprocess.Popen(['pip3','install',f'{pkg}'])
    p.wait()
    if p.poll() !=0:
        return False
    else:
        return True

print("+--------------------------------------------------+")
print("|========== Student Manager Build Script ==========|")
print("+--------------------------------------------------+")

if input("Do you want to check packages for build?(y/n):").lower() == "y":
    print("Checking Packages...")

    try:
        import tqdm
    except ImportError:
        installPkg("tqdm")
        import tqdm

    pkgs = [
        "PyQt6",
        "PyQt6-tools",
        "PyQt6-Fluent-Widgets[full]",
        "matplotlib",
        "pillow",
        "pyinstaller",
        "nuitka",
    ]

    for i in pkgs:
        if not installPkg(i):
            print(f"\033[1;31mFailed to install '{i}'.\033[0m")
            exit(-1)

    print("========== Packages Install Success ==========")


with open("BUILD",'w+') as BUILD:
    BUILD_NUMBER = int(BUILD.read()) + 1
    print(f"The software is about to be compiled, version:{software_version}.{BUILD_NUMBER}")
    if input("Are you sure to continue?(y/n): ").lower() == "y":
        print("Modifying 'BUILD'...")
        BUILD.write(BUILD_NUMBER)



print("Build Success.")
