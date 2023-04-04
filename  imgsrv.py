import time
import os

cs361_img_folder = r'C:\Users\Sabrina\PycharmProjects\CS361-Assignment2\animal_crossing'

while True:
    time.sleep(1)
    with open('image-service.txt', 'r+') as img_service_file:
        read_img_file = img_service_file.readline()
        if read_img_file.isnumeric():
            img_file_num = int(read_img_file)
            img_file_num = img_file_num % len(os.listdir(cs361_img_folder))
            img_service_file.seek(0)
            img_service_file.truncate()
            img_service_file.write(f'C:\\Users\\Sabrina\\PycharmProjects\\CS361-Assignment2\\animal_crossing{img_file_num}.jpg')