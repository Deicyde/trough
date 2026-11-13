---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.eC1NormOn, MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.H, MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.frobeniusNorm, MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.σ₂, MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.theorem_1_1
statement: formalized
---

# Hessian estimates for the σ₂ equation

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html).

## C¹ norm on a set

Let $E$ and $F$ be real normed spaces and let $\mu$ be a measure on $E$
(by default the volume measure). For a function $f : E \to F$ and a set $s \subseteq E$, write
$\mu_s$ for the restriction of $\mu$ to $s$. The $C^1$ norm of $f$ on $s$ is the extended
nonnegative real number

$$\|f\|_{C^1(s)} = \|f\|_{L^\infty(\mu_s)} + \|Df\|_{L^\infty(\mu_s)},$$

where $\|g\|_{L^\infty(\mu_s)}$ is the $\mu_s$-essential supremum of $\|g\|$, and $Df$ is the
Fréchet derivative of $f$ on all of $E$ (taken to be $0$ at points where $f$ is not
differentiable), a function from $E$ to the continuous linear maps $E \to F$, measured in the
operator norm.

Formalized by `MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.eC1NormOn`, a definition declared in [WantedExt/Analysis/HessianEstimatesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HessianEstimatesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html#e-c1-norm-on).

## Hessian operator within a set

Let $E$ be a real Hilbert space, let $f : E \to \mathbb{R}$,
let $s \subseteq E$ and let $x \in E$. Write $D^2 f(x)$ for the second Fréchet derivative of $f$
within $s$ at $x$, that is, the derivative within $s$ at $x$ of the map sending $y$ to the
derivative of $f$ within $s$ at $y$; it is a continuous bilinear form on $E$. The Hessian
operator of $f$ within $s$ at $x$ is the continuous linear map $Hf(x) : E \to E$ determined by
$\langle Hf(x)\, u, v \rangle = D^2 f(x)(u, v)$ for all $u, v \in E$.

Formalized by `MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.H`, a definition declared in [WantedExt/Analysis/HessianEstimatesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HessianEstimatesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html#h).

## Frobenius norm

Let $E$ and $F$ be finite-dimensional real inner product spaces. The
Frobenius norm of a continuous linear map $T : E \to F$ is
$\|T\|_F = \sqrt{\operatorname{tr}(T^* T)}$, where $T^* : F \to E$ is the adjoint of $T$ and the
trace is taken on $E$.

Formalized by `MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.frobeniusNorm`, a definition declared in [WantedExt/Analysis/HessianEstimatesWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HessianEstimatesWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html#frobenius-norm).

## Second elementary symmetric function of the eigenvalues

Let $E$ be a finite-dimensional
real inner product space of dimension $n$. If $T : E \to E$ is a symmetric linear map with
eigenvalues $\lambda_1, \dots, \lambda_n$, listed with multiplicity, then
$\sigma_2(T) = \sum_{1 \le i < j \le n} \lambda_i \lambda_j$. If $T$ is not symmetric, then
$\sigma_2(T) = 0$ by convention.

Formalized by `MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.σ₂`, a definition declared in [WantedExt/Analysis/HessianEstimatesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HessianEstimatesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html#untitled).

## Shankar–Yuan Hessian estimate for the sigma-2 equation in dimension four

There is a function
$C : [0, \infty] \to \mathbb{R}$ with the following property. Let $B_1(0)$ be the open unit ball in
$\mathbb{R}^4$, and let $u : \mathbb{R}^4 \to \mathbb{R}$ be smooth ($C^\infty$) on $B_1(0)$ with
finite $C^1$ norm $\|u\|_{C^1(B_1(0))}$ with respect to Lebesgue measure. Suppose that for every
$x \in B_1(0)$ the Laplacian satisfies $\Delta u(x) > 0$ and the Hessian operator $Hu(x)$ of $u$
within $B_1(0)$ satisfies $\sigma_2(Hu(x)) = 1$, where $\sigma_2$ of a symmetric operator is the
second elementary symmetric function of its eigenvalues and $\sigma_2$ of a non-symmetric operator
is $0$. Then the Frobenius norm of the Hessian operator at the origin satisfies
$\|Hu(0)\|_F \le C(\|u\|_{C^1(B_1(0))})$.

## Sources

- R. Shankar and Y. Yuan, `Hessian estimates for the sigma-2 equation in dimension four`, Annals of Math, 201 (2) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_hessian_estimates` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HessianEstimatesWanted.HessianEstimates.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Analysis/HessianEstimatesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HessianEstimatesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hessian estimates for the σ₂ equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/partial-differential-equations/hessian-estimates-for-the-equation)
