import java.util.Arrays;
import java.util.Stack;

public class PossibleEqualMaximumSum {

    public static int sum(Stack<Integer> stack) {
        if (stack.isEmpty()) {
            return 0;
        }
        int top = stack.pop();
        int prev = sum(stack);
        stack.push(top);
        return prev + top;
    }

    public static void main(String[] args) {
        Stack<Integer> stack[] = new Stack[3];
        for (int i = 0; i < stack.length; i++) {
            stack[i] = new Stack<>();
        }

        int stack1[] = { 4, 1, 3, 5, 7, 1 };
        int stack2[] = { 1, 8, 2, 2, 4, 0 };
        int stack3[] = { 1, 2, 3, 5, 0, 0 };
        for (int i = stack1.length - 1; i >= 0; i--) {
            stack[0].push(stack1[i]);
            stack[1].push(stack2[i]);
            stack[2].push(stack3[i]);
        }
        System.out.println(Arrays.toString(stack));
        int sum[] = new int[stack.length];

        while (!stack[0].isEmpty() && !stack[1].isEmpty() && !stack[2].isEmpty()) {
            for (int i = 0; i < 3; i++) {
                sum[i] = sum(stack[i]);
            }
            if (sum[0] == sum[1] && sum[1] == sum[2]) {
                System.out.println("The maximum possible sum is : " + sum[0]);
                break;
            }
            int max = Math.max(Math.max(sum[0], sum[1]), sum[2]);

            for (int i = 0; i < sum.length; i++) {
                if (max == sum[i]) {
                    sum[i] = stack[i].pop();
                    break;
                }
            }
        }

    }
}
