from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_dir_structure(path, indent=''):
    path = Path(path)
    if path.is_dir():
        entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
        entries_count = len(entries)
        
        for i, entry in enumerate(entries, start=1):
            is_last = i == entries_count
            
            if entry.is_dir():
                icon, color = '📂', Fore.GREEN
            else:
                icon, color = '📜', Fore.BLUE
            
            connector = '┗' if is_last else '┣'
            
            print(f"{indent}{color}{connector} {icon} {entry.name}")
            
            if entry.is_dir():
                next_indent = indent + ('  ' if is_last else '┃ ')
                print_dir_structure(entry, indent=next_indent)

root_path = 'C:\Windows\Boot'
print(f"{Fore.YELLOW}📦 {Path(root_path).name}")
print_dir_structure(root_path)
