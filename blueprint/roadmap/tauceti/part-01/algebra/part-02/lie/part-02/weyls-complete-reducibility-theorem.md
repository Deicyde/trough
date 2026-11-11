---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCompl_of_isKilling
statement: formalized
proof: formalized
---

# Weyl's complete reducibility theorem

Over a field of characteristic zero, every Lie
submodule of a finite-dimensional module over a Lie algebra with nondegenerate Killing form has a
complement, so the module is a direct sum of irreducibles.

The `sl₂` case, `TauCeti.exists_isCompl_of_toLieSubalgebra_eq_top`, is the rank-one instance of
the same argument, run with the concrete Casimir operator of an `sl₂` triple.

```lean
TauCeti.exists_isCompl_of_isKilling.{u, v, w} {K : Type u} {L : Type v} [Field K] [CharZero K]
  [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] {M : Type w} [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  (N : LieSubmodule K L M) : ∃ N', IsCompl N N'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCompl_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.exists_isCompl_of_isKilling).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCompl_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.exists_isCompl_of_isKilling)
- [Source of `TauCeti.exists_isCompl_of_isKilling` in TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean#L256)
