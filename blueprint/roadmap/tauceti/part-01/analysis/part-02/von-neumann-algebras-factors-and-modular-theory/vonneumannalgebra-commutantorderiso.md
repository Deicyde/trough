---
declaration: def
origin: cited
lean: VonNeumannAlgebra.commutantOrderIso
statement: formalized
---

# VonNeumannAlgebra.commutantOrderIso

Taking commutants is an order-reversing involution of the lattice of von Neumann
algebras.

```lean
VonNeumannAlgebra.commutantOrderIso.{u_1} {H : Type u_1} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] : VonNeumannAlgebra H ≃o (VonNeumannAlgebra H)ᵒᵈ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`VonNeumannAlgebra.commutantOrderIso`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Lattice.html#VonNeumannAlgebra.commutantOrderIso).

## Sources

- [Tau Ceti documentation: `VonNeumannAlgebra.commutantOrderIso`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Lattice.html#VonNeumannAlgebra.commutantOrderIso)
- [Source of `VonNeumannAlgebra.commutantOrderIso` in TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean#L240)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
