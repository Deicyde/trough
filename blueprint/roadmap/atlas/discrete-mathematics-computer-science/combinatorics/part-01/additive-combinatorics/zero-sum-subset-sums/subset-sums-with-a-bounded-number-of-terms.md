---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedHFoldSumset, MetaMathlibExt.yangChenBound, MetaMathlibExt.yangChenBound_one_one_one_two, MetaMathlibExt.yangChenBound_one_one_two_two, MetaMathlibExt.generalizedHFoldSumset_zero_one_two, MetaMathlibExt.boundedSubsetSums, MetaMathlibExt.boundedSubsetSums_one_one_neg_one_one_two, MetaMathlibExt.repetitionSequence
statement: formalized
---

# Subset sums with a bounded number of terms

38 results, 15 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html).

## Generalized $h$-fold sumset

For elements $a_0, \dots, a_{k-1}$ of an additive commutative
monoid $G$ (not necessarily distinct), natural numbers $\bar r = (r_0, \dots, r_{k-1})$ and a
natural number $h$, the generalized $h$-fold sumset of $A = (a_0, \dots, a_{k-1})$ is the finite
set $h^{(\bar r)}A = \{\sum_j s_j a_j : s_j \in \mathbb{N}, s_j \le r_j, \sum_j s_j = h\}$, where
$s_j a_j$ is the sum of $s_j$ copies of $a_j$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1 (definition of `h^{(r̄)}A`).

Formalized by `MetaMathlibExt.generalizedHFoldSumset`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#generalized-hfold-sumset).

## The Yang–Chen bound

Let $k, h \in \mathbb{N}$ and $\bar r = (r_0, \dots, r_{k-1})$ with
all $r_j \in \mathbb{N}$; all sums below run over indices $j \in \{0, \dots, k-1\}$. Let $\mu$ be
the largest $m \in \{0, \dots, k\}$ with $\sum_{j < m} r_j \le h$, let $\eta$ be the integer such
that $\eta + 1$ is the least $m \in \{0, \dots, k\}$ with $\sum_{j \ge m} r_j \le h$ (so
$\eta = -1$ when $h \ge \sum_j r_j$), and set $\delta = h - \sum_{j < \mu} r_j$ and
$\theta = h - \sum_{j > \eta} r_j$. The Yang–Chen bound is the integer

$$L(\bar r, h) = \sum_{j > \eta} j r_j - \sum_{j < \mu} j r_j + \theta \eta - \delta \mu + 1.$$

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1.1 (definitions of `μ`, `η`, `δ`, `θ` and `L(r̄, h)`).

Formalized by `MetaMathlibExt.yangChenBound`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-bound).

## Yang–Chen bound at $(1, 1, 1)$ and $h = 2$

The Yang–Chen bound $L(\bar r, h)$ for
$\bar r = (1, 1, 1)$ and $h = 2$ equals $3$.

Here $\mu = 2$, $\eta = 0$ and $\delta = \theta = 0$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1.1 (definition of `L(r̄, h)`).

Formalized by `MetaMathlibExt.yangChenBound_one_one_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-bound-one-one-one-two).

## Yang–Chen bound at $(1, 1, 2)$ and $h = 2$

The Yang–Chen bound $L(\bar r, h)$ for
$\bar r = (1, 1, 2)$ and $h = 2$ equals $4$.

Here $\mu = 2$, $\eta = 1$ and $\delta = \theta = 0$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1.1 (definition of `L(r̄, h)`).

Formalized by `MetaMathlibExt.yangChenBound_one_one_two_two`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-bound-one-one-two-two).

## A generalized $2$-fold sumset of $\{0, 1, 2\}$

For $A = (0, 1, 2)$ in the integers and
$\bar r = (1, 1, 1)$, the generalized $2$-fold sumset $2^{(\bar r)}A$, the set of sums
$s_0 \cdot 0 + s_1 \cdot 1 + s_2 \cdot 2$ with $s_0, s_1, s_2 \in \{0, 1\}$ and
$s_0 + s_1 + s_2 = 2$, equals $\{1, 2, 3\}$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1 (definition of `h^{(r̄)}A`).

Formalized by `MetaMathlibExt.generalizedHFoldSumset_zero_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#generalized-hfold-sumset-zero-one-two).

## Subset sums with a bounded number of terms

For natural numbers $\alpha, \beta$ and a
finite subset $A$ of an additive commutative monoid $G$, the set $\Sigma^{\beta}_{\alpha}(A)$ is
the union of the restricted sumsets $m^{\wedge} A$ over $\alpha \le m \le |A| - \beta$, that is,
the set of sums $\sum_{b \in B} b$ over subsets $B \subseteq A$ with
$\alpha \le |B| \le |A| - \beta$. Here $|A| - \beta$ is read as $0$ when $\beta > |A|$.

The source assumes $\alpha + \beta \le |A|$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1 (definition of `Σ^β_α(A)`).

Formalized by `MetaMathlibExt.boundedSubsetSums`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums).

## Bounded subset sums of $\{-1, 1, 2\}$

The set $\Sigma^{1}_{1}(\{-1, 1, 2\})$ of sums of
subsets of the integer set $\{-1, 1, 2\}$ with at least $1$ and at most $2$ elements is
$\{-1, 0, 1, 2, 3\}$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 1 (definition of `Σ^β_α(A)`).

Formalized by `MetaMathlibExt.boundedSubsetSums_one_one_neg_one_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-one-one-neg-one-one).

## Sequence with prescribed multiplicities

Let $G$ be a type, $k \in \mathbb{N}$,
$A = (a_0, \dots, a_{k-1})$ a $k$-tuple of elements of $G$ and $\bar t = (t_0, \dots, t_{k-1})$ a
$k$-tuple of natural numbers. The sequence $(A, \bar t)$ is the finite multiset of elements of $G$
obtained by taking $t_i$ copies of $a_i$ for each $i < k$; an element $x \in G$ thus occurs
$\sum_{i : a_i = x} t_i$ times.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 4 (notation `(A, t̄)` for a finite sequence).

Formalized by `MetaMathlibExt.repetitionSequence`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#repetition-sequence).

## Length of a sequence with repetitions

Let $G$ be a set, $a_0, \dots, a_{k-1} \in G$ (not
necessarily distinct), $t_0, \dots, t_{k-1}$ natural numbers, $A = (a_0, \dots, a_{k-1})$ and
$\bar t = (t_0, \dots, t_{k-1})$. The multiset $(A, \bar t)$, made of $t_i$ copies of $a_i$ for
each $i$, has $t_0 + \dots + t_{k-1}$ elements counted with multiplicity.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 4 (notation `(A, t̄)` for a finite sequence).

Formalized by `MetaMathlibExt.card_repetitionSequence`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-repetition-sequence).

## Subsequence sums with a bounded number of terms

For natural numbers $\alpha, \beta$ and a
finite sequence $\mathcal{A}$ (a multiset) in an additive commutative monoid $G$,
$\Sigma^\beta_\alpha(\mathcal{A})$ is the finite set of the sums $\sigma(\mathcal{B})$ of the
terms of the subsequences $\mathcal{B}$ of $\mathcal{A}$ (sub-multisets) with
$\alpha \le |\mathcal{B}|$ and $|\mathcal{B}| + \beta \le |\mathcal{A}|$, that is, with at least
$\alpha$ and at most $|\mathcal{A}| - \beta$ terms; it is empty when $\beta > |\mathcal{A}|$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 4 (definition of `Σ^β_α(𝒜)`).

Formalized by `MetaMathlibExt.boundedSubsequenceSums`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums).

## An example of bounded subsequence sums

For the sequence of integers
$\mathcal{A} = (-2, 7, 7)$, in which $-2$ occurs once and $7$ twice,
$\Sigma^1_1(\mathcal{A}) = \{-2, 5, 7, 14\}$: the sums of the subsequences with at least one and
at most two terms are $-2$, $7$, $-2 + 7 = 5$ and $7 + 7 = 14$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Section 4 (definition of `Σ^β_α(𝒜)`).

Formalized by `MetaMathlibExt.boundedSubsequenceSums_one_one_example`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-one-one-example).

## Mixed-sign subset-sum bound

For natural numbers $n$, $p$, $\alpha$, $\beta$ (the numbers
of negative and positive elements of a set $A$, and the bounds on subset sizes), let
$\kappa = n + p - \beta$, computed in the integers, $T(x) = x(x+1)/2$ and
$S = T(p) + T(n) + 1$. The integer $L_{n,p}(\alpha, \beta)$, written $L(\alpha, \beta, A)$ in
the source, is $S - T(\beta - n) - T(\beta - p)$ if $1 \le \alpha < \kappa < n \le p$;
$S - T(\beta - n)$ if $1 \le \alpha < n \le \kappa < p$ or $1 \le \alpha = n < \kappa \le p$;
$S$ if $1 \le \alpha < n \le p \le \kappa$, or $1 \le \alpha = n < p < \kappa$, or
$1 \le \alpha = n = p < \kappa$; $S - T(\beta - n) - T(\alpha - n)$ if
$1 \le n < \alpha < \kappa \le p$; $S - T(\alpha - n)$ if $1 \le n < \alpha < p < \kappa$ or
$1 \le n < \alpha = p < \kappa$; $S - T(\alpha - n) - T(\alpha - p)$ if
$1 \le n \le p < \alpha < \kappa$; and $0$ otherwise.

These six cases are mutually exclusive, and when $1 \le n \le p$, $1 \le \alpha$ and
$\alpha + \beta + 1 \le n + p$ exactly one of them applies.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 7 (definition of `L(α, β, A)`).

Formalized by `MetaMathlibExt.mixedSignSubsetSumBound`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#mixed-sign-subset-sum-bound).

## A value of the mixed-sign subset-sum bound

For $n = 1$, $p = 2$ and $\alpha = \beta = 1$,
the mixed-sign subset-sum bound is $L_{1,2}(1, 1) = 5$; this value comes from its second case.

It is attained by $A = \{-1, 1, 2\}$: the sums of subsets of $A$ with one or two elements form
$\{-1, 0, 1, 2, 3\}$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 7 (definition of `L(α, β, A)`).

Formalized by `MetaMathlibExt.mixedSignSubsetSumBound_one_two_one_one`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#mixed-sign-subset-sum-bound-one-two-one).

## Mixed-sign subset-sum bound with zero

For natural numbers $n$, $p$, $\alpha$, $\beta$
(the numbers of negative and positive elements of a set $A$ that also contains $0$, and the
bounds on subset sizes), let $\kappa = n + p + 1 - \beta$, computed in the integers,
$T(x) = x(x+1)/2$, $T_0(x) = x(x-1)/2$ and $S = T(p) + T(n) + 1$. The integer
$L^0_{n,p}(\alpha, \beta)$, written $L_0(\alpha, \beta, A)$ in the source, is
$S - T_0(\beta - n) - T_0(\beta - p)$ if $1 \le \alpha < \kappa < n \le p$;
$S - T_0(\beta - n)$ if $1 \le \alpha < n \le \kappa < p$ or $1 \le \alpha = n < \kappa \le p$;
$S$ if $1 \le \alpha < n \le p \le \kappa$, or $1 \le \alpha = n < p < \kappa$, or
$1 \le \alpha = n = p < \kappa$; $S - T_0(\beta - n) - T_0(\alpha - n)$ if
$1 \le n < \alpha < \kappa \le p$; $S - T_0(\alpha - n)$ if $1 \le n < \alpha < p < \kappa$ or
$1 \le n < \alpha = p < \kappa$; $S - T_0(\alpha - n) - T_0(\alpha - p)$ if
$1 \le n \le p < \alpha < \kappa$; and $0$ otherwise.

These six cases are mutually exclusive, and when $1 \le n \le p$, $1 \le \alpha$ and
$\alpha + \beta + 1 \le n + p + 1$ exactly one of them applies.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 8 (definition of `L₀(α, β, A)`).

Formalized by `MetaMathlibExt.mixedSignZeroSubsetSumBound`, a definition declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#mixed-sign-zero-subset-sum-bound).

## A value of the mixed-sign subset-sum bound with zero

For $n = p = 1$ and
$\alpha = \beta = 1$, the mixed-sign subset-sum bound with zero is $L^0_{1,1}(1, 1) = 3$; this
value comes from its third case.

It is attained by $A = \{-1, 0, 1\}$: the sums of subsets of $A$ with one or two elements form
$\{-1, 0, 1\}$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 8 (definition of `L₀(α, β, A)`).

Formalized by `MetaMathlibExt.mixedSignZeroSubsetSumBound_one_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#mixed-sign-zero-subset-sum-bound-one-one).

## Yang–Chen lower bound for generalized $h$-fold sumsets

Let $k, h \in \mathbb{N}$ and let
$\bar r = (r_0, \dots, r_{k-1})$ be positive integers with $2 \le h \le r_0 + \dots + r_{k-1}$, and
let $L(\bar r, h)$ be the Yang–Chen bound. For all integers $a_0 < a_1 < \dots < a_{k-1}$, the
generalized $h$-fold sumset $h^{(\bar r)}A$ of $A = (a_0, \dots, a_{k-1})$ has at least
$L(\bar r, h)$ elements; and there exist integers $a_0 < a_1 < \dots < a_{k-1}$ for which
$h^{(\bar r)}A$ has exactly $L(\bar r, h)$ elements.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 2 (Yang and Chen).

Stated but not proved: `MetaMathlibExt.yangChen_card_generalizedHFoldSumset_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-card-generalized-hfold-sumset).

## Yang–Chen inverse theorem for at least five terms

Let $k \ge 5$ and $h \ge 2$ be integers,
let $\bar r = (r_0, \dots, r_{k-1})$ be positive integers with $h \le r_0 + \dots + r_{k-1} - 2$,
and let $L(\bar r, h)$ be the Yang–Chen bound. For all integers $a_0 < a_1 < \dots < a_{k-1}$,
with $A = \{a_0, \dots, a_{k-1}\}$, the generalized $h$-fold sumset $h^{(\bar r)}A$ has exactly
$L(\bar r, h)$ elements if and only if $A$ is an arithmetic progression of length $k$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 3 (Yang and Chen).

Stated but not proved: `MetaMathlibExt.yangChen_card_generalizedHFoldSumset_eq_iff_isAP` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-card-generalized-hfold-sumset-2).

## Yang–Chen inverse theorem for three terms

Let $a_0 < a_1 < a_2$ be integers,
$A = \{a_0, a_1, a_2\}$, $\bar r = (r_0, r_1, r_2)$ positive integers and $h \ge 2$ an integer
with $h \le r_0 + r_1 + r_2 - 2$, and let $L(\bar r, h)$ be the Yang–Chen bound. If $r_1 = 1$,
then the generalized $h$-fold sumset $h^{(\bar r)}A$ has exactly $L(\bar r, h)$ elements. If
$r_1 \ge 2$, then $h^{(\bar r)}A$ has exactly $L(\bar r, h)$ elements if and only if $A$ is an
arithmetic progression of length $3$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 4 (Yang and Chen).

Stated but not proved: `MetaMathlibExt.yangChen_card_generalizedHFoldSumset_eq_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-card-generalized-hfold-sumset-3).

## Yang–Chen inverse theorem for four terms

Let $a_0 < a_1 < a_2 < a_3$ be integers,
$A = \{a_0, a_1, a_2, a_3\}$, $\bar r = (r_0, r_1, r_2, r_3)$ positive integers and $h \ge 2$ an
integer with $h \le r_0 + r_1 + r_2 + r_3 - 2$, and let $L(\bar r, h)$ be the Yang–Chen bound.
If $r_1 = r_2 = 1$, then the generalized $h$-fold sumset $h^{(\bar r)}A$ has exactly
$L(\bar r, h)$ elements if and only if $a_1 - a_0 = a_3 - a_2$. If $r_1 \ge 2$ or $r_2 \ge 2$,
then $h^{(\bar r)}A$ has exactly $L(\bar r, h)$ elements if and only if $A$ is an arithmetic
progression of length $4$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 5 (Yang and Chen).

Stated but not proved: `MetaMathlibExt.yangChen_card_generalizedHFoldSumset_eq_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#yang-chen-card-generalized-hfold-sumset-4).

## Bounded subset sums as a generalized h-fold sumset when zero is not in the set

Let $G$
be an abelian group and let $A = \{a_1, \dots, a_k\}$ be a set of $k$ distinct nonzero elements
of $G$. If $\alpha, \beta$ are natural numbers with $\alpha + \beta \le k - 1$, then
$\Sigma^\beta_\alpha(A)$, the set of sums of subsets $B \subseteq A$ with
$\alpha \le |B| \le k - \beta$, equals the generalized $(k - \beta)$-fold sumset
$(k - \beta)^{(\bar r)} A_0$ of $A_0 = (a_0, a_1, \dots, a_k)$, where $a_0 = 0$, with
$\bar r = (k - \alpha - \beta, 1, \dots, 1)$, that is, the set of sums $\sum_{j=0}^{k} s_j a_j$
with $0 \le s_j \le r_j$ for all $j$ and $\sum_j s_j = k - \beta$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Lemma 1.

Stated but not proved: `MetaMathlibExt.boundedSubsetSums_eq_generalizedHFoldSumset_of_zero_not_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-eq-generalized-hfold).

## Bounded subset sums as a generalized h-fold sumset when zero is in the set

Let $G$ be an
abelian group, let $m$ be a natural number, let $a_1, \dots, a_m$ be distinct nonzero elements
of $G$, put $a_0 = 0$ and $k = m + 1$, and let $A = \{a_0, a_1, \dots, a_m\}$, a set of $k$
elements. If $\alpha, \beta$ are natural numbers with $\alpha \ge 1$, $\beta \le k - 1$ and
$\alpha + \beta \le k$, then $\Sigma^\beta_\alpha(A)$, the set of sums of subsets $B \subseteq A$
with $\alpha \le |B| \le k - \beta$, equals the generalized $(k - \beta)$-fold sumset
$(k - \beta)^{(\bar r)} A$ of $A$ listed as $(a_0, a_1, \dots, a_m)$, with
$\bar r = (k - \alpha - \beta + 1, 1, \dots, 1)$, that is, the set of sums
$\sum_{j=0}^{m} s_j a_j$ with $0 \le s_j \le r_j$ for all $j$ and $\sum_j s_j = k - \beta$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Lemma 2.

Stated but not proved: `MetaMathlibExt.boundedSubsetSums_eq_generalizedHFoldSumset_of_zero_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-eq-generalized-hfold-2).

## Reordering invariance of the generalized $h$-fold sumset

Let $G$ be an additive
commutative monoid, $a_0, \dots, a_{k-1} \in G$, $r_0, \dots, r_{k-1}$ and $h$ natural numbers,
and write $h^{(\bar r)}A = \{\sum_j s_j a_j : 0 \le s_j \le r_j, \sum_j s_j = h\}$ for the
generalized $h$-fold sumset of $A = (a_0, \dots, a_{k-1})$ with $\bar r = (r_0, \dots, r_{k-1})$.
For every permutation $\pi$ of $\{0, \dots, k-1\}$, the generalized $h$-fold sumset of
$(a_{\pi(0)}, \dots, a_{\pi(k-1)})$ with $(r_{\pi(0)}, \dots, r_{\pi(k-1)})$ equals
$h^{(\bar r)}A$.

The paper assumes $h \ge 2$, all $r_j$ positive and the $a_j$ distinct; none of this is assumed
here.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Lemma 3.

Stated but not proved: `MetaMathlibExt.generalizedHFoldSumset_comp_perm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#generalized-hfold-sumset-comp-perm).

## Bounded subsequence sums as a generalized h-fold sumset when zero is not a term

Let $G$
be an abelian group and let $a_1, \dots, a_k$ be distinct nonzero elements of $G$. Let
$t_1, \dots, t_k$ be positive integers, let $\mathcal{A}$ be the sequence in which each $a_i$
occurs $t_i$ times, and let $h = t_1 + \dots + t_k$ be its length. If $\alpha, \beta$ are natural
numbers with $\alpha \ge 1$ and $\alpha + \beta \le h - 1$, then $\Sigma^\beta_\alpha(\mathcal{A})$,
the set of sums of subsequences of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$
terms, equals the generalized $(h - \beta)$-fold sumset $(h - \beta)^{(\bar r)} A_0$ of
$A_0 = (a_0, a_1, \dots, a_k)$, where $a_0 = 0$, with
$\bar r = (h - \alpha - \beta, t_1, \dots, t_k)$, that is, the set of sums
$\sum_{j=0}^{k} s_j a_j$ with $0 \le s_j \le r_j$ for all $j$ and $\sum_j s_j = h - \beta$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Lemma 4.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_eq_generalizedHFoldSumset_of_zero_not_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-eq-generalized).

## Bounded subsequence sums as a generalized h-fold sumset when zero is a term

Let $G$ be
an abelian group, let $m$ be a natural number, let $a_1, \dots, a_m$ be distinct nonzero elements
of $G$, and put $a_0 = 0$. Let $t_0, \dots, t_m$ be positive integers, let $\mathcal{A}$ be the
sequence in which each $a_i$ occurs $t_i$ times, and let $h = t_0 + \dots + t_m$ be its length.
If $\alpha, \beta$ are natural numbers with $\alpha \ge 1$, $\beta \le h - 1$ and
$\alpha + \beta \le h$, then $\Sigma^\beta_\alpha(\mathcal{A})$, the set of sums of subsequences
of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$ terms, equals the generalized
$(h - \beta)$-fold sumset $(h - \beta)^{(\bar r)} A$ of $A = (a_0, a_1, \dots, a_m)$ with
$\bar r = (h - \alpha - \beta + t_0, t_1, \dots, t_m)$, that is, the set of sums
$\sum_{j=0}^{m} s_j a_j$ with $0 \le s_j \le r_j$ for all $j$ and $\sum_j s_j = h - \beta$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Lemma 5.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_eq_generalizedHFoldSumset_of_zero_mem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-eq-generalized-2).

## Sharp lower bounds for bounded subset sums of nonnegative sets

Let $k$, $\alpha$, $\beta$
be natural numbers with $k \ge 2$, $\alpha \ge 1$ and $\alpha + \beta + 1 \le k$. For a finite set
$A$ of integers write $\Sigma_\alpha^\beta(A)$ for the set of sums of subsets $B \subseteq A$ with
$\alpha \le |B| \le |A| - \beta$. Every set $A$ of $k$ positive integers satisfies
$|\Sigma_\alpha^\beta(A)| \ge \binom{k+1}{2} - \binom{\alpha+1}{2} - \binom{\beta+1}{2} + 1$,
and every set $A$ of $k$ nonnegative integers containing $0$ satisfies
$|\Sigma_\alpha^\beta(A)| \ge \binom{k}{2} - \binom{\alpha}{2} - \binom{\beta}{2} + 1$. Both
bounds are attained: the first by $A = \{1, 2, \dots, k\}$ and the second by
$A = \{0, 1, \dots, k - 1\}$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 6.

Stated but not proved: `MetaMathlibExt.card_boundedSubsetSums_ge_of_nonneg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subset-sums-ge-of-nonneg).

## Lower bound for bounded subset sums of a mixed-sign set

Let $n$, $p$, $\alpha$, $\beta$ be
natural numbers with $1 \le n \le p$, $1 \le \alpha$ and $\alpha + \beta + 1 \le n + p$, and let
$L_{n,p}(\alpha, \beta)$ be the mixed-sign subset-sum bound. For a finite set $A$ of integers write
$\Sigma_\alpha^\beta(A)$ for the set of sums of subsets $B \subseteq A$ with
$\alpha \le |B| \le |A| - \beta$. Every finite set $A$ of nonzero integers with exactly $n$
negative and exactly $p$ positive elements satisfies
$|\Sigma_\alpha^\beta(A)| \ge L_{n,p}(\alpha, \beta)$, and some such set $A$ attains equality.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 7.

Stated but not proved: `MetaMathlibExt.card_boundedSubsetSums_ge_mixedSign` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subset-sums-ge-mixed-sign).

## Lower bound for subset sums of a mixed-sign set containing zero

Let $n, p, \alpha, \beta$
be natural numbers with $1 \le n \le p$, $1 \le \alpha$ and $\alpha + \beta \le n + p$. Every
finite set $A$ of integers that contains $0$, exactly $n$ negative integers and exactly $p$
positive integers satisfies $|\Sigma^{\beta}_{\alpha}(A)| \ge L_0(\alpha, \beta, A)$, and some
such set $A$ attains equality. Here $\Sigma^{\beta}_{\alpha}(A)$ is the set of sums of subsets
$B \subseteq A$ with $\alpha \le |B| \le |A| - \beta$, and $L_0(\alpha, \beta, A)$ is the
mixed-sign bound with zero, which depends only on $n$, $p$, $\alpha$ and $\beta$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 8.

Stated but not proved: `MetaMathlibExt.card_boundedSubsetSums_ge_mixedSign_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subset-sums-ge-mixed-sign-z).

## Inverse theorem for subset sums of nonnegative sets

Let $k \ge 3$ and let $\alpha, \beta$
be natural numbers with $1 \le \alpha \le k - 2$, $\beta \le k - 2$ and $\alpha + \beta \le k - 1$.
Let $A$ be a set of $k$ integers, and let $\Sigma^{\beta}_{\alpha}(A)$ be the set of sums of
subsets $B \subseteq A$ with $\alpha \le |B| \le k - \beta$. If all elements of $A$ are positive
and $|\Sigma^{\beta}_{\alpha}(A)| = \binom{k+1}{2} - \binom{\alpha+1}{2} - \binom{\beta+1}{2} + 1$,
then $A = d \cdot \{1, 2, \dots, k\}$ for some integer $d > 0$ when $k \ne 3$, and
$A = \{x, y, x + y\}$ for some integers $0 < x < y$ when $k = 3$. If all elements of $A$ are
nonnegative, $0 \in A$ and
$|\Sigma^{\beta}_{\alpha}(A)| = \binom{k}{2} - \binom{\alpha}{2} - \binom{\beta}{2} + 1$, then
$A = d \cdot \{0, 1, \dots, k - 1\}$ for some integer $d > 0$ when $k \ge 5$,
$A = \{0, x, y\}$ for some integers $0 < x < y$ when $k = 3$, and
$A = \{0, x, y, x + y\}$ for some integers $0 < x < y$ when $k = 4$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 9.

Stated but not proved: `MetaMathlibExt.boundedSubsetSums_inverse_of_nonneg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-inverse-of-nonneg).

## Inverse theorem for subset sums of a mixed-sign set

Let $n, p, \alpha, \beta$ be natural
numbers with $1 \le n \le p$, put $k = n + p$, and assume $1 \le \alpha \le k - 2$,
$\beta \le k - 2$ and $\alpha + \beta \le k - 1$. Let $A$ be a finite set of integers that does
not contain $0$ and has exactly $n$ negative and exactly $p$ positive elements, and write $E$ for
the equation $|\Sigma^{\beta}_{\alpha}(A)| = L(\alpha, \beta, A)$. If $k = 3$, $\alpha = 1$ and
$\beta = 0$, then $E$ holds if and only if $A = d \cdot \{-1, 1, 2\}$ for some integer $d > 0$.
If $k = 3$ and $\alpha = \beta = 1$, then $E$ holds if and only if $A = \{x, x + y, y\}$ for some
integers $x, y$ with $x < 0 < x + y < y$. If $k \ge 4$, then $E$ holds if and only if
$A = d \cdot \{-n, \dots, -1, 1, \dots, p\}$ for some integer $d > 0$. Here
$\Sigma^{\beta}_{\alpha}(A)$ is the set of sums of subsets $B \subseteq A$ with
$\alpha \le |B| \le |A| - \beta$, and $L(\alpha, \beta, A)$ is the mixed-sign bound, which
depends only on $n$, $p$, $\alpha$ and $\beta$.

The factor $d$ is then the least positive element of $A$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 10.

Stated but not proved: `MetaMathlibExt.boundedSubsetSums_inverse_mixedSign` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-inverse-mixed-sign).

## Inverse theorem for subset sums of a mixed-sign set containing zero

Let $n, p, \alpha,
\beta$ be natural numbers with $1 \le n \le p$, put $k = n + p + 1$, and assume
$1 \le \alpha \le k - 2$, $\beta \le k - 2$ and $\alpha + \beta \le k - 1$. Let $A$ be a finite set
of integers that contains $0$, exactly $n$ negative integers and exactly $p$ positive integers.
Then $|\Sigma^{\beta}_{\alpha}(A)| = L_0(\alpha, \beta, A)$ if and only if
$A = d \cdot \{-n, -n + 1, \dots, p\}$ for some integer $d > 0$. Here $\Sigma^{\beta}_{\alpha}(A)$
is the set of sums of subsets $B \subseteq A$ with $\alpha \le |B| \le |A| - \beta$, and
$L_0(\alpha, \beta, A)$ is the mixed-sign bound with zero, which depends only on $n$, $p$,
$\alpha$ and $\beta$.

The factor $d$ is then the least positive element of $A$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 11.

Stated but not proved: `MetaMathlibExt.boundedSubsetSums_inverse_mixedSign_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subset-sums-inverse-mixed-sign-z).

## Lower bound for bounded subsequence sums of a positive sequence

Let $k \ge 2$, let
$t_1, \dots, t_k$ be positive integers, let $h = t_1 + \dots + t_k$, and let $\alpha, \beta$ be
natural numbers with $1 \le \alpha$ and $\alpha + \beta \le h - 1$. Put
$\bar r = (h - \alpha - \beta, t_1, \dots, t_k)$. For integers $0 < b_1 < \dots < b_k$, let
$\mathcal{A}$ be the sequence in which $b_i$ occurs $t_i$ times. Then
$|\Sigma^{\beta}_{\alpha}(\mathcal{A})| \ge L(\bar r, h - \beta)$ for all such $b$, and equality
holds for some such $b$. Here $\Sigma^{\beta}_{\alpha}(\mathcal{A})$ is the set of sums of
subsequences of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$ terms, and $L$ is the
Yang–Chen bound.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 13.

Stated but not proved: `MetaMathlibExt.card_boundedSubsequenceSums_ge_of_pos` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subsequence-sums-ge-of-pos).

## Lower bound for bounded subsequence sums of a nonnegative sequence containing zero

Let
$m \ge 1$, let $t_0, \dots, t_m$ be positive integers, let $h = t_0 + \dots + t_m$, and let
$\alpha, \beta$ be natural numbers with $1 \le \alpha$, $\beta \le h - 1$ and
$\alpha + \beta \le h$. Put $\bar r = (h - \alpha - \beta + t_0, t_1, \dots, t_m)$. For integers
$0 < b_1 < \dots < b_m$, let $\mathcal{A}$ be the sequence in which $0$ occurs $t_0$ times and
$b_i$ occurs $t_i$ times. Then $|\Sigma^{\beta}_{\alpha}(\mathcal{A})| \ge L(\bar r, h - \beta)$
for all such $b$, and equality holds for some such $b$. Here $\Sigma^{\beta}_{\alpha}(\mathcal{A})$
is the set of sums of subsequences of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$
terms, and $L$ is the Yang–Chen bound.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 14.

Stated but not proved: `MetaMathlibExt.card_boundedSubsequenceSums_ge_of_nonneg_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subsequence-sums-ge-of-nonn).

## Lower bound for bounded subsequence sums of a mixed-sign sequence

Let $1 \le n \le p$, let
$t_0, \dots, t_{n-1}$ and $t_{n+1}, \dots, t_{n+p}$ be positive integers, let $h$ be their sum,
and let $\alpha, \beta$ be natural numbers with $1 \le \alpha$ and $\alpha + \beta \le h - 1$.
Put $\bar r = (t_0, \dots, t_{n-1}, h - \alpha - \beta, t_{n+1}, \dots, t_{n+p})$. For integers
$c_0 < \dots < c_{n-1} < 0 < d_1 < \dots < d_p$, let $\mathcal{A}$ be the sequence in which
$c_i$ occurs $t_i$ times and $d_j$ occurs $t_{n+j}$ times. Then
$|\Sigma^{\beta}_{\alpha}(\mathcal{A})| \ge L(\bar r, h - \beta)$ for all such $c$ and $d$, and
equality holds for some such $c$ and $d$. Here $\Sigma^{\beta}_{\alpha}(\mathcal{A})$ is the set
of sums of subsequences of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$ terms, and
$L$ is the Yang–Chen bound.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 15.

Stated but not proved: `MetaMathlibExt.card_boundedSubsequenceSums_ge_mixedSign` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subsequence-sums-ge-mixed-s).

## Lower bound for bounded subsequence sums of a mixed-sign sequence containing zero

Let
$1 \le n \le p$, let $t_0, \dots, t_{n-1}$, $t_n$ and $t_{n+1}, \dots, t_{n+p}$ be positive
integers, let $h = t_0 + t_1 + \dots + t_{n+p}$, and let $\alpha, \beta$ be natural numbers with
$1 \le \alpha$ and $\alpha + \beta \le h - 1$. Put
$\bar r = (t_0, \dots, t_{n-1}, h - \alpha - \beta + t_n, t_{n+1}, \dots, t_{n+p})$. For integers
$c_0 < \dots < c_{n-1} < 0 < d_1 < \dots < d_p$, let $\mathcal{A}$ be the sequence in which
$c_i$ occurs $t_i$ times, $0$ occurs $t_n$ times and $d_j$ occurs $t_{n+j}$ times. Then
$|\Sigma^{\beta}_{\alpha}(\mathcal{A})| \ge L(\bar r, h - \beta)$ for all such $c$ and $d$, and
equality holds for some such $c$ and $d$. Here $\Sigma^{\beta}_{\alpha}(\mathcal{A})$ is the set
of sums of subsequences of $\mathcal{A}$ with at least $\alpha$ and at most $h - \beta$ terms, and
$L$ is the Yang–Chen bound.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 16.

Stated but not proved: `MetaMathlibExt.card_boundedSubsequenceSums_ge_mixedSign_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#card-bounded-subsequence-sums-ge-mixed-s-2).

## Inverse theorem for bounded subsequence sums of positive sequences

Let $k \ge 2$, let
$a_1 < \dots < a_k$ be positive integers and $A = \{a_1, \dots, a_k\}$, let $t_1, \dots, t_k$ be
positive integers, let $\mathcal{A}$ be the sequence in which each $a_i$ occurs $t_i$ times, and
let $h = t_1 + \dots + t_k$. Let $\alpha, \beta$ be natural numbers with
$1 \le \alpha \le h - 2$, $\beta \le h - 2$ and $\alpha + \beta \le h - 1$, put
$\bar r = (h - \alpha - \beta, t_1, \dots, t_k)$, and write $E$ for the equality
$|\Sigma^\beta_\alpha(\mathcal{A})| = L(\bar r, h - \beta)$, where $L$ is the Yang–Chen bound.
For an integer $e$ and a set $X$ write $e \cdot X = \{e x : x \in X\}$. Then:
(a) if $k = 2$ and $t_1 = 1$, then $E$ holds; if $k = 2$ and $t_1 \ge 2$, then $E$ holds if and
only if $A = e \cdot \{1, 2\}$ for some integer $e > 0$;
(b) if $k = 3$ and $t_1 = t_2 = 1$, then $E$ holds if and only if $A = \{x, y, x + y\}$ for some
integers $0 < x < y$; if $k = 3$ and $t_1 \ge 2$ or $t_2 \ge 2$, then $E$ holds if and only if
$A = e \cdot \{1, 2, 3\}$ for some integer $e > 0$;
(c) if $k \ge 4$, then $E$ holds if and only if $A = e \cdot \{1, 2, \dots, k\}$ for some integer
$e > 0$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 17.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_inverse_of_pos` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-inverse-of-pos).

## Inverse theorem for bounded subsequence sums of nonnegative sequences containing zero

Let
$m \ge 2$, let $0 < a_1 < \dots < a_m$ be integers, put $a_0 = 0$ and
$A = \{a_0, a_1, \dots, a_m\}$, let $t_0, t_1, \dots, t_m$ be positive integers, let
$\mathcal{A}$ be the sequence in which each $a_i$ occurs $t_i$ times, and let
$h = t_0 + t_1 + \dots + t_m$. Let $\alpha, \beta$ be natural numbers with
$1 \le \alpha \le h - 2$, $\beta \le h - 2$ and $\alpha + \beta \le h - 1$, put
$\bar r = (h - \alpha - \beta + t_0, t_1, \dots, t_m)$, and write $E$ for the equality
$|\Sigma^\beta_\alpha(\mathcal{A})| = L(\bar r, h - \beta)$, where $L$ is the Yang–Chen bound.
For an integer $e$ and a set $X$ write $e \cdot X = \{e x : x \in X\}$. Then:
(a) if $m = 2$ and $t_1 = 1$, then $E$ holds; if $m = 2$ and $t_1 \ge 2$, then $E$ holds if and
only if $A = e \cdot \{0, 1, 2\}$ for some integer $e > 0$;
(b) if $m = 3$ and $t_1 = t_2 = 1$, then $E$ holds if and only if $A = \{0, x, y, x + y\}$ for
some integers $0 < x < y$; if $m = 3$ and $t_1 \ge 2$ or $t_2 \ge 2$, then $E$ holds if and only
if $A = e \cdot \{0, 1, 2, 3\}$ for some integer $e > 0$;
(c) if $m \ge 4$, then $E$ holds if and only if $A = e \cdot \{0, 1, \dots, m\}$ for some integer
$e > 0$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 18.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_inverse_of_nonneg_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-inverse-of-nonn).

## Inverse theorem for bounded subsequence sums of mixed-sign sequences without zero

Let
$1 \le n \le p$, let $c_1 < \dots < c_n < 0 < d_1 < \dots < d_p$ be integers and
$A = \{c_1, \dots, c_n, d_1, \dots, d_p\}$, let $s_1, \dots, s_n, t_1, \dots, t_p$ be positive
integers, let $\mathcal{A}$ be the sequence in which each $c_i$ occurs $s_i$ times and each $d_j$
occurs $t_j$ times, and let $h = s_1 + \dots + s_n + t_1 + \dots + t_p$, with $h \ge 3$. Let
$\alpha, \beta$ be natural numbers with $1 \le \alpha \le h - 2$, $\beta \le h - 2$ and
$\alpha + \beta \le h - 1$, put $\bar r = (s_1, \dots, s_n, h - \alpha - \beta, t_1, \dots, t_p)$,
and write $E$ for the equality $|\Sigma^\beta_\alpha(\mathcal{A})| = L(\bar r, h - \beta)$, where
$L$ is the Yang–Chen bound. Then:
(a) if $n + p = 3$, $\alpha + \beta = h - 1$ and $t_1 = 1$, then $E$ holds if and only if
$A = \{x - y, x, y\}$ for some integers $0 < x < y$;
(b) in every other case, except $n + p = 2$ with $\alpha + \beta = h - 1$, $E$ holds if and only
if $A = \{e x : x \in \{-n, \dots, -1, 1, \dots, p\}\}$ for some integer $e > 0$.

The source states (b) also for $n + p = 2$ and $\alpha + \beta = h - 1$, but there $E$ holds for
every $A$: for $A = \{-2, 7\}$ with $s_1 = 1$, $t_1 = 2$ and $\alpha = \beta = 1$ one has
$|\Sigma^1_1(\mathcal{A})| = |\{-2, 5, 7, 14\}| = 4 = L((1, 1, 2), 2)$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 19.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_inverse_mixedSign` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-inverse-mixed-s).

## Inverse theorem for bounded subsequence sums of mixed-sign sequences containing zero

Let
$1 \le n \le p$, let $c_1 < \dots < c_n < 0 < d_1 < \dots < d_p$ be integers and
$A = \{c_1, \dots, c_n, 0, d_1, \dots, d_p\}$, a set of $k = n + p + 1$ elements, let
$s_1, \dots, s_n, z, t_1, \dots, t_p$ be positive integers, let $\mathcal{A}$ be the sequence in
which each $c_i$ occurs $s_i$ times, $0$ occurs $z$ times and each $d_j$ occurs $t_j$ times, and
let $h = s_1 + \dots + s_n + z + t_1 + \dots + t_p$. Let $\alpha, \beta$ be natural numbers with
$1 \le \alpha \le h - 2$, $\beta \le h - 2$ and $\alpha + \beta \le h$, put
$\bar r = (s_1, \dots, s_n, h - \alpha - \beta + z, t_1, \dots, t_p)$, and write $E$ for the
equality $|\Sigma^\beta_\alpha(\mathcal{A})| = L(\bar r, h - \beta)$, where $L$ is the Yang–Chen
bound. For an integer $e$ and a set $X$ write $e \cdot X = \{e x : x \in X\}$. Then:
(a) if $k = 3$ and $\alpha + \beta = h$, then $E$ holds when $z = 1$, and for $z \ge 2$, $E$ holds
if and only if $A = e \cdot \{-1, 0, 1\}$ for some integer $e > 0$;
(b) if $k = 3$ and $\alpha + \beta \le h - 1$, then $E$ holds if and only if
$A = e \cdot \{-1, 0, 1\}$ for some integer $e > 0$;
(c) if $k = 4$ and $\alpha + \beta = h$, then for $z = t_1 = 1$, $E$ holds if and only if
$A = \{x - y, 0, x, y\}$ for some integers $0 < x < y$, and for $z \ge 2$ or $t_1 \ge 2$, $E$
holds if and only if $A = e \cdot \{-1, 0, 1, 2\}$ for some integer $e > 0$;
(d) if $k = 4$ and $\alpha + \beta \le h - 1$, then $E$ holds if and only if
$A = e \cdot \{-1, 0, 1, 2\}$ for some integer $e > 0$;
(e) if $k \ge 5$, then $E$ holds if and only if $A = e \cdot \{-n, \dots, p\}$ for some integer
$e > 0$.

## Sources

- Raj Kumar Mistri, *Subset and Subsequence Sums with Bounded Numbers of Terms*, INTEGERS 24 (2024), Article A116, Theorem 20.

Stated but not proved: `MetaMathlibExt.boundedSubsequenceSums_inverse_mixedSign_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/BoundedSubsetSumsWanted.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html#bounded-subsequence-sums-inverse-mixed-s-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subset sums with a bounded number of terms](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/subset-sums-with-a-bounded-number-of-terms)
