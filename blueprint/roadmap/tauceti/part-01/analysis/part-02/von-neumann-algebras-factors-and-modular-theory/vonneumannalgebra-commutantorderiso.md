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
- [Source of `VonNeumannAlgebra.commutantOrderIso` in TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/VonNeumannAlgebra/Lattice.lean#L240)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
