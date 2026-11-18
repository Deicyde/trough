---
declaration: module
origin: cited
lean: Lorentz.lightConeSign, Lorentz.sum_halfTurn_lightConeCoeff, Lorentz.sum_prod_halfTurn_lightConeCoeff, Lorentz.prod_lightConeSign_of_sum_lightConeWeight_eq_zero, Lorentz.RankThree.lightConeComponent_act_halfTurn, Lorentz.RankThree.lightConeComponent_eq_zero_of_weight_zero, Lorentz.RankThree.eq_zero_of_isInvariantCoeff, Lorentz.RankThree.eq_zero_of_invariant
statement: formalized
proof: formalized
---

# Lorentz invariants of three four-vector indices

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.RankThree`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean): 9 declarations, 9 with a docstring.

## i. Overview

> A rank-three tensor `T^{μνρ}` has no Lorentz invariant but `0`. Nothing ties three indices:
> the metric takes two and the Levi-Civita symbol four, and an odd number is left over either way.
> For an equivariant map `f : ℂT(fun _ : Fin 3 => .up) →ₗ[ℂ] B`, `IsLorentzCovariant 3`, that is
> `eq_zero_of_invariant`, and `reducesInvariantsTo_bot`, the form the Standard Model files use, is
> the same statement modulo a Lorentz-stable submodule `S`.
>
> The invariants of the range of `f` are the images of invariant tensors, so it is enough that an
> invariant coefficient tensor `c` (`Invariants.Basic`) vanishes. One axis then does all the work,
> with a parity argument in place of a certificate. Along a spatial axis the four light-cone
> directions carry boost weights `2`, `-2`, `0`, `0`, and an invariant `c` has no light-cone component
> of nonzero weight. In a multi-index of total weight `0` the `+2` and `-2` slots pair off, leaving an
> odd number of the three slots transverse. The half turn about the axis, the rotation by `π`, fixes
> time and the axis and negates the two transverse directions (A), so it multiplies each weight-zero
> component by `-1` to an odd power, that is by `-1`, and an invariant component both fixed and
> negated is `0` (B). Every light-cone component of `c` vanishes, so `c` does, and with it the
> invariant. Section C applies this to `f`.

## ii. Key results

> - `eq_zero_of_invariant` : every Lorentz invariant in the range of `f` is zero: three indices carry
>   no invariant contraction
> - `reducesInvariantsTo_bot` : the range of `f` reduces to `⊥`: a Lorentz invariant of
>   `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, lies in `S`

## iv. References

> * None.

## A. The half turn about a spatial axis

> The half turn about the axis `i` is the rotation by `π` about it, `SL2C.halfTurn i` from
> `SL2C.AxisRotations`. Its Lorentz matrix is diagonal, fixing time and the axis and negating
> the two transverse directions, so on the light-cone directions of that axis it is `1` on the
> two of weight `±2` and `-1` on the two transverse ones (`lightConeSign`).

**`Lorentz.lightConeSign`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L71).

> The sign the half turn about an axis gives each light-cone direction of that axis: `1` on
> the two of weight `±2`, `-1` on the two transverse ones.

```lean
def lightConeSign (κ : Fin 4) : ℤ
```

**`Lorentz.sum_halfTurn_lightConeCoeff`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L75).

> The half turn about the axis `i` acts on each light-cone direction along that axis
> by its sign.

```lean
lemma sum_halfTurn_lightConeCoeff (i : Fin 3) (κ : Fin 4) (ν : Fin 1 ⊕ Fin 3) :
    ∑ μ : Fin 1 ⊕ Fin 3, lightConeCoeff i κ μ *
        (((SL2C.toLorentzGroup (SL2C.halfTurn i)).1 ν μ : ℝ) : ℂ)
      = ((lightConeSign κ : ℤ) : ℂ) * lightConeCoeff i κ ν
```

**`Lorentz.sum_prod_halfTurn_lightConeCoeff`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L89).

> The scalar behind the action of the half turn on a light-cone multi-index: the half
> turn acts slot by slot, so the product of the per-slot signs factors out.

```lean
lemma sum_prod_halfTurn_lightConeCoeff (i : Fin 3) {n : ℕ} (c : Fin n → Fin 4)
    (a : Fin n → Fin 1 ⊕ Fin 3) :
    ∑ d : Fin n → Fin 1 ⊕ Fin 3, (∏ j, lightConeCoeff i (c j) (d j)) *
        (∏ j, (((SL2C.toLorentzGroup (SL2C.halfTurn i)).1 (a j) (d j) : ℝ) : ℂ))
      = ((∏ j, lightConeSign (c j) : ℤ) : ℂ) * ∏ j, lightConeCoeff i (c j) (a j)
```

**`Lorentz.prod_lightConeSign_of_sum_lightConeWeight_eq_zero`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L112).

> A light-cone multi-index of three slots and total boost weight zero has an odd
> number of transverse slots, so the half turn acts on it by `-1`.

```lean
lemma prod_lightConeSign_of_sum_lightConeWeight_eq_zero (c : Fin 3 → Fin 4)
    (hc : (∑ j, lightConeWeight (c j)) = 0) : ∏ j, lightConeSign (c j) = -1
```

## B. The classification of the Lorentz invariants

> Writing a coefficient tensor in the light-cone basis of one axis leaves only the multi-indices
> of total weight zero, the others being killed by the boost. The half turn about that axis
> negates exactly those, so they vanish too and nothing is left.

**`Lorentz.RankThree.lightConeComponent_act_halfTurn`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L133).

> The half turn multiplies a light-cone component by the product of the signs of its slots.

```lean
lemma lightConeComponent_act_halfTurn {n : ℕ} (i : Fin 3)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (κ : Fin n → Fin 4) :
    lightConeComponent i (act (SL2C.toLorentzGroup (SL2C.halfTurn i)).1 c) κ
      = ((∏ s, lightConeSign (κ s) : ℤ) : ℂ) * lightConeComponent i c κ
```

**`Lorentz.RankThree.lightConeComponent_eq_zero_of_weight_zero`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L143).

> An invariant coefficient tensor has no weight-zero light-cone component either, the half
> turn negating those.

```lean
lemma lightConeComponent_eq_zero_of_weight_zero {c : (Fin 3 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) (i : Fin 3) {κ : Fin 3 → Fin 4}
    (hκ : ∑ s, lightConeWeight (κ s) = 0) : lightConeComponent i c κ = 0
```

**`Lorentz.RankThree.eq_zero_of_isInvariantCoeff`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L152).

> An invariant coefficient tensor is zero: no light-cone component of it survives.

```lean
lemma eq_zero_of_isInvariantCoeff {c : (Fin 3 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) : c = 0
```

## C. The invariants of an equivariant map

> The invariants of the range of an equivariant map come from invariant tensors, whose coefficient
> tensors are invariant, so section B leaves none of them.

**`Lorentz.RankThree.eq_zero_of_invariant`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L175).

> Every Lorentz invariant in the range of `f` is zero: three indices carry no invariant
> contraction.

```lean
lemma eq_zero_of_invariant (hf : IsLorentzCovariant 3 B repLorentz f) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x = 0
```

**`Lorentz.RankThree.reducesInvariantsTo_bot`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean#L181).

> The range of `f` reduces to `⊥`: a Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a
> Lorentz-stable submodule, lies in `S`.

```lean
lemma reducesInvariantsTo_bot (hf : IsLorentzCovariant 3 B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

## Depends on

- [Equivariant maps out of tensors with four-vector indices](invariants-lorentzcovariance.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankThree.lean)
