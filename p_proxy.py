import os, sys, time, requests, argparse

parser = argparse.ArgumentParser(description="Simple checker proxy =)")
parser.add_argument("--file", type=str, required=True, help="File to check proxy")
parser.add_argument("--out", type=str, required=True, help="Output to valids proxy")
args = parser.parse_args()


r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
d = "\033[0m"
b = "\033[30m"

proxy_list = args.file
output_list = args.out

def chek_valid():
    time.sleep(0.9)
    print(f"[{y}+{d}] Welcome to {g}Piece of proxy{d}!")
    time.sleep(0.5)
    print(f"[{y}+{d}] Check connection to proxy ...")

    with open(proxy_list, 'r') as f:
        for i in f:
            address = i.strip()
            try:
                response = requests.get("http://httpbin.org/ip", proxies={"http": address, "https": address}, timeout=10)
                if response.status_code == 200:
                    print(f"[{g}+{d}] {address}")
                    with open(output_list, 'a') as f:
                        f.write(f"{address}\n")
                else:
                    continue
            except requests.exceptions.RequestException as e:
                print(f"{r}{address}{d}")
            except KeyboardInterrupt:
                sys.exit(0)
chek_valid()
