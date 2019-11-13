import itertools

from src.Gmail import Gmail

# enter email id
email = 'EMAIL'
# enter email password
password = 'PASSWORD'
mailer_service = Gmail(email, password)
email_lists = mailer_service.read_mails()
print(email_lists)
merge_all_list = list(itertools.chain.from_iterable(email_lists))

# remove duplicate entries
final_email_lists = list(dict.fromkeys(merge_all_list))

f = open("email_ids.txt", "a+")
for email in final_email_lists:
    f.write(email + "\n")
f.close()