---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one
statement: formalized
proof: formalized
---

# TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one

A finite free algebra over a Noetherian ring is étale if and only if its fibres over all
primes of height at most one are étale. Minimal primes must be included; no generic étaleness
assumption is imposed.

```lean
TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [CommRing A] [CommRing B] [Algebra A B] [IsNoetherianRing A] [Module.Finite A B]
  [Module.Free A B] :
  Algebra.Etale A B ↔
    ∀ (p : Ideal A) [inst : p.IsPrime], p.height ≤ 1 → Algebra.Etale p.ResidueField (p.Fiber B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The discriminant criterion](the-discriminant-criterion.md)
- [TauCeti.Algebra.etale_iff_traceForm_nondegenerate](tauceti-algebra-etale-iff-traceform-nondegenerat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Purity.html#TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Purity.html#TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one)
- [Source of `TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one` in TauCeti/RingTheory/Etale/Purity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Etale/Purity.lean#L51)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalPurity/STATUS.md)
