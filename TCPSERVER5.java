import java.io.*;
import java.net.*;
class TCPServer1{
 public static void main(String[] args) {
 try {
 // Create a server socket on port 9999
 ServerSocket ss = new ServerSocket(9999);
 System.out.println("Server is waiting for a connection...");
 // Accept the incoming client connection
 Socket s = ss.accept();
 System.out.println("Client connected!");
 // Create input stream to read data from the client
 DataInputStream dis = new DataInputStream(s.getInputStream());
 // Read the message from the client
 String str = dis.readUTF();
 System.out.println("Client says: " + str);
 // Close connections
 dis.close();
 s.close();
 ss.close();
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}
