---
declaration: section
origin: cited
lean: MetaMathlibExt.lucas_fib_weighted_binomial_sum_even_step, MetaMathlibExt.lucas_div_fib_sq_add_one_telescoping, MetaMathlibExt.sum_lucas_div_fib_sq_add_one, MetaMathlibExt.fib_cube_mul_sum_choose_lucas_pow, MetaMathlibExt.ten_mul_fib_cube_dvd, MetaMathlibExt.gibonacci_candido_derivative_identity, MetaMathlibExt.gibonacci_sum_sq_mul_sum_lucas_like, MetaMathlibExt.generalized_fibonacci_gelin_cesaro_derivative
statement: formalized
---

# Fibonacci identities via Fibonacci functions

44 results, 44 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html).

## Weighted binomial sums of Lucas and Fibonacci numbers with even step

Let $F_m$ be the
Fibonacci numbers extended to all integers $m$ ($F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$)
and $L_m = F_{m-1} + F_{m+1}$ the Lucas numbers. For every natural number $n$ and all integers
$k$, $r$ with $k$ even,

$$2 \sum_{j=0}^{n} j \binom{n}{j} L_{r+2kj} = 5 n L_k^{n-1} F_{r+nk} F_k + n L_k^n L_{r+nk}$$

and

$$2 \sum_{j=0}^{n} j \binom{n}{j} F_{r+2kj} = n L_k^{n-1} L_{r+nk} F_k + n L_k^n F_{r+nk}.$$

For $n = 0$ the exponent $n - 1$ is read as $0$; the term carrying it has the factor $n = 0$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 2 (`jis-2024-24.6.2-prop-2`).

Stated but not proved: `MetaMathlibExt.lucas_fib_weighted_binomial_sum_even_step` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#lucas-fib-weighted-binomial-sum-even-ste).

## Two telescoping relations between Lucas and Fibonacci numbers

Let $F_m$ be the Fibonacci
numbers extended to all integers $m$ ($F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$) and
$L_m = F_{m-1} + F_{m+1}$ the Lucas numbers. Then for every integer $k$,

$$\frac{L_{2k+1}}{F_{2k+1}^2 + 1} = \frac{L_{2k}}{F_{2k}^2 + 1} - \frac{L_{2k+2}}{F_{2k+2}^2 + 1}$$

and

$$\frac{L_{2k+1}}{L_{2k} L_{2k+2}} \cdot \frac{(F_{2k}^2 + 1)(F_{2k+2}^2 + 1)}{F_{2k+1}^2 + 1}
= \frac{F_{2k+2}^2 + 1}{L_{2k+2}} - \frac{F_{2k}^2 + 1}{L_{2k}}.$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 3 (`jis-2024-24.6.2-prop-3`).

Stated but not proved: `MetaMathlibExt.lucas_div_fib_sq_add_one_telescoping` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#lucas-div-fib-sq-add-one-telescoping).

## Telescoping sums of Lucas numbers over Fibonacci squares plus one

Let $F_m$ denote the
Fibonacci numbers and $L_m$ the Lucas numbers ($L_0 = 2$, $L_1 = 1$, $L_{m+2} = L_{m+1} + L_m$).
For every natural number $n$,

$$\sum_{k=1}^{n} \frac{L_{2k+1}}{F_{2k+1}^2 + 1} = \frac{3}{2} - \frac{L_{2n+2}}{F_{2n+2}^2 + 1}$$

and

$$\sum_{k=1}^{n} \frac{L_{2k+1}}{L_{2k} L_{2k+2}} \cdot
\frac{(F_{2k}^2 + 1)(F_{2k+2}^2 + 1)}{F_{2k+1}^2 + 1} =
\frac{F_{2n+2}^2 + 1}{L_{2n+2}} - \frac{2}{3},$$

and the real series $\sum_{k \ge 1} L_{2k+1} / (F_{2k+1}^2 + 1)$ has sum $3/2$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 4 (`jis-2024-24.6.2-prop-4`).

Stated but not proved: `MetaMathlibExt.sum_lucas_div_fib_sq_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#sum-lucas-div-fib-sq-add-one).

## Binomial sum with even powers of a Lucas number

Let $F_m$ and $L_m$ denote the Fibonacci
and Lucas numbers. For all natural numbers $k$ and $n$,

$$
F_k^3 \sum_{j=0}^{n} (-1)^{(k+1)(n+j)}\, j \binom{n+j}{2j} L_k^{2j}
= \frac{1}{10} \left((2n+1) F_{2k} L_{(2n+1)k} - F_{(2n+1)k} L_k^2\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 5 (`jis-2024-24.6.2-prop-5`).

Stated but not proved: `MetaMathlibExt.fib_cube_mul_sum_choose_lucas_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#fib-cube-mul-sum-choose-lucas-pow).

## Ten times a Fibonacci cube divides a Fibonacci–Lucas combination

Let $F_m$ denote the
Fibonacci numbers and $L_m$ the Lucas numbers. For all natural numbers $k$ and $n$, the integer
$10 F_k^3$ divides $(2n+1) F_{2k} L_{(2n+1)k} - F_{(2n+1)k} L_k^2$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 6 (`jis-2024-24.6.2-prop-6`).

Stated but not proved: `MetaMathlibExt.ten_mul_fib_cube_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#ten-mul-fib-cube-dvd).

## Cubic gibonacci identity from Candido's identity

Let $G : \mathbb{Z} \to \mathbb{R}$ be
a gibonacci sequence, that is, $G_{j+2} = G_{j+1} + G_j$ for every integer $j$. Then for every
integer $k$,

$$
G_k^2 \bigl(G_{k+1} (G_{k+2} + G_k) + G_{k+2} (G_{k+3} + G_{k+1}) -
G_k (G_{k+1} + G_{k-1})\bigr) +
G_{k+1}^2 \bigl(G_k (G_{k+1} + G_{k-1}) + G_{k+2} (G_{k+3} + G_{k+1}) -
G_{k+1} (G_{k+2} + G_k)\bigr) +
G_{k+2}^2 \bigl(G_k (G_{k+1} + G_{k-1}) + G_{k+1} (G_{k+2} + G_k) -
G_{k+2} (G_{k+3} + G_{k+1})\bigr) = 0.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 7 (`jis-2024-24.6.2-prop-7`).

Stated but not proved: `MetaMathlibExt.gibonacci_candido_derivative_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-candido-derivative-identity).

## Companion of Melham's sum-of-squares identity for gibonacci sequences

Let
$G : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$, satisfy $G_{j+2} = G_{j+1} + G_j$ for
every integer $j$, and let $F_m$ be the Fibonacci numbers. Then for every natural number $n$ and
every integer $k$ (the sums below are empty when $n = 0$),

$$
6 \Bigl(\sum_{j=0}^{2n-1} G_{j+k}^2\Bigr)
\Bigl(\sum_{j=0}^{2n-1} G_{j+k} (G_{j+k+1} + G_{j+k-1})\Bigr) =
F_{2n}^2 \bigl(G_{k+n-2}^3 (G_{k+n-1} + G_{k+n-3}) + 4 G_{k+n-1}^3 (G_{k+n} + G_{k+n-2}) +
4 G_{k+n}^3 (G_{k+n+1} + G_{k+n-1}) + G_{k+n+1}^3 (G_{k+n+2} + G_{k+n})\bigr).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 8 (`jis-2024-24.6.2-prop-8`).

Stated but not proved: `MetaMathlibExt.gibonacci_sum_sq_mul_sum_lucas_like` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-sum-sq-mul-sum-lucas-like).

## Derivative form of the Gelin–Cesàro identity for generalized Fibonacci sequences

Let
$p$ be a real number, let $W : \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = p W_{j+1} + W_j$
for every integer $j$, and put $\gamma_W = (p W_0 W_1 + W_0^2 - W_1^2)(p^2 - 1)$. Then for every
integer $k$,

$$
(W_{k-1} + W_{k-3}) W_{k-1} W_{k+1} W_{k+2} + W_{k-2} (W_k + W_{k-2}) W_{k+1} W_{k+2} +
W_{k-2} W_{k-1} (W_k + W_{k+2}) W_{k+2} + W_{k-2} W_{k-1} W_{k+1} (W_{k+3} + W_{k+1}) =
2 W_k (W_{k+1} + W_{k-1}) \bigl(2 W_k^2 + (-1)^k \gamma_W\bigr).
$$

This is the derivative form of the Horadam–Shannon Gelin–Cesàro identity. The paper's standing
assumption $p \ne 0$ is not needed.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 9 (`jis-2024-24.6.2-prop-9`).

Stated but not proved: `MetaMathlibExt.generalized_fibonacci_gelin_cesaro_derivative` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#generalized-fibonacci-gelin-cesaro-deriv).

## Alternating Fibonacci and Lucas sums from the Gelin–Cesàro identity

Let $F_m$ and $L_m$
denote the Fibonacci and Lucas numbers. For every natural number $n$,

$$
\sum_{k=1}^{n} \frac{(-1)^{k-1} F_{k+2}^2 F_{2k+4}}{F_{k+2}^4 - 1}
= \frac{5}{6} + \frac{(-1)^{n+1}}{2} \left(\frac{F_{2n+3}}{F_{n+1} F_{n+2}} -
\frac{F_{2n+5}}{F_{n+2} F_{n+3}} + \frac{F_{2n+7}}{F_{n+3} F_{n+4}}\right)
$$

and

$$
\sum_{k=1}^{n} \frac{(-1)^{k-1} L_{k+2}^2 F_{2k+4}}{L_{k+2}^4 - 25}
= \frac{5}{14} + \frac{(-1)^{n+1}}{2} \left(\frac{F_{2n+3}}{L_{n+1} L_{n+2}} -
\frac{F_{2n+5}}{L_{n+2} L_{n+3}} + \frac{F_{2n+7}}{L_{n+3} L_{n+4}}\right).
$$

The source's limiting cases are not included: the absolute values of the summands tend to
$\sqrt{5}$ and $1/\sqrt{5}$, so the summands do not tend to $0$ and neither series converges.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 10 (`jis-2024-24.6.2-prop-10`).

Stated but not proved: `MetaMathlibExt.alternating_sum_fib_sq_fib_div_fib_pow_four_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#alternating-sum-fib-sq-fib-div-fib-pow-f).

## Alternating Gelin–Cesàro sum for generalized Fibonacci sequences

Let $p$ be a real
number, let $W : \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = p W_{j+1} + W_j$ for every integer
$j$, and put $\gamma_W = (p W_0 W_1 + W_0^2 - W_1^2)(p^2 - 1)$. Let $n \ge 0$ and $k$ be
integers such that $W_{j+k-2} W_{j+k-1} W_{j+k+1} W_{j+k+2} \ne 0$ for $1 \le j \le n$ and
$W_{n+k-1}$, $W_{k-1}$, $W_{n+k+2}$, $W_{k+2}$ are nonzero. Then

$$
\sum_{j=1}^{n} \frac{(-1)^{j-1} \cdot 2 W_{j+k} (W_{j+k+1} + W_{j+k-1})
\bigl(2 W_{j+k}^2 + (-1)^{j+k} \gamma_W\bigr)}{W_{j+k-2} W_{j+k-1} W_{j+k+1} W_{j+k+2}} =
(-1)^{n+1} \frac{W_{n+k} + W_{n+k-2}}{W_{n+k-1}} + \frac{W_k + W_{k-2}}{W_{k-1}} +
(-1)^{n+1} \frac{W_{n+k+3} + W_{n+k+1}}{W_{n+k+2}} + \frac{W_{k+3} + W_{k+1}}{W_{k+2}}.
$$

The paper's standing assumption $p \ne 0$ is not needed.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 11 (`jis-2024-24.6.2-prop-11`).

Stated but not proved: `MetaMathlibExt.generalized_fibonacci_gelin_cesaro_alternating_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#generalized-fibonacci-gelin-cesaro-alter).

## Reciprocal series of Lucas sequences with doubling subscripts

Let $P \ne 0$ be an
integer and let $U_m = U_m(P, -1)$ and $V_m = V_m(P, -1)$ be the Lucas sequences with parameters
$(P, -1)$, so $U_0 = 0$, $U_1 = 1$, $V_0 = 2$, $V_1 = P$, and both satisfy
$X_{m+2} = P X_{m+1} + X_m$. For every integer $k \ge 1$ and every integer $n \ge 1$,

$$\sum_{j=0}^{n} \frac{2^j V_{k 2^j}}{U_{k 2^j}^2} = \frac{2(-1)^k + V_k}{U_k^2} +
\frac{2(1 - (-1)^k) V_{2k}}{U_{2k}^2} - \frac{2^{n+1}}{U_{k 2^n}^2},$$

and the real series $\sum_{j \ge 0} 2^j V_{k 2^j} / U_{k 2^j}^2$ has sum

$$\frac{2(-1)^k + V_k}{U_k^2} + \frac{2(1 - (-1)^k) V_{2k}}{U_{2k}^2}.$$

The paper's real parameter $p$ is restricted here to integers $P$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 12 (`jis-2024-24.6.2-prop-12`).

Stated but not proved: `MetaMathlibExt.sum_two_pow_lucasV_div_lucasU_sq_doubling` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#sum-two-pow-lucas-v-div-lucas-u-sq-doubl).

## A Fibonacci–Lucas identity for gibonacci sequences

Let $F_m$ denote the Fibonacci
numbers, extended to all integers $m$ by $F_{-m} = (-1)^{m+1} F_m$, and let
$L_m = F_{m-1} + F_{m+1}$ be the Lucas numbers, for every integer $m$. If
$G : \mathbb{Z} \to \mathbb{R}$ satisfies $G_{j+2} = G_{j+1} + G_j$ for every integer $j$, then
for all integers $k$ and $r$,

$$
5 F_k G_{k+r} - L_k \left(G_{k+r+1} + G_{k+r-1}\right)
= 2 (-1)^{k-1} \left(G_{r+1} + G_{r-1}\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 18 (`jis-2024-24.6.2-prop-18`).

Stated but not proved: `MetaMathlibExt.five_fib_mul_gibonacci_sub_lucas_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#five-fib-mul-gibonacci-sub-lucas-mul).

## An identity for products of two gibonacci sequences

Let
$G, H : \mathbb{Z} \to \mathbb{R}$ satisfy $G_{j+2} = G_{j+1} + G_j$ and
$H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for all integers $k$, $r$ and $s$,

$$
5 G_k H_{k+s-r} - \left(G_{k+1} + G_{k-1}\right) \left(H_{k+s-r+1} + H_{k+s-r-1}\right)
= 2 (-1)^{k-r+1} \left(G_{r+1} + G_{r-1}\right) \left(H_{s+1} + H_{s-1}\right) +
2 (-1)^{k-r} \left(G_0 \left(H_{r+s} + H_{r+s-2}\right) +
G_1 \left(H_{r+s+1} + H_{r+s-1}\right)\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 19 (`jis-2024-24.6.2-prop-19`).

Stated but not proved: `MetaMathlibExt.five_gibonacci_mul_sub_two_gibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#five-gibonacci-mul-sub-two-gibonacci).

## Addition formula for gibonacci sequences

Let $F_m$ denote the Fibonacci numbers,
extended to all integers $m$ by $F_{-m} = (-1)^{m+1} F_m$. If $G : \mathbb{Z} \to \mathbb{R}$
satisfies $G_{j+2} = G_{j+1} + G_j$ for every integer $j$, then
$F_{k+1} G_{s+1} + F_k G_s = G_{k+s+1}$ for all integers $k$ and $s$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 20 (`jis-2024-24.6.2-prop-20`).

Stated but not proved: `MetaMathlibExt.fib_mul_gibonacci_add_eq_gibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#fib-mul-gibonacci-add-eq-gibonacci).

## A sum of two gibonacci products in terms of the seeds

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for all
integers $k$ and $s$,

$$
H_{k+1} G_{s+1} + H_k G_s = G_0 H_{k+s} + G_1 H_{k+s+1}.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 21 (`jis-2024-24.6.2-prop-21`).

Stated but not proved: `MetaMathlibExt.gibonacci_mul_gibonacci_add_eq_seed_combination` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-mul-gibonacci-add-eq-seed-comb).

## d'Ocagne-type identity for two gibonacci sequences

Let $G$ and $H$ be gibonacci
sequences, that is, functions $X : \mathbb{Z} \to \mathbb{R}$ with $X_{j+2} = X_{j+1} + X_j$
for every integer $j$. Then for all integers $r$, $s$, $k$,

$$
H_{r+s} G_{k+1} - H_{r+s+1} G_k =
(-1)^{r-1} (H_{s+1} + H_{s-1}) G_{k-r} + (-1)^r (G_0 H_{k+s-r-1} + G_1 H_{k+s-r}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 23 (`jis-2024-24.6.2-prop-23`).

Stated but not proved: `MetaMathlibExt.gibonacci_dOcagne_type_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-d-ocagne-type-identity).

## Shifted product identity for two gibonacci sequences

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for all
integers $s$ and $k$,

$$
G_{k+1} H_{s+1} + G_{k-2} H_{s-2} = 2 G_k H_s + 2 G_{k-1} H_{s-1}.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 24 (`jis-2024-24.6.2-prop-24`).

Stated but not proved: `MetaMathlibExt.gibonacci_product_shift_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-product-shift-identity).

## Product recurrence for three gibonacci sequences

Let
$G, H, I : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$, $j \mapsto H_j$ and
$j \mapsto I_j$, satisfy $G_{j+2} = G_{j+1} + G_j$, $H_{j+2} = H_{j+1} + H_j$ and
$I_{j+2} = I_{j+1} + I_j$ for every integer $j$. Then for all integers $k$, $r$ and $s$,

$$
G_{k+1} H_{r+1} I_{s+1} = 3 G_k H_r I_s + 6 G_{k-1} H_{r-1} I_{s-1} -
3 G_{k-2} H_{r-2} I_{s-2} - G_{k-3} H_{r-3} I_{s-3}.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 25 (`jis-2024-24.6.2-prop-25`).

Stated but not proved: `MetaMathlibExt.gibonacci_triple_product_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-triple-product-recurrence).

## Gibonacci index doubling via Fibonacci squares

Let $F_m$ be the Fibonacci numbers
extended to all integers $m$ ($F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$), and let
$G \colon \mathbb{Z} \to \mathbb{R}$ satisfy $G_{j+2} = G_{j+1} + G_j$ for every integer $j$.
Then for all integers $k$, $s$,

$$G_{2k+s} = F_{k+1}^2 G_{s+1} + F_k^2 G_s - F_{k-1}^2 G_{s-1}.$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 26 (`jis-2024-24.6.2-prop-26`).

Stated but not proved: `MetaMathlibExt.gibonacci_two_mul_add_eq_fib_sq_combination` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-two-mul-add-eq-fib-sq-combinat).

## Seed expansion of a triple gibonacci product

Let $G, H, I \colon \mathbb{Z} \to \mathbb{R}$
satisfy $G_{j+2} = G_{j+1} + G_j$, $H_{j+2} = H_{j+1} + H_j$ and $I_{j+2} = I_{j+1} + I_j$ for
every integer $j$. Then for all integers $k$, $r$, $s$,

$$G_0 H_0 I_{k+r+s-2} + (G_0 H_1 + G_1 H_0) I_{k+r+s-1} + G_1 H_1 I_{k+r+s}
= G_{s+1} H_{r+1} I_{k+1} + G_s H_r I_k - G_{s-1} H_{r-1} I_{k-1}.$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 27 (`jis-2024-24.6.2-prop-27`).

Stated but not proved: `MetaMathlibExt.gibonacci_triple_product_seed_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-triple-product-seed-identity).

## Lucas expansion of shifted gibonacci sums

Let $F_m$ be the Fibonacci numbers, extended
to all integers $m$ by $F_{m+2} = F_{m+1} + F_m$, and let $L_m = F_{m-1} + F_{m+1}$ be the
Lucas numbers. Let $G : \mathbb{Z} \to \mathbb{R}$ be a gibonacci sequence, that is,
$G_{j+2} = G_{j+1} + G_j$ for every integer $j$. Then for all integers $k$ and $r$,
$G_{k+r+1} + G_{k+r-1} = L_k G_{r+1} + L_{k-1} G_r$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 28 (`jis-2024-24.6.2-prop-28`).

Stated but not proved: `MetaMathlibExt.gibonacci_add_gibonacci_eq_lucas_combination` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-add-gibonacci-eq-lucas-combina).

## Seed form of a Lucas-type product identity for two gibonacci sequences

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for all
integers $k$ and $r$,

$$
G_0 (H_{r+k} + H_{r+k-2}) + G_1 (H_{r+k+1} + H_{r+k-1}) =
G_r (H_k + H_{k-2}) + G_{r+1} (H_{k+1} + H_{k-1}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 29 (`jis-2024-24.6.2-prop-29`).

Stated but not proved: `MetaMathlibExt.gibonacci_seed_lucas_like_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-seed-lucas-like-identity).

## Sum of products of two gibonacci sequences

Let $G, H \colon \mathbb{Z} \to \mathbb{R}$
satisfy $G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. For every
natural number $n$ and all integers $k$ and $s$,

$$2 \sum_{j=1}^{n} G_{j+k} H_{j+s} = G_{n+k} H_{n+s+1} + G_{n+k+1} H_{n+s} -
G_{k+1} H_s - G_k H_{s+1}.$$

The printed statement lacks the factor $2$: it fails for the Fibonacci sequence $G = H = F$
with $k = s = 0$ and $n = 1$, where the left side is $1$ and the right side $2$. The paper's own
derivation (its display before the proposition) carries the factor $2$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 30 (`jis-2024-24.6.2-prop-30`).

Stated but not proved: `MetaMathlibExt.two_mul_sum_gibonacci_mul_gibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#two-mul-sum-gibonacci-mul-gibonacci).

## Hoggatt–Bicknell-type binomial sum with Fibonacci cubes

Let $F_m$ denote the Fibonacci
numbers, extended to all integers $m$ by $F_{-m} = (-1)^{m+1} F_m$. If
$G : \mathbb{Z} \to \mathbb{R}$ satisfies $G_{j+2} = G_{j+1} + G_j$ for every integer $j$, then
for every natural number $n$ and all integers $k$ and $r$,

$$
\sum_{j=0}^{4n+1} (-1)^{j+1} \binom{4n+1}{j} F_{j+k}^3 G_{j+r}
= 25^n \left(F_{2n+k+1}^3 G_{2n+r+1} - F_{2n+k}^3 G_{2n+r}\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 31 (`jis-2024-24.6.2-prop-31`).

Stated but not proved: `MetaMathlibExt.alternating_binomial_sum_fib_cube_mul_gibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#alternating-binomial-sum-fib-cube-mul-gi).

## Hoggatt–Bicknell-type binomial sum of four gibonacci sequences

Let
$E, G, H, I : \mathbb{Z} \to \mathbb{R}$ satisfy $E_{j+2} = E_{j+1} + E_j$ for every integer $j$,
and likewise $G$, $H$ and $I$. Then for every natural number $n$ and all integers $k$, $r$, $s$
and $t$,

$$
\sum_{j=0}^{4n+1} (-1)^{j+1} \binom{4n+1}{j} E_{j+k} G_{j+r} H_{j+s} I_{j+t}
= 25^n \left(E_{2n+k+1} G_{2n+r+1} H_{2n+s+1} I_{2n+t+1} -
E_{2n+k} G_{2n+r} H_{2n+s} I_{2n+t}\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 32 (`jis-2024-24.6.2-prop-32`).

Stated but not proved: `MetaMathlibExt.alternating_binomial_sum_four_gibonacci_product` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#alternating-binomial-sum-four-gibonacci).

## Mixed Melham-type sum for two gibonacci sequences

Let $F_m$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$), and let $G, H \colon \mathbb{Z} \to \mathbb{R}$
satisfy $G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for
every natural number $n$ and all integers $k$, $r$,

$$6 \Bigl(\sum_{j=0}^{2n-1} G_{k+j}^2\Bigr) \Bigl(\sum_{j=0}^{2n-1} H_{r+j} G_{k+j}\Bigr)
= F_{2n}^2 \bigl(H_{r+n-2} G_{k+n-2}^3 + 4 H_{r+n-1} G_{k+n-1}^3 +
4 H_{r+n} G_{k+n}^3 + H_{r+n+1} G_{k+n+1}^3\bigr).$$

The paper leaves $n$ unquantified; it is taken as a natural number, as in
Proposition 8.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 33 (`jis-2024-24.6.2-prop-33`).

Stated but not proved: `MetaMathlibExt.six_mul_sum_gibonacci_sq_mul_sum_mixed` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#six-mul-sum-gibonacci-sq-mul-sum-mixed).

## Four-sequence Melham-type identity for gibonacci sequences

Let
$G, H, I, J : \mathbb{Z} \to \mathbb{R}$ satisfy $G_{j+2} = G_{j+1} + G_j$ for every integer $j$,
and likewise $H$, $I$ and $J$, and let $F_m$ denote the Fibonacci numbers. For every natural
number $n$ and all integers $k$, $r$, $s$ and $t$, writing
$S(X, x; Y, y) = \sum_{j=0}^{2n-1} X_{x+j} Y_{y+j}$ for sequences $X, Y$ and integers $x, y$,

$$
2 S(G, k; J, t) S(H, r; I, s) + 2 S(I, s; J, t) S(G, k; H, r) +
2 S(G, k; I, s) S(H, r; J, t)
= F_{2n}^2 \big(G_{k+n-2} H_{r+n-2} I_{s+n-2} J_{t+n-2} +
4 G_{k+n-1} H_{r+n-1} I_{s+n-1} J_{t+n-1} + 4 G_{k+n} H_{r+n} I_{s+n} J_{t+n} +
G_{k+n+1} H_{r+n+1} I_{s+n+1} J_{t+n+1}\big).
$$

The source leaves $n$ unquantified; it is taken to be a natural number.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 34 (`jis-2024-24.6.2-prop-34`).

Stated but not proved: `MetaMathlibExt.four_gibonacci_melham_type_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#four-gibonacci-melham-type-identity).

## Two-sequence gibonacci identity with a Fibonacci factor

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$, and let $F_m$ be
the Fibonacci numbers, extended to negative indices by $F_{-m} = (-1)^{m+1} F_m$. Then for all
integers $r$, $s$ and $k$,

$$
H_s G_{k+r} + (-1)^{r-1} H_{s-r} G_k = F_r (G_0 H_{k+s-1} + G_1 H_{k+s}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 35 (`jis-2024-24.6.2-prop-35`).

Stated but not proved: `MetaMathlibExt.gibonacci_mul_add_neg_one_pow_eq_fib_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-mul-add-neg-one-pow-eq-fib-mul).

## Four-index product identity for two gibonacci sequences

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$, and let $F_m$ be
the Fibonacci numbers, extended to negative indices by $F_{-m} = (-1)^{m+1} F_m$. Then for all
integers $k$, $r$, $s$ and $t$,

$$
F_s (G_0 H_{k+r+t-1} + G_1 H_{k+r+t}) - (-1)^r F_{s-r} G_k (H_{t+1} + H_{t-1}) +
(-1)^r G_k H_{s-r+t} = G_{k+s} H_{r+t}.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 36 (`jis-2024-24.6.2-prop-36`).

Stated but not proved: `MetaMathlibExt.gibonacci_product_four_index_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-product-four-index-identity).

## Two-sequence Candido-type identity for gibonacci sequences

Let $G$ and $H$ be gibonacci
sequences, that is, functions $X : \mathbb{Z} \to \mathbb{R}$ with $X_{j+2} = X_{j+1} + X_j$
for every integer $j$. Then for all integers $r$ and $k$,

$$
2 (H_r G_k^3 + H_{r+1} G_{k+1}^3 + H_{r+2} G_{k+2}^3) =
(G_k^2 + G_{k+1}^2 + G_{k+2}^2)(H_r G_k + H_{r+1} G_{k+1} + H_{r+2} G_{k+2}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 37 (`jis-2024-24.6.2-prop-37`).

Stated but not proved: `MetaMathlibExt.gibonacci_candido_two_sequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-candido-two-sequence).

## Four-sequence Candido-type identity for gibonacci sequences

Let $G$, $H$, $M$, $N$ be
gibonacci sequences, that is, functions $X : \mathbb{Z} \to \mathbb{R}$ with
$X_{j+2} = X_{j+1} + X_j$ for every integer $j$. For two such sequences $X$, $Y$ and integers
$x$, $y$ write $T(X, x; Y, y) = X_x Y_y + X_{x+1} Y_{y+1} + X_{x+2} Y_{y+2}$. Then for all
integers $k$, $r$, $s$, $t$,

$$
6 (G_k H_r M_s N_t + G_{k+1} H_{r+1} M_{s+1} N_{t+1} + G_{k+2} H_{r+2} M_{s+2} N_{t+2}) =
T(G, k; M, s) \, T(H, r; N, t) + T(G, k; H, r) \, T(M, s; N, t) +
T(G, k; N, t) \, T(H, r; M, s).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 38 (`jis-2024-24.6.2-prop-38`).

Stated but not proved: `MetaMathlibExt.gibonacci_candido_four_sequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-candido-four-sequence).

## Lucas multiplier identity for gibonacci sequences

Let $F_m$ be the Fibonacci numbers,
extended to all integers $m$ by $F_{m+2} = F_{m+1} + F_m$, and let $L_m = F_{m-1} + F_{m+1}$ be
the Lucas numbers. Let $G : \mathbb{Z} \to \mathbb{R}$ be a gibonacci sequence, that is,
$G_{j+2} = G_{j+1} + G_j$ for every integer $j$. Then for all integers $r$ and $s$,
$G_{s+r} + (-1)^r G_{s-r} = L_r G_s$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 39 (`jis-2024-24.6.2-prop-39`).

Stated but not proved: `MetaMathlibExt.gibonacci_add_neg_one_pow_mul_eq_lucas_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-add-neg-one-pow-mul-eq-lucas-m).

## Two-sequence gibonacci identity with a Fibonacci factor and Lucas-type sums

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$, and let $F_m$ be
the Fibonacci numbers, extended to negative indices by $F_{-m} = (-1)^{m+1} F_m$. Then for all
integers $r$, $k$ and $s$,

$$
G_s (H_{r+k+1} + H_{r+k-1}) + (-1)^{r-1} G_{s-r} (H_{k+1} + H_{k-1}) =
G_0 F_r (H_{k+s} + H_{k+s-2}) + G_1 F_r (H_{k+s+1} + H_{k+s-1}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 40 (`jis-2024-24.6.2-prop-40`).

Stated but not proved: `MetaMathlibExt.gibonacci_lucas_like_mul_add_eq_fib_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-lucas-like-mul-add-eq-fib-mul).

## Two-sequence Gelin–Cesàro derivative identity for gibonacci sequences

Let
$G, H : \mathbb{Z} \to \mathbb{R}$, written $j \mapsto G_j$ and $j \mapsto H_j$, satisfy
$G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$, and put
$e_G = G_0^2 - G_1^2 + G_0 G_1$. Then for all integers $k$ and $r$,

$$
H_{k+r-2} G_{k-1} G_{k+1} G_{k+2} + G_{k-2} H_{k+r-1} G_{k+1} G_{k+2} +
G_{k-2} G_{k-1} H_{k+r+1} G_{k+2} + G_{k-2} G_{k-1} G_{k+1} H_{k+r+2} =
4 H_{k+r} G_k^3 - 2 e_G G_0 (H_{r+2} + H_r) + 2 e_G G_1 (H_{r+1} + H_{r-1}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 42 (`jis-2024-24.6.2-prop-42`).

Stated but not proved: `MetaMathlibExt.gibonacci_gelin_cesaro_two_sequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-gelin-cesaro-two-sequence).

## Catalan-type identity for Fibonacci and gibonacci numbers

Let $F_m$ denote the Fibonacci
numbers, extended to all integers $m$ by $F_{-m} = (-1)^{m+1} F_m$. If
$G : \mathbb{Z} \to \mathbb{R}$ satisfies $G_{j+2} = G_{j+1} + G_j$ for every integer $j$, then
for all integers $k$, $r$ and $s$,

$$
F_{k+r} G_{k-r+s} + F_{k-r} G_{k+r+s}
= 2 F_k G_{k+s} + (-1)^{k+r+1} F_r^2 \left(G_{s+1} + G_{s-1}\right).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 43 (`jis-2024-24.6.2-prop-43`).

Stated but not proved: `MetaMathlibExt.fib_gibonacci_catalan_type_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#fib-gibonacci-catalan-type-identity).

## Lucas-weighted identity for two gibonacci sequences

Let $F_m$ be the Fibonacci numbers
extended to all integers $m$ ($F_0 = 0$, $F_1 = 1$, $F_{m+2} = F_{m+1} + F_m$) and
$L_m = F_{m-1} + F_{m+1}$ the Lucas numbers, and let $G, H \colon \mathbb{Z} \to \mathbb{R}$
satisfy $G_{j+2} = G_{j+1} + G_j$ and $H_{j+2} = H_{j+1} + H_j$ for every integer $j$. Then for
all integers $r$, $s$, $t$,

$$L_r (G_0 H_{s+t-1} + G_1 H_{s+t}) - (-1)^r G_{s-r} (H_{t+1} + H_{t-1})
= H_{r+t} (G_{s+1} + G_{s-1}).$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 44 (`jis-2024-24.6.2-prop-44`).

Stated but not proved: `MetaMathlibExt.lucas_mul_gibonacci_seed_sub_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 662](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L662). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#lucas-mul-gibonacci-seed-sub-eq).

## Two-sequence Catalan-type identity for gibonacci sequences

Let $F_m$ be the Fibonacci
numbers, extended to all integers $m$ by $F_{m+2} = F_{m+1} + F_m$, and let $G$ and $H$ be
gibonacci sequences, that is, functions $X : \mathbb{Z} \to \mathbb{R}$ with
$X_{j+2} = X_{j+1} + X_j$ for every integer $j$. Then for all integers $k$, $r$, $s$, $t$,

$$
G_{k+s-r} H_{k+r+t} + G_{k+s+r} H_{k-r+t} =
2 G_{k+s} H_{k+t} +
(-1)^{k+r} F_r^2 \bigl(G_0 (H_{s+t} + H_{s+t-2}) + G_1 (H_{s+t+1} + H_{s+t-1})\bigr) -
(-1)^{k+r} F_r^2 (G_{s+1} + G_{s-1}) (H_{t+1} + H_{t-1}).
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 45 (`jis-2024-24.6.2-prop-45`).

Stated but not proved: `MetaMathlibExt.gibonacci_catalan_type_two_sequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-catalan-type-two-sequence).

## Gibonacci identity with Fibonacci-square denominators

Let $G : \mathbb{Z} \to \mathbb{R}$,
written $j \mapsto G_j$, satisfy $G_{j+2} = G_{j+1} + G_j$ for every integer $j$, and let $F_m$ be
the Fibonacci numbers, extended to negative indices by $F_{-m} = (-1)^{m+1} F_m$. Then for all
integers $r$ and $k$,

$$
\frac{G_{r+2}}{F_{2k}^2 + 1} - \frac{G_r}{F_{2k+2}^2 + 1} =
\frac{G_{2k+r+3} + G_{2k+r+1}}{F_{2k+1} (F_{2k+1}^2 + 1)} - \frac{G_{r+1}}{F_{2k+1}^2 + 1}.
$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 46 (`jis-2024-24.6.2-prop-46`).

Stated but not proved: `MetaMathlibExt.gibonacci_div_fib_sq_add_one_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#gibonacci-div-fib-sq-add-one-identity).

## Ratio form of the Binet formula for Horadam sequences

Let $P$, $Q$, $\sigma$, $\tau$ be
real numbers with $Q \neq 0$, $\sigma + \tau = P$ and $\sigma \tau = Q$, and let
$W \colon \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = P W_{j+1} - Q W_j$ for every integer $j$.
Then for every integer $k$: if $W_1 \neq \sigma W_0$, then

$$\frac{W_{k+1} - \sigma W_k}{W_1 - \sigma W_0} = \tau^k,$$

and if $W_1 \neq \tau W_0$, then

$$\frac{W_{k+1} - \tau W_k}{W_1 - \tau W_0} = \sigma^k.$$

This covers the paper's sequence $W_j(W_0, W_1; p)$, the case $P = p$, $Q = -1$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Lemma 47 (`jis-2024-24.6.2-lem-47`).

Stated but not proved: `MetaMathlibExt.horadam_sub_root_mul_div_eq_zpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#horadam-sub-root-mul-div-eq-zpow).

## Product exchange identity for two Horadam sequences

Let $P$, $Q$ be real numbers with
$Q \neq 0$, and let $W, Z \colon \mathbb{Z} \to \mathbb{R}$ satisfy
$W_{j+2} = P W_{j+1} - Q W_j$ and $Z_{j+2} = P Z_{j+1} - Q Z_j$ for every integer $j$. Then for
all integers $r$, $k$,

$$Z_r W_{k+1} - Q Z_{r-1} W_k = W_1 Z_{k+r} - Q W_0 Z_{k+r-1}.$$

The paper states this for $Q < 0$; the identity holds for every $Q \neq 0$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 48 (`jis-2024-24.6.2-prop-48`).

Stated but not proved: `MetaMathlibExt.horadam_product_exchange_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#horadam-product-exchange-identity).

## Companion Lucas sequence identity for Horadam sequences

Let $P$, $Q$ be real numbers
with $Q \neq 0$. Let $W \colon \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = P W_{j+1} - Q W_j$
for every integer $j$, and let $V \colon \mathbb{Z} \to \mathbb{R}$ (the companion Lucas sequence)
satisfy the same recurrence with $V_0 = 2$ and $V_1 = P$. Then for all integers $k$, $r$,

$$V_r W_{k+1} - Q V_{r-1} W_k = W_{k+r+1} - Q W_{k+r-1}.$$

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Proposition 49 (`jis-2024-24.6.2-prop-49`).

Stated but not proved: `MetaMathlibExt.horadam_companion_lucas_mul_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#horadam-companion-lucas-mul-identity).

## Companion Binet formula for generalized Fibonacci sequences

Let $p$ be a real number and
let $W : \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = p W_{j+1} + W_j$ for every integer $j$. Put
$\sigma = (p + \sqrt{p^2 + 4})/2$ and $\tau = (p - \sqrt{p^2 + 4})/2$. Then for every integer
$j$,

$$
(W_1 - W_0 \tau) \sigma^j + (W_1 - W_0 \sigma) \tau^j = W_{j+1} + W_{j-1}.
$$

Here $A = W_1 - W_0 \tau$ and $B = W_1 - W_0 \sigma$ are the Binet constants of $W$, so that
$W_j = (A \sigma^j - B \tau^j)/(\sigma - \tau)$.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Lemma 13 (`jis-2024-24.6.2-lem-13`).

Stated but not proved: `MetaMathlibExt.generalizedFibonacci_binet_add_eq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#generalized-fibonacci-binet-add-eq-add).

## Derivative of a branch of $\lambda^x$ for negative $\lambda$

Let $\lambda < 0$ be real
and $m$ an integer, and consider the branch $\lambda^y = (-\lambda)^y e^{i\pi(2m+1)y}$, a function
of real $y$ with complex values, where $(-\lambda)^y$ is the real power of the positive number
$-\lambda$. For every real $x$ this function has derivative
$\lambda^x \bigl(i\pi(2m+1) + \ln(-\lambda)\bigr)$ at $x$. The branch corresponds to the
journal proof's evaluation $\ln(-1) = i\pi(2m+1)$.

The case of a positive base, where $\lambda^x$ has derivative $\lambda^x \ln \lambda$, is standard
and is not part of this statement.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Lemma 14 (`jis-2024-24.6.2-lem-14`).

Stated but not proved: `MetaMathlibExt.hasDerivAt_neg_rpow_branch` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#has-deriv-at-neg-rpow-branch).

## Real part of the derivative of the generalized Fibonacci function at integers

Let $p$
be a real number and let $W : \mathbb{Z} \to \mathbb{R}$ satisfy $W_{j+2} = p W_{j+1} + W_j$ for
every integer $j$. Put $\delta = \sqrt{p^2 + 4}$, $\sigma = (p + \delta)/2$,
$\tau = (p - \delta)/2$, $A = W_1 - W_0 \tau$ and $B = W_1 - W_0 \sigma$. For an integer $m$,
define $w : \mathbb{R} \to \mathbb{C}$ by

$$
w(x) = \frac{A \sigma^x - B (-\tau)^x e^{i \pi (2m + 1) x}}{\delta}.
$$

Then for every integer $j$, $\operatorname{Re} w'(j) = (W_{j+1} + W_{j-1}) \ln \sigma / \delta$.

Since $\tau < 0$, $w(x)$ is $(A \sigma^x - B \tau^x)/\delta$ with $\tau^x$ read on the branch
$(-\tau)^x e^{i \pi (2m + 1) x}$; this is the generalized Fibonacci function of the journal text.

## Sources

- Kunle Adegoke, *Fibonacci Identities via Fibonacci Functions*, Journal of Integer Sequences 27 (2024), Article 24.6.2, Theorem 15 (`jis-2024-24.6.2-thm-15`).

Stated but not proved: `MetaMathlibExt.generalizedFibonacci_function_deriv_re` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean, line 789](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciFunctionIdentitiesWanted.lean#L789). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html#generalized-fibonacci-function-deriv-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci identities via Fibonacci functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-identities-via-fibonacci-functions)
