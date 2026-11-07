---
declaration: theorem
origin: cited
lean: TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup
statement: formalized
proof: formalized
---

# TauCeti.BinaryGolay.isUnimodular\_ofIsotropicSubgroup\_codeInZeroLatticeDiscriminantGroup

**Gluing `2 ℤ²⁴` along the Golay code gives a unimodular lattice**, because the glue is
Lagrangian.

```lean
TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup :
  ((TauCeti.ConstructionA.zeroLattice 2 (Fin 24)).ofIsotropicSubgroup ⋯
      (TauCeti.ConstructionA.codeInZeroLatticeDiscriminantGroup 2 (Fin 24)
        (Submodule.toAddSubgroup TauCeti.BinaryGolay.code))
      TauCeti.BinaryGolay.isIsotropic_codeInZeroLatticeDiscriminantQuadraticModule).IsUnimodular
```

## Depends on

- [TauCeti.ConstructionA.lattice](tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../part-04/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../../part-04/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../part-04/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [Gluing along a code gives a unimodular lattice exactly when the code is Lagrangian](gluing-along-a-code-gives-a-unimodular-lattice-e.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.html#TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.html#TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup)
- [Source of `TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.lean#L106)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AlgebraicCodingTheory/STATUS.md)
