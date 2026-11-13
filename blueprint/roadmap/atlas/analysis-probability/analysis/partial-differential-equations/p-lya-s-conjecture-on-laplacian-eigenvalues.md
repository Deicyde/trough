---
declaration: section
origin: cited
lean: NonnegativeDiscreteSpectrum, NonnegativeDiscreteSpectrum.ext, NonnegativeDiscreteSpectrum.sublevelSet, NonnegativeDiscreteSpectrum.sublevelSet_finite, NonnegativeDiscreteSpectrum.sublevelFinset, NonnegativeDiscreteSpectrum.mem_sublevelFinset, NonnegativeDiscreteSpectrum.countingFunction, NonnegativeDiscreteSpectrum.rieszMean
statement: formalized
proof: formalized
---

# Pólya's conjecture on Laplacian eigenvalues

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html).

## Nonnegative discrete spectrum

A nonnegative discrete spectrum is a sequence of real
numbers $E_0, E_1, E_2, \ldots$, the eigenvalues listed with multiplicity, such that
$E_j \ge 0$ for every $j$, $E_i \le E_j$ whenever $i \le j$, and $E_j \to +\infty$ as
$j \to \infty$.

The sequence is not required to be the spectrum of any particular operator, such as a
Dirichlet or Neumann Laplacian.

Formalized by `NonnegativeDiscreteSpectrum`, a structure declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#nonnegative-discrete-spectrum).

## A nonnegative discrete spectrum is determined by its eigenvalues

If two nonnegative
discrete spectra $S$ and $T$ have the same $j$-th eigenvalue for every index $j \in \mathbb{N}$,
then $S = T$.

Formalized by `NonnegativeDiscreteSpectrum.ext`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#ext).

## Strict sublevel set

For a nonnegative discrete spectrum with eigenvalues
$E_0 \le E_1 \le \cdots$ and a real number $\Lambda$, the strict sublevel set at $\Lambda$ is the
set of indices $\{j \in \mathbb{N} : E_j < \Lambda\}$.

The strict inequality matches the convention that $(\Lambda - E_j)_+^0$ equals $1$ only when
$E_j < \Lambda$, avoiding $0^0 = 1$ at the cutoff.

Formalized by `NonnegativeDiscreteSpectrum.sublevelSet`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#sublevel-set).

## Strict sublevel sets are finite

For a nonnegative discrete spectrum with eigenvalues
$E_0 \le E_1 \le \cdots$ and every real number $\Lambda$, the strict sublevel set
$\{j \in \mathbb{N} : E_j < \Lambda\}$ is finite.

Since $E_j \to +\infty$, there is $N$ with $E_j \ge \Lambda$ for all $j \ge N$, so the set is
contained in $\{0, 1, \ldots, N - 1\}$.

Formalized by `NonnegativeDiscreteSpectrum.sublevelSet_finite`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#sublevel-set-finite).

## Finite strict sublevel set

For a nonnegative discrete spectrum with eigenvalues
$E_0 \le E_1 \le \cdots$ and a real number $\Lambda$, the finite strict sublevel set at $\Lambda$ is
the strict sublevel set $\{j \in \mathbb{N} : E_j < \Lambda\}$, regarded as a finite set of
indices; it is finite because $E_j \to +\infty$.

Formalized by `NonnegativeDiscreteSpectrum.sublevelFinset`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#sublevel-finset).

## Membership in the finite strict sublevel set

For a nonnegative discrete spectrum with
eigenvalues $E_0 \le E_1 \le \cdots$, a real number $\Lambda$ and an index $j \in \mathbb{N}$, the
index $j$ lies in the finite strict sublevel set at $\Lambda$ if and only if $E_j < \Lambda$.

Formalized by `NonnegativeDiscreteSpectrum.mem_sublevelFinset`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#mem-sublevel-finset).

## Eigenvalue counting function

For a nonnegative discrete spectrum with eigenvalues
$E_0 \le E_1 \le \cdots$ and a real number $\Lambda$, the counting function $N(\Lambda)$ is the
number of indices $j \in \mathbb{N}$ with $E_j < \Lambda$, so eigenvalues are counted with
multiplicity.

Formalized by `NonnegativeDiscreteSpectrum.countingFunction`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#counting-function).

## Riesz mean

For a nonnegative discrete spectrum with eigenvalues $E_0 \le E_1 \le \cdots$
and real numbers $\sigma$ and $\Lambda$, the Riesz mean of order $\sigma$ at $\Lambda$ is the
finite sum $R_\sigma(\Lambda) = \sum_{j \in \mathbb{N},\, E_j < \Lambda} (\Lambda - E_j)^\sigma$
over indices, where $x^\sigma$ is the real power.

Formalized by `NonnegativeDiscreteSpectrum.rieszMean`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#riesz-mean).

## The Riesz mean of order zero is the counting function

For a nonnegative discrete
spectrum with eigenvalues $E_0 \le E_1 \le \cdots$ and every real number $\Lambda$, the Riesz
mean of order $0$ at $\Lambda$ equals the counting function at $\Lambda$, viewed as a real
number: $R_0(\Lambda) = N(\Lambda)$.

Every summand $(\Lambda - E_j)^0$ has strictly positive base $\Lambda - E_j$, so it equals $1$.

Formalized by `NonnegativeDiscreteSpectrum.rieszMean_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DiscreteSpectrum.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#riesz-mean-zero).

## Smooth test functions

For an open set $\Omega \subseteq \mathbb{R}^n$, the space of smooth
test functions on $\Omega$ is the real vector space of infinitely differentiable functions
$f : \mathbb{R}^n \to \mathbb{R}$ whose support is compact and contained in $\Omega$.

These functions form the core of the Dirichlet form.

Formalized by `DirichletLaplacian.SmoothTestSpace`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#smooth-test-space).

## Rayleigh quotient

For a smooth test function $f$ on an open set
$\Omega \subseteq \mathbb{R}^n$, the Rayleigh quotient of $f$ is

$$R(f) = \frac{\int_{\mathbb{R}^n} \|Df(x)\|^2 \, dx}{\int_{\mathbb{R}^n} |f(x)|^2 \, dx},$$

where $\|Df(x)\|$ is the operator norm of the derivative of $f$ at $x$ (equal to
$|\nabla f(x)|$) and both integrals are against Lebesgue measure. For $f = 0$ the quotient
$0/0$ is read as $0$.

Formalized by `DirichletLaplacian.rayleighQuotient`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#rayleigh-quotient).

## Variational eigenvalue

For an open set $\Omega \subseteq \mathbb{R}^n$ and an index
$j \ge 0$, the variational eigenvalue of $\Omega$ at index $j$ is the Courant–Fischer min–max
value

$$\lambda_j(\Omega) = \inf_V \, \sup_{f \in V,\ f \ne 0} R(f),$$

where $V$ ranges over the $(j+1)$-dimensional subspaces of the space of smooth test functions
on $\Omega$ and $R(f)$ is the Rayleigh quotient of $f$. Infima and suprema are taken in
$\mathbb{R}$, where an empty set, or a set unbounded in the relevant direction, has value $0$.

This is a definition only: it does not claim that the values are attained, nonnegative,
monotone in $j$, divergent, or eigenvalues of an operator.

Formalized by `DirichletLaplacian.variationalEigenvalue`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#variational-eigenvalue).

## Dirichlet spectrum of an open set

A nonnegative discrete spectrum $S = (S_j)_{j \ge 0}$
is the Dirichlet spectrum of an open set $\Omega \subseteq \mathbb{R}^n$ when
$S_j = \lambda_j(\Omega)$ for every $j \ge 0$, where $\lambda_j(\Omega)$ is the variational
eigenvalue of $\Omega$ at index $j$.

Formalized by `NonnegativeDiscreteSpectrum.IsDirichletSpectrum`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#is-dirichlet-spectrum).

## Volume of the unit ball

For $n \ge 0$, $\omega_n$ is the Lebesgue measure of the open
unit ball $\{x \in \mathbb{R}^n : |x| < 1\}$ of Euclidean space $\mathbb{R}^n$, as a real
number.

Formalized by `EuclideanLaplacian.unitBallVolume`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#unit-ball-volume).

## Volume of a domain

For an open set $\Omega \subseteq \mathbb{R}^n$, the volume $|\Omega|$
is the Lebesgue measure of $\Omega$ taken as a real number, with $|\Omega| = 0$ when the
Lebesgue measure of $\Omega$ is infinite.

Formalized by `EuclideanLaplacian.domainVolume`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#domain-volume).

## Semiclassical counting coefficient

For an open set $\Omega \subseteq \mathbb{R}^n$, the
semiclassical counting coefficient is $\omega_n |\Omega| / (2\pi)^n$, where $\omega_n$ is the
volume of the unit ball in $\mathbb{R}^n$ and $|\Omega|$ is the Lebesgue measure of $\Omega$
taken as a real number, with $|\Omega| = 0$ when that measure is infinite.

Formalized by `EuclideanLaplacian.semiclassicalCountingCoefficient`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#semiclassical-counting-coefficient).

## Pólya eigenvalue benchmark

For an open set $\Omega \subseteq \mathbb{R}^n$ and an index
$j \ge 0$, the Pólya benchmark at index $j$ is

$$(2\pi)^2 \left(\frac{j+1}{\omega_n |\Omega|}\right)^{2/n},$$

where $\omega_n$ is the volume of the unit ball in $\mathbb{R}^n$ and $|\Omega|$ is the volume of
$\Omega$. Indices start at $0$, so index $j$ belongs to the $(j+1)$-st eigenvalue.

Division by zero is read as $0$: the exponent is $0$ when $n = 0$, and the base is $0$ when
$\omega_n |\Omega| = 0$.

Formalized by `EuclideanLaplacian.polyaEigenvalueBenchmark`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/DirichletSpectrum.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#polya-eigenvalue-benchmark).

## Neumann Pólya benchmark

For an open set $\Omega \subseteq \mathbb{R}^n$ and a natural
number $j$, the Neumann Pólya benchmark of $\Omega$ at index $j$ is the real number
$(2\pi)^2 \left(j / (\omega_n |\Omega|)\right)^{2/n}$, where $\omega_n$ is the volume of the unit
ball of $\mathbb{R}^n$, $|\Omega|$ is the volume of $\Omega$, the power is the real power with
exponent $2/n$, and a quotient by $0$ is read as $0$.

The index is zero-based: $j$ is the source's one-based eigenvalue number minus one, so index
zero records the constant Neumann mode in positive dimension.

Formalized by `EuclideanLaplacian.neumannPolyaEigenvalueBenchmark`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NeumannPolyaBenchmark.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NeumannPolyaBenchmark.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#neumann-polya-eigenvalue-benchmark).

## Neumann and Dirichlet Pólya benchmarks agree after an index shift

For every open set
$\Omega \subseteq \mathbb{R}^n$ and every natural number $j$, the Neumann Pólya benchmark of
$\Omega$ at index $j + 1$ equals the Pólya eigenvalue benchmark of $\Omega$ at index $j$.

In the source's one-based numbering, the Neumann index $j + 2$ has the same Weyl benchmark as
the Dirichlet index $j + 1$.

Formalized by `EuclideanLaplacian.neumannPolyaEigenvalueBenchmark_succ`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NeumannPolyaBenchmark.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NeumannPolyaBenchmark.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html#neumann-polya-eigenvalue-benchmark-succ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pólya's conjecture on Laplacian eigenvalues](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/partial-differential-equations/p-lya-s-conjecture-on-laplacian-eigenvalues)
