<h2><a href="https://www.geeksforgeeks.org/problems/target-sum-1626326450/1">Target Sum 1626326450/1</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of integers arr[] and an integer <strong>target</strong>. We need to build an <strong>expression </strong>out of arr[]<strong> </strong>by adding one of the symbols '<strong>+</strong>' or  '<strong>-</strong>' before each integer in arr[] and then concatenate all the integers. <br/></span><span style="font-size: 18px;">For example<strong> </strong>: if arr[] = [2, 1], you can add a '<strong>+</strong>' before 2 and a '<strong>-</strong>' before 1 and concatenate them to build the expression "+2-1". <br/></span><span style="font-size: 18px;">Return the number of different <strong>expressions</strong> that can be built, which evaluates to <strong>target.</strong></span></p>
<p><span style="font-size: 18px;"><strong>Note : </strong></span><span style="font-size: 14pt;">An expression is considered different from another if the placement of '+' and '-' operators differs, even if the resulting value is the same.<strong> </strong></span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [1, 1, 1, 1, 1], target = 3
<strong>Output: </strong>5<strong>
Explanation: </strong>There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 3], target = 2
<strong>Output: </strong>1<br/></span><span style="font-size: 18px;"><strong>Explanation: </strong>There are 1 way to assign symbols to make the sum of nums be target 2(+1 -2 +3). </span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br/>1 </span><span style="font-size: 18px;">≤ arr.size() </span><span style="font-size: 18px;">≤ 50<br/></span><span style="font-size: 18px;">1 ≤ arr[i] ≤ 20<br/>0 </span><span style="font-size: 18px;">≤ sum(arr) </span><span style="font-size: 18px;">≤ </span>1000<br/><span style="font-size: 18px;">-1000 ≤ </span><span style="font-size: 18px;">target </span><span style="font-size: 18px;">≤ </span><span style="font-size: 18px;">1000</span></p></div>