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
- [Weyl's theorem as a decomposition](../part-02/weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_leviComplement`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviComplement).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_leviComplement`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviComplement)
- [Source of `TauCeti.exists_leviComplement` in TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean#L139)
