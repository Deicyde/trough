---
declaration: section
origin: cited
lean: MetaMathlibExt.symConsEmbedding, MetaMathlibExt.fixedPerimeterPartitions, MetaMathlibExt.mem_fixedPerimeterPartitions, MetaMathlibExt.card_fixedPerimeterPartitions_three, MetaMathlibExt.IsDDistinctParts, MetaMathlibExt.isDDistinctParts_examples, MetaMathlibExt.perimeterDistinctCount, MetaMathlibExt.perimeterDistinctArmLegCount
statement: formalized
---

# Alder-type inequalities for fixed perimeter partitions

23 results, 13 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html).

## Prepending a part to a multiset

For natural numbers $m$ and $k$, the map that sends a
multiset $t$ of $k$ natural numbers to the multiset obtained from $t$ by adding one copy of $m$
is injective, so it embeds the multisets of size $k$ into all multisets of natural numbers.

With $m$ the largest part, it builds the partitions of a given perimeter from their largest part
and their remaining parts.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1 (a partition is determined by its largest part and its remaining parts).

Formalized by `MetaMathlibExt.symConsEmbedding`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#sym-cons-embedding).

## Partitions with fixed perimeter

The perimeter of a partition is its largest part plus its
number of parts minus $1$. For a natural number $n$, the partitions with perimeter $n$ form the
finite set of all finite multisets $s$ of positive integers whose largest element plus number of
elements (counted with multiplicity) equals $n + 1$.

The set is enumerated directly: for each number of parts $k = 1, \dots, n$ the largest part is
$n + 1 - k$, and it is prepended to a multiset of $k - 1$ parts from $1, \dots, n + 1 - k$, so the
$2^{n-1}$ partitions with perimeter $n$ (for $n \ge 1$) are listed without filtering or
deduplication.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1 (perimeter `Γ(π) = α(π) + λ(π) - 1`).

Formalized by `MetaMathlibExt.fixedPerimeterPartitions`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#fixed-perimeter-partitions).

## Membership in the partitions with fixed perimeter

Let $n$ be a natural number and $s$ a
finite multiset of natural numbers. Then $s$ is a partition with perimeter $n$ if and only if
every element of $s$ is positive and the largest element of $s$ (taken to be $0$ if $s$ is empty)
plus the number of elements of $s$, counted with multiplicity, equals $n + 1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.

Formalized by `MetaMathlibExt.mem_fixedPerimeterPartitions`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#mem-fixed-perimeter-partitions).

## The partitions of perimeter three

There are exactly four partitions with perimeter $3$,
that is, four finite multisets of positive integers whose largest element plus number of elements
(counted with multiplicity) equals $4$.

They are $3$, $2 + 1$, $2 + 2$ and $1 + 1 + 1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.

Formalized by `MetaMathlibExt.card_fixedPerimeterPartitions_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#card-fixed-perimeter-partitions-three).

## Partitions into d-distinct parts

Let $d$ be a natural number. A finite multiset $s$ of
natural numbers has $d$-distinct parts when no element occurs in $s$ more than once and any two
elements $x < y$ of $s$ satisfy $x + d \le y$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1 (`d`-distinct parts, as in Alder's `q_d(n)`).

Formalized by `MetaMathlibExt.IsDDistinctParts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#is-ddistinct-parts).

## Examples of 2-distinct partitions

The partition $5 + 3$ has $2$-distinct parts, and the
partition $4 + 3$ does not.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.

Formalized by `MetaMathlibExt.isDDistinctParts_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#is-ddistinct-parts-examples).

## Fixed perimeter partitions into $d$-distinct parts

For natural numbers $d$, $a$ and $n$,
$h_d^{(a)}(n)$ is the number of partitions of perimeter $n$ into $d$-distinct parts that are all
at least $a$. Here the perimeter of a partition is its largest part plus its number of parts
minus $1$, and a partition has $d$-distinct parts when no part repeats and any two parts differ
by at least $d$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Equation (1.1).

Formalized by `MetaMathlibExt.perimeterDistinctCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-count).

## Partitions into d-distinct parts by largest part and length

For natural numbers $d$, $a$,
$m$ and $k$, $h_d^{(a)}(m, k)$ is the number of nonempty finite multisets of positive integers with
largest element $m$, exactly $k$ elements counted with multiplicity, all elements at least $a$,
and $d$-distinct parts. Such a partition has perimeter $m + k - 1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.1 (refinement of (1.1)).

Formalized by `MetaMathlibExt.perimeterDistinctArmLegCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-arm-leg-count).

## Fixed perimeter partitions into parts in one residue class

For natural numbers $d$, $a$
and $n$, $f_d^{(a)}(n)$ is the number of partitions with perimeter $n$ all of whose parts are
congruent to $a$ modulo $d + 1$. Here a partition is a nonempty multiset of positive integers,
and its perimeter is its largest part plus its number of parts minus one.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Equation (1.2).

Formalized by `MetaMathlibExt.perimeterResidueCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-residue-count).

## Partitions into parts in one residue class, by largest part and length

For natural
numbers $d$, $a$, $m$ and $k$, $f_d^{(a)}(m, k)$ is the number of nonempty multisets of positive
integers with largest part $m$ and exactly $k$ elements (counted with multiplicity), all of
which are congruent to $a$ modulo $d + 1$.

Such a partition has perimeter (largest part plus number of parts minus one) equal to
$m + k - 1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.1 (refinement of (1.2)).

Formalized by `MetaMathlibExt.perimeterResidueArmLegCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-residue-arm-leg-count).

## Fixed perimeter partitions into parts $\equiv \pm a \pmod{d+3}$

For natural numbers
$d$, $a$ and $n$, $\ell_d^{(a)}(n)$ is the number of partitions of perimeter $n$ into parts
congruent to $a$ or $-a$ modulo $d + 3$, where the perimeter of a partition is its largest part
plus its number of parts minus $1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Equation (1.3).

Formalized by `MetaMathlibExt.perimeterPMResidueCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-pmresidue-count).

## Partitions into parts $\equiv \pm a \pmod{d+3}$ by largest part and number of parts

For
natural numbers $d$, $a$, $\alpha$ and $\lambda$, $\ell_d^{(a)}(\alpha, \lambda)$ is the number of
nonempty partitions into parts congruent to $a$ or $-a$ modulo $d + 3$ with largest part $\alpha$
and exactly $\lambda$ parts (so $\ell_d^{(a)}(0, 0) = 0$: the empty partition is not counted).

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Section 1.1 (refinement of (1.3)).

Formalized by `MetaMathlibExt.perimeterPMResidueArmLegCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-pmresidue-arm-leg-count).

## Small values of the fixed-perimeter partition counts

Take $d = a = 1$. Among the
partitions with perimeter $3$, exactly two have $1$-distinct parts that are all at least $1$,
exactly two have all parts congruent to $1$ modulo $2$, and exactly two have all parts congruent
to $1$ or $-1$ modulo $4$. Moreover, exactly one partition with largest part $2$ and $2$ parts has
$1$-distinct parts that are all at least $1$, exactly one partition with largest part $3$ and $1$
part has all parts congruent to $1$ modulo $2$, and exactly one partition with largest part $1$
and $3$ parts has all parts congruent to $1$ or $-1$ modulo $4$.

The partitions counted in the last three cases are $2 + 1$, $3$ and $1 + 1 + 1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Equations (1.1)–(1.3).

Formalized by `MetaMathlibExt.perimeterCounts_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-counts-small-values).

## Fixed-perimeter identity for $d$-distinct parts

Let $d$ and $n$ be positive integers and
let $a$ be an integer with $1 \le a \le d + 1$. Then the number $h_d^{(a)}(n)$ of partitions of
perimeter $n$ into $d$-distinct parts (no part repeats and any two parts differ by at least $d$),
all at least $a$, equals the number $f_d^{(a)}(n)$ of partitions of perimeter $n$ into parts
congruent to $a$ modulo $d + 1$. Here the perimeter of a partition is its largest part plus its
number of parts minus $1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Theorem 1.

Stated but not proved: `MetaMathlibExt.perimeterDistinctCount_eq_perimeterResidueCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-count-eq-perimeter-re).

## Refined equality of distinct-part and residue counts

Let $d$, $a$, $m$ and $k$ be natural
numbers with $d \ge 1$, $1 \le a \le d + 1$, $m \ge 1$ and $k \ge 1$. Write $h_d^{(a)}(m, k)$ for
the number of partitions into $d$-distinct parts, all at least $a$, with largest part $m$ and $k$
parts, and $f_d^{(a)}(m, k)$ for the number of partitions into parts congruent to $a$ modulo
$d + 1$ with largest part $m$ and $k$ parts. Then
$h_d^{(a)}(m, k) = f_d^{(a)}(a + (d + 1)(k - 1), j)$, where $j = \max(m + 1 - a - d(k - 1), 0)$.

In the source the second argument is $m + 1 - a - d(k - 1)$; it is replaced by $0$ when it is not
positive, and then both sides vanish.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Theorem 1.

Stated but not proved: `MetaMathlibExt.perimeterDistinctArmLegCount_eq_perimeterResidueArmLegCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-arm-leg-count-eq-peri).

## Counting d-distinct partitions by largest part and length

Let $d$, $a$, $m$ and $k$ be
positive integers with $a \le d + 1$, and write $h_d^{(a)}(m, k)$ for the number of partitions into
$d$-distinct parts, all at least $a$, with largest part $m$ and $k$ parts. Then
$h_d^{(a)}(m, k) \ne 0$ if and only if $m \ge a + d(k - 1)$, and in that case
$h_d^{(a)}(m, k) = \binom{m - a - (d - 1)(k - 1)}{k - 1}$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Lemma 1.

Stated but not proved: `MetaMathlibExt.perimeterDistinctArmLegCount_ne_zero_iff_and_eq_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-arm-leg-count-ne-zero).

## Nonvanishing and binomial count for parts $\equiv a \pmod{d+1}$

Let $d$, $a$, $\alpha$
and $\lambda$ be positive integers with $a \le d + 1$, and let $f_d^{(a)}(\alpha, \lambda)$ be the
number of partitions into parts congruent to $a$ modulo $d + 1$ with largest part $\alpha$ and
exactly $\lambda$ parts. Then $f_d^{(a)}(\alpha, \lambda) \ne 0$ if and only if $\alpha \ge a$ and
$\alpha \equiv a \pmod{d + 1}$, and in that case
$f_d^{(a)}(\alpha, \lambda) = \binom{(\alpha - a)/(d + 1) + \lambda - 1}{\lambda - 1}$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Lemma 2.

Stated but not proved: `MetaMathlibExt.perimeterResidueArmLegCount_ne_zero_iff_and_eq_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-residue-arm-leg-count-ne-zero).

## A floor inequality for perimeter counts

Let $d$, $a$ and $n$ be natural numbers with
$d \ge 1$, $a \ge 1$, $2a < d + 3$ and $a \le n$. Then
$\lfloor \lfloor (n - a)/(d + 1) \rfloor / 2 \rfloor \le \lfloor (n - a)/(d + 3) \rfloor$
and
$\lfloor (\lfloor (n - a)/(d + 1) \rfloor + 1) / 2 \rfloor \le \lfloor (n + a)/(d + 3) \rfloor$.

The lower bounds by $0$ in the source hold automatically and are not stated.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Lemma 3.

Stated but not proved: `MetaMathlibExt.floor_half_div_le_div_of_two_mul_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#floor-half-div-le-div-of-two-mul-lt).

## Nonvanishing and binomial count for parts $\equiv \pm a \pmod{d+3}$

Let $d$, $a$,
$\alpha$ and $\lambda$ be positive integers with $a < (d + 3)/2$, and let
$\ell_d^{(a)}(\alpha, \lambda)$ be the number of partitions into parts congruent to $a$ or $-a$
modulo $d + 3$ with largest part $\alpha$ and exactly $\lambda$ parts. Then
$\ell_d^{(a)}(\alpha, \lambda) \ne 0$ if and only if $\alpha \ge a$ and
$\alpha \equiv \pm a \pmod{d + 3}$. Moreover, if $\alpha \ge a$ and $\alpha \equiv a \pmod{d + 3}$,
then $\ell_d^{(a)}(\alpha, \lambda) = \binom{2(\alpha - a)/(d + 3) + \lambda - 1}{\lambda - 1}$,
and if $\alpha \ge a$ and $\alpha \equiv -a \pmod{d + 3}$, then
$\ell_d^{(a)}(\alpha, \lambda) = \binom{2(\alpha + a)/(d + 3) + \lambda - 2}{\lambda - 1}$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Lemma 4.

Stated but not proved: `MetaMathlibExt.perimeterPMResidueArmLegCount_ne_zero_iff_and_eq_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-pmresidue-arm-leg-count-ne-zer).

## Reverse Alder-type inequality for fixed perimeter partitions

Let $d$, $n$ and $a$ be
positive integers with $a < (d + 3)/2$. Then the number $h_d^{(a)}(n)$ of partitions of perimeter
$n$ into $d$-distinct parts (no part repeats and any two parts differ by at least $d$), all at
least $a$, is at most the number $\ell_d^{(a)}(n)$ of partitions of perimeter $n$ into parts
congruent to $a$ or $-a$ modulo $d + 3$. Here the perimeter of a partition is its largest part
plus its number of parts minus $1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Theorem 2.

Stated but not proved: `MetaMathlibExt.perimeterDistinctCount_le_perimeterPMResidueCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-count-le-perimeter-pm).

## Monotonicity of fixed perimeter counts with $d$-distinct parts

For natural numbers
$d$, $a$ and $n$, let $h_d^{(a)}(n)$ be the number of partitions of perimeter $n$ (largest part
plus number of parts minus $1$) into $d$-distinct parts, all at least $a$, where parts are
$d$-distinct when no part repeats and any two parts differ by at least $d$. If $d$, $n$ and $a$
are positive, then $h_d^{(a+1)}(n) \le h_d^{(a)}(n)$, $h_{d+1}^{(a)}(n) \le h_d^{(a)}(n)$ and
$h_d^{(a)}(n) \le h_d^{(a)}(n + 1)$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Proposition 1.

Stated but not proved: `MetaMathlibExt.perimeterDistinctCount_shift_inequalities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-distinct-count-shift-inequalit).

## Monotonicity of fixed perimeter counts with parts $\equiv \pm a \pmod{d+3}$

For natural
numbers $d$, $a$ and $n$, let $\ell_d^{(a)}(n)$ be the number of partitions of perimeter $n$
(largest part plus number of parts minus $1$) into parts congruent to $a$ or $-a$ modulo $d + 3$.
If $d$, $n$ and $a$ are positive with $a < (d + 3)/2$, then
$\ell_d^{(a)}(n) \le \ell_d^{(a)}(n + 1)$ and $\ell_{d+1}^{(a)}(n) \le \ell_d^{(a)}(n)$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Proposition 1.

Stated but not proved: `MetaMathlibExt.perimeterPMResidueCount_shift_inequalities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-pmresidue-count-shift-inequali).

## Alder-type inequality in the degenerate case $a = (d + 3)/2$

Let $n$ be a positive
integer, let $d$ be an odd natural number and put $a = (d + 3)/2$. Then the number
$\ell_d^{(a)}(n)$ of partitions of perimeter $n$ into parts congruent to $a$ or $-a$ modulo
$d + 3$ is at most the number $h_d^{(a)}(n)$ of partitions of perimeter $n$ into $d$-distinct
parts (no part repeats and any two parts differ by at least $d$), all at least $a$. Here the
perimeter of a partition is its largest part plus its number of parts minus $1$.

## Sources

- Ling Chen, Isabelle Hernandez, Zain Shields, and Holly Swisher, *Analogues of Alder-Type Partition Inequalities for Fixed Perimeter Partitions*, INTEGERS 24 (2024), Article A102, Proposition 2.

Stated but not proved: `MetaMathlibExt.perimeterPMResidueCount_le_perimeterDistinctCount_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FixedPerimeterAlderWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html#perimeter-pmresidue-count-le-perimeter-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alder-type inequalities for fixed perimeter partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities/alder-type-inequalities-for-fixed-perimeter-part)
