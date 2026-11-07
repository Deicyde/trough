---
declaration: def
origin: cited
lean: TauCeti.ContinuousKaehlerDifferential.substEquiv
statement: formalized
---

# Formal coordinate changes act invertibly on one-forms

For a formal coordinate `φ`,
substitution `f dX ↦ f (φ) dφ` into continuous one-forms, as an equivalence that is semilinear
over the substitution automorphism `TauCeti.LaurentSeries.substAlgEquiv φ` of `K⸨X⸩`. Its inverse
is substitution of the compositional inverse `φ⁻¹`.

```lean
TauCeti.ContinuousKaehlerDifferential.substEquiv.{u_1} {K : Type u_1} [Field K]
  (φ : TauCeti.FormalCoordinate K) :
  TauCeti.ContinuousKaehlerDifferential K ≃ₛₗ[↑(TauCeti.LaurentSeries.substAlgEquiv φ).toRingEquiv]
    TauCeti.ContinuousKaehlerDifferential K
```

## Depends on

- [TauCeti.FormalCoordinate](tauceti-formalcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousKaehlerDifferential.substEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/KaehlerDifferential/Basic.html#TauCeti.ContinuousKaehlerDifferential.substEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousKaehlerDifferential.substEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/KaehlerDifferential/Basic.html#TauCeti.ContinuousKaehlerDifferential.substEquiv)
- [Source of `TauCeti.ContinuousKaehlerDifferential.substEquiv` in TauCeti/RingTheory/LaurentSeries/KaehlerDifferential/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/KaehlerDifferential/Basic.lean#L385)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
