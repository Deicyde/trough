---
declaration: section
origin: cited
lean: MetaMathlibExt.oresme_convolution_self, MetaMathlibExt.fib_oresme_convolution, MetaMathlibExt.two_pow_pred_mul_fib_modEq_five, MetaMathlibExt.lucasNumber_oresme_convolution, MetaMathlibExt.two_pow_mul_lucasNumber_succ_modEq_five, MetaMathlibExt.pellNumber_oresme_convolution, MetaMathlibExt.two_pow_mul_pellNumber_combination_modEq, MetaMathlibExt.pellLucasSequence_oresme_convolution
statement: formalized
---

# Oresme numbers

13 results, 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html).

## Self-convolution of the Oresme numbers

Let $O_m = m/2^m$ denote the Oresme numbers. For
every natural number $n$, $\sum_{k=0}^{n} O_k O_{n-k} = \frac{(n+1) n (n-1)}{6 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 2.1.

Stated but not proved: `MetaMathlibExt.oresme_convolution_self` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#oresme-convolution-self).

## Fibonacci–Oresme convolution

Let $F_m$ denote the Fibonacci numbers, with $F_0 = 0$,
$F_1 = 1$ and $F_{m+2} = F_{m+1} + F_m$, and let $O_m = m/2^m$ denote the Oresme numbers. For
every natural number $n$,
$\sum_{k=0}^{n} F_k O_{n-k} = \frac{2}{5} F_{n+1} - \frac{2(n+1)}{5 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 4.1.

Stated but not proved: `MetaMathlibExt.fib_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#fib-oresme-convolution).

## Oresme–Fibonacci congruence modulo 5

Let $F_n$ denote the Fibonacci numbers, with
$F_0 = 0$ and $F_1 = 1$. For every natural number $n$, $2^{n-1} F_n \equiv n \pmod 5$, where at
$n = 0$ the exponent $n - 1$ is taken to be $0$ (both sides are then $0$).

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 4.2.

Stated but not proved: `MetaMathlibExt.two_pow_pred_mul_fib_modEq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-pred-mul-fib-mod-eq-five).

## Lucas–Oresme convolution

Let $L_m$ denote the Lucas numbers and let $O_m = m/2^m$
denote the Oresme numbers. For every natural number $n$,
$\sum_{k=0}^{n} L_k O_{n-k} = \frac{2}{5} L_{n+1} - \frac{2}{5 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 4.3.

Stated but not proved: `MetaMathlibExt.lucasNumber_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#lucas-number-oresme-convolution).

## Powers of two times Lucas numbers modulo 5

Let $L_m$ denote the Lucas numbers. For every
natural number $n$, $2^n L_{n+1} \equiv 1 \pmod{5}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 4.4.

Stated but not proved: `MetaMathlibExt.two_pow_mul_lucasNumber_succ_modEq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-mul-lucas-number-succ-mod-eq-fiv).

## Pell–Oresme convolution

Let $P_m$ denote the Pell numbers and let $O_m = m/2^m$ denote
the Oresme numbers. For every natural number $n$,
$\sum_{k=0}^{n} P_k O_{n-k} = \frac{2}{49}(5 P_{n+1} - 4 P_n) - \frac{2(7n + 5)}{49 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 5.2.

Stated but not proved: `MetaMathlibExt.pellNumber_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#pell-number-oresme-convolution).

## Oresme–Pell congruence modulo 49

For every natural number $n$, the Pell numbers $P_n$
satisfy $2^n (5 P_{n+1} - 4 P_n) \equiv 7n + 5 \pmod{49}$ as integers.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 5.3.

Stated but not proved: `MetaMathlibExt.two_pow_mul_pellNumber_combination_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-mul-pell-number-combination-mod).

## Pell–Lucas–Oresme convolution

Let $Q_m$ denote the Pell–Lucas numbers, with
$Q_0 = Q_1 = 1$ and $Q_{m+2} = 2Q_{m+1} + Q_m$, and let $O_m = m/2^m$ denote the Oresme numbers.
For every natural number $n$,
$\sum_{k=0}^{n} Q_k O_{n-k} = \frac{2}{49}(5 Q_{n+1} - 4 Q_n) + \frac{7n - 2}{49 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 5.4.

Stated but not proved: `MetaMathlibExt.pellLucasSequence_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#pell-lucas-sequence-oresme-convolution).

## Oresme–Pell–Lucas congruence modulo 49

Let $Q_n$ denote the Pell–Lucas numbers, with
$Q_0 = Q_1 = 1$. For every natural number $n$,
$2^{n+1} (5 Q_{n+1} - 4 Q_n) \equiv 2 - 7n \pmod{49}$ as integers.

The paper prints $2^{n+1}(5Q_{n+1} - 4Q_n) \equiv 2 - 7n \equiv 0$. Its proof (base values $2$ and
$44$ on both sides, inductive hypothesis $2^{n+1}(5Q_{n+1} - 4Q_n) - (2 - 7n) \equiv 0$)
establishes the single congruence above, while the second link $2 - 7n \equiv 0 \pmod{49}$ fails
at $n = 0$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 5.5.

Stated but not proved: `MetaMathlibExt.two_pow_succ_mul_pellLucasSequence_combination_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-succ-mul-pell-lucas-sequence-com).

## Jacobsthal–Oresme convolution

Let $J_m$ denote the Jacobsthal numbers, the terms of the
Lucas sequence $U(1, -2)$, and let $O_m = m/2^m$ denote the Oresme numbers. For every natural
number $n$,
$\sum_{k=0}^{n} J_k O_{n-k} = \frac{2}{9} J_{n+1} - \frac{2(n+1)}{9 \cdot 2^n}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 6.2.

Stated but not proved: `MetaMathlibExt.jacobsthal_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#jacobsthal-oresme-convolution).

## Powers of two times Jacobsthal numbers modulo 9

Let $J_m$ denote the Jacobsthal numbers,
the terms of the Lucas sequence $U(1, -2)$. For every natural number $n$,
$2^n J_{n+1} \equiv n + 1 \pmod{9}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 6.3.

Stated but not proved: `MetaMathlibExt.two_pow_mul_jacobsthal_succ_modEq_nine` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-mul-jacobsthal-succ-mod-eq-nine).

## Jacobsthal–Lucas–Oresme convolution

Let $j_m$ denote the Jacobsthal–Lucas numbers and
let $O_m = m/2^m$ denote the Oresme numbers. For every natural number $n$,
$\sum_{k=0}^{n} j_k O_{n-k} = \frac{2}{9} j_{n+1} - \frac{2}{9 \cdot 2^n}$.

The paper prints $+$ where the equality sign belongs, with no relation between the two sides;
this is the equality reading, which matches Propositions 4.3 and 6.2 and Corollary 6.5.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Proposition 6.4.

Stated but not proved: `MetaMathlibExt.jacobsthalLucasNumber_oresme_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#jacobsthal-lucas-number-oresme-convoluti).

## Powers of two times Jacobsthal–Lucas numbers modulo 9

Let $j_m$ denote the
Jacobsthal–Lucas numbers. For every natural number $n$, $2^n j_{n+1} \equiv 1 \pmod{9}$.

## Sources

- Michael R. Bacon and Charles K. Cook, *Some Properties of Oresme Numbers and Convolutions with Various Second Order Sequences*, The Fibonacci Quarterly 62 (2024), no. 3, Article cookbacon061124, Corollary 6.5.

Stated but not proved: `MetaMathlibExt.two_pow_mul_jacobsthalLucasNumber_succ_modEq_nine` is written with `theorem_wanted` in [WantedExt/NumberTheory/OresmeConvolutionsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OresmeConvolutionsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html#two-pow-mul-jacobsthal-lucas-number-succ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Oresme numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/oresme-numbers)
