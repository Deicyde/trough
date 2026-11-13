---
declaration: section
origin: cited
lean: MetaMathlibExt.diagonalSequence, MetaMathlibExt.diagonalSequence_seven_seven_four_one_one_one, MetaMathlibExt.diagonalOfList, MetaMathlibExt.diagonalOfList_one_two_one, MetaMathlibExt.diagonalNormalForm, MetaMathlibExt.diagonalNormalForm_four_example, MetaMathlibExt.diagonalMaxPartition, MetaMathlibExt.diagonalMaxPartition_four_example
statement: formalized
---

# Diagonal sequences of integer partitions

42 results, 20 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html).

## Diagonal sequence of a partition

Let $\alpha$ be a partition with parts
$\alpha_1 \ge \alpha_2 \ge \dots \ge \alpha_t$, and set $\alpha_i = 0$ for $i > t$. Its diagonal
sequence $\delta(\alpha) = (d_k)_{k \ge 0}$ has $d_0 = 0$ and, for $k \ge 1$, $d_k$ equal to the
number of indices $i$ with $1 \le i \le k$ and $\alpha_i + i - 1 \ge k$, that is, the number of
cells of the Young diagram on its $k$-th diagonal from upper right to lower left. Equivalently,
$d_k$ is the number of $i$ with $1 \le i \le k$ such that at least $i$ parts of $\alpha$ are at
least $k + 1 - i$; the definition uses this form, with the parts given as a finite multiset of
natural numbers.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1, Definition of the diagonal sequence (1.1).

Formalized by `MetaMathlibExt.diagonalSequence`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-sequence).

## Diagonal sequence of $(7, 7, 4, 1, 1, 1)$

The diagonal sequence of the partition
$(7, 7, 4, 1, 1, 1)$ takes the values $0, 1, 2, 3, 4, 4, 4, 2, 1, 0$ at the indices
$0, 1, \dots, 9$. This is the paper's running example.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (example after the definition); characteristic check of `diagonalSequence`.

Formalized by `MetaMathlibExt.diagonalSequence_seven_seven_four_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-sequence-seven-seven-four-one-o).

## Sequence of a finite list

A finite list $(d_1, \dots, d_\ell)$ of natural numbers
determines the sequence of natural numbers whose value at index $k$ is $d_k$ for
$1 \le k \le \ell$, and $0$ for $k = 0$ and for $k > \ell$. This is the indexing of diagonal
sequences, which take the value $0$ at index $0$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (trailing zeroes of `δ(α)` are omitted).

Formalized by `MetaMathlibExt.diagonalOfList`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-of-list).

## The list sequence of $(1, 2, 1)$

The sequence given by the list $(1, 2, 1)$ takes the
values $0, 1, 2, 1, 0, 0$ at the indices $0, 1, 2, 3, 4, 5$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1; characteristic check of `diagonalOfList`.

Formalized by `MetaMathlibExt.diagonalOfList_one_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-of-list-one-two-one).

## Normal form of a diagonal sequence

For a natural number $q$ and a sequence
$s = (s_k)$ of natural numbers, the normal form is the list
$(1, 2, \dots, q - 1, q, q^{(s_q)}, (q-1)^{(s_{q-1})}, \dots, 1^{(s_1)})$, where $v^{(m)}$
denotes $m$ copies of $v$: the numbers $1, \dots, q$ followed by $s_v$ copies of $v$ for
$v = q, q - 1, \dots, 1$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 1, display (2.1).

Formalized by `MetaMathlibExt.diagonalNormalForm`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-normal-form).

## Diagonal normal form for $q = 4$ and $s = (1, 1, 0, 2)$

For $q = 4$ and $s_1 = 1$,
$s_2 = 1$, $s_3 = 0$, $s_4 = 2$, the diagonal normal form
$(1, 2, 3, 4, 4^{(s_4)}, 3^{(s_3)}, 2^{(s_2)}, 1^{(s_1)})$, where $v^{(m)}$ denotes $m$ copies
of $v$, is $(1, 2, 3, 4, 4, 4, 2, 1)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 2 (example after Corollary 4); characteristic check of `diagonalNormalForm`.

Formalized by `MetaMathlibExt.diagonalNormalForm_four_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-normal-form-four-example).

## Maximal partition of a diagonal normal form

For a natural number $q$ and a sequence
$s = (s_k)$ of natural numbers, $\bar\alpha = (\bar\alpha_1, \dots, \bar\alpha_q)$ is the list of
the $q$ numbers $\bar\alpha_i = q - i + 1 + \sum_{k=i}^{q} s_k$, $1 \le i \le q$, in this order.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 1.

Formalized by `MetaMathlibExt.diagonalMaxPartition`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-max-partition).

## Maximal partition for $q = 4$ and $s = (1, 1, 0, 2)$

For $q = 4$ and $s_1 = 1$,
$s_2 = 1$, $s_3 = 0$, $s_4 = 2$, the maximal partition $\bar\alpha$, with parts
$\bar\alpha_i = q - i + 1 + \sum_{k=i}^{q} s_k$ for $1 \le i \le q$, is $(8, 6, 4, 3)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 2 (example after Corollary 4); characteristic check of `diagonalMaxPartition`.

Formalized by `MetaMathlibExt.diagonalMaxPartition_four_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-max-partition-four-example).

## Minimal partition of a diagonal normal form

For a natural number $q$ and a sequence
$s = (s_k)$ of natural numbers, $\underline\alpha$ is the list
$(q^{(s_q + 1)}, (q-1)^{(s_{q-1} + 1)}, \dots, 1^{(s_1 + 1)})$, where $v^{(m)}$ denotes $m$
copies of $v$: first $s_q + 1$ copies of $q$, then $s_{q-1} + 1$ copies of $q - 1$, and so on
down to $s_1 + 1$ copies of $1$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 2.

Formalized by `MetaMathlibExt.diagonalMinPartition`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-min-partition).

## Minimal partition for $q = 4$ and $s = (1, 1, 0, 2)$

For $q = 4$ and $s_1 = 1$,
$s_2 = 1$, $s_3 = 0$, $s_4 = 2$, the minimal partition
$\underline\alpha = (4^{(s_4 + 1)}, 3^{(s_3 + 1)}, 2^{(s_2 + 1)}, 1^{(s_1 + 1)})$, where
$v^{(m)}$ denotes $m$ copies of $v$, is $(4, 4, 4, 3, 2, 2, 1, 1)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 2 (example after Corollary 4); characteristic check of `diagonalMinPartition`.

Formalized by `MetaMathlibExt.diagonalMinPartition_four_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-min-partition-four-example).

## Conjugate of a multiset of parts

For a finite multiset $\alpha$ of natural numbers with
largest element $m$ (and $m = 0$ if $\alpha$ is empty), the conjugate $\alpha^*$ is the multiset
of the $m$ numbers $c_0, c_1, \dots, c_{m-1}$, where $c_j$ is the number of elements of $\alpha$
greater than $j$, counted with multiplicity. When $\alpha$ is the multiset of parts of a
partition, these are the parts of the conjugate partition.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (conjugate partition `α*`).

Formalized by `MetaMathlibExt.conjugateParts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#conjugate-parts).

## The conjugate of $(3, 1)$ is $(2, 1, 1)$

The conjugate of the partition with parts
$\{3, 1\}$ is the partition with parts $\{2, 1, 1\}$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1; characteristic check of `conjugateParts`.

Formalized by `MetaMathlibExt.conjugateParts_three_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#conjugate-parts-three-one).

## Diagonal class of a partition

For a partition $p$ of $n$, its diagonal class
$\delta^{-1}(\delta(p))$ is the finite set of all partitions $\beta$ of $n$ whose diagonal
sequence $\delta(\beta)$ equals the diagonal sequence $\delta(p)$ of $p$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (definition of `[d]`).

Formalized by `MetaMathlibExt.diagonalClass`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-class).

## Every partition lies in its diagonal class

For every partition $p$ of $n$, $p$ belongs
to the diagonal class of $p$, the set of partitions of $n$ whose diagonal sequence equals that
of $p$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (definition of `[d]`); characteristic check of `diagonalClass`.

Formalized by `MetaMathlibExt.mem_diagonalClass_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#mem-diagonal-class-self).

## Partitions with a prescribed diagonal sequence

For a natural number $n$ and a sequence
$d = (d_k)_{k \ge 0}$ of natural numbers, $[d]$ is the finite set of partitions $\beta$ of $n$
whose diagonal sequence $\delta(\beta)$ equals $d$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (definition of `[d]` for `d ∈ Δ(n)`).

Formalized by `MetaMathlibExt.diagonalClassOf`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-class-of).

## A partition lies in the class of its diagonal sequence

Every partition $\beta$ of $n$
belongs to the set of partitions of $n$ whose diagonal sequence equals that of $\beta$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 1 (definition of `[d]`); characteristic check of `diagonalClassOf`.

Formalized by `MetaMathlibExt.mem_diagonalClassOf_diagonalSequence`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#mem-diagonal-class-of-diagonal-sequence).

## Majorization of part lists

For finite lists $a = (a_1, \dots, a_s)$ and
$b = (b_1, \dots, b_t)$ of natural numbers, $a$ majorizes $b$, written $a \succ b$, when
$b_1 + \dots + b_k \le a_1 + \dots + a_k$ for every natural number $k \le \min\{s, t\}$.

No ordering of the lists is required; the source applies majorization to the parts of partitions
listed in decreasing order.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 3 (definition of majorization).

Formalized by `MetaMathlibExt.PartitionMajorizes`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#partition-majorizes).

## Majorization of $(2, 2)$ by $(3, 1)$

The partition $(3, 1)$ majorizes the partition
$(2, 2)$: $3 \ge 2$ and $3 + 1 \ge 2 + 2$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 3; characteristic check of `PartitionMajorizes`.

Formalized by `MetaMathlibExt.partitionMajorizes_three_one_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#partition-majorizes-three-one-two-two).

## Number of $k$-vn-arrangements

Let $k$ be a natural number and $M$ a finite multiset of
integers. A $k$-vn-arrangement of $M$ is a finite sequence $(v_1, \dots, v_b)$ of integers whose
multiset of entries is $M$ and with $v_{i+1} - v_i \le k$ for all $1 \le i < b$. This is the
number of distinct such sequences; sequences are compared entry by entry, so exchanging two
equal entries gives the same arrangement. For $k = 1$ these are the vn-arrangements.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 4 (definitions of vn-arrangement and k-vn-arrangement).

Formalized by `MetaMathlibExt.vnArrangementCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#vn-arrangement-count).

## A singleton multiset has one $k$-vn-arrangement

For every natural number $k$ and every
integer $a$, the one-element multiset $\{a\}$ has exactly one $k$-vn-arrangement.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Section 4; characteristic check of `vnArrangementCount`.

Formalized by `MetaMathlibExt.vnArrangementCount_singleton`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#vn-arrangement-count-singleton).

## Increments of the diagonal sequence

Let $\alpha$ be a partition of $n$ with diagonal
sequence $(d_k)_{k \ge 0}$, where $d_0 = 0$, and let $k \ge 0$. Then $d_{k+1} \le d_k + 1$, with
equality if and only if $d_j = j$ for every $j$ with $1 \le j \le k + 1$. Moreover, if
$d_{k+1} \le d_k$, then $d_{k+2} \le d_{k+1}$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Lemma 1.

Stated but not proved: `MetaMathlibExt.diagonalSequence_succ_le_and_antitone` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-sequence-succ-le-and-antitone).

## Existence and uniqueness of the diagonal normal form

Write $v^{(m)}$ for $m$ copies of
$v$. For every partition $\alpha$ of $n \ge 1$ there are an integer $q > 0$ and natural numbers
$s_1, \dots, s_q$ such that the diagonal sequence of $\alpha$, indexed from $0$, is
$(0, 1, 2, \dots, q, q^{(s_q)}, (q-1)^{(s_{q-1})}, \dots, 1^{(s_1)}, 0, 0, \dots)$ and
$q(q+1)/2 + \sum_{k=1}^{q} k s_k = n$. Moreover $q$ and $s_1, \dots, s_q$ are unique: if
$q' > 0$ and $s'_1, \dots, s'_{q'}$ give the same diagonal sequence, then $q' = q$ and
$s'_k = s_k$ for $1 \le k \le q$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 1.

Stated but not proved: `MetaMathlibExt.exists_unique_diagonalNormalForm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#exists-unique-diagonal-normal-form).

## The maximal partition has the prescribed diagonal normal form

Let $q > 0$ and let
$s_1, \dots, s_q$ be natural numbers with $q(q+1)/2 + \sum_{k=1}^{q} k s_k = n$, and let
$\bar\alpha = (\bar\alpha_1, \dots, \bar\alpha_q)$ with
$\bar\alpha_i = q - i + 1 + \sum_{k=i}^{q} s_k$. Then the entries of $\bar\alpha$ are positive,
sum to $n$ and are strictly decreasing; the diagonal sequence of $\bar\alpha$ is
$(1, 2, \dots, q, q^{(s_q)}, (q-1)^{(s_{q-1})}, \dots, 1^{(s_1)})$ followed by zeros, where
$v^{(m)}$ denotes $m$ copies of $v$; $s_i = \bar\alpha_i - \bar\alpha_{i+1} - 1$ for
$1 \le i < q$; and $s_q = \bar\alpha_q - 1$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 1.

Stated but not proved: `MetaMathlibExt.diagonalMaxPartition_spec` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-max-partition-spec).

## Counting diagonal sequences

For every natural number $n$, including $n = 0$, the number
of distinct diagonal sequences of partitions of $n$ equals the number of partitions of $n$ into
distinct parts, and the number of partitions of $n$ into distinct parts equals the number of
partitions of $n$ into odd parts.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 2.

Stated but not proved: `MetaMathlibExt.ncard_diagonalSequences_eq_card_distincts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#ncard-diagonal-sequences-eq-card-distinc).

## Conjugate of a partition with prescribed gaps between its parts

Let $q \ge 0$ and let
$s_1, \dots, s_q$ be natural numbers. The conjugate of the partition $\bar\alpha$ with parts
$\bar\alpha_i = q - i + 1 + \sum_{k=i}^{q} s_k$ for $1 \le i \le q$ is the partition
$\underline{\alpha} = (q^{(s_q + 1)}, (q-1)^{(s_{q-1} + 1)}, \dots, 1^{(s_1 + 1)})$, where
$v^{(r)}$ means $r$ copies of $v$; the parts are compared as multisets.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 2.

Stated but not proved: `MetaMathlibExt.conjugateParts_diagonalMaxPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#conjugate-parts-diagonal-max-partition).

## Equal diagonal sequences of the maximal and minimal partitions

Let $q \ge 0$ and
$s_1, \dots, s_q \ge 0$ be natural numbers, write $v^{(m)}$ for $m$ copies of $v$, and let
$\bar\alpha$ and $\underline\alpha$ be the partitions with parts
$\bar\alpha_i = q - i + 1 + s_i + s_{i+1} + \dots + s_q$ for $1 \le i \le q$ and
$\underline\alpha = (q^{(s_q + 1)}, (q-1)^{(s_{q-1} + 1)}, \dots, 1^{(s_1 + 1)})$. Then
$\bar\alpha$ and $\underline\alpha$ have the same diagonal sequence; this diagonal sequence,
indexed from $0$, is $(0, 1, 2, \dots, q, q^{(s_q)}, \dots, 1^{(s_1)}, 0, 0, \dots)$; and the
multiset of its nonzero entries $1, 2, \dots, q, q^{(s_q)}, \dots, 1^{(s_1)}$ equals the multiset
of parts of $\underline\alpha$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 3.

Stated but not proved: `MetaMathlibExt.diagonalSequence_max_eq_min_and_multiset` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-sequence-max-eq-min-and-multise).

## Repeated parts and large gaps in a diagonal class

Let $q \ge 0$ and
$s_1, \dots, s_q \ge 0$ be natural numbers, write $v^{(m)}$ for $m$ copies of $v$, and let
$\bar\alpha$ and $\underline\alpha$ be the partitions with parts
$\bar\alpha_i = q - i + 1 + s_i + s_{i+1} + \dots + s_q$ for $1 \le i \le q$ and
$\underline\alpha = (q^{(s_q + 1)}, (q-1)^{(s_{q-1} + 1)}, \dots, 1^{(s_1 + 1)})$. Let $\alpha$
be a partition of $n$ with parts $\alpha_1 \ge \dots \ge \alpha_t$, set $\alpha_{t+1} = 0$, and
suppose that the diagonal sequence of $\alpha$, indexed from $0$, is
$(0, 1, 2, \dots, q, q^{(s_q)}, \dots, 1^{(s_1)}, 0, 0, \dots)$. If $\alpha \ne \bar\alpha$, then
$\alpha_i = \alpha_{i+1}$ for some $i$ with $1 \le i < t$. If $\alpha \ne \underline\alpha$, then
$\alpha_i - \alpha_{i+1} \ge 2$ for some $i$ with $1 \le i \le t$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 4.

Stated but not proved: `MetaMathlibExt.exists_eq_succ_of_ne_diagonalMaxPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#exists-eq-succ-of-ne-diagonal-max-partit).

## The largest part of a partition with given diagonal sequence

Let $\alpha$ be a partition
of $n$, let $q$ and $s_1, s_2, \dots$ be natural numbers, and suppose the diagonal sequence of
$\alpha$ is $(1, 2, \dots, q, q^{(s_q)}, (q-1)^{(s_{q-1})}, \dots, 1^{(s_1)})$ followed by zeros,
where $v^{(m)}$ denotes $m$ copies of $v$. Then the largest part of $\alpha$ (taken to be $0$ if
$\alpha$ has no parts) lies in the set
$A_1 = \{q + \sum_{i=j}^{q} s_i : 1 \le j \le q + 1\}$, that is,
$A_1 = \{q, q + s_q, q + s_q + s_{q-1}, \dots, q + s_q + \dots + s_1\}$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 3.

Stated but not proved: `MetaMathlibExt.sup_parts_mem_diagonalFirstPartSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#sup-parts-mem-diagonal-first-part-set).

## Sums of squared parts and the diagonal sequence

Let $\alpha$ be a partition of $n$ with
diagonal sequence $(d_k)_{k \ge 1}$ and conjugate partition $\alpha^*$, and write $s(\gamma)$ for
the sum of the squares of the parts of a partition $\gamma$. Then
$s(\alpha) + s(\alpha^*) = 2 \sum_{k=1}^{2n} k \, d_k$. Consequently every partition $\beta$ of
$n$ with the same diagonal sequence as $\alpha$ satisfies
$s(\beta) + s(\beta^*) = s(\alpha) + s(\alpha^*)$.

The paper sums only up to the last diagonal $t + \alpha_1 - 1$, where $t$ is the number of parts
and $\alpha_1$ the largest part; summing to $2n$ adds only zero terms.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_sq_add_sum_sq_conjugate_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#sum-sq-add-sum-sq-conjugate-eq).

## Conjugation reverses majorization

For partitions $\alpha$ and $\beta$ of $n$, with parts
listed in decreasing order, $\alpha$ majorizes $\beta$ if and only if the conjugate partition
$\beta^*$ majorizes the conjugate partition $\alpha^*$, again with parts listed in decreasing
order.

This is Theorem 7.B.5 of Marshall, Olkin and Arnold, as quoted in the source.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, proof of Proposition 5 (citing [4], Theorem 7.B.5).

Stated but not proved: `MetaMathlibExt.partitionMajorizes_iff_conjugate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#partition-majorizes-iff-conjugate).

## The diagonal class lies between the maximal and minimal partitions in majorization

Let
$p$ be a partition of $n$, let $q$ be a natural number and $s = (s_k)$ a sequence of natural
numbers, and suppose that the diagonal sequence of $p$ is $(1, 2, \dots, q, q^{(s_q)},
(q-1)^{(s_{q-1})}, \dots, 1^{(s_1)})$ followed by zeros, where $v^{(m)}$ denotes $m$ copies of
$v$. Let $\alpha$ be the parts of $p$ in decreasing order, let
$\bar\alpha = (\bar\alpha_1, \dots, \bar\alpha_q)$ with
$\bar\alpha_i = q - i + 1 + \sum_{k=i}^{q} s_k$, and let
$\underline\alpha = (q^{(s_q + 1)}, (q-1)^{(s_{q-1} + 1)}, \dots, 1^{(s_1 + 1)})$. Then
$\bar\alpha \succ \alpha$ and $\alpha \succ \underline\alpha$, where for lists $a$ and $b$,
$a \succ b$ means $b_1 + \dots + b_k \le a_1 + \dots + a_k$ for every $k$ up to the length of
the shorter list.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 5.

Stated but not proved: `MetaMathlibExt.diagonalMaxPartition_majorizes_majorizes_min` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-max-partition-majorizes-majoriz).

## Counting vn-arrangements of a multiset

Let $t$ be a natural number, let $b_0, b_1, \dots$
be natural numbers, and let $M$ be the multiset of integers containing $b_i$ copies of $i$ for
each $0 \le i \le t$, so that $M$ has $m = b_0 + \dots + b_t$ elements. Then the number of
vn-arrangements of $M$, that is, orderings $(v_1, \dots, v_m)$ of $M$ with $v_{j+1} - v_j \le 1$
for all $j$, is $\prod_{i=0}^{t-1} \binom{b_i + b_{i+1}}{b_i}$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 6.

Stated but not proved: `MetaMathlibExt.vnArrangementCount_one_eq_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#vn-arrangement-count-one-eq-prod).

## Vn-arrangements of consecutive integers

For every integer $a$ and every natural number
$t \ge 1$, the set $\{a, a + 1, \dots, a + t - 1\}$ of $t$ consecutive integers has exactly
$2^{t-1}$ vn-arrangements, that is, orderings $(v_1, \dots, v_t)$ of its elements with
$v_{i+1} - v_i \le 1$ for all $i$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 5.

Stated but not proved: `MetaMathlibExt.vnArrangementCount_consecutive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#vn-arrangement-count-consecutive).

## Counting $k$-vn-arrangements of a multiset

Let $k \le t$ be natural numbers, let
$b_0, b_1, \dots$ be natural numbers, and let $M$ be the multiset of integers containing $b_i$
copies of $i$ for each $0 \le i \le t$, so that $M$ has $m = b_0 + \dots + b_t$ elements. Then
the number of $k$-vn-arrangements of $M$, that is, orderings $(v_1, \dots, v_m)$ of $M$ with
$v_{j+1} - v_j \le k$ for all $j$, is

$$
\binom{b_0 + \dots + b_k}{b_0, \dots, b_k} \prod_{i=1}^{t-k} \binom{b_i + \dots + b_{i+k}}{b_{i+k}}
$$

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 7.

Stated but not proved: `MetaMathlibExt.vnArrangementCount_eq_multinomial_mul_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#vn-arrangement-count-eq-multinomial-mul).

## Partitions in a diagonal class with as many parts as the initial staircase

Let $\alpha$
be a partition of $n$ with diagonal sequence $\delta(\alpha) = (d_j)_{j \ge 1}$, set $d_0 = 0$,
and let $q, L \ge 0$ be integers with $d_j = j$ for all $1 \le j \le q$, $d_{q+1} \ne q + 1$,
$d_L \ne 0$ and $d_{L+1} = 0$. Put $b_i = \max(d_i - d_{i+1}, 0)$. Then the number of partitions
of $n$ with exactly $q$ parts whose diagonal sequence equals $\delta(\alpha)$ is

$$\prod_{i=q}^{L-1} \binom{b_i + b_{i+1}}{b_i}.$$

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 8.

Stated but not proved: `MetaMathlibExt.card_diagonalClass_filter_card_parts_eq_q` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-filter-card-parts-eq).

## Partitions in a diagonal class with more parts than the initial staircase

Let $\alpha$
be a partition of $n$ with diagonal sequence $\delta(\alpha) = (d_j)_{j \ge 1}$, set $d_0 = 0$,
and let $q, L \ge 0$ be integers with $d_j = j$ for all $1 \le j \le q$, $d_{q+1} \ne q + 1$,
$d_L \ne 0$ and $d_{L+1} = 0$. Put $b_i = \max(d_i - d_{i+1}, 0)$. Then for every $k > q$ the
number of partitions of $n$ with exactly $k$ parts whose diagonal sequence equals
$\delta(\alpha)$ is

$$\binom{b_{k-1} + b_k}{b_{k-1} + 1} \prod_{i=q}^{k-2} \binom{b_i + b_{i+1} + 1}{b_i + 1}
\prod_{i=k}^{L-1} \binom{b_i + b_{i+1}}{b_i}.$$

For $k > L$ both sides are $0$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Proposition 9.

Stated but not proved: `MetaMathlibExt.card_diagonalClass_filter_card_parts_eq_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-filter-card-parts-eq-2).

## Number of partitions with a given diagonal sequence

Let $\alpha$ be a partition of $n$
with diagonal sequence $\delta(\alpha) = (d_j)_{j \ge 1}$, set $d_0 = 0$, and let $q, L \ge 0$ be
integers with $d_j = j$ for all $1 \le j \le q$, $d_{q+1} \ne q + 1$, $d_L \ne 0$ and
$d_{L+1} = 0$. Put $b_i = \max(d_i - d_{i+1}, 0)$. Then the number of partitions of $n$ whose
diagonal sequence equals $\delta(\alpha)$ is

$$\prod_{i=q}^{L-1} \binom{b_i + b_{i+1} + 1}{b_i + 1}.$$

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_diagonalClass_eq_prod_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-eq-prod-choose).

## Diagonal classes whose multiplicities are at least two

Let $q \ge 1$, let
$s = (s_1, s_2, \dots)$ be a sequence of natural numbers, and let $\alpha$ be a partition of $n$
whose diagonal sequence $\delta(\alpha) = (d_i)_{i \ge 1}$ is
$(1, 2, \dots, q, q^{(s_q)}, (q-1)^{(s_{q-1})}, \dots, 1^{(s_1)})$ followed by zeros, where
$v^{(r)}$ means $r$ copies of $v$. Put $L = q + s_1 + \dots + s_q$. If $s_i \ge 2$ for all
$1 \le i < q$, then exactly one partition of $n$ with diagonal sequence $\delta(\alpha)$ has
exactly $q$ parts; if moreover $s_q \ge 1$, then the number of partitions of $n$ with diagonal
sequence $\delta(\alpha)$ is $\prod_{i=q}^{L} (\max(d_i - d_{i+1}, 0) + 1)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 6 (1), (2).

Stated but not proved: `MetaMathlibExt.card_diagonalClass_of_two_le_s` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-of-two-le-s).

## Every positive integer is the size of a diagonal class

For every positive integer $m$
there are a natural number $n$ and a partition $\alpha$ of $n$ whose class, the set of partitions
of $n$ with the same diagonal sequence as $\alpha$, has exactly $m$ elements.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 6 (3).

Stated but not proved: `MetaMathlibExt.exists_card_diagonalClass_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#exists-card-diagonal-class-eq).

## Truncating the staircase of a diagonal sequence

For $m \ge 0$ and a sequence
$s = (s_1, s_2, \dots)$ of natural numbers, let $d(m, s)$ be the sequence
$(1, 2, \dots, m, m^{(s_m)}, (m-1)^{(s_{m-1})}, \dots, 1^{(s_1)})$ followed by zeros, where
$v^{(r)}$ means $r$ copies of $v$, and let $n(m, s) = m(m+1)/2 + \sum_{j=1}^{m} j s_j$. Let
$1 \le k < q$ with $s_k \ge 2$ and $s_j = 0$ for all $k < j \le q$. Then the number of partitions
of $n(q, s)$ with diagonal sequence $d(q, s)$ equals the number of partitions of $n(k, s)$ with
diagonal sequence $d(k, s)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 6 (4).

Stated but not proved: `MetaMathlibExt.card_diagonalClassOf_truncate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-of-truncate).

## Capping the multiplicities of a diagonal sequence at two

For $m \ge 0$ and a sequence
$s = (s_1, s_2, \dots)$ of natural numbers, let $d(m, s)$ be the sequence
$(1, 2, \dots, m, m^{(s_m)}, (m-1)^{(s_{m-1})}, \dots, 1^{(s_1)})$ followed by zeros, where
$v^{(r)}$ means $r$ copies of $v$, and let $n(m, s) = m(m+1)/2 + \sum_{j=1}^{m} j s_j$. Let
$q \ge 1$ and $\sigma_j = \min(s_j, 2)$ for all $j$. Then the number of partitions of $n(q, s)$
with diagonal sequence $d(q, s)$ equals the number of partitions of $n(q, \sigma)$ with diagonal
sequence $d(q, \sigma)$.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 6 (5).

Stated but not proved: `MetaMathlibExt.card_diagonalClassOf_min_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#card-diagonal-class-of-min-two).

## Diagonal classes of size at most three

Let $\alpha$ be a partition of $n \ge 1$, let
$d = \delta(\alpha)$ be its diagonal sequence, written without its trailing zeros, and let
$[\alpha]$ be the set of partitions of $n$ with diagonal sequence $d$, each written by its parts
in decreasing order. Here $v^{(r)}$ means $r$ copies of $v$, and a run $a, a - 1, \dots, b$ with
$a < b$ is empty.
(1) If $|[\alpha]| = 1$, then there is $q \ge 1$ with $n = \binom{q+1}{2}$,
$d = (1, 2, \dots, q)$ and $[\alpha] = \{(q, q - 1, \dots, 1)\}$.
(2) If $|[\alpha]| = 2$, then either there are $q \ge 1$ and $k \ge 2$ with
$n = \binom{q+1}{2} + k$, $d = (1, 2, \dots, q, 1^{(k)})$ and
$[\alpha] = \{(q + k, q - 1, \dots, 1), (q, q - 1, \dots, 1, 1^{(k)})\}$, or $n = 2$,
$d = (1, 1)$ and $[\alpha] = \{(2), (1, 1)\}$.
(3) If $|[\alpha]| = 3$, then either there are $q \ge 2$ and $k \ge 2$ with
$n = \binom{q+1}{2} + 2k$, $d = (1, 2, \dots, q, 2^{(k)})$ and $[\alpha] = \{(q + k, q - 1 + k,
q - 2, \dots, 1), (q, q - 1, \dots, 3, 2^{(k+1)}, 1), (q + k, q - 1, \dots, 2, 1^{(k+1)})\}$, or
$d = (1, 2, 1)$ and $[\alpha] = \{(3, 1), (2, 2), (2, 1, 1)\}$, or $d = (1, 2, 2)$ and
$[\alpha] = \{(3, 2), (3, 1, 1), (2, 2, 1)\}$.

Part (4) of the corollary, on classes of size $4$, is false as printed and is not included.

## Sources

- Michael Neubauer and Harmony Vargas, *Diagonal Sequences of Integer Partitions*, INTEGERS 25 (2025), Article A60, Corollary 7 (1)–(3).

Stated but not proved: `MetaMathlibExt.diagonalClass_classification_card_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/DiagonalSequencesWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html#diagonal-class-classification-card-le-th).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diagonal sequences of integer partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/diagonal-sequences-of-integer-partitions)
