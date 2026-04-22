from pathlib import Path

def print_tree(path, prefix=''):
    # Iterate through current directory items
    for item in sorted(path.iterdir()):
        connector = '├── ' if item != list(path.iterdir())[-1] else '└── '
        print(f'{prefix}{connector}{item.name}')
        
        if item.is_dir():
            # Extend prefix for sub-folders
            new_prefix = prefix + ('│   ' if connector == '├── ' else '    ')
            print_tree(item, new_prefix)

# Usage
root_path = Path('.')
print(root_path.name + '/')
print_tree(root_path)
