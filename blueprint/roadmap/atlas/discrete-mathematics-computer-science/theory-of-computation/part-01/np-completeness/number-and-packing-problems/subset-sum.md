---
declaration: section
origin: cited
lean: Cslib.Complexity.Karp.encodeSS, Cslib.Complexity.Karp.subsetSumDec, Cslib.Complexity.Karp.pairDigit, Cslib.Complexity.Karp.touches, Cslib.Complexity.Karp.vtxNum, Cslib.Complexity.Karp.edgeNum, Cslib.Complexity.Karp.ssTarget, Cslib.Complexity.Karp.ssNums
statement: formalized
proof: formalized
---

# Subset sum

121 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/index.html).

## Bit-string encoding of SUBSET-SUM instances

The instance with numbers $a_1, \dots, a_r$
and target $t$ is encoded as the block of $t$ followed by the blocks of $a_1, \dots, a_r$ in
order. The block of a number is its binary expansion, least significant bit first and empty for
the number $0$, made self-delimiting by writing each bit $c$ as $1c$ and appending a final $0$.

Formalized by `Cslib.Complexity.Karp.encodeSS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#encode-ss).

## The SUBSET-SUM problem

The decision problem that accepts a bit string $x$ exactly when
$x$ encodes a SUBSET-SUM instance with a list of numbers $a_1, \dots, a_r$ and a target $t$ such
that some sublist of $a_1, \dots, a_r$ sums to $t$. A sublist keeps some of the entries in their
order, so a number may be used as often as it occurs in the list.

Formalized by `Cslib.Complexity.Karp.subsetSumDec`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#subset-sum-dec).

## Place value of a vertex pair in the SUBSET-SUM reduction

The place value of pair number
$q$ is $4^q$. The numbers of the reduction from VERTEX-COVER to SUBSET-SUM are written in base
$4$, with the digit at position $q$ belonging to pair $q$.

Formalized by `Cslib.Complexity.Karp.pairDigit`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#pair-digit).

## Pairs touching a vertex

Let $p_0, \dots, p_{m-1}$ be the vertex pairs $(i, j)$ with
$i < j < n$ in encoding order (rows $i$ ascending, within a row $j$ descending). For a list $b$
of pair bits, a vertex $v$ and an index $q$, the test is true when bit $b_q$ is set and $v$ is one
of the two entries of $p_q$. An index past the end of $b$ counts as an unset bit, and for
$q \ge m$ the pair $p_q$ is taken to be $(0, 0)$.

Formalized by `Cslib.Complexity.Karp.touches`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#touches).

## Vertex numbers of the SUBSET-SUM reduction

Let $p_0, \dots, p_{m-1}$ be the vertex pairs
$(i, j)$ with $i < j < n$ in encoding order (rows $i$ ascending, within a row $j$ descending),
and let $b$ be a list of pair bits. The number of a vertex $v$ is $4^m + \sum 4^q$, the sum over
the indices $q < m$ such that bit $b_q$ is set and $v$ is an entry of $p_q$, where an index past
the end of $b$ counts as unset. In base $4$ it has digit $1$ at position $m$ and at each such
$q$, and $0$ elsewhere.

Formalized by `Cslib.Complexity.Karp.vtxNum`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#vtx-num).

## Edge numbers of the SUBSET-SUM reduction

Given a list $b$ of pair bits and a pair index
$q$, the number of pair $q$ is $4^q$ if bit $b_q$ is set and $0$ otherwise; an index past the end
of $b$ counts as an unset bit.

Formalized by `Cslib.Complexity.Karp.edgeNum`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#edge-num).

## Target of the SUBSET-SUM reduction

Let $m = n(n-1)/2$ be the number of vertex pairs
$(i, j)$ with $i < j < n$, and let $b$ be a list of pair bits. For $k \in \mathbb{N}$ the target
is $k \cdot 4^m + \sum 2 \cdot 4^q$, the sum over the indices $q < m$ such that bit $b_q$ is set
(an index past the end of $b$ counts as unset). So the quotient of the target by $4^m$ is $k$, and
its base-$4$ digit at position $q < m$ is $2$ when $b_q$ is set and $0$ otherwise.

Formalized by `Cslib.Complexity.Karp.ssTarget`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#ss-target).

## Numbers of the SUBSET-SUM reduction

For $n$ vertices and a list $b$ of pair bits, with
$m = n(n-1)/2$ vertex pairs, the numbers of the instance are the vertex numbers of
$v = 0, \dots, n - 1$, in this order, followed by the edge numbers of the pairs
$q = 0, \dots, m - 1$, in this order.

Formalized by `Cslib.Complexity.Karp.ssNums`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#ss-nums).

## Fixed no-instance of SUBSET-SUM

The encoding of the SUBSET-SUM instance with no numbers
and target $1$. It is a no-instance, because the only sublist of the empty list sums to $0$.

Formalized by `Cslib.Complexity.Karp.noSS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#no-ss).

## Reduction from VERTEX-COVER to SUBSET-SUM

The map on bit strings reads $x$ as $k$ ones, a
zero, $n$ ones, a zero and a remaining list $b$ of pair bits. If this parse succeeds and $b$ has
exactly $n(n-1)/2$ bits, one per vertex pair, then $x$ is sent to the encoding of the SUBSET-SUM
instance whose numbers are the numbers of the reduction for $n$ and $b$ and whose target is the
target for $k$, $n$ and $b$. Otherwise $x$ is sent to the fixed no-instance with no numbers and
target $1$.

Formalized by `Cslib.Complexity.Karp.reduceSS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSum.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSum.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#reduce-ss).

## The fixed no-instance of SUBSET-SUM

The encoded SUBSET-SUM instance with no numbers and
target $1$ is a no-instance: the SUBSET-SUM decision problem returns false on it.

Formalized by `Cslib.Complexity.Karp.subsetSumDec_noSS`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#subset-sum-dec-no-ss).

## Base-4 expansions with digits below $4$ are unique

Let $m, A, B \in \mathbb{N}$ and let
$d, e : \mathbb{N} \to \mathbb{N}$ satisfy $d(q) < 4$ and $e(q) < 4$ for every $q < m$. Then
$A \cdot 4^m + \sum_{q < m} d(q) \, 4^q = B \cdot 4^m + \sum_{q < m} e(q) \, 4^q$ holds if and only
if $A = B$ and $d(q) = e(q)$ for every $q < m$.

Formalized by `Cslib.Complexity.Karp.add_sum_digits_eq_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#add-sum-digits-eq-iff).

## Sublists of the reduction's numbers as vertex and pair sets

Let $n, t \in \mathbb{N}$, let
$b$ be a list of booleans, and let $m$ be the length of the list of vertex pairs $(i, j)$,
$i < j < n$. Write $x_v$ for the vertex number of $v$ and $y_q$ for the pair number of $q$ defined
from $n$ and $b$. Some sublist (a subsequence, not necessarily contiguous) of the reduction's
numbers for $n$ and $b$ sums to $t$ if and only if there are finite sets $S$ of vertices $v < n$
and $F$ of pair indices $q < m$ with $\sum_{v \in S} x_v + \sum_{q \in F} y_q = t$.

Formalized by `Cslib.Complexity.Karp.exists_sublist_ssNums_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#exists-sublist-ss-nums-iff).

## A vertex number in base 4

Let $n, v \in \mathbb{N}$, let $b$ be a list of booleans, and let
$m$ be the length of the list of vertex pairs $(i, j)$, $i < j < n$. The vertex number of $v$
defined from $n$ and $b$ equals $4^m + \sum_{q < m} t_q 4^q$, where $t_q = 1$ if entry $q$ of $b$
(counting from $0$) is true and $v$ is an endpoint of the $q$-th pair, and $t_q = 0$ otherwise.

Formalized by `Cslib.Complexity.Karp.vtxNum_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#vtx-num-eq).

## The target in base 4

Let $k, n \in \mathbb{N}$, let $b$ be a list of booleans, and let $m$
be the length of the list of vertex pairs $(i, j)$, $i < j < n$. The reduction's target for $k$,
$n$ and $b$ equals $k \cdot 4^m + \sum_{q < m} c_q 4^q$, where $c_q = 2$ if entry $q$ of $b$
(counting from $0$) is true and $c_q = 0$ otherwise, in particular when $b$ has no entry $q$.

Formalized by `Cslib.Complexity.Karp.ssTarget_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#ss-target-eq).

## A subset sum of the reduction's numbers in base 4

Let $n \in \mathbb{N}$, let $b$ be a
list of booleans, let $m$ be the length of the list of vertex pairs $(i, j)$, $i < j < n$, and let
$S$ and $F$ be finite sets of natural numbers with every element of $F$ below $m$. Write $x_v$ for
the vertex number of $v$ and $y_q$ for the pair number of $q$ defined from $n$ and $b$. For $q < m$
let $t_{v,q} = 1$ if entry $q$ of $b$ (counting from $0$) is true and $v$ is an endpoint of the
$q$-th pair, and $t_{v,q} = 0$ otherwise; let $f_q = 1$ if $q \in F$ and entry $q$ of $b$ is true,
and $f_q = 0$ otherwise. An absent entry counts as false. Then
$\sum_{v \in S} x_v + \sum_{q \in F} y_q = |S| \cdot 4^m +
\sum_{q < m} \left(\sum_{v \in S} t_{v,q} + f_q\right) 4^q$.

Formalized by `Cslib.Complexity.Karp.sum_vtxNum_add_sum_edgeNum`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#sum-vtx-num-add-sum-edge-num).

## Vertices of a set touching a vertex pair

Let $n$ be a natural number, let
$p_0, \dots, p_{m-1}$ be the vertex pairs in encoding order for $n$, let $b$ be a list of pair
bits, let $q < m$ with $p_q = (i, j)$, and let $S$ be a finite set of natural numbers. Write $[P]$
for $1$ if $P$ holds and $0$ otherwise. Then the number of $v \in S$ for which the test whether
pair $q$ touches $v$ under $b$ is true equals $[i \in S] + [j \in S]$ if the bit $b_q$ is set, and
$0$ otherwise (an index past the end of $b$ counts as an unset bit).

Formalized by `Cslib.Complexity.Karp.sum_touches_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#sum-touches-eq).

## Vertex covers in terms of the pair bits

Let $n \in \mathbb{N}$, let $b$ be a list of
booleans with one entry for each pair in the list of vertex pairs $(i, j)$, $i < j < n$, and let
$G$ be the graph on the vertices $0, \dots, n - 1$ encoded by the pair bits $b$. Let $s$ be a
finite set of vertices of $G$ and $S$ a finite set of natural numbers such that each vertex $i$
lies in $s$ exactly when $i \in S$. Then $s$ is a vertex cover of $G$ if and only if, for every
index $q$ (counting from $0$) of the pair list whose entry in $b$ is true, the $q$-th pair
$(i_q, j_q)$ satisfies $i_q \in S$ or $j_q \in S$.

Formalized by `Cslib.Complexity.Karp.isVertexCover_toGraph_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#is-vertex-cover-to-graph-iff).

## Vertex covers of size $k$ match subset sums hitting the target

Let $k, n \in \mathbb{N}$
and let $b$ be a list of booleans with one entry for each pair in the list of vertex pairs
$(i, j)$, $i < j < n$. Let $G$ be the graph on the vertices $0, \dots, n - 1$ encoded by the pair
bits $b$. Then $G$ has a vertex cover with exactly $k$ vertices if and only if some sublist (a
subsequence, not necessarily contiguous) of the reduction's numbers for $n$ and $b$ sums to the
reduction's target for $k$, $n$ and $b$.

Formalized by `Cslib.Complexity.Karp.exists_cover_iff_exists_sublist`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumCorrect.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#exists-cover-iff-exists-sublist).

## Value of the empty bit list

The empty bit list, read as a binary number least significant
bit first, has value $0$.

Formalized by `Cslib.Complexity.Karp.EmitSS.bitsVal_nil`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-01/index.html#bits-val-nil).

## Value of a bit list with a leading bit

Write $\mathrm{val}(l)$ for the value of a bit list
$l$ read as a binary number least significant bit first, and for a bit $b$ write $[b]$ for $1$ if
$b$ is true and $0$ if $b$ is false. For every bit $b$ and every bit list $l$, the list with first
entry $b$ followed by $l$ has value $[b] + 2 \cdot \mathrm{val}(l)$.

Formalized by `Cslib.Complexity.Karp.EmitSS.bitsVal_cons`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#bits-val-cons).

## A bit list without trailing false is the binary code of its value

For every bit list $l$
whose last entry is not false (the empty list included), the binary code, least significant bit
first, of the value of $l$ read least significant bit first is $l$ itself.

Formalized by `Cslib.Complexity.Karp.EmitSS.encodeNat_bitsVal`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#encode-nat-bits-val).

## Value of a list of two-bit digits

Write $\mathrm{val}(l)$ for the value of a bit list $l$
read as a binary number least significant bit first. Let $f$ assign to each bit a list of exactly
two bits. Then for every bit list $b_0, b_1, \dots, b_{m-1}$, the concatenation
$f(b_0) f(b_1) \cdots f(b_{m-1})$ has value $\sum_{q < m} 4^q \, \mathrm{val}(f(b_q))$.

Formalized by `Cslib.Complexity.Karp.EmitSS.bitsVal_flatMap2`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#bits-val-flat-map2).

## Binary code of the value of a bit list

Read a bit list $l$ as a binary number, least
significant bit first. The binary code of its value (least significant bit first, with no trailing
false bits) is $l$ with all of its trailing false bits removed.

Formalized by `Cslib.Complexity.Karp.EmitSS.encodeNat_bitsVal_rev`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#encode-nat-bits-val-rev).

## Delimiting a bit list that ends in true

For every bit list $u = (u_1, \dots, u_k)$, the
self-delimiting form of $u$ followed by the bit true is
$(\mathrm{true}, u_1, \mathrm{true}, u_2, \dots, \mathrm{true}, u_k,
\mathrm{true}, \mathrm{true}, \mathrm{false})$.

Formalized by `Cslib.Complexity.Karp.EmitSS.delimit_append_true`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#delimit-append-true).

## Output block of a vertex-number digit

For a bit $t$, the block is the four-bit list
$(\mathrm{true}, t, \mathrm{true}, \mathrm{false})$.

In the reduction from VERTEX-COVER to SUBSET-SUM, the self-delimiting code of a vertex number
consists of one such block for each pair digit, followed by
$(\mathrm{true}, \mathrm{true}, \mathrm{false})$.

Formalized by `Cslib.Complexity.Karp.EmitSS.blk`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#blk).

## Output block of an edge number

For $q \in \mathbb{N}$ and a bit $b$: if $b$ is true, the
block is $q$ copies of $(\mathrm{true}, \mathrm{false}, \mathrm{true}, \mathrm{false})$ followed by
$(\mathrm{true}, \mathrm{true}, \mathrm{false})$; if $b$ is false, it is the one-bit list
$(\mathrm{false})$.

This is the self-delimiting binary code of $4^q$ when $b$ is true and of $0$ when $b$ is false.

Formalized by `Cslib.Complexity.Karp.EmitSS.edgeEnc`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#edge-enc).

## Output of all edge numbers

Write $E(q, b)$ for the output block of the edge number of pair
$q$ with bit $b$. For a bit list $(b_{m-1}, \dots, b_1, b_0)$, listing the bit of the last pair
first, the output is the concatenation $E(0, b_0) \, E(1, b_1) \cdots E(m-1, b_{m-1})$.

Formalized by `Cslib.Complexity.Karp.EmitSS.edgeOut`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#edge-out).

## The pair walk over lists of marks

For lists $L$ and $R$ of booleans, the pair walk
$W(L, R)$ is the list of pairs of booleans defined by recursion on $L$. If $L$ is empty, then
$W(L, R)$ is empty. If $L$ has first entry $a$ and remaining entries $L'$, then $W(L, R)$
consists of the pairs $(a, r)$ for the entries $r$ of $R$ in order, followed by $W(L', R')$,
where $R'$ is the list $R$ with $a$ put in front.

Formalized by `Cslib.Complexity.Karp.EmitSS.walkM`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#walk-m).

## Triangular numbers

For a natural number $n$, the triangular number $T(n)$ is the sum
$0 + 1 + \cdots + (n - 1)$ of the natural numbers below $n$. It is defined by recursion:
$T(0) = 0$ and $T(i + 1) = T(i) + i$.

Formalized by `Cslib.Complexity.Karp.EmitSS.tri`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#tri).

## The pair walk lists the vertex pairs in reverse

Let $f$ be a function from the natural
numbers to the booleans, let $n$ be a natural number, and let $W$ be the pair walk. For every
$i \le n$, let $L$ be the list $f(i - 1), \dots, f(1), f(0)$ (empty when $i = 0$) and $R$ the
list $f(i), f(i + 1), \dots, f(n - 1)$ (empty when $i = n$). Then $W(L, R)$ is obtained as
follows: list the pairs $(a, j)$ of natural numbers with $a < i$ and $a < j < n$, with $a$
ascending and, for each $a$, $j$ descending; reverse this list; and replace each pair $(a, j)$
by $(f(a), f(j))$.

Formalized by `Cslib.Complexity.Karp.EmitSS.walkM_pairs`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#walk-m-pairs).

## Vertex marks for a vertex

For natural numbers $n$ and $v$, the list of $n$ bits whose
entries, from first to last, record for $i = n-1, n-2, \dots, 0$ whether $i = v$.

Formalized by `Cslib.Complexity.Karp.EmitSS.mkL`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#mk-l).

## Touch bits from the pair walk of a vertex

Let $n$ and $v$ be natural numbers, let $m$ be
the number of vertex pairs in encoding order for $n$, and let $b$ be a list of $m$ pair bits. Let
$L$ be the list of vertex marks for $v$ among $n$, let $(x_0, y_0), \dots, (x_{k-1}, y_{k-1})$ be
the pair walk $W(L, [\,])$, and let $c_0, \dots, c_{m-1}$ be the list $b$ reversed. Then the list
of the entries $c_l \wedge (y_l \vee x_l)$ for $l = 0, \dots, \min(k, m) - 1$, reversed, is the
list of the values at $q = 0, 1, \dots, m - 1$ of the test whether pair $q$ touches $v$ under
$b$.

Formalized by `Cslib.Complexity.Karp.EmitSS.walk_touches`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumDigits.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#walk-touches).

## Stacks of the SUBSET-SUM reduction machine

The machine has fifteen stacks: the input $X$
and the output $O$; $A$, which holds the cover size $k$, and $H$, used to halve it; $N$, which
holds the number $n$ of vertices, and $M$, the pair count; $C$, which counts the pair bits; the
scratch stacks $S_1$ and $S_2$; $Y$ and $Z$, which hold the pair bits; $T$, which holds the
target's bits; and $L$, $R$ and $R_t$, which hold the vertex marks.

Formalized by `Cslib.Complexity.Karp.EmitSS.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#k).

## Stack alphabets of the subset-sum emitter

In the VERTEX-COVER to SUBSET-SUM machine the
output stack $\mathsf{O}$ holds Booleans, and every other stack holds token symbols.

Formalized by `Cslib.Complexity.Karp.EmitSS.Γ`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#untitled).

## Labels of the subset-sum emitter

The control labels of the subset-sum emitter machine
are: $\mathrm{rdK}$, $\mathrm{rdN}$ and $\mathrm{mv}$ (parsing the two unary numbers $k$ and $n$
that open the input, and moving the pair bits); $\mathrm{tri}$, $\mathrm{triC}$,
$\mathrm{triC2}$, $\mathrm{cmp}$ and, for every ordering $o$, the labels $\mathrm{rc}(o)$ and
$\mathrm{rcB}(o)$ (counting the pairs and comparing that count with the number of pair bits);
$\mathrm{eg}$, $\mathrm{egX}$, $\mathrm{egR}$, $\mathrm{egR2}$ and $\mathrm{egY}$ (the edge
numbers); $\mathrm{vinit}$, $\mathrm{vtx}$, $\mathrm{pr}$, $\mathrm{rend}$, $\mathrm{rmv}$,
$\mathrm{vend}$, $\mathrm{vchk}$ and $\mathrm{rs}$ (the vertex numbers); $\mathrm{hv}$,
$\mathrm{hv0}$, $\mathrm{hv1}$ and $\mathrm{hvB}$ (the binary digits of $k$); $\mathrm{tem0}$,
$\mathrm{tsk}$ and $\mathrm{tem}$ (writing the target); $\mathrm{bad}$, which writes the fixed
no-instance; and the halting label $\mathrm{done}$.

Formalized by `Cslib.Complexity.Karp.EmitSS.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#lab).

## Counter unit of the subset-sum emitter

The unit symbol of the counters of the
VERTEX-COVER to SUBSET-SUM machine is the token symbol $\mathrm{cl}$; a counter with value $n$
holds exactly $n$ copies of it.

Formalized by `Cslib.Complexity.Karp.EmitSS.U`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#u).

## Test for the input bit true (SUBSET-SUM reduction machine)

On the result of a pop, which
is either a symbol or nothing (when the stack was empty), the test returns true exactly when the
result is the input-bit symbol $\mathrm{bit}(\mathrm{true})$, and false otherwise.

Formalized by `Cslib.Complexity.Karp.EmitSS.isT`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#is-t).

## Test for the value symbol true (SUBSET-SUM reduction machine)

On the result of a pop,
which is either a symbol or nothing (when the stack was empty), the test returns true exactly when
the result is the value symbol $\mathrm{val}(\mathrm{true})$, which this machine uses for a pair
bit or vertex mark that is true, and false otherwise.

Formalized by `Cslib.Complexity.Karp.EmitSS.isV`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#is-v).

## Reading a pair bit or vertex mark

The partial map from token symbols to bits that
sends the symbol $\mathrm{val}(b)$ to $b$ and gives no value on every other symbol.

Formalized by `Cslib.Complexity.Karp.EmitSS.valOf`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-02/index.html#val-of).

## Branch after the count comparison (SUBSET-SUM reduction machine)

The label the machine
takes after comparing the pair-bit count with the pair count: the result "equal" leads to the
label $\mathrm{eg}$, which starts the edge-number phase, and the results "less than" and
"greater than" lead to the failure label $\mathrm{bad}$, which writes the fixed no-instance of
SUBSET-SUM.

Formalized by `Cslib.Complexity.Karp.EmitSS.cmpOut`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#cmp-out).

## The subset-sum emitter machine

A multi-stack machine with the labels of the subset-sum
emitter as control labels, a Boolean internal state, and the stacks of the emitter: the output
stack $O$ holds bits, every other stack holds symbols. Stacks are read top first, $U$ is the
counter unit, and to prepend a list to $O$ is to push it so that it reads top first. The labels
act as follows.

$\mathrm{rdK}$: if $X$ is empty, go to $\mathrm{bad}$; otherwise pop $X$, and if the popped
symbol is $\mathrm{bit}(\mathrm{true})$ push $U$ on $A$ and repeat, else go to $\mathrm{rdN}$.
$\mathrm{rdN}$: the same, except that each $\mathrm{bit}(\mathrm{true})$ pushes $U$ on $N$ and
$\mathrm{val}(\mathrm{false})$ on $L$, and the other case goes to $\mathrm{mv}$. $\mathrm{mv}$: if
$X$ is empty, go to $\mathrm{tri}$; otherwise pop $X$, let $s$ say whether the popped symbol is
$\mathrm{bit}(\mathrm{true})$, push $\mathrm{val}(s)$ on $Y$, then $\mathrm{bit}(\mathrm{false})$
and $\mathrm{bit}(s)$ on $T$, then $U$ on $C$, and repeat.

$\mathrm{tri}$: pop $N$; if it was empty go to $\mathrm{cmp}$, else go to $\mathrm{triC}$, which
pops $N$ until it is empty, pushing $U$ on $M$ and on $S_1$ for each popped symbol, and then to
$\mathrm{triC2}$, which pops $S_1$ until it is empty, pushing $U$ on $N$ for each, and returns to
$\mathrm{tri}$. $\mathrm{cmp}$: pop $C$ and $M$ together, pushing $U$ on $S_1$ for each symbol
popped from $C$ and on $S_2$ for each symbol popped from $M$, until one of them was empty; go to
$\mathrm{rc}(o)$ where $o$ is $<$, $=$ or $>$ according as only $C$, both, or only $M$ was empty.
$\mathrm{rc}(o)$ pops $S_1$ until empty, pushing $U$ on $C$ for each, then $\mathrm{rcB}(o)$ pops
$S_2$ until empty, pushing $U$ on $M$ for each, then goes to $\mathrm{eg}$ if $o$ is $=$ and to
$\mathrm{bad}$ otherwise.

$\mathrm{eg}$: if $Y$ is empty, go to $\mathrm{egY}$; otherwise pop $Y$, let $s$ say whether the
popped symbol is $\mathrm{val}(\mathrm{true})$, push $\mathrm{val}(s)$ on $Z$, pop $C$ and $M$,
and if $s$ is true prepend $(\mathrm{true}, \mathrm{true}, \mathrm{false})$ to $O$ and go to
$\mathrm{egX}$, else prepend $(\mathrm{false})$ to $O$ and repeat. $\mathrm{egX}$ pops $C$ until
it is empty, prepending $(\mathrm{true}, \mathrm{false}, \mathrm{true}, \mathrm{false})$ to $O$
for each popped symbol; then $\mathrm{egR}$ pops $M$ until empty, pushing $U$ on $C$ and on $S_1$
for each, and $\mathrm{egR2}$ pops $S_1$ until empty, pushing $U$ on $M$ for each, and returns to
$\mathrm{eg}$. $\mathrm{egY}$: while the top of $Z$ is some $\mathrm{val}(b)$, pop it and push
$\mathrm{val}(b)$ on $Y$; then go to $\mathrm{vinit}$.

$\mathrm{vinit}$: pop $L$; if a symbol was popped, push $\mathrm{val}(\mathrm{true})$ on $L$ and
go to $\mathrm{vtx}$, else go to $\mathrm{hv}$. $\mathrm{vtx}$: prepend
$(\mathrm{true}, \mathrm{true}, \mathrm{false})$ to $O$ and go to $\mathrm{pr}$. $\mathrm{pr}$: if
$R$ is empty, go to $\mathrm{rend}$; otherwise pop $R$, let $m$ be true exactly when the popped
symbol is $\mathrm{val}(\mathrm{true})$ and push $\mathrm{val}(m)$ on $\mathrm{Rt}$, let $a$ be
true exactly when the top of $L$ is $\mathrm{val}(\mathrm{true})$, pop $Y$, let $b$ be true
exactly when a $\mathrm{val}(\mathrm{true})$ was popped and push $\mathrm{val}(b)$ on $Z$,
prepend $(\mathrm{true}, b \wedge (m \vee a), \mathrm{true}, \mathrm{false})$ to $O$, and repeat.
$\mathrm{rend}$: while the top of $\mathrm{Rt}$ is some $\mathrm{val}(b)$, pop it and push
$\mathrm{val}(b)$ on $R$; then go to $\mathrm{rmv}$. $\mathrm{rmv}$: pop $L$, push
$\mathrm{val}(t)$ on $R$ where $t$ is true exactly when a $\mathrm{val}(\mathrm{true})$ was
popped, and go to $\mathrm{vend}$ if $L$ is now empty, else to $\mathrm{pr}$. $\mathrm{vend}$:
while the top of $Z$ is some $\mathrm{val}(b)$, pop it and push $\mathrm{val}(b)$ on $Y$; then
go to $\mathrm{vchk}$. $\mathrm{vchk}$: go to $\mathrm{hv}$ if the top of $R$ is
$\mathrm{val}(\mathrm{true})$, else to $\mathrm{rs}$. $\mathrm{rs}$: if $R$ is empty, go to
$\mathrm{vtx}$; otherwise pop $R$; if the popped symbol is $\mathrm{val}(\mathrm{true})$, pop $L$
and push $\mathrm{val}(\mathrm{true})$ and then $\mathrm{val}(\mathrm{false})$ on $L$, else push
$\mathrm{val}(\mathrm{false})$ on $L$; repeat.

$\mathrm{hv}$: go to $\mathrm{tem0}$ if $A$ is empty, else to $\mathrm{hv0}$. $\mathrm{hv0}$: pop
$A$; if it was empty, push $\mathrm{bit}(\mathrm{false})$ on $T$ and go to $\mathrm{hvB}$, else go
to $\mathrm{hv1}$. $\mathrm{hv1}$: pop $A$; if it was empty, push $\mathrm{bit}(\mathrm{true})$
on $T$ and go to $\mathrm{hvB}$, else push $U$ on $H$ and go to $\mathrm{hv0}$. $\mathrm{hvB}$
pops $H$ until it is empty, pushing $U$ on $A$ for each, and returns to $\mathrm{hv}$.
$\mathrm{tem0}$: prepend $(\mathrm{false})$ to $O$ and go to $\mathrm{tsk}$. $\mathrm{tsk}$: if
$T$ is empty, go to $\mathrm{done}$; otherwise pop $T$, and if the popped symbol is
$\mathrm{bit}(\mathrm{true})$ prepend $(\mathrm{true}, \mathrm{true})$ to $O$ and go to
$\mathrm{tem}$, else repeat. $\mathrm{tem}$: if $T$ is empty, go to $\mathrm{done}$; otherwise pop
$T$, let $s$ say whether the popped symbol is $\mathrm{bit}(\mathrm{true})$, prepend
$(\mathrm{true}, s)$ to $O$, and repeat. $\mathrm{bad}$: prepend the encoding of the subset-sum
instance with no numbers and target $1$ to $O$ and go to $\mathrm{done}$. $\mathrm{done}$: halt.

Formalized by `Cslib.Complexity.Karp.EmitSS.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#prog).

## Start label of the subset-sum emitter

The VERTEX-COVER to SUBSET-SUM machine starts at
the label $\mathsf{rdK}$, which begins parsing the input by reading its leading unary number.

Formalized by `Cslib.Complexity.Karp.EmitSS.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#start).

## Testing a popped input bit

For every bit $b$, the test for the input bit true of the
SUBSET-SUM reduction machine, applied to the popped symbol $\mathrm{bit}(b)$, returns $b$.

Formalized by `Cslib.Complexity.Karp.EmitSS.isT_bit`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#is-t-bit).

## Testing a popped input bit

For every bit $b$, the test for the input bit true of the
SUBSET-SUM reduction machine, applied to the popped symbol $\mathrm{bit}(b)$, returns $b$.

Formalized by `Cslib.Complexity.Karp.EmitSS.isV_val`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#is-v-val).

## Testing a popped input bit

For every bit $b$, the test for the input bit true of the
SUBSET-SUM reduction machine, applied to the popped symbol $\mathrm{bit}(b)$, returns $b$.

Formalized by `Cslib.Complexity.Karp.EmitSS.isBitBlock_val`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#is-bit-block-val).

## Subset-sum emitter: reading the unary k

Let $k$ and $i$ be natural numbers, $v$ a Boolean
state, $r = (r_1, \dots, r_m)$ a list of bits and $S$ stack contents such that stack $X$ holds,
top first, $k$ copies of $\mathrm{bit}(\mathrm{true})$, then $\mathrm{bit}(\mathrm{false})$, then
$\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, and stack $A$ holds exactly $i$ copies of the
counter unit $U$. Then $k + 1$ steps of the subset-sum emitter machine lead from label
$\mathrm{rdK}$ with state $v$ and stacks $S$ to label $\mathrm{rdN}$ with some state and some
stacks $S'$ such that $S'(X)$ is $\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, $S'(A)$ holds
exactly $i + k$ copies of $U$, and every stack other than $X$ and $A$ is unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.rdK_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rd-k-some).

## Subset-sum emitter: unterminated unary prefix at rdK

Let $r = (r_1, \dots, r_m)$ be a
list of bits on which reading a unary length prefix fails (equivalently, no $r_i$ is
$\mathrm{false}$). Then for every Boolean state $v$ and all stack contents $S$ whose stack $X$
holds $\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, top first, $m + 1$ steps of the subset-sum
emitter machine lead from label $\mathrm{rdK}$ with state $v$ and stacks $S$ to label
$\mathrm{bad}$ with some state and some stacks that agree with $S$ on every stack other than $X$
and $A$.

Formalized by `Cslib.Complexity.Karp.EmitSS.rdK_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rd-k-none).

## Subset-sum emitter: reading the unary n

Let $n$ and $i$ be natural numbers, $v$ a Boolean
state, $r = (r_1, \dots, r_m)$ a list of bits and $S$ stack contents such that stack $X$ holds,
top first, $n$ copies of $\mathrm{bit}(\mathrm{true})$, then $\mathrm{bit}(\mathrm{false})$, then
$\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, stack $N$ holds exactly $i$ copies of the counter
unit $U$, and stack $L$ holds exactly $i$ copies of $\mathrm{val}(\mathrm{false})$. Then $n + 1$
steps of the subset-sum emitter machine lead from label $\mathrm{rdN}$ with state $v$ and stacks
$S$ to label $\mathrm{mv}$ with some state and some stacks $S'$ such that $S'(X)$ is
$\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, $S'(N)$ holds exactly $i + n$ copies of $U$,
$S'(L)$ holds exactly $i + n$ copies of $\mathrm{val}(\mathrm{false})$, and every stack other than
$X$, $N$ and $L$ is unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.rdN_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rd-n-some).

## Subset-sum emitter: unterminated unary prefix at rdN

Let $r = (r_1, \dots, r_m)$ be a
list of bits on which reading a unary length prefix fails (equivalently, no $r_i$ is
$\mathrm{false}$). Then for every Boolean state $v$ and all stack contents $S$ whose stack $X$
holds $\mathrm{bit}(r_1), \dots, \mathrm{bit}(r_m)$, top first, $m + 1$ steps of the subset-sum
emitter machine lead from label $\mathrm{rdN}$ with state $v$ and stacks $S$ to label
$\mathrm{bad}$ with some state and some stacks that agree with $S$ on every stack other than $X$,
$N$ and $L$.

Formalized by `Cslib.Complexity.Karp.EmitSS.rdN_none`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rd-n-none).

## Subset-sum emitter: moving the pair bits

Let $r = (b_1, \dots, b_m)$ be a list of bits,
$v$ a Boolean state, $c$ a natural number and $S$ stack contents such that stack $X$ holds
$\mathrm{bit}(b_1), \dots, \mathrm{bit}(b_m)$, top first, and stack $C$ holds exactly $c$ copies of
the counter unit $U$. Then $m + 1$ steps of the subset-sum emitter machine lead from label
$\mathrm{mv}$ with state $v$ and stacks $S$ to label $\mathrm{tri}$ with some state and some
stacks $S'$ such that: $S'(Y)$ is $S(Y)$ after pushing $\mathrm{val}(b_1), \dots,
\mathrm{val}(b_m)$ in turn; $S'(T)$ is $S(T)$ after pushing, for $i = 1, \dots, m$ in turn,
$\mathrm{bit}(\mathrm{false})$ and then $\mathrm{bit}(b_i)$; $S'(C)$ holds exactly $c + m$ copies
of $U$; and every stack other than $X$, $Y$, $T$ and $C$ is unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.mv_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#mv-run).

## Run of the pair-counting loop of the subset-sum emitter

Let $n, p \in \mathbb{N}$ and
let $T_n = 0 + 1 + \dots + (n - 1)$. Start the VERTEX-COVER to SUBSET-SUM machine at label
$\mathsf{tri}$ with any state bit and with stacks $S$ in which the counter stacks $\mathsf{N}$ and
$\mathsf{M}$ hold exactly $n$ and $p$ unit symbols and the scratch stack $\mathsf{S1}$ is empty.
Then after exactly $(n + 1)^2$ steps the machine is at label $\mathsf{cmp}$ with some state bit
and stacks $S'$ in which $\mathsf{M}$ holds exactly $p + T_n$ unit symbols and every stack other
than $\mathsf{N}$ and $\mathsf{M}$ is as in $S$.

Formalized by `Cslib.Complexity.Karp.EmitSS.tri_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#tri-run).

## Edge-number phase (SUBSET-SUM reduction machine)

Let $d$ be a list of bits (in the
machine, the pair bits listed from the last pair down), $v$ a value of the machine's Boolean flag
and $S$ an assignment of contents to the stacks, and write $\mathrm{val}(d)$ for the list of the
symbols $\mathrm{val}(b)$ for the entries $b$ of $d$, in order. Suppose stack $Y$ holds
$\mathrm{val}(d)$ (first element on top), stacks $C$ and $M$ each hold $|d|$ copies of the unit
symbol, and stack $S_1$ is empty. Then, starting at label $\mathrm{eg}$ with flag $v$ and stacks
$S$, the machine reaches label $\mathrm{egY}$ in at most $|d|(3|d| + 4) + 1$ steps, with some
flag $v'$ and stacks $S'$ such that $S'(Y)$ is empty, $S'(Z)$ is the reverse of
$\mathrm{val}(d)$ followed by $S(Z)$, $S'(O)$ is the edge-number output of $d$ followed by
$S(O)$, and every stack other than $Y$, $Z$, $O$, $C$, $M$ holds the same contents as in $S$.

For each pair $q$ the machine pops its bit onto $Z$ and writes its edge number, using
$C = M = q$.

Formalized by `Cslib.Complexity.Karp.EmitSS.eg_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#eg-run).

## Subset-sum emitter: one row of the pair walk

Stacks are listed top first. Let $a$ be a
bit, $\ell$ a list of symbols, $(m_1, \dots, m_p)$ and $(b_1, \dots, b_p)$ two lists of bits of
the same length $p$, $y$ a list of symbols, $v$ a Boolean state and $S$ stack contents such that
$S(R)$ is $\mathrm{val}(m_1), \dots, \mathrm{val}(m_p)$, $S(L)$ is $\mathrm{val}(a)$ followed by
$\ell$, and $S(Y)$ is $\mathrm{val}(b_1), \dots, \mathrm{val}(b_p)$ followed by $y$. For a bit $t$
let $\mathrm{blk}(t)$ be the list $(\mathrm{true}, t, \mathrm{true}, \mathrm{false})$, and put
$d_i = b_i \wedge (m_i \vee a)$. Then $p + 1$ steps of the subset-sum emitter machine lead from
label $\mathrm{pr}$ with state $v$ and stacks $S$ to label $\mathrm{rend}$ with some state and
some stacks $S'$ such that: $S'(R)$ is empty; $S'(\mathrm{Rt})$ is
$\mathrm{val}(m_p), \dots, \mathrm{val}(m_1)$ followed by $S(\mathrm{Rt})$; $S'(Y) = y$; $S'(Z)$
is $\mathrm{val}(b_p), \dots, \mathrm{val}(b_1)$ followed by $S(Z)$; $S'(O)$ is the concatenation
$\mathrm{blk}(d_p) \cdots \mathrm{blk}(d_1)$ followed by $S(O)$; and every stack other than $R$,
$\mathrm{Rt}$, $Y$, $Z$ and $O$ is unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.pr_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#pr-run).

## Run of the subset-sum emitter's pair walk

Let $L_m \ne []$, $r_m$ and $w$ be lists of
booleans, and for a list $\ell$ of booleans write $\bar\ell$ for the list of mark symbols
$\mathrm{val}(x)$, $x \in \ell$. Let $(a_1, c_1), \dots, (a_m, c_m)$ be the mark pairs
$\mathrm{walkM}(L_m, r_m)$, and suppose $w = (b_1, \dots, b_m)$ has the same length $m$. Start the
emitter machine at label $\mathrm{pr}$ with any internal state $v$ and stacks $S$ such that
$S_L = \bar L_m$, $S_R = \bar r_m$, $S_{Rt}$ is empty and $S_Y = \bar w \mathbin{+\!\!+} y$ for a
list of symbols $y$. Then after exactly $2m + 3|L_m|$ steps the machine is at label
$\mathrm{vend}$, with some internal state $v'$ and stacks $S'$ such that $S'_L$ and $S'_{Rt}$ are
empty, $S'_R = \overline{\mathrm{rev}(L_m) \mathbin{+\!\!+} r_m}$, $S'_Y = y$,
$S'_Z = \mathrm{rev}(\bar w) \mathbin{+\!\!+} S_Z$ and $S'_O = \mathrm{blk}(t_m) \mathbin{+\!\!+}
\cdots \mathbin{+\!\!+} \mathrm{blk}(t_1) \mathbin{+\!\!+} S_O$,
where $t_i = b_i \wedge (c_i \vee a_i)$ and $\mathrm{blk}(t) = [\mathrm{true}, t, \mathrm{true},
\mathrm{false}]$; every stack other than $L$, $R$, $Rt$, $Y$, $Z$ and $O$ is unchanged.

The rows of the walk come from the vertex marks on $L$ (top first) and the columns from the marks
on $R$; after each row the column marks are restored from $Rt$ and the row mark moves onto $R$.

Formalized by `Cslib.Complexity.Karp.EmitSS.walk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#walk-run).

## Subset-sum emitter: one vertex number

Stacks are listed top first. Let $n$ be a natural
number, $p_0, \dots, p_{P-1}$ the pairs $(i, j)$ with $i < j < n$ in encoding order (rows $i$
ascending, within a row $j$ descending), $(\beta_0, \dots, \beta_{P-1})$ a list of $P$ pair bits
and $w < n$ a vertex. Let $N_w = 4^P + \sum_q 4^q$, the sum over the $q < P$ such that $\beta_q$
is true and $w$ is an endpoint of $p_q$, and let $m_u$ be true if $u = w$ and false otherwise.
Let $v$ be a Boolean state and $S$ stack contents such that $S(L)$ is
$\mathrm{val}(m_{n-1}), \dots, \mathrm{val}(m_0)$, $S(Y)$ is
$\mathrm{val}(\beta_{P-1}), \dots, \mathrm{val}(\beta_0)$, and $S(R)$, $S(\mathrm{Rt})$ and $S(Z)$
are empty. Then $3P + 3n + 2$ steps of the subset-sum emitter machine lead from label
$\mathrm{vtx}$ with state $v$ and stacks $S$ to label $\mathrm{vchk}$ with some state and some
stacks $S'$ such that: $S'(L)$, $S'(\mathrm{Rt})$ and $S'(Z)$ are empty; $S'(R)$ is
$\mathrm{val}(m_0), \dots, \mathrm{val}(m_{n-1})$; $S'(Y) = S(Y)$; $S'(O)$ is the self-delimiting
encoding of the binary representation of $N_w$ (least significant bit first) followed by $S(O)$;
and every stack other than $L$, $R$, $\mathrm{Rt}$, $Y$, $Z$ and $O$ is unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.round_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#round-run).

## Subset-sum emitter: moving unmarked vertices back to L

Let $c$ be a natural number,
$\rho = (\rho_1, \dots, \rho_k)$ a list of bits, $v$ a Boolean state and $S$ stack contents whose
stack $R$ holds, top first, $c$ copies of $\mathrm{val}(\mathrm{false})$ followed by
$\mathrm{val}(\rho_1), \dots, \mathrm{val}(\rho_k)$. Then $c$ steps of the subset-sum emitter
machine lead from label $\mathrm{rs}$ with state $v$ and stacks $S$ back to label $\mathrm{rs}$
with some state and some stacks $S'$ such that $S'(R)$ is
$\mathrm{val}(\rho_1), \dots, \mathrm{val}(\rho_k)$, $S'(L)$ is $c$ copies of
$\mathrm{val}(\mathrm{false})$ followed by $S(L)$, and every stack other than $R$ and $L$ is
unchanged.

Formalized by `Cslib.Complexity.Karp.EmitSS.rsF_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rs-f-run).

## Run of the mark-return loop of the subset-sum emitter

Let $n, w \in \mathbb{N}$ with
$w + 1 < n$. Start the VERTEX-COVER to SUBSET-SUM machine at label $\mathsf{rs}$ with any state
bit and with stacks $S$ in which stack $\mathsf{L}$ is empty and stack $\mathsf{R}$ holds, top
first, the symbols $\mathrm{val}(b_0), \dots, \mathrm{val}(b_{n-1})$, where $b_i$ is true exactly
when $i = w + 1$. Then after exactly $n + 1$ steps the machine is at label $\mathsf{vtx}$ with
some state bit and stacks $S'$ in which $\mathsf{R}$ is empty, $\mathsf{L}$ holds, top first, the
symbols $\mathrm{val}(c_{n-1}), \dots, \mathrm{val}(c_0)$, where $c_i$ is true exactly when
$i = w$, and every stack other than $\mathsf{R}$ and $\mathsf{L}$ is as in $S$. So the vertex
mark moves from vertex $w + 1$ to vertex $w$.

Formalized by `Cslib.Complexity.Karp.EmitSS.rs_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#rs-run).

## Run of the vertex-number phase of the subset-sum emitter

Let $n \in \mathbb{N}$, let
$p_0, \dots, p_{P-1}$ be the vertex pairs $(i, j)$ with $i < j < n$, listed with $i$ ascending
and, for each $i$, with $j$ descending, let $\beta_0, \dots, \beta_{P-1}$ be bits, and let
$w < n$. For a vertex $u$ let $a_u$ be $4^P$ plus the sum of $4^q$ over the indices $q < P$ such
that $\beta_q$ is true and $p_q$ contains $u$. Start the VERTEX-COVER to SUBSET-SUM machine at
label $\mathsf{vtx}$ with any state bit and with stacks $S$ in which stack $\mathsf{L}$ holds, top
first, the symbols $\mathrm{val}(c_{n-1}), \dots, \mathrm{val}(c_0)$, where $c_i$ is true exactly
when $i = w$, the stacks $\mathsf{R}$, $\mathsf{Rt}$ and $\mathsf{Z}$ are empty, and stack
$\mathsf{Y}$ holds, top first, the symbols
$\mathrm{val}(\beta_{P-1}), \dots, \mathrm{val}(\beta_0)$. Then within at most
$(w + 1)(3P + 4n + 4)$ steps the machine reaches label $\mathsf{hv}$ with some state bit and
stacks $S'$ in which the output stack $\mathsf{O}$ holds, top first, the self-delimiting binary
encodings of $a_0, a_1, \dots, a_w$ followed by the contents of $\mathsf{O}$ in $S$, and every
stack other than $\mathsf{L}$, $\mathsf{R}$, $\mathsf{Rt}$, $\mathsf{Y}$, $\mathsf{Z}$ and
$\mathsf{O}$ is as in $S$. Here the binary encoding lists the bits least significant first, and
the self-delimiting encoding replaces each bit $b$ by $\mathrm{true}, b$ and appends
$\mathrm{false}$.

Formalized by `Cslib.Complexity.Karp.EmitSS.vtx_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#vtx-run).

## One halving step of the binary conversion (SUBSET-SUM reduction machine)

Let $c$ and $p$
be natural numbers, $r$ a bit (read as $0$ or $1$ in arithmetic), $v$ a value of the machine's
Boolean flag and $S$ an assignment of contents to the stacks. Suppose stack $A$ holds $2c + r$
copies of the unit symbol and stack $H$ holds $p$ copies. Then, starting at label $\mathrm{hv0}$
with flag $v$ and stacks $S$, the machine reaches label $\mathrm{hvB}$ in exactly $2c + r + 1$
steps, with some flag $v'$ and stacks $S'$ such that $S'(A)$ is empty, $S'(H)$ holds $p + c$
copies of the unit symbol, $S'(T)$ is the input-bit symbol $\mathrm{bit}(r)$ on top of $S(T)$,
and every stack other than $A$, $H$, $T$ holds the same contents as in $S$.

Formalized by `Cslib.Complexity.Karp.EmitSS.hv0_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-03/index.html#hv0-run).

## Binary conversion (SUBSET-SUM reduction machine)

Let $k$ be a natural number, $v$ a value
of the machine's Boolean flag and $S$ an assignment of contents to the stacks, and list the binary
digits of $k$ least significant first, without leading zeros (so there are none for $k = 0$).
Suppose stack $A$ holds $k$ copies of the unit symbol and stack $H$ is empty. Then, starting at
label $\mathrm{hv}$ with flag $v$ and stacks $S$, the machine reaches label $\mathrm{tem0}$ in at
most $6k + 1$ steps, with some flag $v'$ and stacks $S'$ such that $S'(T)$ is the reverse of the
list of input-bit symbols $\mathrm{bit}(b)$ for these binary digits $b$ of $k$, followed by
$S(T)$, and every stack other than $A$, $H$, $T$ holds the same contents as in $S$.

The machine thus pushes the binary digits of $k$ onto $T$ least significant first.

Formalized by `Cslib.Complexity.Karp.EmitSS.hv_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#hv-run).

## Run of the target-bit loop of the subset-sum emitter

Let $l = (b_1, \dots, b_m)$ be a
list of bits. Start the VERTEX-COVER to SUBSET-SUM machine at label $\mathsf{tem}$ with any state
bit and with stacks $S$ in which stack $\mathsf{T}$ holds exactly the bit symbols of
$b_1, \dots, b_m$, top first. Then after exactly $m + 1$ steps the machine is at label
$\mathsf{done}$ with some state bit and stacks $S'$ in which the output stack $\mathsf{O}$ holds,
top first, $\mathrm{true}, b_m, \mathrm{true}, b_{m-1}, \dots, \mathrm{true}, b_1$ followed by the
contents of $\mathsf{O}$ in $S$, and every stack other than $\mathsf{T}$ and $\mathsf{O}$ is as in
$S$. That is, each popped bit $b$ is written as $b$ and then $\mathrm{true}$.

Formalized by `Cslib.Complexity.Karp.EmitSS.tem_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#tem-run).

## Run of the target-output phase of the subset-sum emitter

Let $l$ be a list of bits, let
$l'$ be $l$ with its leading $\mathrm{false}$ bits removed, and let $o$ be a list of bits. Start
the VERTEX-COVER to SUBSET-SUM machine at label $\mathsf{tsk}$ with any state bit and with stacks
$S$ in which stack $\mathsf{T}$ holds exactly the bit symbols of $l$, first bit on top, and the
output stack $\mathsf{O}$ holds $\mathrm{false}$ followed by $o$. Then after exactly $|l| + 1$
steps the machine is at label $\mathsf{done}$ with some state bit and stacks $S'$ in which
$\mathsf{O}$ holds the self-delimiting encoding of the reverse of $l'$ followed by $o$, and every
stack other than $\mathsf{T}$ and $\mathsf{O}$ is as in $S$. Here the self-delimiting encoding of
a list replaces each bit $b$ by $\mathrm{true}, b$ and appends $\mathrm{false}$.

Formalized by `Cslib.Complexity.Karp.EmitSS.tsk_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#tsk-run).

## Run of the VERTEX-COVER to SUBSET-SUM machine

Let $x$ be a bit string. Start the
VERTEX-COVER to SUBSET-SUM machine at its start label with any state bit and with stacks in
which the input stack $\mathsf{X}$ holds the bit symbols of $x$, first bit on top, and every other
stack is empty. Then within at most $40(|x| + 1)^4$ steps the machine reaches the label
$\mathsf{done}$ with some state bit and stacks in which the output stack $\mathsf{O}$ holds,
top first, the image of $x$ under the bit-string reduction from VERTEX-COVER to SUBSET-SUM.

Formalized by `Cslib.Complexity.Karp.EmitSS.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean, line 830](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumEmit.lean#L830). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#run).

## Whether a bit string ends in false

For a Boolean $z$ and a list of bits $p$, the value
is $z$ when $p$ is empty and the negation of the last bit of $p$ otherwise. So if $z$ records
whether the bits read so far end in false, the value records whether those bits followed by $p$
end in false.

With $z$ false the value is true exactly when $p$ is non-empty and ends in false, that is, when
$p$ is not the canonical binary code of a number, least significant bit first.

Formalized by `Cslib.Complexity.Karp.SSVerify.lastF`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#last-f).

## Canonical binary strings are those not ending in zero

For every bit string $p$, encoding
in binary (least significant bit first) the natural number that $p$ decodes to gives back $p$ if
and only if the trailing-zero test, started with no trailing zero, reports that $p$ does not end
in $0$; that is, $p$ is empty or its last bit is $1$.

Formalized by `Cslib.Complexity.Karp.SSVerify.encodeNat_decodeNat_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#encode-nat-decode-nat-iff).

## Parsing number blocks, with fuel

For a fuel $n$ and a list of bits $r$, the result is
either a list of numbers or a failure. If $r$ is empty, the result is the empty list. If $r$ is
non-empty and $n = 0$, parsing fails. If $r$ is non-empty and $n = m + 1$, one prefix-coded
number is decoded off the front of $r$: if this gives a number $a$ with remainder $r'$, the result
is $a$ followed by the result for $r'$ with fuel $m$ (failing if that fails), and otherwise
parsing fails. Here the prefix code of $a$ is the canonical binary code of $a$, least significant
bit first, with each bit $b$ written as the pair true, $b$, followed by a final false.

Formalized by `Cslib.Complexity.Karp.SSVerify.numsAux`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#nums-aux).

## Decoding a SUBSET-SUM instance

A block holding a bit string $p$ writes each bit $b$ of $p$
as the two bits $1, b$ and ends with a single $0$. The decoder reads a bit string $x$ as one block
holding the target $t$, followed by blocks holding numbers $a_1, \dots, a_n$ that run exactly to
the end of $x$, where each block must hold the canonical binary representation of its number
(least significant bit first, no trailing $0$). It returns the list $(a_1, \dots, a_n)$ together
with $t$, and fails if $x$ does not split this way.

Formalized by `Cslib.Complexity.Karp.SSVerify.decodeSS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#decode-ss).

## Decoding a SUBSET-SUM instance inverts its encoding

For every bit string $x$, every
list $a$ of natural numbers and every natural number $t$, the SUBSET-SUM decoder returns the
instance $(a, t)$ on $x$ if and only if $x$ is the encoding of the SUBSET-SUM instance with
numbers $a$ and target $t$.

Formalized by `Cslib.Complexity.Karp.SSVerify.decodeSS_eq_some`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#decode-ss-eq-some).

## Numbers chosen by a mask

For a list of numbers $a_0, \dots, a_{k-1}$ and a list of bits
$w$, the list of those $a_i$ with $w_i$ true, in their original order, where positions $i$ beyond
the end of $w$ count as false.

Formalized by `Cslib.Complexity.Karp.SSVerify.pick`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#pick).

## The SUBSET-SUM verifier

For bit strings $x$ and $w$, the verifier accepts $(x, w)$ exactly
when $x$ is the encoding of a SUBSET-SUM instance with numbers $a_0, \dots, a_{n-1}$ and target
$t$, and the sum of the $a_i$ for which bit $i$ of $w$ is true equals $t$; bits beyond the end of
$w$ count as false, and bits of $w$ past position $n - 1$ are ignored. If $x$ is not the encoding
of an instance, the verifier rejects.

Formalized by `Cslib.Complexity.Karp.SSVerify.ssCheck`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#ss-check).

## Every sublist is selected by a mask

If $l$ is a sublist of a list $a$ of natural numbers,
then there is a list $w$ of Booleans of the same length as $a$ such that the entries $a_i$ of $a$
with $w_i$ true, taken in order, form exactly $l$.

Formalized by `Cslib.Complexity.Karp.SSVerify.exists_pick`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#exists-pick).

## SUBSET-SUM is characterized by its verifier

A bit string $x$ is a yes-instance of
SUBSET-SUM if and only if there is a bit string $w$ with $|w| \le |x|$ such that the SUBSET-SUM
verifier accepts $(x, w)$.

Formalized by `Cslib.Complexity.Karp.SSVerify.subsetSumDec_iff`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#subset-sum-dec-iff).

## Carry bit of a full adder

For bits $a$, $b$ and a carry-in $c$, the carry out of adding
$a$, $b$ and $c$ is $(a \wedge b) \vee (c \wedge (a \oplus b))$, which is true iff at least two of
$a$, $b$, $c$ are true.

Formalized by `Cslib.Complexity.Karp.SSVerify.carry`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#carry).

## Adding a carry bit

For a carry bit $c$ and a bit string $u$ (least significant bit
first), $\mathrm{inc}(c, u)$ adds $c$ to $u$ by ripple carry: on the empty string it is $[1]$ if
$c$ is true and empty otherwise, and on a string with first bit $a$ and rest $u'$ it is the bit
$a \oplus c$ followed by $\mathrm{inc}(a \wedge c, u')$.

Formalized by `Cslib.Complexity.Karp.SSVerify.incB`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#inc-b).

## Ripple-carry addition of bit lists

For a carry-in bit $c$ and bit lists $u$ and $p$, both
least significant bit first, the ripple-carry sum walks $p$. If $p$ is empty, the result is $u$ with
the carry $c$ added (a final carry becomes a new last bit). Otherwise, with $a$ the first bit of $u$
($a$ is false when $u$ is empty) and $b$ the first bit of $p$, the result is the bit
$a \oplus b \oplus c$ followed by the ripple-carry sum of the rest of $u$ and the rest of $p$ with
carry-in the carry out of $a$, $b$ and $c$.

Formalized by `Cslib.Complexity.Karp.SSVerify.addB`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#add-b).

## Addition is correct on canonical numbers

For every bit $c$ and all natural numbers $m$ and
$n$, the ripple-carry sum, with carry-in $c$, of the canonical binary expansions of $m$ and $n$
(least significant bit first, no trailing false bit) is the canonical binary expansion of
$m + n + c$, where $c$ counts as $1$ if true and $0$ if false. In particular the sum stays
canonical.

Formalized by `Cslib.Complexity.Karp.SSVerify.addB_encodeNat`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#add-b-encode-nat).

## Stacks of the SUBSET-SUM verifier

The verifier has seven stacks: the input $X$, the
witness $W$, the target $T$ (most significant bit on top), the running sum $A$ (least significant
bit on top), the new sum $B$ (most significant bit on top), and the scratch stacks $P$ and $Q$ of
the final comparison.

Formalized by `Cslib.Complexity.Karp.SSVerify.K`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#k).

## Labels of the SUBSET-SUM verifier

The verifier has the labels $\mathrm{tgt}(z)$, reading
the target; $\mathrm{next}$, starting the next number; $\mathrm{add}(c, z)$, adding a chosen
number with carry $c$; $\mathrm{skip}(z)$, skipping an unchosen number; $\mathrm{fin}(c)$,
carrying $c$ through the rest of the sum; $\mathrm{back}$, moving the new sum back;
$\mathrm{fmove}$, moving the final sum for the comparison; $\mathrm{cmp}$, comparing;
$\mathrm{yes}$, accepting; and $\mathrm{no}$, rejecting, for all bits $c$ and $z$. In
$\mathrm{tgt}(z)$, $\mathrm{add}(c, z)$ and $\mathrm{skip}(z)$ the flag $z$ records whether the
bits of the current block read so far end in $0$.

Formalized by `Cslib.Complexity.Karp.SSVerify.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#lab).

## Statements of the SUBSET-SUM verifier

The statements of the SUBSET-SUM verifier machine
are the statements of a multi-stack Turing machine in Mathlib's TM2 model whose stacks are the
seven stacks $X$, $W$, $T$, $A$, $B$, $P$, $Q$, each over the symbol alphabet of the SAT verifier,
whose labels are the labels of the SUBSET-SUM verifier, and whose local state is a Boolean.

Formalized by `Cslib.Complexity.Karp.SSVerify.Stmt`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-04/index.html#stmt).

## Reading one pair of a block

For a flag $z$ (the bits read so far end in false), a
statement $\mathit{done}$ and statements $\mathit{body}(b)$ for each bit $b$: if the input stack
$X$ is empty, go to the label $\mathsf{no}$. Otherwise pop the top of $X$ as a bit, a symbol that
is not a bit counting as false. If it is false (the end marker), go to $\mathsf{no}$ when $z$ is
true and run $\mathit{done}$ otherwise. If it is true, go to $\mathsf{no}$ if $X$ is now empty,
and otherwise pop the next symbol of $X$ as a payload bit $b$ (again a non-bit counts as false)
and run $\mathit{body}(b)$.

Formalized by `Cslib.Complexity.Karp.SSVerify.rdS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#rd-s).

## Adding one payload bit to the sum

The machine statement for adding the payload bit $b$
with carry $c$: pop the top symbol of the sum stack $A$ and read it as a bit $a$ (false if $A$ is
empty or the symbol is not a bit), push the bit $a \oplus b \oplus c$ onto $B$, and go to the label
that adds a chosen number with carry the carry out of $a$, $b$ and $c$ and flag $\lnot b$ (the flag
records whether the bits of the block read so far end in false).

Formalized by `Cslib.Complexity.Karp.SSVerify.addS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#add-s).

## Carry step of the SUBSET-SUM verifier

For a carry bit $c$, the verifier statement that
carries $c$ through the rest of the sum on stack $A$: if $A$ is empty, it sets the local variable
to true, pushes the bit $1$ onto $B$ when $c$ is true and goes to label $\mathrm{back}$; otherwise
it pops the top symbol of $A$, read as a bit $a$ (a symbol that is not a bit reads as $0$), sets
the local variable to $a$, pushes the bit $a \oplus c$ onto $B$ and goes to label
$\mathrm{fin}(a \wedge c)$.

Formalized by `Cslib.Complexity.Karp.SSVerify.finS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#fin-s).

## Starting the next number

The verifier's statement at the label $\mathsf{next}$. If the
input stack $X$ is empty, it goes to the label $\mathsf{fmove}$ (move the sum, then compare).
Otherwise it pops the top of the witness stack $W$ and reads it as a bit $c$, taking $c$ false
when $W$ is empty or its top is not a bit; $c$ becomes the internal state. It then goes to the
label $\mathsf{add}$ with carry false if $c$ is true, and to the label $\mathsf{skip}$ if $c$ is
false, in both cases with the flag "the bits read so far end in false" unset.

Formalized by `Cslib.Complexity.Karp.SSVerify.nextS`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#next-s).

## The SUBSET-SUM verifier program

The program on the stacks $X, W, T, A, B, P, Q$ over
the verifier's symbols, with Boolean internal state, given label by label. A popped symbol that
is not a bit counts as false, as does a pop from an empty stack. Reading a pair of a block off
$X$ with flag $z$ ("the bits read so far end in false") goes to $\mathsf{no}$ if $X$ is empty;
on the end marker false it goes to $\mathsf{no}$ if $z$ holds and otherwise ends the block; on
true it reads a payload bit $b$, going to $\mathsf{no}$ if $X$ has ended.

* $\mathsf{tgt}(z)$: read a pair of the target block with flag $z$; at the end of the block go
  to $\mathsf{next}$; on a payload bit $b$, push $b$ onto $T$ and go to $\mathsf{tgt}(\lnot b)$.
* $\mathsf{next}$: if $X$ is empty go to $\mathsf{fmove}$; otherwise pop a witness bit $c$ off
  $W$ (false if absent) and go to $\mathsf{add}$ with carry false if $c$, else to
  $\mathsf{skip}$, with the flag unset.
* $\mathsf{add}(c, z)$: read a pair with flag $z$; at the end of the block go to
  $\mathsf{fin}(c)$; on a payload bit $b$, pop a bit $a$ off $A$ (false if absent), push
  $a \oplus b \oplus c$ onto $B$ and go to $\mathsf{add}(c', \lnot b)$, where $c'$ is the carry
  out of $a + b + c$.
* $\mathsf{skip}(z)$: read a pair with flag $z$; at the end of the block go to $\mathsf{next}$;
  on a payload bit $b$ go to $\mathsf{skip}(\lnot b)$.
* $\mathsf{fin}(c)$: carry $c$ through the rest of $A$, pushing the result bits onto $B$, then
  go to $\mathsf{back}$.
* $\mathsf{back}$: move the bits on top of $B$ onto $A$ one by one, then go to $\mathsf{next}$.
* $\mathsf{fmove}$: move the bits on top of $A$ onto $B$ one by one, then go to $\mathsf{cmp}$.
* $\mathsf{cmp}$: compare the bit blocks on top of $B$ and $T$, using $P$ and $Q$ as scratch, and
  go to $\mathsf{yes}$ if they are equal and to $\mathsf{no}$ otherwise.
* $\mathsf{yes}$ and $\mathsf{no}$: halt.

Formalized by `Cslib.Complexity.Karp.SSVerify.prog`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#prog).

## Start state of the SUBSET-SUM verifier

The SUBSET-SUM verifier machine starts in its
target-reading state, with the flag recording whether the bits read so far end in false set to
false.

Formalized by `Cslib.Complexity.Karp.SSVerify.start`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#start).

## Stack contents of the SUBSET-SUM verifier

For lists of symbols $x$, $w$, $t$, $a$, $b$,
this assigns contents to the seven stacks of the SUBSET-SUM verifier machine: the input stack $X$
holds $x$, the witness stack $W$ holds $w$, the target stack $T$ holds $t$, the sum stacks $A$ and
$B$ hold $a$ and $b$, and the scratch stacks $P$ and $Q$ are empty.

Formalized by `Cslib.Complexity.Karp.SSVerify.st`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#st).

## Rejection by the SUBSET-SUM verifier within a step bound

For a natural number $n$ and a
configuration $c$ of the SUBSET-SUM verifier, $\mathrm{Rej}(n, c)$ holds when there are an
internal state $v$ and stack contents $S$ such that the verifier runs from $c$ in at most $n$
steps to the configuration with label $\mathsf{no}$, internal state $v$ and stacks $S$.

Formalized by `Cslib.Complexity.Karp.SSVerify.Rej`, a definition declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#rej).

## Rejecting in one step

Let $l$ be a label, $v$ a Boolean and $S$ an assignment of stack
contents. If executing the verifier's statement at label $l$ from internal state $v$ and stacks
$S$ yields the next label $\mathsf{no}$, then the verifier reaches a configuration with label
$\mathsf{no}$ from the configuration $(l, v, S)$ within one step.

Formalized by `Cslib.Complexity.Karp.SSVerify.rej_one`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#rej-one).

## Reading the target block

Let $p$ and $s$ be lists of bits, and write $\mathrm{delimit}(p)$
for the self-delimiting encoding of $p$ (each bit $b$ written as true followed by $b$, then a
terminating false). Suppose the SUBSET-SUM verifier machine is in its target-reading state, with
flag $z$ recording whether the bits read so far end in false and any value of its local Boolean
variable, with the bits of $\mathrm{delimit}(p)$ followed by the bits of $s$ on the input stack
$X$, a list $t$ of symbols on the target stack $T$, arbitrary contents on the stacks $W$, $A$, $B$,
and the scratch stacks $P$, $Q$ empty. Then after exactly $|p| + 1$ steps the stack $X$ holds the
bits of $s$, the bits of $p$ have been pushed onto $T$ one at a time (so that $T$ holds, from the
top, the bits of $p$ in reverse order followed by $t$), the stacks $W$, $A$, $B$, $P$, $Q$ are
unchanged, the local variable is false, and the machine is in its rejecting state if either $p$
is non-empty and ends in false or $p$ is empty and $z$ is true, and in the state that starts the
next number otherwise.

Formalized by `Cslib.Complexity.Karp.SSVerify.tgt_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#tgt-run).

## Skipping a number block

Let $p$ and $s$ be lists of bits, and write $\mathrm{delimit}(p)$
for the self-delimiting encoding of $p$ (each bit $b$ written as true followed by $b$, then a
terminating false). Suppose the SUBSET-SUM verifier machine is in the state that skips an
unchosen number block, with flag $z$ recording whether the bits read so far end in false and any
value of its local Boolean variable, with the bits of $\mathrm{delimit}(p)$ followed by the bits
of $s$ on the input stack $X$, arbitrary contents on the stacks $W$, $T$, $A$, $B$, and the
scratch stacks $P$, $Q$ empty. Then after exactly $|p| + 1$ steps the stack $X$ holds the bits of
$s$, all other stacks are unchanged, the local variable is false, and the machine is in its
rejecting state if either $p$ is non-empty and ends in false or $p$ is empty and $z$ is true, and
in the state that starts the next number otherwise.

Formalized by `Cslib.Complexity.Karp.SSVerify.skip_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#skip-run).

## Carry phase of the SUBSET-SUM verifier

Let $x$, $w$, $t$ and $\mathit{acc}$ be lists of
stack symbols, $u$ a list of bits, $c$ a carry bit and $v$ a Boolean, and write
$\mathrm{inc}(c, u)$ for the result of adding the carry $c$ to $u$ (least significant bit first).
Started at label $\mathrm{fin}(c)$ with variable $v$, with $x$, $w$, $t$ on the stacks $X$, $W$,
$T$, the bits of $u$ on $A$ (first bit on top), $\mathit{acc}$ on $B$ and $P$, $Q$ empty, the
verifier takes exactly $|u| + 1$ steps to reach label $\mathrm{back}$ with variable true, where
$X$, $W$, $T$ are unchanged, $A$, $P$, $Q$ are empty, and $B$ holds the bits of
$\mathrm{inc}(c, u)$ on top of $\mathit{acc}$, last bit on top.

Formalized by `Cslib.Complexity.Karp.SSVerify.fin_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#fin-run).

## Adding a canonical chosen block

Let $p$ and $\mathit{rest}$ be bit lists and $z$ a bit
such that $p$ is nonempty and ends in true, or $p$ is empty and $z$ is false (the flag $z$
records whether the bits of the block read so far end in false), and let $c$ be a bit. Start the
SUBSET-SUM verifier machine at the label that adds a chosen number with carry $c$ and flag $z$,
with any value of the local variable, the self-delimiting encoding of $p$ followed by
$\mathit{rest}$ (as bit symbols) on the input stack $X$, symbol lists $w$ on $W$ and $t$ on $T$, a
bit list $u$ (as bit symbols, least significant bit first) on the sum stack $A$, a symbol list
$\mathit{acc}$ on $B$, and the scratch stacks $P$ and $Q$ empty. Then within $|p| + |u| + 2$ steps
the machine reaches the label that moves the new sum back, with some value of the local variable,
$\mathit{rest}$ on $X$, $w$ on $W$, $t$ on $T$, $A$, $P$ and $Q$ empty, and on $B$ the ripple-carry
sum of $u$ and $p$ with carry-in $c$ (as bit symbols, most significant bit on top) above
$\mathit{acc}$.

Formalized by `Cslib.Complexity.Karp.SSVerify.add_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#add-run).

## The verifier rejects a chosen block that ends in false

Let $p$ and $\mathit{rest}$ be bit
lists and $z$ a bit such that $p$ is nonempty and ends in false, or $p$ is empty and $z$ is true
(the flag $z$ records whether the bits of the block read so far end in false). Let $c$ be a bit and
$u$ a bit list. Start the SUBSET-SUM verifier machine at the label that adds a chosen number with
carry $c$ and flag $z$, with any value of the local variable, the self-delimiting encoding of $p$
followed by $\mathit{rest}$ (as bit symbols) on the input stack $X$, any symbol lists on $W$, $T$
and $B$, $u$ (as bit symbols) on the sum stack $A$, and the scratch stacks $P$ and $Q$ empty. Then
the machine reaches the rejecting label within $|p| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.SSVerify.add_rej`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#add-rej).

## The verifier rejects an unterminated target block

Let $r$ be a list of bits that does
not begin with a self-delimiting block, that is, parsing one self-delimiting block off the front
of $r$ fails. Suppose the SUBSET-SUM verifier machine is in its target-reading state, with either
value of the flag $z$ recording whether the bits read so far end in false and either value of its
local Boolean variable, with the bits of $r$ on the input stack $X$, arbitrary contents on the
stacks $W$, $T$, $A$, $B$, and the scratch stacks $P$, $Q$ empty. Then the machine reaches its
rejecting state within $|r| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.SSVerify.tgt_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#tgt-fail).

## The verifier rejects an unterminated skipped block

Let $r$ be a list of bits that does
not begin with a self-delimiting block, that is, parsing one self-delimiting block off the front
of $r$ fails. Suppose the SUBSET-SUM verifier machine is in the state that skips an unchosen
number block, with either value of the flag $z$ recording whether the bits read so far end in
false and either value of its local Boolean variable, with the bits of $r$ on the input stack
$X$, arbitrary contents on the stacks $W$, $T$, $A$, $B$, and the scratch stacks $P$, $Q$ empty.
Then the machine reaches its rejecting state within $|r| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.SSVerify.skip_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#skip-fail).

## The verifier rejects an unterminated chosen block

Let $r$ be a bit list from whose front no
complete self-delimiting block can be parsed, let $c$ and $z$ be bits, and let $u$ be a bit list.
Start the SUBSET-SUM verifier machine at the label that adds a chosen number with carry $c$ and
flag $z$ (the flag records whether the bits of the block read so far end in false), with any value
of the local variable, $r$ (as bit symbols) on the input stack $X$, any symbol lists on $W$, $T$
and $B$, $u$ (as bit symbols) on the sum stack $A$, and the scratch stacks $P$ and $Q$ empty. Then
the machine reaches the rejecting label within $|r| + 1$ steps.

Formalized by `Cslib.Complexity.Karp.SSVerify.add_fail`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#add-fail).

## Moving the new sum back

Let $\mathit{res}$ be a bit list. Start the SUBSET-SUM verifier
machine at the label that moves the new sum back, with any value of the local variable, symbol lists
$x$, $w$, $t$ on $X$, $W$, $T$, the sum stack $A$ empty, $\mathit{res}$ (as bit symbols, last bit
on top) on $B$, and the scratch stacks $P$ and $Q$ empty. Then after exactly
$|\mathit{res}| + 1$ steps the machine is at the label that starts the next number, with some value
of the local variable, $x$, $w$, $t$ unchanged, $\mathit{res}$ (as bit symbols, first bit on top)
on $A$, and $B$, $P$, $Q$ empty.

Formalized by `Cslib.Complexity.Karp.SSVerify.back_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#back-run).

## Moving the final sum for the comparison

Let $x$, $w$, $t$ be lists of stack symbols, $s$
a list of bits and $v$ a Boolean. Started at label $\mathrm{fmove}$ with variable $v$, with $x$,
$w$, $t$ on the stacks $X$, $W$, $T$, the bits of $s$ on $A$ (first bit on top) and $B$, $P$, $Q$
empty, the verifier takes exactly $|s| + 1$ steps to reach label $\mathrm{cmp}$, with some value
of the variable, where $X$, $W$, $T$ are unchanged, $A$, $P$, $Q$ are empty, and $B$ holds the
bits of $s$, last bit on top.

Formalized by `Cslib.Complexity.Karp.SSVerify.fmove_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#fmove-run).

## Comparing the sum with the target

Let $s$ and $\tau$ be bit lists. Start the SUBSET-SUM
verifier machine at the comparison label, with any value of the local variable, symbol lists $x$
and $w$ on $X$ and $W$, the target $\tau$ on $T$ and the sum $s$ on $B$ (both as bit symbols, last
bit on top), and the stacks $A$, $P$ and $Q$ empty. Then within $|s| + 1$ steps the machine reaches
the accepting label if $s = \tau$ and the rejecting label otherwise.

Formalized by `Cslib.Complexity.Karp.SSVerify.cmp_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-05/index.html#cmp-run).

## The summing loop of the SUBSET-SUM verifier

Let $N$ be a natural number and $t$ a list
of symbols. Write $\langle m \rangle$ for the canonical binary code of a natural number $m$, least
significant bit first, and put a bit list on a stack as the list of its name-bit symbols. Let $n$
and $s$ be natural numbers, $r$ and $w$ bit lists and $v$ a Boolean, with $|r| \le n$ and
$|\langle s \rangle| + |r| \le N$. Start the SUBSET-SUM verifier at the label $\mathsf{next}$
with internal state $v$, with $r$ on $X$, $w$ on $W$, $t$ on $T$, $\langle s \rangle$ on $A$,
and the stacks $B$, $P$ and $Q$ empty. Then for some internal state $v'$ and stack contents $S'$
it runs within $|r| \cdot (2N + 6) + 1$ steps to the configuration with internal state $v'$,
stacks $S'$ and label $\mathsf{fmove}$ if parsing the number blocks of $r$ with fuel $n$
succeeds, and label $\mathsf{no}$ if it fails. Moreover, if that parsing gives the list of
numbers $a$, and $\sigma$ is $s$ plus the sum of the numbers of $a$ chosen by the mask $w$, then
$|\langle \sigma \rangle| \le N$, and for some list of symbols $w'$ the stacks $S'$ hold nothing
on $X$, $w'$ on $W$, $t$ on $T$, $\langle \sigma \rangle$ on $A$, and nothing on $B$, $P$ and
$Q$.

Formalized by `Cslib.Complexity.Karp.SSVerify.loop_run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#loop-run).

## Cubic bound on the verifier's phase costs

For natural numbers $X$, $W$, $P$, $R$ and $S$
with $P + R \le X$ and $S \le X$,
$P + 1 + (R(2X + 6) + 1) + (S + 1) + (S + 1) \le 16 (X + W + 1)^3$.

Formalized by `Cslib.Complexity.Karp.SSVerify.cost_le`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#cost-le).

## The SUBSET-SUM verifier machine

Let $x$ and $w$ be lists of bits and $v$ a Boolean, and
let $S$ assign stack contents with the bits of $x$ on $X$, the bits of $w$ on $W$ and every other
stack empty. Started at the start label with internal state $v$ and stacks $S$, the verifier
program reaches, within $16(|x| + |w| + 1)^3$ steps, a configuration with label $\mathsf{yes}$
if the SUBSET-SUM check accepts $(x, w)$, and with label $\mathsf{no}$ otherwise.

Formalized by `Cslib.Complexity.Karp.SSVerify.run`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumVerify.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#run).

## The SUBSET-SUM verifier machine as a host component

The multi-stack Turing machine
that checks SUBSET-SUM certificates, packaged as a host component: it has seven stacks, each
holding symbols of the SAT verifier alphabet, its labels and its program are those of the
machine, and the list of its stacks names each of the seven stacks exactly once.

Formalized by `Cslib.Complexity.Karp.ssVerifyComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#ss-verify-comp).

## SUBSET-SUM is in NP

SUBSET-SUM is the decision problem on bit strings that accepts $x$
exactly when $x$ encodes a target $t$ followed by natural numbers $a_1, \dots, a_n$ (each written
in binary and delimited) such that some, possibly empty, sublist of $a_1, \dots, a_n$ sums to
$t$. This decision problem belongs to NP: there are a polynomial $p$ with natural-number
coefficients and a polynomial-time computable verifier $R$ such that SUBSET-SUM accepts $x$
exactly when $R(x, w)$ holds for some bit string $w$ with $|w| \le p(|x|)$.

Formalized by `Cslib.Complexity.Karp.subsetSumDec_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#subset-sum-dec-mem-np).

## The VERTEX-COVER to SUBSET-SUM machine as a host component

The multi-stack Turing
machine that computes the VERTEX-COVER to SUBSET-SUM reduction on bit strings, packaged as a
host component: its fifteen stacks (the output stack holds booleans, every other stack holds
symbols of the SAT verifier alphabet), its labels and its program are those of the machine, and
the list of its stacks names each of the fifteen stacks exactly once.

Formalized by `Cslib.Complexity.Karp.emitSSComp`, an abbreviation declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#emit-sscomp).

## The VERTEX-COVER to SUBSET-SUM reduction is polynomial-time

The reduction map on bit
strings, which sends the encoding of a VERTEX-COVER instance $(k, G)$ to the encoding of the
SUBSET-SUM instance built from it (one base-4 number for each vertex and for each pair of
vertices of $G$, and a target) and every other bit string to the instance with no numbers and
target $1$, is computable in polynomial time.

Formalized by `Cslib.Complexity.Karp.isPolyTime_reduceSS`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#is-poly-time-reduce-ss).

## SUBSET-SUM is NP-hard

Let SUBSET-SUM be the decision problem on bit strings that
accepts exactly the strings encoding a target $t$ followed by natural numbers $a_1, \dots, a_n$
(each written in binary and delimited) such that some, possibly empty, sublist of
$a_1, \dots, a_n$ sums to $t$. Every decision problem $L$ in NP reduces to SUBSET-SUM by a
polynomial-time many-one reduction: there is a polynomial-time computable map $f$ on bit strings
such that, for every bit string $x$, $L$ accepts $x$ exactly when SUBSET-SUM accepts $f(x)$.

Formalized by `Cslib.Complexity.Karp.subsetSumDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#subset-sum-dec-np-hard).

## SUBSET-SUM is NP-complete

Let SUBSET-SUM be the decision problem on bit strings that
accepts exactly the strings encoding a target $t$ followed by natural numbers $a_1, \dots, a_n$
(each written in binary and delimited) such that some, possibly empty, sublist of
$a_1, \dots, a_n$ sums to $t$. Then SUBSET-SUM belongs to NP, and every decision problem $L$ in
NP reduces to SUBSET-SUM by a polynomial-time many-one reduction: there is a polynomial-time
computable map $f$ on bit strings such that, for every bit string $x$, $L$ accepts $x$ exactly
when SUBSET-SUM accepts $f(x)$.

Formalized by `Cslib.Complexity.Karp.subsetSumDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Karp/SubsetSumComplete.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#subset-sum-dec-np-complete).

## SUBSET-SUM verifier computes the mask-selected sum

On canonical delimited `encodeNat` blocks, the existing component
leaves the selected sum at a halt label. Normalize raw payloads first:
malformed blocks can instead reject early, leaving only a partial sum.
The cost uses framed bit length, never numeric magnitudes. The mask is
consumed; copy it before reuse in another component.

Formalized by `Cslib.Complexity.SSVerifierSum.sum_component_run`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierSum.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierSum.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#sum-component-run).

## A long enough all-true mask selects the whole list

A mask long enough to select every item gives the original list.

Formalized by `Cslib.Complexity.SSVerifierSum.pick_all`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierSum.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierSum.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#pick-all).

## Embedded SUBSET-SUM summing component reaches the mapped label

Reach the common mapped label after summing canonical `encodeNat`
blocks; unembedded stacks remain intact. The input agreement requires
prior normalization. A raw parse-failure exit can expose a partial sum.
This is only a reachability guarantee: `hφ` does not make the endpoint
fresh, distinct from mapped live labels, or a halt of the host. Callers
must establish their intended label separation and the code run next.
The embedded mask is consumed; each later sum needs its own saved copy.

Formalized by `Cslib.Complexity.SSVerifierSum.sum_embed`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierSum.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierSum.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#sum-embed).

## Framed input of two natural numbers

Two canonical Nat blocks in the existing list framing.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.pairInput`, a definition declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#pair-input).

## Labels of the binary addition machine

Original verifier labels plus initialization, clear, reverse, and halt.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.Lab`, an abbreviation declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#lab).

## Identity embedding of the verifier stacks

Reuse all original verifier stacks without re-encoding symbols.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.identity`, a definition declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#identity).

## Redirection of the verifier's halt labels

Redirect the two halt labels, leaving every live label distinct.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.redirect`, a definition declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#redirect).

## Only halt labels are redirected to the cleanup label

The cleanup continuation cannot alias any live verifier label.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.redirect_eq_clear_iff`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#redirect-eq-clear-iff).

## Binary addition program built on the SUBSET-SUM machine

Run the existing sum machine, then clear the mask and restore LSB order.
Only the original halt labels are redirected to a continuation.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.prog`, a definition declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#prog).

## Bit length of the sum is at most the input length

The canonical sum fits within the two framed operands' bit length.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.length_sum_le_input`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#length-sum-le-input).

## Binary addition of framed numbers in quadratic time

Add two canonically framed numbers, leaving only the LSB-first result.
The bound is quadratic in encoded input length; no loop enumerates values.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.run`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-06/index.html#run-2).

## Embedded run of the binary addition component

The addition component runs in a host, with every external stack
unchanged and all embedded workspace cleared.

Formalized by `Cslib.Complexity.SSVerifierArithmetic.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/SSVerifierArithmetic.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/part-07/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subset sum](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/subset-sum)
