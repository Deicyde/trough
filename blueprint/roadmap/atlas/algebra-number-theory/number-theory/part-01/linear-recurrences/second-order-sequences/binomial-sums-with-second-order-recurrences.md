---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasU_lucasV_sum_choose_sq_alternating, MetaMathlibExt.lucasU_lucasV_sum_choose_cube_alternating, MetaMathlibExt.lucasU_lucasV_sum_choose_sq, MetaMathlibExt.lucasU_lucasV_sum_catalan_even, MetaMathlibExt.lucasU_lucasV_sum_catalan_shifted, MetaMathlibExt.lucasU_lucasV_sum_choose_two_n, MetaMathlibExt.lucasU_lucasV_sum_choose_four_n_even_alternating, MetaMathlibExt.lucasU_lucasV_sum_choose_triple_alternating
statement: formalized
---

# Binomial sums with second-order recurrences

16 results, 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html).

## Alternating squared-binomial sum with Lucas sequences

Let $p$ be an integer and let
$U_n$ and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$,
$V_0 = 2$, $V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every natural
number $n$,

$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^2 U_{2n-k} V_k = (-1)^n \binom{2n}{n} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_sq_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-sq-alternatin).

## Dixon-type alternating sum with Lucas sequences

Let $p$ be an integer and let $U_n$ and
$V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every natural number $n$,

$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3 U_{2n-k} V_k = (-1)^n \binom{3n}{n} \binom{2n}{n} U_{2n},$$

where $\binom{3n}{n} \binom{2n}{n} = (3n)!/(n!)^3$ is the trinomial coefficient.

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_cube_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-cube-alternat).

## Squared-binomial convolution of the Lucas sequences U and V

Let $p$ be an integer and let
$U$ and $V$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so that $U_0 = 0$, $U_1 = 1$,
$V_0 = 2$, $V_1 = p$, and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every natural
number $n$

$$\sum_{k=0}^{n} \binom{n}{k}^2 U_{n-k} V_k = \binom{2n}{n} U_n.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.3.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-sq).

## Even-index Catalan convolution with Lucas sequences

Let $p$ be an integer, let $U_n$
and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$, and let $C_j$ be the $j$-th Catalan
number. Then for every natural number $n$, in the rationals,

$$\sum_{k=0}^{n} C_{2n-2k} C_{2k} U_k V_{n-k} =
\frac{2^{2n}}{2} \cdot \frac{n+2}{2n+1} C_{n+1} U_n.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.4.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_catalan_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-catalan-even).

## Shifted Catalan convolution with Lucas sequences

Let $p$ be an integer, let $U_n$ and
$V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$, and let $C_j$ be the $j$-th Catalan
number. Then for all natural numbers $n$ and $m$ with $m \ge 1$, in the rationals,

$$\sum_{k=0}^{n} C_{n-k+m} C_{k+m} U_k V_{n-k} =
2 \binom{2m-1}{m} \frac{(n+m+2)(n+1)}{(n+2m+1)(n+2m+2)} C_{n+m+1} U_n.$$

The paper states $m \in \mathbb{N}_0$; at $m = 0$ the printed right side is twice the sum
($p = 1$, $n = 1$: the sum is $2$, the printed right side is $4$), so $m = 0$ is excluded.

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.5.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_catalan_shifted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-catalan-shifted).

## Convolution of U and V with shifted binomial weights

Let $p$ be an integer and let $U$ and
$V$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so that $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$, and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every natural number $n$

$$\sum_{k=0}^{n} \binom{2n}{k} \binom{2n}{n+k} U_k V_{n-k} = \binom{4n}{n} U_n.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.6.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_two_n` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-two-n).

## Alternating sum of $\binom{2n}{k} \binom{4n}{2k}$ with Lucas sequences

Let $p$ be an
integer and let $U_n$ and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$,
$U_1 = 1$, $V_0 = 2$, $V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every
natural number $n$, in the rationals,

$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k} \binom{4n}{2k} U_k V_{2n-k} =
(-1)^n \frac{\binom{6n}{2n} \binom{2n}{n}}{\binom{3n}{n}} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.7.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_four_n_even_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-four-n-even-a).

## Alternating triple-binomial convolution of U and V

Let $p$ be an integer and let $U$ and
$V$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so that $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$, and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every natural number $n$

$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k} \binom{4n}{k} \binom{4n}{2n+k} U_k V_{2n-k} =
(-1)^n \binom{2n}{n} \binom{5n}{2n} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.8.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_triple_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-triple-altern).

## Alternating sum with reciprocal binomial coefficients and Lucas sequences

Let $p$ be an
integer and let $U_n$ and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$,
$U_1 = 1$, $V_0 = 2$, $V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every
natural number $n$, in the rationals,

$$\sum_{k=0}^{2n} (-1)^k \frac{\binom{2n}{k}}{\binom{4n}{k} \binom{4n}{2n+k}} U_k V_{2n-k} =
\frac{4n+1}{3n+1} \cdot \frac{1}{\binom{4n}{2n}} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.9.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_inv_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-inv-alternati).

## Sum of $\binom{n}{k} \binom{2n}{n+k} \binom{n+k}{k}$ with Lucas sequences

Let $p$ be an
integer and let $U_n$ and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$,
$U_1 = 1$, $V_0 = 2$, $V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every
natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k} \binom{2n}{n+k} \binom{n+k}{k} U_k V_{n-k} = \binom{2n}{n}^2 U_n.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.10.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_n_plus_k` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-n-plus-k).

## Binomial-Catalan sum with Lucas sequences

Let $p$ be an integer, let $U_n$ and $V_n$ be
the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$, $V_1 = p$ and
both satisfy $X_{j+2} = p X_{j+1} + X_j$, and let $C_j$ be the $j$-th Catalan number. Then for
every natural number $n$,

$$\sum_{k=0}^{n} \binom{2n}{2k} C_k C_{n-k} U_{n-k} V_k = C_n C_{n+1} U_n.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.11.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_catalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-catalan).

## Alternating binomial-Catalan sum with Lucas sequences

Let $p$ be an integer, let $U_n$
and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$, and let $C_j$ be the $j$-th Catalan
number. Then for every natural number $n$,

$$\sum_{k=0}^{2n} (-1)^k \binom{4n}{2k} C_k C_{2n-k} U_{2n-k} V_k = (-1)^n C_n C_{2n} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.12.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_catalan_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-catalan-alter).

## Alternating two-binomial Catalan convolution of U and V

Let $p$ be an integer and let $U$
and $V$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so that $U_0 = 0$, $U_1 = 1$, $V_0 = 2$,
$V_1 = p$, and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Writing $C_j$ for the $j$-th Catalan
number, for every natural number $n$

$$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k} \binom{4n}{2k} C_k C_{2n-k} U_{2n-k} V_k =
(-1)^n \binom{3n+1}{n} C_n C_{2n} U_{2n}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 2.13.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_sq_catalan_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-sq-catalan-al).

## Binomial sums with signs $(-1)^{\binom{k}{2}}$ and Lucas sequences

Let $p$ be an integer
and let $U_n$ and $V_n$ be the Lucas sequences $U(p, -1)$ and $V(p, -1)$, so $U_0 = 0$,
$U_1 = 1$, $V_0 = 2$, $V_1 = p$ and both satisfy $X_{j+2} = p X_{j+1} + X_j$. Then for every
natural number $n$,

$$\sum_{k=0}^{4n+1} (-1)^{\binom{k}{2}} \binom{4n+1}{k} U_k V_{4n+1-k} = (-1)^n 2^{2n+1} U_{4n+1}$$

and

$$\sum_{k=0}^{4n+1} (-1)^{\binom{k}{2}} \binom{4n+1}{k} V_k U_{4n+1-k} = (-1)^n 2^{2n+1} U_{4n+1}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 3.1.

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_sum_choose_sign_choose_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#lucas-u-lucas-v-sum-choose-sign-choose-t).

## Two-sided binomial sums of products of Lucas sequences

Let $p$ be an integer, let $U$
and $V$ be the two-sided second-order sequences for $p$ with $U_0 = 0$, $U_1 = 1$, $V_0 = 2$ and
$V_1 = p$, both satisfying $X_{j+1} = p X_j + X_{j-1}$ for every integer $j$, and put
$\Delta = p^2 + 4$. Then for every natural number $n > 0$ and all integers $m$ and $r$,

$$\sum_{k=-n}^{n} \binom{2n}{n+k} U_{k+m} U_{k+r} = \Delta^{n-1} V_{m+r},$$



$$\sum_{k=-n}^{n} \binom{2n}{n+k} V_{k+m} V_{k+r} = \Delta^{n} V_{m+r},$$



$$\sum_{k=-n}^{n} \binom{2n}{n+k} U_{k+m} V_{k+r} = \Delta^{n} U_{m+r},$$



$$\sum_{k=-n}^{n} \binom{2n}{n+k} V_{k+m} U_{k+r} = \Delta^{n} U_{m+r}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 3.2.

Stated but not proved: `MetaMathlibExt.secondOrderBiSeq_sum_central_choose_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#second-order-bi-seq-sum-central-choose-m).

## Weighted two-sided binomial sums of products of Lucas sequences

Let $p$ be an integer,
let $U$ and $V$ be the two-sided second-order sequences for $p$ with $U_0 = 0$, $U_1 = 1$,
$V_0 = 2$ and $V_1 = p$, both satisfying $X_{j+1} = p X_j + X_{j-1}$ for every integer $j$, and
put $\Delta = p^2 + 4$. Then for every natural number $n > 0$ and all integers $m$ and $r$,

$$\sum_{k=-n}^{n} k \binom{2n}{n+k} U_{k+m} U_{k+r} = n p \Delta^{n-1} U_{m+r},$$



$$\sum_{k=-n}^{n} k \binom{2n}{n+k} V_{k+m} V_{k+r} = n p \Delta^{n} U_{m+r},$$



$$\sum_{k=-n}^{n} k \binom{2n}{n+k} U_{k+m} V_{k+r} = n p \Delta^{n-1} V_{m+r},$$



$$\sum_{k=-n}^{n} k \binom{2n}{n+k} V_{k+m} U_{k+r} = n p \Delta^{n-1} V_{m+r}.$$

## Sources

- John M. Campbell and Emrah Kılıç, *Binomial Sums Involving Second-Order Linearly Recurrent Sequences*, The Fibonacci Quarterly 62 (2024), Article 62-1/campbell10202023, Proposition 3.3.

Stated but not proved: `MetaMathlibExt.secondOrderBiSeq_sum_central_choose_mul_weighted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/SecondOrderBinomialSumsWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html#second-order-bi-seq-sum-central-choose-m-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial sums with second-order recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/binomial-sums-with-second-order-recurrences)
