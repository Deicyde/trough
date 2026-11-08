---
declaration: theorem
origin: cited
lean: TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff
statement: formalized
proof: formalized
---

# Gluing along a code gives a unimodular lattice exactly when the code is Lagrangian

For an
even modulus and a quadratically isotropic code `C`, the overlattice of the zero-code lattice
`m ℤ^ι` glued along the discriminant subgroup of `C` is unimodular exactly when `C` equals its
orthogonal complement in the coordinate alphabet `(ℤ/m)^ι`.

```lean
TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff.{u_1}
  (m : ℕ) [NeZero m] (ι : Type u_1) [Fintype ι] (hm : Even m) (C : TauCeti.AdditiveCode (ZMod m) ι)
  (hC : ((TauCeti.FiniteQuadraticModule.zmodStandard m hm).coordinatePower ι).IsIsotropic C) :
  ((TauCeti.ConstructionA.zeroLattice m ι).ofIsotropicSubgroup ⋯
        (TauCeti.ConstructionA.codeInZeroLatticeDiscriminantGroup m ι C) ⋯).IsUnimodular ↔
    ((TauCeti.FiniteBilinearModule.zmodStandard m).coordinatePower ι).IsLagrangian C
```

## Depends on

- [TauCeti.ConstructionA.lattice](tauceti-constructiona-lattice.md)
- [TauCeti.FiniteQuadraticModule](../integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [Even overlattices correspond to quadratic-isotropic subgroups](../integral-lattices-discriminant-forms-and-overlat/even-overlattices-correspond-to-quadratic-isotro.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Quadratic.html#TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Quadratic.html#TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff)
- [Source of `TauCeti.ConstructionA.isUnimodular_ofIsotropicSubgroup_codeInZeroLatticeDiscriminantGroup_iff` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Quadratic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/Quadratic.lean#L116)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AlgebraicCodingTheory/STATUS.md)
