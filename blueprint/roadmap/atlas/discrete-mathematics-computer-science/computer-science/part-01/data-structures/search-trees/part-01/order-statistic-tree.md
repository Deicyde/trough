---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.OrderStatisticTree.Entry, Cslib.Algorithms.Lean.OrderStatisticTree.Tree, Cslib.Algorithms.Lean.OrderStatisticTree.cachedSize, Cslib.Algorithms.Lean.OrderStatisticTree.erase, Cslib.Algorithms.Lean.OrderStatisticTree.CacheCorrect, Cslib.Algorithms.Lean.OrderStatisticTree.Ordered, Cslib.Algorithms.Lean.OrderStatisticTree.inorder, Cslib.Algorithms.Lean.OrderStatisticTree.node
statement: formalized
proof: formalized
---

# Order statistic tree

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html).

## Order-statistic tree node entry

A node entry of an order-statistic tree over a type
$\alpha$ consists of a key in $\alpha$ and a natural number, the cached number of nodes in the
subtree rooted at that node.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.Entry`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#entry).

## Order-statistic tree

An order-statistic tree with keys in a type $\alpha$ is a binary
tree, possibly empty, each of whose nodes carries a key in $\alpha$ together with a natural
number, meant as the cached number of nodes in the subtree rooted at that node. That these
caches are correct is a separate condition.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.Tree`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#tree).

## Cached root size

The cached root size of an order-statistic tree is the subtree size
stored in the entry of its root node, and is $0$ for the empty tree.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cachedSize`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cached-size).

## Erasing the size caches of an order-statistic tree

The erasure of an order-statistic
tree is the binary tree of the same shape whose node keys are the keys of the original nodes:
the empty tree is sent to the empty tree, and a node is sent to the node with the same key
whose left and right subtrees are the erasures of the original left and right subtrees, so
every cached subtree size is dropped.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.erase`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#erase).

## Correct size caches

An order-statistic tree has correct size caches when, at every
node, the cached subtree size equals the number of nodes of the left subtree plus the number of
nodes of the right subtree plus one, that is, the number of nodes of the subtree rooted at that
node. The empty tree has correct size caches.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.CacheCorrect`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct).

## Ordered order-statistic tree

An order-statistic tree over a type equipped with a
relation $<$ is ordered when the binary tree obtained by erasing its cached sizes is an ordered
binary search tree: at every node, each key of the left subtree is $<$ the node's key, the
node's key is $<$ each key of the right subtree, and both subtrees are ordered.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#ordered).

## Inorder traversal of an order-statistic tree

The inorder traversal of an
order-statistic tree is the inorder traversal of the binary tree obtained by erasing its cached
subtree sizes: the traversal of the left subtree, then the root key, then the traversal of the
right subtree, and the empty list for the empty tree.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.inorder`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#inorder).

## Order-statistic tree node with computed cache

Given a key $k$ and order-statistic
trees $L$ and $R$, the node built from them has key $k$, left subtree $L$, right subtree $R$,
and cached subtree size equal to the cached root size of $L$ plus the cached root size of $R$
plus one, where the empty tree has cached root size zero.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.node`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#node).

## Search in an order-statistic tree

Let $\alpha$ be a linearly ordered type and
$q \in \alpha$. Searching for $q$ in the empty tree returns false. At a node with key $k$, the
search continues in the left subtree if $q < k$, continues in the right subtree if $k < q$, and
returns true otherwise.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#contains).

## Insertion into an order-statistic tree

Inserting a key $k$ of a linearly ordered type
into the empty tree gives a single node with key $k$ and cached size $1$. For a nonempty tree
with root key $r$: if $k < r$, the key is inserted into the left subtree; if $r < k$, it is
inserted into the right subtree; in both cases the root is rebuilt with key $r$ and cached size
equal to the cached root sizes of its two subtrees plus one (an empty subtree counts as zero).
Otherwise $k = r$ and the tree is returned unchanged.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#insert).

## Order-statistic tree built from a list

For a linearly ordered key type, the
order-statistic tree built from a list of keys is obtained by inserting the keys into the empty
tree from right to left: the empty list gives the empty tree, and a list with head $k$ and
tail $l$ gives the insertion of $k$ into the tree built from $l$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#from-list).

## Rank in an order-statistic tree

For a key $q$ of a linearly ordered type, the rank of
$q$ in an order-statistic tree is computed by descending from the root. It is $0$ for the empty
tree. At a node with key $k$, left subtree $L$ and right subtree $R$, it is the rank of $q$ in
$L$ if $q < k$; it is $s(L) + 1$ plus the rank of $q$ in $R$ if $k < q$; and it is $s(L)$ if
$q = k$. Here $s(L)$ is the subtree size cached at the root of $L$, and $0$ if $L$ is empty.

When the cached sizes are correct and the tree is ordered, this is the number of keys in the
tree strictly smaller than $q$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.rank`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#rank).

## Select in an order-statistic tree

For an order-statistic tree $T$ and a natural number
$i$, select at index $i$ in $T$ is computed by descending from the root. It returns nothing for
the empty tree. At a node with key $k$, left subtree $L$ and right subtree $R$, it is select at
index $i$ in $L$ if $i < s(L)$; it returns $k$ if $i = s(L)$; and it is select at index
$i - s(L) - 1$ in $R$ if $i > s(L)$. Here $s(L)$ is the subtree size cached at the root of $L$,
and $0$ if $L$ is empty.

When the cached sizes are correct, this returns the key at zero-based position $i$ of the
inorder traversal, and nothing if $T$ has at most $i$ nodes.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.select`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#select).

## Correct caches give the tree size

If an order-statistic tree $T$ has correct cached
subtree sizes at every node, then the cached root size of $T$ (zero for the empty tree) equals
the number of nodes of $T$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cachedSize_eq_numNodes`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cached-size-eq-num-nodes).

## The cache-computing node constructor preserves correct size caches

Let $k$ be a key and
let $L$ and $R$ be order-statistic trees whose cached subtree sizes are correct at every node.
Then the node with key $k$, left subtree $L$ and right subtree $R$, whose root cache is the
cached root size of $L$ plus the cached root size of $R$ plus one, also has correct cached
subtree sizes at every node.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cacheCorrect_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct-node).

## Insertion commutes with forgetting the size caches

Let $\alpha$ be a linearly ordered
type, $k \in \alpha$ and $T$ an order-statistic tree over $\alpha$. Forgetting the cached sizes
of the tree obtained by inserting $k$ into $T$ gives the same binary tree as inserting $k$, by
ordinary binary-search-tree insertion, into $T$ with its cached sizes forgotten.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.erase_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#erase-insert).

## Insertion preserves correct size caches

Let $\alpha$ be a linearly ordered type, let
$k \in \alpha$, and let $T$ be an order-statistic tree over $\alpha$ whose cached subtree sizes
are correct at every node. Then the tree obtained by inserting $k$ into $T$ also has correct
cached subtree sizes at every node.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cacheCorrect_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct-insert).

## Insertion preserves ordering of order-statistic trees

Let $T$ be an order-statistic
tree over a linearly ordered key type that is ordered, meaning that after its cached sizes are
erased, at every node each key of the left subtree is strictly smaller than the node's key and
each key of the right subtree is strictly larger. Then for every key $k$, the tree obtained by
inserting $k$ into $T$ is again ordered.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#ordered-insert).

## Order-statistic trees built from a list have correct size caches

Let $\alpha$ be a
linearly ordered type. For every list $\ell$ of elements of $\alpha$, the order-statistic tree
obtained by inserting the elements of $\ell$ into the empty tree, from right to left, has correct
cached subtree sizes at every node.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cacheCorrect_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct-from-list).

## Order-statistic trees built from lists are ordered

For every list $l$ of keys from a
linearly ordered type, the order-statistic tree built from $l$ by successive insertion is
ordered: after its cached sizes are erased, at every node each key of the left subtree is
strictly smaller than the node's key and each key of the right subtree is strictly larger.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.ordered_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#ordered-from-list).

## Keys of an order-statistic tree built from a list

For a linearly ordered key type, a
key $k$ and a list $l$ of keys, $k$ is a key of some node of the order-statistic tree built
from $l$ by successive insertion if and only if $k$ occurs in $l$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#mem-from-list).

## Search in an ordered order-statistic tree is correct

Let $\alpha$ be a linearly ordered
type and $T$ an order-statistic tree over $\alpha$ that is ordered: after forgetting the cached
sizes, at every node all keys in the left subtree are smaller than the node's key and all keys in
the right subtree are larger. Then for every $q \in \alpha$, comparison search for $q$ in $T$
returns true if and only if $q$ is the key of some node of $T$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#contains-eq-true-iff).

## Cached rank agrees with traversal rank

Let $T$ be an order-statistic tree over a
linearly ordered key type whose cached subtree sizes are correct at every node and which is
ordered. Then for every query $q$, the rank of $q$ computed by descending $T$ with cached
left-subtree sizes equals the number of entries strictly smaller than $q$ in the inorder
traversal of the binary tree obtained by erasing the caches of $T$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.rank_eq_bstRank`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#rank-eq-bst-rank).

## Cached select agrees with inorder select

For every order-statistic tree $T$ whose
cached subtree sizes are correct and every natural number $i$, select at index $i$ in $T$
(descending with the cached sizes) returns the same result as taking the element at zero-based
position $i$ of the inorder traversal of the binary tree obtained from $T$ by erasing the cached
sizes; in particular both return nothing when that position does not exist.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.select_eq_bstSelect`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#select-eq-bst-select).

## Select inverts rank in an order-statistic tree

Let $T$ be an order-statistic tree over
a linearly ordered type whose cached subtree sizes are correct and which satisfies the
binary-search-tree ordering. For every key $k$ in $T$, select in $T$ at the index equal to the
rank of $k$ in $T$ returns $k$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.select_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#select-rank).

## Rank inverts select in an order-statistic tree

Let $T$ be an order-statistic tree
over a linearly ordered type whose cached subtree sizes are correct and which satisfies the
binary-search-tree ordering. If select at zero-based index $i$ in $T$ returns a key $k$, then
the rank of $k$ in $T$ equals $i$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.rank_select`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#rank-select).

## Merging order-statistic trees

The merge of order-statistic trees $A$ and $B$ is defined by
recursion on $A$. If $A$ is empty, it is $B$. If $A$ has root key $x$, left subtree $L$ and right
subtree $R$, it is the node with key $x$, left subtree $L$ and right subtree the merge of $R$ and
$B$, whose cached size is the sum of the cached root sizes of its children plus one, an empty
child counting as zero. Thus $B$ is attached below the rightmost path of $A$, and every node on
that path gets a recomputed cache.

The merge is intended for trees in which every key of $A$ is smaller than every key of $B$, but it
is defined for all pairs of trees.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.merge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#merge).

## Deletion from an order-statistic tree

Deleting a key $k$ from an order-statistic tree over a
linearly ordered type follows the comparison path from the root. The empty tree stays empty. At a
node with key $x$, left subtree $L$ and right subtree $R$: if $k < x$, the result is the node with
key $x$, left subtree the deletion of $k$ from $L$ and right subtree $R$; if $x < k$, it is the
node with key $x$, left subtree $L$ and right subtree the deletion of $k$ from $R$; otherwise
($k = x$) it is the merge of $L$ and $R$. Each rebuilt node gets as cached size the sum of the
cached root sizes of its children plus one, an empty child counting as zero.

If $k$ does not occur in the tree, the result has the same keys.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#delete).

## Order-statistic merge preserves cache correctness

Let $A$ and $B$ be order-statistic trees
whose cached subtree size at every node equals the number of nodes in that node's subtree. Then
the merge of $A$ and $B$ has the same property. No ordering between the keys of $A$ and $B$ is
assumed.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cacheCorrect_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct-merge).

## Order-statistic deletion preserves cache correctness

Let $\alpha$ be a linearly ordered
type, $k \in \alpha$ a key and $T$ an order-statistic tree over $\alpha$. If the cached subtree size
at every node of $T$ equals the number of nodes in that node's subtree, then the same holds for the
tree obtained by deleting $k$ from $T$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.cacheCorrect_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#cache-correct-delete).

## Merging separated ordered order-statistic trees preserves order

Let $\alpha$ be a
linearly ordered type and let $L$ and $R$ be ordered order-statistic trees over $\alpha$ such
that $x < y$ for every key $x$ of $L$ and every key $y$ of $R$. Then the merge of $L$ and $R$
is ordered.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.ordered_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#ordered-merge).

## Deletion preserves order in an order-statistic tree

Let $\alpha$ be a linearly ordered
type and let $T$ be an order-statistic tree over $\alpha$ that is ordered, that is, after its
cached sizes are removed, every key in a left subtree is strictly smaller than the key of its node
and every key in a right subtree is strictly larger. Then for every key $k$, the tree obtained
from $T$ by deleting $k$ is again ordered.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.ordered_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#ordered-delete).

## Inorder traversal of an order-statistic merge

For order-statistic trees $A$ and $B$, the
inorder traversal of the merge of $A$ and $B$ is the inorder traversal of $A$ followed by the
inorder traversal of $B$. No ordering between the keys of $A$ and $B$ is assumed.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.inorder_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#inorder-merge).

## Keys of an order-statistic merge

For order-statistic trees $A$ and $B$ over a type $\alpha$
and any $x \in \alpha$, $x$ is a key of the merge of $A$ and $B$ if and only if $x$ is a key of $A$
or a key of $B$. No ordering between the keys of $A$ and $B$ is assumed.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.mem_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#mem-merge).

## Inorder traversal after order-statistic deletion

Let $\alpha$ be a linearly ordered type,
$k \in \alpha$ and $T$ an ordered order-statistic tree over $\alpha$ (at every node, all keys of
the left subtree are smaller and all keys of the right subtree are larger than the node's key).
The inorder traversal of the tree obtained by deleting $k$ from $T$ is the inorder traversal of
$T$ with every occurrence of $k$ removed.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.inorder_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#inorder-delete).

## Keys of an order-statistic tree after deletion

Let $\alpha$ be a linearly ordered type,
$k \in \alpha$ and $T$ an ordered order-statistic tree over $\alpha$ (at every node, all keys of
the left subtree are smaller and all keys of the right subtree are larger than the node's key).
For every $y \in \alpha$, $y$ is a key of the tree obtained by deleting $k$ from $T$ if and only
if $y$ is a key of $T$ and $y \ne k$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.mem_delete_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#mem-delete-iff).

## Deleted key is absent from an order-statistic tree

Let $\alpha$ be a linearly ordered
type, $k \in \alpha$ and $T$ an ordered order-statistic tree over $\alpha$ (at every node, all keys
of the left subtree are smaller and all keys of the right subtree are larger than the node's
key). Then $k$ is not a key of the tree obtained by deleting $k$ from $T$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.not_mem_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#not-mem-delete).

## Search misses a key deleted from an order-statistic tree

Let $\alpha$ be a linearly ordered
type, $k \in \alpha$ and $T$ an ordered order-statistic tree over $\alpha$ (at every node, all keys
of the left subtree are smaller and all keys of the right subtree are larger than the node's
key). Comparison search for $k$ in the tree obtained by deleting $k$ from $T$ returns false.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.contains_delete_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#contains-delete-self).

## Rank after deletion in an order-statistic tree

Let $\alpha$ be a linearly ordered type
and let $T$ be an order-statistic tree over $\alpha$ that is ordered and whose cached subtree
sizes are correct. Let $k$ and $q$ be keys and let $T'$ be the tree obtained from $T$ by
deleting $k$. Then the rank of $q$ in $T'$, computed by navigation with cached sizes, equals the
number of entries strictly smaller than $q$ in the inorder traversal of $T'$ with its cached
sizes removed.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.rank_delete_eq_bstRank`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#rank-delete-eq-bst-rank).

## Selection after deletion in an order-statistic tree

Let $\alpha$ be a linearly ordered
type and let $T$ be an order-statistic tree over $\alpha$ whose cached subtree sizes are correct.
Let $k$ be a key and let $T'$ be the tree obtained from $T$ by deleting $k$. Then for every
natural number $i$, selecting position $i$ in $T'$ by navigation with cached sizes returns the
entry at zero-based position $i$ of the inorder traversal of $T'$ with its cached sizes removed,
and returns nothing when that traversal has at most $i$ entries.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.select_delete_eq_bstSelect`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#select-delete-eq-bst-select).

## Selecting the rank of a surviving key after deletion

Let $\alpha$ be a linearly ordered
type, let $T$ be an order-statistic tree over $\alpha$ that is ordered and whose cached subtree
sizes are correct, let $k$ be a key, and let $T'$ be the tree obtained from $T$ by deleting $k$.
If $y$ is a key of $T'$, then selecting, with cached sizes, the position in $T'$ given by the
cached rank of $y$ in $T'$ returns $y$.

Formalized by `Cslib.Algorithms.Lean.OrderStatisticTree.select_rank_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OrderStatisticTree/Delete.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html#select-rank-delete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Order statistic tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/order-statistic-tree)
