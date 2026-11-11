---
declaration: abbrev
origin: cited
lean: TauCeti.AInfinityCategory.PositiveHochschild.complex
statement: formalized
---

# TauCeti.AInfinityCategory.PositiveHochschild.complex

The positive-arity suspended Hochschild complex of an A-infinity category.

```lean
TauCeti.AInfinityCategory.PositiveHochschild.complex.{u, v, w} {R : Type w} [CommRing R]
  {C : Type u} [TauCeti.GradedLinearQuiver R C] (𝒞 : TauCeti.AInfinityCategory R C) :
  CochainComplex (ModuleCat R) ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hochschild differential squares to zero](the-hochschild-differential-squares-to-zero.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityCategory.PositiveHochschild.complex`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Hochschild/Basic.html#TauCeti.AInfinityCategory.PositiveHochschild.complex).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityCategory.PositiveHochschild.complex`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Hochschild/Basic.html#TauCeti.AInfinityCategory.PositiveHochschild.complex)
- [Source of `TauCeti.AInfinityCategory.PositiveHochschild.complex` in TauCeti/CategoryTheory/AInfinity/Hochschild/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/AInfinity/Hochschild/Basic.lean#L129)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
