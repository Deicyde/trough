---
declaration: theorem
origin: cited
lean: TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII
statement: formalized
proof: formalized
---

# Over `ℤ/2^r` with `r ≥ 1`, a self-orthogonal code has an even unimodular Construction A lattice exactly when it is a Type II code

```lean
TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII.{u_1} {ι : Type u_1}
  [Fintype ι] {r : ℕ} (hr : r ≠ 0) (C : TauCeti.AdditiveCode (ZMod (2 ^ r)) ι)
  (hC :
    (AddSubgroup.toZModSubmodule (2 ^ r)) C ≤
      ((AddSubgroup.toZModSubmodule (2 ^ r)) C).euclideanDual) :
  (TauCeti.ConstructionA.integralLattice (2 ^ r) C hC).IsEven ∧
      (TauCeti.ConstructionA.integralLattice (2 ^ r) C hC).IsUnimodular ↔
    TauCeti.TwoPowCode.IsTypeII r C
```

## Depends on

- [TauCeti.ConstructionA.lattice](tauceti-constructiona-lattice.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Even.html#TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Even.html#TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII)
- [Source of `TauCeti.ConstructionA.isEven_and_isUnimodular_integralLattice_iff_isTypeII` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Even.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Even.lean#L195)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
