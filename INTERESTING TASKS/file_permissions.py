file_permissions_input = []
tasks_input = []
file_permissions = {}
file_access_log = []
operations = {'execute': 'X',  'read': 'R', 'write': 'W'}
for _ in range(int(input())):
    file_permissions_input.append(input())
for _ in range(int(input())):
    tasks_input.append(input())
for row in file_permissions_input:
    info = row.split()
    name, operation_set = info[0], set(info[1:])
    file_permissions[name] = operation_set
for row in tasks_input:
    info = row.split()
    operation, name = info[0], info[1]
    if operations[operation] in file_permissions[name]:
        file_access_log.append('OK')
    else:
        file_access_log.append('Access denied')
for status in file_access_log:
    print(status)