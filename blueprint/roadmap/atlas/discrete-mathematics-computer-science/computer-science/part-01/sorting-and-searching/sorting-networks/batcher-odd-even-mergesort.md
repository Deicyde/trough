---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.SortingNetworks.OddEven.relabel, Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_relabel, Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_relabel_of_not_mem, Cslib.Algorithms.Lean.SortingNetworks.OddEven.finalLayer, Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenMerge, Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenSortN, Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_finalLayer, Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenMerge_merges
statement: formalized
proof: formalized
---

# Batcher odd–even mergesort

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html).

## Relabeling the wires of a comparator list

Given a map $e : \mathbb{N} \to \mathbb{N}$
and a list of comparators, each a pair $(i, j)$ of wires in $\mathbb{N}$, the relabeled list
replaces every comparator $(i, j)$ by $(e(i), e(j))$ and keeps the order of the list.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.relabel`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#relabel).

## Running a relabeled network

Let $\alpha$ be a linearly ordered type and let
$e : \mathbb{N} \to \mathbb{N}$ be injective. For every list of comparators, every
$f : \mathbb{N} \to \alpha$ and every wire $j$, running the list relabeled by $e$ on $f$ gives at
wire $e(j)$ the same value as running the original list on the input $i \mapsto f(e(i))$ gives at
wire $j$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_relabel`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#run-n-relabel).

## Relabeled networks fix the wires outside the image

Let $\alpha$ be a linearly ordered
type, $e : \mathbb{N} \to \mathbb{N}$ any map and $f : \mathbb{N} \to \alpha$ an assignment of
values to the wires. For every list of comparators and every wire $x$ that is not of the form
$e(y)$, running the list relabeled by $e$ on $f$ gives the value $f(x)$ at wire $x$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_relabel_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#run-n-relabel-of-not-mem).

## Last layer of the odd-even merger

For $k \in \mathbb{N}$, this is the list of comparators
$(2i + 1, 2i + 2)$ for $i = 0, 1, \dots, 2^{k+1} - 2$, in increasing order of $i$. It compares the
neighbouring wires $2i + 1$ and $2i + 2$ and is the last layer of the odd-even merger on
$2^{k+2}$ wires.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.finalLayer`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#final-layer).

## Batcher's odd-even merger

For $k \in \mathbb{N}$, the odd-even merger on wires
$0, \dots, 2^{k+1} - 1$ is the comparator list defined by recursion on $k$. For $k = 0$ it is the
single comparator $(0, 1)$. For $k + 1$ it is the merger for $k$ with each wire $i$ renamed to
$2i$ (merging the even wires), followed by the merger for $k$ with each wire $i$ renamed to
$2i + 1$ (merging the odd wires), followed by the comparators $(2i + 1, 2i + 2)$ for
$i = 0, 1, \dots, 2^{k+1} - 2$ in increasing order of $i$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenMerge`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-merge).

## Batcher's odd-even merge sort

For $k \in \mathbb{N}$, odd-even merge sort on wires
$0, \dots, 2^k - 1$ is the comparator list defined by recursion on $k$. For $k = 0$ it is empty.
For $k + 1$ it is the sorter for $k$ (sorting wires $0, \dots, 2^k - 1$), followed by the sorter
for $k$ with each wire $i$ renamed to $2^k + i$ (sorting wires $2^k, \dots, 2^{k+1} - 1$),
followed by Batcher's odd-even merger on $2^{k+1}$ wires.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenSortN`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-sort-n).

## Output of the last layer of the odd-even merger

Let $\alpha$ be a linearly ordered type,
$k \in \mathbb{N}$ and $f : \mathbb{N} \to \alpha$ an assignment of values to the wires. Running
the final layer for $k$ on $f$ gives at a wire $x$ the value $\min(f(x), f(x + 1))$ if $x$ is
odd and $\lfloor x / 2 \rfloor < 2^{k+1} - 1$; otherwise the value $\max(f(x - 1), f(x))$ if
$x$ is even, $x > 0$ and $(x - 2) / 2 < 2^{k+1} - 1$; and the value $f(x)$ in all other cases.
In other words, for each $i < 2^{k+1} - 1$ wire $2i + 1$ receives the minimum and wire $2i + 2$
the maximum of the values of $f$ on these two wires, and every other wire keeps its value.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.runN_finalLayer`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#run-n-final-layer).

## The odd-even merger merges

Let $k \in \mathbb{N}$ and let $f$ assign a Boolean value to
each wire $0, 1, 2, \dots$, with false read as $0$ and true as $1$. Let $a, c \le 2^k$ be such
that wires $0, \dots, 2^k - 1$ hold $a$ zeros followed by ones (wire $i < 2^k$ holds $0$ exactly
when $i < a$) and wires $2^k, \dots, 2^{k+1} - 1$ hold $c$ zeros followed by ones (wire
$2^k + i$, for $i < 2^k$, holds $0$ exactly when $i < c$). Then after Batcher's odd-even merger
on $2^{k+1}$ wires runs on $f$, every wire $j < 2^{k+1}$ holds $0$ exactly when $j < a + c$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenMerge_merges`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-merge-merges).

## Odd-even merge sort sorts every $0$-$1$ input

Let $k \in \mathbb{N}$ and let $f$ assign a
Boolean value to each wire $0, 1, 2, \dots$, with false read as $0$ and true as $1$. After
Batcher's odd-even merge sort on $2^k$ wires runs on $f$, there is $z \le 2^k$ such that every
wire $j < 2^k$ holds $0$ exactly when $j < z$: wires $0, \dots, 2^k - 1$ hold $z$ zeros followed
by ones.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenSortN_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-sort-n-sorts).

## Relabeling keeps comparators within an interval

Let $ps$ be a list of comparators,
each a pair of natural numbers, that lies within $[l, h)$, and let $e : \mathbb{N} \to \mathbb{N}$
satisfy $l' \le e(x) < h'$ for every $x$ with $l \le x < h$. Then the list obtained from $ps$ by
relabeling its wires by $e$ lies within $[l', h')$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.relabel_within`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#relabel-within).

## Size of the odd-even merger

For every $k \in \mathbb{N}$, Batcher's odd-even merger on
$2^{k+1}$ wires consists of exactly $k \cdot 2^k + 1$ comparators.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.length_oddEvenMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#length-odd-even-merge).

## Size of Batcher's odd-even merge sort

For every $k \in \mathbb{N}$, the number $L$ of
comparators of Batcher's odd-even merge sort on $2^k$ wires satisfies
$4(L + 1) + k \cdot 2^k = (k^2 + 4) \cdot 2^k$, that is, $L = (k^2 - k + 4) \cdot 2^k / 4 - 1$.

The identity is stated without subtraction or division, and is exact for every $k$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.length_oddEvenSortN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#length-odd-even-sort-n).

## Batcher's odd-even merge sorting network

For $k \in \mathbb{N}$, this is the comparator
network on the $2^k$ wires $0, \dots, 2^k - 1$ given by the comparators of Batcher's odd-even
merge sort on $2^k$ wires, in the same order, with any comparator that touches a wire $\ge 2^k$
dropped.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenSorter`, a definition declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-sorter).

## Batcher's odd-even merge sort sorts every input over every linear order

For every
$k \in \mathbb{N}$ and every linearly ordered type $\alpha$, Batcher's odd-even merge sorting
network on $2^k$ wires sorts every input over $\alpha$: for every assignment $v$ of elements of
$\alpha$ to the wires $0, \dots, 2^k - 1$, the output of the network on $v$ is monotone in the
wire order.

The proof goes through the 0-1 principle.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.oddEvenSorter_sorts`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEven.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-sorter-sorts).

## Levels of a relabeled comparator list

Let $e : \mathbb{N} \to \mathbb{N}$ be
injective, let $p$ be a comparator list and let $\ell$ be an initial level assignment. For
every wire $j$, the level of wire $e(j)$ after running $p$ with its wires relabeled by $e$,
starting from $\ell$, equals the level of wire $j$ after running $p$ starting from
$\ell \circ e$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.levels_relabel`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#levels-relabel).

## Relabeled comparator lists leave the other wires alone

Let $p$ be a comparator list,
let $e : \mathbb{N} \to \mathbb{N}$ be any map and let $\ell$ be an initial level assignment.
For every wire $x$ outside the image of $e$, the level of $x$ after running $p$ with its
wires relabeled by $e$, starting from $\ell$, is $\ell(x)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.levels_relabel_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#levels-relabel-of-not-mem).

## Relabeling wires preserves a depth bound

If a comparator list has depth at most $d$
and $e : \mathbb{N} \to \mathbb{N}$ is injective, then the comparator list obtained by
relabeling its wires by $e$ also has depth at most $d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.depthLE_relabel`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#depth-le-relabel).

## Levels of a relabeled comparator list on the image wires

Let $p$ be a comparator
list and let $e : \mathbb{N} \to \mathbb{N}$ be injective. If two initial level assignments
$\ell$ and $\ell'$ agree on every wire $e(y)$, then the levels after running $p$ with its
wires relabeled by $e$, starting from $\ell$ and from $\ell'$, agree on every wire $e(y)$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.levels_relabel_congr`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#levels-relabel-congr).

## Parallel composition of relabeled comparator lists

Let $e$ and $e'$ be injective
maps $\mathbb{N} \to \mathbb{N}$ with disjoint images, that is, $e(y) \ne e'(y')$ for all
$y$ and $y'$. If the comparator lists $p$ and $q$ both have depth at most $d$, then $p$ with
its wires relabeled by $e$, followed by $q$ with its wires relabeled by $e'$, has depth at
most $d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.depthLE_append_relabel`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#depth-le-append-relabel).

## The final layer of the odd-even merger has depth at most one

For every $k$, the
final layer of the odd-even merger on $2^{k+2}$ wires, which compares wires $2i + 1$ and
$2i + 2$ for each $i < 2^{k+1} - 1$, has depth at most $1$: its comparators are disjoint.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.depthLE_finalLayer`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#depth-le-final-layer).

## Depth bound for Batcher's odd-even merger

For every $k$, Batcher's odd-even merger on
$2^{k+1}$ wires has depth at most $k + 1$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.depthLE_oddEvenMerge`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#depth-le-odd-even-merge).

## Depth bound for Batcher's odd-even merge sort as a comparator list

For every $k$,
there is a $d$ with $2d \le k(k+1)$ such that the comparator list of Batcher's odd-even merge
sort on wires $0, \dots, 2^k - 1$ has depth at most $d$; that is, its depth is at most
$k(k+1)/2$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.OddEven.depthLE_oddEvenSortN`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#depth-le-odd-even-sort-n).

## Depth bound for Batcher's odd-even merge sorting network

For every $k$, there is a
$d$ with $2d \le k(k+1)$ such that Batcher's odd-even merge sorting network on $2^k$ wires
has depth at most $d$; that is, its depth is at most $k(k+1)/2$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.oddEvenSorter_depthLE`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#odd-even-sorter-depth-le).

## Lower bound for the depth of Batcher's odd-even merge sorting network

For all $k$
and $d$, if Batcher's odd-even merge sorting network on $2^k$ wires has depth at most $d$,
then $k \le d$.

Formalized by `Cslib.Algorithms.Lean.SortingNetworks.le_of_oddEvenSorter_depthLE`, a theorem declared in [CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/SortingNetworks/OddEvenDepth.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html#le-of-odd-even-sorter-depth-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Batcher odd–even mergesort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/sorting-networks/batcher-odd-even-mergesort)
