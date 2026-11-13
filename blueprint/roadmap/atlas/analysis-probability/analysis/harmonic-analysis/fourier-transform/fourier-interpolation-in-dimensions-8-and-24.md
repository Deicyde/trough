---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.Radial, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.realIncl, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.coeffs, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidlyDecreasing, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidlyDecreasingSamples, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RadialSchwartz, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidSampleData, MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.CKMRV
statement: formalized
---

# Fourier interpolation in dimensions 8 and 24

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html).

## Radial function

A function is radial if it takes the same value at points with the same norm.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.Radial`, a definition declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#radial).

## Embedding of the first coordinate axis

For a positive integer $n$, this is the map
$\mathbb{R} \to \mathbb{R}^n$ sending $r$ to $(r, 0, \dots, 0)$, whose image is the first
coordinate axis.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.realIncl`, an abbreviation declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#real-incl).

## Fourier sample sequences

Let $n \ge 1$ and $k_0 \ge 0$ be integers, let $f$ be a
complex-valued Schwartz function on $\mathbb{R}^n$ with Fourier transform
$\hat f(\xi) = \int f(x) e^{-2\pi i \langle x, \xi \rangle}\,dx$, let $e_1$ be the first
standard basis vector and let $r_k = \sqrt{2k}$. The samples of $f$ are the four complex
sequences indexed by the integers $k \ge k_0$ whose $k$-th terms are, in this order,
$f(r_k e_1)$, $\hat f(r_k e_1)$, the derivative at $r = r_k$ of $r \mapsto f(r e_1)$, and the
derivative at $r = r_k$ of $r \mapsto \hat f(r e_1)$.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.coeffs`, a definition declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#coeffs).

## Rapidly decreasing sequences

For a natural number $k_0$, a complex sequence
$(a_k)_{k \ge k_0}$ indexed by the integers $k \ge k_0$ is rapidly decreasing if
$k^m |a_k| \to 0$ as $k \to \infty$ for every natural number $m$.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidlyDecreasing`, a definition declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#rapidly-decreasing).

## Rapidly decreasing sample quadruples

For a natural number $k_0$, a family $(a_{k,j})$
of complex numbers indexed by the integers $k \ge k_0$ and $j \in \{0, 1, 2, 3\}$ is a rapidly
decreasing quadruple if each of its four sequences $(a_{k,j})_{k \ge k_0}$ is rapidly
decreasing, that is, $k^m |a_{k,j}| \to 0$ as $k \to \infty$ for every $j$ and every natural
number $m$.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidlyDecreasingSamples`, a definition declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#rapidly-decreasing-samples).

## Radial Schwartz functions

For a natural number $n$, this is the set of complex-valued
Schwartz functions $f$ on $\mathbb{R}^n$ that are radial: $f(x) = f(y)$ whenever $|x| = |y|$.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RadialSchwartz`, an abbreviation declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#radial-schwartz).

## Rapidly decreasing sample data

For a natural number $k_0$, this is the set of families
$(a_{k,j})$ of complex numbers indexed by the integers $k \ge k_0$ and $j \in \{0, 1, 2, 3\}$
whose four sequences $(a_{k,j})_{k \ge k_0}$ are all rapidly decreasing: $k^m |a_{k,j}| \to 0$
as $k \to \infty$ for every $j$ and every natural number $m$.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.RapidSampleData`, an abbreviation declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#rapid-sample-data).

## Radial Fourier interpolation property

Let $n \ge 1$ and $k_0 \ge 0$ be integers. For a
complex-valued Schwartz function $f$ on $\mathbb{R}^n$, let
$\hat f(\xi) = \int f(x) e^{-2\pi i \langle x, \xi \rangle}\,dx$ be its Fourier transform, let
$e_1$ be the first standard basis vector and let $r_k = \sqrt{2k}$. The sampling map from index
$k_0$ sends $f$ to the four complex sequences indexed by the integers $k \ge k_0$ whose $k$-th
terms are $f(r_k e_1)$, $\hat f(r_k e_1)$ and the derivatives at $r = r_k$ of
$r \mapsto f(r e_1)$ and of $r \mapsto \hat f(r e_1)$. Call $f$ radial if $f(x) = f(y)$ whenever
$|x| = |y|$, and call a sequence $(a_k)_{k \ge k_0}$ rapidly decreasing if $k^m |a_k| \to 0$ as
$k \to \infty$ for every natural number $m$. The property $\mathrm{CKMRV}(n, k_0)$ holds when
the sampling map from index $k_0$ is a bijection from the radial Schwartz functions on
$\mathbb{R}^n$ onto the quadruples of rapidly decreasing sequences indexed by $k \ge k_0$.

The bijection is required to be the sampling map itself, so no interpolation basis is hidden
in the definition.

Formalized by `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.CKMRV`, a definition declared in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#ckmrv).

## Cohn–Kumar–Miller–Radchenko–Viazovska Fourier interpolation theorem

Let
$(n, k_0)$ be $(8, 1)$ or $(24, 2)$. For a complex-valued Schwartz function $f$ on
$\mathbb{R}^n$, let $\hat f(\xi) = \int f(x) e^{-2\pi i \langle x, \xi \rangle}\,dx$ be its
Fourier transform, let $e_1$ be the first standard basis vector and let $r_k = \sqrt{2k}$.
The sampling map sends $f$ to the four complex sequences indexed by the integers $k \ge k_0$
whose $k$-th terms are $f(r_k e_1)$, $\hat f(r_k e_1)$ and the derivatives at $r = r_k$ of
$r \mapsto f(r e_1)$ and of $r \mapsto \hat f(r e_1)$. Call $f$ radial if $f(x) = f(y)$
whenever $|x| = |y|$, and call a sequence $(a_k)_{k \ge k_0}$ rapidly decreasing if
$k^m |a_k| \to 0$ as $k \to \infty$ for every natural number $m$. Then the sampling map is a
bijection from the radial Schwartz functions on $\mathbb{R}^n$ onto the quadruples of rapidly
decreasing sequences indexed by $k \ge k_0$. So sampling starts at radius $\sqrt 2$ in
dimension $8$ and at radius $2$ in dimension $24$.

## Sources

- H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, 'Universal optimality of the E8 and Leech lattices and interpolation formulas', Ann. of Math. 196 (2022), 983-1082, Theorem 1.9, https://doi.org/10.4007/annals.2022.196.3.3. Problem `ckmrv_fourier_interpolation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.CKMRVInterpolationWanted.Analysis.CKMRVInterpolation.ckmrv_fourier_interpolation` is written with `theorem_wanted` in [WantedExt/Analysis/CKMRVInterpolationWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/CKMRVInterpolationWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html#ckmrv-fourier-interpolation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier interpolation in dimensions 8 and 24](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-interpolation-in-dimensions-8-and-24)
