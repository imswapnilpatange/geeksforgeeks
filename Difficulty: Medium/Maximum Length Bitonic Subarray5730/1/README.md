<h2><a href="https://www.geeksforgeeks.org/problems/maximum-length-bitonic-subarray5730/1">Maximum Length Bitonic Subarray5730/1</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong> of size <strong>n</strong> containing positive integers, return the maximum length of the bitonic<strong> </strong>subarray.</span></p>
<p><span style="font-size: 18px;">A subarray <strong>arr[i...j]</strong> is considered bitonic if its elements first monotonically increase, and then monotonically decrease. Formally, there exists and index <strong>k</strong> (where <strong>i &lt;= k &lt;= j</strong>) such that:</span></p>
<ul>
<li><span style="font-size: 18px;">arr[i] &lt;= arr[i+1] &lt;= . . . &lt;= arr[k] </span></li>
<li><span style="font-size: 18px;">arr[k] &gt;= arr[k+1] &gt;= . . . &gt;= arr[j]</span></li>
</ul>
<p><strong style="font-size: 18px;">Examples: </strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [12, 4, 78, 90, 45, 23]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest bitonic subarray is [4, 78, 90, 45, 23], it starts increasing at 4, peaks at 90, and decreases to 23, giving length of 5.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [10, 20, 30, 40]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The array [10, 20, 30, 40] is striclty increasing with no decreasing part, so longest bitonic subarray is the entire array itself, giving a length of 4.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [10, 10, 10, 10]
<strong>Output:</strong> 4</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br/>1 ≤  n ≤ 10<sup>6</sup><br/>1 ≤ arr[i] ≤ 10<sup>6</sup></span></p></div>