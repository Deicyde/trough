---
declaration: theorem
origin: cited
lean: TauCeti.SpinPolarizationData.kostantSpinRep_isotypic
statement: formalized
proof: formalized
---

# Kostant's isotypy theorem for the spinor module

Any two irreducible Lie submodules of the
spinor module of a polarization of the Killing form are isomorphic.

```lean
TauCeti.SpinPolarizationData.kostantSpinRep_isotypic.{u, v} {K : Type u} [Field K] {L : Type v}
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L]
  (P : TauCeti.SpinPolarizationData (TauCeti.LieAlgebra.killingQuadraticForm K L)) [CharZero K]
  [IsAlgClosed K] : LieModule.IsIsotypic K L (ExteriorAlgebra K ↥P.W)
```

## Depends on

- [The spinor module of Kostant's theorem](the-spinor-module-of-kostants-theorem.md)

## Proof depends on

- [The lattice form of Weyl's theorem](../../algebra/part-02/lie/part-01/the-lattice-form-of-weyls-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.kostantSpinRep_isotypic`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_isotypic).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.kostantSpinRep_isotypic`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_isotypic)
- [Source of `TauCeti.SpinPolarizationData.kostantSpinRep_isotypic` in TauCeti/RepresentationTheory/Spin/Kostant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Kostant.lean#L201)
