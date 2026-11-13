---
declaration: section
origin: cited
lean: MetaMathlibExt.gradient_descent_convex_sublinear_rate, gradientDescentTrajectory, IsUnitSmoothConvex, GradientDescentUniformRate, gradientDescentExponent, gradientDescentSilverRatio, silverGradientDescentExponent, silverGradientDescentSchedule
statement: formalized
proof: formalized
---

# Gradient descent

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html).

## Sublinear rate of gradient descent for smooth convex functions

Let $E$ be a
finite-dimensional real inner product space, let $L > 0$, and let $f : E \to \mathbb{R}$ be
convex and differentiable with $L$-Lipschitz gradient $\nabla f$. Let $x^\star \in E$ be a global
minimizer of $f$, let $0 < \eta \le 1/L$, and let $(x_k)_{k \ge 0}$ be any sequence in $E$ with
$x_{k+1} = x_k - \eta \nabla f(x_k)$ for all $k$. Then for every $k \ge 1$,
$f(x_k) - f(x^\star) \le \|x_0 - x^\star\|^2 / (2 \eta k)$.

Proof: The descent lemma and first-order convexity inequality are proved on affine lines. They
bound each objective gap by a difference of squared distances to $x^\star$; telescoping and the
monotonicity of $f(x_k)$ in $k$ give the rate, as in L. Vandenberghe, ECE236C lecture notes
"Gradient method" (Spring 2022), slides 1.23-1.26.

## Sources

- Y. Nesterov, Introductory Lectures on Convex Optimization, Section 2.1; https://en.wikipedia.org/wiki/Gradient_descent.

Formalized by `MetaMathlibExt.gradient_descent_convex_sublinear_rate`, a theorem declared in [MathlibExt/Analysis/Convex/GradientDescent.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescent.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-convex-sublinear-rate).

## Gradient descent with a step schedule

Let $E$ be a real Hilbert space,
$f : E \to \mathbb{R}$, $s : \mathbb{N} \to \mathbb{R}$ a sequence of step sizes and $x_0 \in E$.
The gradient descent trajectory of $f$ from $x_0$ with steps $s$ is the sequence
$(x_k)_{k \in \mathbb{N}}$ in $E$ starting at $x_0$ with $x_{k+1} = x_k - s_k \nabla f(x_k)$.

Here $\nabla f(x)$ is taken to be $0$ at points $x$ where $f$ is not differentiable.

Formalized by `gradientDescentTrajectory`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-trajectory).

## Convex functions with $1$-Lipschitz gradient

A function $f : E \to \mathbb{R}$ on a real
Hilbert space $E$ is unit-smooth convex if it is convex, differentiable, and its gradient is
$1$-Lipschitz: $\lVert \nabla f(x) - \nabla f(y) \rVert \le \lVert x - y \rVert$ for all
$x, y \in E$.

Formalized by `IsUnitSmoothConvex`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#is-unit-smooth-convex).

## Uniform last-iterate rate of a step schedule

A step schedule
$s : \mathbb{N} \to \mathbb{R}$ achieves a uniform last-iterate rate with exponent
$c \in \mathbb{R}$ if there are a real number $C > 0$ and an integer $K \ge 1$ with the following
property. For every $d \in \mathbb{N}$, every convex differentiable function
$f : \mathbb{R}^d \to \mathbb{R}$ whose gradient is $1$-Lipschitz for the Euclidean norm, every
$x^\star \in \mathbb{R}^d$ with $f(x^\star) \le f(x)$ for all $x$, every $x_0 \in \mathbb{R}^d$ and
every integer $k \ge K$, the $k$-th gradient descent iterate $x_k$ of $f$ from $x_0$ with steps
$s$ satisfies

$$f(x_k) - f(x^\star) \le \frac{C \lVert x_0 - x^\star \rVert^2}{k^c}.$$

The constants $C$ and $K$ are chosen before, and do not depend on, $d$, $f$, $x^\star$, $x_0$
and $k$.

Formalized by `GradientDescentUniformRate`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-uniform-rate).

## The gradient descent exponent

The gradient descent exponent is the supremum, in the
extended reals $[-\infty, +\infty]$, of the set of real numbers $c$ such that some step schedule
$s : \mathbb{N} \to \mathbb{R}$ achieves a uniform last-iterate rate with exponent $c$. In
particular, it is $-\infty$ if there is no such $c$, and $+\infty$ if these exponents are
unbounded above.

## Sources

- OptimizationProblems, `constants/35a.md` (constant C35).

Formalized by `gradientDescentExponent`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-exponent).

## Silver ratio

The silver ratio is the real number $\rho = 1 + \sqrt{2}$.

It is the ratio used by the stepsize-hedging (silver) step schedule.

Formalized by `gradientDescentSilverRatio`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-silver-ratio).

## Silver exponent

The silver exponent is $\log_2 \rho = \log \rho / \log 2$, where
$\rho = 1 + \sqrt{2}$ is the silver ratio.

It is the catalogue's proposed optimal value of the gradient descent exponent.

Formalized by `silverGradientDescentExponent`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#silver-gradient-descent-exponent).

## Silver step schedule

The silver step schedule is the sequence
$s_t = 1 + \rho^{\nu_2(t + 1) - 1}$ for $t \in \mathbb{N}$, where $\rho = 1 + \sqrt{2}$ is the
silver ratio and $\nu_2(n)$ is the exponent of $2$ in the prime factorization of $n$.

The exponent $\nu_2(t + 1) - 1$ is an integer and equals $-1$ for even $t$, where
$s_t = 1 + \rho^{-1} = \sqrt{2}$.

Formalized by `silverGradientDescentSchedule`, a definition declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#silver-gradient-descent-schedule).

## Constant unit steps achieve exponent one

The step schedule with every step size equal to
$1$ achieves a uniform last-iterate rate with exponent $1$.

This follows from the fixed-step descent theorem; it is a lower bound for the gradient descent
exponent, not its conjectured optimal value.

Formalized by `gradientDescentUniformRate_one`, a theorem declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-uniform-rate-one).

## The gradient descent exponent is at least one

The gradient descent exponent is at
least $1$.

Formalized by `one_le_gradientDescentExponent`, a theorem declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#one-le-gradient-descent-exponent).

## Gradient descent with zero step sizes stays put

Let $E$ be a real Hilbert space,
$f : E \to \mathbb{R}$ and $x_0 \in E$. If every step size is $0$, then for every $k \in \mathbb{N}$
the $k$-th gradient descent iterate of $f$ from $x_0$ equals $x_0$.

Formalized by `gradientDescentTrajectory_zeroSchedule`, a theorem declared in [MathlibExt/Analysis/Convex/GradientDescentExponent.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/GradientDescentExponent.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html#gradient-descent-trajectory-zero-schedul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gradient descent](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/gradient-descent/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/convex-analysis-and-variations/gradient-descent)
