---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zeta4.ramanujan_part1_ch7_entry10_zeta4, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8.ramanujan_part1_ch7_entry8, MathlibExt.Analysis.Ramanujan.Part1Ch7.Chapter7PhiArgument, MathlibExt.Analysis.Ramanujan.Part1Ch7.chapter7Phi, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry15Vonstaudtclausen.ramanujan_part1_ch7_entry15_vonstaudtclausen, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry16Kummercongruence.ramanujan_part1_ch7_entry16_kummercongruence, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry17Bernoullipolysymmetry.ramanujan_part1_ch7_entry17_bernoullipolysymmetry, MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry19Zetanegint.ramanujan_part1_ch7_entry19_zetanegint
statement: formalized
proof: formalized
---

# Berndt's power-difference function φᵣ

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html).

## The Entry 10 zeta factor in Bernoulli form

Let $n$ be a positive integer, and for
$z \in \mathbb{C}$ put $B^*(z) = 2\,\Gamma(z + 1)\,\zeta(z) / (2\pi)^z$. Then the functions
$Z(r) = (1 - n^{r+1})\,\zeta(-r)$ and
$B(r) = (n^{r+1} - 1) \sin(\pi r / 2)\, B^*(r + 1) / (r + 1)$ are meromorphic on $\mathbb{C}$,
and $Z(r) = B(r)$ for all $r \in \mathbb{C}$ outside a closed discrete subset of $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 10.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zeta4.ramanujan_part1_ch7_entry10_zeta4`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta4.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta4.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry10-zeta4).

## Bernoulli-number expansion of a Bernoulli-polynomial difference

For every positive
integer $r$ and every $x \in \mathbb{C}$, $\frac{B_{r+1}(x + 1) - B_{r+1}(1)}{r + 1}$ equals
$\frac{1}{r + 1} \sum_{k=0}^{r} \binom{r+1}{k} B_k\, x^{r+1-k} + x^r$, where $B_{r+1}(x)$ is the
Bernoulli polynomial and $B_k$ are the Bernoulli numbers with $B_1 = -\tfrac12$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8.ramanujan_part1_ch7_entry8`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry8).

## Arguments of Berndt's $\varphi_r(x)$

The open interval $(-1, 0)$ of real numbers, that
is, the set of real $x$ with $-1 < x < 0$.

On this interval $x + 1$ lies in $(0, 1)$, so the Hurwitz zeta function at parameter $x + 1$ is
not affected by reduction modulo $1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Chapter7PhiArgument`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Phi.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Phi.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-phi-argument).

## Berndt's function $\varphi_r(x)$ on $(-1, 0)$

For a complex number $r$ and a real number
$x$ with $-1 < x < 0$, $\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$, where $\zeta$ is the
Riemann zeta function and $\zeta(s, a)$ is the Hurwitz zeta function, both analytically continued
in $s$. At $r = -1$, where both have a pole, $\zeta(1)$ and $\zeta(1, x + 1)$ denote the finite
values that the formal definitions assign at the pole.

On this interval $x + 1$ lies in $(0, 1)$, so the Hurwitz zeta function at parameter $x + 1$ is
not affected by reduction modulo $1$.

## Sources

- Bruce C. Berndt, *Ramanujan's Notebooks, Part I*, Chapter 7, equation (2.4), p. 152.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.chapter7Phi`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Phi.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Phi.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-phi).

## A sine series for $\varphi_r(x-1) - \varphi_r(-x)$

For complex $r$ and real $-1 < y < 0$
let $\varphi_r(y) = \zeta(-r) - \zeta(-r, y + 1)$, where $\zeta$ is the Riemann zeta function and
$\zeta(s, a)$ is the Hurwitz zeta function. Let $r$ be a complex number with
$\operatorname{Re} r > -1$ and let $0 < x < 1$. Then the partial sums of
$\sum_{k \ge 1} \sin(2\pi k x) / (2\pi k)^{r+1}$ converge to a limit $L$, and

$$\frac{\varphi_r(x-1) - \varphi_r(-x)}{4\,\Gamma(r+1)} = -\cos\left(\frac{\pi r}{2}\right) L.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 15.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry15Vonstaudtclausen.ramanujan_part1_ch7_entry15_vonstaudtclausen`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry15Vonstaudtclausen.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry15Vonstaudtclausen.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry15-vonstaudtcla).

## A cosine series for $\varphi_r(x-1) + \varphi_r(-x)$

For complex $r$ and real $-1 < y < 0$
let $\varphi_r(y) = \zeta(-r) - \zeta(-r, y + 1)$, where $\zeta$ is the Riemann zeta function and
$\zeta(s, a)$ is the Hurwitz zeta function. Let $r$ be a complex number with
$\operatorname{Re} r > -1$ and let $0 < x < 1$. Then the partial sums of
$\sum_{k \ge 1} \cos(2\pi k x) / (2\pi k)^{r+1}$ converge to a limit $L$, and

$$\frac{\varphi_r(x-1) + \varphi_r(-x) - 2\zeta(-r)}{4\,\Gamma(r+1)}
  = \sin\left(\frac{\pi r}{2}\right) L.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 16.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry16Kummercongruence.ramanujan_part1_ch7_entry16_kummercongruence`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry16Kummercongruence.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry16Kummercongruence.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry16-kummercongru).

## $\varphi_r(-1/4) - \varphi_r(-3/4)$ through the Dirichlet beta function

Let $\chi$ be the
function on $\mathbb{Z}/4\mathbb{Z}$ with $\chi(1) = 1$, $\chi(3) = -1$ and $\chi(0) = \chi(2) = 0$,
let $\beta$ be its Dirichlet $L$-function (analytically continued to $\mathbb{C}$), and let
$E^*(s) = 2\,\Gamma(s)\,\beta(s) / (\pi/2)^s$. For complex $r$ and real $-1 < y < 0$ let
$\varphi_r(y) = \zeta(-r) - \zeta(-r, y + 1)$, where $\zeta$ is the Riemann zeta function and
$\zeta(s, a)$ is the Hurwitz zeta function, and put

$$\ell(r) = \varphi_r(-1/4) - \varphi_r(-3/4), \qquad
  \rho(r) = \frac{2 \cos(\pi r / 2)\, E^*(r+1)}{4^{r+1}}.$$

Then $\beta$ is entire; for every complex $s$ with $\operatorname{Re} s > 0$ the partial sums
$\sum_{k=0}^{N-1} (-1)^k / (2k+1)^s$ tend to $\beta(s)$ as $N \to \infty$; $E^*$, $\ell$ and $\rho$
are meromorphic on $\mathbb{C}$; and $\ell(r) = \rho(r)$ for all $r$ outside a closed discrete
subset of $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry17Bernoullipolysymmetry.ramanujan_part1_ch7_entry17_bernoullipolysymmetry`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry17Bernoullipolysymmetry.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry17Bernoullipolysymmetry.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry17-bernoullipol).

## Ramanujan's functional equation for $\varphi$ at rationals with odd denominator

For
$-1 < x < 0$ and $r \in \mathbb{C}$ let $\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$, where
$\zeta$ is the Riemann zeta function and $\zeta(s, a)$ the Hurwitz zeta function. Let $p$ and $q$
be natural numbers with $0 < p < q$ and $q$ odd, and for $r \in \mathbb{C}$ put
$L(r) = \frac{(2\pi q)^r}{4\,\Gamma(r)} \bigl(\varphi_{r-1}(p/q - 1) - \varphi_{r-1}(-p/q)\bigr)$
and $R(r) = \sin(\pi r/2) \sum_{j=1}^{(q-1)/2} \sin(2\pi j p/q)\, D_j(r)$, where
$D_j(r) = \varphi_{-r}(j/q - 1) - \varphi_{-r}(-j/q)$. Then $L$ and $R$ are meromorphic on
$\mathbb{C}$ and agree outside a closed discrete subset of $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry19Zetanegint.ramanujan_part1_ch7_entry19_zetanegint`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry19Zetanegint.lean, line 778](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry19Zetanegint.lean#L778). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry19-zetanegint).

## Ramanujan's functional equation for $\varphi$ at $-1/3$ and $-2/3$

For $-1 < x < 0$
and $r \in \mathbb{C}$ let $\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$, where $\zeta$ is the
Riemann zeta function and $\zeta(s, a)$ the Hurwitz zeta function. Then the functions
$L(r) = \frac{(6\pi)^r}{2\sqrt{3}\,\Gamma(r)} \bigl(\varphi_{r-1}(-1/3) - \varphi_{r-1}(-2/3)\bigr)$
and $R(r) = \sin(\pi r/2) \bigl(\varphi_{-r}(-1/3) - \varphi_{-r}(-2/3)\bigr)$ of $r \in \mathbb{C}$
are meromorphic on $\mathbb{C}$ and agree outside a closed discrete subset of $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 20.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry20Generalizedbernoullisum.ramanujan_part1_ch7_entry20_generalizedbernoullisum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry20Generalizedbernoullisum.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry20Generalizedbernoullisum.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry20-generalizedb).

## Bernoulli-polynomial form of Berndt's $\varphi_r$

For a natural number $r$ and
$x \in \mathbb{C}$, $P_r(x) = \frac{B_{r+1}(x + 1) - B_{r+1}(1)}{r + 1}$, where $B_{r+1}$ is the
Bernoulli polynomial of degree $r + 1$.

For positive $r$ this polynomial agrees on $-1 < x < 0$ with Berndt's
$\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$, where $\zeta$ is the Riemann zeta function and
$\zeta(s, a)$ the Hurwitz zeta function, and so extends it to all of $\mathbb{C}$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8Bernoullibound.chapter7IntegerPhi`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-integer-phi).

## Bernoulli and zeta expansions of $P_r$, and sums of powers

Let $r$ be a positive integer
and $P_r(x) = \frac{B_{r+1}(x + 1) - B_{r+1}(1)}{r + 1}$, where $B_{r+1}$ is the Bernoulli
polynomial of degree $r + 1$. Then for every $x \in \mathbb{C}$,
$P_r(x) = \frac{1}{r + 1} \sum_{k=0}^{r} \binom{r+1}{k} B_k\, x^{r+1-k} + x^r$, where $B_k$
are the Bernoulli numbers with $B_1 = -\tfrac12$, and
$P_r(x) = \frac{x^{r+1}}{r + 1} + \frac{x^r}{2} - \frac{2}{r + 1} Z_r(x)$, where
$Z_r(x) = \sum_{k=1}^{\lfloor r/2 \rfloor} \binom{r+1}{2k}\, k\, \zeta(1 - 2k)\, x^{r+1-2k}$
and $\zeta$ is the Riemann zeta function. Moreover $P_r(n) = \sum_{k=1}^{n} k^r$ for every
natural number $n$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8Bernoullibound.ramanujan_part1_ch7_entry8_bernoullibound`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry8-bernoulliboun).

## Berndt's $\varphi_r$ as a Bernoulli-polynomial difference for positive integer $r$

Let
$r$ be a positive integer and $-1 < x < 0$. Then $\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$,
where $\zeta$ is the Riemann zeta function and $\zeta(s, a)$ the Hurwitz zeta function, equals
$P_r(x) = \frac{B_{r+1}(x + 1) - B_{r+1}(1)}{r + 1}$, where $B_{r+1}$ is the Bernoulli
polynomial of degree $r + 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8Bernoullibound.chapter7Phi_eq_chapter7IntegerPhi`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-phi-eq-chapter7-integer-phi).

## Bernoulli and zeta expansions of Berndt's $\varphi_r$ on $(-1, 0)$

Let $r$ be a positive
integer and, for $-1 < x < 0$, let $\varphi_r(x) = \zeta(-r) - \zeta(-r, x + 1)$, where $\zeta$
is the Riemann zeta function and $\zeta(s, a)$ the Hurwitz zeta function. Then for every
$-1 < x < 0$,
$\varphi_r(x) = \frac{1}{r + 1} \sum_{k=0}^{r} \binom{r+1}{k} B_k\, x^{r+1-k} + x^r$, where $B_k$
are the Bernoulli numbers with $B_1 = -\tfrac12$, and
$\varphi_r(x) = \frac{x^{r+1}}{r + 1} + \frac{x^r}{2} - \frac{2}{r + 1} Z_r(x)$, where
$Z_r(x) = \sum_{k=1}^{\lfloor r/2 \rfloor} \binom{r+1}{2k}\, k\, \zeta(1 - 2k)\, x^{r+1-2k}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 8, for Berndt's `φ_r` (`chapter7Phi`) on its domain `-1 < x < 0`.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry8Bernoullibound.ramanujan_part1_ch7_entry8_phi`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry8Bernoullibound.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry8-phi).

## Admissible parameters for the power-difference series

A complex number $x$ is admissible
when $j + 1 + x \ne 0$ for every natural number $j$, that is, when $x$ is not one of
$-1, -2, -3, \dots$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.chapter7Admissible`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-admissible-3).

## Terms of the power-difference series

For complex numbers $r$ and $x$ and a natural number
$j$, the $j$-th term is $(j + 1)^r - (j + 1 + x)^r$, where $w^r = e^{r \log w}$ is the principal
power for $w \ne 0$, while $0^r = 0$ for $r \ne 0$ and $0^0 = 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.chapter7PowerDifferenceTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term-4).

## The power-difference series

For complex numbers $r$ and $x$,
$\varphi_r(x) = \sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ (principal powers), where
the sum is taken to be $0$ when the series is not summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.chapter7PowerDifferenceSum`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7PowerDifference.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-sum-2).

## Ramanujan's distribution relation for the power-difference function

Let
$\varphi : \mathbb{C} \times \mathbb{C} \to \mathbb{C}$, written $(r, x) \mapsto \varphi_r(x)$, be
such that for every $x \in \mathbb{C}$ the function $r \mapsto \varphi_r(x)$ is meromorphic on
$\mathbb{C}$, and such that for all $r, x \in \mathbb{C}$ with $\operatorname{Re} r < 0$ the
series $\sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ converges absolutely with sum
$\varphi_r(x)$. Let $n$ be a positive integer and $x \in \mathbb{C}$. Then the functions
$L(r) = \varphi_r(x) - n^r \sum_{k=0}^{n-1} \varphi_r\bigl((x - k)/n\bigr)$ and
$Z(r) = (1 - n^{r+1})\,\zeta(-r)$ are meromorphic on $\mathbb{C}$, and $L(r) = Z(r)$ for all
$r \in \mathbb{C}$ outside a closed discrete subset of $\mathbb{C}$.

Complex powers are principal-branch powers: $w^r = \exp(r \log w)$ for $w \ne 0$, and
$0^r = 0$ for $r \ne 0$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 10.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zeta2.ramanujan_part1_ch7_entry10_zeta2`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta2.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta2.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry10-zeta2).

## Power difference term in Ramanujan's Entry 10

The power-difference term of Ramanujan's Entry 10 is [the $j$-th term of the power-difference series](berndt-s-power-difference-function.md), $(j + 1)^r - (j + 1 + x)^r$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zeta2.chapter7PowerDifferenceTerm`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta2.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zeta2.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term).

## Left side of the corollary to Entry 10

For a function
$\varphi : \mathbb{C} \to \mathbb{C} \to \mathbb{C}$, a natural number $n$ and $r \in \mathbb{C}$,
the left side of the corollary to Entry 10 is $\sum_{k=1}^{n-1} \varphi(r, -k/n)$, the empty sum
$0$ when $n \le 1$. In Berndt's notation, $\varphi(r, x)$ is written $\varphi_r(x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Entry10CorollaryLeft`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-entry10-corollary-left).

## Right side of the corollary to Entry 10

For a natural number $n$ and $r \in \mathbb{C}$,
the right side of the corollary to Entry 10 is $(n - n^{-r})\,\zeta(-r)$, where $n^{-r}$ is the
principal complex power and $\zeta$ is the Riemann zeta function.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Entry10CorollaryRight`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-entry10-corollary-right).

## The points $-k/n$ are admissible

For natural numbers $n$ and $k$ with
$1 \le k \le n - 1$, the point $x = -k/n$ is admissible, that is, $j + 1 + x \neq 0$ for every
natural number $j$.

These are the points at which the left side of the corollary to Entry 10 evaluates $\varphi$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Admissible_neg_div`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-admissible-neg-div).

## The corollary to Entry 10 in the half-plane $\operatorname{Re} r < -1$

Call
$x \in \mathbb{C}$ admissible if $j + 1 + x \neq 0$ for every natural number $j$. Let
$\varphi : \mathbb{C} \to \mathbb{C} \to \mathbb{C}$ be such that, for every $r \in \mathbb{C}$ with
$\operatorname{Re} r < 0$ and every admissible $x$, the series
$\sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ of principal complex powers is
unconditionally summable with sum $\varphi(r, x)$. Then for every natural number $n$ and every
$r \in \mathbb{C}$ with $\operatorname{Re} r < -1$,
$\sum_{k=1}^{n-1} \varphi(r, -k/n) = (n - n^{-r})\,\zeta(-r)$, where $\zeta$ is the Riemann zeta
function.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Entry10CorollaryLeft_eq_right`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-entry10-corollary-left-eq-right).

## Ramanujan's corollary to Entry 10 of Chapter 7

Call $x \in \mathbb{C}$ admissible if
$j + 1 + x \neq 0$ for every natural number $j$. Let
$\varphi : \mathbb{C} \to \mathbb{C} \to \mathbb{C}$ be such that, for every admissible $x$, the
function $r \mapsto \varphi(r, x)$ is entire, and, for every $r \in \mathbb{C}$ with
$\operatorname{Re} r < 0$ and every admissible $x$, the series
$\sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ of principal complex powers is
unconditionally summable with sum $\varphi(r, x)$. Then for every positive integer $n$ the
functions $L(r) = \sum_{k=1}^{n-1} \varphi(r, -k/n)$ and $R(r) = (n - n^{-r})\,\zeta(-r)$, where
$\zeta$ is the Riemann zeta function, are meromorphic on $\mathbb{C}$, and the set of
$r \in \mathbb{C}$ with $L(r) \neq R(r)$ has no accumulation point in $\mathbb{C}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.ramanujan_part1_ch7_entry10_zetaviabernoulli`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry10-zetaviaberno).

## Admissibility in the corollary of Ramanujan's Entry 10

Admissibility in the corollary of Ramanujan's Entry 10 is [admissibility for the power-difference series](berndt-s-power-difference-function.md): $x$ is not one of $-1, -2, -3, \dots$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Admissible`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-admissible).

## Power difference term in the corollary of Entry 10

The power-difference term of the corollary of Ramanujan's Entry 10 is [the $j$-th term of the power-difference series](berndt-s-power-difference-function.md), $(j + 1)^r - (j + 1 + x)^r$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7PowerDifferenceTerm`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term-2).

## Zero is admissible

The point $x = 0$ is admissible: $j + 1 + x \neq 0$ for every natural
number $j$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7Admissible_zero`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-admissible-zero).

## Power-difference terms vanish at exponent zero

For every $x \in \mathbb{C}$ and every
natural number $j$, the power-difference term $(j + 1)^r - (j + 1 + x)^r$ vanishes at $r = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7PowerDifferenceTerm_zero_left`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term-zero-left).

## Power-difference terms vanish at $x = 0$

For every $r \in \mathbb{C}$ and every natural
number $j$, the power-difference term $(j + 1)^r - (j + 1 + x)^r$ vanishes at $x = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry10Zetaviabernoulli.chapter7PowerDifferenceTerm_zero_right`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean, line 693](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry10Zetaviabernoulli.lean#L693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term-zero-righ).

## Convergence and holomorphy of the power-difference series

Let $x$ be an admissible
complex number. For every complex $r$ with $\operatorname{Re} r < 0$ the series
$\sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ (principal powers) is summable, and its
sum $\varphi_r(x)$ is a holomorphic function of $r$ on the half-plane $\operatorname{Re} r < 0$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7, Entry 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry9Bernoulligrowth.ramanujan_part1_ch7_entry9_bernoulligrowth`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry9-bernoulligrow).

## Admissibility in Ramanujan's Entry 9

Admissibility in Ramanujan's Entry 9 is [admissibility for the power-difference series](berndt-s-power-difference-function.md): $x$ is not one of $-1, -2, -3, \dots$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry9Bernoulligrowth.chapter7Admissible`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-admissible-2).

## Power difference term in Ramanujan's Entry 9

The power-difference term of Ramanujan's Entry 9 is [the $j$-th term of the power-difference series](berndt-s-power-difference-function.md), $(j + 1)^r - (j + 1 + x)^r$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry9Bernoulligrowth.chapter7PowerDifferenceTerm`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-term-3).

## Power difference sum in Ramanujan's Entry 9

The power-difference sum of Ramanujan's Entry 9 is [the power-difference series](berndt-s-power-difference-function.md) $\varphi_r(x)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry9Bernoulligrowth.chapter7PowerDifferenceSum`, an abbreviation declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Bernoulligrowth.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#chapter7-power-difference-sum).

## Entire continuations of the power-difference series agree and take Bernoulli values

Let $f$ and $g$ be complex-valued functions of two complex variables $(r, x)$ such that, for every
admissible $x$, both $r \mapsto f(r, x)$ and $r \mapsto g(r, x)$ are entire, and for every
admissible $x$ and every complex $r$ with $\operatorname{Re} r < 0$ the series
$\sum_{j \ge 0} \bigl((j + 1)^r - (j + 1 + x)^r\bigr)$ (principal powers) has sum $f(r, x)$ and
also has sum $g(r, x)$. Then $f(r, x) = g(r, x)$ for every admissible $x$ and every complex $r$,
and for every natural number $m$ and every admissible $x$,
$f(m, x) = g(m, x) = \bigl(B_{m+1}(x + 1) - B_{m+1}(1)\bigr)/(m + 1)$, where $B_n$ is the $n$-th
Bernoulli polynomial.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 7.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch7.Entry9Zetaeven.ramanujan_part1_ch7_entry9_zetaeven`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Zetaeven.lean, line 1736](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch7Entry9Zetaeven.lean#L1736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html#ramanujan-part1-ch7-entry9-zetaeven).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Berndt's power-difference function φᵣ](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/berndt-s-power-difference-function)
