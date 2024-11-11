import java.io.*;
import java.net.*;

public class FileServer {
    public static void main(String[] args) {
        try {
            // Create a server socket on port 9876
            ServerSocket serverSocket = new ServerSocket(9876);
            System.out.println("Waiting for file...");

            // Accept the incoming client connection
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected!");

            // Create input and output streams to communicate with the client
            InputStream inputStream = clientSocket.getInputStream();
            FileOutputStream fileOutputStream = new FileOutputStream("received_file.txt");

            // Read the file data from the client and save it
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                fileOutputStream.write(buffer, 0, bytesRead);
            }

            System.out.println("File received and saved as 'received_file.txt'");

            // Close the streams and the socket
            fileOutputStream.close();
            inputStream.close();
            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
