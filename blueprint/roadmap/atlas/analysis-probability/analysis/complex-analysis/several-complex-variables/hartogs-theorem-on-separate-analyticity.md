---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.HartogsWanted.hartogs_posLog_norm_le_circleAverage, MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_uncurry_of_separately_differentiable_of_bounded, MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_uncurry_of_separately_differentiable_of_locally_bounded, MathlibExt.Analysis.Complex.HartogsWanted.differentiableOn_cauchyCoefficient_of_separately_differentiable_of_bounded, MathlibExt.Analysis.Complex.HartogsWanted.norm_cauchyCoefficient_le, MathlibExt.Analysis.Complex.HartogsWanted.hartogsPolydiscIntegral, MathlibExt.Analysis.Complex.HartogsWanted.hartogsPolydisc_submean, MathlibExt.Analysis.Complex.HartogsWanted.hartogs_eventually_uniform_of_submean
statement: formalized
proof: formalized
---

# Hartogs' theorem on separate analyticity

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html).

## Sub-mean-value inequality for the positive logarithm of a holomorphic function

Let
$c \in \mathbb{C}$, $R > 0$ and let $f : \mathbb{C} \to \mathbb{C}$ be analytic at every point of
the closed disc $|z - c| \le R$. Then

$$\log^+ |f(c)| \le \frac{1}{2\pi} \int_0^{2\pi} \log^+ |f(c + R e^{i\theta})| \, d\theta,$$

where $\log^+ t = \max(0, \log t)$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogs_posLog_norm_le_circleAverage`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#hartogs-pos-log-norm-le-circle-average).

## Osgood's lemma at the origin

Let $E$ be a complex normed space and let $f(z, w)$ be a
complex-valued function of $z \in E$ and $w \in \mathbb{C}$ such that $z \mapsto f(z, w)$ is
complex differentiable on all of $E$ for every $w \in \mathbb{C}$ and $w \mapsto f(z, w)$ is
complex differentiable on all of $\mathbb{C}$ for every $z \in E$. If there is a real number $M$
with $|f(z, w)| \le M$ whenever $\|z\| \le 1$ and $|w| \le 1$, then $f$, as a function on
$E \times \mathbb{C}$, is complex differentiable at $(0, 0)$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_uncurry_of_separately_differentiable_of_bounded`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#differentiable-at-uncurry-of-separately).

## Osgood's lemma for functions bounded on open sets

Let $E$ be a complex normed space and
let $f(z, w)$ be a complex-valued function of $z \in E$ and $w \in \mathbb{C}$ such that
$z \mapsto f(z, w)$ is complex differentiable on all of $E$ for every $w \in \mathbb{C}$ and
$w \mapsto f(z, w)$ is complex differentiable on all of $\mathbb{C}$ for every $z \in E$. Let
$U \subseteq E$ and $V \subseteq \mathbb{C}$ be open sets and $M$ a real number with
$|f(z, w)| \le M$ for all $z \in U$ and $w \in V$. Then $f$, as a function on
$E \times \mathbb{C}$, is complex differentiable at every point $(z_0, w_0)$ with $z_0 \in U$ and
$w_0 \in V$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_uncurry_of_separately_differentiable_of_locally_bounded`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#differentiable-at-uncurry-of-separately-2).

## Holomorphic dependence of Cauchy coefficients on a parameter

Let $E$ be a
finite-dimensional complex normed space, let $z_0 \in E$, $w_0 \in \mathbb{C}$, $A > 0$, $B > 0$
and $M \in \mathbb{R}$, and let $f(z, w)$ be a complex-valued function of $z \in E$ and
$w \in \mathbb{C}$ such that $z \mapsto f(z, w)$ is complex differentiable on all of $E$ for every
$w$ and $w \mapsto f(z, w)$ is complex differentiable on all of $\mathbb{C}$ for every $z$.
Suppose $|f(z, w)| \le M$ whenever $\|z - z_0\| \le A$ and $|w - w_0| \le B$. Then for every
$k \in \mathbb{N}$ the $k$-th Cauchy coefficient of $f(z, \cdot)$ about $w_0$ on the circle of
radius $B/2$,

$$a_k(z) = \frac{1}{2\pi i} \oint_{|w - w_0| = B/2} \frac{f(z, w)}{(w - w_0)^{k+1}} \, dw,$$

is a complex differentiable function of $z$ on the open ball $\|z - z_0\| < A/2$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.differentiableOn_cauchyCoefficient_of_separately_differentiable_of_bounded`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#differentiable-on-cauchy-coefficient-of).

## Cauchy's estimate for Taylor coefficients

Let $f : \mathbb{C} \to \mathbb{C}$ be
complex differentiable on all of $\mathbb{C}$, let $c \in \mathbb{C}$, $R > 0$ and
$M \in \mathbb{R}$ with $|f(z)| \le M$ for all $z$ with $|z - c| = R$. Then for every
$k \in \mathbb{N}$ the $k$-th coefficient of the Cauchy power series of $f$ about $c$ on the
circle of radius $R$,

$$a_k = \frac{1}{2\pi i} \oint_{|w - c| = R} \frac{f(w)}{(w - c)^{k+1}} \, dw,$$

satisfies $|a_k| \le M R^{-k}$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.norm_cauchyCoefficient_le`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#norm-cauchy-coefficient-le).

## Iterated integral over a polydisc

For $n \in \mathbb{N}$, a function
$u : \mathbb{C}^n \to \mathbb{R}$, a centre $c \in \mathbb{C}^n$ and a radius $R \in \mathbb{R}$,
the iterated polydisc integral $I(u, c, R)$ is defined by recursion on $n$. For $n = 0$ it is
$u(c)$. For $n = m + 1$, writing $c = (c_0, c_1, \dots, c_m)$, it is

$$I(u, c, R) = \int_{|z - c_0| \le R} I\big(u(z, \cdot), (c_1, \dots, c_m), R\big) \, dz,$$

where $u(z, \cdot)$ is the function $y \mapsto u(z, y)$ on $\mathbb{C}^m$ and $dz$ is Lebesgue
measure on $\mathbb{C}$. Thus, for $c = (c_0, \dots, c_{n-1})$ and $D_j$ the closed disc
$|z - c_j| \le R$,

$$I(u, c, R) = \int_{D_0} \cdots \int_{D_{n-1}} u(z_0, \dots, z_{n-1}) \, dz_{n-1} \cdots dz_0.$$

Each integral is a Bochner integral, taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogsPolydiscIntegral`, a definition declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 875](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L875). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#hartogs-polydisc-integral).

## Sub-mean-value inequality on a polydisc

Let $n \in \mathbb{N}$, let
$u : \mathbb{C}^n \to \mathbb{R}$ be continuous, let $c \in \mathbb{C}^n$ and $R > 0$. Write
$\overline{P}(c, R) = \{x \in \mathbb{C}^n : |x_j - c_j| \le R \text{ for all } j\}$ for the
closed polydisc, and for $x \in \mathbb{C}^n$ and $w \in \mathbb{C}$ write $x_{j \leftarrow w}$
for $x$ with its $j$-th coordinate replaced by $w$. Suppose that for every
$x \in \overline{P}(c, R)$, every coordinate $j$ and every $r$ with $0 < r \le R$,

$$u(x) \le \frac{1}{2\pi} \int_0^{2\pi} u(x_{j \leftarrow x_j + r e^{i\theta}}) \, d\theta.$$

Then $(\pi R^2)^n \, u(c) \le I(u, c, R)$, where $\pi R^2$ is the area of a disc of radius $R$
and $I(u, c, R)$ is the iterated polydisc integral of $u$ about $c$ with radius $R$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogsPolydisc_submean`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 939](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L939). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#hartogs-polydisc-submean).

## Hartogs' lemma for sub-mean-value functions

Let $n \in \mathbb{N}$, $c \in \mathbb{C}^n$,
$R > 0$ and $C \ge 0$. For $\rho \ge 0$ write
$\overline{P}(c, \rho) = \{x \in \mathbb{C}^n : |x_j - c_j| \le \rho \text{ for all } j\}$ for the
closed polydisc, and for $x \in \mathbb{C}^n$ and $w \in \mathbb{C}$ write $x_{j \leftarrow w}$
for $x$ with its $j$-th coordinate replaced by $w$. Let $(u_k)_{k \in \mathbb{N}}$ be real-valued
functions on $\mathbb{C}^n$ such that each $u_k$ is continuous on $\overline{P}(c, R)$,
$0 \le u_k(x) \le C$ for all $k$ and all $x \in \overline{P}(c, R)$, and $u_k(x) \to 0$ as
$k \to \infty$ for every $x \in \overline{P}(c, R)$. Suppose moreover that for every $k$, every
$x \in \overline{P}(c, R)$, every coordinate $j$ and every $r > 0$ such that
$x_{j \leftarrow z} \in \overline{P}(c, R)$ for all $z$ with $|z - x_j| \le r$,

$$u_k(x) \le \frac{1}{2\pi} \int_0^{2\pi} u_k(x_{j \leftarrow x_j + r e^{i\theta}}) \, d\theta.$$

Then for every $\varepsilon > 0$ there is $K$ such that $u_k(x) \le \varepsilon$ for all
$k \ge K$ and all $x \in \overline{P}(c, R/4)$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogs_eventually_uniform_of_submean`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 1335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L1335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#hartogs-eventually-uniform-of-submean).

## Hartogs' theorem on separate analyticity

Let $n \in \mathbb{N}$ and let
$f : \mathbb{C}^n \to \mathbb{C}$ be such that for every point $x \in \mathbb{C}^n$ and every
coordinate $i$, the function $z \mapsto f(x_1, \dots, x_{i-1}, z, x_{i+1}, \dots, x_n)$ is
complex differentiable on all of $\mathbb{C}$. Then $f$ is complex differentiable on all of
$\mathbb{C}^n$.

No continuity or boundedness of $f$ is assumed.

Proof: induction on the number of variables. Baire category gives a polydisc where $f$ is
bounded, where Osgood's lemma makes it holomorphic; Hartogs' lemma on sub-mean-value functions
then makes the Cauchy expansion in the last variable converge locally uniformly.

## Sources

- Hartogs separate analyticity (Osgood–Hartogs); see Hörmander; Lean is scalar-valued entire separately holomorphic via Function.update slices implies jointly Differentiable ℂ, finite-dimensional ℂⁿ specialization.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogs_separate_analyticity`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean, line 1794](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsSeparateAnalyticity.lean#L1794). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html#hartogs-separate-analyticity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hartogs' theorem on separate analyticity](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-theorem-on-separate-analyticity)
