# i =1

# while i<=5:
#     print('*'* i)
#     i+=1

# print("Done")


# secret_number=9
# guess_count=0
# guess_limit=3

# while guess_count< guess_limit:
#     guess= int(input('Guess:'))
#     guess_count +=1
#     if(guess == secret_number):
#         print('You won!')
#         break
# else:
#     print('You Lost!')

##Remember we can use three quotations for multi line print statements

is_car_started =False
is_car_stopped=False

while True:
    user_input = input('>').lower()
    if user_input == 'help':
        print('''
'start-to start the car'       
'stop-to-stop-the-car'
'quit-to-exit'
        ''')
    elif user_input =='start':
        if not is_car_started:
            is_car_started=True
            print('car started...ready to go')
        else:
            print('Car already started')
    elif user_input =='stop':
        if not is_car_stopped:
            is_car_stopped=True
            print('car stopped')
        else:
            print('Car already stopped')
    elif user_input =='quit':
        break
    else:
        print("Heey..i don't understand that")
        


