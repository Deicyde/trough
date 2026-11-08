---
declaration: theorem
origin: cited
lean: LieModule.Cohomology.twoCocycle_eq_range_d₁₂, LieModule.Cohomology.exists_d₁₂_eq
statement: formalized
proof: formalized
---

# Whitehead's second lemma, as an equality of submodules

the 2-cocycles of a
Lie algebra with nondegenerate Killing form in characteristic zero, with values in a
finite-dimensional module, are exactly the coboundaries.

```lean
LieModule.Cohomology.twoCocycle_eq_range_d₁₂.{u, v, w} {K : Type u} {L : Type v} {M : Type w}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M] :
  LieModule.Cohomology.twoCocycle K L M = (LieModule.Cohomology.d₁₂ K L M).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective homomorphism of Lie algebras](../lie/the-first-isomorphism-theorem-for-a-surjective-h.md)
- [Weyl's theorem as a decomposition](../representation-theory/part-02/weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`LieModule.Cohomology.twoCocycle_eq_range_d₁₂`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.twoCocycle_eq_range_d%E2%82%81%E2%82%82).

## Other forms

**Whitehead's second lemma.** Formalized in Tau Ceti as [`LieModule.Cohomology.exists_d₁₂_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.exists_d%E2%82%81%E2%82%82_eq).

```lean
LieModule.Cohomology.exists_d₁₂_eq.{u, v, w} {K : Type u} {L : Type v} {M : Type w} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  (c : ↥(LieModule.Cohomology.twoCocycle K L M)) : ∃ f, (LieModule.Cohomology.d₁₂ K L M) f = ↑c
```

## Sources

- [Tau Ceti documentation: `LieModule.Cohomology.twoCocycle_eq_range_d₁₂`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.twoCocycle_eq_range_d%E2%82%81%E2%82%82)
- [Source of `LieModule.Cohomology.twoCocycle_eq_range_d₁₂` in TauCeti/Algebra/Lie/Whitehead.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Whitehead.lean#L141)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
