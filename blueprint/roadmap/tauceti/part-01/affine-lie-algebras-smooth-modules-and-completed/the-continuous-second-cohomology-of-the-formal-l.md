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

- [TauCeti.LieModule.Cohomology.continuousSecondCohomology](tauceti-liemodule-cohomology-continuoussecondcoh.md)

## Proof depends on

- [TauCeti.LieAlgebra.exists\_eq\_smul\_killingForm](tauceti-liealgebra-exists-eq-smul-killingform.md)
- [Whitehead's first lemma](whiteheads-first-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one)
- [Source of `TauCeti.CurrentAlgebra.finrank_continuousSecondCohomology_eq_one` in TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean#L541)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
