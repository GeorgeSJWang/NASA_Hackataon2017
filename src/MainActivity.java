package com.example.gw.hello_word;

import android.app.Activity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.widget.Toast;
import android.content.Intent;
import android.location.LocationManager;
import android.location.Location;
import android.telephony.TelephonyManager;
import android.content.Context;

public class MainActivity extends Activity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
    //    Intent myIntent = new Intent(MainActivity.this, Client_Socket.class);


        /* Get data from GPS
        try {
            LocationManager lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
            Location location = lm.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            double longitude = location.getLongitude();
            double latitude = location.getLatitude();
        } catch (Exception e) {
            Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_LONG).show();
        }
        */

        String mPhoneNumber;

        /* Get telephone number of itself
        try {
            TelephonyManager tMgr =(TelephonyManager)this.getSystemService(Context.TELEPHONY_SERVICE);
            mPhoneNumber = tMgr.getLine1Number();
        } catch (Exception e) {
            Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_LONG).show();
        }
        */

        mPhoneNumber = "975738316";
        int foo = Integer.parseInt(mPhoneNumber);

        double latitude  = 25.032969;
        double longitude = 121.565418;

        try {
            Intent myIntent = new Intent(MainActivity.this, Client_Socket.class);
            myIntent.putExtra("latitude",  latitude);
            myIntent.putExtra("longitude", longitude);
            myIntent.putExtra("phoneNum",  foo);
            MainActivity.this.startActivity(myIntent);
            Toast.makeText(MainActivity.this, "User location updated!", Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_LONG).show();
        }

        return true;
    }

}