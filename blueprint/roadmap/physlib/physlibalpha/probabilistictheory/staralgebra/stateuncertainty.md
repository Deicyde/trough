---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.AlgState.apply_selfAdjoint, PhyslibAlpha.ProbabilisticTheory.AlgState.fluctuation, PhyslibAlpha.ProbabilisticTheory.AlgState.star_fluctuation, PhyslibAlpha.ProbabilisticTheory.AlgState.covariance, PhyslibAlpha.ProbabilisticTheory.AlgState.variance, PhyslibAlpha.ProbabilisticTheory.AlgState.bracket, PhyslibAlpha.ProbabilisticTheory.AlgState.apply_fluctuation_mul, PhyslibAlpha.ProbabilisticTheory.AlgState.bracket_eq_im
statement: formalized
proof: formalized
---

# Uncertainty relations for states on a `*`-algebra

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.StateUncertainty`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean): 20 declarations, 16 with a docstring.

> The Robertson–Schrödinger relation and Robertson's relation for several observables hold for a
> state on any unital `*`-algebra, with no norm on the algebra.

## i. Overview

> A state `ω` on a unital `*`-algebra `A`, as in `AlgState`, gives the positive semidefinite inner
> product `⟨x, y⟩ = ω(x⋆ y)` on `A`. The fluctuation `a - ω(a)` of a self-adjoint `a` is again
> self-adjoint, because `ω(a)` is real. For a family of observables `a_j`, the inner products of
> their fluctuations form the matrix `Σ + iΩ`, where `Σ` is the covariance matrix and `Ω` the
> matrix of expectations of brackets. It is a Gram matrix, so it is positive semidefinite, and so
> is its transpose `Σ - iΩ`. Hence `|det Ω| ≤ det Σ`, by `Matrix.abs_det_le_det_of_posSemidef`.
> For two observables, Cauchy–Schwarz gives `Cov(a, b)² + ω⟨⁅a, b⁆⟩² ≤ Var a · Var b`.
>
> If `ω` is invariant under a `⋆`-automorphism `σ` with `σ a = a` and `σ b = -b`, then
> `ω(a b) = ω(σ (a b)) = -ω(a b)` and `ω(b) = 0`, so the entries `Σ_ab` and `Ω_ab` vanish.
>
> The C⋆-algebra version is `UnitalPositiveLinearMap.robertson_det`. This one also applies to an
> algebra that is not complete, such as the quasi-local algebra of an infinite crystal, and so to
> its translation invariant states and the thermodynamic limit states of `InvariantState`.

## ii. Key results

> - `AlgState.covarianceMatrix`, `AlgState.bracketMatrix` : the matrices `Σ` and `Ω`.
> - `AlgState.gram_fluctuation` : `Σ + iΩ` is the Gram matrix of the fluctuations.
> - `AlgState.robertson_schrodinger` : the Robertson–Schrödinger relation.
> - `AlgState.robertson_det` : **Robertson's relation for several observables**,
>   `|det Ω| ≤ det Σ`.
> - `AlgState.covariance_eq_zero_of_symm`, `AlgState.bracket_eq_zero_of_symm` : in a state
>   invariant under a `⋆`-automorphism, an even and an odd observable have `Σ_ab = Ω_ab = 0`.

## iv. References

> * H. P. Robertson, *An indeterminacy relation for several observables and its classical
>   interpretation*, Phys. Rev. 46 (1934) 794.

## A. Fluctuations

**`PhyslibAlpha.ProbabilisticTheory.AlgState.apply_selfAdjoint`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L73).

> A self-adjoint element has a real expectation.

```lean
lemma apply_selfAdjoint (a : selfAdjoint A) : ω (a : A) = ((ω (a : A)).re : ℂ)
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.fluctuation`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L79).

> The fluctuation `a - ω(a)` of an observable.

```lean
def fluctuation (a : selfAdjoint A) : A
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.star_fluctuation`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L81).

```lean
lemma star_fluctuation (a : selfAdjoint A) : star (ω.fluctuation a) = ω.fluctuation a
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.covariance`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L86).

> The covariance `Re ω((a - ω(a)) (b - ω(b)))` of two observables.

```lean
noncomputable def covariance (a b : selfAdjoint A) : ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.variance`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L90).

> The variance of an observable.

```lean
noncomputable def variance (a : selfAdjoint A) : ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.bracket`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L93).

> The expectation of the bracket of two observables.

```lean
noncomputable def bracket (a b : selfAdjoint A) : ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.apply_fluctuation_mul`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L96).

> `ω((a - ω(a)) (b - ω(b))) = ω(a b) - ω(a) ω(b)`.

```lean
lemma apply_fluctuation_mul (a b : selfAdjoint A) :
    ω (ω.fluctuation a * ω.fluctuation b) = ω ((a : A) * b) - ω (a : A) * ω (b : A)
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.bracket_eq_im`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L107).

> The bracket is the imaginary part of `ω((a - ω(a)) (b - ω(b)))`.

```lean
lemma bracket_eq_im (a b : selfAdjoint A) :
    ω.bracket a b = (ω (ω.fluctuation a * ω.fluctuation b)).im
```

## B. The matrices `Σ` and `Ω`

**`PhyslibAlpha.ProbabilisticTheory.AlgState.covarianceMatrix`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L129).

> The covariance matrix `Σ_jk = Cov(a_j, a_k)` of a family of observables.

```lean
noncomputable def covarianceMatrix (a : ι → selfAdjoint A) : Matrix ι ι ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.bracketMatrix`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L133).

> The matrix `Ω_jk = ω⟨⁅a_j, a_k⁆⟩` of expectations of brackets.

```lean
noncomputable def bracketMatrix (a : ι → selfAdjoint A) : Matrix ι ι ℝ
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.fluctuationVector`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L137).

> The fluctuation of an observable as a vector of the pre-Hilbert space of the state.

```lean
def fluctuationVector (a : selfAdjoint A) : ω.PreGNS
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.inner_fluctuationVector`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L139).

```lean
lemma inner_fluctuationVector (a b : selfAdjoint A) :
    ⟪ω.fluctuationVector a, ω.fluctuationVector b⟫_ℂ =
      ω (ω.fluctuation a * ω.fluctuation b)
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.gram_fluctuation`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L147).

> **`Σ + iΩ` is the Gram matrix of the fluctuations.**

```lean
lemma gram_fluctuation (a : ι → selfAdjoint A) :
    gram ℂ (fun j => ω.fluctuationVector (a j)) =
      (ω.covarianceMatrix a).map ((↑) : ℝ → ℂ) +
        Complex.I • (ω.bracketMatrix a).map ((↑) : ℝ → ℂ)
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.transpose_gram_fluctuation`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L157).

> `Σ - iΩ` is the transpose of the Gram matrix.

```lean
lemma transpose_gram_fluctuation (a : ι → selfAdjoint A) :
    (gram ℂ (fun j => ω.fluctuationVector (a j)))ᵀ =
      (ω.covarianceMatrix a).map ((↑) : ℝ → ℂ) -
        Complex.I • (ω.bracketMatrix a).map ((↑) : ℝ → ℂ)
```

## C. Uncertainty relations

**`PhyslibAlpha.ProbabilisticTheory.AlgState.robertson_schrodinger`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L170).

> **The Robertson–Schrödinger relation** for a state on a `*`-algebra:
> `Cov(a, b)² + ω⟨⁅a, b⁆⟩² ≤ Var a · Var b`.

```lean
lemma robertson_schrodinger (a b : selfAdjoint A) :
    ω.covariance a b ^ 2 + ω.bracket a b ^ 2 ≤ ω.variance a * ω.variance b
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.robertson_det`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L184).

> **Robertson's uncertainty relation for several observables** for a state on a `*`-algebra:
> for every finite family of observables, `|det Ω| ≤ det Σ`.

```lean
lemma robertson_det [Fintype ι] [DecidableEq ι] (a : ι → selfAdjoint A) :
    |(ω.bracketMatrix a).det| ≤ (ω.covarianceMatrix a).det
```

## D. Symmetric states

**`PhyslibAlpha.ProbabilisticTheory.AlgState.apply_eq_zero_of_symm`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L199).

```lean
lemma apply_eq_zero_of_symm : ω (b : A) = 0
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.apply_mul_eq_zero_of_symm`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L207).

```lean
lemma apply_mul_eq_zero_of_symm : ω ((a : A) * b) = 0
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.covariance_eq_zero_of_symm`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L216).

> **In a symmetric state, an even and an odd observable have covariance zero.**

```lean
lemma covariance_eq_zero_of_symm : ω.covariance a b = 0
```

**`PhyslibAlpha.ProbabilisticTheory.AlgState.bracket_eq_zero_of_symm`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean#L224).

> **In a symmetric state, an even and an odd observable have a bracket of expectation
> zero.**

```lean
lemma bracket_eq_zero_of_symm : ω.bracket a b = 0
```

## Depends on

- [The GNS representation of a state on a unital `*`-algebra](gns.md)
- [The Lie bracket of observables](lie.md)

## Proof depends on

- [Uncertainty relations](../cstaralgebra/uncertainty.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/StateUncertainty.lean)
