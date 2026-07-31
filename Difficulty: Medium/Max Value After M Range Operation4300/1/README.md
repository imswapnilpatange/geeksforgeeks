<h2><a href="https://www.geeksforgeeks.org/problems/max-value-after-m-range-operation4300/1">Max Value After M Range Operation4300/1</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given three arrays <strong>a[],</strong> <strong>b[]</strong>, and <strong>k[]</strong>, representing <strong>m</strong> range increment operations on an array arr[] of size <strong>n,</strong> where all elements of arr[] are initially 0.</span></p>
<ul>
<li><span style="font-size: 14pt;">Increment(a[i], b[i], k[i]) adds k[i] to each element arr[j] such that a[i] ≤ j ≤ b[i] (mainly indexes in range from a[i] to b[i])</span></li>
<li><span style="font-size: 14pt;">After performing all the given operations, find the maximum value present in the array.</span></li>
</ul>
<p><strong style="font-size: 18px;">Examples:</strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 5,<strong> </strong>a[] = [0, 1, 2], b[] = [1, 4, 3], k[] = [100, 100, 100]
<strong>Output:</strong> 200
<strong>Explanation</strong>: Initially, arr = [0, 0, 0, 0, 0]
After the first operation: arr = [100, 100, 0, 0, 0]
After the second operation: arr = [100, 200, 100, 100, 100]
After the third operation: arr = [100, 200, 200, 200, 100]
The maximum element after all operations is 200.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 4,<strong> </strong>a[] = [1, 0, 3], b[] = [2, 0, 3], k[] = [603, 286, 882]
<strong>Output:</strong> 882
<strong>Explanation</strong>: Initially, arr = [0, 0, 0, 0]
After the first operation: arr = [0, 603, 603, 0]
After the second operation: arr = [286, 603, 603, 0]
After the third operation: arr = [286, 603, 603, 882]
The maximum element after all operations is 882.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:<br/></strong></span><span style="font-size: 18px;">1 ≤  n ≤ 10<sup>6<br/></sup></span><span style="font-size: 18px;">1 ≤  a.size() = b.size() = k.size() = m  ≤ 10</span><sup>6</sup><br/><span style="font-size: 18px;">0 ≤  a<sub>i  </sub>≤  b<sub>i </sub> ≤ n-1<br/></span><span style="font-size: 18px;">0 ≤  k<sub>i </sub> ≤ 10<sup>6</sup></span></p></div>