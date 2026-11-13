---
declaration: section
origin: cited
lean: MetaMathlibExt.IsTribonacciRepr, MetaMathlibExt.isTribonacciRepr_nil, MetaMathlibExt.isTribonacciRepr_nine, MetaMathlibExt.tribonacciWord_eq_of_isTribonacciRepr, MetaMathlibExt.abs_tribonacci_succ_sub_mul_lt, MetaMathlibExt.tribonacci_succ_sub_mul_sign_changes, MetaMathlibExt.tendsto_trithoff_first_column_div, MetaMathlibExt.exists_fibternary_sum_four_and_tribternary_sum_three
statement: formalized
---

# Tribonacci representations and the Trithoff array

40 results, 16 proved and 24 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html).

## Tribonacci representation

Let $T_n$ be the Tribonacci numbers, $T_0 = T_1 = 0$,
$T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$. A list $w = (w_0, \dots, w_{\ell-1})$ of
natural numbers, read least significant digit first, is a Tribonacci representation of a
natural number $n$ when every digit $w_i$ is $0$ or $1$, no three consecutive entries of $w$
are all equal to $1$, and $n = \sum_{i=0}^{\ell-1} w_i T_{i+3}$. Leading zeros (trailing
entries of $w$) are allowed.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 2.3 (Tribonacci representation).

Formalized by `MetaMathlibExt.IsTribonacciRepr`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#is-tribonacci-repr).

## The empty word represents zero

The empty digit list is a Tribonacci representation
of $0$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 2.3.

Formalized by `MetaMathlibExt.isTribonacciRepr_nil`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#is-tribonacci-repr-nil).

## A Tribonacci representation of nine

The digit list $(0, 1, 0, 1)$, read least
significant digit first (the word $1010$ written most significant digit first), is a
Tribonacci representation of $9$.

With $T_n$ the Tribonacci numbers ($T_0 = T_1 = 0$, $T_2 = 1$), this is
$9 = T_6 + T_4 = 7 + 2$, the paper's example $(9)_T = 1010$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 2.3.

Formalized by `MetaMathlibExt.isTribonacciRepr_nine`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#is-tribonacci-repr-nine).

## Duchêne–Rigo: letters of the Tribonacci word from Tribonacci representations

Let $w$
be a Tribonacci representation of a natural number $m$, written most significant digit first,
with missing digits read as $0$. The letter of the infinite Tribonacci word at position $m$
(positions counted from $0$) is $a$ if $w$ ends in $0$, $b$ if $w$ ends in $01$, and $c$ if $w$
ends in $11$. In particular the empty representation of $0$ ends in $0$, and the
representation $1$ of $1$ ends in $01$.

This is the paper's statement about the $n$-th letter, with $m = n - 1$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 1 (quoting Duchêne and Rigo 2008) (`jis-2025-25.5.4-thm-1`).

Stated but not proved: `MetaMathlibExt.tribonacciWord_eq_of_isTribonacciRepr` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-word-eq-of-is-tribonacci-repr).

## Tribonacci approximation error bound

Let $T_0 = T_1 = 0$, $T_2 = 1$,
$T_{m+3} = T_{m+2} + T_{m+1} + T_m$ be the Tribonacci numbers, let $\alpha$ be the real root of
$x^3 = x^2 + x + 1$, and let $\beta$ be a non-real complex root of the same equation, with
$\gamma = \overline{\beta}$ the other non-real root. Then for every natural number $n$,

$$|T_{n+1} - \alpha T_n| < \frac{2 \alpha^{-n/2}}{|\beta - \gamma|}.$$

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 2 (`jis-2025-25.5.4-lem-2`).

Stated but not proved: `MetaMathlibExt.abs_tribonacci_succ_sub_mul_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#abs-tribonacci-succ-sub-mul-lt).

## Tribonacci differences do not keep one strict sign for three steps

Let $T_n$ be the
Tribonacci numbers ($T_0 = T_1 = 0$, $T_2 = 1$, $T_{n+3} = T_{n+2} + T_{n+1} + T_n$) and let
$\alpha$ be a real number with $\alpha^3 = \alpha^2 + \alpha + 1$. Then for every $n \ge 0$ the
three numbers $T_{k+1} - \alpha T_k$ for $k = n, n + 1, n + 2$ are neither all positive nor all
negative.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 3 (`jis-2025-25.5.4-prop-3`).

Stated but not proved: `MetaMathlibExt.tribonacci_succ_sub_mul_sign_changes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-succ-sub-mul-sign-changes).

## Growth of the first column of the Trithoff array

Let $\alpha$ be a real number with
$\alpha^3 = \alpha^2 + \alpha + 1$, and let $a_0 < a_1 < a_2 < \cdots$ be the positive integers
that have a Tribonacci representation with least significant digit $1$, in increasing order
(the first column of the Trithoff array, OEIS A003265). Then $a_r / (r + 1)$ tends to
$\alpha / (\alpha - 1)$ as $r \to \infty$.

The limit equals $(\alpha^2 + 1) / 2$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 6 (`jis-2025-25.5.4-prop-6`).

Stated but not proved: `MetaMathlibExt.tendsto_trithoff_first_column_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tendsto-trithoff-first-column-div).

## Sums of Fibternary and Tribternary numbers

Call a natural number Fibternary if its
base-$3$ digits are all $0$ or $1$ with no two consecutive $1$s, and Tribternary if its
base-$3$ digits are all $0$ or $1$ with no three consecutive $1$s. Every natural number is a
sum of four Fibternary numbers and also a sum of three Tribternary numbers (the summands
may be $0$ and need not be distinct).

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 21 (`jis-2025-25.5.4-prop-21`).

Stated but not proved: `MetaMathlibExt.exists_fibternary_sum_four_and_tribternary_sum_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#exists-fibternary-sum-four-and-tribterna).

## Fibternary multiples

Every positive integer $n$ has a positive multiple $m$ that is
Fibternary: the base-$3$ digits of $m$ are all $0$ or $1$, and no two consecutive digits
of $m$ are both $1$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 22 (`jis-2025-25.5.4-prop-22`).

Stated but not proved: `MetaMathlibExt.exists_fibternary_multiple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#exists-fibternary-multiple).

## Tribbinary and Tribternary multiples

Every positive integer $n$ has a positive
multiple whose binary digits contain no three consecutive $1$s (a Tribbinary number), and a
positive multiple whose base-$3$ digits are all $0$ or $1$ with no three consecutive $1$s (a
Tribternary number).

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Corollary 23 (`jis-2025-25.5.4-cor-23`).

Stated but not proved: `MetaMathlibExt.exists_tribbinary_and_tribternary_multiple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#exists-tribbinary-and-tribternary-multip).

## Tribonacci value of a digit word

Let $T_0 = T_1 = 0$, $T_2 = 1$ and
$T_{k+3} = T_{k+2} + T_{k+1} + T_k$ be the Tribonacci numbers. The Tribonacci value of a finite
word $w$ of natural-number digits $w_0, w_1, \dots, w_{\ell-1}$, listed from the least
significant digit, is $[w]_T = \sum_{i=0}^{\ell-1} w_i T_{i+3}$, so the digits weigh
$1, 2, 4, 7, 13, \dots$. Digits may exceed $1$ and three consecutive ones are allowed, so this
also evaluates the paper's non-canonical and improper representations.

For a Tribonacci representation $w$ of $n$, the value of $w$ followed by a new least
significant digit $0$ is the Tribonacci successor $\mathrm{out}(n)$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Sections 2.3, 5 and 6.1.

Formalized by `MetaMathlibExt.tribonacciValue`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-value).

## The empty digit word has Tribonacci value zero

The Tribonacci value of the empty
digit word is $0$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 2.3.

Formalized by `MetaMathlibExt.tribonacciValue_nil`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-value-nil).

## The non-canonical Tribonacci word $1110$ has value $13$

The digit word $1110$, written
most significant digit first, whose digits weigh the Tribonacci numbers $T_6 = 7$, $T_5 = 4$,
$T_4 = 2$ and $T_3 = 1$, has Tribonacci value $7 + 4 + 2 = 13$. It is the paper's example of a
non-canonical representation: its digits are $0$ and $1$ but it has three consecutive ones.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 5.

Formalized by `MetaMathlibExt.tribonacciValue_one_one_one_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-value-one-one-one-zero).

## The improper Tribonacci word $1030$ has value $13$

The digit word $1030$, written most
significant digit first, whose digits weigh the Tribonacci numbers $T_6 = 7$, $T_5 = 4$,
$T_4 = 2$ and $T_3 = 1$, has Tribonacci value $1 \cdot 7 + 3 \cdot 2 = 13$. It is the paper's
example of an improper representation, with a digit larger than $1$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciValue_one_zero_three_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-value-one-zero-three-zero).

## Indices used by records of the Tribonacci successor

Let $T_n$ be the Tribonacci numbers
($T_0 = T_1 = 0$, $T_2 = 1$, $T_{n+3} = T_{n+2} + T_{n+1} + T_n$) and let $\alpha$ be a real
number with $\alpha^3 = \alpha^2 + \alpha + 1$. For each $n$ fix a Tribonacci representation
$R(n) = (r_0, r_1, \dots, r_{\ell-1})$ of $n$: digits in $\{0, 1\}$ with no three consecutive
ones and $n = \sum_i r_i T_{i+3}$. Let $\mathrm{out}(n) = \sum_i r_i T_{i+4}$ be the Tribonacci
successor of $n$. Call $n$ a positive record if $n > 0$ and
$\mathrm{out}(m) - \alpha m < \mathrm{out}(n) - \alpha n$ for every $m < n$, and a negative
record if $n > 0$ and $\mathrm{out}(n) - \alpha n < \mathrm{out}(m) - \alpha m$ for every
$m < n$. If the digit $r_i$ of $R(n)$ equals $1$, then $T_{i+4} - \alpha T_{i+3} > 0$ when $n$
is a positive record, and $T_{i+4} - \alpha T_{i+3} < 0$ when $n$ is a negative record.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 4, part 1 and its negative analogue (`jis-2025-25.5.4-prop-4`).

Stated but not proved: `MetaMathlibExt.tribonacciSucc_record_indices` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-succ-record-indices).

## Partial sums along the positive and negative indices are records

Let $T_n$ be the
Tribonacci numbers ($T_0 = T_1 = 0$, $T_2 = 1$, $T_{n+3} = T_{n+2} + T_{n+1} + T_n$) and let
$\alpha$ be a real number with $\alpha^3 = \alpha^2 + \alpha + 1$. For each $n$ fix a Tribonacci
representation $R(n) = (r_0, r_1, \dots, r_{\ell-1})$ of $n$: digits in $\{0, 1\}$ with no three
consecutive ones and $n = \sum_i r_i T_{i+3}$. Let $\mathrm{out}(n) = \sum_i r_i T_{i+4}$ be the
Tribonacci successor of $n$. Call $n$ a positive record if $n > 0$ and
$\mathrm{out}(m) - \alpha m < \mathrm{out}(n) - \alpha n$ for every $m < n$, and a negative
record if $n > 0$ and $\mathrm{out}(n) - \alpha n < \mathrm{out}(m) - \alpha m$ for every
$m < n$. Let $P(1) < P(2) < \cdots$ list the indices $i$ with $T_{i+1} - \alpha T_i > 0$, and
$Q(1) < Q(2) < \cdots$ those with $T_{i+1} - \alpha T_i < 0$. Then for every $k \ge 2$ the
number $T_{P(2)} + \cdots + T_{P(k)}$ is a positive record and $T_{Q(2)} + \cdots + T_{Q(k)}$ is
a negative record.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 4, part 2 and its negative analogue (`jis-2025-25.5.4-prop-4`).

Stated but not proved: `MetaMathlibExt.tribonacciSucc_record_of_partial_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-succ-record-of-partial-sum).

## Late records use $T_{P(t)}$ and $T_{Q(t)}$

Let $T_n$ be the Tribonacci numbers
($T_0 = T_1 = 0$, $T_2 = 1$, $T_{n+3} = T_{n+2} + T_{n+1} + T_n$) and let $\alpha$ be a real
number with $\alpha^3 = \alpha^2 + \alpha + 1$. For each $n$ fix a Tribonacci representation
$R(n) = (r_0, r_1, \dots, r_{\ell-1})$ of $n$: digits in $\{0, 1\}$ with no three consecutive
ones and $n = \sum_i r_i T_{i+3}$. Let $\mathrm{out}(n) = \sum_i r_i T_{i+4}$ be the Tribonacci
successor of $n$. Call $n$ a positive record if $n > 0$ and
$\mathrm{out}(m) - \alpha m < \mathrm{out}(n) - \alpha n$ for every $m < n$, and a negative
record if $n > 0$ and $\mathrm{out}(n) - \alpha n < \mathrm{out}(m) - \alpha m$ for every
$m < n$. Let $P(1) < P(2) < \cdots$ list the indices $i$ with $T_{i+1} - \alpha T_i > 0$, and
$Q(1) < Q(2) < \cdots$ those with $T_{i+1} - \alpha T_i < 0$. Let $t > 1$. If
$n_0 < n_1 < \cdots$ are the positive records, there is $N_0$ such that for every $N > N_0$ the
representation $R(n_N)$ has digit $1$ at index $P(t) - 3$, that is, it uses $T_{P(t)}$. If
$n'_0 < n'_1 < \cdots$ are the negative records, there is $N_0$ such that for every $N > N_0$
the representation $R(n'_N)$ has digit $1$ at index $Q(t) - 3$, that is, it uses $T_{Q(t)}$.

The paper states part 3 for negative records with $P(t)$; following its remark that similar
statements hold for negative differences, it is read with $Q(t)$, since a negative record uses
only indices $i$ with $T_{i+1} - \alpha T_i < 0$ (Proposition 4, part 1).

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 4, part 3 (`jis-2025-25.5.4-prop-4`).

Stated but not proved: `MetaMathlibExt.tribonacciSucc_record_eventually_contains` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-succ-record-eventually-contai).

## Row numbers of the Trithoff array

Let $T_0 = T_1 = 0$, $T_2 = 1$ and
$T_{k+3} = T_{k+2} + T_{k+1} + T_k$ be the Tribonacci numbers, and let $U_i = T_i + T_{i+1}$,
so that $U_0, U_1, U_2, \dots = 0, 1, 2, 3, 6, 11, \dots$. Let $n$ have Tribonacci
representation $a1$, where $a$ is a digit word written most significant digit first, and let
$[a]_T$ be the Tribonacci value of $a$. Then $n$ is the $(n - [a]_T)$-th smallest positive
integer whose Tribonacci representation ends in $1$ (OEIS A003265, the first column of the
Trithoff array), and $n - [a]_T = 1 + [a1]_U$, where $[a1]_U$ is the sum of the digits of $a1$
weighted by $U_0, U_1, U_2, \dots$ starting from the least significant digit.

The paper writes $U_i = T_{2,i-2}$; its alternative formula $T_{i+1} - T_i$ is shifted, and the
displayed values $0, 1, 2, 3, 6, 11, \dots$ are used.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 7 (`jis-2025-25.5.4-lem-7`).

Stated but not proved: `MetaMathlibExt.trithoff_row_number_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#trithoff-row-number-eq).

## Differences along a Trithoff row

Let $T_0 = T_1 = 0$, $T_2 = 1$ and
$T_{m+3} = T_{m+2} + T_{m+1} + T_m$ be the Tribonacci numbers, and for a finite word
$w = (w_0, \dots, w_{\ell-1})$ of natural-number digits, listed from the least significant
digit, let $[w]_T = \sum_{i=0}^{\ell-1} w_i T_{i+3}$ be its Tribonacci value. Let
$a = (a_0, \dots, a_{\ell-1})$ be a Tribonacci representation of a natural number $n$ (all
digits $0$ or $1$, no three consecutive ones, and $[a]_T = n$), and let
$b = (b_0, \dots, b_\ell)$ be the word with $b_i = a_i + a_{i-1}$, where $a_{-1} = a_\ell = 0$
(the product $11 \cdot a$ computed digit-wise without carries). For $k \ge 0$ write $0^k a$ for
the word $(0, \dots, 0, a_0, \dots, a_{\ell-1})$ with $k$ zeros placed before $a_0$, that is, at
the least significant end. Then there is a natural number $k$ with
$[0^{k+1} a]_T - [0^k a]_T = [b]_T$.

The entries of the Trithoff row of $n$ from $n$ onwards are $[0^k a]_T$ for $k \ge 0$, so
$[b]_T$ is the difference of two consecutive entries of that row.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 8 (`jis-2025-25.5.4-prop-8`).

Stated but not proved: `MetaMathlibExt.exists_trithoff_row_difference_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#exists-trithoff-row-difference-eq).

## Appending a zero to a non-canonical Tribonacci representation

Let $T_0 = T_1 = 0$,
$T_2 = 1$ and $T_{k+3} = T_{k+2} + T_{k+1} + T_k$ be the Tribonacci numbers, and for a digit
word $u$, written most significant digit first, let $[u]_T$ be its Tribonacci value, in which
the $i$-th digit from the right (counting from $0$) weighs $T_{i+3}$. Let $w$ be a digit word
with all digits in $\{0, 1\}$ (three consecutive ones are allowed) and $[w]_T = n$, and let $v$
be a Tribonacci representation of $n$. Then $[w0]_T = [v0]_T$, where $w0$ and $v0$ are $w$ and
$v$ followed by the digit $0$; that is, $w0$ evaluates to the Tribonacci successor
$\mathrm{out}(n) = [v0]_T$ of $n$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 12 (`jis-2025-25.5.4-lem-12`).

Stated but not proved: `MetaMathlibExt.tribonacciValue_cons_zero_of_noncanonical` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-value-cons-zero-of-noncanonic).

## Precolumns of the Trithoff array

Write $[u]_T$ for the Tribonacci value of a digit
word $u$, written most significant digit first. Let $n$ have Tribonacci representation $abc1$,
where $a$ is a digit word and $b$, $c$ are digits. Let $\mathrm{out}(n) = [abc10]_T$ and
$\mathrm{out}^2(n) = [abc100]_T$ be the next two entries of the Trithoff row of $n$, and extend
the row to the left by the Tribonacci rule: in the integers, the wall is
$W = \mathrm{out}^2(n) - \mathrm{out}(n) - n$ and the seed is $S = \mathrm{out}(n) - n - W$.
Then $W = [abc]_T + 1$, $S = [ab]_T + c$, and the pre-seed $n - W - S$ equals $[a]_T + b$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 13 (`jis-2025-25.5.4-lem-13`).

Stated but not proved: `MetaMathlibExt.trithoff_precolumns` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#trithoff-precolumns).

## Wall, seed and pre-seed of the Trithoff array via the Tribonacci word

Let
$f_1 < f_2 < \cdots$ be the positive integers whose Tribonacci representation ends in $1$ (the
first column of the Trithoff array). For each row $r \ge 1$ let $\mathrm{out}(f_r)$ and
$\mathrm{out}^2(f_r)$ be the Tribonacci values of the Tribonacci representation of $f_r$,
written most significant digit first, followed by one and by two zeros, that is, with one and
with two new least significant digits $0$. Define, in the integers, the wall
$W_r = \mathrm{out}^2(f_r) - \mathrm{out}(f_r) - f_r$, the seed
$S_r = \mathrm{out}(f_r) - f_r - W_r$ and the pre-seed $P_r = f_r - W_r - S_r$. Count positions
in the infinite Tribonacci word from $1$. Then (i) for every $r \ge 1$, $W_r$ is the $r$-th
position holding $a$ or $b$; (ii) $S_1 = 0$, the seed is non-decreasing in $r$, it takes the
value $0$ exactly once, and it takes each value $m \ge 1$ exactly twice if position $m$ holds
$a$ and exactly once otherwise; and (iii) $P_1 = 0$, the pre-seed is non-decreasing in $r$, it
takes the value $0$ exactly twice, and it takes each value $m \ge 1$ exactly three times if
position $m$ holds $a$ or $b$ and exactly twice if it holds $c$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 14 (`jis-2025-25.5.4-thm-14`).

Stated but not proved: `MetaMathlibExt.trithoff_wall_seed_preseed` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#trithoff-wall-seed-preseed).

## Gaps in the first column of the Trithoff array

Let $f_1 < f_2 < \cdots$ be the positive
integers whose Tribonacci representation ends in the digit $1$ (OEIS A003265, the first column
of the Trithoff array). For every $j \ge 1$ the difference $f_{j+1} - f_j$ is $2$ or $3$, and
$f_{j+1} - f_j = 3$ exactly when $j = p_a(k) + p_b(k)$ for some $k \ge 1$, where $p_a(k)$ and
$p_b(k)$ are the positions, counted from $1$, of the $k$-th occurrences of the letters $a$ and
$b$ in the infinite Tribonacci word.

The paper identifies these sums $p_a(k) + p_b(k)$, that is A003144 + A003145, with A305373.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Proposition 11 (`jis-2025-25.5.4-prop-11`).

Stated but not proved: `MetaMathlibExt.trithoff_first_column_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#trithoff-first-column-sub).

## ExtraTribs

An extraTrib is a two-sided integer sequence
$S \colon \mathbb{Z} \to \mathbb{Z}$ that follows the Tribonacci rule
$S(n+3) = S(n+2) + S(n+1) + S(n)$ for every $n \in \mathbb{Z}$ and whose terms are eventually
positive: there is an integer $N$ with $S(n) > 0$ for all $n \ge N$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 4.

Formalized by `MetaMathlibExt.IsExtraTrib`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#is-extra-trib).

## The zero sequence is not an extraTrib

The constant sequence $n \mapsto 0$ on
$\mathbb{Z}$ is not an extraTrib.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 4.

Formalized by `MetaMathlibExt.not_isExtraTrib_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#not-is-extra-trib-zero).

## Difference-inverses of extraTribs

Let $S$ be an extraTrib. There is exactly one
sequence $Q \colon \mathbb{Z} \to \mathbb{Q}$ that follows the Tribonacci rule
$Q(n+3) = Q(n+2) + Q(n+1) + Q(n)$ for all $n \in \mathbb{Z}$ and satisfies
$Q(n+1) - Q(n) = S(n)$ for all $n \in \mathbb{Z}$. Moreover, there is an extraTrib $Q$ with
$Q(n+1) - Q(n) = S(n)$ for all $n \in \mathbb{Z}$ if and only if $S$ is not of Type EEOO
(parities repeating even, even, odd, odd), that is, there is no integer $k$ such that for
every $n \in \mathbb{Z}$, $S(n)$ is even exactly when $(n - k) \bmod 4$ is $0$ or $1$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 9 (`jis-2025-25.5.4-thm-9`).

Stated but not proved: `MetaMathlibExt.extraTrib_difference_inverse` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#extra-trib-difference-inverse).

## ExtraTribs cannot be inverted forever

Let $S$ be an extraTrib. There is no sequence
$S_0, S_1, S_2, \dots$ of functions $\mathbb{Z} \to \mathbb{Z}$ with $S_0 = S$ such that for
every $k \ge 0$ the function $S_{k+1}$ is an extraTrib and a difference-inverse of $S_k$, that
is, $S_{k+1}(n+1) - S_{k+1}(n) = S_k(n)$ for all $n \in \mathbb{Z}$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 10 (`jis-2025-25.5.4-thm-10`).

Stated but not proved: `MetaMathlibExt.extraTrib_not_infinitely_invertible` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#extra-trib-not-infinitely-invertible).

## Row numbers of divisible extraTribs

Let $S$ be an extraTrib and let $n$ be a natural
number dividing every term $S(k)$, $k \in \mathbb{Z}$. Let $f_0 < f_1 < f_2 < \dots$ be the
positive integers whose Tribonacci representation has least significant digit $1$ (the first
column of the Trithoff array), let $r$ be a natural number, and let $w$ be a Tribonacci
representation of $f_r$. For a digit list $v$ written least significant digit first, let
$[v]_T$ be its value in the Tribonacci base and $0^j v$ be $v$ preceded by $j$ zeros in the
least significant positions. If there is an integer $k_0$ with $S(k_0 + j) = [0^j w]_T$ for
every natural number $j$, that is, the tail $S(k_0), S(k_0 + 1), \dots$ is row $r + 1$ of the
Trithoff array, then $r + 1 \equiv 1 \pmod{n}$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 18 (`jis-2025-25.5.4-thm-18`).

Stated but not proved: `MetaMathlibExt.extraTrib_row_number_modEq_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#extra-trib-row-number-mod-eq-one).

## Signs of an extraTrib to the left

Let $S$ be an extraTrib. Then $S(k) < 0$ for some
integer $k$, and whenever $S(k) < 0$, for every integer $n$ with $n + 2 < k$ the three terms
$S(n)$, $S(n+1)$, $S(n+2)$ are neither all positive nor all negative.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 19 (`jis-2025-25.5.4-lem-19`).

Stated but not proved: `MetaMathlibExt.extraTrib_left_extension` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#extra-trib-left-extension).

## The reversal of an extraTrib is not an extraTrib

If $S : \mathbb{Z} \to \mathbb{Z}$
is an extraTrib, then the sequence $n \mapsto |S(-n)|$ is not an extraTrib.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 20 (`jis-2025-25.5.4-thm-20`).

Stated but not proved: `MetaMathlibExt.not_isExtraTrib_reversal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#not-is-extra-trib-reversal).

## Leftmost carrying

Let $w = w_0 w_1 \cdots w_{\ell-1}$ be a word of natural-number digits,
written most significant digit first with positions numbered from $0$, and let $k$ be the least
index with $k + 3 < \ell$ and $w_{k+1}, w_{k+2}, w_{k+3} > 0$. Leftmost carrying replaces the
block $w_k w_{k+1} w_{k+2} w_{k+3}$ by $(w_k + 1)(w_{k+1} - 1)(w_{k+2} - 1)(w_{k+3} - 1)$ and
leaves the other digits unchanged; it is undefined when there is no such $k$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciLeftmostCarry`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-leftmost-carry).

## Leftmost carrying of $0111$

Leftmost carrying takes the word $0111$, written most
significant digit first, to $1000$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 5.

Formalized by `MetaMathlibExt.tribonacciLeftmostCarry_zero_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-leftmost-carry-zero-one-one-o).

## Weight of an improper word

Let $w$ be a word of natural-number digits, written most
significant digit first, and let $v = 0w$ be $w$ padded with a $0$ on the left, with positions
numbered from $0$. Let $p$ be the position of the leftmost digit $\ge 2$ of $v$ (the improper
boundary), or the length of $v$ if there is no such digit. The weight of $w$ is the sum of the
digits of $v$ that come after the last $0$ of $v$ before position $p$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciImproperWeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-improper-weight).

## Weight of the improper word $010113$

The word $010113$, written most significant digit
first, has weight $1 + 1 + 3 = 5$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciImproperWeight_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-improper-weight-example).

## One step of Tribonacci canonization

Let $w$ be a word of natural-number digits, written
most significant digit first, and let $v = 0w$ be $w$ padded with a $0$ on the left, with
positions numbered from $0$. If leftmost carrying applies to $v$, the step returns its result
(Step 1). Otherwise let $p$ be the position of the leftmost digit $\ge 2$ of $v$ (the improper
boundary), or the length of $v$ if there is no such digit. If $v$ has no position $p + 3$, the
step is undefined. Otherwise, if $v_{p-1} = 0$, the step (Step 2a) sets $v_{p-1}$ to $1$,
decreases $v_p$ by $2$ and increases $v_{p+3}$ by $1$, as in $0abcd \mapsto 1(a-2)bc(d+1)$; if
$v_{p-1} \ne 0$, the step (Step 2b) sets $v_{p-2}$ to $1$ and $v_{p-1}$ to $0$, decreases $v_p$
by $2$ and increases $v_{p+2}$ and $v_{p+3}$ by $1$, as in
$01a0cd \mapsto 10(a-2)0(c+1)(d+1)$. All other digits of $v$ are unchanged.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciCanonizationStep`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-canonization-step).

## Canonization run

Words are written most significant digit first. The run of at most
$n$ canonization steps on a word $w$ of natural numbers is defined by recursion on $n$: it
returns $w$ if $n = 0$ or if $w$ is canonical (every digit is $0$ or $1$ and there are no
three consecutive $1$s); otherwise it applies one canonization step to $w$ and returns the
run of at most $n - 1$ steps on the result, and it is undefined when that step is undefined.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciCanonizationRun`, a definition declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-canonization-run).

## Canonizing $2000000$

Words are written most significant digit first. Running at most
two steps of the canonization procedure on the word $2000000$ yields $10001000$.

Both words have value $88$: with $T_n$ the Tribonacci numbers ($T_0 = T_1 = 0$, $T_2 = 1$)
and the digit in position $i$ from the right (starting at $0$) weighted by $T_{i+3}$, they
are $2 T_9 = 2 \cdot 44$ and $T_{10} + T_6 = 81 + 7$. A single Step 2a of the procedure
produces the result.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Section 6.1.

Formalized by `MetaMathlibExt.tribonacciCanonizationRun_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-canonization-run-example).

## Leftmost carrying does not move the improper boundary left or raise the weight

Let $w$ be
a word of natural-number digits, written most significant digit first, with some digit $\ge 2$.
Suppose leftmost carrying applied to the padded word $0w$ gives a word $u$ (of the same length as
$0w$) that still has a digit $\ge 2$. Then the position of the leftmost digit $\ge 2$ in $u$ is at
least its position in $0w$, and the weight of $u$ is at most the weight of $w$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Lemma 15 (`jis-2025-25.5.4-lem-15`).

Stated but not proved: `MetaMathlibExt.tribonacciLeftmostCarry_boundary_weight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-leftmost-carry-boundary-weigh).

## Termination of the canonization procedure

Words are written most significant digit
first. Let $w$ be a word of natural numbers with some digit at least $2$, let $m$ be its
improper weight, and let $k \ge 3m$. Then there is an $n$ such that running at most $n$ steps
of the canonization procedure on $w 0^k$ ($w$ followed by $k$ zeros) yields a word whose
digits are all $0$ or $1$ and which has no three consecutive $1$s.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Theorem 16 (`jis-2025-25.5.4-thm-16`).

Stated but not proved: `MetaMathlibExt.tribonacciCanonizationRun_terminates` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-canonization-run-terminates).

## Canonizing a word followed by zeros

Words are written most significant digit first.
Let $w$ be a word of natural numbers with some digit at least $2$, and suppose that running at
most $n$ steps of the canonization procedure on $w$ yields a word $v$ whose digits are all $0$
or $1$ and which has no three consecutive $1$s. Then for every $k$, running at most $n$ steps
of the canonization procedure on $w 0^k$ ($w$ followed by $k$ zeros) yields $v 0^k$.

## Sources

- E. Chen et al., *Generalizing the Wythoff Array and Other Fibonacci Facts to Tribonacci Numbers*, Journal of Integer Sequences 28 (2025), Article 25.5.4, Corollary 17 (`jis-2025-25.5.4-cor-17`).

Stated but not proved: `MetaMathlibExt.tribonacciCanonizationRun_append_zeros` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TribonacciWythoffWanted.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html#tribonacci-canonization-run-append-zeros).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tribonacci representations and the Trithoff array](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/tribonacci-representations-and-the-trithoff-arra)
