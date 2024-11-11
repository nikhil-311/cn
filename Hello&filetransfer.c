#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <arpa/inet.h> 
 
#define PORT 8080 
#define BUFFER_SIZE 1024 
 
void send_file(FILE *fp, int sockfd) { 
char data[BUFFER_SIZE] = {0}; 
 
while (fgets(data, BUFFER_SIZE, fp) != NULL) { 
if (send(sockfd, data, sizeof(data), 0) == -1) { 
perror("Error sending file"); 
exit(1); 
} 
bzero(data, BUFFER_SIZE); 
} 
} 
 
int main() { 
int sock = 0; 
struct sockaddr_in serv_addr; 
char buffer[BUFFER_SIZE] = {0}; 
char *hello = "Hello from client"; 
FILE *fp; 
char *filename = "file_to_send.txt"; 
 

if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) { 
printf("\nSocket creation error\n"); 
return -1; 
} 
 

serv_addr.sin_family = AF_INET; 
serv_addr.sin_port = htons(PORT); 
 
if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) { 
printf("\nInvalid address or Address not supported\n"); 
return -1; 
} 
 

if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) { 
printf("\nConnection Failed\n"); 
return -1; 
} 
 

send(sock, hello, strlen(hello), 0); 
printf("Hello message sent to server\n"); 
 

read(sock, buffer, BUFFER_SIZE); 
printf("Message from server: %s\n", buffer); 
 

fp = fopen(filename, "r"); 
if (fp == NULL) { 
perror("File open error"); 
exit(1); 
} 
 
send_file(fp, sock); 
printf("File '%s' sent to server\n", filename); 
 
fclose(fp); 
close(sock); 
 
return 0; 
} 

//file transfer


#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <unistd.h> 
#include <arpa/inet.h> 
 
#define PORT 8080 
#define BUFFER_SIZE 1024 
 
void send_file(FILE *fp, int sockfd) { 
char data[BUFFER_SIZE] = {0}; 
 
while (fgets(data, BUFFER_SIZE, fp) != NULL) { 
if (send(sockfd, data, sizeof(data), 0) == -1) { 
perror("Error sending file"); 
exit(1); 
} 
bzero(data, BUFFER_SIZE); 
} 
} 
 
int main() { 
int server_fd, new_socket; 
struct sockaddr_in address; 
int addrlen = sizeof(address); 
char buffer[BUFFER_SIZE] = {0}; 
char *hello = "Hello from server"; 
FILE *fp; 
char *filename = "received_file.txt"; 

if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) { 
perror("Socket failed"); 
exit(EXIT_FAILURE); 
} 
 

address.sin_family = AF_INET; 
address.sin_addr.s_addr = INADDR_ANY; 
address.sin_port = htons(PORT); 
 

if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) { 
perror("Bind failed"); 
close(server_fd); 
exit(EXIT_FAILURE); 
} 
 

if (listen(server_fd, 3) < 0) { 
perror("Listen failed"); 
close(server_fd); 
exit(EXIT_FAILURE); 
} 
 
printf("Server is listening on port %d\n", PORT); 
 

if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) { 
perror("Accept failed"); 
close(server_fd); 
exit(EXIT_FAILURE); 
} 
 

read(new_socket, buffer, BUFFER_SIZE); 
printf("Message from client: %s\n", buffer); 
 
send(new_socket, hello, strlen(hello), 0); 
printf("Hello message sent to client\n"); 
 

fp = fopen(filename, "w"); 
if (fp == NULL) { 
perror("File open error"); 
exit(1); 
} 
 
while (1) { 
ssize_t n = recv(new_socket, buffer, BUFFER_SIZE, 0); 
if (n <= 0) { 
break; 
} 
fprintf(fp, "%s", buffer); 
bzero(buffer, BUFFER_SIZE); 
} 
printf("File received and saved as '%s'\n", filename); 
 
fclose(fp); 
close(new_socket); 
close(server_fd); 
return 0; 
} 