#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

#define PORT 9090
#define MAXLINE 1024

void send_file(int sockfd, const char *filename) {
    char buffer[MAXLINE];
    FILE *fp;
    size_t n;

    fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("File opening failed");
        return;
    }

    while ((n = fread(buffer, sizeof(char), MAXLINE, fp)) > 0) {
        send(sockfd, buffer, n, 0);
    }

    printf("File sent successfully.\n");
    fclose(fp);
}

int main() {
    int sockfd, n;
    char buffer[MAXLINE];
    struct sockaddr_in servaddr;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Socket creation failed");
        exit(1);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, "127.0.0.1", &servaddr.sin_addr) <= 0) {
        perror("Invalid address or Address not supported");
        exit(1);
    }

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Connection failed");
        close(sockfd);
        exit(1);
    }

    printf("Connected to the server.\n");

    // Continuous messaging loop
    while (1) {
        printf("Client: ");
        fgets(buffer, MAXLINE, stdin);

        if (strncmp(buffer, "FILE_TRANSFER", 13) == 0) {
            // Signal the server for file transfer
            send(sockfd, "FILE_TRANSFER", 13, 0);

            printf("Enter file: ");  // Prompt for file name
            fgets(buffer, MAXLINE, stdin);
            buffer[strcspn(buffer, "\n")] = '\0'; // Remove the newline character

            // Send the file
            send_file(sockfd, buffer);
        } else {
            send(sockfd, buffer, strlen(buffer), 0);

            memset(buffer, 0, MAXLINE);
            n = recv(sockfd, buffer, MAXLINE, 0);
            if (n <= 0) {
                printf("Server disconnected.\n");
                break;
            }
            buffer[n] = '\0';
            printf("Server: %s\n", buffer);
        }
    }

    close(sockfd);
    return 0;
}
