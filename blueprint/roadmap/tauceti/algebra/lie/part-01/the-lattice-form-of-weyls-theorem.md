---
declaration: theorem
origin: cited
lean: TauCeti.complementedLattice_lieSubmodule_of_isKilling
statement: formalized
proof: formalized
---

# The lattice form of Weyl's theorem

the Lie submodules of a finite-dimensional module over
a Lie algebra with nondegenerate Killing form form a complemented lattice.

```lean
TauCeti.complementedLattice_lieSubmodule_of_isKilling.{u, v, w} (K : Type u) (L : Type v) [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  (M : Type w) [AddCommGroup M] [_root_.Module K M] [LieRingModule L M] [LieModule K L M]
  [FiniteDimensional K M] : ComplementedLattice (LieSubmodule K L M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's complete reducibility theorem](../part-02/weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.complementedLattice_lieSubmodule_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.complementedLattice_lieSubmodule_of_isKilling).

## Sources

- [Tau Ceti documentation: `TauCeti.complementedLattice_lieSubmodule_of_isKilling`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.html#TauCeti.complementedLattice_lieSubmodule_of_isKilling)
- [Source of `TauCeti.complementedLattice_lieSubmodule_of_isKilling` in TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CompleteReducibility.lean#L265)
