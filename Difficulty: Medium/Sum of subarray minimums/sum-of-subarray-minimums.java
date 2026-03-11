import java.util.*;

class Solution {

    /*
    Core Idea (Compressed Modeling + Invariants)

    For each element arr[i], compute how many subarrays use it as the minimum.

    Contribution formula:
        contribution(i) = arr[i] * L * R

    where
        L = i - prevSmaller[i]
        R = nextSmallerEq[i] - i

    Definitions:
        prevSmaller[i]   = nearest index left of i with value < arr[i]
        nextSmallerEq[i] = nearest index right of i with value <= arr[i]

    Total answer:
        sum += arr[i] * L * R

    Invariants:
        • Use monotonic increasing stack
        • Stack maintains indices where:
              arr[stack[0]] <= arr[stack[1]] <= ...
        • Tie breaking to avoid duplicate counting:
              Left  → strictly smaller (<)
              Right → smaller or equal (<=)

    This ensures each subarray minimum is counted exactly once.

    Complexity:
        Time  : O(n)
        Space : O(n)
    */

    public int sumSubMins(int[] arr) {

        int n = arr.length;

        int[] prev = new int[n];
        int[] next = new int[n];

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {                               // Step 1: Previous Smaller Element
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i])
                stack.pop();

            prev[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        stack.clear();

        for (int i = n - 1; i >= 0; i--) {                          // Step 2: Next Smaller or Equal Element
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i])
                stack.pop();

            next[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long sum = 0;
        for (int i = 0; i < n; i++) {                               // Step 3: Compute contribution

            long left = i - prev[i];
            long right = next[i] - i;

            sum += (long) arr[i] * left * right;
        }

        return (int) sum;
    }
}