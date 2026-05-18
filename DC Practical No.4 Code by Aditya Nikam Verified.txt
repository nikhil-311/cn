import time

# List of Servers
servers = {
    "Server-1": 0,
    "Server-2": 0,
    "Server-3": 0
}

# ---------------- ROUND ROBIN ----------------
def round_robin(requests):

    server_names = list(servers.keys())

    print("\nUsing Round Robin Algorithm\n")

    for i in range(requests):

        # Select server one by one
        server = server_names[i % len(server_names)]

        # Increase active requests
        servers[server] += 1

        print(f"[{server}] Handling request {i+1} | Active: {servers[server]}")

        time.sleep(0.5)

        # Complete request
        servers[server] -= 1

        print(f"[{server}] Completed request {i+1} | Active: {servers[server]}")

        time.sleep(0.5)

    print("\nAll requests processed.")


# ---------------- LEAST CONNECTION ----------------
def least_connection(requests):

    print("\nUsing Least Connection Algorithm\n")

    for i in range(requests):

        # Find server with least active connections
        server = min(servers, key=servers.get)

        # Increase active connections
        servers[server] += 1

        print(f"[{server}] Handling request {i+1} | Active: {servers[server]}")

        time.sleep(0.5)

        # Complete request
        servers[server] -= 1

        print(f"[{server}] Completed request {i+1} | Active: {servers[server]}")

        time.sleep(0.5)

    print("\nAll requests processed.")


# ---------------- MAIN PROGRAM ----------------

print("Choose Load Balancing Algorithm")
print("1. Round Robin")
print("2. Least Connection")

choice = input("Enter your choice: ")

requests = int(input("Enter number of requests: "))

# User Choice
if choice == "1":
    round_robin(requests)

elif choice == "2":
    least_connection(requests)

else:
    print("Invalid Choice!")