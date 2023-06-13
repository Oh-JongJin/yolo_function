import os

# Label path to access
label_path = 'coco/valid/labels/'
label_list = os.listdir(label_path)

# Create a new folder and save it here
result_label_path = 'del_face_labels/valid/'
os.makedirs(result_label_path, exist_ok=True)

# Class number to remove
del_class = 1

for count, name in enumerate(label_list):
    result_list = []
    print(count, f'{label_path}{name}')
    with open(f'{label_path}{name}', 'r') as f:
        data = f.readlines()
    data.sort()

    for i in data:
        if i.find(f'{del_class} ') == 0:
            data.remove(i)
        else:
            result_list.append(i)

    with open(f'{result_label_path}{name}', 'w') as f:
        for i in result_list:
            f.write(i)
