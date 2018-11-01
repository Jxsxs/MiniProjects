import java.util.*;
import java.io.*;
public class Mandados{
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try{
			int cuantos = Integer.parseInt(br.readLine());
			String nombres[] = {"luis","jorge","carlos", "artemio","vicente", "jesus","tobola","eric"};
			for (int x = 0;x<cuantos ; x++) {
				int perd = new Random().nextInt(nombres.length);
				String quien = nombres[perd];
				String tmp = "";
				if (!quien.equals(tmp)) {
					System.out.println("Pierde: " + quien);	
					tmp = quien;
				}
				else{
					x-=1;	
				}
				
			}
			
		}catch(IOException e){
			System.out.println("Error: " + e.getMessage());
		}
	}
}
