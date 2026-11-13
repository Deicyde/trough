---
declaration: section
origin: cited
lean: MetaMathlibExt.heightOneMultipleZeta, MetaMathlibExt.heightOneMultipleZeta_zero, MetaMathlibExt.multipleHurwitzZeta, MetaMathlibExt.multipleHurwitzZeta_zero, MetaMathlibExt.hasSum_heightOneMultipleZeta_mul_pow, MetaMathlibExt.hasSum_heightOneMultipleZeta_mul_nat_pow, MetaMathlibExt.tsum_heightOneMultipleZeta_mul_neg_nat_pow, MetaMathlibExt.hasSum_heightOneMultipleZeta_goldbach
statement: formalized
---

# Height one multiple zeta values

11 results, 4 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html).

## Height one multiple zeta function

For a complex number $s$ and an integer $j \ge 0$, the
height one multiple zeta function is

$$\zeta(s, \{1\}^j) = \sum_{n \ge 0} (n + 1)^{-s} \sum_{T} \prod_{m \in T} \frac{1}{m},$$

where $T$ runs over the $j$-element subsets of $\{1, \dots, n\}$. Writing $n_1 = n + 1$ and
$T = \{n_2, \dots, n_{j+1}\}$, this is
$\zeta(s, \{1\}^j) = \sum_{n_1 > \cdots > n_{j+1} \ge 1} n_1^{-s} (n_2 \cdots n_{j+1})^{-1}$, which
converges for $\operatorname{Re} s > 1$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Section 1.

Formalized by `MetaMathlibExt.heightOneMultipleZeta`, a definition declared in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#height-one-multiple-zeta).

## Height one multiple zeta function of depth one

For every complex number $s$, the height
one multiple zeta function $\zeta(s, \{1\}^j)$ at $j = 0$ is the Dirichlet series of the Riemann
zeta function: $\zeta(s, \{1\}^0) = \sum_{n \ge 0} (n + 1)^{-s}$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Section 1.

Formalized by `MetaMathlibExt.heightOneMultipleZeta_zero`, a theorem declared in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#height-one-multiple-zeta-zero).

## Multiple Hurwitz zeta function

For complex numbers $r$ and $s$, the multiple Hurwitz zeta
function of order $r$, with Hurwitz parameter $a = 1$, is the Dirichlet series

$$\zeta_r(s) = \sum_{m \ge 0} \binom{m + r - 1}{m} (m + 1)^{-s},$$

where $\binom{m + r - 1}{m} = r (r + 1) \cdots (r + m - 1) / m!$. The series converges for
$\operatorname{Re} r < \operatorname{Re} s$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Section 2, Equation (2.2).

Formalized by `MetaMathlibExt.multipleHurwitzZeta`, a definition declared in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#multiple-hurwitz-zeta).

## Multiple Hurwitz zeta function of order zero

For every complex number $s$, the multiple
Hurwitz zeta function of order $0$ is identically one: $\zeta_0(s) = 1$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Section 2, Equation (2.2).

Formalized by `MetaMathlibExt.multipleHurwitzZeta_zero`, a theorem declared in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#multiple-hurwitz-zeta-zero).

## Expansion of the multiple Hurwitz zeta function in height one multiple zeta values

Let
$r$ and $s$ be complex numbers with $\operatorname{Re} s > 1$, $|r - 1| < |s - 1|$ and
$\operatorname{Re} r < \operatorname{Re} s$. Write $\zeta(s, \{1\}^j)$ for the height one multiple
zeta function and $\zeta_r(s)$ for the multiple Hurwitz zeta function of order $r$. Then the series
$\sum_{j \ge 0} \zeta(s, \{1\}^j) \, (r - 1)^j$ is summable with sum $\zeta_r(s)$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Theorem 1.

Stated but not proved: `MetaMathlibExt.hasSum_heightOneMultipleZeta_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#has-sum-height-one-multiple-zeta-mul-pow).

## Height one multiple zeta series weighted by powers of a natural number

Let $n \ge 0$ be
an integer. Write $\zeta(s, \{1\}^j)$ for the height one multiple zeta function, $\zeta$ for the
Riemann zeta function, $c(n, m)$ for the unsigned Stirling numbers of the first kind and
$B_j^{(k)}(x)$ for the poly-Bernoulli polynomials. For every complex $s$ with
$\operatorname{Re} s > n + 1$, the series $\sum_{j \ge 0} \zeta(s, \{1\}^j) \, n^j$ (with $0^0 = 1$)
is summable with sum $\frac{1}{n!} \sum_{m=0}^{n} c(n, m) \, \zeta(s - m)$. For every complex $s$
with $\operatorname{Re} s > 1$, the series $\sum_{j \ge 0} B_j^{(-n)}(-1) \, \zeta(s + n, \{1\}^j)$
is summable with sum $\zeta(s)$.

The source states the second identity with $C_j^{(-n)} = B_j^{(-n)}(1)$, where its poly-Bernoulli
polynomials have the generating function with $e^{-xt}$; with the factor $e^{xt}$ used here this
coefficient is $B_j^{(-n)}(-1)$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Corollary 1.

Stated but not proved: `MetaMathlibExt.hasSum_heightOneMultipleZeta_mul_nat_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#has-sum-height-one-multiple-zeta-mul-nat).

## Height one multiple zeta series weighted by powers of a negative integer

Let $r \ge 1$
be an integer and let $\zeta(s, \{1\}^j)$ denote the height one multiple zeta function. For
every complex number $s$ with $\operatorname{Re} s > r + 1$,

$$\sum_{j \ge 0} \zeta(s, \{1\}^j) (-r)^j = \sum_{m=0}^{r-1} \binom{r-1}{m} (-1)^m (m+1)^{-s}.$$

For every integer $k > r + 1$,

$$\sum_{j \ge 0} \zeta(k, \{1\}^j) (-r)^j = \frac{H_{r,k-1}}{r},$$

where $H_{r,k-1} = \sum_{i=1}^{r} (-1)^{i-1} \binom{r}{i} i^{-(k-1)}$ is the rational Roman
harmonic number (Equation (2.18)).

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Corollary 2.

Stated but not proved: `MetaMathlibExt.tsum_heightOneMultipleZeta_mul_neg_nat_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#tsum-height-one-multiple-zeta-mul-neg-na).

## Generalized Goldbach series for height one multiple zeta values

Let $k \ge 1$ be an
integer. Write $\zeta(s, \{1\}^j)$ for the height one multiple zeta function, $\zeta$ for the
Riemann zeta function, $c(k, m)$ for the unsigned Stirling numbers of the first kind,
$H_k = \sum_{i=1}^{k} 1/i$ for the $k$-th harmonic number and
$H_{k,k} = \sum_{i=1}^{k} (-1)^{i-1} \binom{k}{i} i^{-k}$ for the Roman harmonic number. Then the
series $\sum_{j \ge 0} \bigl(k^j \zeta(k + 1, \{1\}^j) - \frac{1}{k! \, k}\bigr)$ is summable with
sum $\frac{1}{k!} \bigl(\sum_{m=0}^{k-1} c(k, m) \, \zeta(k + 1 - m) + H_k\bigr)$, and the series
$\sum_{j \ge 0} (-1)^j \bigl(k^j \zeta(k + 1, \{1\}^j) - \frac{1}{k! \, k}\bigr)$ is summable with
sum $\frac{H_{k,k}}{k} - \frac{1}{2 \, k! \, k}$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Theorem 2.

Stated but not proved: `MetaMathlibExt.hasSum_heightOneMultipleZeta_goldbach` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#has-sum-height-one-multiple-zeta-goldbac).

## Expansion of the hyperharmonic zeta function in height one multiple zeta values

Let $r$
and $s$ be complex numbers with $\operatorname{Re} s > 0$, $|r| < |s|$ and
$\operatorname{Re} r < \operatorname{Re} s$. Write $\zeta(s, \{1\}^j)$ for the height one multiple
zeta function, $H_m^{[r]}(k)$ for the generalized hyperharmonic numbers and
$H_m^{[r]} = H_m^{[r]}(1)$; equivalently, $H_m^{[r]}$ is the derivative of $\binom{m + r - 1}{m}$
with respect to $r$. Then the series $\sum_{j \ge 0} (j + 1) \, \zeta(s + 1, \{1\}^j) \, r^j$ is
summable with sum the hyperharmonic zeta function $\sigma(r, s) = \sum_{m \ge 1} H_m^{[r]} m^{-s}$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Theorem 3, second equality.

Stated but not proved: `MetaMathlibExt.hasSum_succ_mul_heightOneMultipleZeta_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#has-sum-succ-mul-height-one-multiple-zet).

## Shifted alternating series of height one multiple zeta values

Let $k \ge -1$ and
$p \ge 0$ be integers, write $\zeta(s, \{1\}^p)$ for the height one multiple zeta function and
$\zeta_r(s)$ for the multiple Hurwitz zeta function of order $r$. Then the partial sums of the
series $\nu_{k,p} = \sum_{n \ge 2} \frac{(-1)^n \, \zeta(n, \{1\}^p)}{n + k}$ converge to
$\int_0^1 (1 - r)^{k+1} \, \zeta_r(p + 2) \, dr$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Theorem 4.

Stated but not proved: `MetaMathlibExt.tendsto_alternating_heightOneMultipleZeta_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#tendsto-alternating-height-one-multiple).

## Linear Laurent coefficient of the height one multiple zeta function

Let $j \ge 1$ be an
integer, write $\zeta(s, \{1\}^{j-1})$ for the height one multiple zeta function and $\zeta_r(s)$
for the multiple Hurwitz zeta function of order $r$. There are complex numbers
$c_0, \dots, c_{j-1}$ and a function $F$ analytic at $s = 1$ such that
$\zeta(s, \{1\}^{j-1}) = \sum_{i=0}^{j-1} c_i (s - 1)^{-(i+1)} + F(s)$ for all $s$ near $1$
with $\operatorname{Re} s > 1$, and

$$-F'(1) = \int_0^1 \bigl((1 - r) \, \zeta_r(j + 2) - \zeta_r(j + 1)\bigr) \, dr - a_{j+1},$$

where $a_{j+1}$ is the coefficient of $s^{j+1}$ in the Taylor expansion of $1/\Gamma(s + 1)$
at $s = 0$.

The number $-F'(1)$ generalizes the first Stieltjes constant $\gamma_1$: for $j = 1$ and
$\operatorname{Re} s > 1$, $\zeta(s, \{1\}^0)$ equals the Riemann zeta function $\zeta(s)$, whose
Laurent expansion at $s = 1$ is $\zeta(s) = \frac{1}{s - 1} + \gamma - \gamma_1 (s - 1) + \cdots$
with Euler's constant $\gamma$, so $-F'(1) = \gamma_1$.

## Sources

- Paul Thomas Young, *Series of Height One Multiple Zeta Functions*, INTEGERS 24 (2024), Article A43, Corollary 3.

Stated but not proved: `MetaMathlibExt.heightOneMultipleZeta_laurent_linear_coeff` is written with `theorem_wanted` in [WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HeightOneMultipleZetaSeriesWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html#height-one-multiple-zeta-laurent-linear).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Height one multiple zeta values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/height-one-multiple-zeta-values)
