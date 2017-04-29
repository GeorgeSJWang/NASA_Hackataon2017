package com.example.gw.hello_word;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.lang.Thread;
import android.widget.Toast;
import android.app.Activity;
import android.os.Bundle;

public class Client_Socket extends Activity {

    private String myLocation;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Bundle b = getIntent().getExtras();
        final double latitude  = b.getDouble("latitude");
        final double longitude = b.getDouble("longitude");



        new Thread() {
            public void run() {


                InetAddress serverAddr = null;
                SocketAddress sc_add   = null;
                Socket socket          = null;

                try {
                    serverAddr = InetAddress.getByName("140.112.30.37");
                    sc_add = new InetSocketAddress(serverAddr, 8865);

                    socket = new Socket();
                    socket.connect(sc_add, 2000);

                    // send data
                    DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                    myLocation = new String();
                    myLocation = "114.36.129.178,"+String.valueOf(latitude)+","+String.valueOf(longitude);

                    out.writeUTF(myLocation);

                    socket.close();

                } catch (UnknownHostException e) {
                    Toast.makeText(Client_Socket.this, "Unknown Host", Toast.LENGTH_LONG).show();
                } catch (SocketException e) {
                    Toast.makeText(Client_Socket.this, "Socket Host", Toast.LENGTH_LONG).show();
                } catch (IOException e) {
                    Toast.makeText(Client_Socket.this, "IO Exception", Toast.LENGTH_LONG).show();
                }
            }
        }.start();
    }
}