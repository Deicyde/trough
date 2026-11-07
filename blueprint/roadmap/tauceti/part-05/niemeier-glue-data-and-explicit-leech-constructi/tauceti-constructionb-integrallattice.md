---
declaration: def
origin: cited
lean: TauCeti.ConstructionB.integralLattice
statement: formalized
---

# TauCeti.ConstructionB.integralLattice

**Construction B** of a self-orthogonal binary linear code, as an integral lattice: the
Construction A vectors whose coordinate sum is divisible by four, with the halved dot product.

```lean
TauCeti.ConstructionB.integralLattice.{u_1} {ι : Type u_1} [Fintype ι]
  (C : TauCeti.LinearCode (ZMod 2) ι) (hC : Submodule.IsSelfOrthogonal C) :
  TauCeti.IntegralLattice (ι → ℚ)
```

## Depends on

- [TauCeti.ConstructionA.lattice](../../part-01/algebraic-codes-and-code-lattice-constructions/tauceti-constructiona-lattice.md)
- [TauCeti.IntegralLattice](../../part-04/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionB.integralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Basic.html#TauCeti.ConstructionB.integralLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionB.integralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Basic.html#TauCeti.ConstructionB.integralLattice)
- [Source of `TauCeti.ConstructionB.integralLattice` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Basic.lean#L216)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
