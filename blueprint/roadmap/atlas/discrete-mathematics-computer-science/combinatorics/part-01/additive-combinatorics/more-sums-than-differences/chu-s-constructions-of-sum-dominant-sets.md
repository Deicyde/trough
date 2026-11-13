---
declaration: section
origin: cited
lean: MetaMathlibExt.setOfConsecutiveDifferences, MetaMathlibExt.setOfConsecutiveDifferences_cons, MetaMathlibExt.setOfConsecutiveDifferences_example, MetaMathlibExt.chuBlock, MetaMathlibExt.chuBlock_one_two, MetaMathlibExt.chu_family_balanced, MetaMathlibExt.chu_family_difference_dominated, MetaMathlibExt.chu_family_mstd_increasing
statement: formalized
---

# Chu's constructions of sum-dominant sets

20 results, 7 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html).

## Sets given by consecutive differences

For an integer $a$ and natural numbers
$g_1, \dots, g_r$, the set $(a \mid g_1, \dots, g_r)$ is the finite set of integers
$\{a, a + g_1, a + g_1 + g_2, \dots, a + g_1 + \dots + g_r\}$; for $r = 0$ it is $\{a\}$.

When every $g_i$ is positive, the differences between consecutive elements of this set, listed
from the smallest element to the largest, are $g_1, \dots, g_r$; a zero gap repeats a partial
sum, which the set records once.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 1 (Spohn's notation).

Formalized by `MetaMathlibExt.setOfConsecutiveDifferences`, a definition declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#set-of-consecutive-differences).

## Prepending a gap

For an integer $a$ and natural numbers $g_1, \dots, g_r$ ($r \ge 0$),
write $(a \mid g_1, \dots, g_r)$ for the set of partial sums
$\{a, a + g_1, \dots, a + g_1 + \dots + g_r\}$. Then for every natural number $g$,
$(a \mid g, g_1, \dots, g_r) = \{a\} \cup (a + g \mid g_1, \dots, g_r)$.

When $g > 0$, the new element $a$ is smaller than every element of $(a + g \mid g_1, \dots, g_r)$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 1 (Spohn's notation).

Formalized by `MetaMathlibExt.setOfConsecutiveDifferences_cons`, a theorem declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#set-of-consecutive-differences-cons).

## An example of difference notation

The set with least element $0$ and consecutive
differences $1, 5, 1, 1, 9, 7$ is $(0 \mid 1, 5, 1, 1, 9, 7) = \{0, 1, 6, 7, 8, 17, 24\}$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 1 (Spohn's notation).

Formalized by `MetaMathlibExt.setOfConsecutiveDifferences_example`, a theorem declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#set-of-consecutive-differences-example).

## Chu difference block

For a natural number $k$, the difference block $M^k$ is the list of
natural numbers $1, 4, \ldots, 4, 3$ of length $k + 2$: a $1$, then $k$ copies of $4$, then a $3$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 1 (definition of `M^k`).

Formalized by `MetaMathlibExt.chuBlock`, a definition declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-block).

## The Chu difference blocks $M^1$ and $M^2$

The Chu difference block $M^1$ is the list
$1, 4, 3$, and the Chu difference block $M^2$ is the list $1, 4, 4, 3$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 1 (definition of `M^k`).

Formalized by `MetaMathlibExt.chuBlock_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-block-one-two).

## A balanced family of Chu et al

Let $k$ be a positive integer and let
$A = (0 \mid 1, 1, 2, M^k, M^{k+1}, 1, 1) \subseteq \mathbb{Z}$ be the set of partial sums,
starting at $0$, of the difference sequence formed by $1, 1, 2$, the Chu difference blocks $M^k$
and $M^{k+1}$, and $1, 1$. Then $A$ is balanced: $|A + A| = |A - A|$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 1.

Stated but not proved: `MetaMathlibExt.chu_family_balanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-balanced).

## A difference-dominated family of Chu et al

Let $k$ be a positive integer and let
$A = (0 \mid 1, 1, 2, M^k, M^{k+1}, M^{k+1}, 1, 1) \subseteq \mathbb{Z}$ be the set of partial
sums, starting at $0$, of the difference sequence formed by $1, 1, 2$, the Chu difference blocks
$M^k$, $M^{k+1}$ and $M^{k+1}$, and $1, 1$. Then $A$ is difference-dominated:
$|A + A| < |A - A|$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 2.

Stated but not proved: `MetaMathlibExt.chu_family_difference_dominated` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-difference-dominated).

## MSTD sets with $M^k$ before $M^{k+1}$ (Theorem 3)

Let $k$ be a positive integer, let
$M^n$ denote the block $1, 4, \dots, 4, 3$ with $n$ fours, and let $M_1$ be one of the
sequences $(1, 1, 2)$, $(1, 1, 2, 1)$. Let $A = (0 \mid 1, 1, 2, M^k, M^{k+1}, M_1)$ be the set
of partial sums, starting from $0$, of the concatenated sequence $1, 1, 2, M^k, M^{k+1}, M_1$.
Then $A$ is sum-dominated: $|A - A| < |A + A|$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 3.

Stated but not proved: `MetaMathlibExt.chu_family_mstd_increasing` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-mstd-increasing).

## MSTD sets with $M^{k+1}$ before $M^k$ (Theorem 4)

Let $k$ be a positive integer, let
$M^n$ denote the block $1, 4, \dots, 4, 3$ with $n$ fours, and let $M_1$ be one of the
sequences $(1, 1)$, $(1, 1, 2)$, $(1, 1, 2, 1)$. Let $A = (0 \mid 1, 1, 2, M^{k+1}, M^k, M_1)$
be the set of partial sums, starting from $0$, of the concatenated sequence
$1, 1, 2, M^{k+1}, M^k, M_1$. Then $A$ is sum-dominated: $|A - A| < |A + A|$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 4.

Stated but not proved: `MetaMathlibExt.chu_family_mstd_decreasing` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-mstd-decreasing).

## Kumar–Mohan–Pandey sets

For natural numbers $k$, $l$, $t$, let $M^n$ be the block
$1, 4, \dots, 4, 3$ with $n$ fours, and let $D$ be the sequence made of $t$ copies of the block
$1, 1, 2, M^k, \dots, M^k$ (with $l$ copies of $M^k$) followed by $1, 1, 2, 1$. The set
$A_{k,l,t}$ is $(0 \mid D)$, the set of partial sums of $D$ starting from $0$.

Each block $1, 1, 2, M^k, \dots, M^k$ has sum $4(kl + l + 1)$, matching the bounds
$t(kl + l + 1)$ in Lemmas 1-7 of the paper.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 3 (the set of Lemmas 1-7 and Theorems 6-7).

Formalized by `MetaMathlibExt.chuFamilyKLT`, a definition declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt).

## The Kumar–Mohan–Pandey set $A_{1,1,1}$

For $k = l = t = 1$, the Kumar–Mohan–Pandey set
$A_{1,1,1}$, the set of partial sums starting from $0$ of the sequence
$1, 1, 2, 1, 4, 3, 1, 1, 2, 1$, is $\{0, 1, 2, 4, 5, 9, 12, 13, 14, 16, 17\}$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Section 3 (the set of Lemmas 1-7 and Theorems 6-7).

Formalized by `MetaMathlibExt.chuFamilyKLT_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-one-one-one).

## Differences in the Kumar–Mohan–Pandey sets (Lemma 1)

Let $k$, $l$, $t$ be positive
integers, let $A = A_{k,l,t}$ be the Kumar–Mohan–Pandey set, and put $T = t(kl + l + 1)$. Then
the difference set $A - A$ contains $4i$ and $1 + 4i$ for every integer $i$ with
$1 \le i \le 1 + T$, and contains $3 + 4i$ for every integer $i$ with $0 \le i \le T$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 1.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_mem_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-mem-sub).

## Positive differences of the form 6 + 4m in the Chu family set

Let $k$, $l$, $t$ be
positive integers and let $A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$,
$t$. Then exactly $lt + t$ elements $d$ of $A - A$ satisfy $d \ge 6$ and $d \equiv 2 \pmod 4$;
that is, exactly $lt + t$ positive differences of $A$ have the form $6 + 4m$ with $m \ge 0$ an
integer.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 3.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_card_sub_six_add_four_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-card-sub-six-add-four-mul).

## Elements of the Kumar–Mohan–Pandey sets (Lemma 4)

Let $k$, $l$, $t$ be positive
integers, let $A = A_{k,l,t}$ be the Kumar–Mohan–Pandey set, and put $T = t(kl + l + 1)$. Then
$1 + 4i \in A$ for every integer $i$ with $0 \le i \le 1 + T$, and $2 + 4T \in A$ and
$4 + 4T \in A$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 4.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-mem).

## Elements of the sumset of the Chu family set

Let $k$, $l$, $t$ be positive integers, let
$A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$, $t$, and let
$T = t(kl + l + 1)$. Then $1 + 4i$ and $2 + 4i$ lie in $A + A$ for every integer $i$ with
$0 \le i \le 2 + 2T$, and $3 + 4i$ lies in $A + A$ for every integer $i$ with $0 \le i \le 1 + 2T$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 5.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_mem_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-mem-add).

## Block starting points of the Chu family set

Let $k$, $l$, $t$ be positive integers and
let $A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$, $t$. Then
$4 + (4k + 4)i + (4kl + 4l + 4)j \in A$ for all integers $i$, $j$ with $0 \le i \le l$ and
$0 \le j \le t - 1$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 6.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_mem_block_starts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-mem-block-starts).

## Size of the difference set of the Chu family set

Let $k$, $l$, $t$ be positive integers
and let $A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$, $t$. Then
$|A - A| = 11 + 6klt + 8lt + 8t$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 6.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_card_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-card-sub).

## Lower bound for the sumset of the Chu family set

Let $k$, $l$, $t$ be positive integers
and let $A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$, $t$. Then
$|A + A| \ge 11 + 6klt + 10lt + 8t$.

Together with $|A - A| = 11 + 6klt + 8lt + 8t$ (Theorem 6), this shows that $A$ is sum-dominated
(MSTD): $|A + A| > |A - A|$.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Theorem 7.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_card_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-card-add).

## Six disjoint families in the sumset of the Chu family set

Let $k$, $l$, $t$ be positive
integers, let $A \subseteq \mathbb{Z}$ be the Chu family set with parameters $k$, $l$, $t$, and
let $P = 8kl + 8l + 8$. Let $X_1$, $X_2$, $X_4$, $X_5$ be the sets of the integers
$Pj + (4k + 4)i + 4$, $Pj + (4k + 4)i + 8$, $Pj + 4kl + 4l + (4k + 4)i + 8$ and
$Pj + 4kl + 4l + (4k + 4)i + 12$ respectively, for $1 \le i \le l$ and $0 \le j \le t - 1$, and
let $X_3$, $X_6$ be the sets of the integers $Pj + 4kl + 4l + 12$ and $Pj + 8kl + 8l + 16$
respectively, for $0 \le j \le t - 1$. Then $A + A$ contains $\{0, 4, 8\}$ and each of
$X_1, \ldots, X_6$, and the sets $X_1, \ldots, X_6$ are pairwise disjoint.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Lemma 7.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_add_supset_six_families` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-add-supset-six-families).

## Two families of runs with the same sums (Proposition 1)

Let $k$, $l$, $t$ be natural
numbers, let $M^k$ be the block $1, 4, \dots, 4, 3$ with $k$ fours, and let $B$ be the
concatenation of $l$ copies of $M^k$. For $j \ge 1$ let $R_1(j)$ be the sequence $1, 1$ followed
by $j$ copies of $2, B, 1, 1$, and let $R_3(j)$ be the sequence $2$ followed by $j$ copies of
$B, 1, 1, 2$. Then the sums of the entries of $R_1(j)$ for $1 \le j \le t$ form the same set as
the sums of the entries of $R_3(j)$ for $1 \le j \le t$.

In the paper, $R_1$ and $R_3$ are runs of consecutive differences of the set of Lemma 2, so
they give the same positive differences of that set. The paper's hypothesis $k, l, t \ge 1$ is
not needed.

## Sources

- Manish Kumar, Mohan and Ram Krishna Pandey, *A Conjecture of Chu et al. and a New Family of MSTD Sets*, INTEGERS 24 (2024), Article A32, Proposition 1.

Stated but not proved: `MetaMathlibExt.chuFamilyKLT_run_sums_R1_eq_R3` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ChuMSTDFamiliesWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html#chu-family-klt-run-sums-r1-eq-r3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chu's constructions of sum-dominant sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/chu-s-constructions-of-sum-dominant-sets)
