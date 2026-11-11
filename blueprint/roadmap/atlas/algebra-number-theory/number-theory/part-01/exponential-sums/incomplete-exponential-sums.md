---
declaration: section
origin: cited
lean: MetaMathlibExt.one_div_sin_pi_lt, MetaMathlibExt.sum_one_div_abs_sin_lt, MetaMathlibExt.sum_abs_sin_mul_div_lt, MetaMathlibExt.exists_trigPoly_minorant_majorant, MetaMathlibExt.norm_incomplete_quadratic_sum_lt, MetaMathlibExt.norm_incomplete_monic_cubic_sum_lt, MetaMathlibExt.exists_incompleteSum_eq_completeSum_add, MetaMathlibExt.sqrt_le_sup_norm_completeSum
statement: formalized
---

# Incomplete exponential sums

16 results, 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html).

## Partial-fraction bound for the cosecant

For every real number $x$ with $0 < x < 1$,

$$\frac{1}{\sin(\pi x)} < \frac{1}{\pi}\left(\frac{1}{x} + \frac{2x}{1 - x^2}\right).$$

That is, the first two terms of the partial-fraction expansion of $\pi / \sin(\pi x)$ bound it
from above.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 3.1 (quoted from [3, Lemma 2.2]).

Stated but not proved: `MetaMathlibExt.one_div_sin_pi_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#one-div-sin-pi-lt).

## Bound for a sum of reciprocal sines

Let $p$ be a prime, let $a$ be an integer not
divisible by $p$, let $B$ be an integer with $1 \le B < p/2$, and let $\gamma$ be the
Euler–Mascheroni constant. Then

$$
\sum_{h=1}^{B} \frac{1}{|\sin(\pi a h / p)|} <
\frac{p}{\pi}\left(\log B + \gamma + \frac{1}{2B}\right) + \frac{pB(B+1)}{\pi(p^2 - B^2)}.
$$

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.sum_one_div_abs_sin_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#sum-one-div-abs-sin-lt).

## Bound for a weighted sum of absolute sines

Let $K$ be a positive integer, let $\xi$ be a
real number, and let $\gamma$ be the Euler–Mascheroni constant. Then

$$
\sum_{y=1}^{K} \frac{|\sin(y\xi)|}{y} <
\frac{2}{\pi}\left(\log(K + 1) + \gamma + \log 2\right) + \frac{3}{\pi(K + 1)}
$$

and

$$
\sum_{y=1}^{K} \frac{|\sin(y\xi)|}{y} <
\frac{2}{\pi}\log K + \frac{2}{\pi}(\gamma + \log 2) + \frac{5}{\pi K}.
$$

The second bound is the form (3.1) of the first, obtained from $\log(K + 1) < \log K + 1/K$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 3.4 (quoted from [3, Lemma 2.1]) and inequality (3.1).

Stated but not proved: `MetaMathlibExt.sum_abs_sin_mul_div_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#sum-abs-sin-mul-div-lt).

## Trigonometric polynomials bounding the indicator of an arc

Let $a \le b$ be real
numbers with $b - a < 1$ and let $K \ge 1$ be an integer. Let $\chi(x) = 1$ if
$a \le x - n \le b$ for some integer $n$, and $\chi(x) = 0$ otherwise. Then there are complex
numbers $\alpha_-(k)$ and $\alpha_+(k)$, for $k \in \mathbb{Z}$, with
$\alpha_\pm(0) = b - a \pm \frac{1}{K+1}$, such that for every real $x$ the trigonometric
polynomials $S_\pm(x) = \sum_{k=-K}^{K} \alpha_\pm(k) e^{2\pi i k x}$ are real and satisfy
$S_-(x) \le \chi(x) \le S_+(x)$.

Only the constant coefficients and the pointwise bounds are stated; no bounds on the
coefficients $\alpha_\pm(k)$ with $k \ne 0$ are asserted.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 4.1.

Stated but not proved: `MetaMathlibExt.exists_trigPoly_minorant_majorant` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#exists-trig-poly-minorant-majorant).

## Incomplete quadratic exponential sums of medium length

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $a, b, c$ be integers with $p \nmid a$, and let $B$ be an integer
with $\sqrt{p} < B < p/2$. Then $\left|\sum_{x=1}^{B} e_p(a x^2 + b x + c)\right| <
\sqrt{\frac{2}{\pi} \, p \log \frac{16.6 B^2}{p}}$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.norm_incomplete_quadratic_sum_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-quadratic-sum-lt).

## Bounds for short incomplete exponential sums of monic cubics

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $b, c$ be integers, let $B$ be an integer with
$4 p^{1/3} < B < \sqrt{p/12}$, and put $S = \sum_{x=1}^{B} e_p(x^3 + b x^2 + c x)$. Then
$|S| < (Bp)^{1/4} \left(\log \frac{B^3}{p}\right)^{1/4} (\log (Bp))^{1/4}$ and
$|S| < (Bp)^{1/4} (\log p)^{1/2}$.

The second bound is stated on the same range $4 p^{1/3} < B < \sqrt{p/12}$ as the first,
although the source states it for $B < \sqrt{p/12}$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.norm_incomplete_monic_cubic_sum_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-monic-cubic-sum-lt).

## Completing an incomplete exponential sum

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $f$ be a polynomial with integer coefficients, and let $B$ be an
integer with $1 \le B \le p$. Put
$T_p(B) = \frac{1}{p} \sum_{y=1}^{p-1} \left|\frac{\sin(\pi B y/p)}{\sin(\pi y/p)}\right|$ and
$M = \max_{1 \le y \le p-1} \left|\sum_{x=1}^{p} e_p(f(x) + yx)\right|$. Then there is a complex
number $\theta$ with $|\theta| \le 1$ such that
$\sum_{x=1}^{B} e_p(f(x)) = \frac{B}{p} \sum_{x=1}^{p} e_p(f(x)) + \theta \, T_p(B) \, M$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.exists_incompleteSum_eq_completeSum_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#exists-incomplete-sum-eq-complete-sum-ad).

## Lower bound for the maximal twisted complete exponential sum

Let $p$ be a prime, let $f$
be a polynomial with integer coefficients, and write $e_p(t) = e^{2\pi i t / p}$ for integers $t$.
Then

$$\max_{0 \le y \le p - 1} \left| \sum_{x=1}^{p} e_p(f(x) + yx) \right| \ge \sqrt{p}.$$

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.sqrt_le_sup_norm_completeSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#sqrt-le-sup-norm-complete-sum).

## Explicit completion bound for incomplete exponential sums

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $f$ be a polynomial with integer coefficients whose reduction
modulo $p$ has degree at least $2$, and let $B$ be an integer with $1 \le B \le p$. Put
$\Phi(f, p) = \max_{0 \le y \le p-1} \left|\sum_{x=1}^{p} e_p(f(x) + yx)\right|$. Then
$\left|\sum_{x=1}^{B} e_p(f(x))\right| \le
\min\left\{\frac{2}{\pi^2} \log p + 3.29 + \frac{B}{p},
\frac{4}{\pi^2} \log p + \frac{B}{p} + 0.35\right\} \Phi(f, p)$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.norm_incompleteSum_le_min_mul_sup` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-sum-le-min-mul-sup).

## Logarithmic completion bound for incomplete exponential sums

Let $p \ge 5$ be a prime,
write $e_p(t) = e^{2\pi i t/p}$, let $f$ be a polynomial with integer coefficients whose reduction
modulo $p$ has degree at least $2$, and let $B$ be an integer with $1 \le B \le p$. Put
$\Phi(f, p) = \max_{0 \le y \le p-1} \left|\sum_{x=1}^{p} e_p(f(x) + yx)\right|$. Then
$\left|\sum_{x=1}^{B} e_p(f(x))\right| < \Phi(f, p) \log p$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Corollary 1.1.

Stated but not proved: `MetaMathlibExt.norm_incompleteSum_lt_sup_mul_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-sum-lt-sup-mul-log).

## Bound for a truncated sum of reciprocal sines

Let $p$ be a prime, let $a$ be an integer
not divisible by $p$, and let $B$ be an integer with $\sqrt{p/\pi} < B < p/2$. Then

$$
\sum_{h=1}^{B} \min\left\{B, \frac{1}{|\sin(\pi a h / p)|}\right\} <
\frac{p}{\pi}\left(\log\frac{\pi B^2}{p} + 1 + \frac{\pi B}{p}\right) +
\frac{pB(B+1)}{\pi(p^2 - B^2)}.
$$

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 3.3.

Stated but not proved: `MetaMathlibExt.sum_min_one_div_abs_sin_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#sum-min-one-div-abs-sin-lt).

## Bound for a sum of sine ratios

Let $q$, $K$ and $B$ be natural numbers with
$1 \le K < q$ and $B \ge 1$, and let $\gamma$ be the Euler–Mascheroni constant. Then

$$
\sum_{k=1}^{K} \frac{|\sin(\pi B k / q)|}{|\sin(\pi k / q)|} <
\frac{2}{\pi^2} q \log K + \frac{2q}{\pi^2}(\gamma + \log 2) + \frac{q}{\pi} \cdot \frac{K}{q - K} +
\frac{5q}{\pi^2 K}.
$$

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 3.5.

Stated but not proved: `MetaMathlibExt.sum_abs_sin_div_abs_sin_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#sum-abs-sin-div-abs-sin-lt).

## Square of an incomplete quadratic exponential sum

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $a, b, c$ be integers with $p \nmid a$, let $B$ be an integer with
$\sqrt{p} < B < p/2$, and put $S = \sum_{x=1}^{B} e_p(a x^2 + b x + c)$ and
$R = \frac{2pB(B+1)}{\pi(p^2 - B^2)}$. Then $|S|^2$ is at most the minimum of
$\frac{2p}{\pi} \log \frac{B^2}{p} + 1.366 p + 3B + R$ and
$\frac{2p}{\pi} \log B + 0.368 p + B + \frac{p}{\pi B} + R$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Proposition 6.1.

Stated but not proved: `MetaMathlibExt.norm_sq_incomplete_quadratic_sum_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-sq-incomplete-quadratic-sum-le).

## Uniform bound for incomplete quadratic exponential sums

Let $p$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$, let $a, b, c$ be integers with $p \nmid a$, and let $B$ be an integer
with $1 \le B \le p$. Then $\left|\sum_{x=1}^{B} e_p(a x^2 + b x + c)\right| <
\sqrt{p} + \sqrt{\frac{2}{\pi} p \log p + \frac{p}{2}}$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Corollary 6.1.

Stated but not proved: `MetaMathlibExt.norm_incomplete_quadratic_sum_lt_sqrt_add_sqrt` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-quadratic-sum-lt-sqrt-ad).

## Explicit bounds for incomplete cubic exponential sums

Let $p \ge 3$ be a prime, write
$e_p(t) = e^{2\pi i t/p}$ and $\delta_p = \frac{1.0661}{\log \log p}$, let $a, b, c$ be integers
with $p \nmid a$, let $B$ be a positive integer, and put
$S = \sum_{x=1}^{B} e_p(a x^3 + b x^2 + c x)$. If $B < \sqrt{p/2}$, then
$|S| \le 1.1 \, B^{1/4} p^{1/4 + \delta_p/4} (\log p)^{1/4}$. If $\sqrt{p/2} < B \le p$, then
$|S| \le 1.38 \, (1 + p/B^2)^{1/4} B^{3/4} p^{\delta_p/2} (\log p)^{1/4}$.

The hypothesis $p \ge 3$ makes $\log \log p > 0$. For $p = 2$, $f(x) = x^3 + x$ and $B = 2$,
the sum equals $2$ while the second bound is below $0.86$.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.norm_incomplete_cubic_sum_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#norm-incomplete-cubic-sum-le).

## Explicit asymptotic for the logarithmic mean of the divisor function

Let $\tau(n)$ be
the number of positive divisors of $n$ and let $\gamma$ be the Euler–Mascheroni constant. There
is a real constant $C$ such that $\sum_{k=1}^{N} \frac{\log k}{k} - \frac{(\log N)^2}{2}$ tends
to $\frac{\gamma^2 - C}{2}$ as $N \to \infty$ and such that for every real $x \ge 2$,
$\left|\sum_{1 \le n \le x} \frac{\tau(n)}{n} -
\left(\frac{(\log x)^2}{2} + 2\gamma \log x + C\right)\right| \le \frac{2.1 \log x}{x^{2/3}}$.

The first condition says that $C = \gamma^2 - 2\gamma_1$, where
$\gamma_1 = \lim_{N \to \infty} \left(\sum_{k=1}^{N} \frac{\log k}{k} - \frac{(\log N)^2}{2}\right)$
is the first Stieltjes constant.

## Sources

- Todd Cochrane, *Explicit Estimates for Incomplete Exponential Sums*, INTEGERS 25 (2025), Article A48, Lemma 7.1.

Stated but not proved: `MetaMathlibExt.exists_sum_card_divisors_div_sub_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/IncompleteExponentialSumWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html#exists-sum-card-divisors-div-sub-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Incomplete exponential sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/exponential-sums/incomplete-exponential-sums)
