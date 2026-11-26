---
declaration: module
origin: cited
lean: GlobalGaugeGroup.U1.centreEigenspace, GlobalGaugeGroup.U1.mem_centreEigenspace, GlobalGaugeGroup.U1.span_le_centreEigenspace_of_charge, GlobalGaugeGroup.U1.mul_le_centreEigenspace, GlobalGaugeGroup.U1.eq_zero_of_invariant_of_mem_centreEigenspace, GlobalGaugeGroup.U1.mem_of_invariant_of_mem_sup_centreEigenspace
statement: formalized
proof: formalized
---

# The eigenspaces of the elements of `U(1)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.U1.CentreEigenspace`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean): 6 declarations, 6 with a docstring.

> The subspaces on which an element of `U(1)` acts by a scalar, and the families of a given charge.

## i. Overview

> The group `U(1)`, the unit complex numbers `unitary ℂ`, is abelian, so it is its own centre and
> every element `z` plays the part that `-1` plays for `SL(2,ℂ)` and `ω 1` for `SU(N)`.
> `centreEigenspace ρ z ε` names the subspace on which `z` acts by the scalar `ε` (A). A family of
> charge `q`, moved by `u` to `u ^ q` times itself, spans a subspace of the eigenspace of `z` at
> `z ^ q` (B). For a representation on an algebra by algebra maps the scalar of a product is the
> product of the scalars (C), and a vector that the group fixes and that lies in an eigenspace with
> `ε ≠ 1` is zero, also modulo a stable submodule `S` (D).

## ii. Key results

> - `GlobalGaugeGroup.U1.centreEigenspace` : the subspace on which `z` acts by `ε`.
> - `GlobalGaugeGroup.U1.span_le_centreEigenspace_of_charge` : a family of charge `q` lies in the
>   eigenspace of `z` at `z ^ q`.
> - `GlobalGaugeGroup.U1.eq_zero_of_invariant_of_mem_centreEigenspace` : an invariant in an
>   eigenspace with `ε ≠ 1` is zero.
> - `GlobalGaugeGroup.U1.mem_of_invariant_of_mem_sup_centreEigenspace` : the same modulo a stable
>   submodule.

## iv. References

> The same pattern for `SL(2,ℂ)` is
> `PhyslibAlpha.Relativity.LorentzGroup.Invariants.CentreEigenspace`, and for `SU(N)`
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.CentreEigenspace`.

## A. The eigenspaces

**`GlobalGaugeGroup.U1.centreEigenspace`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L63).

> The subspace on which the element `z` of `U(1)` acts by the scalar `ε`.

```lean
def centreEigenspace (ρ : Representation ℂ (unitary ℂ) V) (z : unitary ℂ) (ε : ℂ) :
    Submodule ℂ V
```

**`GlobalGaugeGroup.U1.mem_centreEigenspace`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L68).

> Membership of `centreEigenspace` unfolded: `z` scales the vector by `ε`.

```lean
lemma mem_centreEigenspace {ρ : Representation ℂ (unitary ℂ) V} {z : unitary ℂ} {ε : ℂ}
    {x : V} : x ∈ centreEigenspace ρ z ε ↔ ρ z x = ε • x
```

## B. Families of a given charge

**`GlobalGaugeGroup.U1.span_le_centreEigenspace_of_charge`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L80).

> A family of charge `q`, moved by every `u` to `u ^ q` times itself, spans a subspace of the
> eigenspace of `z` at `z ^ q`.

```lean
lemma span_le_centreEigenspace_of_charge {ρ : Representation ℂ (unitary ℂ) V} {ι : Type*}
    {T : ι → V} {q : ℤ} (hT : ∀ (u : unitary ℂ) (l : ι), ρ u (T l) = ((u : ℂ) ^ q) • T l)
    (z : unitary ℂ) : Submodule.span ℂ (Set.range T) ≤ centreEigenspace ρ z ((z : ℂ) ^ q)
```

## C. Scalars multiply

**`GlobalGaugeGroup.U1.mul_le_centreEigenspace`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L93).

> For a representation by multiplicative maps, the scalar of a product is the product of the
> scalars.

```lean
lemma mul_le_centreEigenspace {A : Type} [Ring A] [Algebra ℂ A]
    {ρ : Representation ℂ (unitary ℂ) A}
    (hmul : ∀ (g : unitary ℂ) (x y : A), ρ g (x * y) = ρ g x * ρ g y) {z : unitary ℂ}
    {W₁ W₂ : Submodule ℂ A} {ε₁ ε₂ : ℂ} (h₁ : W₁ ≤ centreEigenspace ρ z ε₁)
    (h₂ : W₂ ≤ centreEigenspace ρ z ε₂) :
    W₁ * W₂ ≤ centreEigenspace ρ z (ε₁ * ε₂)
```

## D. Invariants in an eigenspace

**`GlobalGaugeGroup.U1.eq_zero_of_invariant_of_mem_centreEigenspace`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L111).

> A vector fixed by `U(1)` that lies in an eigenspace of `z` with `ε ≠ 1` is zero: `z` fixes it
> and scales it by `ε`.

```lean
lemma eq_zero_of_invariant_of_mem_centreEigenspace {ρ : Representation ℂ (unitary ℂ) V}
    {z : unitary ℂ} {ε : ℂ} (hε : ε ≠ 1) {x : V} (hx : x ∈ centreEigenspace ρ z ε)
    (hinv : ∀ u : unitary ℂ, ρ u x = x) : x = 0
```

**`GlobalGaugeGroup.U1.mem_of_invariant_of_mem_sup_centreEigenspace`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean#L120).

> A subspace on which `z` acts by `ε ≠ 1` carries no invariant beyond a stable submodule `S`: an
> invariant of the join with `S` already lies in `S`.

```lean
lemma mem_of_invariant_of_mem_sup_centreEigenspace {ρ : Representation ℂ (unitary ℂ) V}
    {z : unitary ℂ} {ε : ℂ} (hε : ε ≠ 1) {W : Submodule ℂ V}
    (hW : W ≤ centreEigenspace ρ z ε) (S : Submodule ℂ V)
    (hS : ∀ g : unitary ℂ, ∀ y ∈ S, ρ g y ∈ S) {x : V} (hx : x ∈ W ⊔ S)
    (hinv : ∀ g : unitary ℂ, ρ g x = x) : x ∈ S
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Reducing invariants modulo a stable submodule](../../../mathematics/part-01/invariantreduction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/U1/CentreEigenspace.lean)
