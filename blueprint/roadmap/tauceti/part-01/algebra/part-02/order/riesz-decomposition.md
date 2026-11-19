---
declaration: theorem
origin: cited
lean: TauCeti.HasRieszInterpolation.exists_decomposition
statement: formalized
proof: formalized
---

# Riesz decomposition

under interpolation, `0 ≤ g ≤ a + b` with `0 ≤ a` and `0 ≤ b`
splits as `g = g₁ + g₂` with `0 ≤ g₁ ≤ a` and `0 ≤ g₂ ≤ b`.

```lean
TauCeti.HasRieszInterpolation.exists_decomposition.{u_1} {G : Type u_1} [AddCommGroup G]
  [Preorder G] [IsOrderedAddMonoid G] (h : TauCeti.HasRieszInterpolation G) {a b g : G} (ha : 0 ≤ a)
  (hb : 0 ≤ b) (hg : 0 ≤ g) (hgab : g ≤ a + b) :
  ∃ g₁ g₂, 0 ≤ g₁ ∧ g₁ ≤ a ∧ 0 ≤ g₂ ∧ g₂ ≤ b ∧ g₁ + g₂ = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasRieszInterpolation.exists_decomposition`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/Group/DimensionGroup.html#TauCeti.HasRieszInterpolation.exists_decomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.HasRieszInterpolation.exists_decomposition`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/Group/DimensionGroup.html#TauCeti.HasRieszInterpolation.exists_decomposition)
- [Source of `TauCeti.HasRieszInterpolation.exists_decomposition` in TauCeti/Algebra/Order/Group/DimensionGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Order/Group/DimensionGroup.lean#L130)
