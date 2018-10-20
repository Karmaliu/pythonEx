from sys import argv

script, user_name = argv
prompt  = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a fow questions,")
print(f"Do yout like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)


# """ 放入多行文本
print(f"""
  Alright, so you said {likes} about liking me.
  you live in {lives}. Not sure where that is.
  And you have a {computer} computer. Nice.
""")

