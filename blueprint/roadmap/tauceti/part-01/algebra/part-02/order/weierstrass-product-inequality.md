---
declaration: theorem
origin: cited
lean: Multiset.one_sub_prod_map_one_sub_le_sum
statement: formalized
proof: formalized
---

# Weierstrass product inequality

For `t ∈ [0, 1]`, `1 - ∏ (1 - t) ≤ ∑ t`.

```lean
Multiset.one_sub_prod_map_one_sub_le_sum.{u_1} {R : Type u_1} [CommRing R] [LinearOrder R]
  [IsStrictOrderedRing R] {s : Multiset R} (h₀ : ∀ t ∈ s, 0 ≤ t) (h₁ : ∀ t ∈ s, t ≤ 1) :
  1 - (Multiset.map (fun t => 1 - t) s).prod ≤ s.sum
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Multiset.one_sub_prod_map_one_sub_le_sum`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Ring/Multiset.html#Multiset.one_sub_prod_map_one_sub_le_sum).

## Sources

- [Tau Ceti documentation: `Multiset.one_sub_prod_map_one_sub_le_sum`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Ring/Multiset.html#Multiset.one_sub_prod_map_one_sub_le_sum)
- [Source of `Multiset.one_sub_prod_map_one_sub_le_sum` in TauCeti/Algebra/Order/BigOperators/Ring/Multiset.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Order/BigOperators/Ring/Multiset.lean#L34)
