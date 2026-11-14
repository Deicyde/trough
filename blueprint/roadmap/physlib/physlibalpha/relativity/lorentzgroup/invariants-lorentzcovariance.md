---
declaration: module
origin: cited
lean: Lorentz.IsLorentzCovariant, Lorentz.sum_pi_fin_two, Lorentz.vectorIdx, Lorentz.vectorIdx_symm_apply, Lorentz.coeffEquiv, Lorentz.coeffEquiv_apply, Lorentz.coeffEquiv_symm_apply, Lorentz.permT_coeffEquiv_symm
statement: formalized
proof: formalized
---

# Equivariant maps out of tensors with four-vector indices

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.LorentzCovariance`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean): 22 declarations, 20 with a docstring.

## i. Overview

> A family of vectors of a complex module `B`, indexed by `n` spacetime directions and moved by a
> representation `repLorentz` of `SL(2,ℂ)` with one factor of the Lorentz matrix per index, is
> packaged as a linear map `f` out of the complex Lorentz tensors with `n` contravariant indices,
> and `IsLorentzCovariant n B repLorentz f` says that `f` is equivariant (A). The rank-specific
> files of this folder classify the Lorentz invariants in the range of such a map.
>
> The components of a tensor, relabelled by `Fin 1 ⊕ Fin 3` in each slot, are a coefficient tensor,
> `coeffEquiv` (B), on which `SL(2,ℂ)` acts by `Invariants.act`. An invariant tensor therefore has
> an invariant coefficient tensor, `Invariants.IsInvariantCoeff`, and a classification of the
> invariant coefficient tensors is a classification of the invariants in the range of `f` (C).
>
> A family `T` of vectors indexed by `n` directions is the map `ofComponents T`, sending each basis
> tensor to the matching vector, and it is equivariant exactly when the vectors obey the
> transformation law of the components of a tensor (D),
>
> `repLorentz g (T l) = ∑_a (∏ i, Λ(g)_{a i, l i}) • T a`,
>
> with `l` free and `a` summed, and the summed index first in each factor of the Lorentz matrix
> `Λ(g)` of `g`. Permuting the slots by `permT σ` reads the coefficient tensor and the family at
> permuted index vectors (`permT_coeffEquiv_symm`, `ofComponents_comp_permT`).

## ii. Key results

> - `Lorentz.IsLorentzCovariant` : equivariant maps out of tensors with `n` four-vector indices.
> - `Lorentz.coeffEquiv` : the components of such a tensor, as a coefficient tensor.
> - `Lorentz.invariant_iff_isInvariantCoeff` : a tensor is invariant exactly when its coefficient
>   tensor is.
> - `Lorentz.IsLorentzCovariant.reducesInvariantsTo_span` : a spanning set of the invariant
>   coefficient tensors gives a reduction of the invariants of the range.
> - `Lorentz.isLorentzCovariant_ofComponents_iff` : the map of a family is equivariant exactly when
>   the family obeys the transformation law.

## iv. References

> * None.

## A. Equivariant maps

**`Lorentz.IsLorentzCovariant`**, an abbrev, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L74).

> A family with `n` four-vector indices `T^{μ₁ ⋯ μₙ}` in a representation `repLorentz` of
> `SL(2,ℂ)`: an equivariant linear map out of the complex Lorentz tensors with `n` contravariant
> indices.

```lean
abbrev IsLorentzCovariant (n : ℕ) (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B)
    (f : ℂT(fun _ : Fin n => Color.up) →ₗ[ℂ] B) : Prop
```

**`Lorentz.sum_pi_fin_two`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L80).

> A sum over families of two four-vector indices is a double sum.

```lean
lemma sum_pi_fin_two {M : Type*} [AddCommMonoid M] (f : (Fin 2 → Fin 1 ⊕ Fin 3) → M) :
    ∑ d : Fin 2 → Fin 1 ⊕ Fin 3, f d
      = ∑ x : Fin 1 ⊕ Fin 3, ∑ y : Fin 1 ⊕ Fin 3, f ![x, y]
```

## B. Coefficient tensors

**`Lorentz.vectorIdx`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L103).

> The component indices of a tensor with `n` contravariant indices, which are labelled by
> `Fin 1 ⊕ Fin 3` in each slot.

```lean
def vectorIdx (n : ℕ) :
    ComponentIdx (S := complexLorentzTensor) (fun _ : Fin n => Color.up)
      ≃ (Fin n → Fin 1 ⊕ Fin 3)
```

**`Lorentz.vectorIdx_symm_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L108).

```lean
lemma vectorIdx_symm_apply (d : Fin n → Fin 1 ⊕ Fin 3) (i : Fin n) :
    (vectorIdx n).symm d i = d i
```

**`Lorentz.coeffEquiv`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L112).

> The components of a tensor with `n` contravariant indices, as a coefficient tensor.

```lean
noncomputable def coeffEquiv (n : ℕ) :
    ℂT(fun _ : Fin n => Color.up) ≃ₗ[ℂ] ((Fin n → Fin 1 ⊕ Fin 3) → ℂ)
```

**`Lorentz.coeffEquiv_apply`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L116).

```lean
lemma coeffEquiv_apply (t : ℂT(fun _ : Fin n => Color.up)) (d : Fin n → Fin 1 ⊕ Fin 3) :
    coeffEquiv n t d = (Tensor.basis _).repr t ((vectorIdx n).symm d)
```

**`Lorentz.coeffEquiv_symm_apply`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L121).

> The tensor with coefficient tensor `c` is the combination of the basis tensors with those
> coefficients.

```lean
lemma coeffEquiv_symm_apply (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    (coeffEquiv n).symm c = ∑ d, c d • Tensor.basis _ ((vectorIdx n).symm d)
```

**`Lorentz.permT_coeffEquiv_symm`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L132).

> Permuting the slots of a tensor by `σ` permutes its coefficient tensor: slot `i` of
> `permT σ h t` holds slot `σ i` of `t`, so the new coefficient at `d` is the old one at
> `d ∘ σ.symm`.

```lean
lemma permT_coeffEquiv_symm (σ : Equiv.Perm (Fin n))
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    permT σ h ((coeffEquiv n).symm c) = (coeffEquiv n).symm fun d => c (d ∘ σ.symm)
```

**`Lorentz.coeffEquiv_smul`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L148).

> The action of `g` on tensors is the action `act` of its Lorentz matrix on coefficient
> tensors.

```lean
lemma coeffEquiv_smul (g : SL(2,ℂ)) (t : ℂT(fun _ : Fin n => Color.up)) :
    coeffEquiv n (g • t) = act (SL2C.toLorentzGroup g).1 (coeffEquiv n t)
```

**`Lorentz.invariant_iff_isInvariantCoeff`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L161).

> A tensor is invariant exactly when its coefficient tensor is an invariant coefficient
> tensor.

```lean
lemma invariant_iff_isInvariantCoeff (t : ℂT(fun _ : Fin n => Color.up)) :
    (∀ g : SL(2,ℂ), g • t = t) ↔ IsInvariantCoeff (coeffEquiv n t)
```

## C. The reduction to invariant coefficient tensors

**`Lorentz.IsLorentzCovariant.reducesInvariantsTo_span`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L182).

> When the invariant coefficient tensors lie in the span of the coefficient tensors `K j`, the
> invariants of the range of `f` reduce to the span of the images of the tensors with those
> coefficients.

```lean
lemma reducesInvariantsTo_span (hf : IsLorentzCovariant n B repLorentz f) {ι : Type*}
    (K : ι → (Fin n → Fin 1 ⊕ Fin 3) → ℂ)
    (hK : ∀ c, IsInvariantCoeff c → c ∈ Submodule.span ℂ (Set.range K)) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
      (Submodule.span ℂ (Set.range fun j => f ((coeffEquiv n).symm (K j))))
```

**`Lorentz.IsLorentzCovariant.reducesInvariantsTo_bot_of_isInvariantCoeff`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L194).

> When the only invariant coefficient tensor is zero, the range of `f` reduces to `⊥`.

```lean
lemma reducesInvariantsTo_bot_of_isInvariantCoeff (hf : IsLorentzCovariant n B repLorentz f)
    (hK : ∀ c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ, IsInvariantCoeff c → c = 0) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

**`Lorentz.IsLorentzCovariant.eq_zero_of_isInvariantCoeff`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L202).

> When the only invariant coefficient tensor is zero, so is every Lorentz invariant in the
> range of `f`.

```lean
lemma eq_zero_of_isInvariantCoeff (hf : IsLorentzCovariant n B repLorentz f)
    (hK : ∀ c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ, IsInvariantCoeff c → c = 0) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x = 0
```

## D. Maps from components

**`Lorentz.ofComponents`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L223).

> The linear map out of the tensors with `n` contravariant indices sending the basis tensor
> with components `d` to `T d`.

```lean
noncomputable def ofComponents (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    ℂT(fun _ : Fin n => Color.up) →ₗ[ℂ] B
```

**`Lorentz.ofComponents_coeffEquiv_symm`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L228).

> `ofComponents T` contracts the coefficient tensor of its argument with `T`.

```lean
lemma ofComponents_coeffEquiv_symm (T : (Fin n → Fin 1 ⊕ Fin 3) → B)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    ofComponents T ((coeffEquiv n).symm c) = ∑ d, c d • T d
```

**`Lorentz.range_ofComponents`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L235).

> The range of `ofComponents T` is the span of the vectors `T d`.

```lean
lemma range_ofComponents (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    LinearMap.range (ofComponents T) = Submodule.span ℂ (Set.range T)
```

**`Lorentz.ofComponents_sum`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L241).

> `ofComponents` of a sum of families is the sum of the maps.

```lean
lemma ofComponents_sum {ι : Type*} (s : Finset ι) (T : ι → (Fin n → Fin 1 ⊕ Fin 3) → B) :
    ofComponents (fun d => ∑ i ∈ s, T i d) = ∑ i ∈ s, ofComponents (T i)
```

**`Lorentz.comp_ofComponents`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L247).

> A linear map applied after `ofComponents T` is `ofComponents` of its values on the
> components.

```lean
lemma comp_ofComponents {B' : Type*} [AddCommGroup B'] [Module ℂ B'] (σ : B →ₗ[ℂ] B')
    (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    σ ∘ₗ ofComponents T = ofComponents fun d => σ (T d)
```

**`Lorentz.ofComponents_comp_permT`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L254).

> Precomposing `ofComponents T` with the slot permutation `permT σ` reads the family at the
> permuted index vectors `d ∘ σ`.

```lean
lemma ofComponents_comp_permT (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    ofComponents T ∘ₗ permT σ h = ofComponents fun d => T (d ∘ σ)
```

**`Lorentz.ofComponents_comp_permT_eq_neg`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L265).

> A family antisymmetric under reading its index vectors through `σ` gives a map
> antisymmetric under `permT σ`.

```lean
lemma ofComponents_comp_permT_eq_neg (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B} (hT : ∀ d, T (d ∘ σ) = -T d) :
    ofComponents T ∘ₗ permT σ h = -ofComponents T
```

**`Lorentz.ofComponents_comp_permT_eq_self`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L274).

> A family symmetric under reading its index vectors through `σ` gives a map invariant under
> `permT σ`.

```lean
lemma ofComponents_comp_permT_eq_self (σ : Fin n → Fin n)
    (h : IsReindexing (fun _ : Fin n => Color.up) (fun _ => Color.up) σ)
    {T : (Fin n → Fin 1 ⊕ Fin 3) → B} (hT : ∀ d, T (d ∘ σ) = T d) :
    ofComponents T ∘ₗ permT σ h = ofComponents T
```

**`Lorentz.isLorentzCovariant_ofComponents_iff`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean#L283).

> The map of a family is equivariant exactly when the family obeys the transformation law of
> the components of a tensor with `n` four-vector indices.

```lean
lemma isLorentzCovariant_ofComponents_iff {repLorentz : Representation ℂ SL(2,ℂ) B}
    (T : (Fin n → Fin 1 ⊕ Fin 3) → B) :
    IsLorentzCovariant n B repLorentz (ofComponents T) ↔
      ∀ (g : SL(2,ℂ)) l, repLorentz g (T l) = ∑ a : Fin n → Fin 1 ⊕ Fin 3,
        (∏ i, (((SL2C.toLorentzGroup g).1 (a i) (l i) : ℝ) : ℂ)) • T a
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Invariant coefficient tensors on spacetime indices](invariants-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [The colours of complex Lorentz tensors are closed under adjoints](invariants-adjointclosed.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LorentzCovariance.lean)
