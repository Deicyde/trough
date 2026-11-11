---
declaration: theorem
origin: cited
lean: TauCeti.MonoidalQuotient.instMonoidalLinear
statement: formalized
proof: formalized
---

# TauCeti.MonoidalQuotient.instMonoidalLinear

The quotient of a monoidal `S`-linear category by a tensor ideal is monoidal `S`-linear.

```lean
TauCeti.MonoidalQuotient.instMonoidalLinear.{v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  (I : TauCeti.MonoidalIdeal C) (S : Type u_1) [Semiring S] [CategoryTheory.Linear S C]
  [CategoryTheory.MonoidalLinear S C] : CategoryTheory.MonoidalLinear S (TauCeti.MonoidalQuotient I)
```

## Depends on

- [TauCeti.MonoidalIdeal](tauceti-monoidalideal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MonoidalQuotient.instMonoidalLinear`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.html#TauCeti.MonoidalQuotient.instMonoidalLinear).

## Sources

- [Tau Ceti documentation: `TauCeti.MonoidalQuotient.instMonoidalLinear`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.html#TauCeti.MonoidalQuotient.instMonoidalLinear)
- [Source of `TauCeti.MonoidalQuotient.instMonoidalLinear` in TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Envelope/Quotient/Basic.lean#L180)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
