from datetime import datetime, timedelta
from time import sleep


def main():
    start = datetime.now()
    while datetime.now() - timedelta(minutes=10) < start:
        # with open(f"logs/test-runner-{start.strftime('%Y%m%d%H%M%S')}.log", "w") as fh:
        print(f"The time is {str(datetime.now())}")
        sleep(30)


if __name__ == "__main__":
    main()
