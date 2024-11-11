import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
public class SimpleUDPClient {
 public static void main(String[] args) {
 try {
 // Create a socket for sending data
 DatagramSocket clientSocket = new DatagramSocket();
 InetAddress serverAddress = InetAddress.getByName("localhost");
 // Message to send to server
 String message = "Hello from UDP Client";
 byte[] buffer = message.getBytes();
 // Prepare a packet with the message, server address, and port
 DatagramPacket packet = new DatagramPacket(buffer, buffer.length, serverAddress,
9999);
 clientSocket.send(packet); // Send the packet to the server
 System.out.println("Message sent to server: " + message);
 // Close the socket
 clientSocket.close();
 } catch (Exception e) {
 System.out.println("An error occurred: " + e.getMessage());
 }
 }
}