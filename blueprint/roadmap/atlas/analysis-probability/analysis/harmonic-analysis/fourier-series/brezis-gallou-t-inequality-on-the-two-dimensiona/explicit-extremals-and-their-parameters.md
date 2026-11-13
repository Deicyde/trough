---
declaration: section
origin: cited
lean: TorusSobolev.FiniteExtremalParameter, TorusSobolev.ExtremalParameter, TorusSobolev.KernelAdmissible, TorusSobolev.extremalCoefficient, TorusSobolev.IsExplicitExtremal, TorusSobolev.SameExtremalOrbit
statement: formalized
proof: formalized
---

# Explicit extremals and their parameters

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html).

## Finite extremal parameters

A finite extremal parameter is a real number $\mu$ with
$\mu < -1$ or $\mu > 0$.

The endpoints $\mu = -1$ and $\mu = \infty$ are not finite extremal parameters; the extremal
parameter domain adds them separately.

Formalized by `TorusSobolev.FiniteExtremalParameter`, an abbreviation declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#finite-extremal-parameter).

## Extremal parameters

An extremal parameter is either a finite extremal parameter, that
is, a real number $\mu$ with $\mu < -1$ or $\mu > 0$, or one of two further parameters: the
first-shell parameter, standing for the endpoint $\mu = -1$, and the biharmonic parameter,
standing for the endpoint $\mu = \infty$.

Together these cover the parameter domain $(-\infty, -1] \cup (0, \infty]$, the two endpoints
being represented by limiting coefficient families rather than by values of $\mu$.

Formalized by `TorusSobolev.ExtremalParameter`, an inductive type declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#extremal-parameter).

## Kernel-admissible extremal parameters

Write $|k|^2 = k_1^2 + k_2^2$ for a frequency
$k \in \mathbb{Z}^2$. A finite extremal parameter $\mu$ is kernel-admissible when
$|k|^2 \neq 0$ and $1 + \mu |k|^2 \neq 0$ for every nonzero frequency $k$; the first-shell
parameter is always kernel-admissible; the biharmonic parameter is kernel-admissible when
$|k|^2 \neq 0$ for every nonzero frequency $k$.

These conditions make every reciprocal in the extremal coefficients well defined.

Formalized by `TorusSobolev.KernelAdmissible`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#kernel-admissible).

## Extremal coefficients

Let $p$ be a kernel-admissible extremal parameter and write
$|k|^2 = k_1^2 + k_2^2$ for $k \in \mathbb{Z}^2$. The extremal coefficients $c_p(k)$, complex
numbers indexed by $k \in \mathbb{Z}^2$, are as follows. If $p$ is a finite parameter $\mu$, then
$c_p(0) = 0$ and $c_p(k) = 2\pi / (|k|^2 (1 + \mu |k|^2))$ for $k \neq 0$. If $p$ is the
first-shell parameter, then $c_p(k) = \pi$ when $|k|^2 = 1$ and $c_p(k) = 0$ otherwise. If $p$ is
the biharmonic parameter, then $c_p(0) = 0$ and $c_p(k) = 2\pi / |k|^4$ for $k \neq 0$.

The values are real and do not depend on the proof of admissibility.

Formalized by `TorusSobolev.extremalCoefficient`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#extremal-coefficient).

## Explicit extremals

A continuous real function $u$ on the torus
$\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$ is an explicit extremal when there are a
kernel-admissible extremal parameter $p$ and a real number $a \neq 0$ such that the extremal
coefficients $c_p(k)$ are summable over $k \in \mathbb{Z}^2$, the Fourier coefficient
$\hat u(k) = \frac{1}{2\pi} \int_{[0, 2\pi]^2} u(x) e^{-i k \cdot x} \, dx$ equals $a \, c_p(k)$
for every $k \in \mathbb{Z}^2$, and
$u(x) = \frac{1}{2\pi} \sum_{k \in \mathbb{Z}^2} a \, c_p(k) \, e^{i k \cdot x}$ for every
$x \in \mathbb{T}$.

Formalized by `TorusSobolev.IsExplicitExtremal`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#is-explicit-extremal).

## Same extremal orbit

Two continuous real functions $u$ and $v$ on the torus
$\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$ lie in the same extremal orbit when there are a
real number $a \neq 0$ and a point $x_0 \in \mathbb{T}$ such that $v(x) = a \, u(x - x_0)$ for
every $x \in \mathbb{T}$.

Formalized by `TorusSobolev.SameExtremalOrbit`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/TorusSobolev/Extremals.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html#same-extremal-orbit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit extremals and their parameters](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/explicit-extremals-and-their-parameters)
