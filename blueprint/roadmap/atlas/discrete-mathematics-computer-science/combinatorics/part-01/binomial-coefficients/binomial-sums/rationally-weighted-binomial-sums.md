---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_pow_mul_coeff_eq_sum_stirlingSecond_derivative, MetaMathlibExt.sum_risingStep_mul_coeff_eq_sum_hsuShiue_derivative, MetaMathlibExt.stirlingSecond_three_eq, MetaMathlibExt.sum_neg_one_pow_choose_two_pow_mul_sq, MetaMathlibExt.sum_poly_mul_fib_pow_eq_sum_stirlingSecond_derivative, MetaMathlibExt.sum_pow_mul_choose_mul_fib, MetaMathlibExt.sum_pow_mul_choose_mul_lucasNumber, MetaMathlibExt.sum_pow_mul_choose_mul_secondOrder
statement: formalized
---

# Rationally weighted binomial sums

17 results, 1 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html).

## Scherk's identity

Write $S(r, i)$ for the Stirling numbers of the second kind. Let $N$ and
$r$ be natural numbers, let $a_0, \dots, a_N$ be real numbers, and let $f$ be the polynomial
$f(y) = \sum_{k=0}^{N} a_k y^k$, with $i$-th derivative $f^{(i)}$. Then for every real number $x$,
with the convention $0^0 = 1$,

$$\sum_{k=0}^{N} k^r a_k x^k = \sum_{i=0}^{r} S(r, i) \, x^i f^{(i)}(x).$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 2.1, equation (2.1).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_coeff_eq_sum_stirlingSecond_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-pow-mul-coeff-eq-sum-stirling-second).

## Scherk's identity with $s$-rising factorials

Let $s$ be a real number and let $S(n, k)$
be the generalized Stirling numbers of Hsu and Shiue with parameters $(-s, 1, 0)$: a real array
with $S(0, 0) = 1$, $S(n, 0) = 0$ for $n \ge 1$, $S(n, k) = 0$ for $n < k$, and
$S(n+1, k+1) = S(n, k) + (k + 1 + ns) \, S(n, k+1)$ for all $n, k \ge 0$. Let $N$ and $r$ be
natural numbers, let $a_0, \dots, a_N$ be real numbers, and let $f(y) = \sum_{k=0}^{N} a_k y^k$,
with $i$-th derivative $f^{(i)}$. Then for every real number $x > 0$,

$$\sum_{k=0}^{N} k (k + s) \cdots (k + (r-1)s) \, a_k x^{k + rs} =
\sum_{i=0}^{r} S(r, i) \, x^{rs + i} f^{(i)}(x),$$

where the product $k (k + s) \cdots (k + (r-1)s)$ has the $r$ factors $k + js$, $0 \le j < r$,
and is $1$ when $r = 0$.

The powers of $x$ have real exponents, which is why $x > 0$ is assumed.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 2.1, equation (2.2).

Stated but not proved: `MetaMathlibExt.sum_risingStep_mul_coeff_eq_sum_hsuShiue_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-rising-step-mul-coeff-eq-sum-hsu-shi).

## Stirling numbers of the second kind with three blocks

For every integer $r \ge 1$, the
Stirling number of the second kind $S(r, 3)$ satisfies
$S(r, 3) = \frac{3^{r-1} + 1}{2} - 2^{r-1}$.

The source states this for $r \ge 3$; both sides vanish at $r = 1$ and $r = 2$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Proposition 2.2.

Formalized by `MetaMathlibExt.stirlingSecond_three_eq`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#stirling-second-three-eq).

## Greenstreet's identity

For every natural number $N$,

$$\sum_{k=1}^{N} (-1)^k \binom{N}{k} 2^{N-k} k^2 = N^2 - 2N.$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 2.3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_two_pow_mul_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-neg-one-pow-choose-two-pow-mul-sq).

## Polynomially weighted Fibonacci sums via derivatives

Let $F_n$ denote the Fibonacci
numbers and $S(r, i)$ the Stirling numbers of the second kind. Let $t$ and $N$ be natural numbers,
let $A_0, \dots, A_t$ be complex numbers, let $h(y) = \sum_{r=0}^{t} A_r y^r$, and let $P$ be the
polynomial $P(y) = \sum_{j=0}^{N} F_j y^j$, with $i$-th derivative $P^{(i)}$. Then for every
$x \in \mathbb{C}$,

$$\sum_{k=0}^{N} h(k) F_k x^k = \sum_{r=0}^{t} A_r \sum_{i=0}^{r} S(r, i) \, x^i P^{(i)}(x).$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 2.4.

Stated but not proved: `MetaMathlibExt.sum_poly_mul_fib_pow_eq_sum_stirlingSecond_derivative` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-poly-mul-fib-pow-eq-sum-stirling-sec).

## Power-weighted binomial sums of Fibonacci numbers

Let $F_n$ denote the Fibonacci numbers,
$S(r, i)$ the Stirling numbers of the second kind and $(N)_i = N(N-1) \cdots (N-i+1)$ the falling
factorial, with $(N)_0 = 1$. For all natural numbers $N$ and $r$,

$$\sum_{k=0}^{N} k^r \binom{N}{k} F_k = \sum_{i=0}^{r} S(r, i) \, (N)_i \, F_{2N-i},$$

where the terms with $i > N$ vanish because $(N)_i = 0$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 2.5.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_choose_mul_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-pow-mul-choose-mul-fib).

## Power-weighted binomial sums of Lucas numbers

Let $L_n$ denote the Lucas numbers
($L_0 = 2$, $L_1 = 1$, $L_{n+2} = L_{n+1} + L_n$), $S(r, i)$ the Stirling numbers of the second
kind and $(N)_i = N(N-1) \cdots (N-i+1)$ the falling factorial, with $(N)_0 = 1$. For all natural
numbers $N$ and $r$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{N} k^r \binom{N}{k} L_k = \sum_{i=0}^{r} S(r, i) \, (N)_i \, L_{2N-i},$$

where the terms with $i > N$ vanish because $(N)_i = 0$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 2.5.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_choose_mul_lucasNumber` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-pow-mul-choose-mul-lucas-number).

## Power-weighted binomial sums of a second-order linear recurrence

Let $a$ and $b$ be real
numbers and let $(W_n)_{n \ge 0}$ be a real sequence with $W_{n+2} = a W_{n+1} + b W_n$ for all
$n \ge 0$. Write $S(r, i)$ for the Stirling numbers of the second kind and
$(N)_i = N(N-1) \cdots (N-i+1)$ for the falling factorial, with $(N)_0 = 1$. Then for all natural
numbers $N$ and $r$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{N} k^r \binom{N}{k} a^k b^{N-k} W_k = \sum_{i=0}^{r} S(r, i) (N)_i a^i W_{2N-i},$$

where the terms with $i > N$ vanish because $(N)_i = 0$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 2.5.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_choose_mul_secondOrder` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-pow-mul-choose-mul-second-order).

## Weighted binomial Fibonacci sums for the powers one to four

Let $F_n$ denote the Fibonacci
numbers. For every natural number $N$,

$$\sum_{k=1}^{N} k \binom{N}{k} F_k = N F_{2N-1},$$



$$\sum_{k=1}^{N} k^2 \binom{N}{k} F_k = N F_{2N-1} + N(N-1) F_{2N-2},$$



$$\sum_{k=1}^{N} k^3 \binom{N}{k} F_k = N F_{2N-1} + 3N(N-1) F_{2N-2} + N(N-1)(N-2) F_{2N-3},$$



$$\sum_{k=1}^{N} k^4 \binom{N}{k} F_k = N F_{2N-1} + 7N(N-1) F_{2N-2} +
6N(N-1)(N-2) F_{2N-3} + N(N-1)(N-2)(N-3) F_{2N-4}.$$

Every term with a negative Fibonacci index has coefficient zero.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 2.6.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_choose_mul_fib_small` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-pow-mul-choose-mul-fib-small).

## Polynomially weighted binomial Fibonacci sums

Let $F_n$ denote the Fibonacci numbers,
$S(j, i)$ the Stirling numbers of the second kind and $(N)_i = N(N-1)\cdots(N-i+1)$ the falling
factorial. Let $A_0, A_1, A_2, \dots$ be complex numbers and $N$, $t$ natural numbers, and put
$h(y) = \sum_{j=0}^{t} A_j y^j$. Then

$$\sum_{k=1}^{N} h(k) \binom{N}{k} F_k =
\sum_{j=0}^{t} A_j \sum_{i=0}^{j} S(j, i)\, (N)_i\, F_{2N-i}.$$

Moreover,
$\sum_{k=1}^{N} (A_0 + A_1 k + A_2 k^2 + A_3 k^3 + A_4 k^4) \binom{N}{k} F_k$ equals
$A_0 F_{2N} + (A_1 + A_2 + A_3 + A_4) \binom{N}{1} F_{2N-1} +
2(A_2 + 3A_3 + 7A_4) \binom{N}{2} F_{2N-2} + 6(A_3 + 6A_4) \binom{N}{3} F_{2N-3} +
24 A_4 \binom{N}{4} F_{2N-4}$.

The source's hypotheses $N, t > 0$ and $t \le N/2$ are not needed and are dropped.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 2.7.

Stated but not proved: `MetaMathlibExt.sum_poly_mul_choose_mul_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-poly-mul-choose-mul-fib).

## Polynomially weighted binomial sums of powers of a second-order sequence

Let $a$, $b$ be
real numbers and $(U_n)_{n \ge 0}$ a real sequence with $U_{n+2} = a U_{n+1} + b U_n$ for all $n$.
Let $\alpha \ne \beta$ be complex numbers with $\alpha + \beta = a$ and $\alpha\beta = -b$ (the
roots of $y^2 = ay + b$), and put $A = (U_1 - U_0\beta)/(\alpha - \beta)$ and
$B = (U_1 - U_0\alpha)/(\alpha - \beta)$. Let $S(j, i)$ denote the Stirling numbers of the second
kind and $(N)_i = N(N-1)\cdots(N-i+1)$ the falling factorial. Let $c_0, c_1, c_2, \dots$ be
complex numbers, $t$, $N$, $r$ natural numbers and $h(y) = \sum_{j=0}^{t} c_j y^j$. Then for every
complex number $x$,

$$\sum_{k=0}^{N} h(k) \binom{N}{k} U_k^r x^k =
\sum_{j=0}^{t} c_j \sum_{i=0}^{j} S(j, i)\, x^i \sum_{\ell=0}^{r} \binom{r}{\ell} A^\ell
(-B)^{r-\ell} (N)_i\, (\alpha^\ell \beta^{r-\ell})^i (1 + \alpha^\ell \beta^{r-\ell} x)^{N-i}.$$

The source prints $A^j$, with the outer index $j$, where its proof gives $A^\ell$; the printed
form fails for the Fibonacci numbers $U_k = F_k$, $h = 1$, $r = N = 1$, $x = 0$ (left side $0$,
printed right side $1 - 1/\sqrt{5}$). The source's coefficients $A_j$ of $h$ are renamed $c_j$,
and positivity of $r$, $N$, $t$ is dropped.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 2.8.

Stated but not proved: `MetaMathlibExt.sum_poly_mul_choose_mul_secondOrder_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-poly-mul-choose-mul-second-order-pow).

## Binomial sums with rising-factorial denominators

Write $m^{(i)} = m(m+1)\cdots(m+i-1)$
for the rising factorial. For all natural numbers $N$ and $s \ge 1$ and every real number $x$,

$$\sum_{k=0}^{N} \binom{N}{k} \frac{x^{k+s}}{(k+1)^{(s)}} =
\frac{(1+x)^{N+s} - 1}{(N+1)^{(s)}} - \sum_{j=1}^{s-1} \frac{x^j}{j!\,(N+1)^{(s-j)}}.$$

The source writes $\binom{n}{k}$ for $\binom{N}{k}$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 3.1, equation (3.1).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_pow_div_ascFactorial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-choose-mul-pow-div-asc-factorial).

## Rising-factorial weighted sums via iterated antiderivatives

Let $N$ and $s$ be natural
numbers, $a_0, \dots, a_N$ real numbers and $f(y) = \sum_{k=0}^{N} a_k y^k$. Let
$I_0, I_1, I_2, \dots$ be functions $\mathbb{R} \to \mathbb{R}$ with $I_0 = f$ such that for every
$j \ge 0$ the function $I_{j+1}$ is differentiable on $\mathbb{R}$ with derivative $I_j$ (the
constants of integration are arbitrary). Write $m^{(i)} = m(m+1)\cdots(m+i-1)$ for the rising
factorial. Then for every real number $x$,

$$\sum_{k=0}^{N} \frac{a_k\, x^{k+s}}{(k+1)^{(s)}} =
I_s(x) - \sum_{j=1}^{s} \frac{I_j(0)\, x^{s-j}}{(s-j)!}.$$

The source assumes $s > 0$; for $s = 0$ the identity reads $f(x) = I_0(x)$.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Theorem 3.1, equation (3.2).

Stated but not proved: `MetaMathlibExt.sum_coeff_mul_pow_div_ascFactorial_eq_antideriv` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-coeff-mul-pow-div-asc-factorial-eq-a).

## Epsteen's identity

For every natural number $n$,

$$\sum_{k=0}^{n} \frac{1}{k+1} \binom{n}{k} = \frac{2^{n+1} - 1}{n+1}.$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 3.2.

Stated but not proved: `MetaMathlibExt.sum_choose_div_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-choose-div-succ).

## Finkel's identity

For every natural number $n$, with $H_n = \sum_{j=1}^{n} 1/j$ the
$n$-th harmonic number,

$$\sum_{k=1}^{n} (-1)^{k-1} \frac{1}{k} \binom{n}{k} = H_n.$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 3.2.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_div_eq_harmonic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-neg-one-pow-choose-div-eq-harmonic).

## Binomial sums weighted by $x^k/k^2$

For every natural number $n$ and every real number
$x$,

$$\sum_{k=1}^{n} \binom{n}{k} \frac{x^k}{k^2} =
\sum_{k=1}^{n} \frac{1}{k} \sum_{j=1}^{k} \frac{(1+x)^j}{j} -
\sum_{k=1}^{n} \frac{1}{k} \sum_{j=1}^{k} \frac{1}{j}.$$

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 3.2.

Stated but not proved: `MetaMathlibExt.sum_choose_mul_pow_div_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-choose-mul-pow-div-sq).

## Alternating binomial sum with inverse-square weights

For every natural number $n$, with
$H_k = \sum_{j=1}^{k} 1/j$ the $k$-th harmonic number,

$$\sum_{k=1}^{n} (-1)^{k-1} \frac{1}{k^2} \binom{n}{k} = \sum_{k=1}^{n} \frac{H_k}{k}.$$

This is the case $x = -1$ of identity (3.6) of the source.

## Sources

- Andreea M. Stănică, Gabriela N. Stănică, and Pantelimon Stănică, *An Evaluation of Rationally Weighted Binomial Sums Via Some Differential and Integral Operators*, The Fibonacci Quarterly 62 (2024), Article 62-1/stanica09202023, Corollary 3.2.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_div_sq_eq_sum_harmonic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RationallyWeightedBinomialSumsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html#sum-neg-one-pow-choose-div-sq-eq-sum-har).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rationally weighted binomial sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/rationally-weighted-binomial-sums)
