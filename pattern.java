package while_loop;

public class pattern {

	public static void main(String[] args) {
		int n = 4;
		int i = 1;
		
		while(i<=n) {
			int j = 1;
			while (j<=i) {
				System.out.print(j);
				j = j+1;
			}
			System.out.println();
			i = i+1;
			
		}

	}

}
