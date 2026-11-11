---
declaration: theorem
origin: cited
lean: TauCeti.periodicCyclicCohomology.isIso_ι_of_isZero_hochschildCohomology
statement: formalized
proof: formalized
---

# Stabilization of periodic cyclic cohomology

For a unital algebra whose Hochschild
cohomology `HH^m(A, Hom_R(A, M))` vanishes in all degrees `m > n + 2k`, the canonical map
`H^(n+2k)(Tot) → HP^n` is an isomorphism.

```lean
TauCeti.periodicCyclicCohomology.isIso_ι_of_isZero_hochschildCohomology.{u, v, u_1} {R : Type u_1}
  {A : Type u} {M : Type v} [CommRing R] [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M]
  {n k : ℕ}
  (h :
    ∀ (m : ℕ),
      n + 2 * k < m → CategoryTheory.Limits.IsZero (TauCeti.hochschildCohomology R A M m)) :
  CategoryTheory.IsIso (TauCeti.periodicCyclicCohomology.ι R A M n k)
```

## Depends on

- [Periodic cyclic cohomology `HP^n(A; M)`](periodic-cyclic-cohomology-hp-n-a-m.md)

## Proof depends on

- [Exactness of `H^m(Tot) → H^(m+2)(Tot) → HH^(m+2)`](exactness-of-h-m-tot-h-m-2-tot-hh-m-2.md)
- [Exactness of `HH^(m+1) → H^m(Tot) → H^(m+2)(Tot)`](exactness-of-hh-m-1-h-m-tot-h-m-2-tot.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.periodicCyclicCohomology.isIso_ι_of_isZero_hochschildCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology.isIso_%CE%B9_of_isZero_hochschildCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.periodicCyclicCohomology.isIso_ι_of_isZero_hochschildCohomology`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.html#TauCeti.periodicCyclicCohomology.isIso_%CE%B9_of_isZero_hochschildCohomology)
- [Source of `TauCeti.periodicCyclicCohomology.isIso_ι_of_isZero_hochschildCohomology` in TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/PeriodicCohomology.lean#L300)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
