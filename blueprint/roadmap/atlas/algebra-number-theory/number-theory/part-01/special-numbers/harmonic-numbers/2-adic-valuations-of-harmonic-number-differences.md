---
declaration: section
origin: cited
lean: MetaMathlibExt.weightedBinaryDigitSum, MetaMathlibExt.weightedBinaryDigitSum_two, MetaMathlibExt.weightedBinaryDigitSum_four, MetaMathlibExt.padicValRat_two_harmonic_sub_neg, MetaMathlibExt.card_filter_padicValRat_two_harmonic_sub, MetaMathlibExt.padicValRat_two_harmonic_two_mul_sub, MetaMathlibExt.padicValRat_two_harmonic_pow_sub, MetaMathlibExt.sum_padicValRat_two_harmonic_sub
statement: formalized
---

# 2-adic valuations of harmonic number differences

11 results, 3 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html).

## Weighted binary digit sum

For a natural number $n$, the weighted binary digit sum of $n$
is $a(n) = \sum_i i \cdot 2^i$, where $i$ runs over the indices of the $1$ bits in the binary
expansion of $n$. Equivalently, if $n = 2^{a_1} + \dots + 2^{a_t}$ with distinct exponents
$a_1, \dots, a_t$, then $a(n) = a_1 2^{a_1} + \dots + a_t 2^{a_t}$; in particular $a(0) = 0$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Corollary 2 and Theorem 4; the first values `0, 0, 2, 2, 8, 8, 10, 10, 24, ...` are displayed there.

Formalized by `MetaMathlibExt.weightedBinaryDigitSum`, a definition declared in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#weighted-binary-digit-sum).

## Weighted binary digit sum of 2

The weighted binary digit sum of $2$ is $a(2) = 2$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 4 (displayed values).

Formalized by `MetaMathlibExt.weightedBinaryDigitSum_two`, a theorem declared in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#weighted-binary-digit-sum-two).

## Weighted binary digit sum of 4

The weighted binary digit sum of $4$ is $a(4) = 8$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 4 (displayed values).

Formalized by `MetaMathlibExt.weightedBinaryDigitSum_four`, a theorem declared in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#weighted-binary-digit-sum-four).

## Kürschák's strengthening of Theisinger's theorem

Let $H_k = \sum_{j=1}^{k} 1/j$ be the
$k$-th harmonic number (so $H_0 = 0$) and let $\nu_2$ denote the $2$-adic valuation on the
rational numbers. For all natural numbers $m$ and $n$ with $m + 2 \le n$, the $2$-adic valuation
$\nu_2(H_n - H_m)$ is negative; that is, $H_n - H_m$ is not a $2$-adic integer.

In particular $H_n - H_m$ is not an integer.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 2. for `0 ≤ m ≤ n - 2` the difference `H_n - H_m` does not lie in the ring of `2`-adic integers.

Stated but not proved: `MetaMathlibExt.padicValRat_two_harmonic_sub_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#padic-val-rat-two-harmonic-sub-neg).

## Fiber counts of the 2-adic valuations of $H_n - H_m$

Let $H_k = \sum_{j=1}^{k} 1/j$ be
the $k$-th harmonic number (so $H_0 = 0$) and let $\nu_2$ denote the $2$-adic valuation on the
rational numbers. Let $n$ and $a$ be natural numbers such that the binary digit of $n$ in
position $a$ is $1$, that is, $2^a$ occurs in the binary expansion of $n$. Then exactly $2^a$ of
the natural numbers $m < n$ satisfy $\nu_2(H_n - H_m) = -a$.

The source theorem also locates these values of $m$ in intervals determined by the partial sums
of the binary expansion of $n$; that refinement is not part of this statement.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 3: writing `n = ∑_{i=1}^{t} 2^{aᵢ}` in binary, among the values `ν₂(H_n - H_m)` for `m = 0, 1, …, n - 1` exactly `2^{aᵢ}` are equal to `-aᵢ`, for each exponent `aᵢ` occurring in the expansion.

Stated but not proved: `MetaMathlibExt.card_filter_padicValRat_two_harmonic_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#card-filter-padic-val-rat-two-harmonic-s).

## 2-adic valuation of $H_{2n} - H_n$

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th harmonic
number and let $\nu_2$ denote the $2$-adic valuation on the rational numbers. For every natural
number $n \ge 1$, $\nu_2(H_{2n} - H_n) = -\lfloor \log_2(2n) \rfloor$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Lemma 1: for `n ≥ 1`, `ν₂(H_{2n} - H_n) = -⌊log₂(2n)⌋`.

Stated but not proved: `MetaMathlibExt.padicValRat_two_harmonic_two_mul_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#padic-val-rat-two-harmonic-two-mul-sub).

## 2-adic valuation of $H_{2^a} - H_{2^a - m}$

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th
harmonic number (so $H_0 = 0$) and let $\nu_2$ denote the $2$-adic valuation on the rational
numbers. For all natural numbers $a$ and $m$ with $1 \le m \le 2^a$,
$\nu_2(H_{2^a} - H_{2^a - m}) = -a$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Corollary 1: if `n = 2^a` is a power of `2` then `ν₂(H_n - H_{n-m}) = -a` for every `1 ≤ m ≤ n`.

Stated but not proved: `MetaMathlibExt.padicValRat_two_harmonic_pow_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#padic-val-rat-two-harmonic-pow-sub).

## Sum of the 2-adic valuations of $H_n - H_m$

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th
harmonic number (so $H_0 = 0$), let $\nu_2$ denote the $2$-adic valuation on the rational
numbers, and let $a(n)$ be the weighted binary digit sum of $n$. For every natural number $n$,
$\sum_{m=0}^{n-1} \nu_2(H_n - H_m) = -a(n)$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Corollary 2: `∑_{m=0}^{n-1} ν₂(H_n - H_m) = -a(n)`, where `a(n) = weightedBinaryDigitSum n`.

Stated but not proved: `MetaMathlibExt.sum_padicValRat_two_harmonic_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#sum-padic-val-rat-two-harmonic-sub).

## Recurrence for the weighted binary digit sum

Let $a(n)$ denote the weighted binary digit
sum of $n$. For every natural number $n$, $a(2n) = 2a(n) + 2n$ and $a(2n + 1) = a(2n)$.

The source theorem also gives a two-variable generating function, which is not part of this
statement.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 4: the weighted binary digit sum satisfies `a(2n) = 2a(n) + 2n` and `a(2n + 1) = a(2n)`, with `a(0) = a(1) = 0`.

Stated but not proved: `MetaMathlibExt.weightedBinaryDigitSum_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#weighted-binary-digit-sum-recurrence).

## 2-adic valuation of $H_n - H_{n-2^r}$

Let $H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th
harmonic number and let $\nu_2$ denote the $2$-adic valuation on the rational numbers. For all
natural numbers $r$ and $n$ with $2^r \le n$,
$\nu_2(H_n - H_{n-2^r}) = -r - \nu_2(\lfloor n / 2^r \rfloor)$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 5: for `m = 2^r` with `1 ≤ m ≤ n`, `ν₂(H_n - H_{n-m}) = -r - ν₂(⌊n / m⌋)`.

Stated but not proved: `MetaMathlibExt.padicValRat_two_harmonic_sub_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#padic-val-rat-two-harmonic-sub-pow).

## Piecewise formula for the 2-adic valuation of $H_n - H_{n-m}$

Let
$H_k = \sum_{j=1}^{k} 1/j$ be the $k$-th harmonic number and let $\nu_2$ denote the $2$-adic
valuation on the rational numbers (for a positive integer it is the exponent of $2$ in its
factorization). Let $m$ and $n$ be natural numbers with $1 \le m \le n$, and put
$M = \lceil \log_2(m + 1) \rceil$ and $j = \lfloor (n - m) / 2^M \rfloor$. If
$2^M j + m \le n \le 2^M (j + 1) - 1$, then $\nu_2(H_n - H_{n-m}) = 1 - M$. If
$2^M (j + 1) \le n \le 2^M (j + 1) + m - 1$, then $\nu_2(H_n - H_{n-m}) = -M - \nu_2(j + 1)$.

## Sources

- Lengyel, *On the 2-Adic Valuation of Differences of Harmonic Numbers*, INTEGERS 24 (2024), Article A27, Theorem 6, formula (3.1): let `M = ⌈log₂(m + 1)⌉` and `j = ⌊(n - m) / 2^M⌋`, where `1 ≤ m ≤ n`. Then `ν₂(H_n - H_{n-m}) = -M + 1` when `2^M * j + m ≤ n ≤ 2^M * (j + 1) - 1`, and `ν₂(H_n - H_{n-m}) = -M - ν₂(j + 1)` when `2^M * (j + 1) ≤ n ≤ 2^M * (j + 1) + m - 1`.

Stated but not proved: `MetaMathlibExt.padicValRat_two_harmonic_sub_piecewise` is written with `theorem_wanted` in [WantedExt/NumberTheory/HarmonicValuationWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HarmonicValuationWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html#padic-val-rat-two-harmonic-sub-piecewise).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-adic valuations of harmonic number differences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/2-adic-valuations-of-harmonic-number-differences)
