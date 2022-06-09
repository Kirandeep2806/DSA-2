import java.util.*;

public class MinCostClimbingStairs {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String[] strArr = s.nextLine().split(" ");
        Integer[] arr1 = new Integer[strArr.length];
        int count = 0;
        for(String str: strArr)
            arr1[count++] = Integer.parseInt(str);
        s.close();
    }
}
