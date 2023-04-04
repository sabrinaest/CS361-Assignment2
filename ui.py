import time

while True:
    user_input = input("Please enter 1 to meet your new Animal Crossing neighbor! Enter 2 if you wish to exit: ")
    if user_input == '1':
        with open('prng-service.txt', 'w') as prng_file:
            prng_file.write('run')

        time.sleep(5)

        with open('prng-service.txt', 'r') as prng_file:
            random_num = prng_file.readline()

        with open('image-service.txt', 'w') as img_service_file:
            img_service_file.seek(0)
            img_service_file.truncate()
            img_service_file.write(random_num)
        print('.')
        print('.')
        print('.')
        print('Looks like they are preparing a house warming basket! :)')
        time.sleep(5)

        with open('image-service.txt', 'r') as img_service_file:
            img_path = img_service_file.readline()
            print('.')
            print('.')
            print('.')
            print('They are very excited to meet you!')
            time.sleep(5)
            print('.')
            print('.')
            print('.')
            print('Meet your new neighbor:', img_path)

    elif user_input == '2':
        print('Goodbye!')
        break
    else:
        print("unknown option")