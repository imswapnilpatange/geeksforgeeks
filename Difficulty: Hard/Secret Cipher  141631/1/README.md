<h2><a href="https://www.geeksforgeeks.org/problems/secret-cipher--141631/1">Secret Cipher  141631/1</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p class="PDq2pG_selectionAnchorContainer" data-end="177" data-start="23"><span style="font-size: 14pt;">Geek wants to send a secret message to his friend Keeg. Instead of sending the original message directly, he encrypts it by inserting the character '*'.</span></p>
<p data-end="215" data-start="179"><span style="font-size: 14pt;">Keeg decodes the message as follows:</span></p>
<ul data-end="395" data-start="216">
<li data-end="257" data-section-id="38pzl8" data-start="216"><span style="font-size: 14pt;"> Traverse the encoded string from left to right and initialize the original string as empty.</span></li>
<li data-end="257" data-section-id="38pzl8" data-start="216"><span style="font-size: 14pt;">Whenever a normal character appears, append it to the current original string.</span></li>
<li data-end="362" data-section-id="f435m5" data-start="258"><span style="font-size: 14pt;"> Whenever '*' is encountered, remove it and append all characters before it to the end of the current original string. </span></li>
<li data-end="395" data-section-id="1mhnp27" data-start="363"><span style="font-size: 14pt;"> Repeat until no '*' remains. </span></li>
</ul>
<p class="PDq2pG_selectionAnchorContainer" data-end="213" data-start="48"><span style="font-size: 14pt;"> </span></p>
<p data-end="501" data-is-last-node="" data-is-only-node="" data-start="397"><span style="font-size: 14pt;">Given the original string s, find the lexicographically smallest encrypted string that decodes to s.</span></p>
<p data-end="600" data-start="504"><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> s = "ababcababcd"
<strong>Output:</strong> ab*c*d
<strong>Explanation: </strong>We can encrypt the string in following way : "ababcababcd" -&gt; "ababc*d" -&gt; "ab*c*d"</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> s = "zzzzzzz"
<strong>Output:</strong> z*z*z
<strong>Explanation: </strong>The string can be encrypted in 2 ways: "z*z*z" and "z**zzz". Out of the two "z*z*z" is smaller in length.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints: </strong><br/>1 ≤ |s| ≤ 10<sup>5</sup></span></p></div>