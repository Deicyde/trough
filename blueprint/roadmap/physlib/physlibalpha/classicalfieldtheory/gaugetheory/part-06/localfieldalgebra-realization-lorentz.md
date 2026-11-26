---
declaration: module
origin: cited
lean: GlobalGaugeGroup.SL, GlobalGaugeGroup.mem_SL_iff, GlobalGaugeGroup.mem_lieAlgebra_SL, GlobalGaugeGroup.mem_lieSubalgebra_SL, GlobalGaugeGroup.SL.toSpecialLinearGroup, GlobalGaugeGroup.continuous_SL_toSpecialLinearGroup, Submodule.mul_mem_span_sub_one, Submodule.aeval_sub_algebraMap_coeff_zero_mem
statement: formalized
proof: formalized
---

# Reynolds elements for SL(2, ℂ)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Realization.Lorentz`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean): 23 declarations, 23 with a docstring.

> A continuous finite-dimensional representation of `SL(2, ℂ)` has a Reynolds element.

## i. Overview

> Let `ρ` be a representation of `SL(2, ℂ)`, the double cover of the proper orthochronous Lorentz
> group, and `W` a finite-dimensional subrepresentation on which `ρ` is continuous. We show that
> `ρ` has a Reynolds element on `W`. This is an element of the group algebra whose coefficients sum
> to one and which projects `W` onto its invariant vectors. Unlike for a compact group, there is no
> Haar average, and the projection is built from Casimir operators instead.
>
> The group `SL(2, ℂ)` is realized as the global gauge group `GlobalGaugeGroup.SL 2`, the closed
> subgroup of `GL(2, ℂ)` of matrices of determinant one. The continuous representation on `W`
> differentiates to a real Lie algebra representation `dρ`. We extend it to all `2 × 2` matrices
> through their traceless part. Its holomorphic and antiholomorphic parts
> `X_L = (dρ X - i dρ (i X)) / 2` and `X_R = (dρ X + i dρ (i X)) / 2` are two commuting complex
> representations of `sl₂`, with `dρ X = X_L + X_R`.
>
> Let `C_L` and `C_R` be the Casimirs of the two `sl₂` actions, and `q_L`, `q_R` polynomials with
> constant term one such that `q_L(C_L)` and `q_R(C_R)` project onto the generalized kernels of the
> Casimirs. Then `P = q_L(C_L) q_R(C_R)` maps `W` into the joint generalized kernel. There both
> `sl₂` actions vanish, so `dρ` vanishes, and `P w` is fixed by every exponential `exp X`. These
> generate `SL(2, ℂ)`, since every matrix of determinant one is a product of transvections and a
> diagonal matrix of determinant one, each of which is an exponential of a traceless matrix.
>
> The general mathematics used here lives in `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2`.
> The generation by exponentials is in `Sl2.Exponential`, the holomorphic and antiholomorphic parts
> in `Sl2.HolomorphicPart`, and the standard triple with its Casimir in `Sl2.Triple` and
> `Sl2.Casimir`.
>
> Finally `P` lies in `1 + span {ρ g - 1}`. The span of the operators `ρ g - 1` is closed under
> products and, being finite-dimensional, closed. It therefore contains each `dρ X`, as the limit of
> `(ρ (exp (t X)) - 1) / t`, and every polynomial in the `dρ X` without constant term. So `P` comes
> from a Reynolds element.

## ii. Key results

> - `GlobalGaugeGroup.SL` : the global gauge group `SL(n, ℂ)`.
> - `GlobalGaugeGroup.SL.exists_sub_one_mem_span` : an operator in `1 + span {ρ g - 1}` with image
>   in the invariants, for a continuous finite-dimensional representation of `SL(2, ℂ)`.
> - `Representation.exists_isReynolds_of_specialLinearGroup` : a representation of `SL(2, ℂ)`
>   continuous on a finite-dimensional subrepresentation has a Reynolds element on it.

## iv. References

> - B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).
> - J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*.

## A. The global gauge group SL(n, ℂ)

**`GlobalGaugeGroup.SL`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L95).

> The global gauge group `SL(n, ℂ)`, the complex `n × n` matrices of determinant one.

```lean
def SL (n : ℕ) : GlobalGaugeGroup (Fin n)
```

**`GlobalGaugeGroup.mem_SL_iff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L106).

> An invertible matrix lies in `SL(n, ℂ)` exactly when it has determinant one.

```lean
lemma mem_SL_iff {n : ℕ} {g : GL (Fin n) ℂ} :
    g ∈ (SL n).group ↔ (g : Matrix (Fin n) (Fin n) ℂ).det = 1
```

**`GlobalGaugeGroup.mem_lieAlgebra_SL`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L111).

> A traceless matrix is a generator of `SL(n, ℂ)`, since `det (exp (t X)) = exp (t tr X) = 1`.

```lean
lemma mem_lieAlgebra_SL {n : ℕ} {X : Matrix (Fin n) (Fin n) ℂ} (htr : X.trace = 0) :
    X ∈ (SL n).lieAlgebra
```

**`GlobalGaugeGroup.mem_lieSubalgebra_SL`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L119).

> A traceless matrix lies in the Lie algebra of `SL(n, ℂ)`.

```lean
lemma mem_lieSubalgebra_SL {n : ℕ} {X : Matrix (Fin n) (Fin n) ℂ} (htr : X.trace = 0) :
    X ∈ (SL n).lieSubalgebra
```

**`GlobalGaugeGroup.SL.toSpecialLinearGroup`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L125).

> The elements of `SL(n, ℂ)` as a global gauge group are those of Mathlib's special linear
> group.

```lean
noncomputable def SL.toSpecialLinearGroup (n : ℕ) :
    (SL n).group ≃* SpecialLinearGroup (Fin n) ℂ
```

**`GlobalGaugeGroup.continuous_SL_toSpecialLinearGroup`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L136).

> The identification of the two forms of `SL(n, ℂ)` is continuous.

```lean
lemma continuous_SL_toSpecialLinearGroup (n : ℕ) : Continuous (SL.toSpecialLinearGroup n)
```

## B. The span of the operators ρ g - 1

### B.1. Products and polynomials

**`Submodule.mul_mem_span_sub_one`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L155).

> The span of `σ h - 1`, for a monoid homomorphism `σ` into an algebra, is closed under
> multiplication, since `(σ g - 1) (σ h - 1) = (σ (g h) - 1) - (σ g - 1) - (σ h - 1)`.

```lean
lemma mul_mem_span_sub_one {H : Type*} [Monoid H] (σ : H →* A) {a b : A}
    (ha : a ∈ span K (Set.range fun h => σ h - 1)) (hb : b ∈ span K (Set.range fun h => σ h - 1)) :
    a * b ∈ span K (Set.range fun h => σ h - 1)
```

**`Submodule.aeval_sub_algebraMap_coeff_zero_mem`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L172).

> In a subspace closed under multiplication, a polynomial in an element `x` of it differs from
> its constant term by an element of it.

```lean
lemma aeval_sub_algebraMap_coeff_zero_mem {S : Submodule K A}
    (hS : ∀ a ∈ S, ∀ b ∈ S, a * b ∈ S) {x : A} (hx : x ∈ S) (q : K[X]) :
    aeval x q - algebraMap K A (q.coeff 0) ∈ S
```

**`Commute.aeval_right`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L190).

> An element commuting with `b` commutes with every polynomial in `b`.

```lean
lemma aeval_right {a b : A} (h : Commute a b) (p : K[X]) : Commute a (aeval b p)
```

### B.2. Derivatives

**`Submodule.mem_of_hasDerivAt`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L209).

> A closed subspace containing every difference `f t - f 0` contains the derivative of `f`
> at `0`, the limit of the difference quotients.

```lean
lemma mem_of_hasDerivAt {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    {S : Submodule ℂ E} (hS : IsClosed (S : Set E)) {f : ℝ → E} {f' : E}
    (hf : HasDerivAt f f' 0) (hmem : ∀ t, f t - f 0 ∈ S) : f' ∈ S
```

**`GlobalGaugeGroup.derivRep_mem_span`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L225).

> The derivative of a representation along a generator lies in the span of the operators
> `ρ g - 1`, as the limit of the difference quotients `(ρ (exp (t X)) - 1) / t`.

```lean
lemma derivRep_mem_span (X : G.lieSubalgebra) :
    derivRep ρ X ∈
      Submodule.span ℂ (Set.range fun g => ((ρ g : (W →L[ℂ] W)ˣ) : W →L[ℂ] W) - 1)
```

## C. Representations of SL(2, ℂ)

### C.1. The derivative on all matrices

**`GlobalGaugeGroup.SL.tracelessPart`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L254).

> The traceless part `X - (tr X / 2) 1` of a `2 × 2` complex matrix, as a homomorphism of real
> Lie algebras into the Lie algebra of `SL(2, ℂ)`.

```lean
noncomputable def SL.tracelessPart : Matrix (Fin 2) (Fin 2) ℂ →ₗ⁅ℝ⁆ (SL 2).lieSubalgebra
```

**`GlobalGaugeGroup.SL.tracelessPart_of_trace_eq_zero`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L272).

> The traceless part of a traceless matrix is the matrix itself.

```lean
lemma SL.tracelessPart_of_trace_eq_zero {X : Matrix (Fin 2) (Fin 2) ℂ} (htr : X.trace = 0) :
    SL.tracelessPart X = ⟨X, mem_lieSubalgebra_SL htr⟩
```

**`GlobalGaugeGroup.SL.derivRepMatrix`**, a def, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L281).

> The derivative of a continuous representation of `SL(2, ℂ)`, extended to all `2 × 2` complex
> matrices through their traceless part.

```lean
noncomputable def SL.derivRepMatrix : Matrix (Fin 2) (Fin 2) ℂ →ₗ⁅ℝ⁆ E →L[ℂ] E
```

**`GlobalGaugeGroup.SL.derivRepMatrix_mem_span`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L285).

> The derivative lies in the span of the operators `ρ g - 1`.

```lean
lemma SL.derivRepMatrix_mem_span (X : Matrix (Fin 2) (Fin 2) ℂ) :
    SL.derivRepMatrix ρ X ∈
      Submodule.span ℂ (Set.range fun g => ((ρ g : (E →L[ℂ] E)ˣ) : E →L[ℂ] E) - 1)
```

**`GlobalGaugeGroup.SL.apply_eq_exp_derivRepMatrix`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L291).

> The representation maps `exp X`, for a traceless `X`, to `exp (dρ X)`.

```lean
lemma SL.apply_eq_exp_derivRepMatrix {g : (SL 2).group} {X : Matrix (Fin 2) (Fin 2) ℂ}
    (htr : X.trace = 0) (hg : ((g : GL (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ) = exp X) :
    ((ρ g : (E →L[ℂ] E)ˣ) : E →L[ℂ] E) = exp (SL.derivRepMatrix ρ X)
```

### C.2. Generation by exponentials

**`GlobalGaugeGroup.SL.induction`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L306).

> An induction principle for `SL(2, ℂ)`. A property of group elements which holds for every
> exponential of a traceless matrix and is stable under products holds for every element.

```lean
lemma SL.induction {p : (SL 2).group → Prop}
    (hexp : ∀ (g : (SL 2).group) (X : Matrix (Fin 2) (Fin 2) ℂ), X.trace = 0 →
      ((g : GL (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ) = exp X → p g)
    (hmul : ∀ g h, p g → p h → p (g * h)) (g : (SL 2).group) : p g
```

### C.3. The projection onto the invariants

**`GlobalGaugeGroup.SL.apply_eq_self_of_sl2`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L338).

> A vector killed by the holomorphic and antiholomorphic images of the standard `sl₂` triple is
> invariant under the representation.

```lean
lemma SL.apply_eq_self_of_sl2 {w : E}
    (hL : ∀ X ∈ ({sl2E, sl2F, sl2H} : Set (Matrix (Fin 2) (Fin 2) ℂ)),
      (SL.derivRepMatrix ρ).holPart X w = 0)
    (hR : ∀ X ∈ ({sl2E, sl2F, sl2H} : Set (Matrix (Fin 2) (Fin 2) ℂ)),
      (SL.derivRepMatrix ρ).antiholPart X w = 0) (g : (SL 2).group) :
    ((ρ g : (E →L[ℂ] E)ˣ) : E →L[ℂ] E) w = w
```

**`GlobalGaugeGroup.SL.apply_eq_zero_of_mem_maxGenEigenspace`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L364).

> A vector in the generalized kernel of the Casimir of a map preserving brackets and real
> multiples is killed by the images of the standard `sl₂` triple.

```lean
lemma SL.apply_eq_zero_of_mem_maxGenEigenspace {φ : Matrix (Fin 2) (Fin 2) ℂ → E →L[ℂ] E}
    (hlie : ∀ X Y, ⁅φ X, φ Y⁆ = φ ⁅X, Y⁆) (hsmul : ∀ (r : ℝ) X, φ ((r : ℂ) • X) = (r : ℂ) • φ X)
    {w : E} (hw : w ∈ Module.End.maxGenEigenspace (ψ (sl2Casimir φ)) 0) :
    ∀ X ∈ ({sl2E, sl2F, sl2H} : Set (Matrix (Fin 2) (Fin 2) ℂ)), φ X w = 0
```

**`GlobalGaugeGroup.SL.exists_sub_one_mem_span`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L380).

> A continuous finite-dimensional representation of `SL(2, ℂ)` has an operator in
> `1 + span {ρ g - 1}` with image in the invariants, the product `q_L(C_L) q_R(C_R)` of the
> projections onto the generalized kernels of the two Casimirs.

```lean
lemma SL.exists_sub_one_mem_span :
    ∃ P : E →L[ℂ] E,
      P - 1 ∈ Submodule.span ℂ (Set.range fun g => ((ρ g : (E →L[ℂ] E)ˣ) : E →L[ℂ] E) - 1) ∧
      ∀ g v, ((ρ g : (E →L[ℂ] E)ˣ) : E →L[ℂ] E) (P v) = P v
```

## D. Reynolds elements for SL(2, ℂ)

**`Representation.coordRepSL`**, a def, [line 440](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L440).

> The coordinate form of a continuous finite-dimensional subrepresentation of `SL(2, ℂ)`, as a
> continuous homomorphism from `SL(2, ℂ)` as a global gauge group into the invertible operators.

```lean
noncomputable def coordRepSL (hW : ContinuousMatrixCoeff W) :
    (SL 2).group →ₜ* ((Fin (Module.finrank ℂ W.toSubmodule) → ℂ) →L[ℂ]
      (Fin (Module.finrank ℂ W.toSubmodule) → ℂ))ˣ
```

**`Representation.coordRepSL_apply`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L455).

> The coordinate form on `SL(2, ℂ)` as a global gauge group is that on Mathlib's special linear
> group.

```lean
lemma coordRepSL_apply (hW : ContinuousMatrixCoeff W) (g : (SL 2).group) :
    ((coordRepSL W hW g : (_ →L[ℂ] _)ˣ) : _ →L[ℂ] _) = coordRep W (SL.toSpecialLinearGroup 2 g)
```

**`Representation.exists_isReynolds_of_specialLinearGroup`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean#L461).

> A representation of `SL(2, ℂ)` which is continuous on a finite-dimensional
> subrepresentation has a Reynolds element on it.

```lean
lemma exists_isReynolds_of_specialLinearGroup (hW : ContinuousMatrixCoeff W) :
    ∃ r, ρ.IsReynolds W.toSubmodule r
```

## Depends on

- [The derivative of a representation of a global gauge group](matterfield-derivrep.md)
- [Reynolds elements for compact groups](../../../mathematics/part-02/representationtheory/reynolds-compact.md)
- [Holomorphic and antiholomorphic parts of a real Lie algebra homomorphism](../../../mathematics/part-02/representationtheory/sl2-holomorphicpart.md)
- [The standard sl₂ triple](../../../mathematics/part-02/representationtheory/sl2-triple.md)

## Proof depends on

- [Lie's Trace Formula](../../../../physlib/mathematics/formathlib/part-01/datastructures-matrix-lietrace.md)
- [Generation of SL(2, ℂ) by exponentials](../../../mathematics/part-02/representationtheory/sl2-exponential.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Lorentz.lean)
