<h2><a href="https://www.geeksforgeeks.org/problems/huffman-encoding3345/1">Huffman Encoding3345/1</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string <strong>s</strong> of distinct characters and their corresponding frequency <strong>f[ ]</strong> i.e. character <strong>s</strong><strong>[i]</strong> has<strong> f[i]</strong> frequency. You need to build the Huffman tree and return all the huffman codes in preorder traversal of the tree.<br/><strong>Note: </strong>While merging if two nodes have the same value, then the node which occurs at first will be taken on the left of Binary Tree and the other one to the right, otherwise Node with less value will be taken on the left of the subtree and other one to the right.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> s = "abcdef", f[] = {5, 9, 12, 13, 16, 45}
<strong>Output: </strong>[0, 100, 101, 1100, 1101, 111]
<strong>Explanation:
</strong></span><span style="font-size: 18px;"><img height="242" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/705885/Web/Other/blobid0_1753358055.webp" width="372"/><br/>HuffmanCodes will be:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br/>1 ≤ s.size() = f.size() ≤ 26</span></p></div>