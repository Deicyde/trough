---
declaration: section
origin: cited
lean: MetaMathlibExt.IsWeightedZeroSumFree, MetaMathlibExt.weightedDavenport, MetaMathlibExt.weightedDavenport_eq_natCast_sInf, MetaMathlibExt.IsWeightedZeroSumFree.take, MetaMathlibExt.weightedDavenport_le, MetaMathlibExt.lt_weightedDavenport, MetaMathlibExt.weightedDavenport_eq_top_iff, MetaMathlibExt.weightedDavenport_zmod_one
statement: formalized
---

# Weighted Davenport constant

124 results, 21 proved and 103 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/index.html).

## Weighted zero-sum free sequences

Let $G$ be an additive commutative monoid and $A$ a
finite set of natural numbers. A finite sequence $s = (s_1, \dots, s_n)$ over $G$ is
$A$-weighted zero-sum free when, for every non-empty set $I \subseteq \{1, \dots, n\}$ of
positions and every choice of weights $a_i \in A$ for $i \in I$, the weighted sum
$\sum_{i \in I} a_i s_i$ is non-zero, where $a_i s_i$ is the sum of $a_i$ copies of $s_i$.
Terms are indexed by position, so repeated terms count separately.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (weighted zero-sum subsequences, as used in Lemmas 2 and 3).

Formalized by `MetaMathlibExt.IsWeightedZeroSumFree`, a definition declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#is-weighted-zero-sum-free).

## Weighted Davenport constant

Let $G$ be an additive commutative monoid and $A$ a finite
set of natural numbers. The $A$-weighted Davenport constant $D_A(G) \in \mathbb{N} \cup \{\infty\}$
is the least length $\ell \in \mathbb{N}$ such that no sequence over $G$ of length $\ell$ is
$A$-weighted zero-sum free, that is, such that every sequence over $G$ of length $\ell$ has a
non-empty $A$-weighted zero-sum subsequence; it is $\infty$ when no such length exists.

For example $D_A(G) = \infty$ when $A = \emptyset$, or when $A = \{1\}$ and $G = \mathbb{Z}$. For
a finite group $G$ and a non-empty weight set $A$ it is finite. The ordinary Davenport constant of
$G$ is $D_{\{1\}}(G)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.weightedDavenport`, a definition declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport).

## The weighted Davenport constant as a least length

Let $G$ be an additive commutative
monoid, $A$ a finite set of natural numbers and $D_A(G)$ the $A$-weighted Davenport constant
of $G$. If there is a length $\ell \in \mathbb{N}$ such that no sequence over $G$ of length
$\ell$ is $A$-weighted zero-sum free, then $D_A(G)$ is finite and equals the least such length.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.weightedDavenport_eq_natCast_sInf`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport-eq-nat-cast-s-inf).

## Prefixes of weighted zero-sum free sequences

Let $G$ be an additive commutative monoid
and $A$ a finite set of natural numbers. If a sequence $s$ over $G$ is $A$-weighted zero-sum
free, then for every $\ell \in \mathbb{N}$ the prefix of $s$ formed by its first $\ell$ terms
(all of $s$ when $\ell$ is at least its length) is $A$-weighted zero-sum free.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.IsWeightedZeroSumFree.take`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#take).

## Upper bound for the weighted Davenport constant

Let $G$ be an additive commutative
monoid, $A$ a finite set of natural numbers, $D_A(G)$ the $A$-weighted Davenport constant of
$G$ and $\ell$ a natural number. If no sequence over $G$ of length $\ell$ is $A$-weighted
zero-sum free, that is, every sequence over $G$ of length $\ell$ has a non-empty $A$-weighted
zero-sum subsequence, then $D_A(G) \le \ell$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.weightedDavenport_le`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport-le).

## Lower bound for the weighted Davenport constant

Let $G$ be an additive commutative
monoid, $A$ a finite set of natural numbers and $D_A(G)$ the $A$-weighted Davenport constant
of $G$. If a sequence over $G$ of length $L$ is $A$-weighted zero-sum free, then $L < D_A(G)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.lt_weightedDavenport`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#lt-weighted-davenport).

## When the weighted Davenport constant is infinite

Let $G$ be an additive commutative
monoid, $A$ a finite set of natural numbers and $D_A(G)$ the $A$-weighted Davenport constant
of $G$. Then $D_A(G) = \infty$ if and only if for every $\ell \in \mathbb{N}$ there is an
$A$-weighted zero-sum free sequence over $G$ of length $\ell$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (definition of `D_A(G)`).

Formalized by `MetaMathlibExt.weightedDavenport_eq_top_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport-eq-top-iff).

## Weighted Davenport constant of the trivial group

For every non-empty finite set $A$ of
natural numbers, the $A$-weighted Davenport constant of the trivial group $\mathbb{Z}/1\mathbb{Z}$
is $D_A(\mathbb{Z}/1\mathbb{Z}) = 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (characteristic value of `D_A`).

Formalized by `MetaMathlibExt.weightedDavenport_zmod_one`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport-zmod-one).

## Davenport constant of the group of order two

The ordinary Davenport constant of
$\mathbb{Z}/2\mathbb{Z}$, that is, its $\{1\}$-weighted Davenport constant, is
$D_{\{1\}}(\mathbb{Z}/2\mathbb{Z}) = 2$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Section 2 (characteristic value of `D_A`).

Formalized by `MetaMathlibExt.weightedDavenport_singleton_one_zmod_two`, a theorem declared in [MathlibExt/Combinatorics/Additive/WeightedDavenport.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/WeightedDavenport.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-davenport-singleton-one-zmod-tw).

## Units modulo n

For a natural number $n$, $U(n)$ is the set of units of the ring
$\mathbb{Z}/n\mathbb{Z}$ of integers modulo $n$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.unitSet`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#unit-set).

## Squares of units modulo n

For a natural number $n$, $U(n)^2$ is the set of elements of
$\mathbb{Z}/n\mathbb{Z}$ of the form $u^2$ with $u$ a unit of $\mathbb{Z}/n\mathbb{Z}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.unitSquareSet`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#unit-square-set).

## Nonzero squares modulo $n$

For a natural number $n$, $S(n)$ is the set of elements $x$
of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ with $x \neq 0$ and $x = y^2$ for some
$y \in \mathbb{Z}_n$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.squareSet`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#square-set).

## Weighted zero-sum sequences

Let $A \subseteq \mathbb{Z}/n\mathbb{Z}$ and let
$S = (x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}/n\mathbb{Z}$. Then $S$ is an $A$-weighted
zero-sum sequence if there are weights $a_1, \dots, a_k \in A$ with
$a_1 x_1 + a_2 x_2 + \dots + a_k x_k = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.HasWeightedZeroSum`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#has-weighted-zero-sum).

## Weighted zero-sum subsequences

Let $A \subseteq \mathbb{Z}/n\mathbb{Z}$ and let
$S = (x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}/n\mathbb{Z}$. Then $S$ has an $A$-weighted
zero-sum subsequence if there are a nonempty set $J \subseteq \{1, \dots, k\}$ of indices and
weights $a_i \in A$ for $i \in J$ with $\sum_{i \in J} a_i x_i = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.HasWeightedZeroSumSubseq`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#has-weighted-zero-sum-subseq).

## Consecutive weighted zero-sum subsequences

Let $A \subseteq \mathbb{Z}/n\mathbb{Z}$ and let
$S = (x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}/n\mathbb{Z}$. Then $S$ has an $A$-weighted
zero-sum consecutive subsequence if there are indices $1 \le l \le h \le k$ and weights
$a_l, \dots, a_h \in A$ with $\sum_{i=l}^{h} a_i x_i = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.HasConsecutiveWeightedZeroSumSubseq`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#has-consecutive-weighted-zero-sum-subseq).

## Representatives of a set of residues

Let $n$ be a natural number and $A$ a subset of
$\mathbb{Z}_n$. The representatives of $A$ form the finite set of natural numbers $a$ with
$0 \le a < n$ whose residue modulo $n$ lies in $A$.

A natural number $a$ acts on $\mathbb{Z}_n$ by $x \mapsto a x$. For $n \ge 1$ every residue has
exactly one representative below $n$, so the weighted Davenport constant of $\mathbb{Z}_n$ with
the representatives of $A$ as weights is the paper's $D_A$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.zmodWeightReps`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#zmod-weight-reps).

## Membership in the weight representatives

Let $A \subseteq \mathbb{Z}/n\mathbb{Z}$.
A natural number $a$ lies in the set of weight representatives of $A$ if and only if $a < n$ and
the residue of $a$ modulo $n$ lies in $A$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.mem_zmodWeightReps`, a theorem declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#mem-zmod-weight-reps).

## Lengths forcing a consecutive weighted zero sum

Let $n$ be a natural number and $A$ a
subset of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$. This is the set of positive integers $k$ such
that every sequence $(x_1, \dots, x_k)$ of elements of $\mathbb{Z}_n$ has a nonempty block of
consecutive terms $x_i, \dots, x_j$ with weights $a_i, \dots, a_j \in A$ such that
$a_i x_i + \dots + a_j x_j = 0$. Its least element, or $0$ when it is empty, is the $A$-weighted
consecutive constant $C_A$ of $\mathbb{Z}_n$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.weightedConsecutiveDefiningSet`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-consecutive-defining-set).

## Weighted consecutive zero-sum constant

Let $n$ be a natural number and $A$ a subset of
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$. The $A$-weighted consecutive constant $C_A$ of
$\mathbb{Z}_n$ is the least positive integer $k$ such that every sequence $(x_1, \dots, x_k)$ of
elements of $\mathbb{Z}_n$ has a nonempty block of consecutive terms $x_i, \dots, x_j$ with
weights $a_i, \dots, a_j \in A$ such that $a_i x_i + \dots + a_j x_j = 0$; it is $0$ when no
such $k$ exists.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.weightedConsecutiveConstant`, a definition declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#weighted-consecutive-constant).

## Weighted zero-sum subsequences are monotone in the weight set

Let
$A \subseteq B \subseteq \mathbb{Z}/n\mathbb{Z}$ and let $S$ be a finite sequence in
$\mathbb{Z}/n\mathbb{Z}$. If $S$ has an $A$-weighted zero-sum subsequence, then $S$ has a
$B$-weighted zero-sum subsequence.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.HasWeightedZeroSumSubseq.mono`, a theorem declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-01/index.html#mono).

## The one-term zero sequence has a square-weighted zero sum

Let $n \ge 2$ and let $S(n)$ be
the set of nonzero squares in $\mathbb{Z}_n$. The sequence over $\mathbb{Z}_n$ whose only term is
$0$ has an $S(n)$-weighted zero sum: there is a weight $a \in S(n)$ with $a \cdot 0 = 0$.

The weight $a = 1$ works; it lies in $S(n)$ because $1 \ne 0$ in $\mathbb{Z}_n$ when $n \ge 2$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Introduction.

Formalized by `MetaMathlibExt.zeroSingleton_hasWeightedZeroSum`, a theorem declared in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#zero-singleton-has-weighted-zero-sum).

## Decomposition of the nonzero squares modulo a prime power

Let $p$ be a prime, let
$r \ge 1$, and let $l = \lfloor (r - 1)/2 \rfloor$. Write $S(p^r)$ for the set of nonzero squares
in $\mathbb{Z}_{p^r}$, $U(p^r)^2$ for the set of squares of units in $\mathbb{Z}_{p^r}$, and
$p^{2k} U(p^r)^2 = \{p^{2k} x : x \in U(p^r)^2\}$. Then

$$S(p^r) = \bigcup_{k=0}^{l} p^{2k} U(p^r)^2,$$

and the sets $p^{2k} U(p^r)^2$ for $k = 0, \dots, l$ are pairwise disjoint.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 4.

Stated but not proved: `MetaMathlibExt.squareSet_primePower_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-set-prime-power-decomposition).

## Scaled unit squares modulo a prime power

Let $p$ be a prime and $r, k$ natural numbers
with $k = 0$ or $2k < r$, and write $U(m)^2$ for the set of squares of units of
$\mathbb{Z}/m\mathbb{Z}$. Then the set $p^{2k} U(p^r)^2 = \{p^{2k} x : x \in U(p^r)^2\}$ in
$\mathbb{Z}/p^r\mathbb{Z}$ has the same number of elements as $U(p^{r-2k})^2$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 5.

Stated but not proved: `MetaMathlibExt.ncard_scale_unitSquares_primePower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#ncard-scale-unit-squares-prime-power).

## Number of nonzero squares modulo a prime power

Let $p$ be a prime and $r \ge 1$, and write
$S(m)$ for the set of nonzero squares and $U(m)^2$ for the set of squares of units in
$\mathbb{Z}/m\mathbb{Z}$. If $r$ is even, then
$|S(p^r)| = \sum_{k=0}^{r/2-1} |U(p^{r-2k})^2|$, and if $r$ is odd, then
$|S(p^r)| = \sum_{k=0}^{(r-1)/2} |U(p^{r-2k})^2|$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 6.

Stated but not proved: `MetaMathlibExt.ncard_squareSet_primePower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#ncard-square-set-prime-power).

## Square-weighted zero sums lift from a prime-power component

Let $n \ge 2$, let $p$ be a
prime dividing $n$, and let $r$ be the exponent of $p$ in $n$. Write $S(m)$ for the set of
nonzero squares in $\mathbb{Z}_m$. Let $x_1, \dots, x_k$ be a sequence in $\mathbb{Z}_n$ whose
reduction $\bar x_1, \dots, \bar x_k$ modulo $p^r$ has an $S(p^r)$-weighted zero sum, that is,
there are $b_1, \dots, b_k \in S(p^r)$ with $\sum_i b_i \bar x_i = 0$. Then there are
$a_1, \dots, a_k \in S(n)$ with $\sum_i a_i x_i = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 7.

Stated but not proved: `MetaMathlibExt.squareWeightedZeroSum_of_primePower_reduction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-weighted-zero-sum-of-prime-power).

## Prime-power bound for the square-weighted consecutive constant

Let $n \ge 2$, let $p$ be a
prime dividing $n$ and let $r = v_p(n)$ be the exponent of $p$ in $n$. For a natural number $m$,
write $S(m)$ for the set of nonzero squares in $\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$ and
$C_{S(m)}$ for the $S(m)$-weighted consecutive constant of $\mathbb{Z}_m$. Then
$C_{S(n)} \le C_{S(p^r)}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 8.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_le_primePower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-consecutive-constant-square-set).

## Square-weighted zero sums lift from $p$ to odd powers $p^r$

Let $p \ge 2$ be a natural
number and $r$ an odd natural number. Write $S(m)$ for the set of nonzero squares in
$\mathbb{Z}_m$. Let $x_1, \dots, x_k$ be a sequence in $\mathbb{Z}_{p^r}$ whose reduction
$\bar x_1, \dots, \bar x_k$ modulo $p$ has an $S(p)$-weighted zero sum, that is, there are
$b_1, \dots, b_k \in S(p)$ with $\sum_i b_i \bar x_i = 0$. Then there are
$a_1, \dots, a_k \in S(p^r)$ with $\sum_i a_i x_i = 0$.

This is at least as strong as the reading with weights in $U(p)^2$, the squares of units of
$\mathbb{Z}_p$, because $U(p)^2 \subseteq S(p)$; the two agree for prime $p$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 9.

Stated but not proved: `MetaMathlibExt.squareWeightedZeroSum_of_reduction_oddPower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-weighted-zero-sum-of-reduction-od).

## Square-weighted zero-sum free unit triples modulo even powers of two

Let $r$ be a nonzero
even natural number, and let $x_1, x_2, x_3$ be units of $\mathbb{Z}_{2^r}$ that are each
congruent to $1$ modulo $4$. Write $S(2^r)$ for the set of nonzero squares in $\mathbb{Z}_{2^r}$.
Then $(x_1, x_2, x_3)$ has no $S(2^r)$-weighted zero-sum subsequence: there are no non-empty set
$J$ of indices and weights $a_j \in S(2^r)$ for $j \in J$ with $\sum_{j \in J} a_j x_j = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 10.

Stated but not proved: `MetaMathlibExt.no_squareWeightedSubseq_three_units_twoPower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#no-square-weighted-subseq-three-units-tw).

## Three-term sequences without square-weighted zero-sum subsequences

Let $p$ be a prime and
$r$ a nonzero even natural number, and write $S(m)$ for the set of nonzero squares in
$\mathbb{Z}/m\mathbb{Z}$. Let $z_1, z_2$ be units of $\mathbb{Z}/p^2\mathbb{Z}$ whose reduction
$(z_1 \bmod p, z_2 \bmod p)$ is not an $S(p)$-weighted zero-sum sequence. Let $T = (x_1, x_2, y_1)$
be a sequence in $\mathbb{Z}/p^r\mathbb{Z}$ whose reduction modulo $p^2$ is $(z_1, z_2, p)$. Then
$T$ has no $S(p^r)$-weighted zero-sum subsequence.

The paper states the lemma for sequences of units modulo $p^r$, which no $y_1$ reducing to the
nonunit $p$ can be; following the paper's proof and its application in Theorem 12, the sequence is
taken in $\mathbb{Z}/p^r\mathbb{Z}$. Then $x_1, x_2$ are automatically units, since $z_1, z_2$ are.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 11.

Stated but not proved: `MetaMathlibExt.no_squareWeightedSubseq_pair_and_prime_of_reduction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#no-square-weighted-subseq-pair-and-prime).

## Square-weighted Davenport constant of even squares is at least four

Let $n \ge 2$ be an
even perfect square. Write $S(n)$ for the set of nonzero squares in
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ and $D_{S(n)} \in \mathbb{N} \cup \{\infty\}$ for the
weighted Davenport constant of $\mathbb{Z}_n$ with weight set $S(n)$, a weight acting by
multiplication. Then $D_{S(n)} \ge 4$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 12.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_evenSquare_lowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-davenport-square-set-even-squar).

## Lifting weighted zero sums from p² to an even power of p

Let $p \ge 2$, $r \ne 0$
and $k$ be natural numbers with $r$ even, and let $t_1, \dots, t_k$ be elements of
$\mathbb{Z}/p^r\mathbb{Z}$, with reductions $\bar t_1, \dots, \bar t_k$ modulo $p^2$. Write
$U(p^2)^2$ for the set of squares of units of $\mathbb{Z}/p^2\mathbb{Z}$ and $S(p^r)$ for the
set of nonzero squares of $\mathbb{Z}/p^r\mathbb{Z}$. If there are
$a_1, \dots, a_k \in U(p^2)^2$ with $a_1 \bar t_1 + \dots + a_k \bar t_k = 0$ in
$\mathbb{Z}/p^2\mathbb{Z}$, then there are $b_1, \dots, b_k \in S(p^r)$ with
$b_1 t_1 + \dots + b_k t_k = 0$ in $\mathbb{Z}/p^r\mathbb{Z}$.

The paper states the lemma for $p > 0$; the stronger hypothesis $p \ge 2$ is deliberate.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 13.

Stated but not proved: `MetaMathlibExt.squareWeightedZeroSum_of_reduction_square` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-weighted-zero-sum-of-reduction-sq).

## Square-weighted constants modulo $p^r$, for $p \ge 2$ and nonzero even $r$, are at most unit-square constants modulo $p^2$

**Square-weighted constants modulo $p^r$, for $p \ge 2$ and nonzero even $r$, are at most
unit-square constants modulo $p^2$.** Let $p \ge 2$ be a natural number and let $r$ be a nonzero
even natural number. Write $S(p^r)$ for the set of nonzero squares in $\mathbb{Z}_{p^r}$ and
$U(p^2)^2$ for the set of squares of units in $\mathbb{Z}_{p^2}$. For a weight set
$A \subseteq \mathbb{Z}_m$, write $D_A(\mathbb{Z}_m)$ for the $A$-weighted Davenport constant of
$\mathbb{Z}_m$, where $A$ acts through its representatives in $\{0, \dots, m - 1\}$ and the value
lies in $\mathbb{N} \cup \{\infty\}$, and write $C_A$ for the least positive length $k$ such that
every sequence of length $k$ in $\mathbb{Z}_m$ has a non-empty consecutive $A$-weighted zero-sum
subsequence, or $0$ if there is no such length. Then
$D_{S(p^r)}(\mathbb{Z}_{p^r}) \le D_{U(p^2)^2}(\mathbb{Z}_{p^2})$ and
$C_{S(p^r)} \le C_{U(p^2)^2}$, the first constant in each inequality taken in $\mathbb{Z}_{p^r}$
and the second in $\mathbb{Z}_{p^2}$.

The paper says $p$ positive; $p = 1$ is excluded (the paper assumes throughout that the modulus is
at least $2$), since then $S(1)$ is empty, so $D_{S(1)}(\mathbb{Z}_1) = \infty$, while
$D_{U(1)^2}(\mathbb{Z}_1) = 1$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 14.

Stated but not proved: `MetaMathlibExt.squareSet_constants_le_unitSquares_modSquare` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-set-constants-le-unit-squares-mod).

## Consecutive square-weighted constant of an even power of two is at most four

For every
even natural number $r \ne 0$, the consecutive $S(2^r)$-weighted zero-sum constant satisfies
$C_{S(2^r)} \le 4$, where $S(2^r)$ is the set of nonzero squares of $\mathbb{Z}/2^r\mathbb{Z}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 15.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_twoPower_le_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-consecutive-constant-square-set-2).

## Square-weighted constants of even squares

Let $n \ge 2$ be an even perfect square and let
$S(n)$ be the set of nonzero squares in $\mathbb{Z}_n$. Then the $S(n)$-weighted Davenport
constant of $\mathbb{Z}_n$, with weights the representatives in $\{0, \dots, n - 1\}$ of the
elements of $S(n)$, equals $4$. Moreover, some positive length $k$ forces every sequence of
length $k$ in $\mathbb{Z}_n$ to have a non-empty consecutive $S(n)$-weighted zero-sum
subsequence, and the least such length, the consecutive constant $C_{S(n)}$, equals $4$.

Since the infimum of the empty set of natural numbers is $0$, the existence clause makes the
equality $C_{S(n)} = 4$ nonvacuous.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 16.

Stated but not proved: `MetaMathlibExt.squareSet_constants_evenSquare` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-set-constants-even-square).

## Two units without square-weighted zero sums modulo any prime divisor

Let $n \ge 2$ be
odd, and write $S(m)$ for the set of nonzero squares in $\mathbb{Z}/m\mathbb{Z}$. Then there are
units $u, v$ of $\mathbb{Z}/n\mathbb{Z}$ such that for every prime $p$ dividing $n$, the sequence
$(u \bmod p, v \bmod p)$ in $\mathbb{Z}/p\mathbb{Z}$ has no $S(p)$-weighted zero-sum subsequence.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Proposition 17.

Stated but not proved: `MetaMathlibExt.exists_pair_units_avoiding_prime_squareWeights` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#exists-pair-units-avoiding-prime-square).

## Square-weighted zero-sum free unit pairs lift to odd prime powers

Let $p$ be an odd
prime, let $r \ge 1$, and let $x_1, x_2$ be units of $\mathbb{Z}_{p^r}$. Write $S(m)$ for the set
of nonzero squares in $\mathbb{Z}_m$, and say that a sequence $(y_i)$ in $\mathbb{Z}_m$ has an
$A$-weighted zero-sum subsequence when there are a non-empty set $J$ of indices and weights
$a_j \in A$ for $j \in J$ with $\sum_{j \in J} a_j y_j = 0$. If the reduction
$(\bar x_1, \bar x_2)$ of $(x_1, x_2)$ modulo $p$ has no $S(p)$-weighted zero-sum subsequence,
then $(x_1, x_2)$ has no $S(p^r)$-weighted zero-sum subsequence.

The paper states the hypothesis with $Q_p$, the set of nonzero quadratic residues modulo $p$,
which equals $S(p)$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 18.

Stated but not proved: `MetaMathlibExt.no_squareWeightedSubseq_pair_of_reduction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#no-square-weighted-subseq-pair-of-reduct).

## The square-weighted Davenport constant of an odd modulus is at least three

Let $n \ge 2$
be odd, let $S(n)$ be the set of nonzero squares in $\mathbb{Z}_n$, and let $A$ be the set of
integers $a$ with $0 \le a < n$ whose residue modulo $n$ lies in $S(n)$. Then the $A$-weighted
Davenport constant $D_{S(n)}$ of $\mathbb{Z}_n$ is at least $3$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 19.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_odd_lowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-davenport-square-set-odd-lower).

## Square-weighted Davenport constant for an even 2-adic valuation of at least two

Let
$n \ge 2$ be a natural number whose exponent $v_2(n)$ of $2$ is even and at least $2$. Write
$S(n)$ for the set of nonzero squares in $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ and
$D_{S(n)} \in \mathbb{N} \cup \{\infty\}$ for the weighted Davenport constant of $\mathbb{Z}_n$
with weight set $S(n)$, a weight acting by multiplication. Then $D_{S(n)} \ge 3$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 20.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_even_twoValuation_lowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-davenport-square-set-even-two-v).

## Consecutive square-weighted constant of an odd prime to an odd power is at most three

For every odd prime $p$ and every odd natural number $r$, the consecutive $S(p^r)$-weighted
zero-sum constant satisfies $C_{S(p^r)} \le 3$, where $S(p^r)$ is the set of nonzero squares of
$\mathbb{Z}/p^r\mathbb{Z}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 21.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_oddPrimePower_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#weighted-consecutive-constant-square-set-3).

## Square-weighted constants of nonsquares with even $2$-adic valuation

Let $n \ge 2$ be a
natural number that is not a perfect square and whose $2$-adic valuation $v_2(n)$ is even
(possibly zero), and let $S(n)$ be the set of nonzero squares in $\mathbb{Z}_n$. Then the
$S(n)$-weighted Davenport constant of $\mathbb{Z}_n$, with weights the representatives in
$\{0, \dots, n - 1\}$ of the elements of $S(n)$, equals $3$. Moreover, some positive length $k$
forces every sequence of length $k$ in $\mathbb{Z}_n$ to have a non-empty consecutive
$S(n)$-weighted zero-sum subsequence, and the least such length, the consecutive constant
$C_{S(n)}$, equals $3$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 22.

Stated but not proved: `MetaMathlibExt.squareSet_constants_nonsquare_even_twoValuation` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-02/index.html#square-set-constants-nonsquare-even-two).

## Consecutive square-weighted constant of an odd power of two is at most two

For every
odd natural number $r$, the consecutive $S(2^r)$-weighted zero-sum constant satisfies
$C_{S(2^r)} \le 2$, where $S(2^r)$ is the set of nonzero squares of $\mathbb{Z}/2^r\mathbb{Z}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 23.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_odd_twoPower_le_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set).

## Square-weighted constants of numbers with odd $2$-adic valuation

Let $n$ be a positive
even natural number whose $2$-adic valuation $v_2(n)$ is odd, and let $S(n)$ be the set of
nonzero squares in $\mathbb{Z}_n$. Then the $S(n)$-weighted Davenport constant of
$\mathbb{Z}_n$, with weights the representatives in $\{0, \dots, n - 1\}$ of the elements of
$S(n)$, equals $2$. Moreover, some positive length $k$ forces every sequence of length $k$ in
$\mathbb{Z}_n$ to have a non-empty consecutive $S(n)$-weighted zero-sum subsequence, and the
least such length, the consecutive constant $C_{S(n)}$, equals $2$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 24.

Stated but not proved: `MetaMathlibExt.squareSet_constants_odd_twoValuation` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#square-set-constants-odd-two-valuation).

## Four-term sequences without square-weighted zero-sum subsequences

Let $p$ be a prime and
$r$ a nonzero even natural number, and write $S(m)$ for the set of nonzero squares in
$\mathbb{Z}/m\mathbb{Z}$. Let $w_1, w_2, u$ be units of $\mathbb{Z}/p^r\mathbb{Z}$ such that the
reduction $(w_1 \bmod p, w_2 \bmod p)$ has no $S(p)$-weighted zero-sum subsequence. Then the
sequence $(u w_1, u w_2, p w_1, p w_2)$ in $\mathbb{Z}/p^r\mathbb{Z}$ has no $S(p^r)$-weighted
zero-sum subsequence.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 25.

Stated but not proved: `MetaMathlibExt.no_squareWeightedSubseq_fourTerm_pattern` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#no-square-weighted-subseq-four-term-patt).

## The square-weighted Davenport constant of an odd square is at least five

Let $n \ge 2$
be an odd perfect square, let $S(n)$ be the set of nonzero squares in $\mathbb{Z}_n$, and let $A$
be the set of integers $a$ with $0 \le a < n$ whose residue modulo $n$ lies in $S(n)$. Then the
$A$-weighted Davenport constant $D_{S(n)}$ of $\mathbb{Z}_n$ is at least $5$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 26.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_oddSquare_lowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-square-set-odd-square).

## Three unit-square cosets sum to every residue modulo an odd prime power

Let $p$ be an
odd prime, let $r \ge 1$, and let $A = U(p^r)^2$ be the set of squares of units of
$\mathbb{Z}/p^r\mathbb{Z}$; for $y \in \mathbb{Z}/p^r\mathbb{Z}$ write $Ay = \{ay : a \in A\}$.
For all units $y_1, y_2, y_3$ of $\mathbb{Z}/p^r\mathbb{Z}$, every element of
$\mathbb{Z}/p^r\mathbb{Z}$ is a sum $x_1 + x_2 + x_3$ with $x_1 \in Ay_1$,
$x_2 \in Ay_2 \cup \{0\}$ and $x_3 \in Ay_3 \cup \{0\}$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 27.

Stated but not proved: `MetaMathlibExt.three_unitSquare_cosets_cover` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#three-unit-square-cosets-cover).

## The square-weighted Davenport constant of an even power of an odd prime is at most five

Let $p$ be an odd prime, let $r$ be a nonzero even natural number, let $S(p^r)$ be the set of
nonzero squares in $\mathbb{Z}_{p^r}$, and let $A$ be the set of integers $a$ with $0 \le a < p^r$
whose residue modulo $p^r$ lies in $S(p^r)$. Then the $A$-weighted Davenport constant
$D_{S(p^r)}$ of $\mathbb{Z}_{p^r}$ is at most $5$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 28.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_oddPrimePower_le_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-square-set-odd-prime).

## The square-weighted Davenport constant of an odd square is five

Let $n \ge 2$ be an odd
perfect square, let $S(n)$ be the set of nonzero squares in $\mathbb{Z}_n$, and let $A$ be the set
of integers $a$ with $0 \le a < n$ whose residue modulo $n$ lies in $S(n)$. Then the $A$-weighted
Davenport constant $D_{S(n)}$ of $\mathbb{Z}_n$ equals $5$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 29.

Stated but not proved: `MetaMathlibExt.weightedDavenport_squareSet_oddSquare` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-square-set-odd-square-2).

## Unit-square-weighted consecutive constant modulo 25 equals nine

Let $U(25)^2$ be the set
of squares of units of $\mathbb{Z}_{25} = \mathbb{Z}/25\mathbb{Z}$. Some positive length $k$ has the
property that every sequence of $k$ elements of $\mathbb{Z}_{25}$ has a nonempty block of
consecutive terms with a $U(25)^2$-weighted sum equal to zero, and the least such length, the
$U(25)^2$-weighted consecutive constant $C_{U(25)^2}$ of $\mathbb{Z}_{25}$, equals $9$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 30.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_unitSquares_twentyFive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-unit-squar).

## Consecutive square-weighted constant of an odd square is at most nine

For every odd
natural number $n \ge 2$ that is a perfect square, the consecutive $S(n)$-weighted zero-sum
constant satisfies $C_{S(n)} \le 9$, where $S(n)$ is the set of nonzero squares of
$\mathbb{Z}/n\mathbb{Z}$.

The hypothesis $n \ge 2$ is the paper's standing convention.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 31.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_oddSquare_le_nine` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-2).

## Square-weighted consecutive constant of $p^r$ for prime $p \ge 7$ and even $r \ge 4$ is at most five

**Square-weighted consecutive constant of $p^r$ for prime $p \ge 7$ and even $r \ge 4$ is at
most five.** Let $p \ge 7$ be a prime and $r \ge 4$ an even natural number. Write $S(p^r)$ for the
set of nonzero squares in $\mathbb{Z}_{p^r} = \mathbb{Z}/p^r\mathbb{Z}$ and $C_{S(p^r)}$ for the
$S(p^r)$-weighted consecutive constant of $\mathbb{Z}_{p^r}$. Then $C_{S(p^r)} \le 5$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 34.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_largePrimePower_le_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-3).

## Square-weighted consecutive constant five for odd squares with a large prime fourth power

Let $n \ge 2$ be an odd perfect square and let $p \ge 7$ be a prime with $p^4 \mid n$. Write $S(n)$
for the set of nonzero squares in $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$. Then some positive length
$k$ has the property that every sequence of $k$ elements of $\mathbb{Z}_n$ has a nonempty block of
consecutive terms with an $S(n)$-weighted sum equal to zero, and the least such length, the
$S(n)$-weighted consecutive constant $C_{S(n)}$ of $\mathbb{Z}_n$, equals $5$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 35.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_oddSquare_largePrime` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-4).

## Four unit terms force a unit-square-weighted zero sum modulo a power of 5

Let $r \ge 1$
and let $U(5^r)^2$ be the set of squares of units of $\mathbb{Z}/5^r\mathbb{Z}$. If a sequence
$s_1, \dots, s_k$ in $\mathbb{Z}/5^r\mathbb{Z}$ has at least four terms, at distinct positions,
that are units, then there are $a_1, \dots, a_k \in U(5^r)^2$ with
$a_1 s_1 + \dots + a_k s_k = 0$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Lemma 36.

Stated but not proved: `MetaMathlibExt.unitSquareWeightedZeroSum_modFivePower_of_four_units` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#unit-square-weighted-zero-sum-mod-five-p).

## Square-weighted consecutive constant of $5^r$ for even $r \ge 4$ is at most seven

Let
$r \ge 4$ be an even natural number. Write $S(5^r)$ for the set of nonzero squares in
$\mathbb{Z}_{5^r} = \mathbb{Z}/5^r\mathbb{Z}$ and $C_{S(5^r)}$ for the $S(5^r)$-weighted consecutive
constant of $\mathbb{Z}_{5^r}$. Then $C_{S(5^r)} \le 7$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 37.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_fivePower_le_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-5).

## Square-weighted consecutive constant of squares divisible by 625 is at most seven

Let
$n \ge 2$ be a perfect square with $5^4 \mid n$. Write $S(n)$ for the set of nonzero squares in
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ and $C_{S(n)}$ for the $S(n)$-weighted consecutive constant
of $\mathbb{Z}_n$. Then $C_{S(n)} \le 7$.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Corollary 38.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_square_divisible_fiveFourth` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-6).

## Consecutive square-weighted constant of the square of an odd squarefree number

Let $m$
be an odd squarefree natural number and let $n = m^2$ with $n \ge 2$. Write $S(n)$ for the set
of nonzero squares of $\mathbb{Z}/n\mathbb{Z}$. Then there is a positive length $k$ such that
every sequence $x_1, \dots, x_k$ in $\mathbb{Z}/n\mathbb{Z}$ has a nonempty block of
consecutive terms $x_i, \dots, x_j$ and weights $a_i, \dots, a_j \in S(n)$ with
$a_i x_i + \dots + a_j x_j = 0$, and the consecutive $S(n)$-weighted zero-sum constant
$C_{S(n)}$, the least such $k$, equals $9$.

The hypothesis $n \ge 2$ is the paper's standing convention.

## Sources

- Krishnendu Paul and Shameek Paul, *Square-Weighted Zero-Sum Constants*, Journal of Integer Sequences 27 (2024), Article 24.6.6, Theorem 39.

Stated but not proved: `MetaMathlibExt.weightedConsecutiveConstant_squareSet_square_oddSquarefree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SquareWeightedZeroSumWanted.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-consecutive-constant-square-set-7).

## Xia's theorem on arithmetic progressions of weights

Let $n \ge 2$ and $a$ be natural
numbers, and let $A = \{(a + i) \bmod n : 0 \le i < \lceil n/2 \rceil\}$ be the set of remainders
modulo $n$ of the $\lceil n/2 \rceil$ consecutive integers
$a, a + 1, \dots, a + \lceil n/2 \rceil - 1$. If $0 \notin A$, then the $A$-weighted Davenport
constant of $\mathbb{Z}/n\mathbb{Z}$ is $D_A(\mathbb{Z}/n\mathbb{Z}) = 2$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 1.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_arithmeticProgression` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-zmod-arithmetic-progr).

## Weighted Davenport constant of $\mathbb{Z}/n\mathbb{Z}$ for the weights prime to $p$

Let
$n$ be a positive integer, $p$ a prime dividing $n$ and $k = v_p(n)$ the exponent of $p$ in $n$.
For the weight set $A = \{a \in \{1, \dots, n - 1\} : p \nmid a\}$, the $A$-weighted Davenport
constant of $\mathbb{Z}/n\mathbb{Z}$ is $D_A(\mathbb{Z}/n\mathbb{Z}) = k + 1$.

This is Xia's theorem. Without the hypothesis $p \mid n$ the formula fails: for $n = 10$ and
$p = 3$ one has $v_3(10) = 0$ but $D_A(\mathbb{Z}/10\mathbb{Z}) = 2$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 2.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_not_dvd_prime` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-zmod-not-dvd-prime).

## Olson's theorem for groups of rank at most two

For positive integers $h$ and $k$ with
$h \mid k$, the Davenport constant $D(G) = D_{\{1\}}(G)$ of
$G = \mathbb{Z}/h\mathbb{Z} \oplus \mathbb{Z}/k\mathbb{Z}$ is $D(G) = h + k - 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 3.

Stated but not proved: `MetaMathlibExt.weightedDavenport_one_zmod_prod_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-one-zmod-prod-of-dvd).

## Olson's theorem for abelian $p$-groups

Let $p$ be a prime, $r \ge 0$ and let
$e_1, \dots, e_r \ge 1$ be natural numbers. The Davenport constant $D(G) = D_{\{1\}}(G)$ of
$G = \mathbb{Z}/p^{e_1}\mathbb{Z} \oplus \dots \oplus \mathbb{Z}/p^{e_r}\mathbb{Z}$ is
$D(G) = 1 + \sum_{i=1}^{r} (p^{e_i} - 1)$. For $r = 0$ the group $G$ is trivial and this reads
$D(G) = 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 4.

Stated but not proved: `MetaMathlibExt.weightedDavenport_one_pi_zmod_prime_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#weighted-davenport-one-pi-zmod-prime-pow).

## A nested ceiling identity for divisors

For all natural numbers $m, n \ge 2$ with
$m \mid n$, we have $\lceil n / (\lceil n/(m-1) \rceil - 1) \rceil = m$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Lemma 1.

Stated but not proved: `MetaMathlibExt.ceilDiv_ceilDiv_sub_one_sub_one_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-03/index.html#ceil-div-ceil-div-sub-one-sub-one-of-dvd).

## Weight sets with weighted Davenport constant $m$ on $\mathbb{Z}/n\mathbb{Z}$

Let
$n \ge 2$ be a natural number and $m \ge 2$ a divisor of $n$. Every finite set $A$ of natural
numbers with $n/m \in A \subseteq \{1, \dots, \lceil n/(m-1) \rceil - 1\}$ has $A$-weighted
Davenport constant $D_A(\mathbb{Z}/n\mathbb{Z}) = m$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 5.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-of-dvd).

## Weighted Davenport constant of $\mathbb{Z}/n\mathbb{Z}$ for the weights $\{1, \dots, r\}$

Let $n$ and $r$ be natural numbers with $1 < r < n$ and let $A = \{1, \dots, r\}$. Then the
$A$-weighted Davenport constant of $\mathbb{Z}/n\mathbb{Z}$ is
$D_A(\mathbb{Z}/n\mathbb{Z}) = \lceil n/r \rceil$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Corollary 1, first part.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_Icc` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-icc).

## Initial-interval weights with weighted Davenport constant $m$

Let $m, n \ge 2$ be
natural numbers with $m \mid n$ and put $r = \lceil n/(m-1) \rceil - 1$. Then the
$\{1, \dots, r\}$-weighted Davenport constant of $\mathbb{Z}/n\mathbb{Z}$ is
$D_{\{1, \dots, r\}}(\mathbb{Z}/n\mathbb{Z}) = m$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Corollary 1, second part.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_Icc_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-icc-of-dvd).

## Long weighted zero-sum free sequences in groups of rank two

Let $m, n \ge 2$ be natural
numbers with $m \mid n$, let $k \ge 1$ and put $\alpha = \lceil n/(m-1) \rceil - 1$. Then there is
a sequence $s$ over $\mathbb{Z}/n\mathbb{Z} \oplus \mathbb{Z}/kn\mathbb{Z}$ of length
$m + \lceil kn/\alpha \rceil - 2$ that is $\{1, \dots, \alpha\}$-weighted zero-sum free: for every
non-empty set $I$ of positions and all weights $a_i \in \{1, \dots, \alpha\}$, the weighted sum
$\sum_{i \in I} a_i s_i$ is non-zero.

In particular the $\{1, \dots, \alpha\}$-weighted Davenport constant of
$\mathbb{Z}/n\mathbb{Z} \oplus \mathbb{Z}/kn\mathbb{Z}$ is at least
$m + \lceil kn/\alpha \rceil - 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_weightedZeroSumFree_zmod_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#exists-weighted-zero-sum-free-zmod-prod).

## Weight sets with prescribed weighted Davenport constant on $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$, divisible case

**Weight sets with prescribed weighted Davenport constant on
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$, divisible case.** Let $n \ge 2$ and
$k \ge 1$ be natural numbers, let $m \ge 2$ be a divisor of $n$, let
$\alpha = \lceil n/(m-1) \rceil - 1$, and suppose that $\alpha$ divides $n$. Then for every finite
set $A$ of natural numbers with $n/m \in A \subseteq \{1, \dots, \alpha\}$, the $A$-weighted
Davenport constant of $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$ is
$D_A(\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}) = m + \lceil kn/\alpha \rceil - 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 6(i).

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_prod_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-prod-of-dvd).

## Weight sets with prescribed weighted Davenport constant on $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$, non-divisible case

**Weight sets with prescribed weighted Davenport constant on
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$, non-divisible case.** Let $n \ge 2$ and
$k \ge 1$ be natural numbers, let $m \ge 2$ be a divisor of $n$, let
$\alpha = \lceil n/(m-1) \rceil - 1$, and suppose that $\alpha$ does not divide $n$. Let $r$ be
the remainder of $n$ modulo $\alpha$, so that $1 \le r < \alpha$, and suppose that
$(k - 1)\alpha < kr$. Then for every finite set $A$ of natural numbers with
$n/m \in A \subseteq \{1, \dots, \alpha\}$, the $A$-weighted Davenport constant of
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}$ is
$D_A(\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/kn\mathbb{Z}) = m + \lceil kn/\alpha \rceil - 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 6(ii).

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_prod_of_not_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-prod-of-not-dvd).

## Weight sets with weighted Davenport constant $2m - 1$ on $\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$

**Weight sets with weighted Davenport constant $2m - 1$ on
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$.** Let $n \ge 2$ be a natural number and
$m \ge 2$ a divisor of $n$. Every finite set $A$ of natural numbers with
$n/m \in A \subseteq \{1, \dots, \lceil n/(m-1) \rceil - 1\}$ has $A$-weighted Davenport constant
$D_A(\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}) = 2m - 1$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Corollary 2.

Stated but not proved: `MetaMathlibExt.weightedDavenport_zmod_prod_self_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-zmod-prod-self-of-dvd).

## Long weighted zero-sum free sequences in abelian $p$-groups

Let $p$ be a prime, let
$r \ge 1$, let $e_1 \le e_2 \le \dots \le e_r$ be natural numbers and let
$G = \mathbb{Z}/p^{e_1}\mathbb{Z} \oplus \dots \oplus \mathbb{Z}/p^{e_r}\mathbb{Z}$. Let $c$ be a
natural number with $1 \le c \le e_1$ and put $\beta = \lceil p^{e_1}/(p^c - 1) \rceil - 1$. Then
there is a sequence $s$ over $G$ of length $\sum_{i=1}^{r} (\lceil p^{e_i}/\beta \rceil - 1)$ that
is $\{1, \dots, \beta\}$-weighted zero-sum free: for every non-empty set $I$ of positions and all
weights $a_i \in \{1, \dots, \beta\}$, the weighted sum $\sum_{i \in I} a_i s_i$ is non-zero.

In particular the $\{1, \dots, \beta\}$-weighted Davenport constant of $G$ is at least
$1 + \sum_{i=1}^{r} (\lceil p^{e_i}/\beta \rceil - 1)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Lemma 3.

Stated but not proved: `MetaMathlibExt.exists_weightedZeroSumFree_pi_zmod_prime_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#exists-weighted-zero-sum-free-pi-zmod-pr).

## Weighted Davenport constant of abelian $p$-groups, divisible case

Let $p$ be a prime,
let $r \ge 1$, let $e_1 \le e_2 \le \dots \le e_r$ be natural numbers and let
$G = \mathbb{Z}/p^{e_1}\mathbb{Z} \oplus \dots \oplus \mathbb{Z}/p^{e_r}\mathbb{Z}$. Let $c$ be a
natural number with $1 \le c \le e_1$, put $\beta = \lceil p^{e_1}/(p^c - 1) \rceil - 1$ and let
$A$ be a finite set of natural numbers with $p^{e_1 - c} \in A \subseteq \{1, \dots, \beta\}$. If
$\beta \mid p^{e_1}$, then the $A$-weighted Davenport constant of $G$ is
$D_A(G) = 1 + \sum_{i=1}^{r} (\lceil p^{e_i}/\beta \rceil - 1)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 7(i).

Stated but not proved: `MetaMathlibExt.weightedDavenport_pi_zmod_prime_pow_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-pi-zmod-prime-pow-of).

## Weighted Davenport constant of abelian $p$-groups, non-divisible case

Let $p$ be a
prime, let $r \ge 1$, let $e_1 \le e_2 \le \dots \le e_r$ be natural numbers and let
$G = \mathbb{Z}/p^{e_1}\mathbb{Z} \oplus \dots \oplus \mathbb{Z}/p^{e_r}\mathbb{Z}$. Let $c$ be a
natural number with $1 \le c \le e_1$, put $\beta = \lceil p^{e_1}/(p^c - 1) \rceil - 1$ and let
$A$ be a finite set of natural numbers with $p^{e_1 - c} \in A \subseteq \{1, \dots, \beta\}$.
Suppose that $\beta \nmid p^{e_1}$ and let $s$ be the remainder of $p^{e_1}$ modulo $\beta$, so
that $1 \le s < \beta$. If $(p^{e_j - e_1} - 1)\beta < s\,p^{e_j - e_1}$ for every
$j \in \{2, \dots, r\}$, then the $A$-weighted Davenport constant of $G$ is
$D_A(G) = 1 + \sum_{i=1}^{r} (\lceil p^{e_i}/\beta \rceil - 1)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Theorem 7(ii).

Stated but not proved: `MetaMathlibExt.weightedDavenport_pi_zmod_prime_pow_of_not_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-pi-zmod-prime-pow-of-2).

## Weighted Davenport constant of $(\mathbb{Z}/p^e\mathbb{Z})^r$

Let $p$ be a prime and let
$a, e, r$ be natural numbers with $1 \le a \le e$ and $r \ge 1$. Let $A$ be a finite set of
natural numbers with $p^{e-a} \in A \subseteq \{1, \dots, \lceil p^e/(p^a - 1) \rceil - 1\}$.
Then the $A$-weighted Davenport constant of $(\mathbb{Z}/p^e\mathbb{Z})^r$ is
$D_A((\mathbb{Z}/p^e\mathbb{Z})^r) = 1 + r(p^a - 1)$.

## Sources

- Md Ibrahim Molla, *New Families of Weight Sets Yielding Prescribed Weighted Zero-Sum Constants*, INTEGERS 26 (2026), Article A89, Corollary 3.

Stated but not proved: `MetaMathlibExt.weightedDavenport_pi_zmod_prime_pow_const` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/WeightedDavenportWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-davenport-pi-zmod-prime-pow-con).

## Unit-weighted zero-sum constants of $\mathbb{Z}_n$

Let $n$ be a positive integer, let
$U(n)$ be the set of units of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, and let $\Omega(n)$ be the
number of prime factors of $n$ counted with multiplicity. Then $D_{U(n)}(n) = \Omega(n) + 1$ and
$C_{U(n)}(n) = 2^{\Omega(n)}$. Here $D_{U(n)}(n)$ is the least positive integer $k$ such that
every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}_n$ has a nonempty set $I$ of indices and units
$a_i \in U(n)$ for $i \in I$ with $\sum_{i \in I} a_i x_i = 0$, and $C_{U(n)}(n)$ is defined in
the same way with $I$ restricted to a block $\{s, s+1, \dots, t\}$ of consecutive indices.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 4 (`jis-2024-24.1.7-thm-4`).

Stated but not proved: `MetaMathlibExt.unit_weighted_zero_sum_constants` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#unit-weighted-zero-sum-constants).

## Quadratic-residue-weighted zero-sum constants modulo a prime

Let $p$ be an odd prime and
let $Q_p$ be the set of squares of units of $\mathbb{Z}_p = \mathbb{Z}/p\mathbb{Z}$. Then
$C_{Q_p}(p) = D_{Q_p}(p) = 3$. Here $D_{Q_p}(p)$ is the least positive integer $k$ such that every
sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}_p$ has a nonempty set $I$ of indices and weights
$a_i \in Q_p$ for $i \in I$ with $\sum_{i \in I} a_i x_i = 0$, and $C_{Q_p}(p)$ is defined in the
same way with $I$ restricted to a block $\{s, s+1, \dots, t\}$ of consecutive indices.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 5 (`jis-2024-24.1.7-thm-5`).

Stated but not proved: `MetaMathlibExt.quadratic_residue_weighted_zero_sum_constants` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#quadratic-residue-weighted-zero-sum-cons).

## Product lower bound for the consecutive weighted zero-sum constant

For a natural number
$n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $C_A(n)$ denote the least positive integer $k$
such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a block of
consecutive terms $x_s, \dots, x_t$ with $s \le t$ and weights $a_s, \dots, a_t \in A$ such that
$a_s x_s + \dots + a_t x_t = 0$. Let $m$ and $q$ be natural numbers and let
$A \subseteq \mathbb{Z}/mq\mathbb{Z}$, $B \subseteq \mathbb{Z}/m\mathbb{Z}$ and
$C \subseteq \mathbb{Z}/q\mathbb{Z}$ be such that the reduction map
$\mathbb{Z}/mq\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$ sends $A$ into $B$ and the reduction map
$\mathbb{Z}/mq\mathbb{Z} \to \mathbb{Z}/q\mathbb{Z}$ sends $A$ into $C$. If $C_A(mq)$, $C_B(m)$
and $C_C(q)$ exist, then $C_A(mq) \ge C_B(m)\,C_C(q)$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 8 (`jis-2024-24.1.7-lem-8`).

Stated but not proved: `MetaMathlibExt.consecutive_constant_mul_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#consecutive-constant-mul-le).

## Lower bound for the weighted Davenport constant of a product modulus

For a natural
number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $D_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a
nonempty set $J$ of indices and weights $a_i \in A$ for $i \in J$ with
$\sum_{i \in J} a_i x_i = 0$. Let $m$ and $q$ be natural numbers and let
$A \subseteq \mathbb{Z}/mq\mathbb{Z}$, $B \subseteq \mathbb{Z}/m\mathbb{Z}$ and
$C \subseteq \mathbb{Z}/q\mathbb{Z}$ be such that the reduction map
$\mathbb{Z}/mq\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}$ sends $A$ into $B$ and the reduction map
$\mathbb{Z}/mq\mathbb{Z} \to \mathbb{Z}/q\mathbb{Z}$ sends $A$ into $C$. If $D_A(mq)$, $D_B(m)$
and $D_C(q)$ exist, then $D_A(mq) \ge D_B(m) + D_C(q) - 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 9 (`jis-2024-24.1.7-lem-9`).

Stated but not proved: `MetaMathlibExt.davenport_constant_add_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#davenport-constant-add-le).

## The index of the Jacobi symbol kernel

Let $n$ be an odd natural number, let $U(n)$
be the group of units of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, and let
$S(n) = \{u \in U(n) : (u/n) = 1\}$, where $(u/n)$ is the Jacobi symbol $(a/n)$ of the
representative $0 \le a < n$ of $u$. If $n$ is not a perfect square, then $S(n)$ is a subgroup of
$U(n)$ of index $2$. If $n$ is a perfect square, then $S(n) = U(n)$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Proposition 11 (`jis-2024-24.1.7-prop-11`).

Stated but not proved: `MetaMathlibExt.jacobi_kernel_index_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#jacobi-kernel-index-two).

## Units lift to the kernel of the Jacobi symbol across a non-square coprime factor

Let $d$
and $n'$ be coprime natural numbers such that $d n'$ is odd and $d$ is not a perfect square, and
put $n = d n'$. Then every unit $y$ of $\mathbb{Z}/n'\mathbb{Z}$ is the reduction modulo $n'$ of a
unit $x$ of $\mathbb{Z}/n\mathbb{Z}$ whose least nonnegative representative $v$ has Jacobi symbol
$\left(\frac{v}{n}\right) = 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 14 (`jis-2024-24.1.7-lem-14`).

Stated but not proved: `MetaMathlibExt.units_subset_image_jacobi_kernel` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#units-subset-image-jacobi-kernel).

## Lifting weighted zero sums along a coprime factor

Let $d$ and $n'$ be coprime natural
numbers, put $n = d n'$, and let $f : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n'\mathbb{Z}$ be
reduction modulo $n'$. Let $A \subseteq \mathbb{Z}/n\mathbb{Z}$ and
$A' \subseteq \mathbb{Z}/n'\mathbb{Z}$ with $A' \subseteq f(A)$, and let
$x_1, \dots, x_k \in \mathbb{Z}/n\mathbb{Z}$ each be divisible by $d$ in $\mathbb{Z}/n\mathbb{Z}$.
If there are $a'_1, \dots, a'_k \in A'$ with $a'_1 f(x_1) + \dots + a'_k f(x_k) = 0$, then there
are $a_1, \dots, a_k \in A$ with $a_1 x_1 + \dots + a_k x_k = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 15 (`jis-2024-24.1.7-lem-15`).

Stated but not proved: `MetaMathlibExt.weighted_zero_sum_of_image` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#weighted-zero-sum-of-image).

## Unit-weighted zero sums modulo an odd prime power

Let $p$ be an odd prime, let $r$ and
$k$ be natural numbers, and let $x_1, \dots, x_k \in \mathbb{Z}/p^r\mathbb{Z}$. Suppose that for
at least two indices $i$ the least nonnegative representative of $x_i$ is coprime to $p$. Then
there are units $a_1, \dots, a_k$ of $\mathbb{Z}/p^r\mathbb{Z}$ with
$a_1 x_1 + \dots + a_k x_k = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 16 (`jis-2024-24.1.7-lem-16`).

Stated but not proved: `MetaMathlibExt.unit_weighted_zero_sum_prime_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#unit-weighted-zero-sum-prime-power).

## Three-term sums of square-weighted units cover $\mathbb{Z}_{p^r}$

Let $p \ge 7$ be a
prime, $r$ a natural number and $n = p^r$; write $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ and
$A = U(n)^2$ for the set of squares of units of $\mathbb{Z}_n$. For all units $x_1, x_2, x_3$ of
$\mathbb{Z}_n$, $A x_1 + A x_2 + A x_3 = \mathbb{Z}_n$: every $z \in \mathbb{Z}_n$ equals
$a_1 x_1 + a_2 x_2 + a_3 x_3$ for some $a_1, a_2, a_3 \in A$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 17 (`jis-2024-24.1.7-lem-17`).

Stated but not proved: `MetaMathlibExt.unit_square_three_sumset_eq_univ` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-04/index.html#unit-square-three-sumset-eq-univ).

## Three-term sums with prescribed square classes cover $\mathbb{Z}_{p^r}$

Let $p \ge 7$ be
a prime, $r \ge 1$ and $n = p^r$; write $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, $U(n)$ for its
group of units, $A_1 = U(n)^2$ for the set of squares of units and $A_2 = U(n) \setminus U(n)^2$.
For all units $x_1, x_2, x_3$ of $\mathbb{Z}_n$ and every $f : \{1, 2, 3\} \to \{1, 2\}$,
$A_{f(1)} x_1 + A_{f(2)} x_2 + A_{f(3)} x_3 = \mathbb{Z}_n$: every $z \in \mathbb{Z}_n$ equals
$a_1 x_1 + a_2 x_2 + a_3 x_3$ for some $a_1 \in A_{f(1)}$, $a_2 \in A_{f(2)}$, $a_3 \in A_{f(3)}$.

The hypothesis $r \ge 1$ is needed: for $r = 0$, $\mathbb{Z}_1 = \{0\}$ has $0 = 0^2$ as its only
unit, so $A_2$ is empty.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 18 (`jis-2024-24.1.7-lem-18`).

Stated but not proved: `MetaMathlibExt.unit_square_class_three_sumset_eq_univ` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#unit-square-class-three-sumset-eq-univ).

## Three unit terms force a square-weighted zero sum modulo $p^r$

Let $p \ge 7$ be a prime,
$r$ a natural number and $n = p^r$, and let $U(n)^2$ be the set of squares of units of
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$. If a sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}_n$ has
at least three indices $i$ with $x_i$ a unit, then there are $a_1, \dots, a_k \in U(n)^2$ with
$a_1 x_1 + \dots + a_k x_k = 0$, that is, the sequence is a $U(n)^2$-weighted zero-sum sequence.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Corollary 19 (`jis-2024-24.1.7-cor-19`).

Stated but not proved: `MetaMathlibExt.unit_square_weighted_zero_sum_prime_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#unit-square-weighted-zero-sum-prime-powe).

## Few unit terms force a Jacobi-weighted zero sum

Let $n$ be an odd squarefree natural
number, $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, and $S(n)$ the set of units $u$ of $\mathbb{Z}_n$
whose Jacobi symbol $(a/n)$ is $1$, where $0 \le a < n$ is the representative of $u$. Let
$(x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}_n$, and call $x_i$ coprime to a prime $p$ when its
representative in $\{0, \dots, n-1\}$ is. Suppose that for every prime divisor $p$ of $n$ at least
two indices $i$ have $x_i$ coprime to $p$, and that at most one index $i$ has $x_i$ a unit. Then
there are $a_1, \dots, a_k \in S(n)$ with $a_1 x_1 + \dots + a_k x_k = 0$, that is, the sequence
is an $S(n)$-weighted zero-sum sequence.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 21 (`jis-2024-24.1.7-lem-21`).

Stated but not proved: `MetaMathlibExt.jacobi_weighted_zero_sum_of_few_units` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-weighted-zero-sum-of-few-units).

## Three terms coprime to one prime force a Jacobi-weighted zero sum

Let $n$ be a squarefree
natural number all of whose prime divisors are at least $7$, let
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, and let $S(n)$ be the set of units $u$ of $\mathbb{Z}_n$
whose Jacobi symbol $(a/n)$ is $1$, where $0 \le a < n$ is the representative of $u$. Let
$(x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}_n$, and call $x_i$ coprime to a prime $p$ when its
representative in $\{0, \dots, n-1\}$ is. Suppose that for every prime divisor $p$ of $n$ at least
two indices $i$ have $x_i$ coprime to $p$, and that for some prime divisor $p$ of $n$ at least
three indices $i$ have $x_i$ coprime to $p$. Then there are $a_1, \dots, a_k \in S(n)$ with
$a_1 x_1 + \dots + a_k x_k = 0$, that is, the sequence is an $S(n)$-weighted zero-sum sequence.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 22 (`jis-2024-24.1.7-lem-22`).

Stated but not proved: `MetaMathlibExt.jacobi_weighted_zero_sum_of_three_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-weighted-zero-sum-of-three-coprim).

## Davenport constant for the weights of Jacobi symbol one

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $D_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a
nonempty set $J$ of indices and weights $a_i \in A$ for $i \in J$ with
$\sum_{i \in J} a_i x_i = 0$. Let $n$ be an odd squarefree natural number and let
$S(n)$ be the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ with Jacobi symbol
$\left(\frac{x}{n}\right) = 1$. If $n$ is prime, then $D_{S(n)}(n) = 3$. If $n$ is not prime and
every prime divisor of $n$ is at least $7$, then $D_{S(n)}(n) = \Omega(n) + 1$, where $\Omega(n)$ is
the number of prime factors of $n$ counted with multiplicity.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 23 (`jis-2024-24.1.7-thm-23`).

Stated but not proved: `MetaMathlibExt.jacobi_davenport_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-davenport-constant).

## Consecutive constant for the weights of Jacobi symbol one

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $C_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a block of
consecutive terms $x_s, \dots, x_t$ with $s \le t$ and weights $a_s, \dots, a_t \in A$ such that
$a_s x_s + \dots + a_t x_t = 0$. Let $n$ be an odd squarefree natural number and let
$S(n)$ be the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ with Jacobi symbol
$\left(\frac{x}{n}\right) = 1$. If $n$ is prime, then $C_{S(n)}(n) = 3$. If $n$ is not prime and
every prime divisor of $n$ is at least $7$, then $C_{S(n)}(n) = 2^{\Omega(n)}$, where $\Omega(n)$ is
the number of prime factors of $n$ counted with multiplicity.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 24 (`jis-2024-24.1.7-thm-24`).

Stated but not proved: `MetaMathlibExt.jacobi_consecutive_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-consecutive-constant).

## Units with equal Jacobi and Legendre symbols form a subgroup of index two

Let $n$ be an
odd natural number and $p$ a prime divisor of $n$, and suppose that $p$ is not the unique prime
divisor of $n$ with odd exponent in $n$; that is, it is not the case that the exponent of $p$ in
$n$ is odd and every prime divisor of $n$ with odd exponent in $n$ equals $p$. Then the set of
units $u$ of $\mathbb{Z}/n\mathbb{Z}$ whose Jacobi symbol $\left(\frac{u}{n}\right)$ equals the
Legendre symbol $\left(\frac{u}{p}\right)$ is a subgroup of index two in the unit group of
$\mathbb{Z}/n\mathbb{Z}$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Proposition 26 (`jis-2024-24.1.7-prop-26`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_index_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-index-two).

## Lifting the Jacobi kernel into the Jacobi agreement set

Let $n$ be an odd natural number
and let $p$, $p'$ be prime divisors of $n$ with $p$ coprime to $n' = n/p$. For a residue $x$ modulo
$N$ and an odd $m$, write $(x/m)$ for the Jacobi symbol $(a/m)$ of the representative
$0 \le a < N$ of $x$. Let $U(m)$ be the group of units of $\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$,
let $S(n') = \{y \in U(n') : (y/n') = 1\}$ and $L(n;p') = \{x \in U(n) : (x/n) = (x/p')\}$, and
let $f_{n,n'} : \mathbb{Z}_n \to \mathbb{Z}_{n'}$ be reduction modulo $n'$. Then
$S(n') \subseteq f_{n,n'}(L(n;p'))$: every $y \in S(n')$ equals $f_{n,n'}(x)$ for some
$x \in L(n;p')$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 28 (`jis-2024-24.1.7-lem-28`).

Stated but not proved: `MetaMathlibExt.jacobi_kernel_subset_image_jacobi_eq_legendre` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-kernel-subset-image-jacobi-eq-leg).

## Units modulo a prime divisor lift to units where the Jacobi and Legendre symbols agree

Let $n$ be odd and let $p'$ be a prime dividing $n$ such that $p'$ is coprime to $n/p'$. Write
$L(n;p')$ for the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ whose least nonnegative
representative $v$ satisfies $\left(\frac{v}{n}\right) = \left(\frac{v}{p'}\right)$, where both
are Jacobi symbols. Then every unit $z$ of $\mathbb{Z}/p'\mathbb{Z}$ is the reduction modulo $p'$
of some element of $L(n;p')$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 29 (`jis-2024-24.1.7-lem-29`).

Stated but not proved: `MetaMathlibExt.units_prime_subset_image_jacobi_eq_legendre` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#units-prime-subset-image-jacobi-eq-legen).

## Chinese remainder lifts into the Jacobi agreement set

Let $n$ be an odd squarefree natural
number, $p'$ a prime divisor of $n$ and $n' = n/p'$. For a residue $x$ modulo $N$ and an odd $m$,
write $(x/m)$ for the Jacobi symbol $(a/m)$ of the representative $0 \le a < N$ of $x$. Let $U(m)$
be the group of units of $\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$, let
$S(n') = \{y \in U(n') : (y/n') = 1\}$ and $L(n;p') = \{x \in U(n) : (x/n) = (x/p')\}$, and for
$m \mid n$ let $f_{n,m} : \mathbb{Z}_n \to \mathbb{Z}_m$ be reduction modulo $m$. Then for every
$y \in S(n')$ and every $z \in U(p')$ there is $x \in L(n;p')$ with $f_{n,n'}(x) = y$ and
$f_{n,p'}(x) = z$. That is, the Chinese remainder isomorphism
$\psi = (f_{n,n'}, f_{n,p'}) : U(n) \to U(n') \times U(p')$ satisfies
$S(n') \times U(p') \subseteq \psi(L(n;p'))$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 31 (`jis-2024-24.1.7-lem-31`).

Stated but not proved: `MetaMathlibExt.jacobi_kernel_prod_units_subset_crt_image` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-kernel-prod-units-subset-crt-imag).

## Weighted zero-sum criterion for the Jacobi–Legendre weights

Let $n$ be a squarefree
natural number all of whose prime divisors are at least $7$, let $p'$ be a prime divisor of $n$,
let $n' = n/p'$, and let $L(n;p')$ be the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ whose Jacobi
symbol $\left(\frac{x}{n}\right)$ equals the Legendre symbol $\left(\frac{x}{p'}\right)$. Let
$(x_1, \dots, x_k)$ be a sequence in $\mathbb{Z}/n\mathbb{Z}$ such that for every prime divisor
$p$ of $n$ at least two terms $x_i$ are not divisible by $p$. Suppose that at most one term $x_i$
maps to a unit under the reduction map $\mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n'\mathbb{Z}$, or
that for some prime divisor $p$ of $n'$ at least three terms $x_i$ are not divisible by $p$. Then
there are weights $a_1, \dots, a_k \in L(n;p')$ with $a_1 x_1 + \dots + a_k x_k = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Lemma 32 (`jis-2024-24.1.7-lem-32`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_weighted_zero_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-weighted-zero-sum).

## Davenport constant of the Jacobi–Legendre weights

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $D_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a
nonempty set $J$ of indices and weights $a_i \in A$ for $i \in J$ with
$\sum_{i \in J} a_i x_i = 0$. Let $n$ be a squarefree natural number all of whose prime divisors are
at least $7$, with $\Omega(n) \ne 2$, where $\Omega(n)$ is the number of prime factors of $n$
counted with multiplicity. Let $p'$ be a prime divisor of $n$ and let $L(n;p')$ be the set of units
$x$ of $\mathbb{Z}/n\mathbb{Z}$ whose Jacobi symbol $\left(\frac{x}{n}\right)$ equals the Legendre
symbol $\left(\frac{x}{p'}\right)$. Then $D_{L(n;p')}(n) = \Omega(n) + 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 33 (`jis-2024-24.1.7-thm-33`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_davenport_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-davenport-constant).

## Davenport constant of the Jacobi–Legendre weights modulo a product of two primes

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $D_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a
nonempty set $J$ of indices and weights $a_i \in A$ for $i \in J$ with
$\sum_{i \in J} a_i x_i = 0$. Let $p'$ and $q$ be distinct primes with $p' \ge 7$ and $q \ge 7$, let
$n = p'q$, and let $L(n;p')$ be the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ whose Jacobi symbol
$\left(\frac{x}{n}\right)$ equals the Legendre symbol $\left(\frac{x}{p'}\right)$. Then
$D_{L(n;p')}(n) = 4$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 34 (`jis-2024-24.1.7-thm-34`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_davenport_constant_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-davenport-constant-tw).

## Consecutive constant of the Jacobi–Legendre weights

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $C_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a block of
consecutive terms $x_s, \dots, x_t$ with $s \le t$ and weights $a_s, \dots, a_t \in A$ such that
$a_s x_s + \dots + a_t x_t = 0$. Let $n$ be a squarefree natural number all of whose prime
divisors are at least $7$, with $\Omega(n) \ne 2$, where $\Omega(n)$ is the number of prime factors
of $n$ counted with multiplicity. Let $p'$ be a prime divisor of $n$ and let $L(n;p')$ be the
set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$ whose Jacobi symbol $\left(\frac{x}{n}\right)$ equals
the Legendre symbol $\left(\frac{x}{p'}\right)$. Then $C_{L(n;p')}(n) = 2^{\Omega(n)}$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 35 (`jis-2024-24.1.7-thm-35`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_consecutive_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-consecutive-constant).

## Consecutive constant of the Jacobi–Legendre weights modulo a product of two primes

For a
natural number $n$ and $A \subseteq \mathbb{Z}/n\mathbb{Z}$, let $C_A(n)$ denote the least positive
integer $k$ such that every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}/n\mathbb{Z}$ has a block of
consecutive terms $x_s, \dots, x_t$ with $s \le t$ and weights $a_s, \dots, a_t \in A$ such that
$a_s x_s + \dots + a_t x_t = 0$. Let $p'$ and $q$ be distinct primes with $p' \ge 7$ and
$q \ge 7$, let $n = p'q$, and let $L(n;p')$ be the set of units $x$ of $\mathbb{Z}/n\mathbb{Z}$
whose Jacobi symbol $\left(\frac{x}{n}\right)$ equals the Legendre symbol
$\left(\frac{x}{p'}\right)$. Then $C_{L(n;p')}(n) = 6$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *Zero-Sum Constants Related to the Jacobi Symbol*, Journal of Integer Sequences 27 (2024), Article 24.1.7, Theorem 36 (`jis-2024-24.1.7-thm-36`).

Stated but not proved: `MetaMathlibExt.jacobi_eq_legendre_consecutive_constant_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JacobiZeroSumConstantsWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#jacobi-eq-legendre-consecutive-constant-2).

## Weighted Davenport constant of a product with product weights

Let $R$ and $R'$ be rings,
$M$ an $R$-module, $N$ an $R'$-module, $A \subseteq R$ and $B \subseteq R'$. Let $D_A(M)$ be the
least positive integer $k$, if one exists, such that every sequence $x_1, \dots, x_k$ in $M$ has
a nonempty set of indices $I$ and weights $a_i \in A$ for $i \in I$ with
$\sum_{i \in I} a_i x_i = 0$, and define $D_B(N)$ in the same way. Let $D_{A \times B}(M \times N)$
be the least positive integer $k$, if one exists, such that every sequence
$(y_1, z_1), \dots, (y_k, z_k)$ in $M \times N$ has a nonempty set of indices $I$ and weights
$(a_i, b_i) \in A \times B$ for $i \in I$ with $\sum_{i \in I} (a_i y_i, b_i z_i) = 0$. If all
three constants exist, then $D_{A \times B}(M \times N) \ge D_A(M) + D_B(N) - 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.davenport_prod_ring_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#davenport-prod-ring-ge).

## Weighted Davenport constant of a product of modules

Let $R$ be a ring and
$A \subseteq R$. For an $R$-module $P$, let $D_A(P)$ be the least positive integer $k$, if one
exists, such that every sequence $x_1, \dots, x_k$ in $P$ has a nonempty set of indices $I$ and
weights $a_i \in A$ for $i \in I$ with $\sum_{i \in I} a_i x_i = 0$. If $M$ and $N$ are
$R$-modules for which $D_A(M)$, $D_A(N)$ and $D_A(M \times N)$ all exist, then
$D_A(M \times N) \ge D_A(M) + D_A(N) - 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.davenport_prod_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#davenport-prod-ge).

## Consecutive weighted zero-sum constant of a product with product weights

Let $R$ and
$R'$ be rings, $M$ an $R$-module, $N$ an $R'$-module, $A \subseteq R$ and $B \subseteq R'$. Let
$C_A(M)$ be the least positive integer $k$, if one exists, such that every sequence
$x_1, \dots, x_k$ in $M$ has indices $s \le t$ and weights $a_s, \dots, a_t \in A$ with
$a_s x_s + \dots + a_t x_t = 0$, and define $C_B(N)$ in the same way. Let
$C_{A \times B}(M \times N)$ be the least positive integer $k$, if one exists, such that every
sequence $(y_1, z_1), \dots, (y_k, z_k)$ in $M \times N$ has indices $s \le t$ and weights
$(a_i, b_i) \in A \times B$ for $s \le i \le t$ with $\sum_{i=s}^{t} (a_i y_i, b_i z_i) = 0$. If
all three constants exist, then $C_{A \times B}(M \times N) \ge C_A(M) \, C_B(N)$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 2.3.

Stated but not proved: `MetaMathlibExt.consecutive_prod_ring_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#consecutive-prod-ring-ge).

## Consecutive weighted zero-sum constant of a product of modules

Let $R$ be a ring and
$A \subseteq R$. For an $R$-module $P$, let $C_A(P)$ be the least positive integer $k$, if one
exists, such that every sequence $x_1, \dots, x_k$ in $P$ has indices $s \le t$ and weights
$a_s, \dots, a_t \in A$ with $a_s x_s + \dots + a_t x_t = 0$. If $M$ and $N$ are $R$-modules
for which $C_A(M)$, $C_A(N)$ and $C_A(M \times N)$ all exist, then
$C_A(M \times N) \ge C_A(M) \, C_A(N)$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 2.4.

Stated but not proved: `MetaMathlibExt.consecutive_prod_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#consecutive-prod-ge).

## Consecutive zero-sum constant of a finite abelian group

Let $G$ be a finite abelian
group and let $C(G)$ be the least positive integer $k$ such that every sequence
$x_1, \dots, x_k$ in $G$ has a block of consecutive terms $x_s, \dots, x_t$ with $s \le t$ and
$x_s + \dots + x_t = 0$. Then $C(G) = |G|$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.consecutive_constant_eq_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-05/index.html#consecutive-constant-eq-card).

## A block of consecutive coordinates orthogonal to $a$ vectors of $\mathbb{Z}_2^m$

Let
$\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$, let $2^a \le m$ and let
$v_1, \dots, v_a \in \mathbb{Z}_2^m$, with coordinates indexed by $\{0, \dots, m - 1\}$. Then there
are indices $s \le t$ in $\{0, \dots, m - 1\}$ such that $\sum_{j = s}^{t} (v_i)_j = 0$ in
$\mathbb{Z}_2$ for every $i$; that is, the nonzero vector whose ones occupy exactly the positions
$s, \dots, t$ is orthogonal to every $v_i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.exists_consecutive_orthogonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-consecutive-orthogonal).

## A block of consecutive integers meeting $a$ given sets evenly

Let $2^a \le m$ and let
$X_1, \dots, X_a$ be finite sets of natural numbers. Then there are integers $s, t$ with
$1 \le s \le t \le m$ such that $|\{s, s + 1, \dots, t\} \cap X_i|$ is even for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 3.3.

Stated but not proved: `MetaMathlibExt.exists_consecutive_even_inter` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-consecutive-even-inter).

## Griffiths' criterion for unit-weighted zero sums modulo a prime power

Let $p$ be a prime,
let $r$ and $k$ be natural numbers, put $n = p^r$, and let
$x_1, \dots, x_k \in \mathbb{Z}/n\mathbb{Z}$. Suppose that for each $i \in [1, r]$ the set
$X_i = \{j : x_j \not\equiv 0 \pmod{p^i}\}$ has an even number of elements. Then there are units
$a_1, \dots, a_k$ of $\mathbb{Z}/n\mathbb{Z}$ with $a_1 x_1 + \dots + a_k x_k = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 3.5.

Stated but not proved: `MetaMathlibExt.unitWeightedZeroSum_of_even_nonDivisible` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#unit-weighted-zero-sum-of-even-non-divis).

## Davenport constant of $\mathbb{Z}_2^a$

Let $\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$. For
every natural number $a$, the least positive integer $k$ such that every sequence of $k$ elements
of the group $\mathbb{Z}_2^a$ has a nonempty subsequence with sum zero is $a + 1$; that is, the
Davenport constant of $\mathbb{Z}_2^a$ is $a + 1$.

The paper states this for positive $a$; for $a = 0$ both sides equal $1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.davenport_zmod_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#davenport-zmod-two-pow).

## A nonzero vector of $\mathbb{Z}_2^m$ orthogonal to $a$ vectors when $a < m$

Let
$\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$, let $a + 1 \le m$ and let
$v_1, \dots, v_a \in \mathbb{Z}_2^m$. Then there is a nonzero $w \in \mathbb{Z}_2^m$ with
$w \cdot v_i = \sum_j w_j (v_i)_j = 0$ in $\mathbb{Z}_2$ for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 4.2.

Stated but not proved: `MetaMathlibExt.exists_ne_zero_orthogonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-ne-zero-orthogonal).

## A nonempty subset of $\{1, \dots, m\}$ meeting $a$ given sets evenly

Let $a + 1 \le m$
and let $X_1, \dots, X_a$ be finite sets of natural numbers. Then there is a nonempty set
$Y \subseteq \{1, \dots, m\}$ such that $|Y \cap X_i|$ is even for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 4.3.

Stated but not proved: `MetaMathlibExt.exists_nonempty_even_inter` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-nonempty-even-inter).

## Zero-sum subsequences of length $m$ in $\mathbb{Z}_2^a$

Let $a$ and $m$ be natural numbers
with $m$ even and $2^a \le m$, and write $\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$. Every sequence
$(x_1, \dots, x_{m+a})$ of length $m + a$ in $\mathbb{Z}_2^a$ has a zero-sum subsequence of length
$m$: there is a set $I$ of exactly $m$ indices with $\sum_{i \in I} x_i = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 5.2.

Stated but not proved: `MetaMathlibExt.exists_zeroSum_card_zmod_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-zero-sum-card-zmod-two-pow).

## A weight-$m$ vector orthogonal to given vectors of $\mathbb{Z}_2^{m+a}$

Let $a$ and $m$ be
natural numbers with $m$ even and $2^a \le m$, write $\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$, and
let $v_1, \dots, v_a$ be vectors in $\mathbb{Z}_2^{m+a}$. Then there is a vector
$w \in \mathbb{Z}_2^{m+a}$ with exactly $m$ coordinates equal to $1$ such that
$w \cdot v_i = \sum_j w_j (v_i)_j = 0$ for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 5.3.

Stated but not proved: `MetaMathlibExt.exists_weight_orthogonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-weight-orthogonal).

## An $m$-subset of $\{1, \dots, m + a\}$ meeting $a$ given sets evenly

Let $m$ be even with
$2^a \le m$, and let $X_1, \dots, X_a$ be finite sets of natural numbers. Then there is a set
$Y \subseteq \{1, \dots, m + a\}$ with $|Y| = m$ such that $|Y \cap X_i|$ is even for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 5.4.

Stated but not proved: `MetaMathlibExt.exists_card_even_inter` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-card-even-inter).

## Unit-weighted zero sums of even length in $\mathbb{Z}_n$

Let $n \ge 1$, let $\Omega(n)$ be
the number of prime factors of $n$ counted with multiplicity, and let $m$ be even with
$2^{\Omega(n)} \le m$. Then every sequence $x_1, \dots, x_{m + \Omega(n)}$ in
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$ has a unit-weighted zero-sum subsequence of length $m$:
there are a set $I \subseteq \{1, \dots, m + \Omega(n)\}$ with $|I| = m$ and units $a_i$ of
$\mathbb{Z}_n$ for $i \in I$ such that $\sum_{i \in I} a_i x_i = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 5.5.

Stated but not proved: `MetaMathlibExt.exists_unitWeightedZeroSum_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-unit-weighted-zero-sum-card).

## Every $m$-dimensional subspace of $\mathbb{Z}_2^{m+a}$ has a vector of weight $m$

Let
$\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$ and let $m$ be even with $2^a \le m$. Then every subspace
$W$ of $\mathbb{Z}_2^{m+a}$ of dimension $m$ contains a vector with exactly $m$ coordinates equal
to $1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Corollary 5.7.

Stated but not proved: `MetaMathlibExt.exists_weight_mem_subspace` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#exists-weight-mem-subspace).

## Largest subspaces of $\mathbb{Z}_2^{m+a}$ with no vector of weight $m$

Let $a$ and $m$ be
natural numbers with $m$ even and $2^a \le m$, and write $\mathbb{Z}_2 = \mathbb{Z}/2\mathbb{Z}$.
The largest dimension of a subspace of $\mathbb{Z}_2^{m+a}$ containing no vector with exactly $m$
coordinates equal to $1$ is $m - 1$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Corollary 5.9.

Stated but not proved: `MetaMathlibExt.max_finrank_avoiding_weight` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#max-finrank-avoiding-weight).

## Unit-weighted Erdős–Ginzburg–Ziv constant of $\mathbb{Z}_n$ for even $n$

Let $n$ be a
positive even integer, let $U(n)$ be the set of units of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$,
and let $\Omega(n)$ be the number of prime factors of $n$ counted with multiplicity. Then
$E_{U(n)}(n) = n + \Omega(n)$, where $E_{U(n)}(n)$ is the least positive integer $k$ such that
for every sequence $(x_1, \dots, x_k)$ in $\mathbb{Z}_n$ there are a set $I$ of exactly $n$
indices and units $a_i \in U(n)$ for $i \in I$ with $\sum_{i \in I} a_i x_i = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 6.3.

Stated but not proved: `MetaMathlibExt.gao_unit_constant_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#gao-unit-constant-of-even).

## Sequences equivalent to the extremal profile have no unit-weighted zero sum of length $2^r$

**Sequences equivalent to the extremal profile have no unit-weighted zero sum of length
$2^r$.** Let $r \ge 1$, $n = 2^r$ and $L = n + r - 1$, and let $U(n)$ be the unit group of
$\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$. Let $y_1, \dots, y_L \in \mathbb{Z}_n$ be a sequence in
which, for each $i \in \{0, \dots, r - 2\}$, exactly one term equals $2^i$, an odd number of
terms equal $2^{r-1}$, and every term is $0$ or $2^i$ for some $i < r$. Let
$x_1, \dots, x_L \in \mathbb{Z}_n$ be $U(n)$-equivalent to $y$: there are $c \in U(n)$,
$b_1, \dots, b_L \in U(n)$ and a permutation $\sigma$ of $\{1, \dots, L\}$ with
$c \, y_{\sigma(i)} = b_i x_i$ for all $i$. Then $x$ has no $U(n)$-weighted zero-sum subsequence
of length $n$: there is no set $I \subseteq \{1, \dots, L\}$ with $|I| = n$ together with
$a_i \in U(n)$ for $i \in I$ such that $\sum_{i \in I} a_i x_i = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 6.4.

Stated but not proved: `MetaMathlibExt.eExtremal_of_unitEquiv_profile` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#e-extremal-of-unit-equiv-profile).

## Structure of extremal sequences for unit-weighted zero sums of length $2^r$

Let $r \ge 1$,
let $n = 2^r$, let $U(n)$ be the set of units of $\mathbb{Z}_n = \mathbb{Z}/n\mathbb{Z}$, and let
$x = (x_1, \dots, x_{n+r-1})$ be a sequence in $\mathbb{Z}_n$ with no $U(n)$-weighted zero-sum
subsequence of length $n$: there is no set $I$ of exactly $n$ indices with units $a_i \in U(n)$
for $i \in I$ such that $\sum_{i \in I} a_i x_i = 0$. Then $x$ is $U(n)$-equivalent to a sequence
$(y_1, \dots, y_{n+r-1})$ in $\mathbb{Z}_n$ in which $2^i$ occurs exactly once for each
$i \in [0, r - 2]$, $2^{r-1}$ occurs an odd number of times and every other term is $0$: there
are a unit $c$, units $b_1, \dots, b_{n+r-1}$ and a permutation $\sigma$ of the indices with
$c \, y_{\sigma(i)} = b_i x_i$ for every $i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 6.6.

Stated but not proved: `MetaMathlibExt.unitEquiv_profile_of_eExtremal` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#unit-equiv-profile-of-e-extremal).

## Luca's lemma on unit-weighted zero sums modulo $2^r$

Let $r$ and $k$ be natural numbers
and let $x_1, \dots, x_k \in \mathbb{Z}/2^r\mathbb{Z}$. If the number of indices $j$ for which
$x_j$ is a unit is even and nonzero, then there are units $a_1, \dots, a_k$ of
$\mathbb{Z}/2^r\mathbb{Z}$ with $a_1 x_1 + \dots + a_k x_k = 0$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 6.5.

Stated but not proved: `MetaMathlibExt.unitWeightedZeroSum_of_even_units` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#unit-weighted-zero-sum-of-even-units).

## Unit-weighted zero sums of multiples of a prime

Let $p$ be a prime, let $n'$ and $k$ be
natural numbers, put $n = p n'$, and let $z_1, \dots, z_k \in \mathbb{Z}/n\mathbb{Z}$. Write
$\bar z_i$ for the reduction of $z_i$ modulo $n'$. If there are units $a_1, \dots, a_k$ of
$\mathbb{Z}/n'\mathbb{Z}$ with $\sum_i a_i \bar z_i = 0$, then there are units $b_1, \dots, b_k$
of $\mathbb{Z}/n\mathbb{Z}$ with $\sum_i b_i \, p z_i = 0$.

In the source the sequence $(p z_1, \dots, p z_k)$ determines the $z_i$ only modulo $n'$, so the
hypothesis does not depend on the choice of the $z_i$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 6.7.

Stated but not proved: `MetaMathlibExt.unitWeightedZeroSum_of_div_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#unit-weighted-zero-sum-of-div-prime).

## Halving consecutive unit-weighted zero-sum free sequences modulo a power of two

Let
$s \ge 0$, $n = 2^{s+1}$ and $n' = 2^s$. Say that a sequence $y_1, \dots, y_L$ in $\mathbb{Z}_m$ has
no consecutive unit-weighted zero-sum if there are no indices $1 \le i \le j \le L$ and units
$a_i, \dots, a_j$ of $\mathbb{Z}_m$ with $a_i y_i + \dots + a_j y_j = 0$. For a sequence
$x_1, \dots, x_{n-1}$ in $\mathbb{Z}_n$, let $r_l \in \{0, \dots, n - 1\}$ be the representative of
$x_l$ and let $\bar x_l \in \mathbb{Z}_{n'}$ be the residue of $\lfloor r_l / 2 \rfloor$. Then
$x_1, \dots, x_{n-1}$ has no consecutive unit-weighted zero-sum if and only if $r_l$ is even for
every $l \ne n'$, $r_{n'}$ is odd, and neither of the sequences $\bar x_1, \dots, \bar x_{n'-1}$
and $\bar x_{n'+1}, \dots, \bar x_{n-1}$ in $\mathbb{Z}_{n'}$ has a consecutive unit-weighted
zero-sum.

Write $U(n)$ for the unit group of $\mathbb{Z}_n$ and $C_{U(n)}(n)$ for the least positive $k$ such
that every sequence of length $k$ in $\mathbb{Z}_n$ has a consecutive unit-weighted zero-sum. Since
$C_{U(n)}(n) = n$, the sequences on the left are the $C$-extremal sequences for $U(n)$: those of
length $C_{U(n)}(n) - 1$ with no consecutive unit-weighted zero-sum.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 6.8.

Stated but not proved: `MetaMathlibExt.cExtremal_iff_halves` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#c-extremal-iff-halves).

## Consecutive weighted zero-sum constant for interval weights

Let $n \ge 2$ and
$1 \le r \le n - 1$, and let $A \subseteq \mathbb{Z}_n$ be the set of residues of
$1, 2, \dots, r$. Let $C_A(n)$ be the least positive integer $k$ such that every sequence
$x_1, \dots, x_k$ in $\mathbb{Z}_n$ has indices $s \le t$ and weights $a_s, \dots, a_t \in A$
with $a_s x_s + \dots + a_t x_t = 0$. Then $C_A(n) = \lceil n / r \rceil$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 7.1.

Stated but not proved: `MetaMathlibExt.consecutive_interval_weights` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#consecutive-interval-weights).

## Consecutive weighted zero-sum constant for odd weights

Let $n$ be a positive even
integer, let $2^r$ be the largest power of $2$ dividing $n$ and let $m = n / 2^r$. Let
$A \subseteq \mathbb{Z}_n$ contain the residue of $m$ and consist of odd elements (residues whose
representative in $\{0, \dots, n - 1\}$ is odd). Let $C_A(n)$ be the least positive integer $k$
such that every sequence $x_1, \dots, x_k$ in $\mathbb{Z}_n$ has indices $s \le t$ and weights
$a_s, \dots, a_t \in A$ with $a_s x_s + \dots + a_t x_t = 0$. Then $C_A(n) = 2^r$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 7.2.

Stated but not proved: `MetaMathlibExt.consecutive_odd_weights` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-06/index.html#consecutive-odd-weights).

## Davenport constant of $\mathbb{Z}_p$ with $k$-th power unit weights is at most $k$

Let
$k$ be an odd prime and $p$ a prime with $p \equiv 1 \pmod{k}$ and $p \not\equiv 1 \pmod{k^2}$.
Let $\mathbb{Z}_p = \mathbb{Z}/p\mathbb{Z}$ and let $U(p)^k$ be the set of $k$-th powers of units
of $\mathbb{Z}_p$. Then every sequence $x_1, \dots, x_k$ of $k$ elements of $\mathbb{Z}_p$ has a
$U(p)^k$-weighted zero-sum subsequence: there are a nonempty set $I \subseteq \{1, \dots, k\}$
and weights $a_i \in U(p)^k$ for $i \in I$ with $\sum_{i \in I} a_i x_i = 0$. In other words,
$D_{U(p)^k}(p) \le k$, where $D_A(p)$ is the least positive $\ell$ such that every sequence of
$\ell$ elements of $\mathbb{Z}_p$ has an $A$-weighted zero-sum subsequence.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Theorem 7.5.

Stated but not proved: `MetaMathlibExt.davenport_unit_pow_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-07/index.html#davenport-unit-pow-le).

## Weighted zero-sum free pairs in a field

Let $F$ be a field, let $A$ be a subgroup of the
multiplicative group $F^*$, and let $x, y \in F$ be nonzero. Then the sequence
$(x_1, x_2) = (x, y)$ has no $A$-weighted zero-sum subsequence, that is, there is no nonempty
set $I \subseteq \{1, 2\}$ with elements $a_i \in A$ for $i \in I$ such that
$\sum_{i \in I} a_i x_i = 0$, if and only if $x$ and $-y$ lie in different cosets of $A$ in $F^*$.

A zero term is by itself a zero-sum subsequence, so the cosets are taken for nonzero $x$ and $y$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Lemma 7.6.

Stated but not proved: `MetaMathlibExt.pair_no_weightedZeroSum_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-07/index.html#pair-no-weighted-zero-sum-iff).

## Weighted zero-sum free pairs for a proper subgroup of $F^\times$

Let $F$ be a field and
$A$ a proper subgroup of the multiplicative group $F^\times$. Then some sequence $x_1, x_2$ in
$F$ has no $A$-weighted zero-sum subsequence: there is no nonempty $I \subseteq \{1, 2\}$ with
weights $a_i \in A$ for $i \in I$ such that $\sum_{i \in I} a_i x_i = 0$.

Hence the weighted Davenport constant $D_A(F)$, the least positive $k$ such that every sequence
of length $k$ in $F$ has an $A$-weighted zero-sum subsequence, is at least $3$ when it exists.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Corollary 7.7.

Stated but not proved: `MetaMathlibExt.davenport_proper_subgroup_ge_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-07/index.html#davenport-proper-subgroup-ge-three).

## Weighted zero-sum free pairs for $k$-th power weights modulo a prime

Let $k \ge 2$, let
$p$ be a prime with $p \equiv 1 \pmod k$, and let $U(p)^k = \{u^k : u \in \mathbb{Z}_p^\times\}$.
Then some sequence $x_1, x_2$ in $\mathbb{Z}_p$ has no $U(p)^k$-weighted zero-sum subsequence:
there is no nonempty $I \subseteq \{1, 2\}$ with weights $a_i \in U(p)^k$ for $i \in I$ such that
$\sum_{i \in I} a_i x_i = 0$.

Hence the weighted Davenport constant $D_{U(p)^k}(p)$, the least positive $k'$ such that every
sequence of length $k'$ in $\mathbb{Z}_p$ has a $U(p)^k$-weighted zero-sum subsequence, is at
least $3$.

## Sources

- Santanu Mondal, Krishnendu Paul and Shameek Paul, *On Unit-Weighted Zero-Sum Constants of `ℤ_n`*, INTEGERS 24 (2024), Article A38, Corollary 7.8.

Stated but not proved: `MetaMathlibExt.davenport_unit_pow_ge_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitWeightedZeroSumConstantsWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/part-07/index.html#davenport-unit-pow-ge-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted Davenport constant](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/weighted-davenport-constant)
