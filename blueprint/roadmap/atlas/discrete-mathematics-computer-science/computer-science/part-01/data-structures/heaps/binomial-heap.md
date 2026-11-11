---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BinomialTree, Cslib.Algorithms.Lean.BinomialTree.rank, Cslib.Algorithms.Lean.BinomialTree.root, Cslib.Algorithms.Lean.BinomialTree.children, Cslib.Algorithms.Lean.BinomialTree.elements, Cslib.Algorithms.Lean.BinomialTree.root_mem_elements, Cslib.Algorithms.Lean.BinomialTree.Valid, Cslib.Algorithms.Lean.BinomialTree.singleton
statement: formalized
proof: formalized
---

# Binomial heap

53 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html).

## Binomial Tree

## Binomial tree

A binomial tree over a type $\alpha$ is a node that stores a rank, which is
a natural number, a root value in $\alpha$, and a list of binomial trees over $\alpha$ as its
children. The type imposes no invariant; the binomial-tree shape and heap order are expressed
by a separate validity predicate.

Formalized by `Cslib.Algorithms.Lean.BinomialTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#binomial-tree).

## Rank of a binomial tree

The rank of a binomial tree is the natural number stored at its
root node.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.rank`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#rank).

## Root of a binomial tree

The root of the binomial tree with rank $r$, root value $a$ and
list of children $c$ is $a$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.root`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#root).

## Children of a binomial tree

The children of a binomial tree are the binomial trees in
the list stored at its root node, in their stored order.

The list carries no ordering constraint in general; in a valid binomial tree of rank $r$ the
children have ranks $r - 1, \dots, 0$ in that order.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.children`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#children).

## Elements of a binomial tree

The multiset of elements of a binomial tree with root value
$x$ and children $t_1, \dots, t_k$ is defined recursively as $\{x\}$ added to the multiset sum of
the multisets of elements of $t_1, \dots, t_k$; the stored rank plays no role.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements).

## The root of a binomial tree is one of its elements

For every binomial tree $t$, the root
of $t$ occurs in the multiset represented by $t$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.root_mem_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#root-mem-elements).

## Valid binomial tree

For a type $\alpha$ with a relation $\le$, validity of binomial
trees over $\alpha$ is defined inductively: the tree with stored rank $r$, root $a$ and list of
children $c_1, \dots, c_k$ is valid when every child $c_i$ is valid, the ranks of
$c_1, \dots, c_k$ are exactly $r - 1, r - 2, \dots, 0$ in this order, the multiset of elements
of the tree (its root together with the elements of all its children) has exactly $2^r$
members counted with multiplicity, and $a \le x$ for every element $x$ of the tree.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#valid).

## Singleton binomial heap

For a value $a$ in a linear order, the binomial heap whose list of
trees consists of exactly one tree: the tree of rank $0$ with root $a$ and no children.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.singleton`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#singleton).

## Linking two binomial trees

Over a linear order, the link of binomial trees $s$ and $t$
is defined as follows. If the root of $s$ is at most the root of $t$, it is the tree whose rank
is one more than the rank of $s$, whose root is the root of $s$, and whose children are $t$
followed by the children of $s$. Otherwise it is the tree whose rank is one more than the rank
of $s$, whose root is the root of $t$, and whose children are $s$ followed by the children of
$t$. In particular, the root of $s$ is kept when the two roots are equal.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.link`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#link).

## Linking binomial trees adds their elements

For any two binomial trees $s$ and $t$ over a
linearly ordered type, the multiset of elements of the tree obtained by linking $s$ and $t$ is
the sum of the multisets of elements of $s$ and $t$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.elements_link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-link).

## Singleton binomial trees are valid

For a linearly ordered type $\alpha$ and any
$a \in \alpha$, the singleton binomial tree with rank $0$, root $a$ and no children is valid.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.valid_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#valid-singleton).

## Children of a valid binomial tree are valid

For a type $\alpha$ with a relation $\le$,
every child of a valid binomial tree over $\alpha$ is itself a valid binomial tree.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.child_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#child-valid).

## Child ranks of a valid binomial tree

For a type $\alpha$ with a relation $\le$, if a
valid binomial tree over $\alpha$ has rank $r$, then the ranks of its children, listed in their
stored order, are $r - 1, r - 2, \dots, 1, 0$; there are no children when $r = 0$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.children_ranks`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#children-ranks).

## Size of a valid binomial tree

For a type $\alpha$ with a relation $\le$, every valid
binomial tree of rank $r$ over $\alpha$ represents a multiset of exactly $2^r$ elements, counted
with multiplicity.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.card_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#card-elements).

## The rank of a valid binomial tree is logarithmic

A valid binomial tree of rank $r$
holding $n$ elements, counted with multiplicity, satisfies $r \le \lfloor \log_2 n \rfloor$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.rank_le_log2_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#rank-le-log2-card).

## The root of a valid binomial tree is a lower bound

For a type $\alpha$ with a relation
$\le$ and a valid binomial tree $t$ over $\alpha$, the root $a$ of $t$ satisfies $a \le v$ for
every element $v$ of the multiset represented by $t$.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.root_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#root-le).

## Linking preserves binomial-tree validity

If $s$ and $t$ are valid binomial trees
of equal rank, then the tree obtained by linking $s$ with $t$ is valid.

Formalized by `Cslib.Algorithms.Lean.BinomialTree.Valid.link`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#link-2).

## Valid binomial forest

For a type $\alpha$ with a relation $\le$, a list of binomial trees
over $\alpha$ is a valid forest when every tree in it is a valid binomial tree and the ranks of its
trees are strictly increasing along the list.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#valid-2).

## Elements of a binomial forest

The multiset of elements of a list of binomial trees
$t_1, \dots, t_k$ is the multiset sum of the multisets of elements of $t_1, \dots, t_k$; for the
empty list it is the empty multiset.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-2).

## Rank lower bound for a forest

For a natural number $r$, a list of binomial trees has
ranks at least $r$ when every tree in it has rank at least $r$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.RanksAtLeast`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#ranks-at-least).

## The empty forest is valid

For every type $\alpha$ with a relation $\le$, the empty list of
binomial trees over $\alpha$ is a valid binomial forest.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.valid_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#valid-nil).

## Validity of binomial forests passes to sublists

For a type $\alpha$ with a relation $\le$
and lists $L$, $R$ of binomial trees over $\alpha$, if $L$ is a sublist of $R$ (obtained by
deleting entries while keeping the order of the rest) and $R$ is a valid forest, then $L$ is a valid
forest.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.Valid.sublist`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#sublist).

## Tree ranks in a valid forest are logarithmic

If $F$ is a valid binomial forest and $T$
is a tree of $F$ of rank $r$, then $r \le \lfloor \log_2 n \rfloor$, where $n$ is the number of
elements, counted with multiplicity, represented by $F$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.Valid.member_rank_le_log2_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#member-rank-le-log2-card).

## A valid binomial forest has logarithmically many trees

Let $\alpha$ be a type with a
relation $\le$. If a valid binomial forest over $\alpha$ has $n$ elements, counted with
multiplicity, then it consists of at most $\lfloor \log_2 n \rfloor + 1$ trees, where
$\lfloor \log_2 0 \rfloor$ is taken to be $0$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.Valid.length_le_log2_card_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#length-le-log2-card-succ).

## A valid binomial forest with no elements has no trees

Let $\alpha$ be a type with a
relation $\le$. If a list of binomial trees over $\alpha$ is a valid binomial forest and its
multiset of elements has cardinality $0$, then the list has length $0$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.Valid.length_eq_zero_of_card_eq_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#length-eq-zero-of-card-eq-zero).

## Carry insertion into a binomial forest

For a linearly ordered type, the carry of a
binomial tree $t$ into a list $F$ of binomial trees is defined by recursion on $F$. If $F$ is
empty, the result is the one-tree list $[t]$. If $F$ starts with a tree $u$ followed by a list
$F'$ and the rank of $t$ is less than the rank of $u$, the result is $F$ with $t$ prepended.
Otherwise the result is the carry of the link of $t$ and $u$ into $F'$.

It is meant for a tree whose rank is no greater than every rank in the forest, where linking
equal-rank trees propagates like a binary carry.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.carry`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#carry).

## Melding binomial forests

Over a linear order, the meld of two lists of binomial trees
is defined by recursion on their total length. For every list $L$, the meld of the empty list
with $L$ is $L$, and the meld of $L$ with the empty list is $L$. For nonempty lists with first
trees $s$ and $t$ and remaining lists $F$ and $G$: if the rank of $s$ is less than the rank of
$t$, the meld is $s$ followed by the meld of $F$ with the second list; if the rank of $t$ is less
than the rank of $s$, it is $t$ followed by the meld of the first list with $G$; and if the ranks
are equal, it is the result of carrying the link of $s$ with $t$ into the meld of $F$ and $G$.

It is intended for forests of strictly increasing ranks, where equal-rank trees are linked and
the carries are propagated.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.meldTrees`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#meld-trees).

## Melding binomial forests adds their elements

For any two lists $L$ and $R$ of binomial
trees over a linearly ordered type, the multiset of elements of the meld of $L$ and $R$ is the
sum of the multisets of elements of $L$ and $R$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.elements_meldTrees`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-meld-trees).

## Melding preserves forest validity and rank lower bounds

Let $r$ be a natural number
and let $F$ and $G$ be valid binomial forests in which every tree has rank at least $r$. Then
the meld of $F$ and $G$ is a valid binomial forest in which every tree has rank at least $r$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.meldTrees_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#meld-trees-correct).

## Removing a minimum-root tree from a forest

For a list $T$ of binomial trees over a linear
order, the result is nothing when $T$ is empty. Otherwise it is the first tree $m$ of $T$ whose root
is minimal among the roots of the trees of $T$, together with the list obtained from $T$ by
deleting that occurrence of $m$, the remaining trees keeping their order.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.removeMinTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#remove-min-tree).

## Removing a minimum-root tree

Let $T$ be a list of binomial trees over a linear order, and
suppose that removing a minimum tree from $T$ returns the tree $m$ and the list $R$. Then the
multiset represented by $m$ plus the multiset represented by the forest $R$ equals the multiset
represented by the forest $T$; $m$ is a member of $T$; $R$ is a sublist of $T$; and the root of
$m$ is at most the root of every tree in $T$.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.removeMinTree_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#remove-min-tree-spec).

## Reversed children of a valid binomial tree form a valid forest

For a linearly ordered
type $\alpha$ and a valid binomial tree $t$ over $\alpha$, the children of $t$ listed in reverse
order form a valid binomial forest: every tree in the list is valid and the ranks strictly
increase along the list.

Formalized by `Cslib.Algorithms.Lean.BinomialForest.valid_reverse_children`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#valid-reverse-children).

## Binomial heap

A binomial min-heap over a linearly ordered type $\alpha$ consists of a
list of binomial trees over $\alpha$ together with a proof that this list is a valid binomial
forest: every tree in it is a valid binomial tree and the tree ranks are strictly increasing
along the list.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#binomial-heap).

## Elements of a binomial heap

Over a linearly ordered type, the multiset of elements of a
binomial heap is the multiset of elements of its list of binomial trees, that is, the multiset sum
of the multisets of elements of its trees.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.elements`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-3).

## Tree ranks in a binomial heap are logarithmic

Every tree in a binomial heap holding $n$
elements, counted with multiplicity, has rank at most $\lfloor \log_2 n \rfloor$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.rank_le_log2_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#rank-le-log2-card-2).

## A binomial heap has logarithmically many trees

If a binomial heap over a linearly ordered
type has $n$ elements, counted with multiplicity, then its number of trees is at most
$\lfloor \log_2 n \rfloor + 1$, where $\lfloor \log_2 0 \rfloor$ is taken to be $0$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.length_le_log2_card_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#length-le-log2-card-succ-2).

## Empty binomial heap

For a linearly ordered type $\alpha$, the empty binomial heap over
$\alpha$ is the binomial heap whose list of trees is empty.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 709](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#empty).

## Melding binomial heaps

Over a linear order, the meld of two binomial heaps is the
binomial heap whose forest is the meld of the forests of the two heaps.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.meld`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#meld).

## One-element binomial heap

For a value $a$ in a linearly ordered type $\alpha$, the
one-element binomial heap of $a$ is the binomial heap whose list of trees consists of exactly one
tree: the binomial tree of rank $0$ with root $a$ and no children.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.singleton`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#singleton-2).

## Insertion into a binomial heap

Inserting a value $x$ into a binomial heap $H$ over a
linearly ordered type gives the meld of the one-element binomial heap containing $x$ with $H$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#insert).

## Minimum of a binomial heap

The minimum lookup of a binomial heap over a linearly ordered
type returns no value when the heap has no trees, and otherwise returns the least of the root
values of its trees, leaving the heap unchanged.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.findMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#find-min).

## Minimum deletion on a binomial forest

Given a list of binomial trees over a linearly
ordered type, if the list is empty there is no result. Otherwise, remove the first tree whose root
is minimal among the roots of the list; the result is the root of that tree together with the
forest obtained by melding its children, in reversed order, with the remaining trees.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMinTrees`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 735](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-trees).

## Deleting the minimum of a binomial heap

If the binomial heap $H$ has no trees, there is no
result. Otherwise, remove from the list of trees of $H$ the first tree whose root is minimal; the
result is that root together with the binomial heap whose list of trees is obtained by melding
the children of the removed tree, in reversed order, with the remaining trees.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min).

## Binomial heap deletion agrees with forest deletion

For every binomial heap $H$ over a
linearly ordered type, deleting the minimum of $H$ and then replacing the remaining heap by its
list of trees gives the same result as minimum deletion on the list of trees of $H$: both have no
result, or both return the same minimum value and the same list of trees.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin_trees`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-trees-2).

## Melding binomial heaps adds their elements

For any two binomial heaps $H_1$ and $H_2$ over
a linearly ordered type, the multiset of elements of the meld of $H_1$ and $H_2$ is the sum of
the multisets of elements of $H_1$ and $H_2$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.elements_meld`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-meld).

## Insertion into a binomial heap adds one occurrence

For every binomial heap $H$ over a
linearly ordered type and every value $v$, the multiset of elements of the heap obtained by
inserting $v$ into $H$ is the multiset of elements of $H$ with one more occurrence of $v$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.elements_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#elements-insert).

## The minimum lookup fails exactly on the empty binomial heap

For a binomial heap $H$ over a
linearly ordered type, the minimum lookup of $H$ returns no value if and only if the list of
trees of $H$ is empty.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.findMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#find-min-eq-none-iff).

## The minimum lookup of a binomial heap returns one of its elements

Let $H$ be a binomial
heap over a linearly ordered type. If the minimum lookup of $H$ returns $m$, then $m$ is an
element of $H$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.findMin_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#find-min-mem).

## The minimum lookup of a binomial heap returns a lower bound

Let $H$ be a binomial heap over
a linearly ordered type. If the minimum lookup of $H$ returns $m$, then $m \le v$ for every
element $v$ of $H$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.findMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#find-min-le).

## Deleting the minimum fails only on the empty binomial heap

For a binomial heap $H$ over a
linearly ordered type, deleting the minimum of $H$ returns no result if and only if the list of
trees of $H$ is empty.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 830](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L830). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-eq-none-iff).

## Deleting the minimum of a binomial heap removes one occurrence

For a binomial heap $H$
over a linearly ordered type, if deleting the minimum of $H$ succeeds and returns a value $m$
and a heap $H'$, then the multiset of elements of $H'$ is the multiset of elements of $H$ with
one occurrence of $m$ removed.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-elements).

## Deleting the minimum of a binomial heap splits its multiset

For a binomial heap $H$ over
a linearly ordered type, if deleting the minimum of $H$ succeeds and returns a value $m$ and a
heap $H'$, then the multiset of elements of $H$ equals the multiset of elements of $H'$ with one
more occurrence of $m$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin_cons_elements`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-cons-elements).

## The value deleted from a binomial heap is a lower bound for its elements

If deleting the
minimum of a binomial heap $H$ over a linearly ordered type succeeds and returns a value $m$
together with a remaining heap, then $m \le v$ for every value $v$ in the multiset of elements of
$H$.

Formalized by `Cslib.Algorithms.Lean.BinomialHeap.deleteMin_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinomialHeap.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html#delete-min-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial heap](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/binomial-heap/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/heaps/binomial-heap)
