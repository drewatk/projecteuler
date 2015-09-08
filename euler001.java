import java.util.ArrayList;

public class Euler1 {
	
	final int under = 1000;
	
	static ArrayList<Integer> multiplesUnder(int multiple, int under) {
		
		under--;
		int nMultiples = (under - (under % multiple)) / multiple;
		ArrayList<Integer> l = new ArrayList<Integer>(nMultiples);
		
		for (int i = 0; i < nMultiples; i++) {
			l.add((i + 1) * multiple);
		}
		return l;
		
	}
	
	static int sumArray(ArrayList<Integer> array) {
		int sum = 0;
		for (Integer i : array) {
			sum += i;
		}
		return sum;
	}
	
	static ArrayList<Integer> removeDupes(ArrayList<Integer> l1, ArrayList<Integer> l2) {
		
		l1.removeAll(l2);
		
		l1.addAll(l2);
		return l1;
	}
	
	public static void main (String [] args) {
		ArrayList<Integer> multiples1 = multiplesUnder(Integer.parseInt(args[0]), Integer.parseInt(args[2]));
		ArrayList<Integer> multiples2 = multiplesUnder(Integer.parseInt(args[1]), Integer.parseInt(args[2]));
		
		ArrayList<Integer> multiples = removeDupes(multiples1, multiples2);
		
		int sum = sumArray(multiples);
		
		System.out.println(sum);
	}
}