---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry24Dougall.ramanujan_part1_ch9_entry24_dougall, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry25Dixon.ramanujan_part1_ch9_entry25_dixon, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9BoundaryLog_eq_log, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9DilogCosTerm_eq_entry24, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9DilogSinTerm_eq_entry24, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.ramanujan_part1_ch9_entry26_ramanujanpi_entry24_terms, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.ramanujan_part1_ch9_entry26_ramanujanpi, MetaMathlibExt.rogersDilog_hoorfarQi_series
statement: formalized
---

# Dilogarithm identities

15 results, 7 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html).

## Entry 24 of Chapter 9 of Ramanujan's notebooks

Let $x, y \in [0, 1]$ and
$\theta, \varphi \in (-\pi, \pi]$ satisfy $x e^{i\theta} + y e^{i\varphi} = 1$. Write
$\ell(t) = \log t$ for $0 < t \le 1$ and $\ell(0) = 0$. Then the four series
$\sum_{k \ge 1} \frac{x^k \cos k\theta}{k^2}$, $\sum_{k \ge 1} \frac{y^k \cos k\varphi}{k^2}$,
$\sum_{k \ge 1} \frac{x^k \sin k\theta}{k^2}$ and $\sum_{k \ge 1} \frac{y^k \sin k\varphi}{k^2}$
converge absolutely, and

$$
\sum_{k \ge 1} \frac{x^k \cos k\theta}{k^2} + \sum_{k \ge 1} \frac{y^k \cos k\varphi}{k^2} =
\frac{\pi^2}{6} - \ell(x) \ell(y) + \theta \varphi,
$$



$$
\sum_{k \ge 1} \frac{x^k \sin k\theta}{k^2} + \sum_{k \ge 1} \frac{y^k \sin k\varphi}{k^2} =
-\varphi \, \ell(x) - \theta \, \ell(y).
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry24Dougall.ramanujan_part1_ch9_entry24_dougall`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry24Dougall.lean, line 1287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry24Dougall.lean#L1287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#ramanujan-part1-ch9-entry24-dougall).

## Entry 25 of Chapter 9 of Ramanujan's notebooks

Let $x, y \in [0, 1]$ and let $\theta$
and $\varphi$ be real numbers with $x e^{i\theta} + y e^{i\varphi} = xy \, e^{i(\theta + \varphi)}$.
Then $1 - x \cos\theta \ne 0$ and $1 - y \cos\varphi \ne 0$. Put
$A_x = 1 - 2x \cos\theta + x^2$, $A_y = 1 - 2y \cos\varphi + y^2$,
$u_x = \arctan \frac{x \sin\theta}{1 - x \cos\theta}$ and
$u_y = \arctan \frac{y \sin\varphi}{1 - y \cos\varphi}$.
Then $A_x > 0$, $A_y > 0$, the four series
$\sum_{k \ge 1} \frac{x^k \cos k\theta}{k^2}$, $\sum_{k \ge 1} \frac{y^k \cos k\varphi}{k^2}$,
$\sum_{k \ge 1} \frac{x^k \sin k\theta}{k^2}$ and $\sum_{k \ge 1} \frac{y^k \sin k\varphi}{k^2}$
converge absolutely, and

$$
\sum_{k \ge 1} \frac{x^k \cos k\theta}{k^2} + \sum_{k \ge 1} \frac{y^k \cos k\varphi}{k^2} =
\frac{\log A_x \log A_y}{8} - \frac{u_x u_y}{2},
$$



$$
\sum_{k \ge 1} \frac{x^k \sin k\theta}{k^2} + \sum_{k \ge 1} \frac{y^k \sin k\varphi}{k^2} =
-\frac{u_y \log A_x}{4} - \frac{u_x \log A_y}{4}.
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry25Dixon.ramanujan_part1_ch9_entry25_dixon`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry25Dixon.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry25Dixon.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#ramanujan-part1-ch9-entry25-dixon).

## The Entry 26 boundary logarithm is the real logarithm

Let $\log$ be the real logarithm,
extended to all of $\mathbb{R}$ by $\log 0 = 0$ and $\log x = \log|x|$ for $x < 0$. For every
real $x$, the boundary logarithm of $x$, defined as $0$ if $x = 0$ and as $\log x$ otherwise,
equals $\log x$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9BoundaryLog_eq_log`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#chapter9-boundary-log-eq-log).

## The Entry 26 and Entry 24 dilogarithm cosine terms agree

For all real $\rho$ and
$\alpha$ and every natural number $j$, the $j$-th term $\rho^{j+1} \cos((j+1)\alpha) / (j+1)^2$ of
the dilogarithm cosine series defined for Entry 26 equals the $j$-th term of the cosine series
defined for Entry 24, which is given by the same formula.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9DilogCosTerm_eq_entry24`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#chapter9-dilog-cos-term-eq-entry24).

## The Entry 26 and Entry 24 dilogarithm sine terms agree

For all real $\rho$ and
$\alpha$ and every natural number $j$, the $j$-th term $\rho^{j+1} \sin((j+1)\alpha) / (j+1)^2$ of
the dilogarithm sine series defined for Entry 26 equals the $j$-th term of the sine series
defined for Entry 24, which is given by the same formula.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.chapter9DilogSinTerm_eq_entry24`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#chapter9-dilog-sin-term-eq-entry24).

## Ramanujan's Landen-type identity in terms of the Entry 24 series

For real $\rho$ and
$\alpha$ and $k \ge 1$ let $c_k(\rho, \alpha) = \rho^k \cos(k\alpha) / k^2$ and
$s_k(\rho, \alpha) = \rho^k \sin(k\alpha) / k^2$ be the terms of the dilogarithm series of
Entry 24, and write $C(\rho, \alpha) = \sum_{j \ge 0} c_{2j+1}(\rho, \alpha)$ and
$S(\rho, \alpha) = \sum_{j \ge 0} s_{2j+1}(\rho, \alpha)$. Let $x, y \in [0, 1]$ and
$\theta, \varphi \in (-\pi, \pi]$ satisfy
$x e^{i\theta} + y e^{i\varphi} + xy\, e^{i(\theta + \varphi)} = 1$. Then the four series
defining $C(x, \theta)$, $C(y, \varphi)$, $S(x, \theta)$ and $S(y, \varphi)$ converge absolutely,
and, where $\log$ is the real logarithm with $\log 0 = 0$,
$C(x, \theta) + C(y, \varphi) = \pi^2/8 - \tfrac12 \log x \log y + \tfrac12 \theta\varphi$ and
$S(x, \theta) + S(y, \varphi) = -\tfrac12 \varphi \log x - \tfrac12 \theta \log y$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.ramanujan_part1_ch9_entry26_ramanujanpi_entry24_terms`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean, line 1817](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean#L1817). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#ramanujan-part1-ch9-entry26-ramanujanpi).

## Ramanujan's Landen-type dilogarithm identity (Entry 26)

For real $\rho$ and $\alpha$
write $C(\rho, \alpha) = \sum_{j \ge 0} \rho^{2j+1} \cos((2j+1)\alpha) / (2j+1)^2$ and
$S(\rho, \alpha) = \sum_{j \ge 0} \rho^{2j+1} \sin((2j+1)\alpha) / (2j+1)^2$. Let
$x, y \in [0, 1]$ and $\theta, \varphi \in (-\pi, \pi]$ satisfy
$x e^{i\theta} + y e^{i\varphi} + xy\, e^{i(\theta + \varphi)} = 1$. Then the four series
defining $C(x, \theta)$, $C(y, \varphi)$, $S(x, \theta)$ and $S(y, \varphi)$ converge absolutely,
and, with the convention $\log 0 = 0$,
$C(x, \theta) + C(y, \varphi) = \pi^2/8 - \tfrac12 \log x \log y + \tfrac12 \theta\varphi$ and
$S(x, \theta) + S(y, \varphi) = -\tfrac12 \varphi \log x - \tfrac12 \theta \log y$.

Proof: Identify the odd series with Legendre's chi function, prove Landen's identity by
differentiation, and extend it to the closed right half-disk by continuity. This follows the route
in Berndt, Part I, Chapter 9, Entry 26, and Lewin, *Polylogarithms and Associated Functions*,
Chapter 1.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 26, p. 273.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry26Ramanujanpi.ramanujan_part1_ch9_entry26_ramanujanpi`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean, line 1876](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry26Ramanujanpi.lean#L1876). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#ramanujan-part1-ch9-entry26-ramanujanpi-2).

## Hoorfar–Qi dilogarithm series

Write $L(x) = \sum_{m \ge 1} x^m/m^2 +
\frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on $[0, 1]$ (with $\log 0 = 0$). For
positive integers $p, q$ and real numbers $\theta, \beta$ with $0 < \theta < 1$ and
$0 < \beta < 1$,

$$
\sum_{n \ge 0} L\left(\frac{\beta(1 - \theta^p)(1 - \theta^q)\theta^n}
{(1 - \beta\theta^{n+p})(1 - \beta\theta^{n+q})}\right) =
\sum_{n=0}^{q-1} L\left(\frac{\beta(1 - \theta^p)\theta^n}{1 - \beta\theta^{n+p}}\right) +
\sum_{n=0}^{p-1} L\left(\frac{1 - \theta^q}{1 - \beta\theta^{n+q}}\right) - p\,L(1 - \theta^q).
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 1, quoting Hoorfar and Qi.

Stated but not proved: `MetaMathlibExt.rogersDilog_hoorfarQi_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-hoorfar-qi-series).

## Bridgeman's dilogarithm series for a positive Pell solution

Write
$L(x) = \sum_{m \ge 1} x^m/m^2 + \frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on
$[0, 1]$ (with $\log 0 = 0$). Let $n$ be a natural number that is not a perfect square, let
$a, b$ be positive rationals with $a^2 - n b^2 = 1$, and put $u = a + b\sqrt{n}$. Define rationals
$a_k, b_k$ by $a_0 = 1$, $b_0 = 0$, $a_{k+1} = a a_k + n b b_k$ and $b_{k+1} = b a_k + a b_k$,
so that $u^k = a_k + b_k\sqrt{n}$. Then

$$
L(1/u^2) = \sum_{k \ge 2} L(b^2/b_k^2),
$$

and if $a$ and $b$ are integers, then for every $k \ge 0$ there is an integer $m$ with $b_k = bm$.

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 3 (3), quoting Bridgeman.

Stated but not proved: `MetaMathlibExt.rogersDilog_pell_positive_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-pell-positive-series).

## Bridgeman's dilogarithm series for a negative Pell solution

Write
$L(x) = \sum_{m \ge 1} x^m/m^2 + \frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on
$[0, 1]$ (with $\log 0 = 0$). Let $n$ be a natural number that is not a perfect square, let
$a, b$ be positive rationals with $a^2 - n b^2 = -1$, and put $u = a + b\sqrt{n}$. Define rationals
$a_k, b_k$ by $a_0 = 1$, $b_0 = 0$, $a_{k+1} = a a_k + n b b_k$ and $b_{k+1} = b a_k + a b_k$,
so that $u^k = a_k + b_k\sqrt{n}$. Then

$$
L(1/u^2) = \sum_{k \ge 1} L\left(\frac{a^2}{n b_{2k}^2}\right) +
\sum_{k \ge 1} L\left(\frac{a^2}{a_{2k+1}^2}\right),
$$

and if $a$ and $b$ are integers, then for every $k \ge 0$ both $b_{2k}/a$ and $a_{2k+1}/a$ are
integers.

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 3 (4), quoting Bridgeman.

Stated but not proved: `MetaMathlibExt.rogersDilog_pell_negative_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-pell-negative-series).

## Sanford's coupled recurrence

Let $a, b$ be real numbers in $(0, 1)$ with $a \ne b$, and
for every natural number $m$ put

$$
x_m = \frac{a(a - b)(1 - b)^m}{a(1 - b)^{m+1} - b(1 - a)^{m+1}}, \qquad
y_m = \frac{b(a - b)(1 - a)^m}{a(1 - b)^{m+1} - b(1 - a)^{m+1}}.
$$

Then for every natural number $n$,

$$
x_{n+1} = \frac{x_n(1 - y_n)}{1 - x_n y_n} \quad\text{and}\quad
y_{n+1} = \frac{y_n(1 - x_n)}{1 - x_n y_n}.
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Lemma 1.

Stated but not proved: `MetaMathlibExt.sanford_coupled_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#sanford-coupled-recurrence).

## Sanford's dilogarithm series identity

Write $L(x) = \sum_{m \ge 1} x^m/m^2 +
\frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on $[0, 1]$ (with $\log 0 = 0$). For
real numbers $a, b \in (0, 1)$ with $a \ne b$,

$$
\sum_{n \ge 0} L\left(\frac{ab(a - b)^2(1 - a)^n(1 - b)^n}
{\left(a(1 - b)^{n+1} - b(1 - a)^{n+1}\right)^2}\right) =
L(a) + L(b) - L\left(\frac{|a - b|}{1 - \min(a, b)}\right).
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 4.

Stated but not proved: `MetaMathlibExt.rogersDilog_sanford_principal_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-sanford-principal-series).

## Sanford's symmetric dilogarithm series

Write $L(x) = \sum_{m \ge 1} x^m/m^2 +
\frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on $[0, 1]$ (with $\log 0 = 0$). For
every real number $a \in (0, 1)$,

$$
\sum_{n \ge 1} L\left(\frac{a^2 \left(\frac{1 - a}{2}\right)^n \left(\frac{1 + a}{2}\right)^n}
{\left(\left(\frac{1 + a}{2}\right)^{n+1} - \left(\frac{1 - a}{2}\right)^{n+1}\right)^2}\right) =
L\left(\frac{1 - a}{1 + a}\right).
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Corollary 1.

Stated but not proved: `MetaMathlibExt.rogersDilog_sanford_symmetric_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-sanford-symmetric-series).

## Sanford's Lucas-sequence dilogarithm series for $Q > 0$

Write
$L(x) = \sum_{m \ge 1} x^m/m^2 + \frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on
$[0, 1]$ (with $\log 0 = 0$). Let $(P, Q)$ be Lucas sequence parameters with $P > 0$, $Q > 0$ and
$D = P^2 - 4Q > 0$, let $U = U(P, Q)$ be the Lucas sequence, and put $\alpha = (P + \sqrt{D})/2$.
Then for every integer $k \ge 1$,

$$
\sum_{n \ge 1} L\left(\frac{U_k^2 Q^{kn}}{U_{k(n+1)}^2}\right) =
L\left(\frac{Q^k}{\alpha^{2k}}\right).
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 5 (8).

Stated but not proved: `MetaMathlibExt.rogersDilog_lucasU_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-lucas-u-series).

## Sanford's Lucas-sequence dilogarithm series for $Q < 0$

Write
$L(x) = \sum_{m \ge 1} x^m/m^2 + \frac{1}{2} \log x \log(1 - x)$ for the Rogers dilogarithm on
$[0, 1]$ (with $\log 0 = 0$). Let $(P, Q)$ be Lucas sequence parameters with $P > 0$ and $Q < 0$,
let $U = U(P, Q)$ be the Lucas sequence and $V = V(P, Q)$ its companion, and put $D = P^2 - 4Q$
and $\alpha = (P + \sqrt{D})/2$. Then for every odd natural number $k$,

$$
\sum_{n \ge 1} L\left(-\frac{V_k^2 Q^{k(2n-1)}}{D\,U_{2kn}^2}\right) +
\sum_{n \ge 1} L\left(\frac{V_k^2 Q^{2kn}}{V_{k(2n+1)}^2}\right) =
L\left(-\frac{Q^k}{\alpha^{2k}}\right).
$$

## Sources

- Chance Sanford, *A Dilogarithm Series and a Generalization of a Theorem of Bridgeman*, INTEGERS 25 (2025), Article A52, Theorem 5 (9).

Stated but not proved: `MetaMathlibExt.rogersDilog_lucasUV_series_of_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RogersDilogarithmSeriesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html#rogers-dilog-lucas-uv-series-of-neg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dilogarithm identities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/dilogarithm-identities)
