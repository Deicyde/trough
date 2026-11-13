---
declaration: module
origin: cited
lean: Lorentz.Invariants.actMat, Lorentz.Invariants.sum_mul_actMat, Lorentz.Invariants.sum_mul_eq_zero_of_actMat_eq, Lorentz.Invariants.two_zpow_ne_one, Lorentz.Invariants.dagger, Lorentz.Invariants.toLorentzGroup_dagger, Lorentz.Invariants.act, Lorentz.Invariants.act_eq_actMat
statement: formalized
proof: formalized
---

# Invariant coefficient tensors on spacetime indices

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.Basic`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean): 21 declarations, 21 with a docstring.

## i. Overview

> The invariants in the range of an equivariant map out of the complex Lorentz tensors with `n`
> contravariant indices are the images of invariant tensors, and the components of a tensor,
> relabelled by `Fin 1 ⊕ Fin 3` in each slot, are a coefficient tensor on which `SL(2,ℂ)` acts by
> `act` (`Invariants.LorentzCovariance`). This file holds the machinery the rank-specific files use
> to classify the invariant coefficient tensors, `IsInvariantCoeff`.
>
> A matrix `M` acts on coefficient functions by `actMat M`, and a covector that the transposed
> matrix reproduces up to a scalar reads off a component that `actMat M` scales by that scalar, so
> an invariant coefficient function has no such component unless the scalar is `1` (A). Writing
> each slot of a coefficient tensor in the light-cone basis of an axis splits it into pieces that
> a boost scales by powers of its parameter, and an invariant keeps only the piece of weight zero:
> `IsInvariantCoeff.lightConeComponent_eq_zero` (B). Section C records what the half turns about the
> axes and the cyclic rotation of the axes force on an invariant coefficient tensor, for any number
> of slots.
>
> The conjugate transpose `dagger g` of an element of `SL(2,ℂ)`, whose Lorentz matrix is the
> transpose of that of `g`, also lives here; it makes the colours of complex Lorentz tensors closed
> under adjoints (`Invariants.AdjointClosed`).

## ii. Key results

> - `Lorentz.Invariants.IsInvariantCoeff` : invariant coefficient tensors.
> - `Lorentz.Invariants.IsInvariantCoeff.lightConeComponent_eq_zero` : the boost kills the
>   light-cone components of nonzero weight.
> - `Lorentz.Invariants.dagger` : the conjugate transpose in `SL(2,ℂ)`.

## iv. References

> * None.

## A. Coefficient functions moved by a matrix

> A matrix `M` acts on coefficient functions by `actMat M`. The weight argument is generic: a
> covector that the transposed matrix reproduces up to a scalar reads off a component that
> `actMat M` scales by that scalar, so an invariant coefficient function has no such component
> unless the scalar is `1`.

**`Lorentz.Invariants.actMat`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L79).

> The action on coefficient functions of a matrix moving the components:
> `(actMat M c) a = ∑_d c_d M_{a d}`, with `a` free and `d` summed.

```lean
def actMat (M : ι → ι → ℂ) (c : ι → ℂ) (a : ι) : ℂ
```

**`Lorentz.Invariants.sum_mul_actMat`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L83).

> A covector `P` that the transposed matrix reproduces up to a scalar `k` reads off a
> component of the coefficients that `actMat M` scales by `k`.

```lean
lemma sum_mul_actMat (M : ι → ι → ℂ) (P c : ι → ℂ) (k : ℂ)
    (hP : ∀ d, ∑ a, P a * M a d = k * P d) :
    ∑ a, P a * actMat M c a = k * ∑ a, P a * c a
```

**`Lorentz.Invariants.sum_mul_eq_zero_of_actMat_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L94).

> A coefficient function fixed by `actMat M` has no component along a covector that the
> transposed matrix scales by an eigenvalue other than `1`.

```lean
lemma sum_mul_eq_zero_of_actMat_eq (M : ι → ι → ℂ) {P c : ι → ℂ} (hc : actMat M c = c) {k : ℂ}
    (hP : ∀ d, ∑ a, P a * M a d = k * P d) (hk : k ≠ 1) :
    ∑ a, P a * c a = 0
```

**`Lorentz.Invariants.two_zpow_ne_one`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L102).

> The boost with parameter `2` distinguishes every nonzero weight: `2 ^ w ≠ 1` for `w ≠ 0`.

```lean
lemma two_zpow_ne_one {w : ℤ} (hw : w ≠ 0) : ((2 : ℝ) : ℂ) ^ w ≠ 1
```

## B. Coefficient tensors on spacetime indices

**`Lorentz.Invariants.dagger`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L120).

> The conjugate transpose `g†` of an element of `SL(2,ℂ)`, again in `SL(2,ℂ)`.

```lean
def dagger (g : SL(2,ℂ)) : SL(2,ℂ)
```

**`Lorentz.Invariants.toLorentzGroup_dagger`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L124).

> The Lorentz matrix of `g†` is the transpose of that of `g`, so these matrices are closed
> under transposition.

```lean
lemma toLorentzGroup_dagger (g : SL(2,ℂ)) :
    (SL2C.toLorentzGroup (dagger g)).1 = (SL2C.toLorentzGroup g).1ᵀ
```

**`Lorentz.Invariants.act`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L130).

> The action of a real `4 × 4` matrix on coefficient tensors, one factor per slot:
> `(act Λ c) a = ∑_d c_d Λ_{a₀ d₀} ⋯`, with `a` free and `d` summed.

```lean
def act (Λ : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (a : Fin n → Fin 1 ⊕ Fin 3) : ℂ
```

**`Lorentz.Invariants.act_eq_actMat`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L135).

> The action on coefficient tensors is that of the matrix of products, one factor per slot.

```lean
lemma act_eq_actMat (Λ : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) :
    act Λ c = actMat (fun a d => ∏ i, ((Λ (a i) (d i) : ℝ) : ℂ)) c
```

**`Lorentz.Invariants.IsInvariantCoeff`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L140).

> A coefficient tensor fixed by `act` of the Lorentz matrix of every `g : SL(2,ℂ)`.

```lean
def IsInvariantCoeff (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) : Prop
```

**`Lorentz.Invariants.lightConeComponent`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L145).

> A light-cone component of a coefficient tensor along axis `i`: the multi-index `κ` picks
> one light-cone direction per slot and `c` is contracted against that choice.

```lean
def lightConeComponent (i : Fin 3) (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (κ : Fin n → Fin 4) : ℂ
```

**`Lorentz.Invariants.lightConeComponent_act`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L154).

> A light-cone multi-index that `Λ` reproduces up to a scalar `k` has its light-cone
> component scaled by `k`. The hypothesis is the eigenvector equation for the covector
> `∏ₛ lightConeCoeff i (κ s) (·)` under the transposed action, which is the form the light-cone
> directions of an axis satisfy for the transformations diagonal in that basis: the boost along
> the axis, with `k` a power of its parameter, and the half turn about it, with `k` the product
> of the signs of the slots.

```lean
lemma lightConeComponent_act (i : Fin 3) (Λ : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ)
    (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (κ : Fin n → Fin 4) (k : ℂ)
    (hΛ : ∀ d : Fin n → Fin 1 ⊕ Fin 3,
      ∑ a : Fin n → Fin 1 ⊕ Fin 3, (∏ s, lightConeCoeff i (κ s) (a s))
          * ∏ s, ((Λ (a s) (d s) : ℝ) : ℂ)
        = k * ∏ s, lightConeCoeff i (κ s) (d s)) :
    lightConeComponent i (act Λ c) κ = k * lightConeComponent i c κ
```

**`Lorentz.Invariants.toLorentzGroup_boostAxis_symm`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L164).

> The Lorentz matrix of a boost is symmetric.

```lean
lemma toLorentzGroup_boostAxis_symm (i : Fin 3) {t : ℝ} (ht : t ≠ 0) (a b : Fin 1 ⊕ Fin 3) :
    (SL2C.toLorentzGroup (SL2C.boostAxis i t ht)).1 a b
      = (SL2C.toLorentzGroup (SL2C.boostAxis i t ht)).1 b a
```

**`Lorentz.Invariants.IsInvariantCoeff.lightConeComponent_eq_zero`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L172).

> An invariant coefficient tensor has no light-cone component of nonzero weight: the boost at
> `t = 2` would rescale such a component by a factor other than `1`.

```lean
lemma IsInvariantCoeff.lightConeComponent_eq_zero {c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) (i : Fin 3) {κ : Fin n → Fin 4}
    (hκ : ∑ s, lightConeWeight (κ s) ≠ 0) :
    lightConeComponent i c κ = 0
```

**`Lorentz.Invariants.eq_sum_lightConeComponent`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L183).

> A coefficient tensor is recovered from its light-cone components.

```lean
lemma eq_sum_lightConeComponent (i : Fin 3) (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ)
    (d : Fin n → Fin 1 ⊕ Fin 3) :
    c d = ∑ κ, (∏ s, lightConeCoeffInv i (d s) (κ s)) * lightConeComponent i c κ
```

## C. The half turns and the cyclic rotation

> The half turn `SL2C.halfTurn k` has a diagonal Lorentz matrix with the signs `halfTurnSign k`,
> so it multiplies the coefficient at `d` by the product of the signs of the slots of `d`. That
> product is `1` or `-1`, and where it is `-1` invariance forces the coefficient to vanish.
>
> The cyclic rotation `SL2C.rotationCycle` has the permutation matrix of `cycDir`, so it moves
> coefficients rather than rescaling them, and invariance says that a coefficient tensor takes
> the same value at `d` and at `cycIdx d`, the index vector with every slot rotated.

**`Lorentz.Invariants.act_halfTurn`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L207).

> The half turn about the axis `k` multiplies the coefficient at `a` by the product of the
> signs `halfTurnSign k` of the slots of `a`.

```lean
lemma act_halfTurn (k : Fin 3) (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (a : Fin n → Fin 1 ⊕ Fin 3) :
    act (SL2C.toLorentzGroup (SL2C.halfTurn k)).1 c a
      = ((∏ s, halfTurnSign k (a s) : ℤ) : ℂ) * c a
```

**`Lorentz.Invariants.prod_halfTurnSign_eq_one_or`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L224).

> The sign a half turn attaches to a coefficient is `1` or `-1`, being a product of such
> signs.

```lean
lemma prod_halfTurnSign_eq_one_or (k : Fin 3) (d : Fin n → Fin 1 ⊕ Fin 3) :
    ∏ s, halfTurnSign k (d s) = 1 ∨ ∏ s, halfTurnSign k (d s) = -1
```

**`Lorentz.Invariants.IsInvariantCoeff.eq_zero_of_prod_halfTurnSign_ne_one`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L233).

> An invariant coefficient tensor vanishes at every index vector that some half turn
> negates.

```lean
lemma IsInvariantCoeff.eq_zero_of_prod_halfTurnSign_ne_one {c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) {k : Fin 3} {d : Fin n → Fin 1 ⊕ Fin 3}
    (hd : ∏ s, halfTurnSign k (d s) ≠ 1) : c d = 0
```

**`Lorentz.Invariants.cycIdx`**, a def, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L243).

> The relabelling `cycDir`, which fixes time and sends `x → y → z → x`, applied in every
> slot.

```lean
def cycIdx (d : Fin n → Fin 1 ⊕ Fin 3) : Fin n → Fin 1 ⊕ Fin 3
```

**`Lorentz.Invariants.cycIdx_cycIdx_cycIdx`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L246).

> Cycling the axes three times is the identity.

```lean
lemma cycIdx_cycIdx_cycIdx (d : Fin n → Fin 1 ⊕ Fin 3) : cycIdx (cycIdx (cycIdx d)) = d
```

**`Lorentz.Invariants.act_rotationCycle`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L251).

> The cyclic rotation permutes coefficients: the new coefficient at `a` is the old one at `a`
> cycled back.

```lean
lemma act_rotationCycle (c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ) (a : Fin n → Fin 1 ⊕ Fin 3) :
    act (SL2C.toLorentzGroup SL2C.rotationCycle).1 c a = c (cycIdx (cycIdx a))
```

**`Lorentz.Invariants.IsInvariantCoeff.apply_cycIdx`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean#L266).

> An invariant coefficient tensor is constant on the orbits of the cyclic rotation.

```lean
lemma IsInvariantCoeff.apply_cycIdx {c : (Fin n → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    (d : Fin n → Fin 1 ⊕ Fin 3) : c (cycIdx d) = c d
```

## Depends on

- [The light-cone basis of an axis](../lightconederiv.md)
- [The cyclic rotation and the half turns](../sl2c/axisrotations.md)

## Proof depends on

- [Conjugation and the kernel of the covering map](../sl2c/basic.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Basic.lean)
