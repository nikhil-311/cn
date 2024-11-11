import java.net.DatagramPacket;
import java.net.DatagramSocket;
public class SimpleUDPServer {
 public static void main(String[] args) {
 try {
 // Create a socket to listen on port 9999
 DatagramSocket serverSocket = new DatagramSocket(9999);
 byte[] buffer = new byte[1024];
 System.out.println("Server is running. Waiting for client message...");
 // Prepare a packet to receive data
 DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
 serverSocket.receive(packet); // Wait for message from client
 // Convert received data to a string and display
 String receivedMessage = new String(packet.getData(), 0, packet.getLength());
 System.out.println("Message from client: " + receivedMessage);
 // Close the socket
 serverSocket.close();
 } catch (Exception e) {
 System.out.println("An error occurred: " + e.getMessage());
 }
 }
}