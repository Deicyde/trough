---
declaration: section
origin: cited
lean: MetaMathlibExt.tribonacci, MetaMathlibExt.tribonacciWithInitialValues111, MetaMathlibExt.generalizedTribonacci, MetaMathlibExt.generalizedTribonacci_zero, MetaMathlibExt.generalizedTribonacci_one, MetaMathlibExt.generalizedTribonacci_two, MetaMathlibExt.generalizedTribonacci_add_three, MetaMathlibExt.generalizedTribonacci_zero_zero_one_eq_tribonacci
statement: formalized
proof: formalized
---

# Tribonacci numbers

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html).

## Tribonacci sequence

The Tribonacci sequence $(T_n)_{n \ge 0}$ is defined by $T_0 = 0$,
$T_1 = 0$, $T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for $n \ge 0$; it begins
$0, 0, 1, 1, 2, 4, \dots$ (OEIS A000073).

## Sources

- Jiaqiang Pan, *Multiple Binomial Transforms and Families of Integer Sequences*, Journal of Integer Sequences 13 (2010), <https://cs.uwaterloo.ca/journals/JIS/VOL13/Pan/pan8.tex>.

Formalized by `MetaMathlibExt.tribonacci`, a definition declared in [MathlibExt/NumberTheory/TribonacciSequenceWithInitialValues001.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciSequenceWithInitialValues001.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci).

## Tribonacci sequence with initial values 1, 1, 1

The sequence $(T_n)_{n \ge 0}$ of natural
numbers defined by $T_0 = T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for every
$n \ge 0$. It begins $1, 1, 1, 3, 5, 9, 17, \dots$ (OEIS A000213).

## Sources

- * Roman Zatorsky and Taras Goy, *Parapermanents of Triangular Matrices and Some General Theorems on Number Sequences*, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Goy/goy2.tex>. * Thomas Garrity, *A Multidimensional Continued Fraction Generalization of Stern's Diatomic Sequence*, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Garrity/garrity4.tex>.

Formalized by `MetaMathlibExt.tribonacciWithInitialValues111`, a definition declared in [MathlibExt/NumberTheory/TribonacciSequenceWithInitialValues111.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciSequenceWithInitialValues111.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-with-initial-values111).

## Generalized Tribonacci sequence

For integers $s_0, s_1, s_2$, the generalized Tribonacci
sequence $(T_n)_{n \ge 0}$ with initial values $s_0, s_1, s_2$ is the sequence of integers
defined by $T_0 = s_0$, $T_1 = s_1$, $T_2 = s_2$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
every $n \ge 0$.

## Sources

- Gessel–Kar (2024), JIS 27, Article 24.1.3, lines 700–719: `T_0 = s₀`, `T_1 = s₁`, `T_2 = s₂`, and `T_{n+3} = T_{n+2} + T_{n+1} + T_n`.

Formalized by `MetaMathlibExt.generalizedTribonacci`, a definition declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci).

## Initial value $T_0 = s_0$ of the generalized Tribonacci sequence

For all integers
$s_0, s_1, s_2$, the generalized Tribonacci sequence $(T_n)_{n \ge 0}$ with initial values
$s_0, s_1, s_2$ satisfies $T_0 = s_0$.

Formalized by `MetaMathlibExt.generalizedTribonacci_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-zero).

## Initial value $T_1 = s_1$ of the generalized Tribonacci sequence

For all integers
$s_0, s_1, s_2$, the generalized Tribonacci sequence $(T_n)_{n \ge 0}$ with initial values
$s_0, s_1, s_2$ satisfies $T_1 = s_1$.

Formalized by `MetaMathlibExt.generalizedTribonacci_one`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-one).

## Initial value $T_2 = s_2$ of the generalized Tribonacci sequence

For all integers
$s_0, s_1, s_2$, the generalized Tribonacci sequence $(T_n)_{n \ge 0}$ with initial values
$s_0, s_1, s_2$ satisfies $T_2 = s_2$.

Formalized by `MetaMathlibExt.generalizedTribonacci_two`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-two).

## Recurrence of the generalized Tribonacci sequence

For all integers $s_0, s_1, s_2$ and
every $n \ge 0$, the generalized Tribonacci sequence $(T_n)_{n \ge 0}$ with initial values
$s_0, s_1, s_2$ satisfies $T_{n+3} = T_{n+2} + T_{n+1} + T_n$.

Formalized by `MetaMathlibExt.generalizedTribonacci_add_three`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-add-three).

## The generalized Tribonacci sequence with initial values $0, 0, 1$ is the Tribonacci sequence

**The generalized Tribonacci sequence with initial values $0, 0, 1$ is the Tribonacci
sequence.** For every $n \ge 0$, the $n$-th term of the generalized Tribonacci sequence with
initial values $0, 0, 1$ equals the $n$-th Tribonacci number $t_n$ (where $t_0 = t_1 = 0$ and
$t_2 = 1$), viewed as an integer.

Formalized by `MetaMathlibExt.generalizedTribonacci_zero_zero_one_eq_tribonacci`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-zero-zero-one-eq).

## Integer and natural Tribonacci sequences with initial values $1, 1, 1$ agree

For every
$n \ge 0$, the $n$-th term of the generalized Tribonacci sequence with initial values $1, 1, 1$
equals the $n$-th term of the Tribonacci sequence of natural numbers with initial values
$1, 1, 1$, viewed as an integer.

Formalized by `MetaMathlibExt.generalizedTribonacci_one_one_one_eq_tribonacciWithInitialValues111`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-one-one-one-eq-tr).

## The generalized Tribonacci sequence with initial values $0, 1, 1$ is the shifted Tribonacci sequence

**The generalized Tribonacci sequence with initial values $0, 1, 1$ is the shifted Tribonacci
sequence.** For every $n \ge 0$, the $n$-th term of the generalized Tribonacci sequence with
initial values $0, 1, 1$ equals the Tribonacci number $t_{n+1}$, viewed as an integer, where
$t_0 = t_1 = 0$ and $t_2 = 1$.

The initial values $0, 1, 1$ are the usual Tribonacci convention used by Gessel–Kar; since the
Tribonacci sequence $t$ starts $0, 0, 1$, the index shift by one is needed.

Formalized by `MetaMathlibExt.generalizedTribonacci_zero_one_one_eq_tribonacci_succ`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedTribonacci.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedTribonacci.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#generalized-tribonacci-zero-one-one-eq-t).

## Backward half of the two-sided Tribonacci sequence

The integer sequence $(B_m)_{m \ge 0}$
is defined by $B_0 = 0$, $B_1 = 0$, $B_2 = 1$ and $B_{m+3} = B_m - B_{m+1} - B_{m+2}$ for
every $m \ge 0$.

Writing $B_m = T_{-m}$, the initial values are $T_0 = 0$, $T_{-1} = 0$, $T_{-2} = 1$, and the
recursion is the Tribonacci recurrence $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ solved for $T_n$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciBackward`, a definition declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-backward).

## Two-sided Tribonacci sequence

The integer sequence $(T_n)_{n \in \mathbb{Z}}$ is defined on
the nonnegative indices by $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$
for $n \ge 0$, and on the negative indices by $T_{-1} = 0$, $T_{-2} = 1$ and
$T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for $m \ge 0$, the recurrence solved for its lowest
term.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt`, a definition declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int).

## The two-sided Tribonacci sequence at $0$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_0 = 0$.

This is the first initial value used by Proposition 1.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_zero`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-zero).

## The two-sided Tribonacci sequence at $1$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_1 = 1$.

This is one of Proposition 1's five indices at which the value lies in $\{\pm 1\}$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_one`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-one).

## The two-sided Tribonacci sequence at $2$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_2 = 1$.

This is one of Proposition 1's five indices at which the value lies in $\{\pm 1\}$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_two`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-two).

## The two-sided Tribonacci sequence at $-1$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_{-1} = 0$.

This fixes the first value across the boundary between negative and nonnegative indices.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_neg_one`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-neg-one).

## The two-sided Tribonacci sequence at $-2$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_{-2} = 1$.

This is one of Proposition 1's five indices at which the value lies in $\{\pm 1\}$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_neg_two`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-neg-two).

## The two-sided Tribonacci sequence at $-3$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_{-3} = -1$.

This is one of Proposition 1's five indices at which the value lies in $\{\pm 1\}$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_neg_three`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-neg-three).

## The two-sided Tribonacci sequence at $-7$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for
$n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for
$m \ge 0$. Then $T_{-7} = 1$.

This is one of Proposition 1's five indices at which the value lies in $\{\pm 1\}$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_neg_seven`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-neg-seven).

## Tribonacci recurrence for the two-sided sequence

Let $(T_n)_{n \in \mathbb{Z}}$ be the
two-sided Tribonacci sequence: $T_0 = 0$, $T_1 = T_2 = 1$ and
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for $n \ge 0$, while $T_{-1} = 0$, $T_{-2} = 1$ and
$T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for $m \ge 0$. Then
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for every integer $n$, including the three indices
$n = -3, -2, -1$ at which the recurrence crosses zero.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Formalized by `MetaMathlibExt.tribonacciInt_add_three`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-add-three).

## On nonnegative indices the two-sided Tribonacci sequence is the shifted Tribonacci sequence

**On nonnegative indices the two-sided Tribonacci sequence is the shifted Tribonacci
sequence.** Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided Tribonacci sequence: $T_0 = 0$,
$T_1 = T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for $n \ge 0$, while $T_{-1} = 0$,
$T_{-2} = 1$ and $T_{-m-3} = T_{-m} - T_{-m-1} - T_{-m-2}$ for $m \ge 0$. Let $(t_n)_{n \ge 0}$
be the Tribonacci sequence with $t_0 = t_1 = 0$, $t_2 = 1$ and $t_{n+3} = t_{n+2} + t_{n+1} + t_n$.
Then $T_n = t_{n+1}$ for every natural number $n$.

This is the bridge between Proposition 1's normalization and Theorem 1's natural-indexed
sequence.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Theorem 1 and Proposition 1 notation.

Formalized by `MetaMathlibExt.tribonacciInt_nat_eq`, a theorem declared in [MathlibExt/NumberTheory/TribonacciInt.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TribonacciInt.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html#tribonacci-int-nat-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tribonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tribonacci-numbers)
