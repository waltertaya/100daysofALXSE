import bcrypt

password = b'super unique secret password'

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# print(f'password: {password}, hashed: {hashed}')


if bcrypt.checkpw(password, hashed):
    print('Logged in successfully')

else:
    print('Invalid password')
