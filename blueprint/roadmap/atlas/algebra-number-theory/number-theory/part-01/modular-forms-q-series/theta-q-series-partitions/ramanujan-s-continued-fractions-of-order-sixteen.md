---
declaration: section
origin: cited
lean: MetaMathlibExt.lambert_order_sixteen_weight_n, MetaMathlibExt.lambert_order_sixteen_legendre_three, MetaMathlibExt.ramanujan_psi_f_chi_eq_qPochhammer, MetaMathlibExt.ramanujanTheta_entry30, MetaMathlibExt.lambert_odd_order_sixteen_eq_continuedFraction, MetaMathlibExt.jacobiThetaOneSineRaw, MetaMathlibExt.jacobiThetaOneSine, MetaMathlibExt.jacobiThetaOneSine_zero
statement: formalized
---

# Ramanujan's continued fractions of order sixteen

10 results, 4 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html).

## Weighted Lambert series for the continued fractions of order sixteen

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$,
$(a_1, \dots, a_k; q)_\infty = (a_1; q)_\infty \cdots (a_k; q)_\infty$ and
$f_k = (q^k; q^k)_\infty$. For every complex number $q$ with $|q| < 1$,

$$\sum_{n \ge 1} n \frac{q^n - q^{7n} - q^{9n} + q^{15n}}{1 - q^{16n}} =
\frac{q f_{16}^2 f_8^2 (q^6, q^{10}; q^{16})_\infty}{(q, q^7, q^9, q^{15}; q^{16})_\infty^2}$$

and

$$\sum_{n \ge 1} n \frac{q^{3n} - q^{5n} - q^{11n} + q^{13n}}{1 - q^{16n}} =
\frac{q^3 f_{16}^2 f_8^2 (q^2, q^{14}; q^{16})_\infty}
{(q^3, q^5, q^{11}, q^{13}; q^{16})_\infty^2}.$$

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Theorem 3, Equations (62)-(63).

Stated but not proved: `MetaMathlibExt.lambert_order_sixteen_weight_n` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#lambert-order-sixteen-weight-n).

## Lambert series of order sixteen twisted by the Legendre symbol modulo $3$

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$,
$(a_1, \dots, a_k; q)_\infty = (a_1; q)_\infty \cdots (a_k; q)_\infty$ and
$f_k = (q^k; q^k)_\infty$, and let $\left(\frac{n}{3}\right)$ be the Legendre symbol modulo $3$.
For every complex number $q$ with $|q| < 1$,

$$\sum_{n \ge 1} \left(\frac{n}{3}\right) \frac{q^n - q^{7n} - q^{9n} + q^{15n}}{1 - q^{16n}} =
\frac{q f_8^2 f_{48} (q^6, q^{10}; q^{16})_\infty (q, q^7, q^9, q^{15}; q^{16})_\infty}
{f_{16} (q^3, q^{21}, q^{27}, q^{45}; q^{48})_\infty}$$

and

$$\sum_{n \ge 1} \left(\frac{n}{3}\right) \frac{q^{3n} - q^{5n} - q^{11n} + q^{13n}}{1 - q^{16n}} =
\frac{q^3 f_8^2 f_{48} (q^2, q^{14}; q^{16})_\infty (q^3, q^5, q^{11}, q^{13}; q^{16})_\infty}
{f_{16} (q^9, q^{15}, q^{33}, q^{39}; q^{48})_\infty}.$$

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Theorem 4, Equations (64)-(65).

Stated but not proved: `MetaMathlibExt.lambert_order_sixteen_legendre_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#lambert-order-sixteen-legendre-three).

## Product forms of Ramanujan's theta functions $\psi$, $f$ and $\chi$

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ and $f_k = (q^k; q^k)_\infty$, and let
$f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's general theta
function. For every complex number $q$ with $|q| < 1$,
$f(q, q^3) = f_2^2 / f_1$, $f(q, -q^2) = f_2^3 / (f_1 f_4)$, $(-q; q^2)_\infty = f_2^2 / (f_1 f_4)$
and $(q; q^2)_\infty = f_1 / f_2$.

In Ramanujan's notation (Berndt, Part III, Chapter 16), with $\psi(q) = f(q, q^3)$,
$f(q) = f(q, -q^2)$ and $\chi(q) = (-q; q^2)_\infty$, these read $\psi(q) = f_2^2 / f_1$,
$f(q) = f_2^3 / (f_1 f_4)$, $\chi(q) = f_2^2 / (f_1 f_4)$ and $\chi(-q) = f_1 / f_2$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Lemma 1.

Stated but not proved: `MetaMathlibExt.ramanujan_psi_f_chi_eq_qPochhammer` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#ramanujan-psi-f-chi-eq-q-pochhammer).

## Ramanujan's Entry 30 (i)–(iii) for the general theta function

Let
$f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's general theta
function and $\psi(q) = f(q, q^3)$. For all complex numbers $a$ and $b$ with $|ab| < 1$,
$f(a, ab^2) f(b, a^2 b) = f(a, b) \psi(ab)$ and $f(a, b) + f(-a, -b) = 2 f(a^3 b, a b^3)$, and if
moreover $a \ne 0$, then $f(a, b) - f(-a, -b) = 2a f(b/a, a^5 b^3)$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Lemma 1 record, quoting Berndt, Part III, Entry 30 (i)-(iii).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_entry30` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#ramanujan-theta-entry30).

## Odd Lambert series for Ramanujan's continued fractions of order sixteen

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ and $(a, b; q)_\infty = (a; q)_\infty (b; q)_\infty$.
For a complex number $q$ with $|q| < 1$, put
$S(a, b) = \sum_{k \ge 0} (q^{a(2k+1)} + q^{b(2k+1)}) / (1 - q^{16(2k+1)})$, a sum over the odd
multiples $n = 2k + 1$, and
$E = q^4 (q^{32}; q^{32})_\infty^4 / (q^{16}; q^{16})_\infty^2$,
$I_1 = q (q^6, q^{26}; q^{32})_\infty / (q^{10}, q^{22}; q^{32})_\infty$ and
$I_2 = q^3 (q^2, q^{30}; q^{32})_\infty / (q^{14}, q^{18}; q^{32})_\infty$. Then
$S(3, 5) - S(11, 13) = E (I_1 + 1/I_1)$ and $S(1, 7) - S(9, 15) = E (I_2 + 1/I_2)$.
At $q = 0$, where $I_1 = I_2 = 0$, the quotients $1/I_1$ and $1/I_2$ are read as $0$ and both
sides of each identity are $0$.

Here $I_1$ and $I_2$ are $I_1(q^2)$ and $I_2(q^2)$ for Ramanujan's continued fractions of order
sixteen $I_1(q) = q^{1/2} (q^3, q^{13}; q^{16})_\infty / (q^5, q^{11}; q^{16})_\infty$ and
$I_2(q) = q^{3/2} (q, q^{15}; q^{16})_\infty / (q^7, q^9; q^{16})_\infty$, and $E$ is the eta
quotient $\eta^4(32\tau) / \eta^2(16\tau)$ for $q = e^{2 \pi i \tau}$, where
$\eta(\tau) = q^{1/24} (q; q)_\infty$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Theorem 2, Equations (54)-(55).

Stated but not proved: `MetaMathlibExt.lambert_odd_order_sixteen_eq_continuedFraction` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#lambert-odd-order-sixteen-eq-continued-f).

## Raw Jacobi theta function $\theta_1$

For complex numbers $z$ and $\tau$, the raw Jacobi
theta function is

$$\theta_1(z \mid \tau) = 2 \sum_{n=0}^{\infty} (-1)^n e^{\pi i \tau (2n+1)^2/4} \sin((2n+1) z)$$

when this series is summable, and $0$ otherwise. With $q = e^{2 \pi i \tau}$, the factor
$e^{\pi i \tau (2n+1)^2/4}$ is $q^{(2n+1)^2/8}$.

The value $0$ for a non-summable series is a convention; it occurs, for example, at $\tau = 0$
and $z = \pi/2$. The intended object is the Jacobi theta function on the upper half-plane
$\operatorname{Im} \tau > 0$, where the series converges for every $z$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Section 3, Equation (11).

Formalized by `MetaMathlibExt.jacobiThetaOneSineRaw`, a definition declared in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#jacobi-theta-one-sine-raw).

## Jacobi theta function $\theta_1$

For complex numbers $z$ and $\tau$ with
$\operatorname{Im} \tau > 0$, the Jacobi theta function is

$$\theta_1(z \mid \tau) = 2 \sum_{n=0}^{\infty} (-1)^n e^{\pi i \tau (2n+1)^2/4} \sin((2n+1) z).$$

With $q = e^{2 \pi i \tau}$, the factor $e^{\pi i \tau (2n+1)^2/4}$ is $q^{(2n+1)^2/8}$.

On the upper half-plane $\operatorname{Im} \tau > 0$ the series converges for every $z$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Section 3, Equation (11).

Formalized by `MetaMathlibExt.jacobiThetaOneSine`, a definition declared in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#jacobi-theta-one-sine).

## The Jacobi theta function $\theta_1$ vanishes at $z = 0$

For every complex number $\tau$
with $\operatorname{Im} \tau > 0$, the Jacobi theta function satisfies $\theta_1(0 \mid \tau) = 0$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Section 3, Equation (11).

Formalized by `MetaMathlibExt.jacobiThetaOneSine_zero`, a theorem declared in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#jacobi-theta-one-sine-zero).

## Oddness of the Jacobi theta function $\theta_1$

For all complex numbers $z$ and $\tau$
with $\operatorname{Im} \tau > 0$, the Jacobi theta function satisfies
$\theta_1(-z \mid \tau) = -\theta_1(z \mid \tau)$.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Section 3, Equation (11).

Formalized by `MetaMathlibExt.jacobiThetaOneSine_neg`, a theorem declared in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#jacobi-theta-one-sine-neg).

## Sine Lambert series of order sixteen as quotients of theta functions

Let $\tau$ and $z$
be complex numbers with $\operatorname{Im} \tau > 0$ and
$|\operatorname{Im} z| < \pi \operatorname{Im} \tau$, let $q = e^{2 \pi i \tau}$, write
$\theta(w) = \theta_1(w \mid 16\tau)$ for the Jacobi theta function $\theta_1$, and let $\theta'$
be the derivative of $\theta$. Then

$$\sum_{n \ge 1} \frac{q^n - q^{7n} - q^{9n} + q^{15n}}{1 - q^{16n}} \sin 2nz =
\frac{-\theta'(0) \theta(8\pi\tau) \theta(6\pi\tau) \theta(2z)}
{4 \theta(z + \pi\tau) \theta(z - \pi\tau) \theta(z + 7\pi\tau) \theta(z - 7\pi\tau)}$$

and

$$\sum_{n \ge 1} \frac{q^{3n} - q^{5n} - q^{11n} + q^{13n}}{1 - q^{16n}} \sin 2nz =
\frac{-\theta'(0) \theta(2\pi\tau) \theta(8\pi\tau) \theta(2z)}
{4 \theta(z + 3\pi\tau) \theta(z - 3\pi\tau) \theta(z + 5\pi\tau) \theta(z - 5\pi\tau)}.$$

Under these hypotheses the series converge and the denominators do not vanish.

## Sources

- A. Vanitha, Nasser Abdo Saeed Bulkhali, and M. P. Chaudhary, *On a Ramanujan’s Continued Fraction of Order Sixteen and New Eisenstein Series Identities*, INTEGERS 25 (2025), Article A16, Lemma 2 of Section 5, Equations (59)-(60).

Stated but not proved: `MetaMathlibExt.lambert_order_sixteen_sine_eq_jacobiThetaOne` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanOrderSixteenWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html#lambert-order-sixteen-sine-eq-jacobi-the).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's continued fractions of order sixteen](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-continued-fractions-of-order-sixteen)
