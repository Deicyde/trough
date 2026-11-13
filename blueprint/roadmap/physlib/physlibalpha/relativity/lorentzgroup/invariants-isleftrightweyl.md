---
declaration: module
origin: cited
lean: Lorentz.IsLeftRightWeyl, Lorentz.IsDualLeftRightWeyl, Lorentz.eq_zero_of_invariant_leftRight, Lorentz.IsLeftRightWeyl.reducesInvariantsTo_bot, Lorentz.IsLeftRightWeyl.eq_zero_of_invariant, Lorentz.IsDualLeftRightWeyl.reducesInvariantsTo_bot, Lorentz.IsDualLeftRightWeyl.eq_zero_of_invariant
statement: formalized
proof: formalized
---

# Lorentz invariants of a left-handed and a right-handed Weyl index

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.IsLeftRightWeyl`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean): 7 declarations, 7 with a docstring.

## i. Overview

> A bispinor `T^{α α'}`, carrying one left-handed and one right-handed Weyl index, has no Lorentz
> invariant but `0`: the pair carries the `(1/2, 1/2)` representation, a single four-vector index,
> which has nothing to contract with. The same holds for the dual pair `T_{α α'}`. The families are
> equivariant linear maps out of `ℂT[.upL, .upR]` and `ℂT[.downL, .downR]`, `IsLeftRightWeyl` and
> `IsDualLeftRightWeyl` (A).
>
> By `TensorSpecies.IsEquivariant.reducesInvariantsTo_bot` it is enough that the only invariant
> tensor is zero (B). Two diagonal elements of `SL(2,ℂ)` already force this. A diagonal
> `g = diag (λ₀, λ₁)` multiplies the component `(a₁, a₂)` of a tensor of `ℂT[.upL, .upR]` by
> `λ_{a₁} * conj λ_{a₂}`, and that of a tensor of `ℂT[.downL, .downR]` by the inverse of this. The
> boost `diag (2, 2⁻¹)` along `z` scales `(0, 0)` by `4` and `(1, 1)` by `4⁻¹`, so these vanish,
> and the half turn `diag (-i, i)` about `z` multiplies `(0, 1)` and `(1, 0)` by `-1`, so these
> vanish too (C).

## ii. Key results

> - `Lorentz.eq_zero_of_invariant_leftRight` : an invariant tensor with a left- and a
>   right-handed Weyl index is zero.
> - `Lorentz.IsLeftRightWeyl.reducesInvariantsTo_bot` : the invariants of the range of a
>   left-right family reduce to `⊥`.
> - `Lorentz.IsDualLeftRightWeyl.reducesInvariantsTo_bot` : the same for the dual indices.

## iv. References

> * None.

## A. Left-right families as equivariant maps

**`Lorentz.IsLeftRightWeyl`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L62).

> A family with a left- and a right-handed Weyl index `T^{α α'}`: an equivariant linear map
> out of `ℂT[.upL, .upR]`.

```lean
abbrev IsLeftRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.upL, .upR] →ₗ[ℂ] B) : Prop
```

**`Lorentz.IsDualLeftRightWeyl`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L68).

> A family with a dual left- and a dual right-handed Weyl index `T_{α α'}`: an equivariant
> linear map out of `ℂT[.downL, .downR]`.

```lean
abbrev IsDualLeftRightWeyl (B : Type*) [AddCommMonoid B] [Module ℂ B]
    (repLorentz : Representation ℂ SL(2,ℂ) B) (f : ℂT[.downL, .downR] →ₗ[ℂ] B) : Prop
```

## B. The invariant tensors vanish

**`Lorentz.eq_zero_of_invariant_leftRight`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L82).

> An invariant tensor with a left- and a right-handed Weyl index, or with their duals, is
> zero. The inverse boost along `z` scales the two diagonal components by `4⁻¹` and `4`, and the
> inverse half turn about `z` negates the two mixed ones; for the dual colours the inverse
> cancels against the inverse in the matrix of the colour.

```lean
lemma eq_zero_of_invariant_leftRight {k k' : complexLorentzTensor.Color}
    (hk : (k = .upL ∧ k' = .upR) ∨ (k = .downL ∧ k' = .downR)) {t : ℂT[k, k']}
    (ht : ∀ g : SL(2,ℂ), g • t = t) : t = 0
```

## C. The classification of the invariants

**`Lorentz.IsLeftRightWeyl.reducesInvariantsTo_bot`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L122).

> The invariants of the range of a left-right family reduce to `⊥`: a Lorentz invariant of
> `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, lies in `S`.

```lean
lemma IsLeftRightWeyl.reducesInvariantsTo_bot {f : ℂT[.upL, .upR] →ₗ[ℂ] B}
    (hf : IsLeftRightWeyl B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

**`Lorentz.IsLeftRightWeyl.eq_zero_of_invariant`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L129).

> Every Lorentz invariant in the range of a left-right family is zero.

```lean
lemma IsLeftRightWeyl.eq_zero_of_invariant {f : ℂT[.upL, .upR] →ₗ[ℂ] B}
    (hf : IsLeftRightWeyl B repLorentz f) {x : B} (hx : x ∈ LinearMap.range f)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x = 0
```

**`Lorentz.IsDualLeftRightWeyl.reducesInvariantsTo_bot`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L137).

> The invariants of the range of a dual left-right family reduce to `⊥`: a Lorentz invariant
> of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, lies in `S`.

```lean
lemma IsDualLeftRightWeyl.reducesInvariantsTo_bot {f : ℂT[.downL, .downR] →ₗ[ℂ] B}
    (hf : IsDualLeftRightWeyl B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

**`Lorentz.IsDualLeftRightWeyl.eq_zero_of_invariant`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean#L144).

> Every Lorentz invariant in the range of a dual left-right family is zero.

```lean
lemma IsDualLeftRightWeyl.eq_zero_of_invariant {f : ℂT[.downL, .downR] →ₗ[ℂ] B}
    (hf : IsDualLeftRightWeyl B repLorentz f) {x : B} (hx : x ∈ LinearMap.range f)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x = 0
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Lorentz invariants of two Weyl indices of the same kind](invariants-isbileftweyl.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/IsLeftRightWeyl.lean)
