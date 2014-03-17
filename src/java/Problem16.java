public class Problem16 {
	
	private static String mul(String s,int n) {
		String res="";
		int c=0;
		for(int i=0;i<s.length();i++) {
			int sum=((s.charAt(s.length()-i-1)-'0')*n)+c;
			res=(sum%10)+res;
			c=sum/10;
			
		}
		if(c>0) {
			res=c+res;
		}	
		return res;

	}

	public static String pow(int n,int m) {
		String s="1";
		while(m-->0) {
			s=mul(s,n);
		}
		return s;
	}
	public static int sum(String s) {
		int res=0;
		for(int i=0;i<s.length();i++) {
			res+=(s.charAt(i)-'0');
		}
		return res;
	}

	public static void main(String[] args) {
		System.out.println(sum(pow(2,1000)));
	}

}
