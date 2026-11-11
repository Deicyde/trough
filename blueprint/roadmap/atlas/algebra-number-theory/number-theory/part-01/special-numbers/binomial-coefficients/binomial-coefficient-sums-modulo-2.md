---
declaration: section
origin: cited
lean: MetaMathlibExt.bitRunLengths, MetaMathlibExt.binaryRunLengths, MetaMathlibExt.runLengthTransform, MetaMathlibExt.runLengthTransform_zero, MetaMathlibExt.runLengthTransform_eleven, MetaMathlibExt.linearRecurrence_eq_companion_pow, MetaMathlibExt.runLengthTransform_linearRecurrence_eq_linearRep, MetaMathlibExt.runLengthTransform_choose_sub_two_mul_fib
statement: formalized
---

# Binomial coefficient sums modulo 2

23 results, 5 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html).

## Run lengths of a digit list

Given a list $b_1, \dots, b_k$ of natural numbers (binary
digits) and a natural number $c$, this is the list, in order of occurrence, of the lengths of the
maximal runs of $1$s in the sequence consisting of $c$ ones followed by $b_1, \dots, b_k$, where
every digit other than $1$ ends a run.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Definition 1.

Formalized by `MetaMathlibExt.bitRunLengths`, a definition declared in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#bit-run-lengths).

## Binary run lengths

For a natural number $n$, the binary run lengths of $n$ form the list
of the lengths of the maximal runs of $1$s in the binary expansion of $n$, in the order in which
the runs occur when the digits are read from the least significant one. This is the paper's list
$\mathcal{L}(n)$, whose order does not matter there; for $n = 0$ the list is empty.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Definition 1.

Formalized by `MetaMathlibExt.binaryRunLengths`, a definition declared in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#binary-run-lengths).

## Run length transform

For a sequence $S : \mathbb{N} \to \mathbb{Z}$, the run length
transform of $S$ is the sequence $T : \mathbb{N} \to \mathbb{Z}$ given by
$T(n) = \prod_{\ell \in \mathcal{L}(n)} S(\ell)$, where $\mathcal{L}(n)$ is the list of the
lengths of the maximal runs of $1$s in the binary expansion of $n$, so that each run contributes
one factor.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Definition 1.

Formalized by `MetaMathlibExt.runLengthTransform`, a definition declared in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform).

## Run length transform at zero

For every sequence $S : \mathbb{N} \to \mathbb{Z}$, the run
length transform of $S$ takes the value $1$ at $0$, since $0$ has no runs of $1$s in binary.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Definition 1.

Formalized by `MetaMathlibExt.runLengthTransform_zero`, a theorem declared in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-zero).

## Run length transform at eleven

For every sequence $S : \mathbb{N} \to \mathbb{Z}$, the run
length transform $T$ of $S$ satisfies $T(11) = S(1) S(2)$: in binary $11$ is $1011$, whose maximal
runs of $1$s have lengths $2$ and $1$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, example after Definition 1.

Formalized by `MetaMathlibExt.runLengthTransform_eleven`, a theorem declared in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-eleven).

## Linear recurrences via powers of the companion matrix

Let $r$ be a natural number, let
$d_0, \dots, d_r$ be integers, and let $S : \mathbb{N} \to \mathbb{Z}$ satisfy $S(0) = 1$ and
$S(m + 1) = d_0 S(m) + d_1 S(m - 1) + \dots + d_r S(m - r)$ for every $m \ge r$. Let $\gamma(1)$
be the $(r + 1) \times (r + 1)$ integer matrix with rows and columns indexed by $0, \dots, r$
whose row $i < r$ has a $1$ in column $i + 1$ and zeros elsewhere, and whose last row is
$(d_r, d_{r-1}, \dots, d_0)$. With $v = (1, 0, \dots, 0)$ and $w = (S(0), \dots, S(r))^{T}$,
we have $S(n) = v \, \gamma(1)^n \, w$ for every natural number $n$.

The values $S(1), \dots, S(r)$ are arbitrary.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Lemma 1.

Stated but not proved: `MetaMathlibExt.linearRecurrence_eq_companion_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#linear-recurrence-eq-companion-pow).

## Run length transform of a linear recurrence (Rampersad–Wiebe Theorem 1)

Let $r \ge 0$, let
$d_0, \dots, d_r$ be integers, and let $S : \mathbb{N} \to \mathbb{Z}$ satisfy $S(0) = 1$ and
$S(m + 1) = d_0 S(m) + d_1 S(m - 1) + \dots + d_r S(m - r)$ for all $m \ge r$. Let $T$ be the run
length transform of $S$, let $v = (1, 0, \dots, 0)$ and $w = (S(0), \dots, S(r))^\top$, let
$\gamma(0)$ be the $(r + 1) \times (r + 1)$ matrix with first column $w$ and zeros elsewhere, and
let $\gamma(1)$ be the $(r + 1) \times (r + 1)$ companion matrix with ones on the superdiagonal,
last row $(d_r, \dots, d_0)$ and zeros elsewhere. Then for every natural number $n$ with binary
digits $b_1 b_2 \cdots b_t$, most significant first,
$T(n) = v \, \gamma(b_1) \gamma(b_2) \cdots \gamma(b_t) \, w$, where for $n = 0$ the product of
matrices is empty and equals the identity.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 1.

Stated but not proved: `MetaMathlibExt.runLengthTransform_linearRecurrence_eq_linearRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-linear-recurrence-e).

## Rampersad–Wiebe Theorem 2

Let $(F_j)_{j \ge 0}$ be the Fibonacci numbers, $F_0 = 0$,
$F_1 = 1$, and let $T$ be the run length transform of $S(i) = F_{i+1}$, i.e. of
$1, 1, 2, 3, 5, 8, \dots$. Then for every natural number $n$,
$\sum_{k=0}^{n} \left(\binom{n - k}{2k} \binom{n}{k} \bmod 2\right) = T(n)$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 2.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_sub_two_mul_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-sub-two-mul).

## Rampersad–Wiebe Theorem 3

Let $(F_j)_{j \ge 0}$ be the Fibonacci numbers, $F_0 = 0$,
$F_1 = 1$, and let $T$ be the run length transform of $S(i) = F_{i+2}$, i.e. of
$1, 2, 3, 5, 8, \dots$. Then for every natural number $n$,
$\sum_{k=0}^{n} \left(\binom{3k}{k} \binom{n}{k} \bmod 2\right) = T(n)$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 3.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_three_mul_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-three-mul-fi).

## Rampersad–Wiebe Theorem 4

Let $T$ be the run length transform of the sequence $S$ with
$S(0) = 1$ and $S(i) = 2^{i-1}$ for $i \ge 1$, i.e. of $1, 1, 2, 4, 8, \dots$. Then for every
natural number $n$, $\sum_{k=0}^{n} \left(\binom{n}{2k} \binom{n}{k} \bmod 2\right) = T(n)$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 4.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_two_mul_pow_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-two-mul-pow).

## Sum of $\binom{n+2k}{2k}\binom{n}{k} \bmod 2$ as a run length transform

For every
natural number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+2k}{2k}\binom{n}{k} \bmod 2\bigr)$
equals the value at $n$ of the run length transform of the sequence $S$ with $S(0) = 1$ and
$S(i) = 2$ for $i \ge 1$, that is, $1, 2, 2, 2, \dots$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 5.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_two_mul_one_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-two-mul).

## Sum of $\binom{n+k}{n-k}\binom{n}{k} \bmod 2$ as a run length transform

For every
natural number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+k}{n-k}\binom{n}{k} \bmod 2\bigr)$
equals the value at $n$ of the run length transform of the sequence $S(i) = i + 1$ of positive
integers $1, 2, 3, \dots$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 6.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_sub_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-sub-succ).

## Rampersad–Wiebe Theorem 7

Let $(N_j)_{j \ge 0}$ be Narayana's cows sequence, $N_0 = 0$,
$N_1 = N_2 = 1$ and $N_j = N_{j-1} + N_{j-3}$ for $j \ge 3$, and let $T$ be the run length
transform of $S(i) = N_{i+1}$, i.e. of $1, 1, 1, 2, 3, 4, 6, 9, \dots$. Then for every natural
number $n$, $\sum_{k=0}^{n} \left(\binom{n - k}{6k} \binom{n}{k} \bmod 2\right) = T(n)$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 7.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_sub_six_mul_narayanaCows` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-sub-six-mul).

## Sum of $\binom{n+3k}{6k}\binom{n}{k} \bmod 2$ as a run length transform

For every
natural number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+3k}{6k}\binom{n}{k} \bmod 2\bigr)$
equals the value at $n$ of the run length transform of the sequence
$S(i) = \lfloor i / 2 \rfloor + 1$ of doubled positive integers $1, 1, 2, 2, 3, 3, \dots$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 8.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_three_mul_six_mul_doubled` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-three-mu).

## Sum of $\binom{n+2k}{2n-k}\binom{n}{k} \bmod 2$ as a run length transform

For every
natural number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+2k}{2n-k}\binom{n}{k} \bmod 2\bigr)$
equals the value at $n$ of the run length transform of the sequence $S$ with $S(0) = S(1) = 1$
and $S(i) = L_{i-2}$ for $i \ge 2$, where $L_0 = 2, L_1 = 1, L_2 = 3, \dots$ are the Lucas
numbers; that is, $S$ is $1, 1, 2, 1, 3, 4, 7, 11, \dots$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 9.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_two_mul_two_mul_sub_lucas` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-two-mul-2).

## Rampersad–Wiebe Theorem 12

Let $(p_j)_{j \ge 0}$ be the shifted Padovan sequence,
$p_0 = 1$, $p_1 = 0$, $p_2 = 1$ and $p_{j+3} = p_{j+1} + p_j$, and let $T$ be the run length
transform of $S(i) = p_{i+2}$, i.e. of $1, 1, 1, 2, 2, 3, 4, 5, \dots$ (the Padovan numbers,
OEIS A000931, from offset $5$). Then for every natural number $n$,
$\sum_{k=0}^{n} \left(\binom{7k - n}{n + k} \binom{n}{k} \bmod 2\right) = T(n)$, where a binomial
coefficient $\binom{a}{b}$ with $a < 0$ is $0$.

Equivalently, a negative top entry $7k - n$ may be replaced by $0$, since the bottom entry $n + k$
is then positive.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 12.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_seven_mul_sub_padovan_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-seven-mul-su).

## Sum of $\binom{n+7k}{3n+k}\binom{n}{k} \bmod 2$ as a run length transform

For every
natural number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+7k}{3n+k}\binom{n}{k} \bmod 2\bigr)$
equals the value at $n$ of the run length transform of the shifted Padovan sequence $P$, given by
$P(0) = 1$, $P(1) = 0$, $P(2) = 1$ and $P(i + 3) = P(i + 1) + P(i)$, that is,
$1, 0, 1, 1, 1, 2, 2, 3, \dots$ (the Padovan numbers, OEIS A000931, from offset $3$).

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 13.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_seven_mul_padovan_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-seven-mu).

## Rampersad–Wiebe Theorem 14

Let $T$ be the run length transform of the sequence $S$ with
$S(i) = 1$ for even $i$ and $S(i) = (i + 1)/2$ for odd $i$, i.e. of $1, 1, 1, 2, 1, 3, 1, 4, \dots$.
Then for every natural number $n$,
$\sum_{k=0}^{n} \left(\binom{6k}{n + 3k} \binom{n}{k} \bmod 2\right) = T(n)$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 14.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_six_mul_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-six-mul-alte).

## Rampersad–Wiebe Theorem 15

Let $T$ be the run length transform of the periodic sequence
$S$ with $S(i) = 0$ if $i \equiv 2 \pmod 3$ and $S(i) = 1$ otherwise, i.e. of
$1, 1, 0, 1, 1, 0, \dots$. Then for every natural number $n$,
$\sum_{k=0}^{n} \left(\binom{8k - 2n}{n + k} \binom{n}{k} \bmod 2\right) = T(n)$, where a binomial
coefficient $\binom{a}{b}$ with $a < 0$ is $0$.

Equivalently, a negative top entry $8k - 2n$ may be replaced by $0$, since the bottom entry $n + k$
is then positive.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 15.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_eight_mul_sub_period_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-eight-mul-su).

## Sum of $\binom{n+5k}{2n+2k}\binom{n}{k} \bmod 2$ as a run length transform

Let
$S : \mathbb{N} \to \mathbb{Z}$ satisfy $S(0) = S(1) = S(2) = S(3) = 1$ and
$S(m) = S(m - 1) + S(m - 2) - S(m - 3) + S(m - 4)$ for every $m \ge 4$. Then for every natural
number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+5k}{2n+2k}\binom{n}{k} \bmod 2\bigr)$ equals
the value at $n$ of the run length transform of $S$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 10.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_five_mul_two_mul_add_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-five-mul).

## Sum of $\binom{n+5k}{2k}\binom{n}{k} \bmod 2$ as a run length transform

Let
$S : \mathbb{N} \to \mathbb{Z}$ satisfy $S(0) = 1$, $S(1) = S(2) = 2$, $S(3) = 3$ and
$S(m) = S(m - 1) + S(m - 2) - S(m - 3) + S(m - 4)$ for every $m \ge 4$. Then for every natural
number $n$, the sum $\sum_{k=0}^{n} \bigl(\binom{n+5k}{2k}\binom{n}{k} \bmod 2\bigr)$ equals the
value at $n$ of the run length transform of $S$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 11.

Stated but not proved: `MetaMathlibExt.runLengthTransform_choose_add_five_mul_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#run-length-transform-choose-add-five-mul-2).

## Binomial parity sums at one less than a power of two

For all natural numbers $m$ and
$\ell$, with $n = 2^\ell - 1$, the sum

$$\sum_{k=0}^{n} \left( \binom{2^m k}{n + k} \binom{n}{k} \bmod 2 \right)$$

equals $1$ if $m$ divides $\ell$, and $0$ otherwise.

The paper takes $m \ge 2$; the statement holds for every $m$, where $0$ divides $\ell$ only
when $\ell = 0$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Lemma 2.

Stated but not proved: `MetaMathlibExt.sum_choose_two_pow_mul_mod_two_two_pow_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#sum-choose-two-pow-mul-mod-two-two-pow-s).

## Binomial parity sums detect run length divisibility

For all natural numbers $m$ and $n$,
the sum

$$\sum_{k=0}^{n} \left( \binom{2^m k}{n + k} \binom{n}{k} \bmod 2 \right)$$

equals $1$ if every maximal run of $1$s in the binary expansion of $n$ has length divisible by
$m$, and $0$ otherwise.

The paper takes $m \ge 2$; the statement holds for every $m$.

## Sources

- Narad Rampersad and Max Wiebe, *Sums of Products of Binomial Coefficients Mod 2 and 2-Regular Sequences*, INTEGERS 24 (2024), Article A73, Theorem 16.

Stated but not proved: `MetaMathlibExt.sum_choose_two_pow_mul_mod_two_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomialModTwoRunLengthWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html#sum-choose-two-pow-mul-mod-two-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial coefficient sums modulo 2](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomial-coefficient-sums-modulo-2)
