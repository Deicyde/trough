---
declaration: def
origin: cited
lean: TauCeti.GroupScheme.factorisationDual
statement: formalized
---

# TauCeti.GroupScheme.factorisationDual

The factorisation dual of a constant-degree isogeny, characterized by
`comp_factorisationDual`. It is a homomorphism from `B` to `A`.

```lean
TauCeti.GroupScheme.factorisationDual.{u} {S : AlgebraicGeometry.Scheme}
  {A B : CategoryTheory.CommGrp (CategoryTheory.Over S)} (f : A ⟶ B)
  [AlgebraicGeometry.LocallyOfFinitePresentation (CategoryTheory.Over.Hom.left f.hom.hom.hom)]
  {n : ℕ} (hf : TauCeti.GroupScheme.IsogenyOfDegree f.hom n) : B ⟶ A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deligne's theorem (`TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`)](../other-results/delignes-theorem-tauceti-algebraicgeometry-finit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupScheme.factorisationDual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupScheme/Isogeny/FactorisationDual.html#TauCeti.GroupScheme.factorisationDual).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupScheme.factorisationDual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupScheme/Isogeny/FactorisationDual.html#TauCeti.GroupScheme.factorisationDual)
- [Source of `TauCeti.GroupScheme.factorisationDual` in TauCeti/AlgebraicGeometry/GroupScheme/Isogeny/FactorisationDual.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/GroupScheme/Isogeny/FactorisationDual.lean#L83)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
