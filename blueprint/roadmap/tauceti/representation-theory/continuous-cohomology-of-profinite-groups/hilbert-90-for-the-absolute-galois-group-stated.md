---
declaration: theorem
origin: cited
lean: TauCeti.hilbert90
statement: formalized
proof: formalized
---

# Hilbert 90 for the absolute Galois group, stated for Mathlib's canonical continuous cohomology

`H¹(G_K, (Kˢ)ˣ) = 0` (NSW (6.2.1)). This is the form in which the vanishing feeds
the canonical all-degree theory, where it makes the Kummer map `Kˣ → H¹(G_K, μₙ)` surjective for
`n` positive and invertible in `K`.

```lean
TauCeti.hilbert90.{u_1} (K : Type u_1) [Field K] :
  CategoryTheory.Limits.IsZero
    (continuousCohomology 1
      (TauCeti.ofDiscreteModule ℤ (TauCeti.AbsoluteGaloisGroup K) (TauCeti.UnitsCoeff K)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbert90`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.html#TauCeti.hilbert90).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbert90`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.html#TauCeti.hilbert90)
- [Source of `TauCeti.hilbert90` in TauCeti/FieldTheory/GaloisCohomology/Hilbert90.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/Hilbert90.lean#L263)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
