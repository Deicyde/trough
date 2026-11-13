---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FiniteTimeSingularityWanted.IsBoundedFunOn, MathlibExt.Analysis.FiniteTimeSingularityWanted.IsBoundedFun, MathlibExt.Analysis.FiniteTimeSingularityWanted.Holder, MathlibExt.Analysis.FiniteTimeSingularityWanted.HolderOn, MathlibExt.Analysis.FiniteTimeSingularityWanted.IsContDiffHolder, MathlibExt.Analysis.FiniteTimeSingularityWanted.IsContDiffHolderOn, MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.directionalDeriv, MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.timeDeriv
statement: formalized
---

# Singularity formation for the Euler equations

15 results, 14 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html).

## Bounded and Hölder continuous functions

## Functions bounded on a set

A function $f : \beta \to \alpha$ into a space $\alpha$ with a
bornology is bounded on a set $s \subseteq \beta$ if the image $f(s)$ is a bounded subset of
$\alpha$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.IsBoundedFunOn`, an abbreviation declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-bounded-fun-on).

## Bounded functions

A function $f : \beta \to \alpha$ into a space $\alpha$ with a
bornology is bounded if its range $f(\beta)$ is a bounded subset of $\alpha$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.IsBoundedFun`, an abbreviation declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-bounded-fun).

## Hölder continuity

Let $X$ and $Y$ be pseudo-extended metric spaces (distances take
values in $[0, \infty]$), let $r \ge 0$ be a real number and $f : X \to Y$. Then $f$ is
$r$-Hölder if there is a constant $C \ge 0$ such that
$d_Y(f(x_1), f(x_2)) \le C \, d_X(x_1, x_2)^r$ for all $x_1, x_2 \in X$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.Holder`, an abbreviation declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#holder).

## Hölder continuity on a set

Let $X$ and $Y$ be pseudo-extended metric spaces (distances
take values in $[0, \infty]$), let $r \ge 0$ be a real number, $s \subseteq X$ and $f : X \to Y$.
Then $f$ is $r$-Hölder on $s$ if there is a constant $C \ge 0$ such that
$d_Y(f(x_1), f(x_2)) \le C \, d_X(x_1, x_2)^r$ for all $x_1, x_2 \in s$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.HolderOn`, an abbreviation declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#holder-on).

## Continuously differentiable functions with Hölder derivative

Let $\mathbb{k}$ be a
nontrivially normed field, $E$ and $F$ normed spaces over $\mathbb{k}$ and $\alpha \ge 0$ a real
number. A function $f : E \to F$ is in $C^{1,\alpha}(E)$ if $f$ is continuously differentiable
over $\mathbb{k}$ and its derivative $Df$, a map from $E$ to the space $L(E, F)$ of continuous
$\mathbb{k}$-linear maps with the operator norm, is bounded and $\alpha$-Hölder.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.IsContDiffHolder`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-cont-diff-holder).

## Continuously differentiable functions with Hölder derivative on a set

Let $\mathbb{k}$
be a nontrivially normed field, $E$ and $F$ normed spaces over $\mathbb{k}$, $s \subseteq E$ and
$\alpha \ge 0$ a real number. A function $f : E \to F$ is in $C^{1,\alpha}(s)$ if $f$ is
continuously differentiable on $s$ over $\mathbb{k}$ and its derivative within $s$, a map from
$E$ to the space $L(E, F)$ of continuous $\mathbb{k}$-linear maps with the operator norm, is
bounded on $s$ and $\alpha$-Hölder on $s$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.IsContDiffHolderOn`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-cont-diff-holder-on).

## Spatial directional derivative of a time-dependent vector field

Given
$u, v : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}^3$, the spatial directional derivative
$(u \cdot \nabla_x) v$ of $v$ in the direction of $u$ is the function
$(x, t) \mapsto D_x v(x, t)\,[u(x, t)]$, where $D_x v(x, t)$ is the Fréchet derivative of
$y \mapsto v(y, t)$ at $x$ (taken to be $0$ if this map is not differentiable at $x$).

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.directionalDeriv`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#directional-deriv).

## Time derivative

For a function $u(x, t) \in \mathbb{R}^3$ of a point $x \in \mathbb{R}^3$
and a time $t \in \mathbb{R}$, the time derivative $\partial_t u(x, t) \in \mathbb{R}^3$ is the
derivative at $t$ of the function $s \mapsto u(x, s)$, taken to be $0$ when that function is not
differentiable at $t$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.timeDeriv`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#time-deriv).

## Spatial gradient

For a function $p(x, t)$ of a point $x \in \mathbb{R}^3$ and a time
$t \in \mathbb{R}$, the spatial gradient $\nabla_x p(x, t) \in \mathbb{R}^3$ is the gradient at $x$
of the function $y \mapsto p(y, t)$, taken to be $0$ when that function is not differentiable
at $x$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.spaceGrad`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#space-grad).

## Divergence

The divergence of a vector field $u : \mathbb{R}^3 \to \mathbb{R}^3$ at a point
$x \in \mathbb{R}^3$ is the trace of the Fréchet derivative $Du(x)$, a linear map from
$\mathbb{R}^3$ to $\mathbb{R}^3$ (taken to be $0$ if $u$ is not differentiable at $x$).

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.div`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#div).

## Standard basis vectors of ℝ³

For $i \in \{0, 1, 2\}$, $e_i \in \mathbb{R}^3$ is the
$i$-th standard basis vector: its $i$-th coordinate is $1$ and its other coordinates are $0$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.e`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#e).

## Vorticity

The vorticity of a vector field $u : \mathbb{R}^3 \to \mathbb{R}^3$ is its curl
$(\nabla \times u)(x) = \sum_{i=1}^{3} e_i \times Du(x)\,e_i$, where $e_1, e_2, e_3$ is the
standard basis of $\mathbb{R}^3$, $\times$ is the cross product and $Du(x)\,e_i$ is the partial
derivative of $u$ at $x$ in direction $e_i$ (all taken to be $0$ when $u$ is not differentiable
at $x$).

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.vorticity`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#vorticity).

## Local solutions of the incompressible Euler equations

Let $T \in \mathbb{R}$, let
$u_0 : \mathbb{R}^3 \to \mathbb{R}^3$, and let $p : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}$
and $u : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}^3$. Write $\partial_t u$ for the time
derivative of $u$, $(u \cdot \nabla_x) u$ for the spatial directional derivative of $u$ in the
direction of $u$, and $\nabla_x p$ for the spatial gradient of $p$. Then $u$ is a local solution
of the incompressible Euler equations up to time $T$, with pressure $p$ and initial data $u_0$,
if $u$ and $p$ are continuously differentiable, as functions of $(x, t)$, on
$\mathbb{R}^3 \times [0, T)$, if for all $x \in \mathbb{R}^3$ and $t \in (0, T)$

$$\partial_t u(x, t) + (u \cdot \nabla_x) u(x, t) + \nabla_x p(x, t) = 0,$$

if for every $t \in (0, T)$ the divergence of $u(\cdot, t)$ is $0$ at every point of
$\mathbb{R}^3$, and if $u(\cdot, 0) = u_0$.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.IsLocalEulerEquationSolution`, a structure declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-local-euler-equation-solution).

## Odd vector fields in three dimensions

A vector field $u : \mathbb{R}^3 \to \mathbb{R}^3$
with components $u_1, u_2, u_3$ is odd if, for each $i \in \{1, 2, 3\}$, the component $u_i$ is an
odd function of the $i$-th coordinate and an even function of each of the other two coordinates,
when the remaining coordinates are held fixed.

Formalized by `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.IsOdd`, a definition declared in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#is-odd).

## Elgindi's theorem: finite-time singularity of $C^{1,\alpha}$ Euler flows

There exist a
real number $\alpha > 0$ and a vector field $u_0 : \mathbb{R}^3 \to \mathbb{R}^3$ that is odd,
has divergence $0$ at every point and lies in $C^{1,\alpha}(\mathbb{R}^3)$, together with a
constant $C > 0$ such that its vorticity satisfies
$|(\nabla \times u_0)(x)| \le C / (|x|^\alpha + 1)$ for every $x \in \mathbb{R}^3$, and there
exist functions $p : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}$ and
$u : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}^3$ such that $u(\cdot, t)$ is odd for every
$t \in [0, 1)$, $u$ is a local solution of the incompressible Euler equations up to time $1$
with pressure $p$ and initial data $u_0$, $u$ lies in $C^{1,\alpha}(\mathbb{R}^3 \times [0, T])$
as a function of $(x, t)$ for every $T \in (0, 1)$, and

$$\int_0^t \sup_{x \in \mathbb{R}^3} |(\nabla \times u(\cdot, s))(x)| \, ds \to +\infty$$

as $t \to 1^-$. Here $|\cdot|$ is the Euclidean norm, differentiability is over $\mathbb{R}$, and
$\mathbb{R}^3 \times \mathbb{R}$ carries the norm $\max(|x|, |t|)$.

Elgindi states the conclusion for the unique local odd solution in this class. Uniqueness of
solutions up to any time $T$ at which they exist was already known, so only existence is
asserted here.

## Sources

- T. M. Elgindi, `Finite-time singularity formation for C^{1,α} solutions to the incompressible Euler equations on ℝ³`, Annals of Math, 194 (3) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_finite_time_singularity` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FiniteTimeSingularityWanted.FiniteTimeSingularity.theorem_1` is written with `theorem_wanted` in [WantedExt/Analysis/FiniteTimeSingularityWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FiniteTimeSingularityWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html#theorem-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Singularity formation for the Euler equations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/partial-differential-equations/singularity-formation-for-the-euler-equations)
