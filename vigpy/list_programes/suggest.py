users=["mohanlal","mamooty","dq","nivin","srk","tovino","unny","prithvi","dq"]
dileep_friends=["mohanlal","nivin","unny"]

#list suggestions of dileep

for u in users:
    if u not in dileep_friends:
        print(u)

