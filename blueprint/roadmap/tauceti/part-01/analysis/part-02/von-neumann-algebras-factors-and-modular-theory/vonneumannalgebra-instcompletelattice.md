---
declaration: instance
origin: cited
lean: VonNeumannAlgebra.instCompleteLattice
statement: formalized
---

# VonNeumannAlgebra.instCompleteLattice

The von Neumann algebras on `H` form a complete lattice: meets are intersections and joins
are generated von Neumann algebras.

```lean
VonNeumannAlgebra.instCompleteLattice.{u_1} {H : Type u_1} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] : CompleteLattice (VonNeumannAlgebra H)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`VonNeumannAlgebra.instCompleteLattice`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Lattice.html#VonNeumannAlgebra.instCompleteLattice).

## Sources

- [Tau Ceti documentation: `VonNeumannAlgebra.instCompleteLattice`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Lattice.html#VonNeumannAlgebra.instCompleteLattice)
- [Source of `VonNeumannAlgebra.instCompleteLattice` in TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean#L78)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
