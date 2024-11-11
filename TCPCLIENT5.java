import java.io.*;
import java.net.*;
class TCPClient1{
 public static void main(String[] args) {
 try {
 // Connect to the server on localhost and port 9999
 Socket s = new Socket("localhost", 9999);
 System.out.println("Connected to server.");
 // Create output stream to send data to the server
 DataOutputStream dout = new DataOutputStream(s.getOutputStream());
 // Send a message to the server
 dout.writeUTF("Hi from the client!");
 dout.flush();
 // Close connection
 dout.close();
 s.close();
 } catch (IOException e) {
 e.printStackTrace();
 }
 }
}