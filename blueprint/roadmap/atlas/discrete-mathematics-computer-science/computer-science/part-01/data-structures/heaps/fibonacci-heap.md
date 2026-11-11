---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.FibonacciTree, Cslib.Algorithms.Lean.FibonacciTree.degree, Cslib.Algorithms.Lean.FibonacciTree.root, Cslib.Algorithms.Lean.FibonacciTree.children, Cslib.Algorithms.Lean.FibonacciTree.elements, Cslib.Algorithms.Lean.FibonacciTree.root_mem_elements, Cslib.Algorithms.Lean.FibonacciTree.card_elements_pos, Cslib.Algorithms.Lean.FibonacciTree.Valid
statement: formalized
proof: formalized
---

# Fibonacci heap

91 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html).

## Fibonacci tree

A Fibonacci tree over a type $\alpha$ is a rose tree: a node carrying a
stored degree $d \in \mathbb{N}$, a root value in $\alpha$, and a finite list of child Fibonacci
trees.

Heap order and the equality of the stored degree with the number of children are not part of
the type; they are imposed by the validity predicate on trees.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#fibonacci-tree).

## Degree of a Fibonacci tree

The degree of the Fibonacci tree with stored degree $d$,
root value $r$ and list of children $c$ is the stored natural number $d$; it is not computed
from the children.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.degree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#degree).

## Root of a Fibonacci tree

The root of a Fibonacci tree is the value stored at its top
node.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.root`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#root).

## Children of a Fibonacci tree

The children of the Fibonacci tree with stored degree $d$,
root value $r$ and list of subtrees $c$ are the trees of the list $c$, in order.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.children`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#children).

## Multiset of a Fibonacci tree

The multiset $M(t)$ of values stored in a Fibonacci tree $t$,
defined recursively: if $t$ has root value $r$ and children $t_1, \dots, t_k$, then
$M(t) = \{r\} + M(t_1) + \cdots + M(t_k)$. The stored degree plays no role.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements).

## The root of a Fibonacci tree is one of its elements

For every Fibonacci tree, its root
value belongs to the multiset of elements the tree represents.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.root_mem_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#root-mem-elements).

## Fibonacci trees are nonempty

Every Fibonacci tree represents at least one element: the
multiset of elements of any Fibonacci tree has positive size.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.card_elements_pos`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#card-elements-pos).

## Valid Fibonacci trees

Let $\alpha$ carry a relation $\le$. A Fibonacci tree with
stored degree $d$, root $r \in \alpha$ and list of children $c$ is valid when every tree in $c$ is
valid, $d$ equals the length of $c$, and $r \le x$ for every element $x$ of the multiset
represented by the tree (the root together with the elements of all children).

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid).

## One-element Fibonacci heap

For a value $x$ of a linearly ordered type, the one-element
Fibonacci heap on $x$ has as its only tree the single-node tree with root $x$, and its cached
minimum is $x$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.singleton`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#singleton).

## Linking two Fibonacci trees

Let $s$ and $t$ be Fibonacci trees over a linearly ordered
type. If the root of $s$ is at most the root of $t$, the link of $s$ and $t$ is the tree with the
root of $s$, stored degree one more than that of $s$, and children $t$ followed by the children
of $s$. Otherwise it is the tree with the root of $t$, stored degree one more than that of $t$,
and children $s$ followed by the children of $t$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.link`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#link).

## Degree of the link of two trees of equal degree

If two Fibonacci trees $s$ and $t$
over a linearly ordered type have the same degree $d$, then their link has degree $d + 1$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.degree_link_of_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#degree-link-of-eq).

## Linking adds the elements

For any two Fibonacci trees $S$ and $T$ over a linearly ordered
type, the tree obtained by linking $S$ and $T$ represents the sum of the multisets represented by
$S$ and by $T$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.elements_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-link).

## Singleton Fibonacci trees are valid

Let $\alpha$ be a linearly ordered type. For every
$v \in \alpha$, the Fibonacci tree of degree $0$ with root $v$ and no children is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.valid_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid-singleton).

## Children of a valid Fibonacci tree are valid

Every child of a valid Fibonacci tree is
itself a valid Fibonacci tree.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.child_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#child-valid).

## The degree of a valid Fibonacci tree is its number of children

For every valid Fibonacci
tree, its stored degree equals the number of its children.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.degree_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#degree-eq).

## Roots of valid Fibonacci trees are lower bounds

The root of a valid Fibonacci tree is no
greater than every element of the multiset the tree represents.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.root_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#root-le).

## The degree of a valid Fibonacci tree is less than its size

For every valid Fibonacci
tree over a type with a relation $\le$, the degree of the tree is strictly less than the
number of elements, counted with multiplicity, of the multiset the tree represents, since
every child contributes at least one element.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.degree_lt_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#degree-lt-card).

## Linking preserves validity of Fibonacci trees

If $s$ and $t$ are valid Fibonacci trees
over a linearly ordered type, then the link of $s$ and $t$ is a valid Fibonacci tree.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#link-2).

## Valid Fibonacci forests

Let $\alpha$ carry a relation $\le$. A Fibonacci forest,
a list of Fibonacci trees with values in $\alpha$, is valid when every tree in it is a valid
Fibonacci tree.

Root degrees may repeat; consolidation is what makes them distinct.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid-2).

## Multiset of a Fibonacci forest

Write $M(t)$ for the multiset of values stored in a
Fibonacci tree $t$. The multiset represented by a Fibonacci forest, a list of Fibonacci trees
$t_1, \dots, t_k$, is the sum $M(t_1) + \cdots + M(t_k)$; the empty forest represents the empty
multiset.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-2).

## Forests with strictly increasing degrees

A Fibonacci forest, a list of Fibonacci trees
$t_1, \dots, t_k$, has sorted degrees when the stored degrees of its trees strictly increase along
the list: $\deg t_i < \deg t_j$ whenever $i < j$.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.SortedDegrees`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#sorted-degrees).

## The empty Fibonacci forest is valid

Let $\alpha$ carry a relation $\le$. The empty
forest, containing no Fibonacci trees with values in $\alpha$, is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.valid_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid-nil).

## Concatenation preserves validity of Fibonacci forests

Let $\alpha$ carry a relation
$\le$. If $F$ and $G$ are valid Fibonacci forests with values in $\alpha$, then the forest
consisting of the trees of $F$ followed by the trees of $G$ is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.valid_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid-append).

## Sublists of valid Fibonacci forests are valid

If a list of Fibonacci trees is a valid
forest, then every sublist of it (a subsequence, not necessarily contiguous) is a valid forest.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.Valid.sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#sublist).

## Elements of a concatenated forest

For any two lists $L$ and $R$ of Fibonacci trees, the
forest made of the trees of $L$ followed by the trees of $R$ represents the sum of the multisets
represented by $L$ and by $R$.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.elements_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-append).

## Minimum root of a forest

The minimum root of a forest of Fibonacci trees over a linearly
ordered type is an optional value: it is absent for the empty forest, and for a nonempty forest
it is the least of the roots of its trees.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.minRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#min-root).

## Minimum of two optional values

For optional values $x$ and $y$ of a linearly ordered
type, their combined minimum is defined as follows: if $x$ and $y$ are both present, with values
$a$ and $b$, it is $\min(a, b)$; if exactly one of $x$ and $y$ is present, it is that value; and
if both are absent, it is absent.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.minOption`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#min-option).

## Only the empty forest has no minimum root

A forest of Fibonacci trees over a linearly
ordered type has no minimum root exactly when it is empty.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.minRoot_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#min-root-eq-none-iff).

## The minimum root is a least root

If a forest $F$ of Fibonacci trees over a linearly
ordered type has minimum root $m$, then $m$ is the root of some tree of $F$ and $m$ is at most
the root of every tree of $F$.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.minRoot_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#min-root-spec).

## Minimum root of a concatenated forest

For forests $F$ and $G$ of Fibonacci trees over a
linearly ordered type, the minimum root of $F$ followed by $G$ is the combined minimum of the
optional minimum roots of $F$ and of $G$: their minimum if both exist, the one that exists if
only one does, and absent if neither does.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.minRoot_append`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#min-root-append).

## Inserting a tree into a forest

Given a Fibonacci tree $t$ and a list of Fibonacci
trees, the insertion of $t$ into the list is defined recursively. Inserting $t$ into the empty
list gives the one-tree list $[t]$. For a list with first tree $s$ and remaining list $L$: if
the stored degree of $t$ is less than the stored degree of $s$, the result is $t$ followed by
$s$ and then $L$; if the two stored degrees are equal, the result is the insertion of the link
of $t$ and $s$ into $L$; otherwise the result is $s$ followed by the insertion of $t$ into $L$.

On a list whose stored degrees strictly increase, this links $t$ with any tree of equal degree
and carries the linked tree forward, as in binary addition.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.addTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#add-tree).

## Consolidation of a forest

The consolidation of a list of Fibonacci trees is defined
recursively: the consolidation of the empty list is the empty list, and the consolidation of a
list with first tree $t$ and remaining list $L$ is the insertion of $t$ into the consolidation
of $L$.

Each insertion links trees of equal stored degree as in binary addition, so the result has
strictly increasing, hence distinct, stored root degrees, as in the consolidate step of CLRS.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.consolidate`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#consolidate).

## Consolidation preserves the elements

For every list of Fibonacci trees over a linearly
ordered type, its consolidation represents the same multiset as the original list.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.elements_consolidate`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-consolidate).

## Consolidation preserves validity

Let $\alpha$ be a linearly ordered type. If a
Fibonacci forest with values in $\alpha$ is valid, then its consolidation is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.valid_consolidate`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#valid-consolidate).

## Consolidation sorts root degrees

For every list of Fibonacci trees, the stored degrees
of the trees in its consolidation are strictly increasing in list order.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.consolidate_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#consolidate-sorted).

## Consolidation yields distinct root degrees

For every list of Fibonacci trees, the trees
in its consolidation have pairwise distinct stored degrees.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.consolidate_degrees_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#consolidate-degrees-nodup).

## Degree-sorted forests have at most as many trees as elements

Let $F$ be a valid forest
of Fibonacci trees whose degrees are strictly increasing along the list. Then the number of
trees in $F$ is at most the number of elements, counted with multiplicity, that $F$ represents.

Every degree is smaller than the total element count and the degrees are distinct.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.length_le_card_of_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#length-le-card-of-sorted).

## Removing a minimum tree from a Fibonacci forest

For a list of Fibonacci trees over a
linearly ordered type, this returns nothing on the empty list. Otherwise it returns the first tree
whose root is minimal among all roots in the list, so earlier trees win ties, together with the list
of the remaining trees in their original order.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.removeMinTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#remove-min-tree).

## Minimum-tree removal in a Fibonacci forest

Let $T$ be a list of Fibonacci trees over a
linearly ordered type. If removing a minimum tree from $T$ returns a tree $m$ and a list $R$, then
the multiset of elements of $m$ plus the multiset of elements of $R$ equals the multiset of elements
of $T$, the tree $m$ belongs to $T$, the list $R$ is a sublist of $T$, and the root of $m$ is at
most the root of every tree in $T$.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.removeMinTree_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#remove-min-tree-spec).

## Fibonacci heap

A Fibonacci min-heap over a linearly ordered type consists of a list of
Fibonacci trees, each valid (heap-ordered, and at every node the stored degree equals the number
of children), together with a cached minimum equal to the least root value of these trees,
absent when the list is empty.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#fibonacci-heap).

## Multiset of a Fibonacci heap

The multiset represented by a Fibonacci heap over a linearly
ordered type is the multiset of its list of trees: the sum, over the trees in the list, of the
multisets of values stored in them. The cached minimum plays no role.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-3).

## Empty Fibonacci heap

The Fibonacci heap over a linearly ordered type whose list of trees
is empty and whose cached minimum is absent.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#empty).

## Singleton Fibonacci heap

For a value $x$ of a linearly ordered type, the singleton
Fibonacci heap on $x$ has as its only tree the single-node tree with root $x$, stored degree $0$
and no children, and its cached minimum is $x$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.singleton`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#singleton-2).

## Melding Fibonacci heaps

The meld of Fibonacci heaps $H_1$ and $H_2$ is the Fibonacci heap
whose root list is the root list of $H_1$ followed by that of $H_2$, and whose cached minimum is
the smaller of the two cached minima when both heaps have one, and otherwise the cached minimum
of whichever heap has one (none if neither does).

No linking happens until the next minimum deletion.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.meld`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#meld).

## Union of Fibonacci heaps

The union of Fibonacci heaps $H_1$ and $H_2$ is their meld: the
heap whose trees are those of $H_1$ followed by those of $H_2$, and whose cached minimum is the
smaller of the two cached minima (the one that exists if a heap is empty, none if both are).

CLRS calls this operation union.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.union`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#union).

## Insertion into a Fibonacci heap

Inserting a value $x$ into a Fibonacci heap $H$ gives
the meld of the one-element Fibonacci heap containing $x$ with $H$, the one-element heap coming
first.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#insert).

## Find-min for Fibonacci heaps

Find-min on a Fibonacci heap returns its cached minimum
without modifying the heap: the least root value of its trees, or no value when the heap has no
trees.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.findMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#find-min).

## Minimum deletion on a forest

Given a list of Fibonacci trees over a linearly ordered type,
the result is nothing if the list is empty. Otherwise the first tree whose root is minimal is
removed, and the result is its root value together with the consolidation of the forest made of
the removed tree's children followed by the remaining trees.

This is the forest-level computation behind deleting the minimum of a Fibonacci heap, without the
validity proofs.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMinTrees`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-trees).

## Deleting the minimum of a Fibonacci heap

If the root list of the heap is empty, the result
is nothing. Otherwise the first tree of the root list whose root is minimal is removed, and the
result is its root value together with the heap whose root list is the consolidation of the
removed tree's children followed by the remaining trees, and whose cached minimum is the minimum
root of this consolidated forest.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min).

## Fibonacci heap minimum deletion agrees with its root-list version

For every Fibonacci
heap $H$, deleting the minimum of $H$ and keeping only the returned value and the root list
of the resulting heap gives the same result as the root-list minimum deletion applied to the
root list of $H$: either both fail, or both return the same value and the same list of
trees.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_trees`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-trees-2).

## The empty Fibonacci heap has no elements

The empty Fibonacci heap represents the empty
multiset.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-empty).

## Multiset of a singleton Fibonacci heap

For every value $x$ of a linearly ordered type, the
singleton Fibonacci heap on $x$, whose only tree is the single-node tree with root $x$, represents
the multiset $\{x\}$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 735](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-singleton).

## Melding adds the elements

For any two Fibonacci heaps $H_1$ and $H_2$ over a linearly
ordered type, the meld of $H_1$ and $H_2$ represents the sum of the multisets represented by
$H_1$ and by $H_2$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements_meld`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-meld).

## The union of Fibonacci heaps adds their multisets

For Fibonacci heaps $H_1$ and $H_2$ over
a linearly ordered type, the multiset represented by the union of $H_1$ and $H_2$ is the sum of
the multisets represented by $H_1$ and by $H_2$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements_union`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-union).

## Insertion adds one occurrence

For every Fibonacci heap $H$ over a linearly ordered type
and every value $x$, the heap obtained by inserting $x$ into $H$ represents the multiset of $H$
with one more occurrence of $x$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.elements_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 751](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L751). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-insert).

## Melding adds the sizes of Fibonacci heaps

For Fibonacci heaps $H_1$ and $H_2$, the number
of elements of the meld of $H_1$ and $H_2$, counted with multiplicity, is the number of
elements of $H_1$ plus the number of elements of $H_2$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.card_elements_meld`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#card-elements-meld).

## Insertion increases the size of a Fibonacci heap by one

For every Fibonacci heap $H$
and every value $x$, the number of elements of the heap obtained by inserting $x$ into $H$,
counted with multiplicity, is the number of elements of $H$ plus one.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.card_elements_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#card-elements-insert).

## Find-min fails exactly on the empty Fibonacci heap

For a Fibonacci heap $H$ over a
linearly ordered type, find-min on $H$ returns no value if and only if $H$ has no trees.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.findMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#find-min-eq-none-iff).

## Find-min returns an element of the Fibonacci heap

Let $H$ be a Fibonacci heap over a
linearly ordered type. If find-min on $H$ returns $m$, then $m$ belongs to the multiset
represented by $H$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.findMin_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#find-min-mem).

## Find-min returns a lower bound of the Fibonacci heap

Let $H$ be a Fibonacci heap over a
linearly ordered type. If find-min on $H$ returns $m$, then $m \le v$ for every value $v$ in the
multiset represented by $H$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.findMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 787](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L787). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#find-min-le).

## Fibonacci heap minimum deletion fails exactly on the empty heap

Deleting the minimum
of a Fibonacci heap fails if and only if the heap's list of root trees is empty.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-eq-none-iff).

## Fibonacci heap minimum deletion removes one copy of the minimum

If deleting the
minimum of a Fibonacci heap $H$ succeeds and returns the value $m$ and the heap $H'$, then the
multiset of elements of $H'$ is the multiset of elements of $H$ with one occurrence of $m$
removed.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-elements).

## Fibonacci heap minimum deletion splits off the minimum

If deleting the minimum of a
Fibonacci heap $H$ succeeds and returns the value $m$ and the heap $H'$, then the multiset of
elements of $H$ is the multiset of elements of $H'$ with one copy of $m$ added.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_cons_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 840](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L840). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-cons-elements).

## Fibonacci heap minimum deletion returns a lower bound

If deleting the minimum of a
Fibonacci heap $H$ succeeds and returns the value $m$, then $m \le v$ for every element $v$
of $H$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 847](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L847). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-le).

## Minimum deletion leaves a Fibonacci heap with strictly increasing root degrees

If
deleting the minimum of a Fibonacci heap succeeds and returns the heap $H'$, then the degrees
of the root trees of $H'$, in list order, are strictly increasing; consolidation is what
makes them so.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_sortedDegrees`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-sorted-degrees).

## After minimum deletion a Fibonacci heap has at most as many roots as elements

If
deleting the minimum of a Fibonacci heap succeeds and returns the heap $H'$, then the number
of root trees of $H'$ is at most the number of elements of $H'$, counted with multiplicity.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.deleteMin_length_le_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean, line 873](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap.lean#L873). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#delete-min-length-le-card).

## Subtree of a Fibonacci tree at a path

For a list $p = (i_1, \dots, i_n)$ of natural
numbers and a Fibonacci tree $t$, the subtree of $t$ at $p$ is found by starting at the root and
moving to the child with zero-based index $i_1$, then to its child with index $i_2$, and so on.
The result is absent when some index is at least the number of children of the current node.
The empty path addresses the whole tree $t$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.subtreeAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#subtree-at).

## Cutting a subtree out of a Fibonacci tree

For a path $p$ of child indices and a Fibonacci
tree $t$, the cut of $t$ at $p$ is either undefined or a pair of an extracted subtree and an
optional remainder tree. For the empty path, the extracted subtree is $t$ and there is no
remainder. For a path consisting of an index $i$ followed by a path $q$, where $t$ has root $r$
and children $c_0, \dots, c_{k-1}$, the cut is undefined if $i \ge k$ or if the cut of $c_i$
at $q$ is undefined. Otherwise, with $s$ the subtree extracted from $c_i$, the extracted
subtree is $s$ and the remainder is the tree with root $r$ whose children are those of $t$
with $c_i$ removed (if the cut of $c_i$ left no remainder) or with $c_i$ replaced by that
remainder (otherwise), and whose stored degree is its new number of children.

When the cut is defined, there is no remainder exactly when $p$ is empty.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at).

## Replacing the root key of a Fibonacci tree

For a Fibonacci tree $t$ and a key $k$, this
is the tree whose root value is $k$ and whose stored degree and list of children are those of $t$.

It is used on an extracted subtree with a key no larger than the old root.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.decreaseRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-root).

## Elements after replacing the root key

For a Fibonacci tree $t$ and any key $k$, the
multiset of elements represented by the tree obtained from $t$ by replacing its root value with $k$
equals the multiset of elements of $t$ with one occurrence of the root of $t$ removed and $k$
added.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.elements_decreaseRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#elements-decrease-root).

## Lowering the root keeps a Fibonacci tree valid

Let $T$ be a valid Fibonacci tree over a
preordered type and let $k$ be a key that is at most the root of $T$. Then the tree obtained
from $T$ by replacing its root by $k$, keeping its degree and children, is valid: the new root
is still no greater than every represented element.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.decreaseRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-root-2).

## Subtrees of a valid Fibonacci tree are valid

If a Fibonacci tree $t$ is valid and a path
$p$ of child indices addresses a subtree $s$ of $t$, then $s$ is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.Valid.subtreeAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#subtree-at-2).

## A cut extracts the addressed subtree

Let $t$ be a Fibonacci tree and $p$ a path of
child indices. If cutting $t$ at $p$ extracts a subtree $s$ (with or without a remainder),
then $s$ is the subtree of $t$ at $p$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt_subtreeAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at-subtree-at).

## Every addressed subtree can be cut out

If a path $p$ of child indices addresses a subtree
$s$ of a Fibonacci tree $t$, then cutting $t$ at $p$ succeeds and extracts exactly $s$, together
with some remainder, which may be absent.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.subtreeAt_cutAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#subtree-at-cut-at).

## A cut without remainder extracts the whole tree

Let $t$ be a Fibonacci tree and $p$ a
path of child indices. If cutting $t$ at $p$ extracts a subtree $s$ and leaves no remainder,
then $s = t$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt_eq_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at-eq-self).

## Cutting a subtree splits the elements of a Fibonacci tree

Let $t$ be a Fibonacci tree
and $p$ a path of child indices. If cutting $t$ at $p$ extracts a subtree $s$ and leaves a
remainder tree $t'$, then the multiset of elements of $t$ is the sum of the multisets of
elements of $t'$ and of $s$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at-elements).

## The subtree extracted by a cut from a valid tree is valid

Let $t$ be a valid Fibonacci
tree over a type with a relation $\le$, and $p$ a path of child indices. If cutting $t$ at $p$
extracts a subtree $s$ (with or without a remainder), then $s$ is valid.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt_sub_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at-sub-valid).

## The remainder of a cut from a valid tree is valid

Let $t$ be a valid Fibonacci tree
over a type with a relation $\le$, and $p$ a path of child indices. If cutting $t$ at $p$
extracts a subtree and leaves a remainder tree $t'$, then $t'$ is valid: its children are
valid, its stored degree equals its number of children, and its root is $\le$ every element
of $t'$.

Formalized by `Cslib.Algorithms.Lean.FibonacciTree.cutAt_remainder_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-at-remainder-valid).

## Cutting a subtree out of a Fibonacci forest

For a forest given as a list of Fibonacci
trees, an index $i$ and a path $p$ of child indices, the cut is undefined if the list has no
tree at position $i$ (counting from $0$) or if cutting that tree $t$ at $p$ is undefined.
Otherwise, if cutting $t$ at $p$ extracts the subtree $s$, the result is $s$ together with the
list in which the tree at position $i$ is removed (if the cut of $t$ left no remainder) or
replaced by the remainder (otherwise).

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.cutTreeAt`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-tree-at).

## Cutting a subtree splits the elements of a Fibonacci forest

Let $F$ be a forest of
Fibonacci trees, $i$ an index and $p$ a path of child indices. If cutting $F$ at the $i$-th tree
and path $p$ extracts a subtree $s$ and leaves the forest $F'$, then the multiset of elements
of $F$ is the sum of the multisets of elements of $F'$ and of $s$.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.cutTreeAt_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-tree-at-elements).

## Cutting a valid forest leaves valid parts

Let $F$ be a valid forest of Fibonacci trees
over a type with a relation $\le$, $i$ an index and $p$ a path of child indices. If cutting $F$
at index $i$ and path $p$ extracts a subtree $s$ and leaves the forest $F'$, then $s$ is a valid
tree and $F'$ is a valid forest.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.cutTreeAt_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-tree-at-valid).

## Every addressed subtree of a forest can be cut out

Let $F$ be a forest of Fibonacci
trees whose tree at position $i$ is $t$, and let $p$ be a path of child indices such that the
subtree of $t$ at $p$ is $s$. Then cutting $F$ at index $i$ and path $p$ is defined and extracts
$s$, together with some remaining forest.

Formalized by `Cslib.Algorithms.Lean.FibonacciForest.cutTreeAt_of_subtreeAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#cut-tree-at-of-subtree-at).

## Decrease-key in a Fibonacci heap

Given a Fibonacci heap $H$ over a linearly ordered type,
a root index $i$, a path $p$ of child indices and a key $k$, decrease-key cuts the subtree $S$ at
path $p$ out of the $i$-th tree of the root list of $H$, replaces the root of $S$ by $k$, and
puts the resulting tree in front of the remaining forest (the root list with the $i$-th tree
replaced by what is left of it after the cut, or removed when $S$ is that whole tree). The
cached minimum of the result is the smaller of $k$ and the previous cached minimum, computed
without rescanning the root list. When the cut fails (the address does not resolve) or $k$ is
greater than the root of $S$, the heap $H$ is returned unchanged.

Unlike CLRS decrease-key, this performs no cascading cuts: the trees carry no mark field.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key).

## Root list after decrease-key

Let $H$ be a Fibonacci heap, $i$ a root index, $p$ a path of
child indices and $k$ a key. Suppose that cutting the subtree at path $p$ out of the $i$-th tree
of the root list of $H$ succeeds, extracting the subtree $S$ and leaving the forest $R$, and that
$k$ is at most the root of $S$. Then the root list of the heap obtained from $H$ by decreasing
the key at root index $i$ and path $p$ to $k$ consists of $S$ with its root replaced by $k$,
followed by the trees of $R$ in order.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_trees_of_cut`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-trees-of-cut).

## Decrease-key at an unresolved address does nothing

Let $H$ be a Fibonacci heap, $i$ a
root index and $p$ a path of child indices. If cutting the subtree at path $p$ out of the $i$-th
tree of the root list of $H$ fails, then for every key $k$, decreasing the key at root index $i$
and path $p$ to $k$ returns $H$ unchanged.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_eq_self_of_cut_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-eq-self-of-cut-none).

## Decrease-key with a larger key does nothing

Let $H$ be a Fibonacci heap, $i$ a root index,
$p$ a path of child indices and $k$ a key. Suppose that cutting the subtree at path $p$ out of
the $i$-th tree of the root list of $H$ succeeds and extracts the subtree $S$, and that $k$ is
not at most the root of $S$ (keys are linearly ordered, so $k$ is greater than that root). Then
decreasing the key at root index $i$ and path $p$ to $k$ returns $H$ unchanged.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_eq_self_of_not_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-eq-self-of-not-le).

## Decrease-key replaces one key

Let $H$ be a Fibonacci heap, $i$ a root index, $p$ a path
of child indices and $k$ a key. Suppose that cutting the subtree at path $p$ out of the $i$-th
tree of the root list of $H$ succeeds and extracts the subtree $S$, and that $k$ is at most the
root of $S$. Then the multiset represented by the heap obtained from $H$ by decreasing the key at
root index $i$ and path $p$ to $k$ is the multiset represented by $H$ with one occurrence of the
root of $S$ removed and one occurrence of $k$ added.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-elements).

## Decrease-key replaces one key, stated by address

Let $H$ be a Fibonacci heap, let $T$ be
the $i$-th tree of its root list, and let $S$ be the subtree of $T$ at the path $p$ of child
indices. If the key $k$ is at most the root of $S$, then the multiset represented by the heap
obtained from $H$ by decreasing the key at root index $i$ and path $p$ to $k$ is the multiset
represented by $H$ with one occurrence of the root of $S$ removed and one occurrence of $k$
added.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_elements_of_subtreeAt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-elements-of-subtree-at).

## Decrease-key preserves the number of elements

Let $H$ be a Fibonacci heap, $i$ a root
index, $p$ a path of child indices and $k$ a key. Suppose that cutting the subtree at path $p$
out of the $i$-th tree of the root list of $H$ succeeds and extracts the subtree $S$, and that
$k$ is at most the root of $S$. Then the multiset represented by the heap obtained from $H$ by
decreasing the key at root index $i$ and path $p$ to $k$ has the same number of elements,
counted with multiplicity, as the multiset represented by $H$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_card_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 652](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L652). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-card-elements).

## Minimum after decrease-key

Let $H$ be a Fibonacci heap whose minimum, as returned by
find-min, is $m$, and let $i$ be a root index, $p$ a path of child indices and $k$ a key. Suppose
that cutting the subtree at path $p$ out of the $i$-th tree of the root list of $H$ succeeds and
extracts the subtree $S$, and that $k$ is at most the root of $S$. Then find-min on the heap
obtained from $H$ by decreasing the key at root index $i$ and path $p$ to $k$ returns
$\min(k, m)$.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_findMin`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-find-min).

## Decrease-key yields a valid forest

For every Fibonacci heap $H$, root index $i$, path $p$
of child indices and key $k$, the root list of the heap obtained from $H$ by decreasing the key
at root index $i$ and path $p$ to $k$ is a valid forest, that is, every tree in it is valid.

This holds by construction: every Fibonacci heap carries a valid forest.

Formalized by `Cslib.Algorithms.Lean.FibonacciHeap.decreaseKey_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/FibonacciHeap/DecreaseKey.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html#decrease-key-valid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci heap](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/heaps/fibonacci-heap)
