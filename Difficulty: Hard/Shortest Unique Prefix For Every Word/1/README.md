<h2><a href="https://www.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1">Shortest Unique Prefix For Every Word/1</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p data-end="171" data-start="23"><span style="font-size: 14pt;">Given an array of strings <strong>arr[ ]</strong>, find the <strong data-end="96" data-start="77">shortest prefix</strong> of each string that uniquely identifies it among all strings in the array. </span><span style="font-size: 14pt;">A <strong>prefix </strong>is unique if it is not a prefix of any other string in the array. </span><span style="font-size: 14pt;">Return the shortest unique prefix for every string in the same order as the input.</span></p>
<p data-end="396" data-start="333"><span style="font-size: 14pt;"><strong data-end="342" data-start="333">Note:</strong> No string in the array is a prefix of another string.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = {"zebra", "dog", "duck", "dove"}
<strong>Output: </strong>z dog du dov
<strong>Explanation: </strong>z =&gt; zebra, dog =&gt; dog, duck =&gt; du, dove =&gt; dov </span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = {"geeksgeeks", "geeksquiz", "geeksforgeeks"}
<strong>Output: </strong>geeksg geeksq geeksf<br/><strong>Explanation: </strong>geeksgeeks =&gt; geeksg, geeksquiz =&gt; geeksq, geeksforgeeks =&gt; geeksf<br/></span></pre>
<div><span style="font-size: 18px;"><strong>Constraints:</strong></span></div>
<div><span style="font-size: 18px;">1 ≤ length of arr, length of each word ≤ 1000</span></div></div>