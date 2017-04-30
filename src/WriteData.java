import java.io.PrintWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;


public class WriteData {

	private PrintWriter writer;

	// constructor
	public WriteData() {
		try{
	    	this.writer = new PrintWriter(new FileOutputStream(new File("userData.csv"), true)); 
		}catch (IOException e) {
			System.out.println("ERROR");
		}
	}

	protected void outputToFile(String user_data) {
		this.writer.println(user_data);
		this.writer.flush();
	}


}