---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition
statement: formalized
---

# A positive definite lattice is `I_k` plus a lattice without vectors of norm one

The
standard lattice `I_k` is carried onto the unit-norm sublattice, with `k` its rank, and the second
summand is the complement `unitNormComplement L`.

```lean
TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  ((TauCeti.IntegralLattice.unitLattice (Fin (Module.finrank ℤ ↥L.unitNormSubmodule))).orthogonalSum
        L.unitNormComplement).Isometry
    L
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/UnitNormSplitting.html#TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/UnitNormSplitting.html#TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition)
- [Source of `TauCeti.IntegralLattice.IsPosDef.unitNormDecomposition` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/UnitNormSplitting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/UnitNormSplitting.lean#L352)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
