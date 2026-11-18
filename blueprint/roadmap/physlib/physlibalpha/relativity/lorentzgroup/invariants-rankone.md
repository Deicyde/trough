---
declaration: module
origin: cited
lean: Lorentz.RankOne.Transverse, Lorentz.RankOne.prod_lightConeCoeffInv_eq_zero, Lorentz.RankOne.eq_zero_of_not_transverse, Lorentz.RankOne.not_transverse_all, Lorentz.RankOne.eq_zero_of_isInvariantCoeff, Lorentz.RankOne.eq_zero_of_invariant, Lorentz.RankOne.reducesInvariantsTo_bot
statement: formalized
proof: formalized
---

# Lorentz invariants of a single four-vector index

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.RankOne`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean): 8 declarations (1 instance with no name), 7 with a docstring.

## i. Overview

> A four-vector `T^{μ}` has no Lorentz invariant but `0`. There is nothing to contract it with:
> the metric takes two indices and the Levi-Civita symbol four. For an equivariant map
> `f : ℂT(fun _ : Fin 1 => .up) →ₗ[ℂ] B`, `IsLorentzCovariant 1`, that is `eq_zero_of_invariant`,
> and `reducesInvariantsTo_bot`, the form the Standard Model files use, is the same statement
> modulo a Lorentz-stable submodule `S`.
>
> The invariants of the range of `f` are the images of invariant tensors, so it is enough that an
> invariant coefficient tensor `c` (`Invariants.Basic`) vanishes. Along a spatial axis the four
> light-cone directions carry boost weights `2`, `-2`, `0`, `0`, and an invariant `c` has no
> light-cone component of nonzero weight, which with one index says `c_d = 0` unless `d` is one of
> the two directions transverse to time and to that axis (A). No direction is transverse to all three
> axes, so running the three axes in turn leaves `c = 0` (B). Section C applies this to `f`.

## ii. Key results

> - `eq_zero_of_invariant` : every Lorentz invariant in the range of `f` is zero: one index carry no
>   invariant contraction
> - `reducesInvariantsTo_bot` : the range of `f` reduces to `⊥`: a Lorentz invariant of
>   `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, lies in `S`

## iv. References

> * None.

## A. What one axis leaves

> The boost along the axis `i` scales the light-cone directions `D₀ - Dᵢ`, `D₀ + Dᵢ` and the two
> transverse ones by `t²`, `t⁻²`, `1`, `1`, so their weights are `2`, `-2`, `0`, `0`. An invariant
> `c` has no light-cone component of nonzero weight, so writing `c_d` in the light-cone basis
> leaves only the two weight-zero directions, and their coefficients in `d` vanish unless `d` is
> itself transverse.

**`Lorentz.RankOne.Transverse`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L70).

> A direction transverse to the boost along axis `i`: neither time nor the axis.

```lean
def Transverse (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) : Prop
```

**An instance with no name**, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L73).

```lean
instance (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) : Decidable (Transverse i μ)
```

**`Lorentz.RankOne.prod_lightConeCoeffInv_eq_zero`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L77).

> A non-transverse direction has no weight-zero light-cone coefficient.

```lean
lemma prod_lightConeCoeffInv_eq_zero {i : Fin 3} {d : Fin 1 → Fin 1 ⊕ Fin 3}
    (hd : ¬ Transverse i (d 0)) {κ : Fin 1 → Fin 4}
    (hκ : ∑ s, lightConeWeight (κ s) = 0) :
    ∏ s, lightConeCoeffInv i (d s) (κ s) = 0
```

**`Lorentz.RankOne.eq_zero_of_not_transverse`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L89).

> An invariant coefficient tensor vanishes off the two directions transverse to the axis.

```lean
lemma eq_zero_of_not_transverse {c : (Fin 1 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    (i : Fin 3) {d : Fin 1 → Fin 1 ⊕ Fin 3} (hd : ¬ Transverse i (d 0)) : c d = 0
```

## B. The classification of the Lorentz invariants

> No direction is transverse to all three axes at once, so applying A to the three axes in turn
> leaves no coefficient standing.

**`Lorentz.RankOne.not_transverse_all`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L107).

> No direction is transverse to all three axes at once, a finite check.

```lean
lemma not_transverse_all (μ : Fin 1 ⊕ Fin 3) :
    ¬(Transverse 0 μ ∧ Transverse 1 μ ∧ Transverse 2 μ)
```

**`Lorentz.RankOne.eq_zero_of_isInvariantCoeff`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L113).

> An invariant coefficient tensor is zero.

```lean
lemma eq_zero_of_isInvariantCoeff {c : (Fin 1 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) : c = 0
```

## C. The invariants of an equivariant map

> The invariants of the range of an equivariant map come from invariant tensors, whose coefficient
> tensors are invariant, so section B leaves none of them.

**`Lorentz.RankOne.eq_zero_of_invariant`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L138).

> Every Lorentz invariant in the range of `f` is zero: one index carry no invariant
> contraction.

```lean
lemma eq_zero_of_invariant (hf : IsLorentzCovariant 1 B repLorentz f) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x = 0
```

**`Lorentz.RankOne.reducesInvariantsTo_bot`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean#L144).

> The range of `f` reduces to `⊥`: a Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a
> Lorentz-stable submodule, lies in `S`.

```lean
lemma reducesInvariantsTo_bot (hf : IsLorentzCovariant 1 B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

## Depends on

- [Equivariant maps out of tensors with four-vector indices](invariants-lorentzcovariance.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankOne.lean)
