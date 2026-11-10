---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_iff_traceForm_nondegenerate
statement: formalized
proof: formalized
---

# TauCeti.Algebra.etale_iff_traceForm_nondegenerate

A finite-dimensional algebra over a field is étale iff its trace form is nondegenerate. The
fibre case in the proof of Stacks, Lemma 49.3.1 (0BJF).

```lean
TauCeti.Algebra.etale_iff_traceForm_nondegenerate.{u_1, u_2} (K : Type u_1) (B : Type u_2) [Field K]
  [CommRing B] [Algebra K B] [FiniteDimensional K B] :
  Algebra.Etale K B ↔ (Algebra.traceForm K B).Nondegenerate
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_iff_traceForm_nondegenerate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_traceForm_nondegenerate).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_iff_traceForm_nondegenerate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_traceForm_nondegenerate)
- [Source of `TauCeti.Algebra.etale_iff_traceForm_nondegenerate` in TauCeti/RingTheory/Etale/Discriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Etale/Discriminant.lean#L62)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/LocalPurity/STATUS.md)
