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

Formalized in Tau Ceti as [`TauCeti.isCompact_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/State/Space.html#TauCeti.isCompact_stateSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_stateSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/State/Space.html#TauCeti.isCompact_stateSpace)
- [Source of `TauCeti.isCompact_stateSpace` in TauCeti/Analysis/CStarAlgebra/State/Space.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/State/Space.lean#L209)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
