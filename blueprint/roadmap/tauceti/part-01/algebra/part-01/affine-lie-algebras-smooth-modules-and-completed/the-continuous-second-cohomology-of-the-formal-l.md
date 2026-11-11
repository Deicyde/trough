---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one
statement: formalized
proof: formalized
---

# The continuous second cohomology of the formal loop algebra of a simple Lie algebra is one-dimensional

Here `L` is a finite-dimensional Lie algebra over an algebraically closed field
of characteristic zero whose adjoint module is irreducible and whose Killing form is
nondegenerate, for instance a simple Lie algebra; the residue class of the Killing form spans.

```lean
TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one.{u_4, u_5} (K : Type u_4)
  (L : Type u_5) [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] [IsAlgClosed K] [LieModule.IsIrreducible K L L] :
  Module.finrank K
      (TauCeti.LieModule.Cohomology.continuousSecondCohomology K (TauCeti.currentAlgebra K L)
        (TrivialLieModule K (TauCeti.currentAlgebra K L) K)) =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Continuous second cohomology of formal currents with discrete coefficients](continuous-second-cohomology-of-formal-currents.md)
- [Schur's lemma for Lie modules](../../part-02/lie/part-02/schurs-lemma-for-lie-modules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one)
- [Source of `TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one` in TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean#L552)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
