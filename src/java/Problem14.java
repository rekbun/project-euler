public class Problem14 {


	public static long get(long inp,long[] dp) {
		if(inp<=1) {
			dp[(int)inp]=0;
			return 1;
		}	
		if(inp<2000000 && dp[(int)inp]>0) {
			return dp[(int)inp];
		}
		if(inp%2==0) {
			inp=inp/2;
		}else {
			inp=3*inp+1;
		}
		long  va= 1+get(inp,dp);
		if(inp<2000000) {
			dp[(int)inp]=va;
		}
		return va;
	}	


	public static void main(String[] args) {
		long max=0;
		int ret=0;
		long [] dp=new long[2000000];
		for(int i=2000000-1;i>0;i--) {
			 long c=get(i,dp);
			
			if(c>max) {
				max=c;
				ret=i;
			}
		}
		System.out.println(ret+" " + max);
	}



}
