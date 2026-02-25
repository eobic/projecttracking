fp = r'C:\Users\ErvinaObic\OneDrive - Platform Accounting Group-Subs\Desktop\Claude\GitHub\projecttracking\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Original lines:', len(lines))

# Find section boundaries by searching for tab comment markers
main_start = main_end = None
ervina_start = ervina_end = None
abdul_start = abdul_end = None
fpv_start = completed_start = None

for i, line in enumerate(lines):
    s = line.strip()
    if '<!-- TAB 1: ALL PROJECTS' in s:
        main_start = i - 1  # include the === line above
    elif '<!-- TAB: FULL PROJECT VIEW' in s:
        fpv_start = i - 1
        if main_start is not None and main_end is None:
            main_end = i - 1  # up to (not including) the === line
    elif '<!-- TAB 2: ERVINA' in s:
        ervina_start = i - 1
    elif '<!-- TAB 3: ABDULRAHMAN' in s:
        abdul_start = i - 1
        if ervina_start is not None and ervina_end is None:
            ervina_end = i - 1
    elif '<!-- TAB 4: ALL COMPLETED' in s:
        completed_start = i - 1
        if abdul_start is not None and abdul_end is None:
            abdul_end = i - 1

print(f'main: {main_start+1}-{main_end}')
print(f'ervina: {ervina_start+1}-{ervina_end}')
print(f'abdul: {abdul_start+1}-{abdul_end}')

# Build set of lines to delete
delete = set()
for i in range(main_start, main_end):
    delete.add(i)
for i in range(ervina_start, ervina_end):
    delete.add(i)
for i in range(abdul_start, abdul_end):
    delete.add(i)

new_lines = [line for i, line in enumerate(lines) if i not in delete]
print('New lines:', len(new_lines))

with open(fp, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
