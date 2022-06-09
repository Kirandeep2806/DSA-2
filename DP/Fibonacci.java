import java.util.*;

class Fibonacci {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n+1];
        for(int i=0; i<n+1; i++) {
            if(i == 0)
                arr[0] = 0;
            else if(i == 1)
                arr[1] = 1;
            else
                arr[i] = arr[i-1] + arr[i-2];
        }
        System.out.println(arr[n]);
        s.close();
    }
}
