import java.lang.*;
import java.io.*;
import java.net.*;


public class Client
{
   private Socket socket = null;
   private BufferedReader reader = null;
   private BufferedWriter writer = null;

   public Client(InetAddress address, int port) throws IOException
   {
      socket = new Socket(address, port);
      reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
      writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
   }

   public void send(String msg) throws IOException
   {
      writer.write(msg, 0, msg.length());
      writer.flush();
   }

   public String recv() throws IOException
   {
      return reader.readLine();
   }

   public static void main(String[] args)
   {
      try {
         InetAddress host = InetAddress.getByName("172.16.126.25");
         Client client = new Client(host, 9090);

         client.send(args[0]);
         String response = client.recv();
         System.out.println("Client received: " + response);
      }
      catch (IOException e) {
         System.out.println("Caught Exception: " + e.toString());
      }
   }
}