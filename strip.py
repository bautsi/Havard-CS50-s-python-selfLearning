introduce = '     Hi my name is bautsi     '
print(introduce)
print(introduce.strip())

email = '     b3r1a3dtw@gmail.com     '
print(email)
new_email = email.strip()
print(new_email.strip('btwaic.'))
# when frontmost & backmost not existed in strip() stop checking and deleting
print(new_email.strip('btwaic.3'))
print(new_email.strip('btwaic.3r'))
print(new_email.strip('btwaic.3r1'))
print(new_email.strip('btwaic.3r1m'))
