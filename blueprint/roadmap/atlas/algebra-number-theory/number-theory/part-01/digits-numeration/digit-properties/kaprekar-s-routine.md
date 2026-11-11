---
declaration: section
origin: cited
lean: MetaMathlibExt.four_digit_kaprekar_structural_classification, MetaMathlibExt.kaprekarDiff, MetaMathlibExt.kaprekarMap, MetaMathlibExt.kaprekarMap_four_6174, MetaMathlibExt.kaprekarMap_three_495, MetaMathlibExt.kaprekarMap_four_495, MetaMathlibExt.kaprekarMap_fixed_iff, MetaMathlibExt.kaprekarFourDigitStep
statement: formalized
---

# Kaprekar's routine

22 results, 13 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html).

## Structure of four-digit Kaprekar dynamics in odd bases

Let $B > 3$ be an odd integer.
For a pair of natural numbers $d = (d_1, d_2)$, let $K(d) = (a - e, b - c)$, where
$a \ge b \ge c \ge e$ are the four numbers $d_1 - 1, B - 1, B - 1, B - d_1$ if $d_2 = 0$, and
$d_1, d_2 - 1, B - d_2 - 1, B - d_1$ if $d_2 \ne 0$, sorted in decreasing order (subtraction is
truncated at $0$). Let $X_B$ be the set of pairs with $1 \le d_1 < B$ and $d_2 \le d_1$, and let
$T_B$ be the set of pairs in $X_B$ with $0 < d_2 < d_1$ and $d_1$, $d_2$ both odd. Let
$\mathcal{P}$ be the set of two-element sets $S$ of subsets of $\mathbb{Z}/B\mathbb{Z}$ such that
every $C \in S$ has the form $\{x, -x\}$ with $x \ne 0$. For a set $S$ of subsets of
$\mathbb{Z}/B\mathbb{Z}$ let $2S = \{2C : C \in S\}$, where $2C = \{2y : y \in C\}$, and for
$d \in T_B$ let $\Phi(d) = \{\{u, -u\}, \{v, -v\}\}$, where $u$ and $v$ are the residues of
$(d_1 + d_2)/2$ and $(d_1 - d_2)/2$ modulo $B$. Then $K$ maps $T_B$ into itself, the third
iterate $K^3$ maps $X_B$ into $T_B$, $S \mapsto 2S$ maps $\mathcal{P}$ into itself, $\Phi$ is a
bijection from $T_B$ onto $\mathcal{P}$, and $\Phi(K(d)) = 2\,\Phi(d)$ for every $d \in T_B$.

Here a pair $(d_1, d_2) \in X_B$ stands for the four-digit base-$B$ numbers whose digits, sorted
as $a \ge b \ge c \ge e$, satisfy $a - e = d_1$ and $b - c = d_2$; the four numbers listed above
are the base-$B$ digits of their Kaprekar image, so $K$ is the Kaprekar map on these pairs.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, "Four-Digit Kaprekar Dynamics in Odd Bases", Journal of Integer Sequences 29 (2026), Article 26.4.7, Theorem `thm:structural`, lines 220-230, <https://cs.uwaterloo.ca/journals/JIS/VOL29/Ono/ono3.tex>.

Formalized by `MetaMathlibExt.four_digit_kaprekar_structural_classification`, a theorem declared in [MathlibExt/NumberTheory/Digits/KaprekarStructuralClassification.lean, line 1070](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Digits/KaprekarStructuralClassification.lean#L1070). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#four-digit-kaprekar-structural-classific).

## Kaprekar difference

Let $l$ be a list of $k$ natural numbers and let
$a_0 \le a_1 \le \dots \le a_{k-1}$ be its entries in increasing order. The Kaprekar difference of
$l$ is $\alpha_M - \alpha_L$, where $\alpha_M = \sum_{i\lt k} a_i 10^i$ and
$\alpha_L = \sum_{i\lt k} a_{k-1-i} 10^i$. When the entries are decimal digits, $\alpha_M$ is the
number written with the digits of $l$ in descending order and $\alpha_L$ is the number written
with them in ascending order (leading zeros allowed).

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Definition 1.1.

Formalized by `MetaMathlibExt.kaprekarDiff`, a definition declared in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-diff).

## Kaprekar map

For natural numbers $n$ and $\alpha$, take the decimal digits of $\alpha$
(without leading zeros, and no digits at all for $\alpha = 0$) and, if there are fewer than $n$
of them, pad them with leading zeros to a string of exactly $n$ digits. The Kaprekar map sends
$\alpha$ to the Kaprekar difference $\alpha_M - \alpha_L$ of this digit string: the number with
these digits in descending order minus the number with them in ascending order. For
$\alpha < 10^n$ this is the Kaprekar transformation on the set $D_n$ of $n$-digit strings; for
$\alpha \ge 10^n$ nothing is padded and all digits of $\alpha$ are used.

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Definition 1.1.

Formalized by `MetaMathlibExt.kaprekarMap`, a definition declared in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-map).

## 6174 is fixed by the four-digit Kaprekar map

The Kaprekar map with $n = 4$ sends $6174$
to itself: $7641 - 1467 = 6174$.

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Section 1.

Formalized by `MetaMathlibExt.kaprekarMap_four_6174`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-map-four-6174).

## 495 is fixed by the three-digit Kaprekar map

The Kaprekar map with $n = 3$ sends $495$ to
itself: $954 - 459 = 495$.

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Section 1.

Formalized by `MetaMathlibExt.kaprekarMap_three_495`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-map-three-495).

## The four-digit Kaprekar map sends 495 to 9081

With $n = 4$, the number $495$ is padded to
the digit string $0495$, and the Kaprekar map sends it to $9540 - 0459 = 9081$.

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Definition 1.1.

Formalized by `MetaMathlibExt.kaprekarMap_four_495`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-map-four-495).

## Classification of decimal Kaprekar numbers

Let $n \ge 3$ and $0 < \alpha < 10^n$. Then
the Kaprekar map on $n$-digit strings fixes $\alpha$ if and only if $\alpha$ is the Kaprekar
difference of some string $s$ of exactly $n$ decimal digits of one of the following five forms,
where juxtaposition is concatenation, $(w)^k$ is the block $w$ repeated $k$ times, and in each
form the exponents are chosen independently with $x, x_1, x_2 \ge 1$ and $y, y_1, y_2 \ge 0$:
$(495)^x$; $6174\,(36)^y$; $(123456789)^x (36)^y$;
$(123456789)^{x_1} (36)^{x_2} (495)^{2x_2} (27)^{3x_2}$;
$(124578)^{x_1} (09)^{x_2} (123456789)^{y_1} (36)^{y_2}$.

The witness string must have length $n$: $495$ is the Kaprekar difference of $(495)^1$, but the
Kaprekar map on $4$-digit strings sends $495$ to $9081$.

## Sources

- Haruo Iwasaki, *A New Classification of the Kaprekar Numbers*, The Fibonacci Quarterly 62 (2024), Article iwasaki06162024-ASrev2, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.kaprekarMap_fixed_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarClassificationWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-map-fixed-iff).

## The four-digit Kaprekar map in difference coordinates

For a base $B$ and a pair of
natural numbers $(d_1, d_2)$, the map $K_B$ forms the list of four digits
$[d_1 - 1, B - 1, B - 1, B - d_1]$ if $d_2 = 0$ and $[d_1, d_2 - 1, B - d_2 - 1, B - d_1]$ if
$d_2 > 0$, sorts it decreasingly as $a_1 \ge a_2 \ge a_3 \ge a_4$, and sets
$K_B(d_1, d_2) = (a_1 - a_4, a_2 - a_3)$. Subtraction of natural numbers is truncated at $0$;
for $1 \le d_1 < B$ and $0 \le d_2 \le d_1$ no truncation occurs.

For such $(d_1, d_2)$ the list holds the digits of the Kaprekar difference (largest minus
smallest arrangement) of any four-digit base-$B$ string with difference coordinates
$(d_1, d_2)$, as in paper displays (5) and (6).

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Section 2.1.

Formalized by `MetaMathlibExt.kaprekarFourDigitStep`, a definition declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-four-digit-step).

## Sample values of the four-digit Kaprekar map

The four-digit Kaprekar map satisfies
$K_{11}(5, 1) = (9, 1)$, $K_{11}(6, 0) = (5, 5)$ and $K_{11}(5, 5) = (2, 0)$ in base $11$, and
$K_7(3, 1) = (5, 1)$, $K_7(5, 1) = (5, 3)$ and $K_7(5, 3) = (3, 1)$ in base $7$.

In particular $(3, 1) \mapsto (5, 1) \mapsto (5, 3) \mapsto (3, 1)$ is a terminal cycle of $K_7$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Examples 7, 12 and 18.

Formalized by `MetaMathlibExt.kaprekarFourDigitStep_examples`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-four-digit-step-examples).

## The four-digit Kaprekar state space

For a base $B$, the state space $X_B$ is the finite
set of pairs of natural numbers $(d_1, d_2)$ with $1 \le d_1 < B$ and $0 \le d_2 \le d_1$.

A nonconstant four-digit base-$B$ string with sorted digits $a_1 \ge a_2 \ge a_3 \ge a_4$ has
difference coordinates $(d_1, d_2) = (a_1 - a_4, a_2 - a_3)$, a point of $X_B$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, display (2).

Formalized by `MetaMathlibExt.kaprekarFourDigitStates`, a definition declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-four-digit-states).

## Sizes of the Kaprekar state spaces in bases 3 and 7

The four-digit Kaprekar state spaces
satisfy $|X_3| = 5$ and $|X_7| = 27$.

Both values agree with the general count $|X_B| = (B - 1)(B + 2)/2$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, display (2) and the proof of Corollary 27.

Formalized by `MetaMathlibExt.kaprekarFourDigitStates_card_examples`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-four-digit-states-card-examples).

## Projective order of 2

For a natural number $n$, the projective order of $2$ modulo $n$ is
the least $m > 0$ with $2^m \equiv 1$ or $2^m \equiv -1 \pmod{n}$,

$$\lambda(n) = \min \{m > 0 : 2^m \equiv \pm 1 \pmod{n}\},$$

and $\lambda(n) = 0$ when no such $m$ exists, which happens exactly when $n$ is even (including
$n = 0$, where congruence modulo $0$ is equality of integers). For odd $n$ these are the terms of
OEIS A003558, which lists $\lambda(2k + 1)$ at index $k$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Definition 19, display (13).

Formalized by `MetaMathlibExt.projectiveOrderTwo`, a definition declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#projective-order-two).

## Characterization of the projective order of 2

Let $n$ and $m$ be natural numbers with
$m > 0$. Suppose that $2^m \equiv 1$ or $2^m \equiv -1 \pmod{n}$, and that for every $k$ with
$0 < k < m$ neither $2^k \equiv 1$ nor $2^k \equiv -1 \pmod{n}$. Then the projective order of $2$
modulo $n$ is $\lambda(n) = m$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Definition 19, display (13).

Formalized by `MetaMathlibExt.projectiveOrderTwo_eq_of`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#projective-order-two-eq-of).

## Values of the projective order of 2

Writing $\lambda(n)$ for the projective order of $2$
modulo $n$, we have $\lambda(7) = 3$, $\lambda(9) = 3$, $\lambda(11) = 5$ and $\lambda(17) = 4$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Examples 7-10 and 23.

Formalized by `MetaMathlibExt.projectiveOrderTwo_examples`, a theorem declared in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#projective-order-two-examples).

## Cycle lengths of doubling on pairs of projective classes

Let $B > 3$ be odd. For
$x \in \mathbb{Z}/B\mathbb{Z}$ write $[x] = \{x, -x\}$ and $2C = \{2c : c \in C\}$ for a subset
$C$ of $\mathbb{Z}/B\mathbb{Z}$, and let $D$ be the doubling map sending a set $T$ of subsets of
$\mathbb{Z}/B\mathbb{Z}$ to $\{2C : C \in T\}$. If $S = \{[r], [s]\}$ for nonzero
$r, s \in \mathbb{Z}/B\mathbb{Z}$ with $[r] \ne [s]$, then $S$ is a periodic point of $D$ and
its minimal period is at most $\lambda(B)$, the projective order of $2$ modulo $B$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Lemma 20 (`jis-2026-26.4.7-lem-20`).

Stated but not proved: `MetaMathlibExt.projective_doubling_minimalPeriod_le_projectiveOrderTwo` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#projective-doubling-minimal-period-le-pr).

## Projective order of 2 is at most half the totient

For every odd natural number $B > 3$,
the projective order of $2$ modulo $B$ satisfies $\lambda(B) \le \lfloor \varphi(B)/2 \rfloor$,
where $\varphi$ is Euler's totient function.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Lemma 21 (quoting Kay and Downes-Ward, Theorem 2) (`jis-2026-26.4.7-lem-21`).

Stated but not proved: `MetaMathlibExt.projectiveOrderTwo_le_totient_div_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#projective-order-two-le-totient-div-two).

## Long Kaprekar cycles force a prime base

Let $B > 3$ be odd, let $K_B$ be the four-digit
Kaprekar map and $X_B$ its state space. Every point of $X_B$ that is periodic for $K_B$ has
minimal period at most $(B - 1)/2$, and if some point of $X_B$ has minimal period exactly
$(B - 1)/2$ under $K_B$, then $B$ is prime.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Corollary 22 (`jis-2026-26.4.7-cor-22`).

Stated but not proved: `MetaMathlibExt.kaprekar_minimalPeriod_le_and_prime_of_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-minimal-period-le-and-prime-of).

## Maximal Kaprekar cycle length in odd bases

Let $B > 3$ be odd, let $K_B$ be the
four-digit Kaprekar map and $X_B$ its state space, and let $\lambda(B)$ be the projective order
of $2$ modulo $B$. Every point of $X_B$ that is periodic for $K_B$ has minimal period at most
$(B - 1)/2$. Moreover, some point of $X_B$ has minimal period exactly $(B - 1)/2$ under $K_B$
if and only if $B \ge 7$, $B$ is prime and $\lambda(B) = (B - 1)/2$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Corollary 3 (`jis-2026-26.4.7-cor-3`).

Stated but not proved: `MetaMathlibExt.kaprekar_minimalPeriod_le_and_eq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-minimal-period-le-and-eq-iff).

## Number of Kaprekar cycles of maximal length

Let $B > 3$ be odd, let $K_B$ be the
four-digit Kaprekar map and $X_B$ its state space, and put $q = (B - 1)/2$. If some point of
$X_B$ has minimal period $q$ under $K_B$, then exactly $q \lfloor (q - 1)/2 \rfloor$ points of
$X_B$ have minimal period $q$ under $K_B$.

Equivalently, $K_B$ then has exactly $\lfloor (q - 1)/2 \rfloor$ terminal cycles of length $q$
on $X_B$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Corollary 5 (`jis-2026-26.4.7-cor-5`).

Stated but not proved: `MetaMathlibExt.kaprekar_card_maximal_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-card-maximal-cycles).

## Explicit count of Kaprekar cycles of each length

Let $B > 3$ be odd and $L \ge 1$, let
$K_B$ be the four-digit Kaprekar map and $X_B$ its state space, let $\varphi$ be Euler's totient
function, and let $\lambda(n)$ denote the projective order of $2$ modulo $n$. For $a \ge 1$ put

$$\mu_B(a) = \sum_{n \mid B,\ n > 1,\ \lambda(n) = a}
\left\lfloor \frac{\varphi(n)}{2a} \right\rfloor$$

and

$$N_B(L) = \mu_B(L) \left\lfloor \frac{L - 1}{2} \right\rfloor + \mu_B(2L) +
\binom{\mu_B(L)}{2} L + \sum_{a, b \mid L,\ a < b,\ \operatorname{lcm}(a, b) = L}
\mu_B(a)\, \mu_B(b) \gcd(a, b),$$

where $n$ ranges over positive divisors of $B$ and $a, b$ in the last sum range over positive
divisors of $L$. Then exactly $L \cdot N_B(L)$ points of $X_B$ have minimal period $L$ under
$K_B$.

Here $N_B(L)$ is the number of terminal cycles of length $L$ of $K_B$ on $X_B$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Theorem 24, with `μ_B` from display (14) (`jis-2026-26.4.7-thm-24`).

Stated but not proved: `MetaMathlibExt.kaprekar_card_minimalPeriod_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-card-minimal-period-eq).

## At least two Kaprekar cycles whose length is the projective order of 2

Let $\lambda(B)$
denote the projective order of $2$ modulo $B$. For every odd base $B > 17$, at least $2\lambda(B)$
points of the state space $X_B$ have minimal period exactly $\lambda(B)$ under the four-digit
Kaprekar map $K_B$.

Each terminal cycle of $K_B$ of length $\lambda(B)$ consists of $\lambda(B)$ such points, so this
says that $K_B$ has at least two terminal cycles of length $\lambda(B)$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Corollary 27 (i) (`jis-2026-26.4.7-cor-27`).

Stated but not proved: `MetaMathlibExt.two_mul_projectiveOrderTwo_le_card_kaprekar_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#two-mul-projective-order-two-le-card-kap).

## Odd bases with a unique Kaprekar cycle

Let $B \ge 3$ be odd, let $K_B$ be the
four-digit Kaprekar map and $X_B$ its state space. There is a point $c \in X_B$, periodic for
$K_B$, whose forward orbit $\{K_B^k(c) : k \ge 0\}$ contains every point of $X_B$ that is
periodic for $K_B$, if and only if $B \in \{3, 5, 7\}$.

That is, $K_B$ has a unique terminal cycle on $X_B$ exactly when $B$ is $3$, $5$ or $7$.

## Sources

- Evan Chen, Ken Ono, Richard E. Schwartz, and Dinesh Thakur, *Four-Digit Kaprekar Dynamics in Odd Bases*, Journal of Integer Sequences 29 (2026), Article 26.4.7, Corollary 27 (ii) (`jis-2026-26.4.7-cor-27`).

Stated but not proved: `MetaMathlibExt.kaprekar_unique_cycle_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/KaprekarOddBasesWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html#kaprekar-unique-cycle-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kaprekar's routine](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/kaprekar-s-routine)
