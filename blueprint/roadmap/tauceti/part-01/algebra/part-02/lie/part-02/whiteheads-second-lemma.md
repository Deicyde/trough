---
declaration: theorem
origin: cited
lean: LieModule.Cohomology.exists_d₁₂_eq, LieModule.Cohomology.twoCocycle_eq_range_d₁₂
statement: formalized
proof: formalized
---

# Whitehead's second lemma

Over a field of characteristic zero, every 2-cocycle of a
Lie algebra with nondegenerate Killing form with values in a finite-dimensional module is a
coboundary.

```lean
LieModule.Cohomology.exists_d₁₂_eq.{u, v, w} {K : Type u} {L : Type v} {M : Type w} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  (c : ↥(LieModule.Cohomology.twoCocycle K L M)) : ∃ f, (LieModule.Cohomology.d₁₂ K L M) f = ↑c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective homomorphism of Lie algebras](../part-01/the-first-isomorphism-theorem-for-a-surjective-h.md)
- [Weyl's theorem as a decomposition](weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`LieModule.Cohomology.exists_d₁₂_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.exists_d%E2%82%81%E2%82%82_eq).

## Other forms

**Whitehead's second lemma, as an equality of submodules.** Formalized in Tau Ceti as [`LieModule.Cohomology.twoCocycle_eq_range_d₁₂`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.twoCocycle_eq_range_d%E2%82%81%E2%82%82).

```lean
LieModule.Cohomology.twoCocycle_eq_range_d₁₂.{u, v, w} {K : Type u} {L : Type v} {M : Type w}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M] :
  LieModule.Cohomology.twoCocycle K L M = (LieModule.Cohomology.d₁₂ K L M).range
```

## Sources

- [Tau Ceti documentation: `LieModule.Cohomology.exists_d₁₂_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.exists_d%E2%82%81%E2%82%82_eq)
- [Source of `LieModule.Cohomology.exists_d₁₂_eq` in TauCeti/Algebra/Lie/Whitehead.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Whitehead.lean#L112)
