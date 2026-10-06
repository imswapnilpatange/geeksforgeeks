<h2><a href="https://www.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1">Longest Increasing Path In A Matrix/1</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given a matrix with <strong>n</strong> rows and <strong>m </strong>columns. Your task is to find the length of the longest path in with the following constraints</span></p>
<ul>
<li><span style="font-size: 18px;">The values in path strictly increasing.  </span><span style="font-size: 18px;">For example if a path of length k has values a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, .... a<sub>k </sub> , then for every i from [2, k] this condition must hold a<sub>i </sub>&gt; a<sub>i-1</sub>.  </span></li>
<li><span style="font-size: 18px;">No cell should be revisited in the path.</span></li>
<li><span style="font-size: 18px;">From each cell,  you can move in any of of the four directions: left, right, up, or down. </span></li>
<li><span style="font-size: 18px;">You are not allowed to move diagonally or move outside the boundary.</span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples</strong><strong>:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 3, m = 3, matrix[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
<strong>Output: </strong>5<strong>
Explanation: </strong>One such path is 1 -&gt; 2 -&gt; 3 -&gt; 6 -&gt; 9, where each number is strictly greater than the previous.<br/></span><img height="194" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894126/Web/Other/blobid0_1746855773.jpg" width="196"/></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">n = 3, m = 3, matrix[][] = [[3, 4, 5], [6, 2, 6], [2, 2, 1]]
</span><strong style="font-size: 18px;">Output: </strong><span style="font-size: 18px;">4</span><strong style="font-size: 18px;">
Explanation: </strong><span style="font-size: 18px;">One of the longest increasing paths is 3 -&gt; 4 -&gt; 5 -&gt; 6.<br/><img height="194" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894126/Web/Other/blobid1_1746855807.jpg" width="196"/></span></span></pre></div>