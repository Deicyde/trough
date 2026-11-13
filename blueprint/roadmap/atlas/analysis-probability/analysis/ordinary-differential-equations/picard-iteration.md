---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_converge, MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_tendsto_of_hasDerivAt, MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_step_estimate
statement: formalized
proof: formalized
---

# Picard iteration

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/picard-iteration/index.html).

## Picard iterates converge

Let $E$ be a real Banach space, let
$f : \mathbb{R} \times E \to E$ be continuous, and let $L \ge 0$ be such that $f(t, \cdot)$ is
$L$-Lipschitz for every $t \in \mathbb{R}$. Fix $t_0 \in \mathbb{R}$ and $x_0 \in E$, and let
$(u_n)_{n \ge 0}$ be maps $\mathbb{R} \to E$ with $u_0(t) = x_0$ and
$u_{n+1}(t) = x_0 + \int_{t_0}^{t} f(s, u_n(s))\,ds$ for all $n$ and $t$. Then there is a map
$x : \mathbb{R} \to E$ with $x(t_0) = x_0$ and $x'(t) = f(t, x(t))$ for every $t \in \mathbb{R}$,
such that $u_n(t) \to x(t)$ as $n \to \infty$ for every $t \in \mathbb{R}$.

Proof: Sum the factorially bounded successive differences, obtaining locally uniform convergence
on every compact time interval. Pass the recursion through the integral and apply the fundamental
theorem of calculus. This is the argument of Teschl, Theorem 2.5 and Corollary 2.6 (Section 2.3),
for the Picard iterates (2.13) of Section 2.2, with a constant global Lipschitz constant.

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 2.3; stable ref https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem.

Formalized by `MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_converge`, a theorem declared in [MathlibExt/Analysis/ODE/PicardIteration.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/PicardIteration.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/picard-iteration/index.html#picard-iterates-converge).

## Picard iterates converge to every global solution of the initial value problem

Let $E$
be a real Banach space, let $f : \mathbb{R} \times E \to E$ be continuous, and let $L \ge 0$ be
such that $f(t, \cdot)$ is $L$-Lipschitz for every $t \in \mathbb{R}$. Fix $t_0 \in \mathbb{R}$
and $x_0 \in E$, and let $(u_n)_{n \ge 0}$ be maps $\mathbb{R} \to E$ with $u_0(t) = x_0$ and
$u_{n+1}(t) = x_0 + \int_{t_0}^{t} f(s, u_n(s))\,ds$ for all $n$ and $t$. If $y : \mathbb{R} \to E$
satisfies $y(t_0) = x_0$ and $y'(t) = f(t, y(t))$ for every $t \in \mathbb{R}$, then
$u_n(t) \to y(t)$ as $n \to \infty$ for every $t \in \mathbb{R}$.

Proof: By the convergence of Picard iterates, the iterates converge pointwise to a global solution
through $x_0$ at $t_0$; by uniqueness of solutions for a Lipschitz right-hand side, it equals $y$.

Formalized by `MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_tendsto_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/ODE/PicardIteration.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/PicardIteration.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/picard-iteration/index.html#picard-iterates-tendsto-of-has-deriv-at).

## Step estimate for Picard iterates

Let $E$ be a real normed space, let
$f : \mathbb{R} \times E \to E$ be continuous, and let $L \ge 0$ be such that $f(t, \cdot)$ is
$L$-Lipschitz for every $t \in \mathbb{R}$. Fix $t_0 \in \mathbb{R}$ and $x_0 \in E$, and let
$(u_n)_{n \ge 0}$ be maps $\mathbb{R} \to E$ with $u_0(t) = x_0$ and
$u_{n+1}(t) = x_0 + \int_{t_0}^{t} f(s, u_n(s))\,ds$ for all $n$ and $t$. If $M$ is a real number
with $\|f(s, x_0)\| \le M$ for every $s \in \mathbb{R}$, then for every $n \ge 0$ and every
$t \in \mathbb{R}$, $\|u_{n+1}(t) - u_n(t)\| \le M L^n |t - t_0|^{n+1} / (n+1)!$.

The integral is the Bochner integral, which is taken to be $0$ when $E$ is not complete.

Proof: Induct on the iterate index, apply the Lipschitz bound under the interval integral, and
integrate the absolute-power majorant exactly, as in the induction for estimate (2.29) in the proof
of Teschl, Theorem 2.5 (Section 2.3).

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 2.3.

Formalized by `MathlibExt.Analysis.ODE.PicardIterationWanted.picard_iterates_step_estimate`, a theorem declared in [MathlibExt/Analysis/ODE/PicardIteration.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ODE/PicardIteration.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/picard-iteration/index.html#picard-iterates-step-estimate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Picard iteration](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/picard-iteration/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/ordinary-differential-equations/picard-iteration)
