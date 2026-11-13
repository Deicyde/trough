---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SplayTree.root?, Cslib.Algorithms.Lean.SplayTree.splay, Cslib.Algorithms.Lean.SplayTree.splay_nil, Cslib.Algorithms.Lean.SplayTree.inorder_splay, Cslib.Algorithms.Lean.SplayTree.mem_splay, Cslib.Algorithms.Lean.SplayTree.numNodes_splay, Cslib.Algorithms.Lean.SplayTree.ordered_splay, Cslib.Algorithms.Lean.SplayTree.root_splay_of_mem
statement: formalized
proof: formalized
---

# Splay tree

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html).

## Root key of a splay tree

The optional root key of a binary tree is undefined (none) for
the empty tree, and is the key $k$ for a tree whose root node holds $k$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.root?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#root).

## Splay operation

Let $\alpha$ be a linearly ordered type and write $(k; L, R)$ for the binary
tree with root key $k$, left subtree $L$ and right subtree $R$. For $x \in \alpha$, the splay
$S_x(t)$ of a binary tree $t$ with keys in $\alpha$ is defined by recursion on $t$. The empty tree
splays to itself, and $t = (k; L, R)$ is left unchanged if $x = k$, if $x < k$ and $L$ is empty,
or if $x > k$ and $R$ is empty. If $x < k$ and $L = (a; A, B)$, then: if $x = a$, the result is
the zig $(a; A, (k; B, R))$; if $x < a$ and $S_x(A) = (d; A_1, A_2)$, the result is the zig-zig
$(d; A_1, (a; A_2, (k; B, R)))$; if $x > a$ and $S_x(B) = (d; B_1, B_2)$, the result is the
zig-zag $(d; (a; A, B_1), (k; B_2, R))$; and if the splayed subtree $S_x(A)$, respectively
$S_x(B)$, is empty, the result is the zig $(a; A, (k; B, R))$. The case $x > k$ with
$R = (b; C, D)$ is the mirror image: if $x = b$, the result is the zig $(b; (k; L, C), D)$; if
$x > b$ and $S_x(D) = (d; D_1, D_2)$, it is the zig-zig $(d; (b; (k; L, C), D_1), D_2)$; if
$x < b$ and $S_x(C) = (d; C_1, C_2)$, it is the zig-zag $(d; (k; L, C_1), (b; C_2, D))$; and if
the splayed subtree is empty, it is the zig $(b; (k; L, C), D)$.

The search path for $x$ runs from the root to the node with key $x$, or to the last node visited
if $x$ is absent. Each recursive step consumes two edges of this path, starting at the root, so
when the path has an odd number of edges the single rotation is performed on its last edge, the
one farthest from the root.

Formalized by `Cslib.Algorithms.Lean.SplayTree.splay`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#splay).

## Splaying the empty tree

For every key $x$ of a linearly ordered type, splaying $x$ in the
empty binary tree gives the empty tree.

Formalized by `Cslib.Algorithms.Lean.SplayTree.splay_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#splay-nil).

## Splaying preserves the inorder traversal

For every key $x$ and every binary tree $t$
over a linearly ordered type, the inorder traversal of the tree obtained by splaying $x$ in $t$
equals the inorder traversal of $t$. No search-tree ordering of $t$ is assumed.

Formalized by `Cslib.Algorithms.Lean.SplayTree.inorder_splay`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#inorder-splay).

## Splaying preserves membership

For keys $x$ and $y$ and a binary tree $t$ over a linearly
ordered type, $y$ is a key of the tree obtained by splaying $x$ in $t$ if and only if $y$ is a
key of $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.mem_splay`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#mem-splay).

## Splaying preserves the number of nodes

For every binary tree $t$ with keys in a linearly
ordered type and every key $x$, the tree obtained by splaying $x$ in $t$ has the same number of
nodes as $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.numNodes_splay`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#num-nodes-splay).

## Splaying preserves the search-tree property

Let $t$ be a binary tree with keys in a
linearly ordered type and let $x$ be a key. If $t$ is a binary search tree (at every node, every
key of the left subtree is strictly smaller and every key of the right subtree strictly larger
than the key of the node), then the tree obtained by splaying $x$ in $t$ is again a binary search
tree.

Formalized by `Cslib.Algorithms.Lean.SplayTree.ordered_splay`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#ordered-splay).

## Splaying a present key brings it to the root

Let $t$ be a binary search tree with keys in
a linearly ordered type (at every node, every key of the left subtree is strictly smaller and
every key of the right subtree strictly larger than the key of the node), and let $x$ be a key
that occurs in $t$. Then there are binary trees $l$ and $r$ such that splaying $x$ in $t$ gives
the tree whose root holds $x$, with left subtree $l$ and right subtree $r$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.root_splay_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#root-splay-of-mem).

## Root key after splaying a present key

Let $t$ be a binary search tree with keys in a
linearly ordered type (at every node, every key of the left subtree is strictly smaller and every
key of the right subtree strictly larger than the key of the node), and let $x$ be a key that
occurs in $t$. Then the tree obtained by splaying $x$ in $t$ is nonempty and its root key is $x$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.root?_splay_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#root-splay-of-mem-2).

## Search-path split at a key

Let $\alpha$ be a linearly ordered type, let $x \in \alpha$, and
write $(k; L, R)$ for the binary tree with root key $k$, left subtree $L$ and right subtree $R$.
The split of a binary tree with keys in $\alpha$ at $x$ is the pair of trees defined by
recursion: the empty tree splits into two empty trees; if $x < k$ and $L$ splits into
$(L_1, L_2)$, then $(k; L, R)$ splits into $(L_1, (k; L_2, R))$; if $k < x$ and $R$ splits into
$(R_1, R_2)$, then $(k; L, R)$ splits into $((k; L, R_1), R_2)$; and if $x = k$, then
$(k; L, R)$ splits into $(L, R)$.

When the tree is a binary search tree (at every node, the keys of the left subtree are strictly
smaller and those of the right subtree strictly larger than the node's key), the first part
holds the keys below $x$ and the second part the keys above $x$; the key $x$, if present, is
dropped.

Formalized by `Cslib.Algorithms.Lean.SplayTree.split`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#split).

## Splay-tree split parts contain only original keys

For keys $x$ and $y$ and a binary
tree $t$ over a linearly ordered type, if $y$ is a key of the left part or of the right part of
the split of $t$ at $x$, then $y$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.mem_of_mem_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#mem-of-mem-split).

## Keys other than the split key survive a split

Let $t$ be a binary tree with keys in a
linearly ordered type, and let $x$ and $y$ be keys with $y \ne x$. If $y$ occurs as a key of $t$,
then $y$ occurs as a key of the left part or of the right part of the split of $t$ at $x$.
The tree $t$ need not be a binary search tree.

Formalized by `Cslib.Algorithms.Lean.SplayTree.mem_split_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#mem-split-of-mem).

## Splitting an ordered tree separates the keys around the split key

Let $t$ be an ordered
binary tree over a linearly ordered type and let $x$ be a key. When $t$ is split at $x$, every
key of the left part is strictly less than $x$ and every key of the right part is strictly
greater than $x$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.all_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#all-split).

## Both parts of a split search tree are search trees

Let $t$ be a binary tree with keys in a
linearly ordered type and let $x$ be a key. If $t$ is a binary search tree (at every node, every
key of the left subtree is strictly smaller and every key of the right subtree strictly larger
than the key of the node), then the left part and the right part of the split of $t$ at $x$ are
both binary search trees.

Formalized by `Cslib.Algorithms.Lean.SplayTree.ordered_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#ordered-split).

## Splay-tree insertion

For a key $x$ and a binary tree $t$ over a linearly ordered type,
inserting $x$ into $t$ splays $x$ in $t$, splits the resulting tree at $x$ into a left part and
a right part, and returns the tree whose root key is $x$, whose left subtree is the left part
and whose right subtree is the right part.

In an ordered tree that already contains $x$, the key is splayed to the root and dropped by the
split, so no duplicate is created.

Formalized by `Cslib.Algorithms.Lean.SplayTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#insert).

## Splay-tree access

For a key $x$ and a binary tree $t$ over a linearly ordered type, the
access of $x$ in $t$ is the pair $(b, t')$, where $t'$ is the tree obtained by splaying $x$ in
$t$ and $b$ is true exactly when $t'$ is nonempty and its root key is $x$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.access`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#access).

## Splay-tree membership test

For a key $x$ and a binary tree $t$ over a linearly ordered
type, the membership test of $x$ in $t$ is the Boolean component of the access of $x$ in $t$:
it is true exactly when the tree obtained by splaying $x$ in $t$ is nonempty and its root key
is $x$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 754](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L754). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#contains).

## The tree returned by a splay-tree access

For a key $x$ and a binary tree $t$ over a
linearly ordered type, the tree component of the access of $x$ in $t$ is the tree obtained by
splaying $x$ in $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.access_snd`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#access-snd).

## Keys after splay-tree insertion

For keys $x$ and $y$ and a binary tree $t$ over a
linearly ordered type, $y$ is a key of the tree obtained by splay-tree insertion of $x$ into $t$
if and only if $y = x$ or $y$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 764](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L764). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#mem-insert).

## Splay-tree insertion preserves the search-tree property

Let $t$ be a binary tree with keys
in a linearly ordered type and let $x$ be a key. If $t$ is a binary search tree (at every node,
every key of the left subtree is strictly smaller and every key of the right subtree strictly
larger than the key of the node), then the splay-tree insertion of $x$ into $t$ is again a binary
search tree.

Formalized by `Cslib.Algorithms.Lean.SplayTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#ordered-insert).

## Splay-tree insertion puts the inserted key at the root

For every binary tree $t$ with keys
in a linearly ordered type and every key $x$, the splay-tree insertion of $x$ into $t$ is a
nonempty tree whose root key is $x$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.root?_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#root-insert).

## Correctness of the splay-tree membership test

For an ordered binary tree $t$ over a
linearly ordered type and a key $x$, the splay-tree membership test of $x$ in $t$ returns true
if and only if $x$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.SplayTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/SplayTree.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html#contains-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Splay tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/splay-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/search-trees/splay-tree)
