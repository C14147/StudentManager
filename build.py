# Student Manager Build Script
# Version 1.0.0
# By C14147@github.com
"""
You can use this program to manager software versions,
then build the project automately.
This project use pyinstaller and nuitka to build.
So,you must install C++ Completer such MinGW or MSVC for
nuitka to build this software.
"""
import subprocess
import shutil
import os

__version__ = "1.0.0"
dev_version = "Development Edition"
if os.path.exists("VERSION"):
	print("Warning: File 'VERSION' is missing. Version will reset.")
	software_version = "1.0.0"
	open("VERSION","w").write("1.0.0")
else:
    software_version = open("VERSION","r").read()
current_path = os.path.abspath('./')

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

    print("Updating Environment Varibles...")
    os.system("setx /A")

    print("========== Packages Install Success ==========")

BUILD_NUMBER = int(open("BUILD",'r').read()) + 1
with open("BUILD",'w') as BUILD:
    print(f"The software is about to be compiled, version:{software_version}.{BUILD_NUMBER}")
    if input("Are you sure to continue?(y/n): ").lower() == "y":
        print("Modifying 'BUILD'...")
        BUILD.write(str(BUILD_NUMBER))
        print("Modifying Software Version...")

        try:
            os.mkdir("BUILD_TEMP")
        except FileExistsError:
            pass
        
        shutil.copytree(
            current_path,
            os.path.join(current_path,"BUILD_TEMP",f"{software_version}.{BUILD_NUMBER}"),
            ignore=shutil.ignore_patterns(
                "BUILD_TEMP","build.py","BUILD"
            )
        )
        
        os.chdir(os.path.join(current_path,"BUILD_TEMP",f"{software_version}.{BUILD_NUMBER}"))
        
        # change __version__ variable in each file
        for root,dirs,files in os.walk("./"):
            for file in files:
                if file.endswith(".py"):
                    if "BUILD_TEMP" in os.path.join(root,file):
                        continue
                    
                    content = open(os.path.join(root,file),'r').read()
                    content = content.replace(dev_version,f"{software_version}.{BUILD_NUMBER}")

                    with open(os.path.join(root,file),'w') as f:
                        f.write(content)

        print("Compiling...")
        p = subprocess.Popen(['pyinstaller','--name','StudentManager','main.py'])
        p.wait()
        if p.poll() !=0:
            print("Compile Failed.")
            exit(-1)
        else:
            print("Build Success.")
            exit(0)
    else:
        pass
        
print("Build Success.")

exit(0)
