---
declaration: def
origin: cited
lean: TauCeti.dgRepresentableHomIso, TauCeti.dgRepresentableHomEquiv
statement: formalized
---

# The DG Yoneda lemma

evaluation at the identity of `X` is an isomorphism from the Hom
complex of right DG modules `Hom(Hom(-, X), F)` to the complex `F(X)`.

```lean
TauCeti.dgRepresentableHomIso.{v} (R : Type v) [CommRing R] {C : Type v} [TauCeti.DGCategory R C]
  (X : C)
  (F :
    CategoryTheory.EnrichedFunctor (CochainComplex (ModuleCat R) ℤ) Cᵒᵖ
      (CochainComplex (ModuleCat R) ℤ)) :
  TauCeti.dgHomComplex R { toEnrichedFunctor := TauCeti.dgRepresentable R X }
      { toEnrichedFunctor := F } ≅
    F.obj (Opposite.op X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgRepresentableHomIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Yoneda.html#TauCeti.dgRepresentableHomIso).

## Other forms

**The DG Yoneda lemma, degreewise.** Formalized in Tau Ceti as [`TauCeti.dgRepresentableHomEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Yoneda.html#TauCeti.dgRepresentableHomEquiv).

```lean
TauCeti.dgRepresentableHomEquiv.{v} (R : Type v) [CommRing R] {C : Type v} [TauCeti.DGCategory R C]
  (X : C)
  (F :
    CategoryTheory.EnrichedFunctor (CochainComplex (ModuleCat R) ℤ) Cᵒᵖ
      (CochainComplex (ModuleCat R) ℤ))
  (n : ℤ) :
  TauCeti.DGHom R n { toEnrichedFunctor := TauCeti.dgRepresentable R X }
      { toEnrichedFunctor := F } ≃ₗ[R]
    ↑((F.obj (Opposite.op X)).X n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.dgRepresentableHomIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Yoneda.html#TauCeti.dgRepresentableHomIso)
- [Source of `TauCeti.dgRepresentableHomIso` in TauCeti/CategoryTheory/DG/Yoneda.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/DG/Yoneda.lean#L356)
