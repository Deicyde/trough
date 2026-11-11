---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_stateSpace
statement: formalized
proof: formalized
---

# Weak-* compactness of the state space

For unital `A`, the state space is weak-* compact,
by the Banach–Alaoglu theorem.

```lean
TauCeti.isCompact_stateSpace.{u_1} {A : Type u_1} [CStarAlgebra A] [PartialOrder A]
  [StarOrderedRing A] : IsCompact (TauCeti.stateSpace A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/StateSpace.html#TauCeti.isCompact_stateSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/StateSpace.html#TauCeti.isCompact_stateSpace)
- [Source of `TauCeti.isCompact_stateSpace` in TauCeti/Analysis/CStarAlgebra/StateSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/StateSpace.lean#L209)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
