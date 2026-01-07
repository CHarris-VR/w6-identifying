#Week 4: Loops and Iterations
# Goal: Identify internal vs external IP addresses

ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]


index = 0
Internal = 0
External = 0

while index <len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        print(f"{ip} is internal.")
        Internal += 1
    else:
        print(f"{ip} is external.")
        External += 1

    index += 1
print(f"Internal Count: {Internal}")
print(f"External Count: {External}")