//UDP CLIENT
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <arpa/inet.h> 
 
#define PORT 8080 
#define BUFFER_SIZE 1024 
 
void send_file(FILE *fp, int sockfd, struct sockaddr_in server_addr) { 
char data[BUFFER_SIZE] = {0}; 
char ack[BUFFER_SIZE] = {0}; 
socklen_t addr_len = sizeof(server_addr); 
ssize_t n; 
 
while (fgets(data, BUFFER_SIZE, fp) != NULL) { 

if (sendto(sockfd, data, strlen(data), 0, (struct sockaddr*)&server_addr, addr_len) == -1) { 
perror("Error sending file data"); 
exit(1); 
} 
 

n = recvfrom(sockfd, ack, BUFFER_SIZE, 0, (struct sockaddr*)&server_addr, &addr_len); 
if (n <= 0) { 
perror("Error receiving acknowledgment"); 
exit(1); 
} 
 
bzero(data, BUFFER_SIZE); 
bzero(ack, BUFFER_SIZE); 
} 
 

sendto(sockfd, "EOF", 3, 0, (struct sockaddr*)&server_addr, addr_len); 
printf("File sent successfully.\n"); 
} 
 
int main() { 
int sockfd; 
struct sockaddr_in server_addr; 
FILE *fp; 
char *filename = "file_to_send.txt"; 
 

if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) { 
perror("Socket creation failed"); 
exit(EXIT_FAILURE); 
} 
 
 
memset(&server_addr, 0, sizeof(server_addr)); 
server_addr.sin_family = AF_INET; 
server_addr.sin_port = htons(PORT); 
server_addr.sin_addr.s_addr = INADDR_ANY; 
 
fp = fopen(filename, "r"); 
if (fp == NULL) { 
perror("File open error"); 
exit(1); 
} 
 

send_file(fp, sockfd, server_addr); 
 

fclose(fp); 
close(sockfd); 
 
return 0; 
}

//UDP SERVER

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <arpa/inet.h> 
 
#define PORT 8080 
#define BUFFER_SIZE 1024 
 
void receive_file(int sockfd, struct sockaddr_in client_addr) { 
char buffer[BUFFER_SIZE] = {0}; 
char *ack = "ACK"; 
FILE *fp; 
socklen_t addr_len = sizeof(client_addr); 
ssize_t n; 
char *filename = "received_file"; 
 
fp = fopen(filename, "wb"); 
if (fp == NULL) { 
perror("File open error"); 
exit(1); 
} 
 
while (1) { 
if (n <= 0) { 
break; 
} 
 
if (strcmp(buffer, "EOF") == 0) { 
printf("File transfer complete.\n"); 
break; 
} 
 
fwrite(buffer, sizeof(char), n, fp); 
bzero(buffer, BUFFER_SIZE); 
 
sendto(sockfd, ack
, strlen(ack), 0, (struct sockaddr*)&client_addr, addr_len); 
} 
 
fclose(fp); 
} 
 
int main() { 
int sockfd; 
struct sockaddr_in server_addr, client_addr; 
 if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) { 
perror("Socket creation failed"); 
exit(EXIT_FAILURE); 
} 
 
memset(&server_addr, 0, sizeof(server_addr)); 
server_addr.sin_family = AF_INET; 
server_addr.sin_addr.s_addr = INADDR_ANY; 
server_addr.sin_port = htons(PORT); 
 
if (bind(sockfd, (const struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) { 
perror("Bind failed"); 
close(sockfd); 
exit(EXIT_FAILURE); 
} 
 
printf("Server is waiting for file...\n"); 
receive_file(sockfd, client_addr); 
close(sockfd); 
 
return 0; 
}