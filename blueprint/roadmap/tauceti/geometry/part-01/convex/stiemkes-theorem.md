---
declaration: theorem
origin: cited
lean: Submodule.exists_pos_dotProduct_eq_zero_iff
statement: formalized
proof: formalized
---

# Stiemke's theorem

A subspace `S` of `ι → K` contains no nonzero nonnegative vector
exactly when some vector with strictly positive coordinates is orthogonal to all of `S`.

```lean
Submodule.exists_pos_dotProduct_eq_zero_iff.{u_4, u_5} {ι : Type u_4} {K : Type u_5} [Fintype ι]
  [Field K] [LinearOrder K] [IsStrictOrderedRing K] (S : Submodule K (ι → K)) :
  (∃ c, (∀ (i : ι), 0 < c i) ∧ ∀ x ∈ S, c ⬝ᵥ x = 0) ↔ ∀ x ∈ S, 0 ≤ x → x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's theorem](gordans-theorem.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_pos_dotProduct_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#Submodule.exists_pos_dotProduct_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `Submodule.exists_pos_dotProduct_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#Submodule.exists_pos_dotProduct_eq_zero_iff)
- [Source of `Submodule.exists_pos_dotProduct_eq_zero_iff` in TauCeti/Geometry/Convex/Cone/Alternative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Convex/Cone/Alternative.lean#L184)
