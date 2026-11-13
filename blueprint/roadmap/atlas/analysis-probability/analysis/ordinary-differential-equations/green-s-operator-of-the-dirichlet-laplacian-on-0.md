---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.GreensOperator.L2UnitInterval, MathlibExt.Analysis.ODE.GreensOperator.sineBasisFun, MathlibExt.Analysis.ODE.GreensOperator.greensEigenvalue, MathlibExt.Analysis.ODE.GreensOperator.greensEigenvalueSqrt, MathlibExt.Analysis.ODE.GreensOperator.greensOperatorSqrt, MathlibExt.Analysis.ODE.GreensOperator.greensKernel, MathlibExt.Analysis.ODE.GreensOperator.greens_kernel_integral_sine_eq, MathlibExt.Analysis.ODE.GreensOperator.greens_operator_eigendecomposition
statement: formalized
proof: formalized
---

# Green's operator of the Dirichlet Laplacian on \[0, 1\]

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html).

## The space $L^2((0, 1))$

$L^2([0, 1])$ is the real Hilbert space of square-integrable
real-valued functions on the unit interval, up to equality almost everywhere, with Lebesgue
measure restricted to $[0, 1]$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.L2UnitInterval`, an abbreviation declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#l2-unit-interval).

## Sine basis functions on $(0, 1)$

For a positive integer $k$, the $k$-th sine basis function
is $u_k : \mathbb{R} \to \mathbb{R}$, $u_k(x) = \sqrt{2} \sin(k\pi x)$.

Restricted to $[0, 1]$, these functions form an orthonormal eigenbasis of the Green's operator with
Dirichlet boundary conditions.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.sineBasisFun`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#sine-basis-fun).

## Eigenvalues of the Dirichlet Green's operator

For a positive integer $k$, the $k$-th
eigenvalue of the Green's operator of $-\frac{d^2}{dx^2}$ on $[0, 1]$ with Dirichlet boundary
conditions $u(0) = u(1) = 0$ is $\lambda_k = \frac{1}{k^2 \pi^2}$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greensEigenvalue`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-eigenvalue).

## Square roots of the Green's operator eigenvalues

For a positive integer $k$, set
$\mu_k = \frac{1}{k\pi}$. This is the square root of the $k$-th eigenvalue $\frac{1}{k^2\pi^2}$ of
the Green's operator of $-\frac{d^2}{dx^2}$ on $[0, 1]$ with Dirichlet boundary conditions.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greensEigenvalueSqrt`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-eigenvalue-sqrt).

## Square root of the Dirichlet Green's operator

Let $L^2([0, 1])$ be the real Hilbert space
of square-integrable functions on $[0, 1]$, and let $(b_k)_{k \ge 1}$ be a Hilbert basis of
$L^2([0, 1])$ indexed by the positive integers with $b_k(x) = \sqrt{2} \sin(k\pi x)$ for almost
every $x \in [0, 1]$. Define $A^{1/2} : L^2([0, 1]) \to L^2([0, 1])$ by

$$A^{1/2} f = \sum_{k \ge 1} \frac{1}{k\pi} \langle b_k, f \rangle\, b_k.$$

Since the Green's operator acts on $b_k$ as multiplication by $\frac{1}{k^2\pi^2}$, this is its
square root.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greensOperatorSqrt`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-operator-sqrt).

## Green's kernel of the Dirichlet Laplacian on $(0, 1)$

For real numbers $x$ and $t$, set
$G(x, t) = \min(x, t)\,(1 - \max(x, t))$.

On $[0, 1]$ this is the Green's kernel of $-\frac{d^2}{dx^2}$ with boundary conditions
$u(0) = u(1) = 0$: the operator $f \mapsto \int_0^1 G(\cdot, t) f(t)\, dt$ inverts
$-\frac{d^2}{dx^2}$ under these conditions.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greensKernel`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-kernel).

## Green's kernel eigenfunction identity for sines

Let $k$ be a positive integer, let
$G(x, t) = \min(x, t)\,(1 - \max(x, t))$ be the Green's kernel, and let
$u_k(x) = \sqrt{2} \sin(k\pi x)$ and $\lambda_k = \frac{1}{k^2\pi^2}$. Then for every
$x \in [0, 1]$,

$$\int_0^1 G(x, t)\, u_k(t)\, dt = \lambda_k\, u_k(x).$$

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greens_kernel_integral_sine_eq`, a lemma declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-kernel-integral-sine-eq).

## Spectral decomposition of the Dirichlet Green's operator

Write $L^2([0, 1])$ for the real
Hilbert space of square-integrable functions on $[0, 1]$ with Lebesgue measure, let
$G(x, t) = \min(x, t)\,(1 - \max(x, t))$ be the Green's kernel, and for each positive integer $k$
let $u_k(x) = \sqrt{2} \sin(k\pi x)$ and $\lambda_k = \frac{1}{k^2\pi^2}$. Let $A$ be a linear map
from $L^2([0, 1])$ to itself that is symmetric, $\langle Af, g \rangle = \langle f, Ag \rangle$ for
all $f, g$, and is given by the Green's kernel, $(Af)(x) = \int_{[0, 1]} G(x, t) f(t)\, dt$ for
almost every $x \in [0, 1]$ and every $f$. Let $(b_k)_{k \ge 1}$ be a Hilbert basis of
$L^2([0, 1])$ indexed by the positive integers with $b_k = u_k$ almost everywhere on $[0, 1]$.
Then $A$ is injective, each $b_k$ is an eigenvector of $A$ with eigenvalue $\lambda_k$, and every
$f \in L^2([0, 1])$ satisfies $Af = \sum_{k \ge 1} \lambda_k \langle b_k, f \rangle\, b_k$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.greens_operator_eigendecomposition`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-operator-eigendecomposition).

## Orthonormality of the sine basis on the unit interval

The canonical sine basis is orthonormal on the unit interval, in product-integral form.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.sine_product_integral`, a lemma declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#sine-product-integral).

## The sine Hilbert basis of $L^2((0, 1))$

The sine Hilbert basis is a Hilbert basis
$(b_k)_{k \ge 1}$ of the real Hilbert space $L^2([0, 1])$, indexed by the positive integers, with
$b_k(x) = \sqrt{2} \sin(k\pi x)$ for almost every $x \in [0, 1]$. Such a basis exists, and since an
element of $L^2([0, 1])$ is determined by its values almost everywhere, it is unique.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.sineHilbertBasis`, a definition declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#sine-hilbert-basis).

## The sine Hilbert basis consists of sine functions

For every positive integer $k$, the
$k$-th element $b_k$ of the sine Hilbert basis of $L^2([0, 1])$ satisfies
$b_k(x) = \sqrt{2} \sin(k\pi x)$ for almost every $x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperator.sineHilbertBasis_coe`, a lemma declared in [MathlibExt/Analysis/ODE/GreensOperator.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperator.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#sine-hilbert-basis-coe).

## Dirichlet eigenvalues of the Laplacian on the unit interval

The `k`-th Dirichlet eigenvalue: `λ_k = (kπ)²`, the eigenvalue of
`-d²/dx²` for the eigenfunction `sineBasisFun k`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletLaplacianEigenvalue`, a definition declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-laplacian-eigenvalue).

## Pointwise derivative of a Dirichlet sine eigenfunction

First derivative of the `k`-th sine eigenfunction.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-has-deriv-at).

## Derivative function of a Dirichlet sine eigenfunction

The derivative of the `k`-th sine eigenfunction, as a function.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_deriv`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-deriv).

## Second derivative of a Dirichlet sine eigenfunction

Second-derivative (eigenvalue) equation for the `k`-th sine
eigenfunction: `u_k'' = -(kπ)² u_k`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_iteratedDeriv_two`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-iterated-deriv-two).

## Dirichlet eigenvalue equation in Sturm-Liouville form

The Dirichlet eigenvalue equation in Sturm-Liouville form:
`-u_k'' = λ_k u_k` with `λ_k = (kπ)²`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.neg_iteratedDeriv_two_eq`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#neg-iterated-deriv-two-eq).

## Sine eigenfunctions vanish at the left endpoint

Left Dirichlet boundary value: `u_k(0) = 0`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_zero`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-zero).

## Sine eigenfunctions vanish at the right endpoint

Right Dirichlet boundary value: `u_k(1) = 0`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_one`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-one).

## Smoothness of the Dirichlet sine eigenfunctions

The sine eigenfunctions are smooth.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_contDiff`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-cont-diff).

## Dirichlet sine eigenfunctions are nonzero

The sine eigenfunctions are nonzero (so they are genuine
eigenfunctions, not the trivial solution). The witness point is
`x = 1 / (2k)`, where `u_k = √2`.

Formalized by `MathlibExt.Analysis.ODE.DirichletSineEigenfunctions.dirichletSine_ne_zero`, a theorem declared in [MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/DirichletSineEigenfunctions.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#dirichlet-sine-ne-zero).

## The square root of the Green's operator is a diagonal operator

Let $(b_k)_{k \ge 1}$ be
a Hilbert basis of $L^2([0, 1])$ indexed by the positive integers with
$b_k(x) = \sqrt{2} \sin(k\pi x)$ for almost every $x \in [0, 1]$, let $\mu_k = \frac{1}{k\pi}$,
and let $C$ be a real number with $|\mu_k| \le C$ for every $k$. Then for every
$f \in L^2([0, 1])$, the square root $A^{1/2} f$ of the Green's operator defined from $(b_k)$
equals $D f$, where $D$ is the bounded diagonal operator with coefficients $(\mu_k)$ in the
basis $(b_k)$ and coefficient bound $C$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorSqrtSquared.greensOperatorSqrt_eq_diagonal`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorSqrtSquared.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorSqrtSquared.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-operator-sqrt-eq-diagonal).

## The square root of the Green's operator squares to the Green's operator

Let
$G(x, t) = \min(x, t)\,(1 - \max(x, t))$ be the Green's kernel and let $A$ be a linear map from
$L^2([0, 1])$ to itself that is symmetric, $\langle Af, g \rangle = \langle f, Ag \rangle$ for all
$f, g$, and is given by the Green's kernel, $(Af)(x) = \int_{[0, 1]} G(x, t) f(t)\, dt$ for almost
every $x \in [0, 1]$ and every $f$. Let $(b_k)_{k \ge 1}$ be a Hilbert basis of $L^2([0, 1])$
indexed by the positive integers with $b_k(x) = \sqrt{2} \sin(k\pi x)$ for almost every
$x \in [0, 1]$, and let $A^{1/2}$ be the square root of the Green's operator defined from
$(b_k)$. Then $A^{1/2}(A^{1/2} f) = Af$ for every $f \in L^2([0, 1])$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorSqrtSquared.greensOperatorSqrt_sq`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorSqrtSquared.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorSqrtSquared.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-operator-sqrt-sq).

## The Green's eigenvalues are summable

The Green's eigenvalues
$\lambda_k = 1/(k^2\pi^2)$, indexed by the positive integers $k$, form a summable family of real
numbers.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.summable_greensEigenvalues`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#summable-greens-eigenvalues).

## The Green's eigenvalues tend to zero

The Green's eigenvalues
$\lambda_k = 1/(k^2\pi^2)$ tend to $0$ along the cofinite filter on the positive integers, that
is, $\lambda_k \to 0$ as $k \to \infty$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.tendsto_cofinite_greensEigenvalues`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#tendsto-cofinite-greens-eigenvalues).

## Sum of the Green's eigenvalues

For the Green's eigenvalues $\lambda_k = 1/(k^2\pi^2)$,
indexed by the positive integers $k$, we have $\sum_{k \ge 1} \lambda_k = 1/6$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.tsum_greensEigenvalues`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#tsum-greens-eigenvalues).

## Sum of the squared Green's eigenvalues

For the Green's eigenvalues
$\lambda_k = 1/(k^2\pi^2)$, indexed by the positive integers $k$, we have
$\sum_{k \ge 1} \lambda_k^2 = 1/90$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.tsum_greensEigenvalues_sq`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#tsum-greens-eigenvalues-sq).

## Diagonal integral of the Green's kernel

The Green's kernel $G$ on $[0, 1]$ satisfies
$\int_0^1 G(x, x)\,dx = 1/6$, since $G(x, x) = x(1 - x)$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.integral_greensKernel_diag`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#integral-greens-kernel-diag).

## The Green's eigenvalues sum to the diagonal integral of the kernel

The sum of the
Green's eigenvalues $\lambda_k = 1/(k^2\pi^2)$ over the positive integers $k$ equals the integral
of the Green's kernel $G$ along the diagonal: $\sum_{k \ge 1} \lambda_k = \int_0^1 G(x, x)\,dx$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.greens_eigenvalue_sum_eq_kernel_diagonal_integral`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#greens-eigenvalue-sum-eq-kernel-diagonal).

## Squared Hilbert–Schmidt norm of the Green's operator

Let
$G(x, t) = \min(x, t)\,(1 - \max(x, t))$ be the Green's kernel and let $A$ be a continuous linear
operator on $L^2([0, 1])$ that is symmetric, $\langle Af, g \rangle = \langle f, Ag \rangle$ for
all $f, g$, and is given by the Green's kernel, $(Af)(x) = \int_{[0, 1]} G(x, t) f(t)\, dt$ for
almost every $x \in [0, 1]$ and every $f$. Let $(b_k)_{k \ge 1}$ be the sine Hilbert basis of
$L^2([0, 1])$. Then the squared Hilbert–Schmidt norm of $A$ in the family $(b_{n+1})_{n \ge 0}$
equals $1/90$, that is, $\sum_{n \ge 0} \|A b_{n+1}\|^2 = 1/90$, the sum being taken in
$[0, \infty]$.

Formalized by `MathlibExt.Analysis.ODE.GreensOperatorTrace.hsNormSq_greensOperator`, a theorem declared in [MathlibExt/Analysis/ODE/GreensOperatorTrace.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/GreensOperatorTrace.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html#hs-norm-sq-greens-operator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Green's operator of the Dirichlet Laplacian on \[0, 1\]](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/ordinary-differential-equations/green-s-operator-of-the-dirichlet-laplacian-on-0)
