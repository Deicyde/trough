---
declaration: module
origin: cited
lean: suTensor.Color, suTensor.modules, suTensor.modulesAddCommGroup, suTensor.modulesModule, suTensor.basisIdx, suTensor.basisIdxFintype, suTensor.basisIdxDecidableEq, suTensor.basis
statement: formalized
proof: formalized
---

# The complex tensor species of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.TensorSpecies`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean): 36 declarations, 27 with a docstring.

> The tensors of `SU(N)` with fundamental, anti-fundamental and adjoint indices.

## i. Overview

> The complex tensors of `SU(N)` carry three kinds of index, in analogy with the complex Lorentz
> tensors `complexLorentzTensor`: a fundamental index, an anti-fundamental index and an adjoint index.
> `suTensor N` is the tensor species with these three colors. The fundamental color is `Fin N → ℂ`
> moved by `g`, the anti-fundamental color is `Fin N → ℂ` moved by `(g⁻¹)ᵀ` (for a unitary `g` the
> complex conjugate), and the adjoint color is the complexification
> `SUAlgebraComplexified N = ℂ ⊗[ℝ] su(N)` of the Lie algebra `SUAlgebra N` of traceless hermitian
> matrices, moved by the adjoint representation `adjRep` with the generalized Gell-Mann matrices as
> basis, as set up in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Adjoint`. The type of tensors
> with colors `c₁, …, cₙ` is written `SuT[N, c₁, …, cₙ]`.
>
> The fundamental and anti-fundamental colors are dual to each other and contract by the dot
> product, with unit `∑ eᵢ ⊗ eᵢ`. The adjoint color is dual to itself and contracts by the trace
> form `tr (A B)` (`adjContr`), with unit `∑ λ_a ⊗ λᵃ` for the Gell-Mann matrices `λ_a` and their
> trace-dual basis `λᵃ = λ_a / 2`. In the standard basis the matrix of `g` is `g` on the
> fundamental color and `(g⁻¹)ᵀ` on the anti-fundamental color (F). The species has no metric
> (`TensorSpecies.WithMetric`). For `N ≥ 3` the fundamental of `SU(N)` is not self-dual, so there is
> no invariant in `ℂᴺ ⊗ ℂᴺ` to raise and lower its indices with. A tensor with one adjoint index
> is an element of the adjoint representation, which has no invariants but zero, so neither has the
> tensor (G).

## ii. Key results

> - `suTensor.Color` : the fundamental, anti-fundamental and adjoint colors.
> - `suTensor.fundRep`, `suTensor.antiFundRep` : the fundamental and anti-fundamental
>   representations.
> - `suTensor` : the complex tensor species of `SU(N)`, with the notation `SuT[N, c₁, …, cₙ]`.
> - `suTensor.toMatrix_fundRep`, `suTensor.toMatrix_antiFundRep` : the matrices of the fundamental
>   and anti-fundamental colors.
> - `suTensor.invariants_adj_eq_bot` : there are no invariant tensors with one adjoint index but
>   zero.

## iv. References

> * None.

## A. The colors and the carriers

**`suTensor.Color`**, an inductive, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L80).

> The colors of the complex tensors of `SU(N)`.

```lean
inductive Color
  /-- The fundamental color. -/
  | fund : Color
  /-- The anti-fundamental color. -/
  | antiFund : Color
  /-- The adjoint color. -/
  | adj : Color
  deriving DecidableEq
```

**`suTensor.modules`**, an abbrev, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L92).

> The carriers of the three colors.

```lean
abbrev modules : Color → Type
```

**`suTensor.modulesAddCommGroup`**, an instance, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L97).

```lean
noncomputable instance modulesAddCommGroup : ∀ c, AddCommGroup (modules N c)
```

**`suTensor.modulesModule`**, an instance, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L102).

```lean
noncomputable instance modulesModule : ∀ c, Module ℂ (modules N c)
```

**`suTensor.basisIdx`**, an abbrev, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L109).

> The labels of the basis vectors, `Fin N` for the fundamental and anti-fundamental colors,
> and the labels of the generalized Gell-Mann matrices for the adjoint.

```lean
abbrev basisIdx : Color → Type
```

**`suTensor.basisIdxFintype`**, an instance, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L114).

```lean
instance basisIdxFintype : ∀ c, Fintype (basisIdx N c)
```

**`suTensor.basisIdxDecidableEq`**, an instance, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L119).

```lean
instance basisIdxDecidableEq : ∀ c, DecidableEq (basisIdx N c)
```

**`suTensor.basis`**, an abbrev, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L126).

> The bases of the carriers, the standard basis for the fundamental and anti-fundamental colors,
> and the generalized Gell-Mann matrices for the adjoint.

```lean
noncomputable abbrev basis : (c : Color) → Basis (basisIdx N c) ℂ (modules N c)
```

## B. The representations

**`suTensor.fundRep`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L138).

> The fundamental representation, `v ↦ g v`.

```lean
noncomputable def fundRep : Representation ℂ (SU N) (Fin N → ℂ)
```

**`suTensor.antiFundRep`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L149).

> The anti-fundamental representation, `v ↦ (g⁻¹)ᵀ v`, the dual of the fundamental one. For
> unitary `g`, `(g⁻¹)ᵀ` is the complex conjugate of `g`.

```lean
noncomputable def antiFundRep : Representation ℂ (SU N) (Fin N → ℂ)
```

**`suTensor.rep`**, an abbrev, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L159).

> The representations of the three colors.

```lean
noncomputable abbrev rep : (c : Color) → Representation ℂ (SU N) (modules N c)
```

## C. The contractions

**`suTensor.fundContr`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L172).

> The contraction of a fundamental against an anti-fundamental index, the dot product
> `v ⊗ w ↦ ∑ vᵢ wᵢ`.

```lean
noncomputable def fundContr : ((fundRep N).tprod (antiFundRep N)).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)
```

**`suTensor.antiFundContr`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L181).

> The contraction of an anti-fundamental against a fundamental index, the dot product
> `w ⊗ v ↦ ∑ wᵢ vᵢ`.

```lean
noncomputable def antiFundContr : ((antiFundRep N).tprod (fundRep N)).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)
```

## D. The units

> The unit of a color is determined by its contraction. For a contraction `V ⊗ W → ℂ`, an element
> `U ∈ W ⊗ V` is sent to the endomorphism `x ↦ ∑ contr (x ⊗ wᵢ) vᵢ` of `V` (`coevalMap`), and `U` is
> a unit exactly when this is the identity. When the contraction separates `W` the map is
> injective, so a unit is unique, and it is invariant, its transform being sent to
> `g ∘ id ∘ g⁻¹ = id`.

**`suTensor.coevalMap`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L208).

> The endomorphism `x ↦ ∑ contr (x ⊗ wᵢ) vᵢ` of `V` attached to `∑ wᵢ ⊗ vᵢ ∈ W ⊗ V`.

```lean
noncomputable def coevalMap (contr : (ρ.tprod σ).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)) : W ⊗[ℂ] V →ₗ[ℂ] V →ₗ[ℂ] V
```

**`suTensor.coevalMap_tmul`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L216).

```lean
lemma coevalMap_tmul (w : W) (v x : V) :
    coevalMap contr (w ⊗ₜ v) x = contr (x ⊗ₜ w) • v
```

**`suTensor.lid_rTensor_assoc_symm_eq_coevalMap`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L220).

> The contraction of `x` against the first factor of `U` is `coevalMap contr U x`.

```lean
lemma lid_rTensor_assoc_symm_eq_coevalMap (x : V) (U : W ⊗[ℂ] V) :
    TensorProduct.lid ℂ V (contr.toLinearMap.rTensor V
      ((TensorProduct.assoc ℂ V W V).symm (x ⊗ₜ[ℂ] U))) = coevalMap contr U x
```

**`suTensor.coevalMap_injective`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L228).

> `coevalMap` is injective when the contraction separates `W`.

```lean
lemma coevalMap_injective [FiniteDimensional ℂ V]
    (h : Function.Injective (TensorProduct.curry contr.toLinearMap).flip) :
    Function.Injective (coevalMap contr)
```

**`suTensor.coevalMap_map`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L237).

> Transforming both factors of `U` conjugates `coevalMap contr U`, by the invariance of the
> contraction.

```lean
lemma coevalMap_map (g : SU N) (U : W ⊗[ℂ] V) :
    coevalMap contr (TensorProduct.map (σ g) (ρ g) U)
      = ρ g ∘ₗ coevalMap contr U ∘ₗ ρ g⁻¹
```

**`suTensor.map_eq_self_of_coevalMap_eq_id`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L252).

> An element whose `coevalMap` is the identity is invariant, when the contraction separates
> `W`.

```lean
lemma map_eq_self_of_coevalMap_eq_id [FiniteDimensional ℂ V]
    (h : Function.Injective (TensorProduct.curry contr.toLinearMap).flip) {U : W ⊗[ℂ] V}
    (hU : coevalMap contr U = LinearMap.id) (g : SU N) :
    TensorProduct.map (σ g) (ρ g) U = U
```

**`suTensor.unitOf`**, a def, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L262).

> The unit intertwining map `a ↦ a • U` of an invariant element `U ∈ W ⊗ V`.

```lean
noncomputable def unitOf {U : W ⊗[ℂ] V} (hU : ∀ g : SU N, TensorProduct.map (σ g) (ρ g) U = U) :
    (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap (σ.tprod ρ)
```

**`suTensor.unitOf_apply`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L271).

```lean
lemma unitOf_apply {U : W ⊗[ℂ] V} (hU : ∀ g : SU N, TensorProduct.map (σ g) (ρ g) U = U)
    (a : ℂ) : unitOf hU a = a • U
```

**`suTensor.pairUnitVal`**, a def, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L278).

> The element `∑ eᵢ ⊗ eᵢ` of `ℂᴺ ⊗ ℂᴺ`, the unit of the fundamental and of the anti-fundamental
> color.

```lean
noncomputable def pairUnitVal : (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ)
```

**`suTensor.comm_pairUnitVal`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L281).

```lean
lemma comm_pairUnitVal : TensorProduct.comm ℂ _ _ (pairUnitVal N) = pairUnitVal N
```

**`suTensor.dotProduct_flip_injective`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L285).

> The dot product separates vectors.

```lean
lemma dotProduct_flip_injective : Function.Injective
    (TensorProduct.curry (TensorProduct.lift (dotProductBilin ℂ ℂ) :
      (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ) →ₗ[ℂ] ℂ)).flip
```

**`suTensor.coevalMap_pairUnitVal`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L291).

> Contracting against `∑ eᵢ ⊗ eᵢ` by the dot product is the identity.

```lean
lemma coevalMap_pairUnitVal {ρ σ : Representation ℂ (SU N) (Fin N → ℂ)}
    (contr : (ρ.tprod σ).IntertwiningMap (Representation.trivial ℂ (SU N) ℂ))
    (h : contr.toLinearMap = TensorProduct.lift (dotProductBilin ℂ ℂ)) :
    coevalMap contr (pairUnitVal N) = LinearMap.id
```

**`suTensor.fundUnit`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L302).

> The unit of the fundamental color, `∑ eᵢ ⊗ eᵢ` in anti-fundamental ⊗ fundamental.

```lean
noncomputable def fundUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((antiFundRep N).tprod (fundRep N))
```

**`suTensor.antiFundUnit`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L308).

> The unit of the anti-fundamental color, `∑ eᵢ ⊗ eᵢ` in fundamental ⊗ anti-fundamental.

```lean
noncomputable def antiFundUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((fundRep N).tprod (antiFundRep N))
```

**`suTensor.adjUnitVal`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L315).

> The element `∑ b_a ⊗ bᵃ` of `su(N)_ℂ ⊗ su(N)_ℂ`, for the Gell-Mann basis `b` and its dual basis
> `bᵃ` under the trace form, the unit of the adjoint color.

```lean
noncomputable def adjUnitVal : (SUAlgebraComplexified N) ⊗[ℂ] (SUAlgebraComplexified N)
```

**`suTensor.coevalMap_adjUnitVal`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L318).

```lean
lemma coevalMap_adjUnitVal : coevalMap (adjContr N) (adjUnitVal N) = LinearMap.id
```

**`suTensor.coevalMap_comm_adjUnitVal`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L328).

```lean
lemma coevalMap_comm_adjUnitVal :
    coevalMap (adjContr N) (TensorProduct.comm ℂ _ _ (adjUnitVal N)) = LinearMap.id
```

**`suTensor.comm_adjUnitVal`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L344).

> The unit of the adjoint color is symmetric.

```lean
lemma comm_adjUnitVal : TensorProduct.comm ℂ _ _ (adjUnitVal N) = adjUnitVal N
```

**`suTensor.adjUnit`**, a def, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L349).

> The unit of the adjoint color, `∑ b_a ⊗ bᵃ`.

```lean
noncomputable def adjUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((adjRep N).tprod (adjRep N))
```

## E. The tensor species

**`suTensor`**, a def, [line 363](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L363).

> The complex tensor species of `SU(N)`, with fundamental, anti-fundamental and adjoint
> indices. The fundamental and anti-fundamental colors are dual to each other, the adjoint
> color dual to itself.

```lean
noncomputable def _root_.suTensor : TensorSpecies ℂ Color (SU N)
    (modules N) (basisIdx N) (rep N) (basis N)
```

## F. The matrices of the fundamental and anti-fundamental colors

**`suTensor.toMatrix_fundRep`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L423).

> The matrix of `g` on the fundamental color is `g`.

```lean
lemma toMatrix_fundRep (g : SU N) :
    LinearMap.toMatrix (Pi.basisFun ℂ (Fin N)) (Pi.basisFun ℂ (Fin N)) (fundRep N g) = g.1
```

**`suTensor.toMatrix_antiFundRep`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L429).

> The matrix of `g` on the anti-fundamental color is `(g⁻¹)ᵀ`.

```lean
lemma toMatrix_antiFundRep (g : SU N) :
    LinearMap.toMatrix (Pi.basisFun ℂ (Fin N)) (Pi.basisFun ℂ (Fin N)) (antiFundRep N g)
      = (g⁻¹).1ᵀ
```

## G. One adjoint index

**`suTensor.invariants_adj_eq_bot`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean#L445).

> There are no invariant tensors with one adjoint index but zero. A tensor with one adjoint
> index is `fromSingleT` of an element of the adjoint representation, which has none.

```lean
lemma invariants_adj_eq_bot : ((suTensor N).tensorRep ![.adj]).invariants = ⊥
```

## Depends on

- [The adjoint representation of `SU(N)`](globalgaugegroup-su-adjoint.md)
- [Equivariant maps out of the tensors of a species](../../../relativity/tensors/equivariant.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/TensorSpecies.lean)
