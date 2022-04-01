import platform
import os

platform = platform.system()

match platform:
    case "Linux":
        command = "python3 --version"
        os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
    case "Darwin":
        pass
    case "Windows":
        os.system("start cmd /K ipconfig")
    case _: print('ciao')
