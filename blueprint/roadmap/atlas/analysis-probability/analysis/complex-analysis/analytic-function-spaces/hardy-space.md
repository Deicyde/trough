---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_sq_szego_coeff, MathlibExt.Analysis.InnerProductSpace.HardySpace.memℓp_szegoKernel, MathlibExt.Analysis.InnerProductSpace.HardySpace.szegoKernel, MathlibExt.Analysis.InnerProductSpace.HardySpace.szegoKernel_zero, MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_sq_szegoKernel, MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_szegoKernel, MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval, MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval_eq_tsum
statement: formalized
---

# Hardy space

20 results, 19 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html).

## Squared norms of the Szegő kernel coefficients

The squared norms of the Szegő kernel coefficients form a geometric
progression with ratio `‖z‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_sq_szego_coeff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#norm-sq-szego-coeff).

## Szegő kernel coefficients lie in ℓ²

The Szegő kernel coefficients are in `ℓ²` when `z` is in the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.memℓp_szegoKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#mem-p-szego-kernel).

## Szegő kernel of the Hardy space

The **Szegő kernel** at `z`: the `ℓ²(ℕ, ℂ)` sequence with
coefficients `(conj z)ⁿ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.szegoKernel`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#szego-kernel).

## Szegő kernel at the origin is the first basis vector

The Szegő kernel at `0` is the first standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.szegoKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#szego-kernel-zero).

## Squared norm of the Szegő kernel

The squared norm of the Szegő kernel is `1 / (1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_sq_szegoKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#norm-sq-szego-kernel).

## Norm of the Szegő kernel

The norm of the Szegő kernel is `1 / √(1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_szegoKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#norm-szego-kernel).

## Point evaluation on the Hardy space

Point evaluation on `H²(𝔻)`: the inner product with the Szegő kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval).

## Hardy-space point evaluation as a Taylor series

Point evaluation is the Taylor series `∑' n, a n * zⁿ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval-eq-tsum).

## Absolute convergence of Taylor series in the Hardy space

The Taylor series of an `H²` function converges absolutely at every
point of the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.summable_hardyEval_terms`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#summable-hardy-eval-terms).

## Point evaluation as a bounded functional on the Hardy space

Point evaluation as a bounded linear functional on `H²(𝔻)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEvalCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval-clm).

## Reproducing property of the Szegő kernel

The bounded point-evaluation functional acts by the inner product
with the Szegő kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEvalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval-clm-apply).

## Norm of Hardy-space point evaluation

The operator norm of point evaluation is `1 / √(1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_hardyEvalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#norm-hardy-eval-clm).

## Pointwise bound for Hardy-space functions

The pointwise bound for `H²` functions: `‖f(z)‖ ≤ ‖f‖ / √(1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.norm_hardyEval_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#norm-hardy-eval-le).

## Hardy-space evaluation at the origin is the constant coefficient

Evaluation at `0` is the constant Taylor coefficient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval-zero).

## Hardy-space evaluation of a single monomial

Evaluation of a monomial `c * zⁿ` (a single Taylor coefficient).

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.hardyEval_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#hardy-eval-single).

## Conjugate reproducing property of the Szegő kernel

The reproducing property in the other order: `⟪a, k_z⟫ = conj (f(z))`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.inner_szegoKernel_right`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#inner-szego-kernel-right).

## Inner product of two Szegő kernels

The inner product of two Szegő kernels is the Szegő kernel function
`1 / (1 - z * conj w)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.inner_szegoKernel_szegoKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#inner-szego-kernel-szego-kernel).

## Taylor coefficients of a Hardy-space function are bounded by its norm

Taylor coefficients of an `H²` function are bounded by its norm: a
single squared coefficient is at most the sum of all of them.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HardySpace.abs_coeff_le_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HardySpace.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HardySpace.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#abs-coeff-le-norm).

## The boundary Hardy space H¹

Let $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ carry its Haar
measure normalized to total mass $1$. The Hardy space $H^1$ is the complex linear subspace of
$L^1(\mathbb{T})$ consisting of those $f$ whose Fourier coefficients
$\hat f(n) = \int_{\mathbb{T}} f(t) e^{-2\pi i n t} dt$ vanish for all integers $n < 0$.

Formalized by `MathlibExt.Analysis.HardySpaceWanted.Analysis.H1`, a definition declared in [WantedExt/Analysis/HardySpaceWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HardySpaceWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#h1).

## Newman's theorem: no bounded projection onto the Hardy space

Let $L^1(\mathbb{T})$ be
the space of integrable complex functions on the circle $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ with
its normalized Haar measure, and let $H^1 \subseteq L^1(\mathbb{T})$ be the boundary Hardy space.
There is no continuous $\mathbb{C}$-linear map $\pi : L^1(\mathbb{T}) \to H^1$ with $\pi(f) = f$
for every $f \in H^1$.

## Sources

- D. J. Newman, 'The nonexistence of projections from L^1 to H^1', Proc. Amer. Math. Soc.; W. Rudin, Fourier Analysis on Groups; Yongxi Lin, Hardy Space and Hartogs Triangle, Theorem 2.8. Problem `H1_not_closedComplemented` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HardySpaceWanted.Analysis.H1_not_closedComplemented` is written with `theorem_wanted` in [WantedExt/Analysis/HardySpaceWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HardySpaceWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html#h1-not-closed-complemented).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hardy space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/hardy-space)
