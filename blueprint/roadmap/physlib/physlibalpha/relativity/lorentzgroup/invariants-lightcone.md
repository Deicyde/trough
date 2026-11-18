---
declaration: module
origin: cited
lean: Lorentz.Invariants.lightConeCoeffZ, Lorentz.Invariants.coe_lightConeCoeffZ, Lorentz.Invariants.lightConeCoeffInvZ, Lorentz.Invariants.coe_lightConeCoeffInvZ_eq_two_mul, Lorentz.Invariants.InBoostPlane, Lorentz.Invariants.lightConeCoeffInvZ_eq_zero_of_inBoostPlane, Lorentz.Invariants.lightConeCoeffInvZ_eq_zero_of_not_inBoostPlane, Lorentz.Invariants.slotZ
statement: formalized
proof: formalized
---

# The light-cone basis of a boost axis over the integers

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.LightCone`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean): 12 declarations (1 instance with no name), 11 with a docstring.

## i. Overview

> `lightConeCoeff` and `lightConeCoeffInv` of `LightConeDeriv` change a spacetime index into the
> light-cone basis of a spatial axis `i`: the two directions `D₀ - Dᵢ` and `D₀ + Dᵢ` of the plane
> the boost along `i` moves, and the two transverse directions. Their entries are `0`, `±1` and
> `±1/2`, so both matrices have integer mirrors, and the rank-four classification computes with
> them in the kernel, which evaluates `ℤ` and does not evaluate `ℂ`. This file holds the mirrors
> and what is proved about them at an arbitrary number of indices.
>
> The change of basis one way is `lightConeCoeffZ`, an exact integer copy. The other way needs
> the halves, and `lightConeCoeffInvZ` clears them, so it is twice the true inverse and a
> contraction over `n` slots carries a factor `2 ^ n` that the rank-four file divides out. That
> is the only normalization in play, and `coe_lightConeCoeffInvZ_eq_two_mul` records it against
> `ℂ`.
>
> `InBoostPlane` separates the two directions of weight `±2` from the two transverse ones, one
> index at a time. `slotZ` is one slot of the change of basis, and `transitionZ` composes it over
> `n` slots into `2 ^ n` times the map keeping the light-cone components of total weight `m`;
> `transitionZ_eq_sum` unfolds that recursion into a single sum over the multi-indices of that
> weight.

## ii. Key results

> - `lightConeCoeffZ` : the four light-cone directions of axis `i`, as integers
> - `lightConeCoeffInvZ` : twice the coordinate directions in the light-cone basis, the `2` clearing
>   the halves
> - `coe_lightConeCoeffInvZ_eq_two_mul` : the integer copy is exactly twice `lightConeCoeffInv`
> - `InBoostPlane` : the boost plane of axis `i`: time and the axis, the two directions the boost
>   moves
> - `slotZ` : one slot's factor: twice the coefficient of `κ` in `μ`, times that of `ν` in `κ`
> - `transitionZ` : two to the number of slots times the entry, at `d` and `e`, of the map keeping the
>   light-cone components of total weight `m` along axis `i`; the factor is the one
>   `lightConeCoeffInvZ` carries, one per slot
> - `transitionZ_eq_sum` : the recursion unfolded, as a sum over the multi-indices of total weight `m`

## iv. References

> * None.

## A. The change of basis over the integers

**`Lorentz.Invariants.lightConeCoeffZ`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L75).

> The four light-cone directions of axis `i`, as integers.

```lean
def lightConeCoeffZ (i : Fin 3) (κ : Fin 4) (μ : Fin 1 ⊕ Fin 3) : ℤ
```

**`Lorentz.Invariants.coe_lightConeCoeffZ`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L82).

> The integer copy casts to `lightConeCoeff`.

```lean
lemma coe_lightConeCoeffZ (i : Fin 3) (κ : Fin 4) (μ : Fin 1 ⊕ Fin 3) :
    ((lightConeCoeffZ i κ μ : ℤ) : ℂ) = lightConeCoeff i κ μ
```

**`Lorentz.Invariants.lightConeCoeffInvZ`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L88).

> Twice the coordinate directions in the light-cone basis, the `2` clearing the halves.

```lean
def lightConeCoeffInvZ (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) (κ : Fin 4) : ℤ
```

**`Lorentz.Invariants.coe_lightConeCoeffInvZ_eq_two_mul`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L95).

> The integer copy is exactly twice `lightConeCoeffInv`.

```lean
lemma coe_lightConeCoeffInvZ_eq_two_mul (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) (κ : Fin 4) :
    ((lightConeCoeffInvZ i μ κ : ℤ) : ℂ) = 2 * lightConeCoeffInv i μ κ
```

## B. The boost plane

> The boost along axis `i` moves time and the axis and fixes the two transverse directions, so
> the light-cone directions of weight `±2` are supported in the first pair and the two of weight
> `0` in the second. Either half of that statement kills half of `lightConeCoeffInvZ`.

**`Lorentz.Invariants.InBoostPlane`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L111).

> The boost plane of axis `i`: time and the axis, the two directions the boost moves.

```lean
def InBoostPlane (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) : Prop
```

**An instance with no name**, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L113).

```lean
instance (i : Fin 3) (μ : Fin 1 ⊕ Fin 3) : Decidable (InBoostPlane i μ)
```

**`Lorentz.Invariants.lightConeCoeffInvZ_eq_zero_of_inBoostPlane`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L117).

> A direction in the boost plane has no transverse light-cone components.

```lean
lemma lightConeCoeffInvZ_eq_zero_of_inBoostPlane {i : Fin 3} {μ : Fin 1 ⊕ Fin 3}
    (hμ : InBoostPlane i μ) {κ : Fin 4} (hκ : κ = 2 ∨ κ = 3) :
    lightConeCoeffInvZ i μ κ = 0
```

**`Lorentz.Invariants.lightConeCoeffInvZ_eq_zero_of_not_inBoostPlane`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L123).

> A transverse direction has no light-cone components in the boost plane.

```lean
lemma lightConeCoeffInvZ_eq_zero_of_not_inBoostPlane {i : Fin 3} {μ : Fin 1 ⊕ Fin 3}
    (hμ : ¬InBoostPlane i μ) {κ : Fin 4} (hκ : κ = 0 ∨ κ = 1) :
    lightConeCoeffInvZ i μ κ = 0
```

## C. The weight-keeping transition over any number of slots

> One slot of the change of basis, keeping the four directions apart, is `slotZ`, and composing it
> over `n` slots while tracking the weight left to distribute gives `transitionZ`. The recursion
> follows B: a slot whose direction lies in the boost plane takes weight `2` or `-2` and leaves
> `m - 2` or `m + 2`, and a transverse slot takes either direction of weight `0`, which is why
> those two are added, and leaves `m`.
>
> Unfolding the recursion into a single sum splits into two independent steps. The case split of
> the recursion is the boost-plane support argument of B and nothing else: once it is resolved,
> one slot is a plain sum over the four directions, each taking its own weight out of `m`
> (`transitionZ_succ`). What is left has no light-cone content at all, the peeling of the first
> slot off a weight-constrained sum over tuples, which is `Physlib.Fin.sum_filter_weight_succ`.
> `transitionZ_eq_sum` is the induction that composes them.

**`Lorentz.Invariants.slotZ`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L149).

> One slot's factor: twice the coefficient of `κ` in `μ`, times that of `ν` in `κ`.

```lean
def slotZ (i : Fin 3) (κ : Fin 4) (μ ν : Fin 1 ⊕ Fin 3) : ℤ
```

**`Lorentz.Invariants.transitionZ`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L156).

> Two to the number of slots times the entry, at `d` and `e`, of the map keeping the light-cone
> components of total weight `m` along axis `i`; the factor is the one `lightConeCoeffInvZ`
> carries, one per slot. A slot of `d` in the boost plane takes weight `2` or `-2`, leaving
> `m - 2` or `m + 2`; a transverse slot takes weight `0` and leaves `m`.

```lean
def transitionZ (i : Fin 3) : {n : ℕ} → (d e : Fin n → Fin 1 ⊕ Fin 3) → ℤ → ℤ
```

**`Lorentz.Invariants.transitionZ_succ`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L169).

> One slot of the transition, with the case split of the recursion resolved: the first slot
> runs over all four light-cone directions, each taking its own weight out of `m`. The two
> directions of the boost plane drop out of a transverse slot and the two transverse ones drop
> out of a slot in the boost plane, which is what the two branches of `transitionZ` record.

```lean
lemma transitionZ_succ (i : Fin 3) {n : ℕ} (d e : Fin (n + 1) → Fin 1 ⊕ Fin 3) (m : ℤ) :
    transitionZ i d e m
      = ∑ κ : Fin 4, slotZ i κ (d 0) (e 0)
          * transitionZ i (Fin.tail d) (Fin.tail e) (m - lightConeWeight κ)
```

**`Lorentz.Invariants.transitionZ_eq_sum`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean#L185).

> The recursion unfolded, as a sum over the multi-indices of total weight `m`.

```lean
lemma transitionZ_eq_sum (i : Fin 3) :
    ∀ {n : ℕ} (d e : Fin n → Fin 1 ⊕ Fin 3) (m : ℤ),
    transitionZ i d e m
      = ∑ κ ∈ Finset.univ.filter
          (fun κ : Fin n → Fin 4 => (∑ s, lightConeWeight (κ s)) = m),
        ∏ s, slotZ i (κ s) (d s) (e s)
```

## Depends on

- [The light-cone basis of an axis](../lightconederiv.md)

## Proof depends on

- [Peeling the first slot off a sum over tuples](../../mathematics/part-02/formathlib/fin.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/LightCone.lean)
