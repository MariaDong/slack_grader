import json
from datetime import datetime

# Prompt for filename and append to relative file_path, save as file_name.
file_name_msg = 'Enter filename for chat log. To run sample, type "sample.json".'
file_name_msg += ' Leave blank and hit [ENTER] 2x to quit.\t'
file_name = input(file_name_msg)
file_path = 'files_to_grade//' + file_name

# Prompt for users filename and append to relative user_path.
user_path_msg = 'Enter filename for user log. To run sample, type "sample.json".'
user_path_msg += 'Leave blank and hit [ENTER] to quit.\t'
user_file_name = input(user_path_msg)
user_path = 'user_file//' + user_file_name

# Open the user_path, parse real names and ids.
# Make user_list, which appends a real name, user id line for text printing.
# make user_list_real_names, which stores only the real names for dict matching.
user_list = []
user_list_real_names = []
with open(user_path, encoding='utf-8') as users_file:
    full_user_data = json.load(users_file)
print("...Creating a user list.")
for user in full_user_data:
    real_name = f"Real Name: {user['real_name']}, "
    id_number = f"Slack User ID: {user['id']}"
    full = real_name + id_number
    user_list.append(full)
    user_list.sort()
    user_list_real_names.append(user['real_name'])
    user_list_real_names.sort()
# print(user_list)
# print(user_list_real_names)

# Save the user_list to a text file in reports folder.
# Use current date_time to second to set a unique filename.
now = datetime.now()
now = now.strftime("%Y-%m-%d-%H-%M-%S")
report_file = 'reports//' + now + '.txt'
print('...Creating a new file for report capture.')
with open(report_file, 'w', encoding='utf-8') as working_file:
    working_file.write(f"REPORT CREATED:\n\t{now}")
    working_file.write(f"\n\nTOTAL USERS:\n\t{len(user_list)}")
    working_file.write(f"\n\nLIST OF ALL USERS:\n")
    for user in user_list:
        working_file.write(f"\t{user}\n")
print('...User list added to report.')

# Create a dictionary to hold users. Pulling from the previously created
# list just keeps everything organized the same way.
comment_data = {}
for user in user_list_real_names:
    comment_data[user] = {
        'Real Name': user,
        'total comments': 0,
        'comments':[],
    }
# print(comment_data)
print("...Comment Data dictionary created.")

# Open json file and prepare student_comments, a list that ignores general
# messages like entering the chat, etc. and only contains comments actually 
# made by users.
student_comments = []
with open(file_path, encoding='utf-8', errors='ignore') as comment_file:
    full_comment_data = json.load(comment_file)
for comment in full_comment_data:
    if 'client_msg_id' in comment.keys():
        student_comments.append(comment)

# Use a for loop to run through each comment in student_comments and append the
# comment text to the appropriate entry in the comment_data dictionary. Increase
# the 'total comments' counter by 1 each time a comment is added.
for comment in student_comments:
    student_name = comment['user_profile']['real_name']
    # print(student_name)
    comment_text = comment['text']
    # print(comment_text)
    comment_data[student_name]['comments'].append(comment_text)
    comment_data[student_name]['total comments'] += 1
# print(comment_data)
print("...Comments tabulated and added to dictionary.")

# Reprint Student Name and Comment Total, but with a numbered list of comments
# after it.
with open(report_file, 'a', encoding='utf-8', errors='ignore') as working_file:
    working_file.write('\nUSER COMMENT COUNTS:')
    for user in comment_data.keys():
        working_file.write(
            f"\n\t{user}\t{comment_data[user]['total comments']} comments")
    working_file.write('\n\nFULL USER COMMENT BREAKDOWN:')
    for user in comment_data.keys():
        comment_text_counter = 1
        working_file.write(
            f"\n\n{user.upper()}:\t{comment_data[user]['total comments']} COMMENTS:")
        for comment in comment_data[user]['comments']:
            formatted_comment = f"\n\t{comment_text_counter}. {comment}"
            working_file.write(formatted_comment)
            comment_text_counter += 1
print("...Comment Data added to report.")
print('All reports have been created. Please check the reports folder!')