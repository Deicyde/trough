---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.BergmanSpace.hasSum_succ_mul_pow_complex, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.hasSum_succ_mul_pow_real, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_sq_bergman_coeff, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.memℓp_bergmanKernel, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanKernel, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanKernel_zero, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_sq_bergmanKernel, MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_bergmanKernel
statement: formalized
---

# Bergman space

30 results, 29 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html).

## Square of the complex geometric series

The Cauchy product of the geometric series with itself: the series
`∑' n, (n + 1) * qⁿ` sums to `(1 - q)⁻¹ ^ 2`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.hasSum_succ_mul_pow_complex`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#has-sum-succ-mul-pow-complex).

## Square of the real geometric series

The real form of the Cauchy product above.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.hasSum_succ_mul_pow_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#has-sum-succ-mul-pow-real).

## Squared norms of the Bergman kernel coefficients

The squared norms of the Bergman kernel coefficients are
`(n + 1) * ‖z‖ ^ (2 * n)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_sq_bergman_coeff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#norm-sq-bergman-coeff).

## Bergman kernel coefficients are square-summable

The Bergman kernel coefficients are in `ℓ²` when `z` is in the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.memℓp_bergmanKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#mem-p-bergman-kernel).

## Bergman kernel

The **Bergman kernel** at `z`: the `ℓ²(ℕ, ℂ)` sequence with
coefficients `√(n + 1) * (conj z)ⁿ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanKernel`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-kernel).

## Bergman kernel at the origin

The Bergman kernel at `0` is the first standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-kernel-zero).

## Squared norm of the Bergman kernel

The squared norm of the Bergman kernel is `1 / (1 - ‖z‖²)²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_sq_bergmanKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#norm-sq-bergman-kernel).

## Norm of the Bergman kernel

The norm of the Bergman kernel is `1 / (1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_bergmanKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#norm-bergman-kernel).

## Point evaluation on the Bergman space

Point evaluation on `A²(𝔻)`: the inner product with the Bergman kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEval`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval).

## Bergman point evaluation as a Taylor series

Point evaluation is the Taylor series `∑' n, a n * √(n + 1) * zⁿ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEval_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-eq-tsum).

## Convergence of the Taylor series of a Bergman space function

The Taylor series of an `A²` function converges at every
point of the disc.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.summable_bergmanEval_terms`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#summable-bergman-eval-terms).

## Bounded point-evaluation functional on the Bergman space

Point evaluation as a bounded linear functional on `A²(𝔻)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEvalCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-clm).

## Bergman point evaluation is the inner product with the kernel

The bounded point-evaluation functional acts by the inner product
with the Bergman kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEvalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-clm-apply).

## Operator norm of Bergman point evaluation

The operator norm of point evaluation is `1 / (1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_bergmanEvalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#norm-bergman-eval-clm).

## Pointwise bound for Bergman space functions

The pointwise bound for `A²` functions: `‖f(z)‖ ≤ ‖f‖ / (1 - ‖z‖²)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.norm_bergmanEval_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#norm-bergman-eval-le).

## Bergman evaluation at the origin

Evaluation at `0` is the constant Taylor coefficient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEval_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-zero).

## Bergman evaluation of a monomial

Evaluation of a monomial `c * √(n + 1) * zⁿ` (a single coefficient).

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEval_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-single).

## Reproducing property of the Bergman kernel, conjugate form

The reproducing property in the other order: `⟪a, k_z⟫ = conj (f(z))`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.inner_bergmanKernel_right`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#inner-bergman-kernel-right).

## Inner product of two Bergman kernels

The inner product of two Bergman kernels is the Bergman kernel function
`(1 - z * conj w)⁻¹ ^ 2`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.inner_bergmanKernel_bergmanKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#inner-bergman-kernel-bergman-kernel).

## Bergman kernel evaluated at its own point

Evaluation of the kernel at its own point: `f_z(k_z) = (1 - ‖z‖²)⁻¹ ^ 2`,
so the pointwise bound is sharp.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanEval_bergmanKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-eval-bergman-kernel).

## Rescaled Bergman monomial

The rescaled monomial `eₙ(z) = √(n + 1) zⁿ` for normalized area
measure `dA / π`, represented by the `n`th standard basis vector in the
coefficient model.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanMonomial`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-monomial).

## Inner products of rescaled Bergman monomials are Kronecker deltas

The coordinate inner products of the rescaled monomials equal the
Kronecker delta.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanMonomial_orthonormal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-monomial-orthonormal).

## Rescaled Bergman monomials are orthonormal

The rescaled monomial family satisfies Mathlib's standard orthonormal
predicate.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.orthonormal_bergmanMonomial`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#orthonormal-bergman-monomial).

## Bergman coefficients as inner products with monomials

The coefficient of `a` at `n` is the inner product with `eₙ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BergmanSpace.bergmanCoeff_eq_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BergmanSpace.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman-coeff-eq-inner).

## The open unit disc

The set $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$.

Formalized by `MathlibExt.Analysis.BergmanCyclicityWanted.Disc`, a definition declared in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#disc).

## Bergman space $A^2$ of the unit disc

A function $f : \mathbb{C} \to \mathbb{C}$ belongs to
the Bergman space $A^2$ when it is analytic on the open unit disc
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ and square-integrable on $\mathbb{D}$ with respect to
Lebesgue area measure $dA$: $f$ is almost everywhere strongly measurable on $\mathbb{D}$ and
$\int_{\mathbb{D}} |f|^2 \, dA < \infty$.

Formalized by `MathlibExt.Analysis.BergmanCyclicityWanted.Bergman`, a definition declared in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#bergman).

## Pointwise reciprocal

For a function $f : \mathbb{C} \to \mathbb{C}$, the function
$z \mapsto f(z)^{-1}$, with the convention $0^{-1} = 0$ at the zeros of $f$.

Formalized by `MathlibExt.Analysis.BergmanCyclicityWanted.Inv`, a definition declared in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#inv).

## Density of polynomial multiples in $A^2$

Write $\mathbb{D}$ for the open unit disc and
$dA$ for Lebesgue area measure on it. For a function $f : \mathbb{C} \to \mathbb{C}$, the statement
that the polynomial multiples of $f$ are dense in the Bergman space $A^2$: for every $g \in A^2$
and every $\varepsilon > 0$ there is a complex polynomial $p$ with
$\left(\int_{\mathbb{D}} |p f - g|^2 \, dA\right)^{1/2} < \varepsilon$.

Formalized by `MathlibExt.Analysis.BergmanCyclicityWanted.Dense`, a definition declared in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#dense).

## Bergman cyclicity conjecture

Write $\mathbb{D}$ for the open unit disc and $dA$ for
Lebesgue area measure on it. The statement that for every function $f : \mathbb{C} \to \mathbb{C}$
with no zeros in $\mathbb{D}$ such that $f$ and its pointwise reciprocal $1/f$ both belong to the
Bergman space $A^2$, the polynomial multiples of $f$ are dense in $A^2$: for every $g \in A^2$ and
every $\varepsilon > 0$ there is a complex polynomial $p$ with
$\left(\int_{\mathbb{D}} |p f - g|^2 \, dA\right)^{1/2} < \varepsilon$.

## Sources

- record `AMR-022-8010`; the record's generalization to other spaces is not part of this statement.

Formalized by `MathlibExt.Analysis.BergmanCyclicityWanted.conjecture`, a definition declared in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#conjecture).

## Invertible non-cyclic functions in the Bergman space $A^2$

Write $\mathbb{D}$ for the open
unit disc and $dA$ for Lebesgue area measure on it. There is a function
$f : \mathbb{C} \to \mathbb{C}$ with no zeros in $\mathbb{D}$ such that $f$ and its pointwise
reciprocal $1/f$ both belong to the Bergman space $A^2$, but the polynomial multiples of $f$ are
not dense in $A^2$: there are $g \in A^2$ and $\varepsilon > 0$ with
$\left(\int_{\mathbb{D}} |p f - g|^2 \, dA\right)^{1/2} \ge \varepsilon$ for every complex
polynomial $p$. That is, the Bergman cyclicity conjecture is false.

Borichev and Hedenmalm (J. Amer. Math. Soc. 10 (1997) 761-796) constructed invertible but
non-cyclic functions in the unweighted Bergman spaces $B^p(\mathbb{D})$, $0 < p < \infty$; the case
$p = 2$ gives such an $f$, as stated in Borichev-Hedenmalm-Volberg (arXiv:math/0304318).

## Sources

- Alexander Borichev, Haakan Hedenmalm and Alexander Volberg, Large Bergman spaces: invertibility, cyclicity, and subspaces of arbitrary index, arXiv:math/0304318 (2003), https://arxiv.org/abs/math/0304318.

Stated but not proved: `MathlibExt.Analysis.BergmanCyclicityWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/BergmanCyclicityWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/BergmanCyclicityWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bergman space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/bergman-space)
