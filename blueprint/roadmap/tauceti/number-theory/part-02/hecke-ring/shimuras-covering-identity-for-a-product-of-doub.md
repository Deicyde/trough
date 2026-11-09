---
declaration: theorem
origin: cited
lean: DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets
statement: formalized
proof: formalized
---

# Shimura's covering identity for a product of double cosets (§3.4)

If `Γ₁ δ₁ Γ₂` is the
union of the right cosets `Γ₁ aᵢ` and `Γ₂ δ₂ Γ₃` is the union of the right cosets `Γ₂ bⱼ`, then
the pointwise product `Γ₁ δ₁ Γ₂ · Γ₂ δ₂ Γ₃` is the union of the right cosets `Γ₁ aᵢ bⱼ`.

The two double cosets splice because `Γ₂ Γ₂ = Γ₂`: an element of the product is `u v` with
`u ∈ Γ₁ δ₁ Γ₂` and `v ∈ Γ₂ δ₂ Γ₃`; writing `v = g bⱼ` with `g ∈ Γ₂` moves `g` into `u`, and `u g`
is again in `Γ₁ δ₁ Γ₂`, hence in some `Γ₁ aᵢ`.

⚠ The union is **not** disjoint, and the family `(i, j) ↦ Γ₁ aᵢ bⱼ` is in general far from
injective. Any repetitions here are right-coset collisions; this theorem neither counts them nor
identifies them with `DoubleCoset.multiplicity`, which uses left-coset representatives. The
identity supplies coverage only, exactly as
`doubleCoset_eq_iUnion_rightCosets_of_forall_exists` does for a single double coset.

```lean
DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets.{u_1, u_2, u_3} {G : Type u_1}
  [Group G] {Γ₁ Γ₂ Γ₃ : Subgroup G} {δ₁ δ₂ : G} {ι : Type u_2} {κ : Type u_3} (a : ι → G)
  (b : κ → G) (hcover₁ : DoubleCoset.doubleCoset δ₁ ↑Γ₁ ↑Γ₂ = ⋃ i, MulOpposite.op (a i) • ↑Γ₁)
  (hcover₂ : DoubleCoset.doubleCoset δ₂ ↑Γ₂ ↑Γ₃ = ⋃ j, MulOpposite.op (b j) • ↑Γ₂) :
  DoubleCoset.doubleCoset δ₁ ↑Γ₁ ↑Γ₂ * DoubleCoset.doubleCoset δ₂ ↑Γ₂ ↑Γ₃ =
    ⋃ p, MulOpposite.op (a p.1 * b p.2) • ↑Γ₁
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Basic.html#DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets).

## Sources

- [Tau Ceti documentation: `DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/Basic.html#DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets)
- [Source of `DoubleCoset.doubleCoset_mul_doubleCoset_eq_iUnion_rightCosets` in TauCeti/NumberTheory/HeckeRing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/HeckeRing/Basic.lean#L637)
