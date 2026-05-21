<h2><a href="https://www.geeksforgeeks.org/problems/1s-surrounded-by-0s/1">1S Surrounded By 0S/1</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an n </span>×<span style="font-size: 18px;"> m binary matrix grid[][], find the total count of all cells containing 1 that are unable to move out of the grid through a path of adjacent 1s.</span></p>
<ul>
<li><span style="font-size: 18px;">Adjacency means you can only move in four directions: <strong>Up</strong>, <strong>Down</strong>, <strong>Left</strong>, and <strong>Righ</strong>t. Diagonal moves are not allowed.</span></li>
<li><span style="font-size: 18px;">Assume that the space immediately outside the grid is an <strong>open path</strong>. Any 1 located directly on the outer boundary of the grid (first row, last row, first column, or last column) can immediately step out, and any 1 connected to it can follow and also step out of the grid.</span></li>
</ul>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong><span style="font-size: 18px;">Input<span style="font-size: 14pt;">:</span></span><span style="font-size: 14pt;"> </span></strong></span><span style="font-size: 14pt;">grid[][] = [[0, 0, 0, 0],
		[1, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 0, 0, 0]]</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Output:</span> </strong></span><span style="font-size: 18px;">3</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Explanation:</span> </strong></span><span style="font-size: 18px;">The highlighted cells represent the land cells.<br/></span> <img height="187" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/926453/Web/Other/blobid0_1778049188.jpg" width="187"/></pre>
<pre><span style="font-size: 18px;"><strong><span style="font-size: 18px;">Input:</span> </strong></span><span style="font-size: 18px;"><span style="font-size: 18px;">grid[][] = [[1, 1, 0, 0, 0, 1]</span></span><span style="font-size: 14pt;">
		[0, 1, 1, 0, 1, 0],
		[0, 0, 0, 1, 1, 0],
		[0, 0, 0, 1, 1, 0],
		[0, 1, 0, 1, 0, 0],
		[1, 1, 0, 0, 0, 1]]</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Output:</span> </strong></span><span style="font-size: 18px;">6</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Explanation:</span> </strong></span><span style="font-size: 18px;">The highlighted cells represent the land cells.<br/><img alt="425537429" height="193" src="https://media.geeksforgeeks.org/wp-content/uploads/20260424153909634770/425537429.webp" width="270"/></span></pre>
<p><strong><span style="font-size: 18px;">Constraints:<br/></span></strong><span style="font-size: 18px;">1 ≤ n, m ≤ 500<br/></span><span style="font-size: 18px;">0 ≤ grid[i][j] ≤ 1</span></p></div>