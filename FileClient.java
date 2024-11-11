import java.io.*;
import java.net.*;
public class FileClient {
 public static void main(String[] args) {
 try {
 Socket socket = new Socket("localhost", 9876);
 FileInputStream fileInputStream = new FileInputStream("received_file.txt");
 OutputStream outputStream = socket.getOutputStream();

 byte[] buffer = new byte[1024];
 int bytesRead;
 while ((bytesRead = fileInputStream.read(buffer)) != -1) {
 outputStream.write(buffer, 0, bytesRead);
 }
 System.out.println("File sent successfully!");
 // Close the streams and the socket
 fileInputStream.close();
 outputStream.close();
 socket.close();
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}