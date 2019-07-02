import multiprocessing as mp
from processone import ProcessOne
from processtwo import ProcessTwo


def main():
    process_one_queue = mp.Queue()
    process_two_queue = mp.Queue()

    process_one = mp.Process(target=ProcessOne, args=(process_one_queue, process_two_queue, ))
    process_two = mp.Process(target=ProcessTwo, args=(process_two_queue, process_one_queue, ))

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()


if __name__ == "__main__":
    main()
