---
declaration: module
origin: cited
lean: Lorentz.IsVectorLeftRightWeyl, Lorentz.IsVectorLeftRightWeyl.repLorentz_map_indexBasis, Lorentz.IsVectorLeftRightWeyl.repLorentz_sum_smul, Lorentz.IsVectorLeftRightWeyl.vectorPair, Lorentz.IsVectorLeftRightWeyl.isLorentzCovariant_vectorPair, Lorentz.IsVectorLeftRightWeyl.map_indexBasis_eq_sum_vectorPair, Lorentz.IsVectorLeftRightWeyl.span_range_vectorPair, Lorentz.IsVectorLeftRightWeyl.ofComponents_vectorPair_metric
statement: formalized
proof: formalized
---

# Lorentz invariants of a four-vector index and a left-right Weyl pair

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.IsVectorLeftRightWeyl`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean): 31 declarations, 30 with a docstring.

## i. Overview

> A family `T^{μ α α'}` carrying one four-vector index and one opposite-chirality Weyl pair is an
> equivariant linear map `f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B`, `IsVectorLeftRightWeyl` (A). Every
> Lorentz invariant in the range of `f` is a multiple of `f σ^^^`, the image of the Pauli
> matrices as a tensor, the shape of the fermion kinetic term `ψ̄_{α'} σ̄^{μ α' α} ∂_μ ψ_α`. That is
> `IsVectorLeftRightWeyl.exists_smul_map_pauliMatrix_add_of_invariant`, stated modulo a
> Lorentz-stable submodule `S`, and packaged as `IsVectorLeftRightWeyl.invariantReductionToSpan`
> (D).
>
> An opposite-chirality Weyl pair carries the `(1/2, 1/2)` representation, which is the
> four-vector representation, so the three indices are two four-vector indices, and two of those
> admit only the metric. The proof makes that literal. The components `f (e_μ ⊗ e_α ⊗ e_α')` of `f`
> move as `T^{μ α α'}` (B); contracting their Weyl pair against the covariant Pauli matrices
> `PauliMatrix.pauliLower`, which intertwine the two index laws (`SL2C.sum_pauliLower_mul_sl2c`),
> gives a family `vectorPair f` of two four-vector indices, whose map is equivariant, whose range
> is the range of `f` by Fierz completeness, and which sends the metric to `f σ^^^` (C); `RankTwo`
> supplies the classification (D). A family of components is turned back into a map by
> `ofVectorComponents` (E).
>
> The Standard Model's fermion symbols are `Module.Dual`-valued, so their spinor indices are dual
> Weyl indices: an equivariant map out of `ℂT[.up, .downR, .downL]`, `IsVectorDualLeftRightWeyl`.
> Dualising both Weyl indices, `dualWeylMap`, is an equivariant surjection from
> `ℂT[.up, .upL, .upR]` carrying `σ^^^` to `σ^__`, so every invariant in the range of such a map is
> a multiple of `f σ^__` (F). A family of dual components is turned into a map by
> `ofDualVectorComponents` (G).

## ii. Key results

> - `Lorentz.IsVectorLeftRightWeyl.invariantReductionToSpan` : the invariants reduce to `f σ^^^`.
> - `Lorentz.dualWeylMap` : the dualisation of the Weyl indices.
> - `Lorentz.IsVectorDualLeftRightWeyl.invariantReductionToSpan` : the invariants reduce to
>   `f σ^__`.

## iv. References

> * None.

## A. Vector-Weyl families as equivariant maps

**`Lorentz.IsVectorLeftRightWeyl`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L77).

> A family with a four-vector index and a left- and a right-handed Weyl index `T^{μ α α'}`:
> an equivariant linear map out of `ℂT[.up, .upL, .upR]`.

```lean
abbrev IsVectorLeftRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B) : Prop
```

## B. The components of an equivariant map

> The components `f (e_μ ⊗ e_α ⊗ e_α')` of an equivariant map are moved by the Lorentz matrix on
> the vector index, by the matrix of `g` on the left Weyl index and by its complex conjugate on
> the right one.

**`Lorentz.IsVectorLeftRightWeyl.repLorentz_map_indexBasis`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L102).

> The components of an equivariant map are moved as `T^{μ α α'}`, the summed index first in
> each factor.

```lean
lemma repLorentz_map_indexBasis (g : SL(2,ℂ)) (d : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2) :
    repLorentz g (f (indexBasis d)) = ∑ e : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2,
      ((((SL2C.toLorentzGroup g).1 e.1 d.1 : ℝ) : ℂ)
        * (g.1 e.2.1 d.2.1 * star (g.1 e.2.2 d.2.2))) • f (indexBasis e)
```

**`Lorentz.IsVectorLeftRightWeyl.repLorentz_sum_smul`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L118).

> Moving a contraction of the Weyl pair at vector index `μ`: the vector index moves by the
> Lorentz matrix and the coefficients of the Weyl pair by the matrix of `g` and its complex
> conjugate.

```lean
lemma repLorentz_sum_smul (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (c : Fin 2 × Fin 2 → ℂ) :
    repLorentz g (∑ a : Fin 2 × Fin 2, c a • f (indexBasis (μ, a)))
      = ∑ ν : Fin 1 ⊕ Fin 3, (((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ)
        • ∑ q : Fin 2 × Fin 2, (∑ d : Fin 2 × Fin 2, c d * (g.1 q.1 d.1 * star (g.1 q.2 d.2)))
          • f (indexBasis (ν, q))
```

## C. The reduction to a pair of four-vector indices

> Contracting the Weyl pair of the components against the covariant Pauli matrices gives a
> family `vectorPair f` of two four-vector indices, whose map `ofComponents (vectorPair f)` is a
> rank-two Lorentz family. By Fierz completeness the contraction is invertible, so its span is the
> range of `f`, and the image of the metric under its map is `f σ^^^`.

**`Lorentz.IsVectorLeftRightWeyl.vectorPair`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L147).

> The family of two four-vector indices obtained by contracting the Weyl pair of the
> components of `f` against the covariant Pauli matrices.

```lean
noncomputable def vectorPair (f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B) :
    (Fin 2 → Fin 1 ⊕ Fin 3) → B
```

**`Lorentz.IsVectorLeftRightWeyl.isLorentzCovariant_vectorPair`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L154).

> The reduced family is a rank-two Lorentz family: the intertwining identity
> `SL2C.sum_pauliLower_mul_sl2c` carries the Weyl pair into a second vector index.

```lean
lemma isLorentzCovariant_vectorPair :
    IsLorentzCovariant 2 B repLorentz (ofComponents (vectorPair f))
```

**`Lorentz.IsVectorLeftRightWeyl.map_indexBasis_eq_sum_vectorPair`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L170).

> The reduction is invertible: by the Fierz completeness relation each component of `f` is
> recovered from the reduced family.

```lean
lemma map_indexBasis_eq_sum_vectorPair (f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B)
    (μ : Fin 1 ⊕ Fin 3) (b : Fin 2 × Fin 2) :
    f (indexBasis (μ, b)) = ∑ ρ : Fin 1 ⊕ Fin 3,
      ((2 : ℂ)⁻¹ * PauliMatrix.pauliLower ρ b.2 b.1) • vectorPair f ![μ, ρ]
```

**`Lorentz.IsVectorLeftRightWeyl.span_range_vectorPair`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L199).

> The reduction does not change the span: the reduced family spans the range of `f`.

```lean
lemma span_range_vectorPair (f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B) :
    Submodule.span ℂ (Set.range (vectorPair f)) = LinearMap.range f
```

**`Lorentz.IsVectorLeftRightWeyl.ofComponents_vectorPair_metric`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L210).

> The image of the metric under the map of the reduced family is the image `f σ^^^` of the
> Pauli tensor: the two lowerings of the vector index cancel, so no sign and no scalar appear.

```lean
lemma ofComponents_vectorPair_metric (f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B) :
    ofComponents (vectorPair f) RankTwo.metric = f σ^^^
```

## D. The classification of the Lorentz invariants

> `RankTwo` classifies the invariants of the range of `ofComponents (vectorPair f)`, which is the
> range of `f`, and the image of the metric under it is `f σ^^^`.

**`Lorentz.IsVectorLeftRightWeyl.repLorentz_map_pauliMatrix`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L238).

> The image `f σ^^^` of the Pauli tensor is Lorentz invariant.

```lean
lemma repLorentz_map_pauliMatrix (g : SL(2,ℂ)) : repLorentz g (f σ^^^) = f σ^^^
```

**`Lorentz.IsVectorLeftRightWeyl.exists_smul_map_pauliMatrix_add_of_invariant`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L245).

> Every Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is a
> multiple of the image `f σ^^^` of the Pauli tensor plus an element of `S`: the shape of the
> fermion kinetic term.

```lean
lemma exists_smul_map_pauliMatrix_add_of_invariant (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ LinearMap.range f ⊔ S) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ a : ℂ, ∃ y ∈ S, x = a • f σ^^^ + y
```

**`Lorentz.IsVectorLeftRightWeyl.invariantReductionToSpan`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L257).

> The Lorentz invariants of the range of `f` reduce to the span of the image `f σ^^^` of the
> Pauli tensor.

```lean
noncomputable def invariantReductionToSpan :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

## E. Maps from components

> A family `T (μ, α, α')` of vectors is the linear map `ofVectorComponents T` sending
> `e_μ ⊗ e_α ⊗ e_α'` to `T (μ, α, α')`, and it is equivariant when the vectors are moved as the
> basis tensors are.

**`Lorentz.ofVectorComponents`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L284).

> The linear map out of `ℂT[.up, .upL, .upR]` sending `e_μ ⊗ e_α ⊗ e_α'` to
> `T (μ, α, α')`.

```lean
noncomputable def ofVectorComponents (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B) :
    ℂT[.up, .upL, .upR] →ₗ[ℂ] B
```

**`Lorentz.ofVectorComponents_indexBasis`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L289).

```lean
lemma ofVectorComponents_indexBasis (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B)
    (d : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2) : ofVectorComponents T (indexBasis d) = T d
```

**`Lorentz.range_ofVectorComponents`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L294).

> The range of `ofVectorComponents T` is the span of the vectors `T d`.

```lean
lemma range_ofVectorComponents (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B) :
    LinearMap.range (ofVectorComponents T) = Submodule.span ℂ (Set.range T)
```

**`Lorentz.isVectorLeftRightWeyl_ofVectorComponents`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L301).

> `ofVectorComponents T` is equivariant when `T (μ, α, α')` is moved as `T^{μ α α'}`: the
> vector index by the Lorentz matrix, the left index by the matrix of `g` and the right index by
> its complex conjugate, the summed index first in each factor.

```lean
lemma isVectorLeftRightWeyl_ofVectorComponents {repLorentz : Representation ℂ SL(2,ℂ) B}
    (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B)
    (hT : ∀ (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2),
      repLorentz g (T (μ, l)) = ∑ (ν : Fin 1 ⊕ Fin 3), ∑ (a : Fin 2 × Fin 2),
        ((((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ)
          * (g.1 a.1 l.1 * star (g.1 a.2 l.2))) • T (ν, a)) :
    IsVectorLeftRightWeyl B repLorentz (ofVectorComponents T)
```

## F. Dual Weyl indices

> A family `T^μ{}_{α' α}` with a four-vector index and a dual right- and a dual left-handed Weyl
> index is an equivariant map out of `ℂT[.up, .downR, .downL]`, `IsVectorDualLeftRightWeyl`.
> Dualising both Weyl indices, `dualWeylMap`, is an equivariant surjection out of
> `ℂT[.up, .upL, .upR]` which carries `σ^^^` to `σ^__`, so composing with it turns such a family
> into an `IsVectorLeftRightWeyl` family with the same range, and section D applies.

**`Lorentz.IsVectorDualLeftRightWeyl`**, an abbrev, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L339).

> A family with a four-vector index and a dual right- and a dual left-handed Weyl index
> `T^μ{}_{α' α}`: an equivariant linear map out of `ℂT[.up, .downR, .downL]`.

```lean
abbrev IsVectorDualLeftRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.up, .downR, .downL] →ₗ[ℂ] B) : Prop
```

**`Lorentz.dualWeylMap`**, a def, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L346).

> Dualising the two Weyl indices of a tensor with a four-vector index and a left-right Weyl
> pair, the dual indices listed in the order of `σ^__`.

```lean
noncomputable def dualWeylMap : ℂT[.up, .upL, .upR] →ₗ[ℂ] ℂT[.up, .downR, .downL]
```

**`Lorentz.dualWeylMap_equivariant`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L352).

> Dualising the Weyl indices commutes with the action of `SL(2,ℂ)`.

```lean
lemma dualWeylMap_equivariant (g : SL(2,ℂ)) (t : ℂT[.up, .upL, .upR]) :
    dualWeylMap (g • t) = g • dualWeylMap t
```

**`Lorentz.dualWeylMap_pauliMatrix`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L360).

> Dualising the Weyl indices of `σ^^^` gives `σ^__`.

```lean
lemma dualWeylMap_pauliMatrix : dualWeylMap σ^^^ = σ^__
```

**`Lorentz.dualWeylMap_surjective`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L368).

> Dualising the Weyl indices is surjective: the dualisations are inverted by raising the
> indices again, and the relabelling by its inverse.

```lean
lemma dualWeylMap_surjective : Function.Surjective dualWeylMap
```

**`Lorentz.IsVectorDualLeftRightWeyl.isVectorLeftRightWeyl_comp_dualWeylMap`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L387).

> Composing with the dualisation of the Weyl indices gives a family with a four-vector index
> and a left-right Weyl pair.

```lean
lemma isVectorLeftRightWeyl_comp_dualWeylMap :
    IsVectorLeftRightWeyl B repLorentz (f ∘ₗ dualWeylMap)
```

**`Lorentz.IsVectorDualLeftRightWeyl.range_comp_dualWeylMap`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L393).

> Composing with the dualisation of the Weyl indices does not change the range.

```lean
lemma range_comp_dualWeylMap : LinearMap.range (f ∘ₗ dualWeylMap) = LinearMap.range f
```

**`Lorentz.IsVectorDualLeftRightWeyl.exists_smul_map_pauliContrDown_add_of_invariant`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L400).

> Every Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is a
> multiple of the image `f σ^__` of the Pauli tensor with dual Weyl indices plus an element of
> `S`: the kinetic term of a Weyl fermion.

```lean
lemma exists_smul_map_pauliContrDown_add_of_invariant (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ LinearMap.range f ⊔ S) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ a : ℂ, ∃ y ∈ S, x = a • f σ^__ + y
```

**`Lorentz.IsVectorDualLeftRightWeyl.invariantReductionToSpan`**, a def, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L411).

> The Lorentz invariants of the range of `f` reduce to the span of the image `f σ^__` of the
> Pauli tensor with dual Weyl indices.

```lean
noncomputable def invariantReductionToSpan :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

## G. Maps from dual components

> A family `T (μ, α, α')` of vectors, indexed by a four-vector index, a dual left-handed and a
> dual right-handed Weyl index, is the linear map `ofDualVectorComponents T` sending
> `e_μ ⊗ e_α' ⊗ e_α` to `T (μ, α, α')`, and it is equivariant when the vectors are moved as the
> basis tensors are.

**`Lorentz.dualIndexEquiv`**, a def, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L440).

> The component indices of a tensor of `ℂT[.up, .downR, .downL]`, as a four-vector index, a
> dual left-handed and a dual right-handed Weyl index.

```lean
def dualIndexEquiv : ComponentIdx (S := complexLorentzTensor) ![.up, .downR, .downL] ≃
    (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2
```

**`Lorentz.ofDualVectorComponents`**, a def, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L451).

> The linear map out of `ℂT[.up, .downR, .downL]` sending `e_μ ⊗ e_α' ⊗ e_α` to
> `T (μ, α, α')`.

```lean
noncomputable def ofDualVectorComponents (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B) :
    ℂT[.up, .downR, .downL] →ₗ[ℂ] B
```

**`Lorentz.range_ofDualVectorComponents`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L456).

> The range of `ofDualVectorComponents T` is the span of the vectors `T d`.

```lean
lemma range_ofDualVectorComponents (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B) :
    LinearMap.range (ofDualVectorComponents T) = Submodule.span ℂ (Set.range T)
```

**`Lorentz.ofDualVectorComponents_mem_span`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L462).

> The image of `ofDualVectorComponents T` lies in the span of the vectors `T d`.

```lean
lemma ofDualVectorComponents_mem_span (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B)
    (t : ℂT[.up, .downR, .downL]) :
    ofDualVectorComponents T t ∈ Submodule.span ℂ (Set.range T)
```

**`Lorentz.ofDualVectorComponents_sum`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L469).

> `ofDualVectorComponents` of a sum of families is the sum of the maps.

```lean
lemma ofDualVectorComponents_sum {ι : Type*} (s : Finset ι)
    (T : ι → (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B) :
    ofDualVectorComponents (fun d => ∑ i ∈ s, T i d) = ∑ i ∈ s, ofDualVectorComponents (T i)
```

**`Lorentz.isVectorDualLeftRightWeyl_ofDualVectorComponents`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L477).

> `ofDualVectorComponents T` is equivariant when `T (μ, α, α')` is moved as `T^μ{}_{α α'}`: the
> vector index by the Lorentz matrix, the dual left index by `(g⁻¹)ᵀ` and the dual right index
> by `(g⁻¹)ᴴ`, the summed index first in each factor.

```lean
lemma isVectorDualLeftRightWeyl_ofDualVectorComponents
    {repLorentz : Representation ℂ SL(2,ℂ) B} (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B)
    (hT : ∀ (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2),
      repLorentz g (T (μ, l)) = ∑ (ν : Fin 1 ⊕ Fin 3), ∑ (a : Fin 2 × Fin 2),
        ((((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ)
          * ((g.1⁻¹)ᵀ a.1 l.1 * (g.1⁻¹)ᴴ a.2 l.2)) • T (ν, a)) :
    IsVectorDualLeftRightWeyl B repLorentz (ofDualVectorComponents T)
```

**`Lorentz.IsVectorDualLeftRightWeyl.invariantReductionToComponentSpan`**, a def, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean#L497).

> For a family whose map is equivariant, the Lorentz invariants of the span of the family
> reduce to the span of the image `ofDualVectorComponents T σ^__` of the Pauli tensor with dual
> Weyl indices.

```lean
noncomputable def IsVectorDualLeftRightWeyl.invariantReductionToComponentSpan
    {repLorentz : Representation ℂ SL(2,ℂ) B} {T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B}
    (hT : IsVectorDualLeftRightWeyl B repLorentz (ofDualVectorComponents T)) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g)
      (Submodule.span ℂ (Set.range T))
```

## Depends on

- [Lorentz invariants among two four-vector indices](invariants-ranktwo.md)
- [The covariant Pauli matrices as plain matrices](../paulimatrices/selfadjoint.md)
- [The Pauli tensor in components](../paulimatrices/totensor.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsVectorLeftRightWeyl.lean)
