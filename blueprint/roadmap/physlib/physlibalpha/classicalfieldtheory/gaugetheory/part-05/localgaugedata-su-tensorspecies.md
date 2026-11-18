---
declaration: module
origin: cited
lean: suTensor.Color, suTensor.modules, suTensor.modulesAddCommGroup, suTensor.modulesModule, suTensor.basisIdx, suTensor.basisIdxFintype, suTensor.basisIdxDecidableEq, suTensor.basis
statement: formalized
proof: formalized
---

# The complex tensor species of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.TensorSpecies`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean): 37 declarations, 26 with a docstring.

## i. Overview

> The complex tensors of `SU(N)` carry three kinds of index, in analogy with the complex Lorentz
> tensors `complexLorentzTensor`: a fundamental index, an anti-fundamental index and an adjoint
> index. `suTensor N` is the tensor species with these three colors. The fundamental color is
> `Fin N → ℂ` moved by `g`, the anti-fundamental color is `Fin N → ℂ` moved by `(g⁻¹)ᵀ` (for a unitary
> `g` the complex conjugate), and the adjoint color is the complexification
> `SUAlgebraComplexified N = ℂ ⊗[ℝ] su(N)` of the Lie algebra `SUAlgebra N` of traceless hermitian
> matrices, moved by the adjoint representation `adjRep` with the generalized Gell-Mann matrices as
> basis, as set up in `LocalGaugeData.SU.Adjoint`. The type of tensors with colors `c₁, …, cₙ` is
> written `SuT[N, c₁, …, cₙ]`.
>
> The fundamental and anti-fundamental colors are dual to each other and contract by the dot
> product, with unit `∑ eᵢ ⊗ eᵢ`. The adjoint color is dual to itself and contracts by the trace
> form `tr (A B)` (`adjContr`), with unit `∑ λ_a ⊗ λᵃ` for the Gell-Mann matrices `λ_a` and their
> trace-dual basis `λᵃ =
>   λ\_a / 2`. In these bases the matrix of `g⁻¹` on each color is the conjugate transpose
> of that of `g`, so the colors are closed under adjoints (F) and the general results on equivariant
> maps out of the tensors of a species apply. The
> species has no metric (`TensorSpecies.WithMetric`): for `N ≥ 3` the fundamental of `SU(N)` is not
> self-dual, so there is no invariant in `ℂᴺ ⊗ ℂᴺ` to raise and lower its indices with.

## ii. Key results

> - `suTensor.Color` : the fundamental, anti-fundamental and adjoint colors.
> - `suTensor.fundRep`, `suTensor.antiFundRep` : the fundamental and anti-fundamental
>   representations.
> - `suTensor` : the complex tensor species of `SU(N)`, with the notation `SuT[N, c₁, …, cₙ]`.
> - `suTensor.isAdjointClosed` : the colors are closed under adjoints, so the general results on
>   equivariant maps (`TensorSpecies.IsEquivariant`) apply.

## iv. References

> * None.

## A. The colors and the carriers

**`suTensor.Color`**, an inductive, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L74).

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

**`suTensor.modules`**, an abbrev, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L86).

> The carriers of the three colors.

```lean
abbrev modules : Color → Type
```

**`suTensor.modulesAddCommGroup`**, an instance, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L91).

```lean
noncomputable instance modulesAddCommGroup : ∀ c, AddCommGroup (modules N c)
```

**`suTensor.modulesModule`**, an instance, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L96).

```lean
noncomputable instance modulesModule : ∀ c, Module ℂ (modules N c)
```

**`suTensor.basisIdx`**, an abbrev, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L103).

> The labels of the basis vectors: `Fin N` for the fundamental and anti-fundamental colors,
> and the labels of the generalized Gell-Mann matrices for the adjoint.

```lean
abbrev basisIdx : Color → Type
```

**`suTensor.basisIdxFintype`**, an instance, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L108).

```lean
instance basisIdxFintype : ∀ c, Fintype (basisIdx N c)
```

**`suTensor.basisIdxDecidableEq`**, an instance, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L113).

```lean
instance basisIdxDecidableEq : ∀ c, DecidableEq (basisIdx N c)
```

**`suTensor.basis`**, an abbrev, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L120).

> The bases of the carriers: the standard basis for the fundamental and anti-fundamental colors,
> and the generalized Gell-Mann matrices for the adjoint.

```lean
noncomputable abbrev basis : (c : Color) → Basis (basisIdx N c) ℂ (modules N c)
```

## B. The representations

**`suTensor.fundRep`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L132).

> The fundamental representation, `v ↦ g v`.

```lean
noncomputable def fundRep : Representation ℂ (SU N) (Fin N → ℂ)
```

**`suTensor.antiFundRep`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L143).

> The anti-fundamental representation, `v ↦ (g⁻¹)ᵀ v`, the dual of the fundamental one. For
> unitary `g`, `(g⁻¹)ᵀ` is the complex conjugate of `g`.

```lean
noncomputable def antiFundRep : Representation ℂ (SU N) (Fin N → ℂ)
```

**`suTensor.rep`**, an abbrev, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L153).

> The representations of the three colors.

```lean
noncomputable abbrev rep : (c : Color) → Representation ℂ (SU N) (modules N c)
```

## C. The contractions

**`suTensor.fundContr`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L166).

> The contraction of a fundamental against an anti-fundamental index, the dot product
> `v ⊗ w ↦ ∑ vᵢ wᵢ`.

```lean
noncomputable def fundContr : ((fundRep N).tprod (antiFundRep N)).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)
```

**`suTensor.antiFundContr`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L175).

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

**`suTensor.coevalMap`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L202).

> The endomorphism `x ↦ ∑ contr (x ⊗ wᵢ) vᵢ` of `V` attached to `∑ wᵢ ⊗ vᵢ ∈ W ⊗ V`.

```lean
noncomputable def coevalMap (contr : (ρ.tprod σ).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)) : W ⊗[ℂ] V →ₗ[ℂ] V →ₗ[ℂ] V
```

**`suTensor.coevalMap_tmul`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L210).

```lean
lemma coevalMap_tmul (w : W) (v x : V) :
    coevalMap contr (w ⊗ₜ v) x = contr (x ⊗ₜ w) • v
```

**`suTensor.lid_rTensor_assoc_symm_eq_coevalMap`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L214).

> The contraction of `x` against the first factor of `U` is `coevalMap contr U x`.

```lean
lemma lid_rTensor_assoc_symm_eq_coevalMap (x : V) (U : W ⊗[ℂ] V) :
    TensorProduct.lid ℂ V (contr.toLinearMap.rTensor V
      ((TensorProduct.assoc ℂ V W V).symm (x ⊗ₜ[ℂ] U))) = coevalMap contr U x
```

**`suTensor.coevalMap_injective`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L222).

> `coevalMap` is injective when the contraction separates `W`.

```lean
lemma coevalMap_injective [FiniteDimensional ℂ V]
    (h : Function.Injective (TensorProduct.curry contr.toLinearMap).flip) :
    Function.Injective (coevalMap contr)
```

**`suTensor.coevalMap_map`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L231).

> Transforming both factors of `U` conjugates `coevalMap contr U`, by the invariance of the
> contraction.

```lean
lemma coevalMap_map (g : SU N) (U : W ⊗[ℂ] V) :
    coevalMap contr (TensorProduct.map (σ g) (ρ g) U)
      = ρ g ∘ₗ coevalMap contr U ∘ₗ ρ g⁻¹
```

**`suTensor.map_eq_self_of_coevalMap_eq_id`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L246).

> An element whose `coevalMap` is the identity is invariant, when the contraction separates
> `W`.

```lean
lemma map_eq_self_of_coevalMap_eq_id [FiniteDimensional ℂ V]
    (h : Function.Injective (TensorProduct.curry contr.toLinearMap).flip) {U : W ⊗[ℂ] V}
    (hU : coevalMap contr U = LinearMap.id) (g : SU N) :
    TensorProduct.map (σ g) (ρ g) U = U
```

**`suTensor.unitOf`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L256).

> The unit intertwining map `a ↦ a • U` of an invariant element `U ∈ W ⊗ V`.

```lean
noncomputable def unitOf {U : W ⊗[ℂ] V} (hU : ∀ g : SU N, TensorProduct.map (σ g) (ρ g) U = U) :
    (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap (σ.tprod ρ)
```

**`suTensor.unitOf_apply`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L265).

```lean
lemma unitOf_apply {U : W ⊗[ℂ] V} (hU : ∀ g : SU N, TensorProduct.map (σ g) (ρ g) U = U)
    (a : ℂ) : unitOf hU a = a • U
```

**`suTensor.pairUnitVal`**, a def, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L272).

> The element `∑ eᵢ ⊗ eᵢ` of `ℂᴺ ⊗ ℂᴺ`, the unit of the fundamental and of the anti-fundamental
> color.

```lean
noncomputable def pairUnitVal : (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ)
```

**`suTensor.comm_pairUnitVal`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L275).

```lean
lemma comm_pairUnitVal : TensorProduct.comm ℂ _ _ (pairUnitVal N) = pairUnitVal N
```

**`suTensor.dotProduct_flip_injective`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L279).

> The dot product separates vectors.

```lean
lemma dotProduct_flip_injective : Function.Injective
    (TensorProduct.curry (TensorProduct.lift (dotProductBilin ℂ ℂ) :
      (Fin N → ℂ) ⊗[ℂ] (Fin N → ℂ) →ₗ[ℂ] ℂ)).flip
```

**`suTensor.coevalMap_pairUnitVal`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L285).

> Contracting against `∑ eᵢ ⊗ eᵢ` by the dot product is the identity.

```lean
lemma coevalMap_pairUnitVal {ρ σ : Representation ℂ (SU N) (Fin N → ℂ)}
    (contr : (ρ.tprod σ).IntertwiningMap (Representation.trivial ℂ (SU N) ℂ))
    (h : contr.toLinearMap = TensorProduct.lift (dotProductBilin ℂ ℂ)) :
    coevalMap contr (pairUnitVal N) = LinearMap.id
```

**`suTensor.fundUnit`**, a def, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L296).

> The unit of the fundamental color, `∑ eᵢ ⊗ eᵢ` in anti-fundamental ⊗ fundamental.

```lean
noncomputable def fundUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((antiFundRep N).tprod (fundRep N))
```

**`suTensor.antiFundUnit`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L302).

> The unit of the anti-fundamental color, `∑ eᵢ ⊗ eᵢ` in fundamental ⊗ anti-fundamental.

```lean
noncomputable def antiFundUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((fundRep N).tprod (antiFundRep N))
```

**`suTensor.adjUnitVal`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L309).

> The element `∑ b_a ⊗ bᵃ` of `su(N)_ℂ ⊗ su(N)_ℂ`, for the Gell-Mann basis `b` and its dual basis
> `bᵃ` under the trace form: the unit of the adjoint color.

```lean
noncomputable def adjUnitVal : (SUAlgebraComplexified N) ⊗[ℂ] (SUAlgebraComplexified N)
```

**`suTensor.coevalMap_adjUnitVal`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L312).

```lean
lemma coevalMap_adjUnitVal : coevalMap (adjContr N) (adjUnitVal N) = LinearMap.id
```

**`suTensor.coevalMap_comm_adjUnitVal`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L322).

```lean
lemma coevalMap_comm_adjUnitVal :
    coevalMap (adjContr N) (TensorProduct.comm ℂ _ _ (adjUnitVal N)) = LinearMap.id
```

**`suTensor.comm_adjUnitVal`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L338).

> The unit of the adjoint color is symmetric.

```lean
lemma comm_adjUnitVal : TensorProduct.comm ℂ _ _ (adjUnitVal N) = adjUnitVal N
```

**`suTensor.adjUnit`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L343).

> The unit of the adjoint color, `∑ b_a ⊗ bᵃ`.

```lean
noncomputable def adjUnit : (Representation.trivial ℂ (SU N) ℂ).IntertwiningMap
    ((adjRep N).tprod (adjRep N))
```

## E. The tensor species

**`suTensor`**, a def, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L360).

> The complex tensor species of `SU(N)`, with fundamental, anti-fundamental and adjoint
> indices. The fundamental and anti-fundamental colors are dual to each other, the adjoint
> color dual to itself.

```lean
noncomputable def suTensor (N : ℕ) : TensorSpecies ℂ suTensor.Color (SU N)
    (suTensor.modules N) (suTensor.basisIdx N) (suTensor.rep N)
    (suTensor.basis N)
```

## F. The colors are closed under adjoints

> For unitary `g`, the matrix of `g⁻¹` on each color is the conjugate transpose of that of `g`: on
> the fundamental color `g⁻¹ = g†`, on the anti-fundamental color `gᵀ = ((g⁻¹)ᵀ)†`, and on the
> adjoint color, in the hermitian and orthogonal Gell-Mann basis, the matrix entries are
> `tr (λ_a g λ_b g⁻¹) / 2`. So every list of colors is closed under adjoints, and the general results
> on equivariant maps (`PhyslibAlpha.Relativity.Tensors.Equivariant`) apply to the tensors of `SU(N)`:
> the invariants in the range of an equivariant map out of `(suTensor N).Tensor c` come from invariant
> tensors.

**`suTensor.toMatrix_fundRep`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L434).

```lean
lemma toMatrix_fundRep (g : SU N) :
    LinearMap.toMatrix (Pi.basisFun ℂ (Fin N)) (Pi.basisFun ℂ (Fin N)) (fundRep N g) = g.1
```

**`suTensor.toMatrix_antiFundRep`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L439).

```lean
lemma toMatrix_antiFundRep (g : SU N) :
    LinearMap.toMatrix (Pi.basisFun ℂ (Fin N)) (Pi.basisFun ℂ (Fin N)) (antiFundRep N g)
      = (g⁻¹).1ᵀ
```

**`suTensor.toMatrix_rep_inv`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L448).

> On every color, the matrix of `g⁻¹` is the conjugate transpose of the matrix of `g`.

```lean
lemma toMatrix_rep_inv (k : Color) (g : SU N) :
    LinearMap.toMatrix (basis N k) (basis N k) (rep N k g⁻¹)
      = (LinearMap.toMatrix (basis N k) (basis N k) (rep N k g))ᴴ
```

**`suTensor.isAdjointClosed`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean#L466).

> Every list of colors of the `SU(N)` tensors is closed under adjoints, with `g' = g⁻¹`.

```lean
lemma isAdjointClosed {n : ℕ} (c : Fin n → Color) : (suTensor N).IsAdjointClosed c
```

## Depends on

- [The adjoint representation of `SU(N)`](../part-04/localgaugedata-su-adjoint.md)
- [Equivariant maps out of the tensors of a species](../../../relativity/tensors/equivariant.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/TensorSpecies.lean)
