# from argparse import ArgumentParser

# from baked.supersix.webapi import SupersixApi
from datetime import datetime, timedelta
from time import sleep


def main():
    start = datetime.now()
    while datetime.now() - timedelta(minutes=10) < start:
        # with open(f"logs/test-runner-{start.strftime('%Y%m%d%H%M%S')}.log", "w") as fh:
        print(f"The time is {str(datetime.now())}")
        sleep(30)


if __name__ == "__main__":
#     parser = ArgumentParser(description="Supersix Web API.")
#     parser.add_argument("--host", type=str, help="Host")
#     parser.add_argument("--port", type=int, default=80, help="Port number")
#     args = parser.parse_args()

#     SupersixApi.run(standalone=True, host=args.host, port=args.port)
    main()
