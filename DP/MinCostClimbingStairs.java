import java.util.*;

public class MinCostClimbingStairs {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String[] strArr = s.nextLine().split(" ");
        int[] arr = new int[strArr.length];
        int count = 0;
        for(String eachVal: strArr)
            arr[count++] = Integer.parseInt(eachVal);
        System.out.println(Arrays.toString(arr) + arr.getClass());
        s.close();
    }
}
