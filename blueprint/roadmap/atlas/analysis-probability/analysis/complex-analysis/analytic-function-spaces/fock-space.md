---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_sq_fock_coeff, MathlibExt.Analysis.InnerProductSpace.FockSpace.memℓp_fockKernel, MathlibExt.Analysis.InnerProductSpace.FockSpace.fockKernel, MathlibExt.Analysis.InnerProductSpace.FockSpace.fockKernel_zero, MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_sq_fockKernel, MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_fockKernel, MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval, MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval_eq_tsum
statement: formalized
proof: formalized
---

# Fock space

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html).

## Squared norms of the Fock kernel coefficients

The squared norms of the Fock kernel coefficients are
`‖z‖ ^ (2 * n) / n!`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_sq_fock_coeff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-sq-fock-coeff).

## Fock kernel coefficients lie in ℓ²

The Fock kernel coefficients are in `ℓ²` for every `z : ℂ`, since
`∑' n, ‖z‖ ^ (2 * n) / n! = Real.exp ‖z‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.memℓp_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#mem-p-fock-kernel).

## Reproducing kernel of the Fock space

The **Fock kernel** at `z`: the `ℓ²(ℕ, ℂ)` sequence with coefficients
`(conj z)ⁿ / √(n!)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockKernel`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-kernel).

## Fock kernel at the origin is the first basis vector

The Fock kernel at `0` is the first standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockKernel_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-kernel-zero).

## Squared norm of the Fock kernel

The squared norm of the Fock kernel is `Real.exp ‖z‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_sq_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-sq-fock-kernel).

## Norm of the Fock kernel

The norm of the Fock kernel is `Real.exp (‖z‖² / 2)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-fock-kernel).

## Point evaluation on the Fock space

Point evaluation on the Fock space: the inner product with the
Fock kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval).

## Fock-space point evaluation as a Taylor series

Point evaluation is the Taylor series `∑' n, a n * zⁿ / √(n!)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-eq-tsum).

## Absolute convergence of Taylor series in the Fock space

The Taylor series of a Fock-space function converges absolutely at
every point of `ℂ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.summable_fockEval_terms`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#summable-fock-eval-terms).

## Point evaluation as a bounded functional on the Fock space

Point evaluation as a bounded linear functional on the Fock space.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEvalCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-clm).

## Reproducing property of the Fock kernel

The bounded point-evaluation functional acts by the inner product
with the Fock kernel.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEvalCLM_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-clm-apply).

## Norm of Fock-space point evaluation

The operator norm of point evaluation is `Real.exp (‖z‖² / 2)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_fockEvalCLM`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-fock-eval-clm).

## Pointwise bound for Fock-space functions

The pointwise bound for Fock-space functions:
`‖f(z)‖ ≤ ‖f‖ * Real.exp (‖z‖² / 2)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_fockEval_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-fock-eval-le).

## Fock-space evaluation at the origin is the constant coefficient

Evaluation at `0` is the constant Taylor coefficient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-zero).

## Fock-space evaluation of a single monomial

Evaluation of a monomial `c * zⁿ / √(n!)` (a single Taylor
coefficient).

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-single).

## Conjugate reproducing property of the Fock kernel

The reproducing property in the other order: `⟪a, k_z⟫ = conj (f(z))`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.inner_fockKernel_right`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#inner-fock-kernel-right).

## Inner product of two Fock kernels is an exponential

The inner product of two Fock kernels is the Fock kernel function
`Complex.exp (z * conj w)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.inner_fockKernel_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#inner-fock-kernel-fock-kernel).

## Modulus of the inner product of two Fock kernels

The norm of the inner product of two Fock kernels is
`Real.exp (z * conj w).re`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_inner_fockKernel_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-inner-fock-kernel-fock-kernel).

## Fock kernel evaluated at its own point

Evaluation of the kernel at its own point: `f_z(k_z) = Real.exp ‖z‖²`,
so the pointwise bound is sharp.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockEval_fockKernel`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-eval-fock-kernel).

## Normalized monomials in the Fock space

The normalized monomial `eₙ(z) = zⁿ / √(n!)`, represented by the `n`th
standard basis vector in the Taylor-coefficient model of Fock space.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockMonomial`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-monomial).

## Normalized Fock monomials are orthonormal standard basis vectors

The rescaled monomials `eₙ(z) = zⁿ / √(n!)`, i.e. the standard basis
vectors of the coefficient model, are orthonormal.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockMonomial_orthonormal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-monomial-orthonormal).

## Normalized Fock monomials form an orthonormal family

The normalized monomial family satisfies Mathlib's standard orthonormal predicate.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.orthonormal_fockMonomial`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#orthonormal-fock-monomial).

## Fock coefficients as inner products with normalized monomials

The coefficient of `a` at `n` is the inner product with `eₙ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockCoeff_eq_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-coeff-eq-inner).

## Coherent state in the Fock space

The **coherent state** at `z`: the normalized Fock kernel,
`ĉ_z = Real.exp (-‖z‖² / 2) • k_z`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.fockCoherent`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#fock-coherent).

## Coherent states are unit vectors

Coherent states are unit vectors.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_fockCoherent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-fock-coherent).

## Inner product of two coherent states

The inner product of two coherent states.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.inner_fockCoherent_fockCoherent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#inner-fock-coherent-fock-coherent).

## Gaussian overlap of coherent states

The overlap of two coherent states is Gaussian:
`‖⟪ĉ_z, ĉ_w⟫‖ = Real.exp (-‖z - w‖² / 2)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.FockSpace.norm_inner_fockCoherent_fockCoherent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/FockSpace.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/FockSpace.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html#norm-inner-fock-coherent-fock-coherent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fock space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/fock-space)
