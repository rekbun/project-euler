public class Problem15 {

	private static long com(long n,long d ) {
		long i=1;
		long cnt=1;
		while(i<=d) {
			cnt=cnt*n/i;
			n--;
			i++;
		}
		return cnt;
	}

	public static long latticePath(int n) {
		return com(2*n,n);

	}
	
	public static void main(String[] args) {
		System.out.println(latticePath(20));
	}


}
