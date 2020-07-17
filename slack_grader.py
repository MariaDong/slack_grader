import json
from datetime import datetime
import time

while True:
    # Prompt for filename and append to relative file_path, save as file_name.
    file_name_msg = 'Enter filename for chat log, e.g. monsterchat.json.'
    file_name_msg += ' Leave blank and hit [ENTER] 2x to quit.\t'
    file_name = input(file_name_msg)
    if len(file_name_msg) < 1: 
        break
    file_path = 'files_to_grade//' + file_name

    # Prompt for users filename and append to relative user_path.
    user_path_msg = 'Enter filename for user log, e.g. users.json.'
    user_path_msg += 'Leave blank and hit [ENTER] to quit.\t'
    user_file_name = input(user_path_msg)
    if len(user_file_name) < 1: 
        break
    user_path = 'user_file//' + user_file_name

    # Open the user_path, parse real_names and make a pretty list.
    user_list = []
    with open(user_path) as users_file:
        full_user_data = json.load(users_file)
    print('Here is a list of all users.')
    for user in full_user_data:
        real_name = f"Real Name: {user['real_name']}, "
        id_number = f"User ID: {user['id']}"
        full = real_name + id_number
        user_list.append(full)
        user_list.sort()
    print(user_list)

    # Save the user_list to a text file in reports folder.
    # Use current date_time to second to set a unique filename.
    now = datetime.now()
    now = now.strftime("%Y-%m-%d-%H-%M-%S")
    report_file = 'reports//' + now
    time.sleep(1)
    print('...Creating a new file for report capture.')
    time.sleep(1)
    with open(report_file, 'w') as working_file:
        working_file.write(f"REPORT CREATED:\n\t{now}")
        working_file.write(f"\nTOTAL USERS:\n\t{len(user_list)}")
        working_file.write(f"\nLIST OF ALL USERS:\n")
        for user in user_list:
            working_file.write(f"\t{user}\n")
    time.sleep(1)
    print('...User list added to report.')

    # json_file = urllib.request.urlopen(address, context=ctx)
    # json_data = json_file.read()
    # json_list = json.loads(json_data)
    # json_list = json_list['comments']
    # comment_sum = 0
    # for user in json_list:
    #     comment_sum += user['count']
    # print(comment_sum)
