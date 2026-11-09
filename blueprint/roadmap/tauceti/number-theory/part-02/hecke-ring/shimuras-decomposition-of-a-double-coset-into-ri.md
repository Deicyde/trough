---
declaration: theorem
origin: cited
lean: DoubleCoset.doubleCoset_eq_iUnion_rightCosets, DoubleCoset.doubleCoset_eq_iUnion_rightCosetRep
statement: formalized
proof: formalized
---

# Shimura's decomposition of a double coset into right cosets

`Γ₁gΓ₂` is the union of the
right cosets `Γ₁ · (g τᵥ⁻¹)`, where `τᵥ` runs over representatives of `Γ₂ ⧸ (Γ₂ ∩ g⁻¹Γ₁g)` — the
mirror of `DoubleCoset.doubleCoset_eq_iUnion_leftCosets`, and of Mathlib's
`doubleCoset_union_rightCoset`, which is indexed by all of `Γ₂` and so repeats each coset.

The inverse on `τᵥ` is what converts the *left*-coset quotient `Γ₂ ⧸ (Γ₂ ∩ g⁻¹Γ₁g)` into an index
for the right cosets: `Γ₁ g τ = Γ₁ g τ'` exactly when `τ'τ⁻¹ ∈ Γ₂ ∩ g⁻¹Γ₁g`.

It lives here rather than beside `doubleCoset_eq_iUnion_leftCosets` because it is phrased with
`DecompQuotient`, which this file defines.

```lean
DoubleCoset.doubleCoset_eq_iUnion_rightCosets.{u_1} {G : Type u_1} [Group G] (Γ₁ Γ₂ : Subgroup G)
  (g : G) :
  DoubleCoset.doubleCoset g ↑Γ₁ ↑Γ₂ = ⋃ v, MulOpposite.op (g * (↑(Quotient.out v))⁻¹) • ↑Γ₁
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DoubleCoset.doubleCoset_eq_iUnion_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Basic.html#DoubleCoset.doubleCoset_eq_iUnion_rightCosets).

## Other forms

**Shimura's decomposition of the double coset, in the `rightCosetRep` spelling.** Formalized in Tau Ceti as [`DoubleCoset.doubleCoset_eq_iUnion_rightCosetRep`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Basic.html#DoubleCoset.doubleCoset_eq_iUnion_rightCosetRep).

```lean
DoubleCoset.doubleCoset_eq_iUnion_rightCosetRep.{u_1} {G : Type u_1} [Group G] {Δ : Submonoid G}
  {Γ₁ Γ₂ : Subgroup G} (D : HeckeCoset Δ Γ₁ Γ₂) :
  DoubleCoset.doubleCoset ↑(Quotient.out D) ↑Γ₁ ↑Γ₂ =
    ⋃ v, MulOpposite.op (DoubleCoset.rightCosetRep D v) • ↑Γ₁
```

## Sources

- [Tau Ceti documentation: `DoubleCoset.doubleCoset_eq_iUnion_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Basic.html#DoubleCoset.doubleCoset_eq_iUnion_rightCosets)
- [Source of `DoubleCoset.doubleCoset_eq_iUnion_rightCosets` in TauCeti/NumberTheory/HeckeRing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/HeckeRing/Basic.lean#L577)
