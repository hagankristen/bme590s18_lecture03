def main():
    filenames = collect_csv_files()
    student_data = cat_data(filenames)
    write_csv(student_data)

def collect_csv_files():
    from glob import glob
    csv_names = []
    for file_name in glob('*.csv'):
        csv_names.append(file_name)
    return csv_names
    pass

def cat_data(filenames):
    import numpy as np
    import json
    all_data = []
    counter = 0
    for csv_file in filenames:
        flag = check_name(csv_file)
        c = np.loadtxt(csv_file, delimiter=',', dtype='str', encoding = 'utf-8-sig')
        if flag:
            all_data.append(c)
            counter = check_camel_case(c, counter)
            check_no_spaces(c, csv_file)
            write_json(c, csv_file)
    print('Number of Camel Cases Found:', counter, flush=True)
    return all_data
    pass

def write_csv(student_files):
    import numpy as np
    np.savetxt("everyone.csv", student_files, delimiter=",",fmt="% s")
    pass

def check_name(entry):
    if entry == 'mlp6.csv':
        flag =0
    elif entry == 'everyone.csv':
        import os
        if os.path.exists("everyone.csv"):
            os.remove("everyone.csv")
        flag = 0
    else:
        flag =1
    return flag
    pass

def write_json(entry, filename):
    import json
    name = filename.strip('.csv')
    json_name = name +'.json'
    save = entry.tolist()
    with open(json_name, 'w') as f:
        json.dump(save, f)
    pass

def check_camel_case(entry, counter):
    team = entry[4]
    flag = (team != team.lower() and team != team.upper())
    if flag:
        counter = counter + 1
    return counter
    pass

def check_no_spaces(entry, filename):
    team = entry[4]
    if team.find(' ') == -1:
        print('Spaces in team name identified in', filename)
    pass

if __name__ == "__main__":
    main()
