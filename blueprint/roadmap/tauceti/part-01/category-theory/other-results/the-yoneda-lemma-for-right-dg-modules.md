---
declaration: def
origin: cited
lean: TauCeti.dgYonedaEquiv
statement: formalized
---

# The Yoneda lemma for right DG modules

DG natural transformations `Hom(-, X) ⟶ F` are the
closed degree-zero elements of `F(X)`.  A transformation goes to the image of the identity of `X`
under its component at `X` (`TauCeti.dgYonedaEquiv_apply_coe`), and a closed element `x` goes to
the transformation sending `g : Y ⟶ X` to `F(g)(x)` (`TauCeti.dgApp_dgYonedaEquiv_symm_v`).

```lean
TauCeti.dgYonedaEquiv.{v, u} {R : Type v} [CommRing R] {C : Type u} [TauCeti.DGCategory R C] (X : C)
  (F :
    CategoryTheory.EnrichedFunctor (CochainComplex (ModuleCat R) ℤ) Cᵒᵖ
      (CochainComplex (ModuleCat R) ℤ)) :
  TauCeti.DGNatTrans (TauCeti.dgRepresentable R X) F ≃
    ↥(ModuleCat.Hom.hom ((F.obj (Opposite.op X)).d 0 1)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgYonedaEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Representable.html#TauCeti.dgYonedaEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.dgYonedaEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Representable.html#TauCeti.dgYonedaEquiv)
- [Source of `TauCeti.dgYonedaEquiv` in TauCeti/CategoryTheory/DG/Representable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/DG/Representable.lean#L432)
