---
declaration: def
origin: cited
lean: TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry
statement: formalized
---

# The discriminant bilinear module of a Construction A lattice is `C⊥ / C`

For a
self-orthogonal additive code `C` over `ℤ/m`, the discriminant bilinear module of `P_m(C)` is the
orthogonal quotient of `C` in the coordinate alphabet `(ℤ/m)^ι`.

```lean
TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry.{u_1} (m : ℕ) [NeZero m]
  (ι : Type u_1) [Fintype ι] (C : TauCeti.AdditiveCode (ZMod m) ι)
  (hC : (AddSubgroup.toZModSubmodule m) C ≤ ((AddSubgroup.toZModSubmodule m) C).euclideanDual) :
  (TauCeti.ConstructionA.integralLattice m C hC).discriminantBilinearModule.Isometry
    (((TauCeti.FiniteBilinearModule.zmodStandard m).coordinatePower ι).orthogonalQuotient C)
```

## Depends on

- [TauCeti.ConstructionA.lattice](tauceti-constructiona-lattice.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/OrthogonalQuotient.html#TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry).

## Sources

- [Tau Ceti documentation: `TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/OrthogonalQuotient.html#TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry)
- [Source of `TauCeti.ConstructionA.discriminantBilinearOrthogonalQuotientIsometry` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/OrthogonalQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/ConstructionA/Code/OrthogonalQuotient.lean#L76)
- [Tau Ceti roadmap status: Algebraic codes and code-lattice constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AlgebraicCodingTheory/STATUS.md)
