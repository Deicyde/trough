---
declaration: theorem
origin: cited
lean: TauCeti.exists_leviComplement
statement: formalized
proof: formalized
---

# Levi's theorem

Over a field of characteristic zero, the solvable radical of a
finite-dimensional Lie algebra has a complementary Lie subalgebra, a Levi complement.

```lean
TauCeti.exists_leviComplement.{u, v} (K : Type u) [Field K] (L : Type v) [LieRing L]
  [LieAlgebra K L] [CharZero K] [FiniteDimensional K L] :
  ∃ S, IsCompl (↑(LieAlgebra.radical K L)) S.toSubmodule
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective homomorphism of Lie algebras](the-first-isomorphism-theorem-for-a-surjective-h.md)
- [Weyl's theorem as a decomposition](../representation-theory/part-02/weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_leviComplement`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviComplement).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_leviComplement`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviComplement)
- [Source of `TauCeti.exists_leviComplement` in TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean#L139)
