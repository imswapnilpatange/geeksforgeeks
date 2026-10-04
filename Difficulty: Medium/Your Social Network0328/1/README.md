<h2><a href="https://www.geeksforgeeks.org/problems/your-social-network0328/1">Your Social Network0328/1</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p class="PDq2pG_selectionAnchorContainer" data-end="343" data-start="240"><span style="font-size: 14pt;">Geek is creating a social networking site called Geeksbook with <strong>n</strong> users numbered from <strong>1 to n</strong>. Each user i (2 ≤ i ≤ n) has exactly one friend, and that friend must have a smaller user number than i. User 1 has no friend. The friends of users 2 to n are given in an array <strong>arr[]</strong> of size n - 1, where:</span></p>
<ul data-end="690" data-start="567">
<li data-end="604" data-section-id="7gklre" data-start="567"><span style="font-size: 14pt;">arr[0] is the friend of user 2. </span></li>
<li data-end="642" data-section-id="1pcqzbe" data-start="605"><span style="font-size: 14pt;"> arr[1] is the friend of user 3. </span></li>
<li data-end="648" data-section-id="1o23ba" data-start="643"><span style="font-size: 14pt;"> ... </span></li>
<li data-end="690" data-section-id="mm8auv" data-start="649"><span style="font-size: 14pt;"> arr[i - 2] is the friend of user i. </span></li>
</ul>
<p data-end="799" data-start="692"><span style="font-size: 14pt;">The relationship is one-way. A user can reach another user by repeatedly following their friend's link. For every user i from 2 to n, find all users j (1 ≤ j &lt; i) that can be reached from i. For every reachable pair (i, j), create an array [i, j, k] where:</span></p>
<ul data-end="1115" data-start="985">
<li data-end="1012" data-section-id="1s3cgrh" data-start="985"><span style="font-size: 14pt;"> i is the starting user. </span></li>
<li data-end="1041" data-section-id="12gznm1" data-start="1013"><span style="font-size: 14pt;"> j is the reachable user. </span></li>
<li data-end="1115" data-section-id="1g1hcf9" data-start="1042"><span style="font-size: 14pt;"> k is the number of links that must be followed to reach j from i. </span></li>
</ul>
<p data-end="1180" data-start="1117"><span style="font-size: 14pt;">The result should contain these arrays in the following order:</span></p>
<ol data-end="1359" data-start="1182">
<li data-end="1219" data-section-id="uymvc5" data-start="1182"><span style="font-size: 14pt;"> Process users i from 2 to n. </span></li>
<li data-end="1301" data-section-id="1klmv91" data-start="1220"><span style="font-size: 14pt;"> For each user i, consider users j from 1 to i - 1 in increasing order. </span></li>
<li data-end="1359" data-section-id="blcbjb" data-start="1302"><span style="font-size: 14pt;"> Include [i, j, k] only if j is reachable from i. </span></li>
</ol>
<p data-end="899" data-start="801"><span style="font-size: 14pt;"> </span></p>
<p data-end="1404" data-start="1361"><span style="font-size: 14pt;">Return a 2D array containing information about all reachable pairs.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong></span><span style="font-size: 18px;">arr[] =<strong> </strong>[1, 2]</span>
<strong><span style="font-size: 18px;">Output:</span> </strong><span style="font-size: 18px;">[[2, 1, 1], [3, 1, 2], [3, 2, 1]]
</span><strong><span style="font-size: 18px;">Explanation:</span> </strong><span style="font-size: 14pt;">The links are 2 → 1<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"> and </span>3 → 2<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">.<span style="font-size: 14pt;"> </span></span>User</span> <span style="font-size: 14pt;">2</span><span style="font-size: 14pt;"> </span><span style="font-size: 14pt;">can reach user</span><span style="font-size: 14pt;"> </span><span style="font-size: 14pt;">1</span><span style="font-size: 14pt;"> </span><span style="font-size: 14pt;">in</span><span style="font-size: 14pt;"> </span><span style="font-size: 14pt;">1</span><span style="font-size: 14pt;"> </span><span style="font-size: 14pt;">link. User 3 can reach user 1 in 2 links. User 3 can reach user 2 in 1 link.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong></span><span style="font-size: 18px;">arr[] =<strong> </strong>[1, 1]</span>
<strong><span style="font-size: 18px;">Output:</span><span style="font-size: 14pt;"> </span></strong><span style="font-size: 14pt;">[[2, 1, 1], [3, 1, 1]]
<strong>Explanation:</strong> The links are 2 → 1 and 3 → 1. User 2 can reach user 1 in 1 link. User 3 can reach user 1 in 1 link.</span></pre></div>