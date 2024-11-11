#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

// 9090
// 5000
// 8888
// 6000

#define PORT 8080
#define MAXLINE 1024

int main() {
    int sockfd, n;
    char buffer[MAXLINE];
    struct sockaddr_in servaddr;

    // Step 1: Create a TCP socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Socket creation failed");
        exit(1);
    }

    // Step 2: Set up the server address structure
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);

    // Step 3: Convert the server IP address to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr) <= 0) {
        perror("Invalid address or Address not supported");
        exit(1);
    }

    // Step 4: Connect to the server
    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Connection failed");
        close(sockfd);
        exit(1);
    }

    printf("Connected to the server.\n");

    // Continuous messaging loop
    while (1) {
        // Step 5: Get message from the user
        printf("Client: ");
        fgets(buffer, MAXLINE, stdin);

        // Send message to the server
        send(sockfd, buffer, strlen(buffer), 0);

        // Clear the buffer and receive response from the server
        memset(buffer, 0, MAXLINE);
        n = recv(sockfd, buffer, MAXLINE, 0);
        if (n <= 0) {
            printf("Server disconnected.\n");
            break;
        }
        buffer[n] = '\0';
        printf("Server: %s\n", buffer);
    }

    // Step 6: Close the socket
    close(sockfd);

    return 0;
}
