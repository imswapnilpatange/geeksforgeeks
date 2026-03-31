class Solution {
    public int maxProfit(int[] arr, int k) {
        int noStock = 0;
        int inHand = -arr[0];

        for (int i = 1; i < arr.length; i++) {
            int temp = noStock;

            noStock = Math.max(noStock, inHand + arr[i] - k);
            inHand = Math.max(inHand, temp - arr[i]);
        }

        return noStock;
    }
}