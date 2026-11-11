---
declaration: def
origin: cited
lean: TauCeti.SpinPolarizationData.kostantSpinLieRingModule
statement: formalized
---

# The spinor module of Kostant's theorem

The Fock module of a polarization of the Killing
form, acted on by `L` through `TauCeti.SpinPolarizationData.kostantSpinRep`. Scoped, like Kostant's
module `CliffordAlgebra.kostantLieRingModule`: the exterior algebra of a subspace of `L` is not
otherwise an `L`-module.

```lean
TauCeti.SpinPolarizationData.kostantSpinLieRingModule.{u, v} {K : Type u} [Field K] {L : Type v}
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L]
  (P : TauCeti.SpinPolarizationData (TauCeti.LieAlgebra.killingQuadraticForm K L)) :
  LieRingModule L (ExteriorAlgebra K ↥P.W)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.kostantSpinLieRingModule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinLieRingModule).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.kostantSpinLieRingModule`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinLieRingModule)
- [Source of `TauCeti.SpinPolarizationData.kostantSpinLieRingModule` in TauCeti/RepresentationTheory/Spin/Kostant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Kostant.lean#L95)
