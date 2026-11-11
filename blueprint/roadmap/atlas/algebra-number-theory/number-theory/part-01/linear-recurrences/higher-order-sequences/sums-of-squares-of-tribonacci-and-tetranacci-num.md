---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.four_mul_sum_tribonacci_mul_sub_two, MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.four_mul_sum_tribonacci_sq, MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.three_mul_sum_tetranacci_mul_sub_two_add_sub_three, MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.three_mul_sum_tetranacci_sq
statement: formalized
---

# Sums of squares of Tribonacci and Tetranacci numbers

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html).

## Sum of products of Tribonacci terms two apart

Let $T \colon \mathbb{Z} \to \mathbb{Z}$
satisfy $T(m+3) = T(m+2) + T(m+1) + T(m)$ for every integer $m$. Then for every
natural number $n$,

$$4 \sum_{k=1}^{n} T(k)\,T(k-2) = \bigl(T(n+1) - T(n-1)\bigr)^2 - \bigl(T(1) - T(-1)\bigr)^2.$$

## Sources

- Karol Gryszka, "A Simple Proof of the Formula for the Sum of Tribonacci and Tetranacci Numbers Squared", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.four_mul_sum_tribonacci_mul_sub_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html#four-mul-sum-tribonacci-mul-sub-two).

## Sum of squares of a Tribonacci sequence

Let $T \colon \mathbb{Z} \to \mathbb{Z}$ satisfy
$T(m+3) = T(m+2) + T(m+1) + T(m)$ for every integer $m$. Then for every natural number $n$,

$$4 \sum_{k=1}^{n} T(k)^2 = 4\,T(n)\,T(n+1) - 4\,T(0)\,T(1) -
\bigl(T(n+1) - T(n-1)\bigr)^2 + \bigl(T(1) - T(-1)\bigr)^2.$$

## Sources

- Karol Gryszka, "A Simple Proof of the Formula for the Sum of Tribonacci and Tetranacci Numbers Squared", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.four_mul_sum_tribonacci_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html#four-mul-sum-tribonacci-sq).

## Sum of products of Tetranacci terms two and three apart

Let
$Q \colon \mathbb{Z} \to \mathbb{Z}$ satisfy $Q(m+4) = Q(m+3) + Q(m+2) + Q(m+1) + Q(m)$ for every
integer $m$. Then for every natural number $n$,

$$3 \sum_{k=1}^{n} Q(k)\bigl(Q(k-2) + Q(k-3)\bigr) = \bigl(Q(n+1) - Q(n-1)\bigr)^2 -
\bigl(Q(1) - Q(-1)\bigr)^2 - Q(n-2)\bigl(Q(n) + Q(n-3)\bigr) + Q(-2)\bigl(Q(0) + Q(-3)\bigr).$$

The boundary terms contain $Q(n) + Q(n-3)$ and $Q(0) + Q(-3)$, with the sign given by the
paper's telescoping calculation.

## Sources

- Karol Gryszka, "A Simple Proof of the Formula for the Sum of Tribonacci and Tetranacci Numbers Squared", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.three_mul_sum_tetranacci_mul_sub_two_add_sub_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html#three-mul-sum-tetranacci-mul-sub-two-add).

## Sum of squares of a Tetranacci sequence

Let $Q \colon \mathbb{Z} \to \mathbb{Z}$ satisfy
$Q(m+4) = Q(m+3) + Q(m+2) + Q(m+1) + Q(m)$ for every integer $m$. Then for every natural
number $n$,

$$3 \sum_{k=1}^{n} Q(k)^2 = 3\,Q(n)\,Q(n+1) - 3\,Q(0)\,Q(1) - \bigl(Q(n+1) - Q(n-1)\bigr)^2 +
\bigl(Q(1) - Q(-1)\bigr)^2 + Q(n-2)\bigl(Q(n) + Q(n-3)\bigr) - Q(-2)\bigl(Q(0) + Q(-3)\bigr).$$

Inside the boundary terms the sums $Q(n) + Q(n-3)$ and $Q(0) + Q(-3)$ carry a plus sign, as in
Gryszka's Lemma 2; this sign is the one forced by the paper's telescoping calculation.

## Sources

- Karol Gryszka, "A Simple Proof of the Formula for the Sum of Tribonacci and Tetranacci Numbers Squared", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.TribonacciTetranacciSumsOfSquaresWanted.three_mul_sum_tetranacci_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/TribonacciTetranacciSumsOfSquaresWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html#three-mul-sum-tetranacci-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of squares of Tribonacci and Tetranacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/sums-of-squares-of-tribonacci-and-tetranacci-num)
