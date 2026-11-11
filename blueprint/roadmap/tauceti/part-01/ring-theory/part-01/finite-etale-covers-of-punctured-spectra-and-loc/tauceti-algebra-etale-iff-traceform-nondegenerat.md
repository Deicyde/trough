---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_iff_traceForm_nondegenerate
statement: formalized
proof: formalized
---

# TauCeti.Algebra.etale_iff_traceForm_nondegenerate

An algebra over a field is étale iff its trace form is nondegenerate. The fibre case in the
proof of Stacks, Lemma 49.3.1 (0BJF).

```lean
TauCeti.Algebra.etale_iff_traceForm_nondegenerate.{u_1, u_2} (K : Type u_1) (B : Type u_2) [Field K]
  [CommRing B] [Algebra K B] : Algebra.Etale K B ↔ (Algebra.traceForm K B).Nondegenerate
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_iff_traceForm_nondegenerate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_traceForm_nondegenerate).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_iff_traceForm_nondegenerate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_traceForm_nondegenerate)
- [Source of `TauCeti.Algebra.etale_iff_traceForm_nondegenerate` in TauCeti/RingTheory/Etale/Discriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Etale/Discriminant.lean#L62)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalPurity/STATUS.md)
