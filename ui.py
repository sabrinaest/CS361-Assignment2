import time

while True:
    user_input = input("Please enter 1 to generate an image. Enter 2 if you wish to exit: ")
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

        time.sleep(5)

        with open('image-service.txt', 'r') as img_service_file:
            img_path = img_service_file.readline()
            print('Here is your image:', img_path)

    elif user_input == '2':
        break
    else:
        print("unknown option")