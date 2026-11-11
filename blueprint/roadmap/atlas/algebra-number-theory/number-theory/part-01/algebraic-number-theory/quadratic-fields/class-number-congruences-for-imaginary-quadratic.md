---
declaration: section
origin: cited
lean: MetaMathlibExt.classNumber_sqrt_neg_prime_congr_bernoulli_euler, MetaMathlibExt.eisensteinRealPeriod_eq_beta_gamma, MetaMathlibExt.weierstrassP_eisenstein_lattice, MetaMathlibExt.sl_add_formula, MetaMathlibExt.sl_rescale_int_expansion, MetaMathlibExt.arcSl_subst_sl, MetaMathlibExt.factorial_mul_coeff_sl_isInt, MetaMathlibExt.two_mul_factorial_coeff_inv_sl_mem_int_inv_three
statement: formalized
---

# Class number congruences for imaginary quadratic fields

19 results, 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html).

## Class number congruences for $\mathbb{Q}(\sqrt{-p})$

Let $p > 3$ be a prime and let $K$
be a number field of degree $2$ over $\mathbb{Q}$ that contains a square root of $-p$, with class
number $h$. Let $B_n$ be the Bernoulli numbers, $t/(e^t - 1) = \sum_n B_n t^n/n!$, and $E_n$ the
Euler numbers, $2/(e^t + e^{-t}) = \sum_n E_n t^n/n!$ (so $E_2 = -1$). If $p \equiv 3 \pmod 4$,
then $p$ divides the numerator, in lowest terms, of the rational number $h + 2B_{(p+1)/2}$. If
$p \equiv 1 \pmod 4$, then $p$ divides the integer $2h - E_{(p-1)/2}$.

Since the denominator of $B_{(p+1)/2}$ is prime to $p$ for $p > 3$ (von Staudt–Clausen) and $p$
is odd, these are the congruences $h \equiv -2B_{(p+1)/2} \pmod p$ and
$h \equiv E_{(p-1)/2}/2 \pmod p$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Theorem 1, quoting [5].

Stated but not proved: `MetaMathlibExt.classNumber_sqrt_neg_prime_congr_bernoulli_euler` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#class-number-sqrt-neg-prime-congr-bernou).

## Beta and Gamma values of the real Eisenstein period

The real number
$\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$ satisfies
$\varpi_1 = \frac13 B(\frac13, \frac13) = \frac{\Gamma(1/3)^3}{2\pi\sqrt3}
= \frac{2^{1/3}}{3\sqrt3} B(\frac16, \frac12)$, where $B$ is the Beta function.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 1.

Stated but not proved: `MetaMathlibExt.eisensteinRealPeriod_eq_beta_gamma` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-real-period-eq-beta-gamma).

## The Weierstrass function of the Eisenstein lattice

Let $\rho = e^{2\pi i/3}$, let
$\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, and let $\wp$ be the Weierstrass function of the
lattice $\Lambda = \varpi_1 \mathbb{Z} + \varpi_1 \rho \mathbb{Z}$, with derivative $\wp'$. Then for
every $u \in \mathbb{C} \setminus \Lambda$:
(a) $\wp(\rho u) = \rho\,\wp(u)$, $\wp(-u) = \wp(u)$, $\wp'(\rho u) = \wp'(u)$ and
$\wp'(-u) = -\wp'(u)$;
(b) $\wp(\bar u) = \overline{\wp(u)}$ and $\wp'(\bar u) = \overline{\wp'(u)}$;
(c) $\wp'(u)^2 = 4\wp(u)^3 - 27$.
Moreover, (d) $\wp(\varpi_1/3) = 3$ and $\wp((1 - \rho)\varpi_1/3) = 0$, and
(e) $\wp'(\varpi_1/3) = -9$ and $\wp'((1 - \rho)\varpi_1/3) = -3\sqrt{3}\,i$.

By (b), $\wp$ and $\wp'$ take real values at real points off $\Lambda$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 2.

Stated but not proved: `MetaMathlibExt.weierstrassP_eisenstein_lattice` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#weierstrass-p-eisenstein-lattice).

## Addition formula for the Eisenstein function Sl

Let $\mathrm{Sl}, \mathrm{Cl}$ be formal
power series in $\mathbb{Q}[[u]]$ with $\mathrm{Sl}' = \mathrm{Cl}^2$,
$\mathrm{Cl}' = -\mathrm{Sl}^2$, $\mathrm{Sl}(0) = 0$ and $\mathrm{Cl}(0) = 1$. In the ring
$\mathbb{Q}[[u, v]]$ of formal power series in two variables,

$$\mathrm{Sl}(u + v)\bigl(\mathrm{Sl}(u)\,\mathrm{Cl}(v)^2 - \mathrm{Sl}(v)\,\mathrm{Cl}(u)^2\bigr)
= \mathrm{Sl}(u)^2\,\mathrm{Cl}(v) - \mathrm{Sl}(v)^2\,\mathrm{Cl}(u),$$

and there is a power series $F \in \mathbb{Q}[[x, y]]$, with every coefficient in $\mathbb{Z}[1/3]$
and no terms of total degree below $4$, such that
$\mathrm{Sl}(u + v) = \mathrm{Sl}(u) + \mathrm{Sl}(v) + F(\mathrm{Sl}(u), \mathrm{Sl}(v))$.

The four conditions determine $\mathrm{Sl}$ and $\mathrm{Cl}$ uniquely: they are the Taylor series
at $0$ of the Eisenstein elliptic functions of the source. The first identity is the addition
formula $\mathrm{Sl}(u + v) = \frac{\mathrm{Sl}(u)^2 \mathrm{Cl}(v) - \mathrm{Sl}(v)^2
\mathrm{Cl}(u)}{\mathrm{Sl}(u) \mathrm{Cl}(v)^2 - \mathrm{Sl}(v) \mathrm{Cl}(u)^2}$ with its
denominator cleared. The arXiv version of the source (arXiv:2204.04425) has the exponent $2$ in
place of $4$; every term of $\mathrm{Sl}(u + v) - \mathrm{Sl}(u) - \mathrm{Sl}(v)$ has total
degree $\equiv 1 \pmod 3$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 4.

Stated but not proved: `MetaMathlibExt.sl_add_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#sl-add-formula).

## Sl(ru) as a power series in Sl(u)

Let $\mathrm{Sl}, \mathrm{Cl}$ be formal power series
in $\mathbb{Q}[[u]]$ with $\mathrm{Sl}' = \mathrm{Cl}^2$, $\mathrm{Cl}' = -\mathrm{Sl}^2$,
$\mathrm{Sl}(0) = 0$ and $\mathrm{Cl}(0) = 1$, and let $r$ be an integer. Then there is a power
series $g \in \mathbb{Q}[[x]]$, with every coefficient in $\mathbb{Z}[1/3]$, such that
$\mathrm{Sl}(ru) = r\,\mathrm{Sl}(u) + \mathrm{Sl}(u)^4\,g(\mathrm{Sl}(u)^3)$. If moreover
$r \ne 0$, there is a power series $h \in \mathbb{Q}[[x]]$, each coefficient of which has the form
$a/(r^j 3^k)$ with $a \in \mathbb{Z}$ and $j, k \ge 0$, such that
$r\,\mathrm{Sl}(u) = \mathrm{Sl}(ru) + r\,\mathrm{Sl}(u)^3\,\mathrm{Sl}(ru)\,h(\mathrm{Sl}(u)^3)$.

Dividing by $r\,\mathrm{Sl}(u)\,\mathrm{Sl}(ru)$, the second identity reads
$\mathrm{Sl}(ru)^{-1} = (r\,\mathrm{Sl}(u))^{-1} + \mathrm{Sl}(u)^2\,h(\mathrm{Sl}(u)^3)$ in the
Laurent series in $u$. The four conditions determine $\mathrm{Sl}$ and $\mathrm{Cl}$ uniquely:
they are the Taylor series at $0$ of the Eisenstein elliptic functions of the source.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 5.

Stated but not proved: `MetaMathlibExt.sl_rescale_int_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#sl-rescale-int-expansion).

## Power series inverse of $\mathrm{Sl}$

Let $S, C \in \mathbb{Q}[[u]]$ be formal power
series with $S' = C^2$, $C' = -S^2$, $S(0) = 0$ and $C(0) = 1$. Then

$$\sum_{n \ge 0} (-1)^n \binom{-2/3}{n} \frac{S^{3n+1}}{3n+1} = u$$

in $\mathbb{Q}[[u]]$, where $\binom{-2/3}{n} = \frac{1}{n!} \prod_{j=0}^{n-1} (-2/3 - j)$ is the
generalized binomial coefficient.

These conditions determine $S$ and $C$ uniquely: they are the Taylor series at $0$ of the
Eisenstein elliptic functions $\mathrm{Sl}$ and $\mathrm{Cl}$. The statement says that
$\mathrm{ArcSl}(t) = \sum_{n \ge 0} (-1)^n \binom{-2/3}{n} t^{3n+1}/(3n+1)$ is the inverse of
$\mathrm{Sl}$ near $0$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Corollary 1.

Stated but not proved: `MetaMathlibExt.arcSl_subst_sl` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#arc-sl-subst-sl).

## The Hurwitz-normalized coefficients of Sl are integers

Let $\mathrm{Sl}, \mathrm{Cl}$ be
formal power series in $\mathbb{Q}[[u]]$ with $\mathrm{Sl}' = \mathrm{Cl}^2$,
$\mathrm{Cl}' = -\mathrm{Sl}^2$, $\mathrm{Sl}(0) = 0$ and $\mathrm{Cl}(0) = 1$, and let $C_n$ be
the coefficient of $u^n$ in $\mathrm{Sl}$. Then $(3m + 1)!\,C_{3m+1}$ is an integer for every
$m \ge 0$.

The four conditions determine $\mathrm{Sl}$ and $\mathrm{Cl}$ uniquely: they are the Taylor series
at $0$ of the Eisenstein elliptic functions of the source.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 7.

Stated but not proved: `MetaMathlibExt.factorial_mul_coeff_sl_isInt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#factorial-mul-coeff-sl-is-int).

## The Hurwitz-normalized coefficients of 1/Sl

Let $\mathrm{Sl}, \mathrm{Cl}$ be formal power
series in $\mathbb{Q}[[u]]$ with $\mathrm{Sl}' = \mathrm{Cl}^2$, $\mathrm{Cl}' = -\mathrm{Sl}^2$,
$\mathrm{Sl}(0) = 0$ and $\mathrm{Cl}(0) = 1$. Write $\mathrm{Sl}(u) = u\,S_0(u)$ with
$S_0 \in \mathbb{Q}[[u]]$, and let $D_n$ be the coefficient of $u^{n+1}$ in $S_0^{-1}$, so that
$1/\mathrm{Sl}(u) = 1/u + \sum_{n \ge 0} D_n u^n$. Then for every $m \ge 0$ the number
$2\,(6m + 2)!\,D_{6m+2}$ lies in $\mathbb{Z}[1/3]$, that is, it equals $a/3^k$ for some
$a \in \mathbb{Z}$ and $k \ge 0$.

The four conditions determine $\mathrm{Sl}$ and $\mathrm{Cl}$ uniquely: they are the Taylor series
at $0$ of the Eisenstein elliptic functions of the source.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 8.

Stated but not proved: `MetaMathlibExt.two_mul_factorial_coeff_inv_sl_mem_int_inv_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#two-mul-factorial-coeff-inv-sl-mem-int-i).

## Denominators of the Hurwitz-type numbers of Sl

Let $\mathrm{Sl}, \mathrm{Cl}$ be formal
power series in $\mathbb{Q}[[u]]$ with $\mathrm{Sl}' = \mathrm{Cl}^2$,
$\mathrm{Cl}' = -\mathrm{Sl}^2$, $\mathrm{Sl}(0) = 0$ and $\mathrm{Cl}(0) = 1$. Let $C_n$ be the
coefficient of $u^n$ in $\mathrm{Sl}$; write $\mathrm{Sl}(u) = u\,S_0(u)$ with
$S_0 \in \mathbb{Q}[[u]]$ and let $D_n$ be the coefficient of $u^{n+1}$ in $S_0^{-1}$, so that
$1/\mathrm{Sl}(u) = 1/u + \sum_{n \ge 0} D_n u^n$. Let $\ell$ be a prime and put
$k = 2(\ell - 1)/3$. If $\ell \equiv 7 \pmod 9$, then $\ell$ does not divide the denominator of
$C_k$ in lowest terms; if $\ell \equiv 4 \pmod 9$, then $\ell$ does not divide the denominator of
$D_k$ in lowest terms.

The four conditions determine $\mathrm{Sl}$ and $\mathrm{Cl}$ uniquely: they are the Taylor series
at $0$ of the Eisenstein elliptic functions of the source.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Theorem 3, first sentence.

Stated but not proved: `MetaMathlibExt.sl_hurwitz_numbers_den_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#sl-hurwitz-numbers-den-coprime).

## Identities for the Eisenstein elliptic functions $\varphi$ and $\psi$

Let
$\rho = e^{2\pi i/3}$, let $\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, and let $\wp$ be the
Weierstrass function of the lattice spanned by $\varpi_1$ and $\varpi_1\rho$. Put
$\varphi(u) = 6\wp(\varpi_1 u)/(9 + \wp'(\varpi_1 u))$ and
$\psi(u) = (\wp'(\varpi_1 u) - 9)/(\wp'(\varpi_1 u) + 9)$. For every $u \in \mathbb{C}$ with
$\varpi_1 u$ off the lattice and $\wp'(\varpi_1 u) \ne -9$: $\varphi(\rho u) = \rho\varphi(u)$,
$\psi(\rho u) = \psi(u)$, $\varphi(\bar u) = \overline{\varphi(u)}$,
$\psi(\bar u) = \overline{\psi(u)}$, the functions $\varphi$ and $\psi$ are complex differentiable
at $u$ with $\varphi'(u) = -3\varpi_1 \psi(u)^2$ and $\psi'(u) = 3\varpi_1 \varphi(u)^2$, and
$\varphi(u)^3 + \psi(u)^3 = 1$. As $u \to 0$ with $u \ne 0$, $\varphi(u) \to 0$ and
$\psi(u) \to 1$. For every $u$ with $\varpi_1 u$ off the lattice and $\wp'(\varpi_1 u)^2 \ne 81$:
$\varphi(-u) = -\varphi(u)/\psi(u)$ and $\psi(-u) = \psi(u)^{-1}$, and if moreover
$\wp(\varpi_1 u) \ne 0$, then $\varphi(u)^{-1} + \varphi(-u)^{-1} = 3/\wp(\varpi_1 u)$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 3, parts (d)-(g).

Stated but not proved: `MetaMathlibExt.eisensteinPhiPsi_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-phi-psi-properties).

## $\mathrm{Sl}$ and $\mathrm{ArcSl}$ are inverse on the real segment

Let
$\rho = e^{2\pi i/3}$, let $\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, let $\wp$ be the
Weierstrass function of the lattice spanned by $\varpi_1$ and $\varpi_1\rho$, and put
$\varphi(u) = 6\wp(\varpi_1 u)/(9 + \wp'(\varpi_1 u))$. For real $x$ put
$\mathrm{Sl}(x) = \varphi(x/(-3\varpi_1))$, and for real $t$ put
$\mathrm{ArcSl}(t) = \int_0^t (1 - s^3)^{-2/3}\,ds$, so that $\varpi_1 = \mathrm{ArcSl}(1)$. Then:
for every $t \in [0, 1]$ the series $\sum_{n \ge 0} (-1)^n \binom{-2/3}{n} t^{3n+1}/(3n+1)$ has
sum $\mathrm{ArcSl}(t)$, where $\binom{-2/3}{n}$ is the generalized binomial coefficient; for
every $x \in [0, \varpi_1]$, $\mathrm{Sl}(x)$ is a real number $s \in [0, 1]$ with
$\mathrm{ArcSl}(s) = x$; and for every $t \in [0, 1]$, $\mathrm{ArcSl}(t) \in [0, \varpi_1]$ and
$\mathrm{Sl}(\mathrm{ArcSl}(t)) = t$.

At $x = 0$, where $\wp$ has a pole, the values $\wp(0)$ and $\wp'(0)$ are taken to be $0$, so
$\mathrm{Sl}(0) = 0$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 6.

Stated but not proved: `MetaMathlibExt.eisensteinSl_inverse_arcSl` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-sl-inverse-arc-sl).

## Jacobi sums of the quadratic and the cubic residue character

Let $K$ be a number field
generated over $\mathbb{Q}$ by a primitive cube root of unity, with ring of integers
$\mathcal{O}_K$. Let $\mu \in \mathcal{O}_K$ with $\mu \equiv 1 \pmod 3$, and let $p$ be a prime
such that the norm of $\mu$ from $\mathcal{O}_K$ to $\mathbb{Z}$ is $p$. Let
$\chi : \mathbb{Z}/p\mathbb{Z} \to \mathcal{O}_K$ be a multiplicative character with
$\chi(t) \equiv t^{(p-1)/3} \pmod{\mu}$ for every integer $t$ (the cubic residue character modulo
$\mu$), and let $\phi$ be the quadratic character of $\mathbb{Z}/p\mathbb{Z}$, with values in
$\{0, \pm 1\} \subset \mathcal{O}_K$. Writing
$J(\alpha, \beta) = \sum_{t \in \mathbb{Z}/p\mathbb{Z}} \alpha(t)\,\beta(1 - t)$, one has
$J(\phi, \chi) = \chi(4)\,J(\chi, \chi)$ and $J(\chi, \chi) = -\mu$.

The source states this for arbitrary characters $\phi$ and $\chi$ of $\mathbb{F}_p^\times$; the
identity holds for the quadratic $\phi$ and the cubic residue character $\chi$ modulo $\mu$, the
characters of the lemma it cites (Ireland-Rosen, Chap. 18, §3 and Chap. 9, §4).

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 13, part (a).

Stated but not proved: `MetaMathlibExt.jacobiSum_quadraticChar_cubicResidueChar` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#jacobi-sum-quadratic-char-cubic-residue).

## The Jacobi sum of the quadratic and a cubic character of a field with $q^2$ elements

Let
$q$ be an odd prime with $q \equiv 2 \pmod 3$, let $F$ be a finite field with $q^2$ elements, let
$\phi$ be the quadratic character of $F$, and let $\chi : F \to \mathbb{C}$ be a multiplicative
character of order $3$, that is, $\chi^3 = 1$ and $\chi \ne 1$ (characters take the value $0$ at
$0$). Then the Jacobi sum $J(\phi, \chi) = \sum_{t \in F} \phi(t)\,\chi(1 - t)$ equals $q$.

The source states this for arbitrary characters $\phi$ and $\chi$ of $F^\times$; the identity
holds for the quadratic $\phi$ and a $\chi$ of order $3$, the characters of the sources it cites.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 13, part (b).

Stated but not proved: `MetaMathlibExt.jacobiSum_quadraticChar_cubicChar_card_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#jacobi-sum-quadratic-char-cubic-char-car).

## Cubic reciprocity

Let $K$ be the cyclotomic field generated by a primitive cube root of
unity, with ring of integers $\mathcal{O}_K$, and let $\zeta \in \mathcal{O}_K$ be a primitive cube
root of unity. Let $\lambda_1, \lambda_2 \in \mathcal{O}_K$ be primes with
$\lambda_1 \equiv \lambda_2 \equiv 1 \pmod 3$, and write $N$ for the absolute value of the norm
from $\mathcal{O}_K$ to $\mathbb{Z}$. If $\omega_1, \omega_2 \in \{1, \zeta, \zeta^2\}$ satisfy
$\lambda_1^{(N\lambda_2 - 1)/3} \equiv \omega_1 \pmod{\lambda_2}$ and
$\lambda_2^{(N\lambda_1 - 1)/3} \equiv \omega_2 \pmod{\lambda_1}$, then $\omega_1 = \omega_2$.

Here $\mathcal{O}_K = \mathbb{Z}[\zeta]$ and $N\lambda_i \equiv 1 \pmod 3$, so the exponents are
integers. In terms of cubic residue symbols the statement is
$(\lambda_1/\lambda_2)_3 = (\lambda_2/\lambda_1)_3$; when $\lambda_1 = \lambda_2$ no such
$\omega_1$ exists and the statement is empty.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 13, part (c).

Stated but not proved: `MetaMathlibExt.cubicResidueSymbol_reciprocity` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#cubic-residue-symbol-reciprocity).

## Point counts of $y^2 + \lambda y = x^3$ modulo primes of $\mathbb{Z}(\zeta_3)$

Let $K$
be the cyclotomic field generated by a primitive cube root of unity, with ring of integers
$\mathcal{O}_K$, let $\zeta \in \mathcal{O}_K$ be a primitive cube root of unity, and write $N$
and $\mathrm{Tr}$ for the norm and trace from $\mathcal{O}_K$ to $\mathbb{Z}$. Let
$\lambda \in \mathcal{O}_K$ satisfy $\lambda \equiv 1 \pmod 3$ with $N\lambda = \ell$ a prime. For
a principal ideal $I$ of $\mathcal{O}_K$, let $n(I)$ be the number of pairs
$(x, y) \in (\mathcal{O}_K/I)^2$ with $y^2 + \lambda y = x^3$. Then:
(d) if $\mu \in \mathcal{O}_K$ with $\mu \ne \lambda$ and $\mu \equiv 1 \pmod 3$ has prime norm
$N\mu = p$, and $\omega \in \{1, \zeta, \zeta^2\}$ satisfies
$\mu^{(\ell-1)/3} \equiv \omega \pmod \lambda$, then
$n((\mu)) + 1 = p + 1 - \mathrm{Tr}(\omega^2\mu)$;
(e) if $q$ is a prime with $q \equiv 2 \pmod 3$, and $\omega \in \{1, \zeta, \zeta^2\}$ satisfies
$q^{(\ell-1)/3} \equiv \omega \pmod \lambda$, then $n((q)) + 1 = q^2 + 1 + q\,\mathrm{Tr}(\omega)$.

The curve $y^2 + \lambda y = x^3$ is a global minimal model of
$E_\lambda : y^2 = x^3 + \lambda^2/4$, and $\mathcal{O}_K/(\mu) \cong \mathbb{F}_p$,
$\mathcal{O}_K/(q) \cong \mathbb{F}_{q^2}$, so $n + 1$ counts the points of $E_\lambda$ over these
fields, including the point at infinity. With $\chi_\lambda(a) = \omega$ the cubic residue symbol
$(a/\lambda)_3$, the right-hand sides are
$p + 1 - (\chi_\lambda(\mu)\bar\mu + \overline{\chi_\lambda(\mu)\bar\mu})$ and
$q^2 + 1 + q(\chi_\lambda(q) + \overline{\chi_\lambda(q)})$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 14, parts (d), (e).

Stated but not proved: `MetaMathlibExt.eisensteinTwist_card_points` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-twist-card-points).

## Torsion of $y^2 = x^3 + \lambda^2/4$ over $\mathbb{Q}(\zeta_3)$

Let $K$ be the cyclotomic
field generated by a primitive cube root of unity, with ring of integers $\mathcal{O}_K$, and let
$\lambda \in \mathcal{O}_K$ satisfy $\lambda \equiv 1 \pmod 3$, with norm from $\mathcal{O}_K$ to
$\mathbb{Z}$ a prime number. Let $E$ be the Weierstrass curve $y^2 = x^3 + \lambda^2/4$ over $K$,
with point at infinity $O$. Then a point $P \in E(K)$ has finite order if and only if $3P = O$;
$3P = O$ if and only if $P$ is $O$, $(0, \lambda/2)$ or $(0, -\lambda/2)$; and $E(K)$ has exactly
$3$ points of finite order.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 14, part (f).

Stated but not proved: `MetaMathlibExt.eisensteinTwist_torsion` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-twist-torsion).

## Congruence for the square of $\tilde\lambda$

Let $\rho = e^{2\pi i/3}$, let
$\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, let $\wp$ be the Weierstrass function of the lattice
spanned by $\varpi_1$ and $\varpi_1\rho$, and put
$\varphi(u) = 6\wp(\varpi_1 u)/(9 + \wp'(\varpi_1 u))$. Let $a, b$ be integers with $a \equiv 1$ and
$b \equiv 0 \pmod 3$ such that $\ell = a^2 - ab + b^2$ is prime, and put $\lambda = a + b\rho$.
Let $r_0 \in \mathbb{Z}/\ell$ satisfy $a + b r_0 = 0$, and let
$\chi : \mathbb{Z}/\ell \to \mathbb{C}$ be such that for every $t \ne 0$ there is
$j \in \mathbb{N}$ with $\chi(t) = \rho^j$ and $t^{(\ell-1)/3} = r_0^j$. Put
$\Lambda = \varphi(1/\lambda)$ and $\tilde\lambda = \prod \varphi(r/\lambda)$, the product
over the integers $0 < r < \ell$ with $\chi(r) = 1$. Then
$\tilde\lambda^2 - \Lambda^{2(\ell-1)/3} = \Lambda^{2(\ell-1)/3 + 1} x$ for some algebraic
integer $x$ in the subfield $\mathbb{Q}(\rho, \Lambda)$ of $\mathbb{C}$.

Here $\lambda\bar\lambda = \ell$, $\rho \mapsto r_0$ identifies $\mathbb{Z}[\rho]/(\lambda)$ with
$\mathbb{Z}/\ell$, and $\chi$ is the cubic residue character modulo $\lambda$. The statement is
the congruence $\tilde\lambda^2 \equiv \Lambda^{2(\ell-1)/3}$ modulo $\Lambda^{2(\ell-1)/3 + 1}$
in the ring of integers of $\mathbb{Q}(\rho, \Lambda)$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 10.

Stated but not proved: `MetaMathlibExt.eisensteinLambdaTilde_sq_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#eisenstein-lambda-tilde-sq-congr).

## Integrality of the elliptic Gauss sum

Let $\rho = e^{2\pi i/3}$, let
$\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, let $\wp$ be the Weierstrass function of the lattice
$\varpi_1 \mathbb{Z} + \varpi_1 \rho \mathbb{Z}$, and let
$\varphi(u) = 6\wp(\varpi_1 u)/(9 + \wp'(\varpi_1 u))$. Let $a, b$ be integers with
$a \equiv 1 \pmod 3$ and $b \equiv 0 \pmod 3$ such that $\ell = a^2 - ab + b^2$ is a prime with
$\ell \equiv 7 \pmod 9$ or $\ell \equiv 4 \pmod 9$, and put $\lambda = a + b\rho$. Let
$r_0 \in \mathbb{Z}/\ell\mathbb{Z}$ satisfy $a + b r_0 = 0$, and let
$\chi_\lambda : \mathbb{Z}/\ell\mathbb{Z} \to \mathbb{C}$ be a function such that for every
$t \ne 0$ there is an integer $k \ge 0$ with $\chi_\lambda(t) = \rho^k$ and
$t^{(\ell-1)/3} = r_0^k$. Let $f = \varphi$ if $\ell \equiv 7 \pmod 9$ and $f = 1/\varphi$ if
$\ell \equiv 4 \pmod 9$, and let

$$G = \frac{1}{3} \sum_{r=1}^{\ell-1} \chi_\lambda(r)\,f(r/\lambda).$$

Then $G$ is an algebraic integer lying in the subfield $\mathbb{Q}(\rho, \varphi(1/\lambda))$ of
$\mathbb{C}$, and $G$ equals the sum of $f(r/\lambda)$ over the integers $1 \le r \le \ell - 1$ with
$\chi_\lambda(r) = 1$.

Here $\chi_\lambda$ is the cubic residue character modulo $\lambda$, read through the isomorphism
$\mathbb{Z}[\rho]/(\lambda) \cong \mathbb{Z}/\ell\mathbb{Z}$ that sends $\rho$ to $r_0$; the
integers $1, \dots, \ell - 1$ represent $(\mathbb{Z}[\rho]/(\lambda))^\times$, so $G$ is the
elliptic Gauss sum $G_\lambda(\chi_\lambda, f)$ of the source.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 11.

Stated but not proved: `MetaMathlibExt.ellipticGaussSum_mem_integers_eq_sum_ker` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#elliptic-gauss-sum-mem-integers-eq-sum-k).

## Congruences for $|\alpha_\lambda|^2$

Let $\rho = e^{2\pi i/3}$, let
$\varpi_1 = \int_0^1 (1 - t^3)^{-2/3}\,dt$, let $\wp$ be the Weierstrass function of the lattice
spanned by $\varpi_1$ and $\varpi_1\rho$, and put
$\varphi(u) = 6\wp(\varpi_1 u)/(9 + \wp'(\varpi_1 u))$. Put
$\mathrm{Sl}(u) = \varphi(u/(-3\varpi_1))$. Let $a, b$ be integers with $a \equiv 1$ and
$b \equiv 0 \pmod 3$ such that $\ell = a^2 - ab + b^2$ is prime, and put $\lambda = a + b\rho$.
Let $r_0 \in \mathbb{Z}/\ell$ satisfy $a + b r_0 = 0$, and let
$\chi : \mathbb{Z}/\ell \to \mathbb{C}$ be such that for every $t \ne 0$ there is
$j \in \mathbb{N}$ with $\chi(t) = \rho^j$ and $t^{(\ell-1)/3} = r_0^j$. Let $f = \varphi$ if
$\ell \equiv 7 \pmod 9$ and $f = 1/\varphi$ otherwise, and put
$G = \frac13 \sum_{0 < r < \ell} \chi(r) f(r/\lambda)$,
$\tilde\lambda = \prod_{0 < r < \ell,\ \chi(r) = 1} \varphi(r/\lambda)$ and
$\alpha = G/\tilde\lambda^2$. Let $k = 2(\ell-1)/3$, and let $C$ and $D$ be the coefficients of
$u^k$ in the Taylor expansions at $0$ of $\mathrm{Sl}(u)$ and of $\mathrm{Sl}(u)^{-1} - u^{-1}$.
If $\ell \equiv 7 \pmod 9$, there are integers $m, m'$ prime to $\ell$ with
$m(|\alpha|^2 - (\overline{\chi(3)}\,C)^2/9) \in \lambda\mathbb{Z}[\rho]$ and
$m'(|\alpha|^2 - (3^{(\ell-7)/6} C)^2) \in \ell\mathbb{Z}$. If $\ell \equiv 4 \pmod 9$, there are
integers $m, m'$ prime to $\ell$ with $m(|\alpha|^2 - (\chi(3) D)^2/9) \in \lambda\mathbb{Z}[\rho]$
and $m'(|\alpha|^2 - (3^{(\ell-4)/3} D)^2) \in \ell\mathbb{Z}$.

Here $\lambda\bar\lambda = \ell$, $\rho \mapsto r_0$ identifies $\mathbb{Z}[\rho]/(\lambda)$ with
$\mathbb{Z}/\ell$, $\chi$ is the cubic residue character $\chi_\lambda$ modulo $\lambda$, $G$ is
the elliptic Gauss sum $G_\lambda(\chi_\lambda, f)$ and $\alpha = \alpha_\lambda$ its coefficient,
so the statement gives congruences modulo $\lambda$ and modulo $\ell$. At $u = 0$, where $\wp$ has
a pole, both functions take the value $0$, their limit there, and $C$, $D$ are their $k$-th
derivatives at $0$ divided by $k!$.

## Sources

- Akihiro Goto, *Congruence Relations Connecting Tate-Shafarevich Groups with Bernoulli-Hurwitz Numbers by Elliptic Gauss Sums in the Eisenstein Integers Case*, INTEGERS 26 (2026), Article A112, Lemma 12.

Stated but not proved: `MetaMathlibExt.ellipticGaussSum_coeff_normSq_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ClassNumberBernoulliEulerCongruenceWanted.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html#elliptic-gauss-sum-coeff-norm-sq-congr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Class number congruences for imaginary quadratic fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/class-number-congruences-for-imaginary-quadratic)
