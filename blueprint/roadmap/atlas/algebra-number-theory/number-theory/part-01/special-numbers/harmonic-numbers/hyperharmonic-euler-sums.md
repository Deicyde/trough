---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedHyperharmonic, MetaMathlibExt.generalizedHyperharmonic_of_lt, MetaMathlibExt.generalizedHyperharmonic_zero_zero, MetaMathlibExt.generalizedHyperharmonic_one_zero, MetaMathlibExt.generalizedHyperharmonic_one_one, MetaMathlibExt.hyperharmonicEulerSum, MetaMathlibExt.hyperharmonicEulerSum_eq_tsum, MetaMathlibExt.oddMultipleHarmonic
statement: formalized
---

# Hyperharmonic Euler sums

38 results, 15 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html).

## Generalized hyperharmonic numbers

For natural numbers $n$ and $k$ and a complex number
$r$, the generalized hyperharmonic number $H_n^{[r]}(k)$ is $0$ when $k > n$; when $k \le n$ it is
the elementary symmetric polynomial of degree $n - k$ in $r, r + 1, \ldots, r + n - 1$ divided by
$n!$, that is,

$$H_n^{[r]}(k) = \frac{1}{n!} \sum_{0 \le j_1 < \cdots < j_{n-k} < n} \prod_{i=1}^{n-k} (r + j_i).$$

The source defines $H_n^{[r]}(k)$ in (2.4) by $(-1)^k k! \, H_n^{[r]}(k) = D_x^k \binom{n+r-x-1}{n}$
at $x = 0$, where $D_x^k$ is the $k$-th derivative in $x$; the explicit form above follows from it.
For $r = 1$ it is the depth-$k$ multiple harmonic number, and for
$r \notin \{0, -1, \ldots, 1 - n\}$ it equals
$\binom{n+r-1}{n} \sum_{1 \le i_1 < \cdots < i_k \le n} \prod_{j=1}^{k} 1/(i_j + r - 1)$,
see (2.10).

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Section 2, (2.4) and (2.10).

Formalized by `MetaMathlibExt.generalizedHyperharmonic`, a definition declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generalized-hyperharmonic).

## Generalized hyperharmonic numbers vanish for $k > n$

For all natural numbers $n$ and $k$
with $n < k$ and every complex number $r$, the generalized hyperharmonic number $H_n^{[r]}(k)$
equals $0$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Section 2, (2.4).

Formalized by `MetaMathlibExt.generalizedHyperharmonic_of_lt`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generalized-hyperharmonic-of-lt).

## Generalized hyperharmonic numbers with both indices zero

For every complex number $r$,
the generalized hyperharmonic number $H_0^{[r]}(0)$ equals $1$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Section 2, (2.4).

Formalized by `MetaMathlibExt.generalizedHyperharmonic_zero_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generalized-hyperharmonic-zero-zero).

## The value $H_1^{(r)}(0) = r$

For every complex number $r$, the generalized
hyperharmonic number $H_1^{[r]}(0)$ equals $r$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Section 2, (2.4).

Formalized by `MetaMathlibExt.generalizedHyperharmonic_one_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generalized-hyperharmonic-one-zero).

## The value $H_1^{(r)}(1) = 1$

For every complex number $r$, the generalized
hyperharmonic number $H_1^{[r]}(1)$ equals $1$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Section 2, (2.4).

Formalized by `MetaMathlibExt.generalizedHyperharmonic_one_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generalized-hyperharmonic-one-one).

## Generalized hyperharmonic Euler sum

For an integer $k \ge 0$, complex numbers $r$ and
$a$ and an integer $p$, the generalized hyperharmonic Euler sum is
$S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$, where $H_n^{[r]}(k)$ is the
generalized hyperharmonic number. A term whose denominator $(n + a)^p$ vanishes counts as $0$,
and $S(k, r; p; a) = 0$ when the series is not summable.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 1 display.

Formalized by `MetaMathlibExt.hyperharmonicEulerSum`, a definition declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum).

## Hyperharmonic Euler sums as sums over all indices

For every integer $k \ge 0$, complex
numbers $r$ and $a$, and integer $p$, write $H_n^{[r]}(k)$ for the generalized hyperharmonic
number. Then the hyperharmonic Euler sum $S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$
equals $\sum_{n \ge 0} H_n^{[r]}(k) / (n + a)^p$, because $H_n^{[r]}(k) = 0$ for $n < k$.

Both sides are the sums of the series in the sense of unconditional summation, with the value $0$
assigned to a series that does not converge, and a term with $n + a = 0$ and $p \ne 0$ is read as
$0$, so the identity holds without any hypothesis.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 1 display.

Formalized by `MetaMathlibExt.hyperharmonicEulerSum_eq_tsum`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-eq-tsum).

## Odd multiple harmonic numbers

For natural numbers $k$ and $n$, the depth-$k$ odd
harmonic number is the real number

$$O_n(k) = \sum_{1 \le i_1 < \cdots < i_k \le n} \prod_{j=1}^{k} \frac{1}{i_j - 1/2}.$$

In particular $O_n(0) = 1$ (the empty product) and $O_n(k) = 0$ for $k > n$ (the empty sum).

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, (1.8) and (2.11).

Formalized by `MetaMathlibExt.oddMultipleHarmonic`, a definition declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#odd-multiple-harmonic).

## Odd multiple harmonic numbers of depth zero

For every natural number $n$, the
depth-zero odd harmonic number $O_n(0)$ equals $1$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, (2.11).

Formalized by `MetaMathlibExt.oddMultipleHarmonic_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#odd-multiple-harmonic-zero).

## Vanishing of odd multiple harmonic numbers of large depth

For natural numbers $k$ and
$n$ with $k > n$, the depth-$k$ odd harmonic number $O_n(k)$ equals $0$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, (2.11).

Formalized by `MetaMathlibExt.oddMultipleHarmonic_of_lt`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#odd-multiple-harmonic-of-lt).

## The first odd harmonic number

The depth-one odd harmonic number $O_1(1)$ equals $2$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, (2.11).

Formalized by `MetaMathlibExt.oddMultipleHarmonic_one_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#odd-multiple-harmonic-one-one).

## The algebra generated by $\log 2$, $\pi^2$ and odd zeta values

This is the
$\mathbb{Q}$-subalgebra of $\mathbb{C}$ generated by $\log 2$, $\pi^2$ and the zeta values
$\zeta(3), \zeta(5), \zeta(7), \dots$ (that is, $\zeta(2j+1)$ for all integers $j \ge 1$). It is
written $\mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \dots]$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 2.

Formalized by `MetaMathlibExt.eulerSumPeriodAlgebra`, a definition declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#euler-sum-period-algebra).

## Generators of the Euler sum period algebra

The numbers $\log 2$ and $\pi^2$ and the odd
zeta values $\zeta(2j + 3)$ for all integers $j \ge 0$ lie in the $\mathbb{Q}$-subalgebra
$\mathbb{Q}[\log 2, \pi^2, \zeta(2j+1)_{j \ge 1}]$ of $\mathbb{C}$ that they generate.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 2.

Formalized by `MetaMathlibExt.generators_mem_eulerSumPeriodAlgebra`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generators-mem-euler-sum-period-algebra).

## The algebra generated by $\log 2$, $\pi$, odd zeta values and even beta values

For
integers $s \ge 2$ let $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ be the value of the Dirichlet
beta function. This is the $\mathbb{Q}$-subalgebra of $\mathbb{C}$ generated by $\log 2$, $\pi$,
the zeta values $\zeta(2j+1)$ for all integers $j \ge 1$ and the beta values $\beta(2j)$ for all
integers $j \ge 1$. It is written
$\mathbb{Q}[\log 2, \pi, \zeta(2j+1)_{j \ge 1}, \beta(2j)_{j \ge 1}]$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 6.

Formalized by `MetaMathlibExt.eulerSumBetaPeriodAlgebra`, a definition declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#euler-sum-beta-period-algebra).

## Generators of the Euler sum beta period algebra

The numbers $\log 2$ and $\pi$, the zeta
values $\zeta(2j + 3)$ for all integers $j \ge 0$, and the Dirichlet beta values
$\beta(2j + 2) = \sum_{n \ge 0} (-1)^n / (2n + 1)^{2j+2}$ for all integers $j \ge 0$ lie in the
$\mathbb{Q}$-subalgebra $\mathbb{Q}[\log 2, \pi, \zeta(2j+1)_{j \ge 1}, \beta(2j)_{j \ge 1}]$ of
$\mathbb{C}$ that they generate.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 6.

Formalized by `MetaMathlibExt.generators_mem_eulerSumBetaPeriodAlgebra`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#generators-mem-euler-sum-beta-period-alg).

## Beta-function evaluation of hyperharmonic Euler sums

Let $k, p \ge 0$ be integers and
let $r, a$ be complex numbers with $\operatorname{Re}(r) < p + 1$ and $\operatorname{Re}(a) > -k$,
such that $r$ is not a positive integer and $a$ is not a nonpositive integer. Write
$H_n^{[r]}(k)$ for the generalized hyperharmonic number and let
$S(k, r; p + 1; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^{p+1}$. Then

$$p! \, k! \, S(k, r; p + 1; a) = (-1)^p D_a^p D_r^k B(a, 1 - r),$$

where $B(a, 1 - r) = \Gamma(a) \Gamma(1 - r) \cdot (1/\Gamma)(a + 1 - r)$, with $1/\Gamma$ the
entire reciprocal of the Gamma function (zero at the poles of $\Gamma$), and $D_a^p D_r^k$ means
the $k$-th complex derivative in $r$ followed by the $p$-th complex derivative in $a$.

The source also states the identity at positive integers $r$, after removing the singularity of
$\Gamma(1 - r)$, and at nonpositive integers $a$, and extends it by analytic continuation; those
cases are not included here.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Theorem 1.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_eq_iteratedDeriv_beta` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-eq-iterated-deri).

## Polygamma structure of hyperharmonic Euler sums

Let $k \ge 0$, $r$ and $p$ be integers
with $1 \le r \le p$, and let $a \in \mathbb{C} \setminus \mathbb{Z}$. Write $H_n^{[r]}(k)$ for
the generalized hyperharmonic number. Then the series
$S(k, r; p + 1; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^{p+1}$ converges absolutely, and its
sum lies in the algebra generated over the field $\mathbb{Q}(a)$ by $\psi(a) + \gamma$, the
derivatives $\psi^{(j)}(a)$ for $j \ge 1$ and the zeta values $\zeta(j)$ for $j \ge 2$, where
$\psi$ is the digamma function and $\gamma$ is the Euler–Mascheroni constant.

The source also extends the result by continuity to integers $a > -k$; that case is not included
here.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Theorem 2.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_mem_adjoin_digamma` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-mem-adjoin-digam).

## Hyperharmonic Euler sums with rational parameters

Let $a$ and $r$ be rational numbers
that are not integers, with $a - r \in \mathbb{Z}$, let $N \ge 1$ be an integer with
$N a \in \mathbb{Z}$, and let $k \ge 0$ and $p > r$ be integers. Put $M = \mathrm{lcm}(2N, 4)$
and $\omega = e^{2 \pi i / M}$, a primitive $M$-th root of unity. Write $H_n^{[r]}(k)$ for the
generalized hyperharmonic numbers. Then the generalized hyperharmonic Euler sum
$S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$ converges, and $S(k, r; p; a) = \pi x$
for some $x$ in the algebra generated over the field $\mathbb{Q}(\omega + \omega^{-1})$ by
$\psi(a) + \gamma$, the derivatives $\psi^{(j)}(a)$ for $j \ge 1$, $\pi^2$ and the odd zeta
values $\zeta(3), \zeta(5), \dots$, where $\psi$ is the digamma function and $\gamma$ is the
Euler–Mascheroni constant.

The field $\mathbb{Q}(\omega + \omega^{-1})$ does not depend on which primitive $M$-th root of
unity $\omega$ is chosen.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Theorem 3.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_rat_mem_pi_mul_adjoin` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-rat-mem-pi-mul-a).

## Duality for hyperharmonic Euler sums

Let $k, p \ge 0$ be integers and let $r, t$ be
complex numbers with $\operatorname{Re}(r) < p + 1$ and $\operatorname{Re}(t) < k + 1$. Write
$H_n^{[r]}(k)$ for the generalized hyperharmonic number. Then the series
$S(k, r; p + 1; 1 - t) = \sum_{n \ge k} H_n^{[r]}(k) / (n + 1 - t)^{p+1}$ and
$S(p, t; k + 1; 1 - r) = \sum_{n \ge p} H_n^{[t]}(p) / (n + 1 - r)^{k+1}$ both converge absolutely,
and $S(k, r; p + 1; 1 - t) = S(p, t; k + 1; 1 - r)$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 1.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_duality` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-duality).

## Hyperharmonic Euler sums with integer parameter and half-integer shift

Let $k \ge 0$, $r$
and $p$ be integers with $1 \le r < p$, and let $a \in \frac{1}{2} + \mathbb{Z}$. Write
$H_n^{[r]}(k)$ for the generalized hyperharmonic number. Then the series
$S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$ converges absolutely, and its sum lies
in the $\mathbb{Q}$-subalgebra $\mathbb{Q}[\log 2, \pi^2, \zeta(2j+1)_{j \ge 1}]$ of $\mathbb{C}$
generated by $\log 2$, $\pi^2$ and the odd zeta values.

The source prints $1 \le r \le p$, but at $r = p$ the series can diverge (for $k = 0$,
$r = p = 1$ and $a = 1/2$ it is $\sum_{n \ge 0} 1/(n + 1/2)$), and the source's Theorem 2 has
exponent $p + 1$ for $r \le p$; so $r < p$ is assumed.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 2, first part.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_half_mem_eulerSumPeriodAlgebra` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-half-mem-euler-s).

## Odd harmonic central binomial sums at integer shifts

Let $k \ge 0$ and $p > 0$ be
integers, let $a$ be an integer with $a > -k$, and let $O_n(k)$ denote the depth-$k$ odd harmonic
number. Then the series of real numbers

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n (n + a)^p}$$

converges, and its sum lies in the algebra $\mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \dots]$
viewed inside $\mathbb{C}$. The terms with $n < k$ are $0$, since $O_n(k) = 0$ for $n < k$, so
this is also the sum over $n \ge k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 2, second part.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_sum_mem_eulerSumPeriodAlgebra` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-sum).

## Central binomial odd harmonic sum with denominator $4^n (n + 1)^2$

For every integer
$k \ge 0$, with $O_n(k)$ the depth-$k$ odd harmonic number,

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n (n + 1)^2} =
2^{k+2} (k + 1 - \log 2) - \sum_{j=1}^{k} (2^{k+2} - 2^j) \zeta(k + 2 - j).$$

The terms with $n < k$ vanish, since $O_n(k) = 0$ for $n < k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 3.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_div_succ_sq_tsum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-div).

## Odd harmonic central binomial sums with weight $\binom{n}{m}$ at integer shifts

Let
$k, m \ge 0$ and $p > m$ be integers, let $a$ be an integer with $a > -k$, and let $O_n(k)$
denote the depth-$k$ odd harmonic number. Then the series of real numbers

$$\sum_{n \ge 0} \binom{n}{m} \frac{\binom{2n}{n} O_n(k)}{4^n (n + a)^p}$$

converges, and its sum lies in the algebra $\mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \dots]$
viewed inside $\mathbb{C}$. The terms with $n < k$ are $0$, since $O_n(k) = 0$ for $n < k$, so
this is also the sum over $n \ge k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 4, first part.

Stated but not proved: `MetaMathlibExt.choose_centralBinom_oddMultipleHarmonic_sum_mem_eulerSumPeriodAlgebra` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#choose-central-binom-odd-multiple-harmon).

## Central binomial odd harmonic sums over $\binom{n+m}{m}$ lie in the period algebra

Let
$O_n(k)$ denote the depth-$k$ odd harmonic number and let
$A = \mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \ldots] \subseteq \mathbb{C}$ be the Euler sum
period algebra. For integers $k \ge 0$, $p \ge 1$, $m \ge 1$ and $a > -k$, the series

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n \binom{n+m}{m} (n + a)^p}$$

converges and its sum lies in $A$.

The terms with $n < k$ are $0$ because $O_n(k) = 0$ there; this includes the term with
$n + a = 0$ when $a \le 0$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 4, second part.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_div_choose_sum_mem_eulerSumPeriodAlgebra` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-div-2).

## Catalan–odd harmonic sum with denominator $4^n n$

Let $k \ge 1$ be an integer, let $C_n$
denote the $n$-th Catalan number and $O_n(k)$ the depth-$k$ odd harmonic number. Then

$$\sum_{n \ge 1} \frac{C_n O_n(k)}{4^n n} = (2^{k+1} - 1) \zeta(k + 1) - 2^{k+1}.$$

Since $O_n(k) = 0$ for $n < k$, the sum can equally be taken over $n \ge k$.

## Sources

- the denominator $4^n n$ is read from the record's two-row layout ($C_n O_n(k)$ over $4^n n$).
- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 5.

Stated but not proved: `MetaMathlibExt.catalan_oddMultipleHarmonic_div_tsum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#catalan-odd-multiple-harmonic-div-tsum).

## Quarter-shift hyperharmonic Euler sums

Let $k \ge 0$ and $0 \le r < p$ be integers, and
let $a$ be a complex number with $a \in \tfrac14 + \mathbb{Z}$ or $a \in \tfrac34 + \mathbb{Z}$.
Write $H_n^{[r]}(k)$ for the generalized hyperharmonic numbers. Then the generalized
hyperharmonic Euler sum $S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$ converges, and
its value lies in the $\mathbb{Q}$-algebra
$\mathbb{Q}[\log 2, \pi, \zeta(3), \zeta(5), \dots, \beta(2), \beta(4), \dots]$ of complex
numbers, where $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ is the Dirichlet beta function.

The source prints $0 \le r \le p$; at $r = p \ge 1$ the series diverges (for $k = 0$ and
$r = p = 1$ it is $\sum_{n \ge 0} 1 / (n + a)$), so $r < p$ is used.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 6.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_quarter_mem_eulerSumBetaPeriodAlgebra` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-quarter-mem-eule).

## Hyperharmonic Euler sums with half-integer parameter and shift

Let $k \ge 0$ be an
integer, let $r, a \in \frac{1}{2} + \mathbb{Z}$, and let $p$ be an integer with $p > r$. Write
$H_n^{[r]}(k)$ for the generalized hyperharmonic number. Then the series
$S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$ converges absolutely, and its sum
equals $\pi x$ for some $x$ in the $\mathbb{Q}$-subalgebra $\mathbb{Q}[\log 2, \pi^2,
\zeta(2j+1)_{j \ge 1}]$ of $\mathbb{C}$ generated by $\log 2$, $\pi^2$ and the odd zeta values.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 7, first part.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_half_half_mem_pi_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-half-half-mem-pi).

## Odd harmonic central binomial sums with weight $\binom{n}{m}$ at half-integer shifts

Let $k, m \ge 0$ and $p > m$ be integers, let $a = d + 1/2$ with $d$ an integer, and let $O_n(k)$
denote the depth-$k$ odd harmonic number. Then the series of real numbers

$$\sum_{n \ge 0} \binom{n}{m} \frac{\binom{2n}{n} O_n(k)}{4^n (n + a)^p}$$

converges, and its sum equals $\pi x$ for some $x$ in the algebra
$\mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \dots] \subseteq \mathbb{C}$. The terms with $n < k$
are $0$, since $O_n(k) = 0$ for $n < k$, so this is also the sum over $n \ge k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 7, second part.

Stated but not proved: `MetaMathlibExt.choose_centralBinom_oddMultipleHarmonic_half_sum_mem_pi_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#choose-central-binom-odd-multiple-harmon-2).

## Central binomial odd harmonic sums over $\binom{n+m}{m}$ at half-integer shifts

Let
$O_n(k)$ denote the depth-$k$ odd harmonic number and let
$A = \mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \ldots] \subseteq \mathbb{C}$ be the Euler sum
period algebra. For integers $k \ge 0$, $p \ge 1$, $m \ge 1$ and $d$, put $a = d + 1/2$. Then the
series

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n \binom{n+m}{m} (n + a)^p}$$

converges, and its sum equals $q + \pi x$ for some rational number $q$ and some $x \in A$.

The terms with $n < k$ vanish, since $O_n(k) = 0$ for $n < k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 7, third part.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_div_choose_half_sum_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-div-3).

## Catalan–odd harmonic sums at the shift $1/2$

Let $k \ge 0$ and $p \ge 1$ be integers,
let $C_n$ denote the $n$-th Catalan number and $O_n(k)$ the depth-$k$ odd harmonic number, and
let $A = \mathbb{Q}[\log 2, \pi^2, \zeta(3), \zeta(5), \ldots] \subseteq \mathbb{C}$ be the Euler
sum period algebra. Then the series

$$S = \sum_{n \ge 0} \frac{C_n O_n(k)}{4^n (n + 1/2)^p}$$

converges, and $S - (-2)^p 2^{k+1} = \pi x$ for some $x \in A$.

The terms with $n < k$ vanish, since $O_n(k) = 0$ for $n < k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 8.

Stated but not proved: `MetaMathlibExt.catalan_oddMultipleHarmonic_half_sum_sub_mem_pi_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#catalan-odd-multiple-harmonic-half-sum-s).

## Central binomial sum over $\binom{n+m}{m} (n + 1/2)^2$

Let $m \ge 1$ be an integer and
write $O_m = O_m(1) = \sum_{i=1}^{m} 1/(i - 1/2)$ for the depth-one odd harmonic number. Then

$$\sum_{n \ge 0} \frac{\binom{2n}{n}}{4^n \binom{n+m}{m} (n + 1/2)^2} =
\frac{4^m \pi}{\binom{2m}{m}} \bigl(2 \log 2 - O_m\bigr) -
\sum_{q=1}^{m} \frac{(-4)^q \binom{m}{q}}{\binom{2q}{q} (q - 1/2)^2}.$$

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 9, first identity.

Stated but not proved: `MetaMathlibExt.centralBinom_div_choose_half_sq_tsum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-div-choose-half-sq-tsum).

## Odd harmonic central binomial sum over $\binom{n+m}{m} (n + 1/2)^2$

Let $m \ge 1$ be an
integer and write $O_j = O_j(1) = \sum_{i=1}^{j} 1/(i - 1/2)$ for the depth-one odd harmonic
number. Then

$$\sum_{n \ge 0} \frac{\binom{2n}{n} (O_n - O_m)}{4^n \binom{n+m}{m} (n + 1/2)^2} =
\frac{4^m \pi}{\binom{2m}{m}} \Bigl(\bigl(O_m - 2 \log 2\bigr)^2 - \frac{\pi^2}{6}\Bigr) +
\sum_{q=1}^{m} \frac{(-4)^q \binom{m}{q} (O_m - O_q)}{\binom{2q}{q} (q - 1/2)^2}.$$

Here $\pi^2 / 6 = \zeta(2)$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 9, second identity.

Stated but not proved: `MetaMathlibExt.centralBinom_oddHarmonic_sub_div_choose_half_sq_tsum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-harmonic-sub-div-choos).

## Products of quarter-shift hyperharmonic Euler sums

Let $k_1, k_2 \ge 0$ be integers,
let $r_1, r_2 \in \tfrac12 + \mathbb{Z}$, $a \in \tfrac14 + \mathbb{Z}$ and
$b \in \tfrac34 + \mathbb{Z}$, and let $p_1, p_2$ be integers with $p_1 > r_1$ and $p_2 > r_2$.
Write $H_n^{[r]}(k)$ for the generalized hyperharmonic numbers and
$S(k, r; p; a) = \sum_{n \ge k} H_n^{[r]}(k) / (n + a)^p$ for the generalized hyperharmonic
Euler sum. Then the series $S(k_1, r_1; p_1; a)$ and $S(k_2, r_2; p_2; b)$ converge, and
$S(k_1, r_1; p_1; a) \, S(k_2, r_2; p_2; b) = \pi x$ for some $x$ in the $\mathbb{Q}$-algebra
$\mathbb{Q}[\log 2, \pi, \zeta(3), \zeta(5), \dots, \beta(2), \beta(4), \dots]$ of complex
numbers, where $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ is the Dirichlet beta function.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 11, first part.

Stated but not proved: `MetaMathlibExt.hyperharmonicEulerSum_quarter_mul_mem_pi_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#hyperharmonic-euler-sum-quarter-mul-mem).

## Products of quarter-shift central binomial odd harmonic sums

Let $O_n(k)$ denote the
depth-$k$ odd harmonic number, let $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ be the Dirichlet
beta function, and let
$B = \mathbb{Q}[\log 2, \pi, \zeta(3), \zeta(5), \ldots, \beta(2), \beta(4), \ldots] \subseteq
\mathbb{C}$. For integers $k_1, k_2 \ge 0$ and $p_1, p_2 \ge 1$, the series

$$S_1 = \sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k_1)}{4^n (n + 1/4)^{p_1}}, \qquad
S_2 = \sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k_2)}{4^n (n + 3/4)^{p_2}}$$

both converge, and $S_1 S_2 = \pi x$ for some $x \in B$.

The terms with $n < k_i$ vanish, since $O_n(k_i) = 0$ for $n < k_i$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 11, second part.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_quarter_mul_mem_pi_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-quar).

## Odd harmonic central binomial sums with weight $\binom{n}{m}$ at shift $1/4$

Let
$k, m \ge 0$ and $p > m$ be integers, let $O_n(k)$ denote the depth-$k$ odd harmonic number, let
$\beta$ be the Dirichlet beta function, and let

$$\varpi = 2 \int_0^1 \frac{dt}{\sqrt{1 - t^4}}$$

be the lemniscate constant. Then the series of real numbers

$$\sum_{n \ge 0} \binom{n}{m} \frac{\binom{2n}{n} O_n(k)}{4^n (n + 1/4)^p}$$

converges, and its sum equals $\varpi x$ for some $x$ in the algebra
$\mathbb{Q}[\log 2, \pi, \zeta(2j+1)_{j \ge 1}, \beta(2j)_{j \ge 1}] \subseteq \mathbb{C}$. The
terms with $n < k$ are $0$, since $O_n(k) = 0$ for $n < k$, so this is also the sum over $n \ge k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 10, first statement.

Stated but not proved: `MetaMathlibExt.choose_centralBinom_oddMultipleHarmonic_quarter_sum_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#choose-central-binom-odd-multiple-harmon-3).

## Odd harmonic central binomial sums with weight $\binom{n}{m}$ at shift $3/4$

Let
$k, m \ge 0$ and $p > m$ be integers, let $O_n(k)$ denote the depth-$k$ odd harmonic number, let
$\beta$ be the Dirichlet beta function, and let

$$\varpi = 2 \int_0^1 \frac{dt}{\sqrt{1 - t^4}}$$

be the lemniscate constant. Then the series of real numbers

$$\sum_{n \ge 0} \binom{n}{m} \frac{\binom{2n}{n} O_n(k)}{4^n (n + 3/4)^p}$$

converges, and its sum equals $(\pi / \varpi) x$ for some $x$ in the algebra
$\mathbb{Q}[\log 2, \pi, \zeta(2j+1)_{j \ge 1}, \beta(2j)_{j \ge 1}] \subseteq \mathbb{C}$. The
terms with $n < k$ are $0$, since $O_n(k) = 0$ for $n < k$, so this is also the sum over $n \ge k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 10, second statement.

Stated but not proved: `MetaMathlibExt.choose_centralBinom_oddMultipleHarmonic_three_quarter_sum_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#choose-central-binom-odd-multiple-harmon-4).

## Central binomial odd harmonic sums over $\binom{n+m}{m}$ at the shift $1/4$

Let $O_n(k)$
denote the depth-$k$ odd harmonic number, let $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ be the
Dirichlet beta function, let
$B = \mathbb{Q}[\log 2, \pi, \zeta(3), \zeta(5), \ldots, \beta(2), \beta(4), \ldots] \subseteq
\mathbb{C}$, and let $\varpi = 2 \int_0^1 dt / \sqrt{1 - t^4}$ be the lemniscate constant. For
integers $k \ge 0$, $p \ge 1$ and $m \ge 1$, the series

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n \binom{n+m}{m} (n + 1/4)^p}$$

converges, and its sum equals $q + \varpi x$ for some rational number $q$ and some $x \in B$.

The terms with $n < k$ vanish, since $O_n(k) = 0$ for $n < k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 10, third statement.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_div_choose_quarter_sum_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-div-4).

## Central binomial odd harmonic sums over $\binom{n+m}{m}$ at the shift $3/4$

Let $O_n(k)$
denote the depth-$k$ odd harmonic number, let $\beta(s) = \sum_{n \ge 0} (-1)^n / (2n+1)^s$ be the
Dirichlet beta function, let
$B = \mathbb{Q}[\log 2, \pi, \zeta(3), \zeta(5), \ldots, \beta(2), \beta(4), \ldots] \subseteq
\mathbb{C}$, and let $\varpi = 2 \int_0^1 dt / \sqrt{1 - t^4}$ be the lemniscate constant. For
integers $k \ge 0$, $p \ge 1$ and $m \ge 1$, the series

$$\sum_{n \ge 0} \frac{\binom{2n}{n} O_n(k)}{4^n \binom{n+m}{m} (n + 3/4)^p}$$

converges, and its sum equals $q + (\pi / \varpi) x$ for some rational number $q$ and some
$x \in B$.

The terms with $n < k$ vanish, since $O_n(k) = 0$ for $n < k$.

## Sources

- Paul Thomas Young, *Parametric Euler Sums of Generalized Hyperharmonic Numbers*, INTEGERS 26 (2026), Article A81, Corollary 10, fourth statement.

Stated but not proved: `MetaMathlibExt.centralBinom_oddMultipleHarmonic_div_choose_three_quarter_sum_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperharmonicEulerSumsWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html#central-binom-odd-multiple-harmonic-div-5).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperharmonic Euler sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-euler-sums)
