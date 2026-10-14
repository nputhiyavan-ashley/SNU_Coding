
password = input()

score = 0

if len(password) >= 8:
    score += 1
else:
    failed.append("
if any(ch.isupper() for ch in password):
    score += 1
else:
    failed.append("uppercase")
m
if any(ch.islower() for ch in password):
    score += 1
else:
    failed.append("lowercase")
if any(ch.isdigit() for ch in password):
    score += 1
else:
    failed.append("digit")

special = "!@#$%^&*()_+-=[]{};:'\",.<>?/|`~"

if any(ch in special for ch in password):
    score += 1
else:
    failed.append("special")

if " " not in password:
    score += 1
else:
    failed.append("space")

if score == 6:
    print("VALID score:6")
else:
    print("INVALID:" + ",".join(failed) + " score:" + str(score))
