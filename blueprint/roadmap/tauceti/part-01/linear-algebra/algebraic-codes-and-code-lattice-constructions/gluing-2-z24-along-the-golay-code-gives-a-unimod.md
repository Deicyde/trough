---
declaration: theorem
origin: cited
lean: TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup
statement: formalized
proof: formalized
---

# Gluing `2 ℤ²⁴` along the Golay code gives a unimodular lattice, because the glue is Lagrangian

```lean
TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup :
  ((TauCeti.ConstructionA.zeroLattice 2 (Fin 24)).ofIsotropicSubgroup ⋯
      (TauCeti.ConstructionA.codeInZeroLatticeDiscriminantGroup 2 (Fin 24)
        (Submodule.toAddSubgroup TauCeti.BinaryGolay.code))
      TauCeti.BinaryGolay.isIsotropic_codeInZeroLatticeDiscriminantQuadraticModule).IsUnimodular
```

## Depends on

- [TauCeti.ConstructionA.lattice](tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [Gluing along a code gives a unimodular lattice exactly when the code is Lagrangian](gluing-along-a-code-gives-a-unimodular-lattice-e.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.html#TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.html#TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup)
- [Source of `TauCeti.BinaryGolay.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Golay.lean#L106)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
