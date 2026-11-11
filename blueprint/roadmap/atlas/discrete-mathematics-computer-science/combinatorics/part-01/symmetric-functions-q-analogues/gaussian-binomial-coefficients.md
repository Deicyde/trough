---
declaration: section
origin: cited
lean: MathlibExt.gaussBinom, MathlibExt.gaussBinom_zero_right, MathlibExt.gaussBinom_zero_succ, MathlibExt.gaussBinom_succ_succ, MathlibExt.gaussBinom_eq_zero_of_lt, MathlibExt.gaussBinom_self, MathlibExt.qPochFin, MathlibExt.qPochFin_zero
statement: formalized
proof: formalized
---

# Gaussian binomial coefficients

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html).

## Gaussian binomial coefficient

Let $R$ be a semiring and $Q \in R$. For natural numbers
$M$ and $k$, the Gaussian binomial coefficient $\binom{M}{k}_Q \in R$ is defined recursively by
$\binom{M}{0}_Q = 1$, $\binom{0}{k+1}_Q = 0$ and
$\binom{M+1}{k+1}_Q = \binom{M}{k}_Q + Q^{k+1} \binom{M}{k+1}_Q$.

Formalized by `MathlibExt.gaussBinom`, a definition declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom).

## Gaussian binomial coefficients with $k = 0$

Let $R$ be a semiring and $Q \in R$. For
every natural number $M$, the Gaussian binomial coefficient $\binom{M}{0}_Q$ equals $1$.

Formalized by `MathlibExt.gaussBinom_zero_right`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-zero-right).

## Gaussian binomial coefficients with $M = 0$

Let $R$ be a semiring and $Q \in R$. For
every natural number $k$, the Gaussian binomial coefficient $\binom{0}{k+1}_Q$ equals $0$.

Formalized by `MathlibExt.gaussBinom_zero_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-zero-succ).

## $Q$-Pascal recursion for Gaussian binomial coefficients

Let $R$ be a semiring and
$Q \in R$. For all natural numbers $M$ and $k$, the Gaussian binomial coefficients satisfy
$\binom{M+1}{k+1}_Q = \binom{M}{k}_Q + Q^{k+1} \binom{M}{k+1}_Q$.

Formalized by `MathlibExt.gaussBinom_succ_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-succ-succ).

## Gaussian binomial coefficients vanish when $k > M$

Let $R$ be a semiring and $Q \in R$.
For natural numbers $M$ and $k$ with $M < k$, the Gaussian binomial coefficient $\binom{M}{k}_Q$
is $0$.

Formalized by `MathlibExt.gaussBinom_eq_zero_of_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-eq-zero-of-lt).

## Diagonal Gaussian binomial coefficients

Let $R$ be a semiring and $Q \in R$. For every
natural number $M$, the Gaussian binomial coefficient $\binom{M}{M}_Q$ equals $1$.

Formalized by `MathlibExt.gaussBinom_self`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-self).

## Finite $Q$-Pochhammer symbol

Let $R$ be a commutative ring and $Q \in R$. For a natural
number $m$, the finite $Q$-Pochhammer symbol $P_Q(m) \in R$ is the product
$\prod_{i < m} (1 - Q^{i+1})$ of $1 - Q^{i+1}$ over the natural numbers $i < m$.

Formalized by `MathlibExt.qPochFin`, a definition declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#q-poch-fin).

## The finite $Q$-Pochhammer symbol at $0$

Let $R$ be a commutative ring and $Q \in R$. The
finite $Q$-Pochhammer symbol $P_Q(m) = \prod_{i < m} (1 - Q^{i+1})$, the product running over the
natural numbers $i < m$, satisfies $P_Q(0) = 1$.

Formalized by `MathlibExt.qPochFin_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#q-poch-fin-zero).

## Recursion for the finite $Q$-Pochhammer symbol

Let $R$ be a commutative ring and
$Q \in R$, and write $P_Q(m) = \prod_{i < m} (1 - Q^{i+1})$ for the finite $Q$-Pochhammer symbol,
the product running over the natural numbers $i < m$. For every natural number $m$,
$P_Q(m+1) = P_Q(m) \, (1 - Q^{m+1})$.

Formalized by `MathlibExt.qPochFin_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#q-poch-fin-succ).

## Product formula for Gaussian binomial coefficients

Let $R$ be a commutative ring and
$Q \in R$, and write $P_Q(m) = \prod_{i < m} (1 - Q^{i+1})$ for the finite $Q$-Pochhammer symbol,
the product running over the natural numbers $i < m$. For natural numbers $k \le M$, the Gaussian
binomial coefficient satisfies $\binom{M}{k}_Q \, P_Q(k) \, P_Q(M - k) = P_Q(M)$.

Formalized by `MathlibExt.gaussBinom_mul_qPochFin_mul_qPochFin`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianBinomial.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gauss-binom-mul-q-poch-fin-mul-q-poch-fi).

## Ehrenborg–Readdy expansion of the Gaussian coefficient

Let $n$ and $k$ be natural numbers
and let $W$ be the set of words $v = v_0 v_1 \cdots v_{n-1}$ over the alphabet $\{0, 1\}$ with
exactly $k$ letters equal to $1$. For a word $v$, let $\operatorname{inv}(v)$ be the number of
pairs $i < j$ with $v_i > v_j$; call $v$ pair-sorted when $v_{2i} \le v_{2i+1}$ for every $i$
with $2i + 1 < n$; and let $\operatorname{asc}_{\mathrm{odd}}(v)$ be the number of $i$ with
$2i + 1 < n$ and $v_{2i} < v_{2i+1}$. Then, in the polynomial ring $\mathbb{N}[q]$,

$$\sum_{v \in W} q^{\operatorname{inv}(v)} = \sum_{v \in W,\ v \text{ pair-sorted}}
q^{\operatorname{inv}(v)} (1 + q)^{\operatorname{asc}_{\mathrm{odd}}(v)}.$$

The left side is MacMahon's inversion generating polynomial of $W$, which equals the Gaussian
coefficient $\binom{n}{k}_q$. Positions are numbered from $0$, so the pairs $(v_{2i}, v_{2i+1})$
are the source's pairs of positions $(1, 2), (3, 4), \ldots$, and
$\operatorname{asc}_{\mathrm{odd}}$ counts its odd ascents.

## Sources

- Richard Ehrenborg and Margaret A. Readdy, "The Gaussian Coefficient Revisited," Journal of Integer Sequences 19 (2016), Article 16.7.8, Corollary 3, equation, lines 301–311, https://cs.uwaterloo.ca/journals/JIS/VOL19/Ehrenborg/ehr3.tex

Formalized by `MetaMathlibExt.gaussian_pair_sorted_expansion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GaussianQBinomial.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GaussianQBinomial.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html#gaussian-pair-sorted-expansion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/gaussian-binomial-coefficients)
