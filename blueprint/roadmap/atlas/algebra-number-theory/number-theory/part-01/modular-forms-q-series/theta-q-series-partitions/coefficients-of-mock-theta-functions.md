---
declaration: section
origin: cited
lean: MetaMathlibExt.mockThetaV, MetaMathlibExt.mockThetaSigma, MetaMathlibExt.mockThetaLambda, MetaMathlibExt.coeff_mockThetaV_zero_one, MetaMathlibExt.coeff_mockThetaSigma_zero_one, MetaMathlibExt.coeff_mockThetaLambda_zero_one, MetaMathlibExt.ramanujanThetaMonomial, MetaMathlibExt.coeff_ramanujanThetaMonomial_one_one_three
statement: formalized
---

# Coefficients of mock theta functions

22 results, 8 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html).

## The eighth-order mock theta function $v(q)$

The mock theta function
$v(q) = \sum_{n \ge 0} q^{(n+1)^2} (-q; q^2)_n / (q; q^2)_{n+1}$, where
$(-q; q^2)_n = \prod_{k=0}^{n-1} (1 + q^{2k+1})$ and
$(q; q^2)_{n+1} = \prod_{k=0}^{n} (1 - q^{2k+1})$, is taken as a power series in $q$ with integer
coefficients.

The $n$th summand has order $(n+1)^2$, so the coefficient of $q^m$ only involves the summands
with $n \le m$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (4).

Formalized by `MetaMathlibExt.mockThetaV`, a definition declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v).

## The sixth-order mock theta function $\sigma(q)$

The mock theta function
$\sigma(q) = \sum_{n \ge 0} q^{(n+1)(n+2)/2} (-q; q)_n / (q; q^2)_{n+1}$, where
$(-q; q)_n = \prod_{k=1}^{n} (1 + q^k)$ and $(q; q^2)_{n+1} = \prod_{k=0}^{n} (1 - q^{2k+1})$, is
taken as a power series in $q$ with integer coefficients.

The $n$th summand has order $(n+1)(n+2)/2 > n$, so the coefficient of $q^m$ only involves the
summands with $n \le m$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (2).

Formalized by `MetaMathlibExt.mockThetaSigma`, a definition declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-sigma).

## The sixth-order mock theta function $\lambda$

With
$(a; b)_n = \prod_{k=0}^{n-1} (1 - a b^k)$, the mock theta function $\lambda$ is the integer
power series

$$
\lambda(q) = \sum_{n \ge 0} \frac{(-1)^n q^n (q; q^2)_n}{(-q; q)_n}.
$$

The $n$th summand has order $n$, so the coefficient of $q^m$ only involves the summands with
$n \le m$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (3).

Formalized by `MetaMathlibExt.mockThetaLambda`, a definition declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-lambda).

## First coefficients of the mock theta function $v$

Write
$v(q) = \sum_{n \ge 0} P_v(n) q^n$ for the eighth-order mock theta function $v$. Then
$P_v(0) = 0$ and $P_v(1) = 1$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (4).

Formalized by `MetaMathlibExt.coeff_mockThetaV_zero_one`, a theorem declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#coeff-mock-theta-v-zero-one).

## First coefficients of the mock theta function $\sigma$

Write
$\sigma(q) = \sum_{n \ge 0} P_\sigma(n) q^n$ for the sixth-order mock theta function $\sigma$.
Then $P_\sigma(0) = 0$ and $P_\sigma(1) = 1$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (2).

Formalized by `MetaMathlibExt.coeff_mockThetaSigma_zero_one`, a theorem declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#coeff-mock-theta-sigma-zero-one).

## First coefficients of the mock theta function $\lambda$

Write
$\lambda(q) = \sum_{n \ge 0} P_\lambda(n) q^n$ for the sixth-order mock theta function $\lambda$.
Then $P_\lambda(0) = 1$ and $P_\lambda(1) = -1$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (3).

Formalized by `MetaMathlibExt.coeff_mockThetaLambda_zero_one`, a theorem declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#coeff-mock-theta-lambda-zero-one).

## Ramanujan's theta function at monomial arguments

For an integer $\varepsilon$ and natural
numbers $a$ and $b$, $f(\varepsilon q^a, \varepsilon q^b)$ is the integer power series in $q$
whose coefficient of $q^n$ is the sum of $\varepsilon^{m^2}$ over the integers $m$ with
$|m| \le n + 1$ and $a \cdot m(m+1)/2 + b \cdot m(m-1)/2 = n$.

When $a + b \ge 1$ the exponent $a \cdot m(m+1)/2 + b \cdot m(m-1)/2$ is at least
$|m|(|m|-1)/2$, so the bound $|m| \le n + 1$ excludes no term and this is Ramanujan's
$f(c, d) = \sum_{m \in \mathbb{Z}} c^{m(m+1)/2} d^{m(m-1)/2}$ at $c = \varepsilon q^a$ and
$d = \varepsilon q^b$; the definition is meant for $a + b \ge 1$. Special cases are
$\psi(q) = f(q, q^3)$ and $f(-q) = f(-q, -q^2)$, which equals
$(q; q)_\infty = \prod_{k \ge 1} (1 - q^k)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Section 2 (definition of `f(c, d)`, Equations (10) and (11)).

Formalized by `MetaMathlibExt.ramanujanThetaMonomial`, a definition declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#ramanujan-theta-monomial).

## First coefficients of Ramanujan's theta function $\psi$

Let
$\psi(q) = f(q, q^3) = \sum_{m \in \mathbb{Z}} q^{m(m+1)/2 + 3m(m-1)/2}$, where $f$ is
Ramanujan's general theta function. The coefficients of $q^0$, $q^1$, $q^2$, $q^3$ in $\psi(q)$
are $1$, $1$, $0$, $1$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Equation (10).

Formalized by `MetaMathlibExt.coeff_ramanujanThetaMonomial_one_one_three`, a theorem declared in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#coeff-ramanujan-theta-monomial-one-one-t).

## The p-dissection of Ramanujan's psi function

Let $p$ be an odd prime, let $f(c, d)$ be
Ramanujan's theta function and $\psi(q) = f(q, q^3)$. Then, as integer power series,
$\psi(q) = \sum_{m=0}^{(p-3)/2} q^{(m^2+m)/2} f(q^{(p^2+(2m+1)p)/2}, q^{(p^2-(2m+1)p)/2}) +
q^{(p^2-1)/8} f(q^{p^2}, q^{3p^2})$, where the last factor is $\psi(q^{p^2})$. Moreover
$(m^2+m)/2 \not\equiv (p^2-1)/8 \pmod p$ for every integer $m$ with $0 \le m \le (p-3)/2$.

The paper quotes this from Cui and Gu, Theorem 2.1.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Lemma 1.

Stated but not proved: `MetaMathlibExt.ramanujanPsi_p_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#ramanujan-psi-p-dissection).

## The $p$-dissection of $f_1$

Let $p \ge 5$ be a prime, let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for $k \ge 1$, and let
$f(a, b) = \sum_{m \in \mathbb{Z}} a^{m(m+1)/2} b^{m(m-1)/2}$ be Ramanujan's general theta
function. Put $c = (p-1)/6$ if $p \equiv 1 \pmod 6$ and $c = (-p-1)/6$ otherwise. Then, as
integer power series,

$$
f_1 = \sum_{t=-(p-1)/2,\ t \ne c}^{(p-1)/2} (-1)^t q^{(3t^2+t)/2}
f\bigl(-q^{(3p^2+(6t+1)p)/2}, -q^{(3p^2-(6t+1)p)/2}\bigr) +
(-1)^c q^{(p^2-1)/24} f_{p^2}.
$$

Moreover, $(3t^2 + t)/2 \not\equiv (p^2 - 1)/24 \pmod p$ for every integer $t$ with
$-(p-1)/2 \le t \le (p-1)/2$ and $t \ne c$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Lemma 2.

Stated but not proved: `MetaMathlibExt.eulerProduct_p_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#euler-product-p-dissection).

## The $p$-dissection of $f_1^3$

Let $p$ be an odd prime and, for $k \ge 1$, let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series,

$$
f_1^3 = \sum_{k=0,\ k \ne (p-1)/2}^{p-1} (-1)^k q^{k(k+1)/2}
\sum_{n \ge 0} (-1)^n (2pn + 2k + 1) q^{pn(pn+2k+1)/2} +
p (-1)^{(p-1)/2} q^{(p^2-1)/8} f_{p^2}^3.
$$

Moreover, $(k^2 + k)/2 \not\equiv (p^2 - 1)/8 \pmod p$ for every integer $k$ with
$0 \le k \le p - 1$ and $k \ne (p-1)/2$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Lemma 3.

Stated but not proved: `MetaMathlibExt.eulerProduct_cube_p_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#euler-product-cube-p-dissection).

## Generating function for the odd-indexed coefficients of $v(q)$

Let $P_v(n)$ be the
coefficient of $q^n$ in the eighth-order mock theta function $v(q)$, and for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series,
$f_1 f_2 \sum_{n \ge 0} P_v(2n+1) q^n = f_4^3$, that is,
$\sum_{n \ge 0} P_v(2n+1) q^n = f_4^3 / (f_1 f_2)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 1.

Stated but not proved: `MetaMathlibExt.mockThetaV_odd_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-odd-generating-function).

## The coefficients of $q^{6n+5}$ in $v(q)$ are divisible by 3

Let $P_v(n)$ be the
coefficient of $q^n$ in the eighth-order mock theta function $v(q)$. Then
$P_v(6n+5) \equiv 0 \pmod 3$ for every $n \ge 0$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 2 (i).

Stated but not proved: `MetaMathlibExt.mockThetaV_coeff_six_mul_add_five_mod_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-coeff-six-mul-add-five-mod).

## Infinite family of congruences modulo 2 for $v(q)$

Let $P_v(n)$ be the coefficient of
$q^n$ in the eighth-order mock theta function $v(q)$, and for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 3$ be a prime whose Legendre symbol
$\left(\frac{-2}{p}\right)$ equals $-1$, and let $\alpha \ge 0$ be an integer. Then the integer
power series $f_1 \sum_{n \ge 0} P_v\bigl(2 p^{2\alpha} n + (3 p^{2\alpha} + 1)/4\bigr) q^n$ and
$f_2 f_4^2$ have congruent coefficients modulo $2$. Moreover, for every $n \ge 0$ and every $j$
with $1 \le j \le p - 1$,
$P_v\bigl(2 p^{2\alpha+2} n + 2 p^{2\alpha+1} j + (3 p^{2\alpha+2} + 1)/4\bigr) \equiv 0 \pmod 2$.

The divisions by $4$ are exact since $p^2 \equiv 1 \pmod 8$. Since $f_1$ has an inverse with
integer coefficients, the first congruence says that
$\sum_{n \ge 0} P_v(2 p^{2\alpha} n + (3 p^{2\alpha} + 1)/4) q^n \equiv \psi(q) \psi(q^2) \pmod 2$,
where $\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$, so that $\psi(q) \psi(q^2) = f_2 f_4^2 / f_1$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 2 (ii), Equations (21) and (22).

Stated but not proved: `MetaMathlibExt.mockThetaV_congruences_mod_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-congruences-mod-two).

## Infinite family of congruences modulo 6 for $v(q)$

Let $P_v(n)$ be the coefficient of
$q^n$ in the eighth-order mock theta function $v(q)$, and for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime whose Legendre symbol
$\left(\frac{-18}{p}\right)$ equals $-1$, and let $\alpha \ge 0$ be an integer. Then for every
$n \ge 0$, $P_v\bigl(6 p^{2\alpha} n + (19 p^{2\alpha} + 1)/4\bigr)$ is congruent modulo $6$ to
the coefficient of $q^n$ in $3 f_1 f_6^3$. Moreover, for every $n \ge 0$ and every $j$ with
$1 \le j \le p - 1$,
$P_v\bigl(6 p^{2\alpha+2} n + 6 p^{2\alpha+1} j + (19 p^{2\alpha+2} + 1)/4\bigr) \equiv 0 \pmod 6$.

The divisions by $4$ are exact since $p^2 \equiv 1 \pmod 8$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 2 (iii), Equations (23) and (24).

Stated but not proved: `MetaMathlibExt.mockThetaV_congruences_mod_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-congruences-mod-six).

## Sum formula for the odd-indexed coefficients of $v(q)$

Let $P_v(n)$ be the coefficient
of $q^n$ in the eighth-order mock theta function $v(q)$, for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $b_4^1(k)$ be the coefficient of $q^k$ in the
integer power series $f_4 / f_1$. Then for every $n \ge 0$,
$P_v(2n+1) = \sum_{m \ge 0,\ m(m+1) \le n} b_4^1\bigl(n - m(m+1)\bigr)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 3.

Stated but not proved: `MetaMathlibExt.mockThetaV_odd_eq_sum_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-odd-eq-sum-regular).

## Sum formula for the coefficients of $q^{6n+5}$ in $v(q)$

Let $P_v(n)$ be the
coefficient of $q^n$ in the eighth-order mock theta function $v(q)$, for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $b_6^3(k)$ be the coefficient of $q^k$ in the
integer power series $(f_6 / f_1)^3$. Then for every $n \ge 0$,
$P_v(6n+5) = 3 b_6^3(n) + 3 \sum_{m \ge 1,\ 2m(3m+1) \le n} (-1)^m b_6^3\bigl(n - 2m(3m+1)\bigr) +
3 \sum_{m \ge 1,\ 2m(3m-1) \le n} (-1)^m b_6^3\bigl(n - 2m(3m-1)\bigr)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 4.

Stated but not proved: `MetaMathlibExt.mockThetaV_six_mul_add_five_eq_sum_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-v-six-mul-add-five-eq-sum-reg).

## Generating function for the odd-indexed coefficients of $\sigma(q)$

Let $P_\sigma(n)$
be the coefficient of $q^n$ in the sixth-order mock theta function $\sigma(q)$, and for
$k \ge 1$ let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series,
$f_1^2 f_3 \sum_{n \ge 0} P_\sigma(2n+1) q^n = f_2^2 f_6^2$, that is,
$\sum_{n \ge 0} P_\sigma(2n+1) q^n = f_2^2 f_6^2 / (f_1^2 f_3)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 5.

Stated but not proved: `MetaMathlibExt.mockThetaSigma_odd_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-sigma-odd-generating-function).

## Congruences modulo 2 for the mock theta function $\sigma$

Write
$\sigma(q) = \sum_{n \ge 0} P_\sigma(n) q^n$ for the sixth-order mock theta function $\sigma$ and
let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime with Legendre symbol
$\left(\frac{-2}{p}\right) = -1$ and let $\alpha \ge 0$ be an integer. Then, coefficientwise,

$$
f_3 \sum_{n \ge 0} P_\sigma\Bigl(2 p^{2\alpha} n + \frac{11 p^{2\alpha} + 1}{12}\Bigr) q^n
\equiv f_2 f_6^2 \pmod 2,
$$

and for all integers $n \ge 0$ and all integers $j$ with $1 \le j \le p - 1$,

$$
P_\sigma\Bigl(2 p^{2\alpha+2} n + 2 p^{2\alpha+1} j + \frac{11 p^{2\alpha+2} + 1}{12}\Bigr)
\equiv 0 \pmod 2.
$$

Since $f_2 f_6^2 / f_3 = f_2 \psi(q^3)$ with $\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$, the first
congruence says that the series of $P_\sigma(2 p^{2\alpha} n + (11 p^{2\alpha} + 1)/12)$ is
congruent to $f_2 \psi(q^3)$ modulo $2$. The division by $12$ is exact since
$p^2 \equiv 1 \pmod{24}$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 6.

Stated but not proved: `MetaMathlibExt.mockThetaSigma_congruences_mod_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-sigma-congruences-mod-two).

## Sum formula for the odd-indexed coefficients of $\sigma(q)$

Let $P_\sigma(n)$ be the
coefficient of $q^n$ in the sixth-order mock theta function $\sigma(q)$, for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $b_2^2(k)$ be the coefficient of $q^k$ in the
integer power series $(f_2 / f_1)^2$. Then for every $n \ge 0$,
$P_\sigma(2n+1) = \sum_{m \ge 0,\ (3m^2+3m)/2 \le n} b_2^2\bigl(n - (3m^2+3m)/2\bigr)$.

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 7.

Stated but not proved: `MetaMathlibExt.mockThetaSigma_odd_eq_sum_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-sigma-odd-eq-sum-regular).

## Even-index coefficients of the mock theta function $\lambda$

Write
$\lambda(q) = \sum_{n \ge 0} P_\lambda(n) q^n$ for the sixth-order mock theta function $\lambda$,
let $f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $b_2^3(m)$ be the coefficient of $q^m$ in
$(f_2/f_1)^3$. Then for every $n \ge 0$,

$$
P_\lambda(2n) = b_2^3(n) + 2 \sum_{k \ge 1,\ 3k^2 \le n} (-1)^k b_2^3(n - 3k^2).
$$

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 8.

Stated but not proved: `MetaMathlibExt.mockThetaLambda_even_eq_sum_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-lambda-even-eq-sum-regular).

## Coefficients of the mock theta function $\lambda$ at indices $6n+2$

Write
$\lambda(q) = \sum_{n \ge 0} P_\lambda(n) q^n$ for the sixth-order mock theta function $\lambda$,
let $f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $\overline{p}_3(j)$ be the coefficient of
$q^j$ in $(f_2/f_1^2)^3$. Then for every $n \ge 0$,

$$
P_\lambda(6n+2) = 3 \sum_{m \ge 0,\ 3m(m+1)/2 \le n} (-1)^m (2m+1)\,
\overline{p}_3\bigl(n - 3m(m+1)/2\bigr) +
6 \sum_{m \ge 0} \sum_{k \ge 1,\ 3k^2 + 3m(m+1)/2 \le n} (-1)^{m+k} (2m+1)\,
\overline{p}_3\bigl(n - 3k^2 - 3m(m+1)/2\bigr).
$$

## Sources

- Sabi Biswas and Nipen Saikia, *Arithmetic Properties of the Coefficients of Some Mock Theta Functions*, INTEGERS 25 (2025), Article A72, Theorem 9.

Stated but not proved: `MetaMathlibExt.mockThetaLambda_six_mul_add_two_eq_sum_overpartition` is written with `theorem_wanted` in [WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MockThetaCoefficientsWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html#mock-theta-lambda-six-mul-add-two-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coefficients of mock theta functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/coefficients-of-mock-theta-functions)
