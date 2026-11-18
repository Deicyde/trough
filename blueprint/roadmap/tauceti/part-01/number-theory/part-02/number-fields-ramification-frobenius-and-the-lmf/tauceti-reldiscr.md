---
declaration: def
origin: cited
lean: TauCeti.relDiscr
statement: formalized
---

# TauCeti.relDiscr

The relative discriminant ideal of the finite torsion-free extension `A → B`.

```lean
TauCeti.relDiscr.{u_3, u_4} (A : Type u_3) (B : Type u_4) [CommRing A] [IsDedekindDomain A]
  [CommRing B] [IsDedekindDomain B] [Algebra A B] [Module.Finite A B] [Module.IsTorsionFree A B] :
  Ideal A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.relDiscr`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Discriminant/Basic.html#TauCeti.relDiscr).

## Sources

- [Tau Ceti documentation: `TauCeti.relDiscr`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Discriminant/Basic.html#TauCeti.relDiscr)
- [Source of `TauCeti.relDiscr` in TauCeti/RingTheory/DedekindDomain/Discriminant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DedekindDomain/Discriminant/Basic.lean#L32)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/NumberFieldArithmetic/STATUS.md)
