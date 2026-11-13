---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.AvlTree.Tree, Cslib.Algorithms.Lean.AvlTree.height, Cslib.Algorithms.Lean.AvlTree.mkNode, Cslib.Algorithms.Lean.AvlTree.CacheCorrect, Cslib.Algorithms.Lean.AvlTree.Balanced, Cslib.Algorithms.Lean.AvlTree.toBinaryTree, Cslib.Algorithms.Lean.AvlTree.Mem, Cslib.Algorithms.Lean.AvlTree.All
statement: formalized
proof: formalized
---

# AVL tree

77 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html).

## Binary trees with cached heights

For a type $\alpha$, a tree with cached heights over
$\alpha$ (the underlying type of AVL trees) is either empty, or a node made of a natural
number $h$ (its cached height), a left subtree, a key in $\alpha$ and a right subtree.

The type does not require $h$ to equal the actual height of the node.

Formalized by `Cslib.Algorithms.Lean.AvlTree.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#tree).

## Cached height of an AVL tree

The cached height of the empty tree is $0$, and the cached
height of a node is the height value stored at that node, so it is read off the root in
constant time.

Formalized by `Cslib.Algorithms.Lean.AvlTree.height`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#height).

## AVL node with computed height

Write $h(T)$ for the cached height at the root of a tree
$T$, with $h$ of the empty tree equal to $0$. Given trees $L$ and $R$ and a key $k$, this is the
node with left subtree $L$, key $k$ and right subtree $R$ whose cached height is
$\max(h(L), h(R)) + 1$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mkNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mk-node).

## Correct cached heights

The empty tree has correct cached heights. A node storing the
height $c$, with left subtree $\ell$ and right subtree $r$, has correct cached heights when
$\ell$ and $r$ have correct cached heights and $c = \max(h(\ell), h(r)) + 1$, where $h$ denotes
the height cached at the root of a tree (and $0$ for the empty tree).

Formalized by `Cslib.Algorithms.Lean.AvlTree.CacheCorrect`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct).

## AVL balance invariant

The empty tree is balanced. A node with left subtree $\ell$ and
right subtree $r$ is balanced when $\ell$ and $r$ are balanced and $h(\ell) \le h(r) + 1$ and
$h(r) \le h(\ell) + 1$, where $h$ denotes the height cached at the root of a tree (and $0$ for the
empty tree). Equivalently, at every node the balance factor $h(\ell) - h(r)$ lies in
$\{-1, 0, 1\}$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.Balanced`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced).

## Erasing the cached heights of an AVL tree

Let $\alpha$ be a type. Erasing the cached
heights sends a tree with cached heights over $\alpha$ to a binary tree over $\alpha$: the empty
tree goes to the empty binary tree, and a node with height $h$, left subtree $L$, key $k$ and
right subtree $R$ goes to the binary-tree node with key $k$ whose left and right subtrees are
the erasures of $L$ and $R$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.toBinaryTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#to-binary-tree).

## Membership in an AVL tree

A key $x$ belongs to a tree $T$ when $x$ belongs to the binary
tree obtained from $T$ by erasing the cached heights. Equivalently, no key belongs to the empty
tree, and $x$ belongs to a node with left subtree $L$, key $k$ and right subtree $R$ exactly when
$x$ belongs to $L$, $x = k$, or $x$ belongs to $R$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem).

## Every key of an AVL tree satisfies a predicate

For a predicate $p$ on keys and a tree $t$
with cached heights, $\mathrm{All}(p, t)$ holds when $p$ holds at the key of every node of $t$. It
is defined as the corresponding predicate on the plain binary tree obtained from $t$ by erasing
its cached heights.

Formalized by `Cslib.Algorithms.Lean.AvlTree.All`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#all).

## Ordered AVL trees

Let $\alpha$ be a type with a relation $<$. A tree with cached
heights over $\alpha$ is ordered when the binary tree obtained by erasing its cached heights
is an ordered binary search tree: the empty tree is ordered, and a node with key $k$ is
ordered when its left and right subtrees are ordered, every key of the left subtree is less
than $k$, and every key of the right subtree is greater than $k$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered).

## Inorder traversal of an AVL tree onto a suffix

Given a tree $t$ and a list $s$, this is
the list of keys of $t$ in inorder (left subtree, root key, right subtree, recursively)
followed by $s$. It is computed in linear time by the binary search tree traversal of $t$ with
its cached heights erased.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorderAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-aux).

## Inorder traversal of an AVL tree

The inorder traversal of a tree $t$ lists its keys with
the left subtree first, then the root key, then the right subtree, recursively. It is the
binary search tree inorder traversal of $t$ with its cached heights erased, computed in linear
time.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder).

## AVL membership is membership in the underlying binary tree

A key $x$ lies in a tree $T$ if
and only if $x$ lies in the binary tree obtained from $T$ by erasing the cached heights.

This holds by definition.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_toBinaryTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-to-binary-tree).

## The all-keys predicate is unchanged by erasing height caches

For a predicate $p$ on keys
and a tree $t$ with cached heights, $\mathrm{All}(p, t)$ holds if and only if $p$ holds at every
key of the plain binary tree obtained from $t$ by erasing its cached heights. This holds by
definition.

Formalized by `Cslib.Algorithms.Lean.AvlTree.all_toBinaryTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#all-to-binary-tree).

## Order of an AVL tree via its underlying binary tree

Let $\alpha$ be a type with a
relation $<$. A tree $t$ with cached heights over $\alpha$ is ordered if and only if the
binary tree obtained from $t$ by erasing the cached heights is an ordered binary search
tree.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_toBinaryTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-to-binary-tree).

## AVL inorder traversal agrees with the erased binary search tree

For every AVL tree
$t$, the inorder traversal of $t$ equals the binary search tree inorder traversal of the binary
tree obtained from $t$ by erasing its cached heights; this holds by definition.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_toBinaryTree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-to-binary-tree).

## Membership search in an AVL tree

For a linearly ordered type $\alpha$ and a key $x$,
the search for $x$ returns false on the empty tree; at a node with key $k$ it searches the left
subtree if $x < k$, searches the right subtree if $k < x$, and returns true otherwise. The cached
heights are ignored.

Formalized by `Cslib.Algorithms.Lean.AvlTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#contains).

## AVL rebalancing

For trees $l$, $r$ with cached heights and a key $x$, write $h(T)$ for
the cached height at the root of a tree $T$ (zero for the empty tree) and $N(A, y, B)$ for the
node with left subtree $A$, key $y$, right subtree $B$ and cached height $\max(h(A), h(B)) + 1$.
The node $\mathrm{balance}(l, x, r)$ is defined by cases. If $h(l) > h(r) + 1$ and $l$ has left
subtree $A$, key $y$ and right subtree $B$, it is the single right rotation $N(A, y, N(B, x, r))$
when $h(B) \le h(A)$, and otherwise, when $B$ has left subtree $B_1$, key $z$ and right subtree
$B_2$, the left-right double rotation $N(N(A, y, B_1), z, N(B_2, x, r))$. Symmetrically, if
$h(l) \le h(r) + 1$, $h(r) > h(l) + 1$ and $r$ has left subtree $A$, key $y$ and right subtree $B$,
it is the single left rotation $N(N(l, x, A), y, B)$ when $h(A) \le h(B)$, and otherwise, when
$A$ has left subtree $A_1$, key $z$ and right subtree $A_2$, the right-left double rotation
$N(N(l, x, A_1), z, N(A_2, y, B))$. In every other case it is $N(l, x, r)$.

For balanced children with correct cached heights whose heights differ by at most two, the result
is balanced again.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance).

## Insertion into an AVL tree

Let the keys be linearly ordered, and write
$\mathrm{balance}(L, k, R)$ for the AVL rebalancing of the node with left subtree $L$, key $k$ and
right subtree $R$. Inserting $x$ into the empty tree gives the node with key $x$, two empty
children and cached height $1$. Inserting $x$ into a node with left subtree $L$, key $k$ and right
subtree $R$ gives $\mathrm{balance}(L', k, R)$, where $L'$ is the result of inserting $x$ into $L$,
when $x < k$; it gives $\mathrm{balance}(L, k, R')$, where $R'$ is the result of inserting $x$
into $R$, when $k < x$; and otherwise it returns the node unchanged.

Formalized by `Cslib.Algorithms.Lean.AvlTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#insert).

## Building an AVL tree from a list

For a linearly ordered type $\alpha$, the tree built
from the empty list is the empty tree, and the tree built from a list with head $x$ and tail
$xs$ is obtained by AVL insertion of $x$ into the tree built from $xs$. Thus the list is
inserted from right to left, starting from the empty tree.

Formalized by `Cslib.Algorithms.Lean.AvlTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#from-list).

## The all-keys predicate in terms of membership (AVL trees)

For a predicate $p$ on keys and
a tree $t$ with cached heights, $\mathrm{All}(p, t)$ holds if and only if $p(x)$ holds for every
$x \in t$, where $x \in t$ means that $x$ is the key of some node of $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.all_iff_forall_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#all-iff-forall-mem).

## Membership in the inorder traversal of an AVL tree

A key $x$ occurs in the inorder
traversal of a tree $T$ if and only if $x$ lies in $T$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-inorder).

## The inorder traversal of an ordered AVL tree is strictly increasing

Let $\alpha$ be a
linearly ordered type. If a tree $t$ with cached heights over $\alpha$ is ordered, then in
the inorder traversal of $t$ every key is less than every key that comes after it.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-inorder).

## The inorder traversal of an ordered AVL tree has no duplicates

For a linearly ordered
type $\alpha$, if an AVL tree is ordered, then its inorder traversal contains no key twice.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-nodup).

## The AVL node constructor preserves cached heights

If two AVL trees $\ell$ and $r$ have
correct cached heights, then for every key $k$ the node built from $\ell$, $k$ and $r$ by the
smart constructor, which stores the height $\max(h(\ell), h(r)) + 1$ where $h$ denotes the height
cached at the root (and $0$ for the empty tree), also has correct cached heights.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_mkNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-mk-node).

## The AVL node constructor preserves balance

Let $\ell$ and $r$ be AVL trees that satisfy
the AVL balance invariant, and write $h(\ell)$ and $h(r)$ for the heights cached at their roots
(with height $0$ for the empty tree). If $h(\ell) \le h(r) + 1$ and $h(r) \le h(\ell) + 1$, then
for every key $k$ the node built from $\ell$, $k$ and $r$ by the smart constructor, which stores
the height $\max(h(\ell), h(r)) + 1$, satisfies the AVL balance invariant.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_mkNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-mk-node).

## Rebalancing when the heights of the children differ by at most one

Let $l$ and $r$ be
trees with cached heights, let $x$ be a key, and write $h(T)$ for the cached height at the root
of a tree $T$ (zero for the empty tree). If $h(l) \le h(r) + 1$ and $h(r) \le h(l) + 1$, then
$\mathrm{balance}(l, x, r)$ is the node with left subtree $l$, key $x$, right subtree $r$ and
cached height $\max(h(l), h(r)) + 1$; no rotation is performed.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance_eq_mkNode_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance-eq-mk-node-of-le).

## Single right rotation in AVL rebalancing

Write $h(T)$ for the cached height at the root
of a tree $T$ (zero for the empty tree), $\langle c; A, y, B \rangle$ for the node with cached
height $c$, left subtree $A$, key $y$ and right subtree $B$, and $N(A, y, B)$ for the node
$\langle \max(h(A), h(B)) + 1; A, y, B \rangle$. Let $A$, $B$, $R$ be trees with cached heights,
let $x$, $y$ be keys and let $c$ be a natural number. If $h(R) + 1 < c$ and $h(B) \le h(A)$, then
$\mathrm{balance}(\langle c; A, y, B \rangle, x, R) = N(A, y, N(B, x, R))$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance_left_single`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance-left-single).

## Left-right double rotation in AVL rebalancing

Write $h(T)$ for the cached height at the
root of a tree $T$ (zero for the empty tree), $\langle c; A, y, B \rangle$ for the node with
cached height $c$, left subtree $A$, key $y$ and right subtree $B$, and $N(A, y, B)$ for the node
$\langle \max(h(A), h(B)) + 1; A, y, B \rangle$. Let $A$, $B$, $C$, $R$ be trees with cached
heights, let $x$, $y$, $z$ be keys and let $c$, $c'$ be natural numbers. If $h(R) + 1 < c$ and
$h(A) < c'$, then $\mathrm{balance}(\langle c; A, y, \langle c'; B, z, C \rangle \rangle, x, R) =
N(N(A, y, B), z, N(C, x, R))$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance_left_double`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance-left-double).

## Single left rotation in AVL rebalancing

Write $h(T)$ for the cached height at the root of
a tree $T$ (zero for the empty tree), $\langle c; A, y, B \rangle$ for the node with cached height
$c$, left subtree $A$, key $y$ and right subtree $B$, and $N(A, y, B)$ for the node
$\langle \max(h(A), h(B)) + 1; A, y, B \rangle$. Let $L$, $A$, $B$ be trees with cached heights,
let $x$, $y$ be keys and let $c$ be a natural number. If $h(L) + 1 < c$ and $h(A) \le h(B)$, then
$\mathrm{balance}(L, x, \langle c; A, y, B \rangle) = N(N(L, x, A), y, B)$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance_right_single`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance-right-single).

## Right-left double rotation in AVL rebalancing

Write $h(T)$ for the cached height at the
root of a tree $T$ (zero for the empty tree), $\langle c; A, y, B \rangle$ for the node with
cached height $c$, left subtree $A$, key $y$ and right subtree $B$, and $N(A, y, B)$ for the node
$\langle \max(h(A), h(B)) + 1; A, y, B \rangle$. Let $L$, $A$, $B$, $C$ be trees with cached
heights, let $x$, $y$, $z$ be keys and let $c$, $c'$ be natural numbers. If $h(L) + 1 < c$ and
$h(C) < c'$, then $\mathrm{balance}(L, x, \langle c; \langle c'; A, z, B \rangle, y, C \rangle) =
N(N(L, x, A), z, N(B, y, C))$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balance_right_double`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balance-right-double).

## AVL rebalancing preserves cached heights

If two AVL trees $\ell$ and $r$ have correct
cached heights, then for every key $k$ the tree produced by the rebalancing function from
$\ell$, $k$ and $r$ also has correct cached heights.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-balance).

## Upper bound on height after AVL rebalancing

Let $l$ and $r$ be trees whose cached
heights are correct at every node, and write $h$ for the cached height. Then for every key $k$,
the rebalanced node $b$ built from $l$, $k$ and $r$ satisfies $h(b) \le \max(h(l), h(r)) + 1$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.height_balance_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#height-balance-le).

## Rebalancing does not drop below the taller child

Write $h(T)$ for the cached height at the
root of a tree $T$, with $h$ of the empty tree equal to $0$, and write $\mathrm{balance}(L, k, R)$
for the AVL rebalancing of the node with left subtree $L$, key $k$ and right subtree $R$. If $L$
and $R$ are trees whose cached heights are correct at every node, then for every key $k$ we have
$\max(h(L), h(R)) \le h(\mathrm{balance}(L, k, R))$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.le_height_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#le-height-balance).

## AVL rebalancing yields a balanced tree

Let $l$ and $r$ be trees whose cached heights are
correct at every node and which are balanced (at every node the cached heights of the two
subtrees differ by at most one), let $x$ be a key, and write $h(T)$ for the cached height at the
root of a tree $T$ (zero for the empty tree). If $h(l) \le h(r) + 2$ and $h(r) \le h(l) + 2$,
then $\mathrm{balance}(l, x, r)$ is balanced.

One insertion step maintains this precondition.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-balance).

## AVL rebalancing preserves the inorder traversal

For all trees $l$ and $r$ and every
key $k$, the inorder traversal of the rebalanced node built from $l$, $k$ and $r$ is the
inorder traversal of $l$, followed by $k$, followed by the inorder traversal of $r$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-balance).

## Membership after AVL rebalancing

Write $\mathrm{balance}(L, k, R)$ for the AVL rebalancing
of the node with left subtree $L$, key $k$ and right subtree $R$. For trees $L$ and $R$ and keys
$k$ and $x$, the key $x$ lies in $\mathrm{balance}(L, k, R)$ if and only if $x$ lies in $L$,
$x = k$, or $x$ lies in $R$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-balance).

## Rebalancing an AVL node preserves the search-tree order

Let $\alpha$ be a linearly
ordered type, let $k \in \alpha$, and let $L$ and $R$ be ordered trees with cached heights
over $\alpha$ such that every key of $L$ is less than $k$ and every key of $R$ is greater
than $k$. Then the tree that rebalancing produces from left subtree $L$, key $k$ and right
subtree $R$ is ordered.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-balance).

## AVL insertion preserves cached heights

Let $\alpha$ be a linearly ordered type. If an
AVL tree $t$ over $\alpha$ has correct cached heights, then for every $x \in \alpha$ the tree
obtained by inserting $x$ into $t$ also has correct cached heights.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-insert).

## Upper bound on height after AVL insertion

For a linearly ordered type $\alpha$, if a tree
$t$ has correct cached heights at every node, then for every key $x$ the cached height of the
tree obtained by inserting $x$ into $t$ is at most the cached height of $t$ plus one.

Formalized by `Cslib.Algorithms.Lean.AvlTree.height_insert_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#height-insert-le).

## Insertion does not lower the height

Write $h(T)$ for the cached height at the root of a
tree $T$, with $h$ of the empty tree equal to $0$. Let the keys be linearly ordered, and let $T$ be
a tree whose cached heights are correct at every node and which satisfies the AVL balance
invariant at every node. Then for every key $x$, if $T'$ is the tree obtained by inserting $x$
into $T$, we have $h(T) \le h(T')$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.le_height_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#le-height-insert).

## AVL insertion preserves balance

Let $\alpha$ be a linearly ordered type, let $t$ be an
AVL tree over $\alpha$ and let $x \in \alpha$. If $t$ has correct cached heights and satisfies
the AVL balance invariant, then the tree obtained by inserting $x$ into $t$ also satisfies the
AVL balance invariant.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-insert).

## Membership after insertion into an AVL tree

Let the keys be linearly ordered. A key $y$
lies in the tree obtained by inserting $x$ into a tree $T$ if and only if $y = x$ or $y$ lies
in $T$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-insert).

## AVL insertion preserves the search-tree order

Let $\alpha$ be a linearly ordered type.
For every key $x \in \alpha$ and every ordered tree $t$ with cached heights over $\alpha$, the
tree obtained by inserting $x$ into $t$ is ordered.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-insert).

## Correctness of AVL search

Let $\alpha$ be a linearly ordered type and let $t$ be an
ordered AVL tree over $\alpha$. Then for every $x \in \alpha$, searching for $x$ in $t$ by
following comparisons from the root returns true if and only if $x$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 831](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L831). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#contains-eq-true-iff).

## AVL trees built from a list have correct cached heights

For every list $L$ over a
linearly ordered type, the AVL tree built from $L$ by successive insertion has correct cached
heights.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 837](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L837). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-from-list).

## AVL trees built from a list are balanced

For every list $L$ over a linearly ordered
type, the AVL tree built from $L$ by successive insertion satisfies the AVL balance invariant.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-from-list).

## AVL trees built from a list are ordered

Let $\alpha$ be a linearly ordered type. For
every list $xs$ of elements of $\alpha$, the tree obtained from the empty tree by inserting
the elements of $xs$ one at a time, from the last element to the first, is ordered.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 851](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-from-list).

## Membership in an AVL tree built from a list

Let the keys be linearly ordered. A key lies
in the tree obtained by inserting the entries of a list one at a time, from last to first, into
the empty tree exactly when it is in the list.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean, line 858](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree.lean#L858). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-from-list).

## Leftmost key of a tree

Given a default value $d$ and a binary tree $T$ with cached
heights, the leftmost key of $T$ with default $d$ is $d$ when $T$ is empty; when $T$ has left
subtree $L$ and root key $k$, it is the leftmost key of $L$ with default $k$. Thus for a
nonempty tree it is the key of the node reached from the root by following left children as
far as possible, and it does not depend on $d$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.minD`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#min-d).

## Removing the leftmost key of an AVL tree

For a tree $t$ with cached heights, the tree
obtained by removing the leftmost key of $t$ is defined by recursion on $t$. The empty tree stays
empty. A node whose left subtree is empty is replaced by its right subtree. A node with nonempty
left subtree $l$, key $k$ and right subtree $r$ is replaced by $\mathrm{balance}(l', k, r)$, where
$l'$ is $l$ with its leftmost key removed and $\mathrm{balance}$ is the AVL rebalancing function.

Formalized by `Cslib.Algorithms.Lean.AvlTree.eraseMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#erase-min).

## Minimum deletion in an AVL tree

Minimum deletion maps a binary tree with cached heights to
the tree obtained by removing its leftmost key and rebalancing on the way back up. It is the
operation of removing the minimum, under the name used for the successor step of deletion, where a
deleted node with two children is replaced by the minimum of its right subtree.

Formalized by `Cslib.Algorithms.Lean.AvlTree.deleteMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#delete-min).

## AVL tree deletion

Let $\alpha$ be a linearly ordered type and $x \in \alpha$. Deleting $x$
from a tree with cached heights is defined by recursion on the tree, where $\mathrm{balance}$
denotes the AVL rebalancing function. The empty tree stays empty. For a node with left subtree
$l$, key $k$ and right subtree $r$: if $x < k$, the result is $\mathrm{balance}(l', k, r)$, where
$l'$ is $l$ with $x$ deleted; if $k < x$, the result is $\mathrm{balance}(l, k, r')$, where $r'$
is $r$ with $x$ deleted; if $x = k$, the node is replaced by $r$ when $l$ is empty, by $l$ when
$r$ is empty, and otherwise by $\mathrm{balance}(l, m, r'')$, where $m$ is the leftmost key of
$r$ and $r''$ is $r$ with its leftmost key removed.

Formalized by `Cslib.Algorithms.Lean.AvlTree.erase`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#erase).

## AVL tree deletion under its alternative name

For a linearly ordered type $\alpha$, a
key $x \in \alpha$ and a tree $t$ with cached heights, $\mathrm{delete}(x, t)$ is defined to be
$\mathrm{erase}(x, t)$, the AVL deletion of $x$ from $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#delete).

## The leftmost key lies in the tree

For every nonempty binary tree $T$ with cached heights
and every default value $d$, the leftmost key of $T$ computed with default $d$ occurs in $T$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.minD_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#min-d-mem).

## Removing the minimum keeps cached heights correct

Let $t$ be a binary tree with a cached
height at each node whose cached heights are correct: each node stores one more than the larger of
the cached heights of its two subtrees, the empty tree having height $0$. Then the cached heights
of the tree obtained from $t$ by removing its leftmost key, rebalancing on the way back up, are
again correct.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_eraseMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-erase-min).

## Removing the leftmost key does not increase the height of an AVL tree

If $t$ is a tree
whose cached heights are correct, then the cached height of the tree obtained from $t$ by removing
its leftmost key is at most the cached height of $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.height_eraseMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#height-erase-min-le).

## Removing the leftmost key lowers the height of an AVL tree by at most one

If $t$ is a
tree whose cached heights are correct and which is balanced, then the cached height of $t$ is at
most one more than the cached height of the tree obtained from $t$ by removing its leftmost key.

Formalized by `Cslib.Algorithms.Lean.AvlTree.le_height_eraseMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#le-height-erase-min).

## Removing the minimum preserves AVL balance

Let $t$ be a binary tree with a cached height
at each node whose cached heights are correct, and which is balanced: at every node the cached
heights of the two subtrees differ by at most one. Then the tree obtained from $t$ by removing its
leftmost key, rebalancing on the way back up, is again balanced.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_eraseMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-erase-min).

## Removing the leftmost key preserves search-tree order

Let $T$ be a binary tree with cached
heights over a linearly ordered type. If $T$ is ordered as a search tree, then so is the tree
obtained from $T$ by removing its leftmost key and rebalancing on the way back up.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_eraseMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-erase-min).

## Keys left after removing the minimum exceed it

Let $t$ be a binary tree with keys from a
linearly ordered type and a cached height at each node, and suppose $t$ is ordered: at every node,
all keys in the left subtree are strictly smaller and all keys in the right subtree are strictly
larger than the key at that node. Let $m$ be the leftmost key of $t$, or an arbitrary default
value if $t$ is empty. Then every key of the tree obtained from $t$ by removing its leftmost key,
rebalancing on the way back up, is strictly greater than $m$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.all_minD_lt_eraseMin_of_ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#all-min-d-lt-erase-min-of-ordered).

## The inorder traversal begins with the leftmost key

Let $t$ be a nonempty tree with
cached heights and $m$ its leftmost key. Then the inorder traversal of $t$ is $m$ followed by the
inorder traversal of the tree obtained from $t$ by removing its leftmost key.

The leftmost key is computed by a function that takes a default value for the empty tree; the
identity holds for every choice of default.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_eq_minD_cons_eraseMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-eq-min-d-cons-erase-min).

## Deletion keeps cached heights correct

Let $t$ be a binary tree with keys from a linearly
ordered type and a cached height at each node whose cached heights are correct: each node stores
one more than the larger of the cached heights of its two subtrees, the empty tree having height
$0$. Then for every key $x$, the cached heights of the tree obtained from $t$ by deleting $x$,
rebalancing along the search path, are again correct.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-erase).

## Deletion does not increase the height of an AVL tree

Let $\alpha$ be a linearly ordered
type, $x \in \alpha$, and $t$ a tree whose cached heights are correct. Then the cached height of
the tree obtained by deleting $x$ from $t$ is at most the cached height of $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.height_erase_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#height-erase-le).

## Deletion lowers the height of an AVL tree by at most one

Let $\alpha$ be a linearly
ordered type, $x \in \alpha$, and $t$ a balanced tree whose cached heights are correct. Then the
cached height of $t$ is at most one more than the cached height of the tree obtained by deleting
$x$ from $t$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.le_height_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#le-height-erase).

## Deletion preserves AVL balance

Let $t$ be a binary tree with keys from a linearly ordered
type and a cached height at each node, whose cached heights are correct, and which is balanced: at
every node the cached heights of the two subtrees differ by at most one. Then for every key $x$,
the tree obtained from $t$ by deleting $x$, rebalancing along the search path, is again balanced.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-erase).

## AVL deletion preserves search-tree order

Let $T$ be a binary tree with cached heights over
a linearly ordered type, ordered as a search tree (every key in a left subtree is smaller, and
every key in a right subtree is larger, than the key at the node). Then for every key $x$, the
tree obtained by deleting $x$ from $T$ with rebalancing is again ordered as a search tree.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-erase).

## Inorder traversal after AVL deletion

Let $\alpha$ be a linearly ordered type,
$x \in \alpha$, and $t$ an ordered tree. Then the inorder traversal of the tree obtained by
deleting $x$ from $t$ is the inorder traversal of $t$ with the first occurrence of $x$ removed;
if $x$ does not occur, the traversal is unchanged.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-erase).

## AVL deletion keeps every other key

Let $T$ be a binary tree with cached heights whose keys
come from a linearly ordered type, and let $x$ and $y$ be keys with $y \ne x$. If $y$ occurs in
$T$, then $y$ occurs in the tree obtained by deleting $x$ from $T$. No search-tree ordering of
$T$ is assumed.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_erase_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-erase-of-mem).

## Deletion removes the deleted key from an ordered AVL tree

Let $T$ be a binary tree with
cached heights over a linearly ordered type, ordered as a search tree. Then for every key $x$,
$x$ does not occur in the tree obtained by deleting $x$ from $T$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.not_mem_erase_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 745](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L745). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#not-mem-erase-self).

## Keys of an ordered AVL tree after deletion

Let $T$ be a binary tree with cached heights
over a linearly ordered type, ordered as a search tree (every key in a left subtree is smaller,
and every key in a right subtree is larger, than the key at the node). Then for all keys $x$
and $y$, $y$ occurs in the tree obtained by deleting $x$ from $T$ if and only if $y$ occurs in
$T$ and $y \ne x$.

Formalized by `Cslib.Algorithms.Lean.AvlTree.mem_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#mem-erase).

## Deleting a key keeps cached heights correct

Let $t$ be a binary tree with keys from a
linearly ordered type and a cached height at each node whose cached heights are correct: each node
stores one more than the larger of the cached heights of its two subtrees, the empty tree having
height $0$. Then for every key $x$, the cached heights of the tree obtained from $t$ by deleting
$x$, rebalancing along the search path, are again correct.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-delete).

## Deleting a key preserves AVL balance

Let $t$ be a binary tree with keys from a linearly
ordered type and a cached height at each node, whose cached heights are correct, and which is
balanced: at every node the cached heights of the two subtrees differ by at most one. Then for
every key $x$, the tree obtained from $t$ by deleting $x$, rebalancing along the search path, is
again balanced.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 806](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L806). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-delete).

## Deleting a key from an ordered AVL tree keeps it ordered

Let $T$ be a binary tree with
cached heights over a linearly ordered type. If $T$ is ordered as a search tree, then for every
key $x$ the tree obtained by deleting $x$ from $T$ with rebalancing is again ordered as a search
tree.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-delete).

## Inorder traversal after AVL deletion, alternative name

Let $\alpha$ be a linearly
ordered type, $x \in \alpha$, and $t$ an ordered tree. Then the inorder traversal of
$\mathrm{delete}(x, t)$, the AVL deletion of $x$ from $t$ under its alternative name, is the
inorder traversal of $t$ with the first occurrence of $x$ removed; if $x$ does not occur, the
traversal is unchanged.

Formalized by `Cslib.Algorithms.Lean.AvlTree.inorder_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 817](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#inorder-delete).

## Minimum deletion keeps cached heights correct

Let $t$ be a binary tree with a cached height
at each node whose cached heights are correct: each node stores one more than the larger of the
cached heights of its two subtrees, the empty tree having height $0$. Then the cached heights of
the tree obtained from $t$ by minimum deletion (removing its leftmost key, rebalancing on the way
back up) are again correct.

Formalized by `Cslib.Algorithms.Lean.AvlTree.cacheCorrect_deleteMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 822](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L822). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#cache-correct-delete-min).

## Minimum deletion preserves AVL balance

Let $t$ be a binary tree with a cached height at
each node whose cached heights are correct, and which is balanced: at every node the cached heights
of the two subtrees differ by at most one. Then the tree obtained from $t$ by minimum deletion
(removing its leftmost key, rebalancing on the way back up) is again balanced.

Formalized by `Cslib.Algorithms.Lean.AvlTree.balanced_deleteMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 827](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L827). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#balanced-delete-min).

## Successor-step minimum removal preserves search-tree order

Let $T$ be a binary tree with
cached heights over a linearly ordered type. If $T$ is ordered as a search tree, then so is the
tree obtained by the minimum-removal step used for the successor in deletion, which removes the
leftmost key of $T$ and rebalances on the way back up.

Formalized by `Cslib.Algorithms.Lean.AvlTree.ordered_deleteMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AvlTree/Delete.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html#ordered-delete-min).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: AVL tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/avl-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/search-trees/avl-tree)
