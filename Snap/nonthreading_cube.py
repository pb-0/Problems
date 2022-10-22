import time

def print_cube(s: int) -> int:
    print("volume:", s**3)


def print_square(s: int) -> int:
    print("area:", s**2)


if __name__ == '__main__':
    start = time.time()
    # t1 = threading.Thread(target=print_cube, args=(5))
    # t2 = threading.Thread(target=print_square, args=(5))

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
    print_cube(5)
    print_square(5)

    print(time.time() - start)