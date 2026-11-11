---
declaration: def
origin: cited
lean: TauCeti.Algebra.WeilRestriction.mapBialgHom
statement: formalized
---

# Functoriality of the Weil restriction of affine group schemes

A bialgebra map
`φ : H₁ →ₐc[B] H₂`, that is, a homomorphism `Spec H₂ → Spec H₁` of affine monoid (for Hopf
algebras, group) schemes over `Spec B`, induces a bialgebra map of Weil restrictions, with
underlying algebra map `WeilRestriction.map A B φ`. On points it is precomposition with `φ`, see
`WeilRestriction.pointsMulEquiv_mapDomain_mapBialgHom`.

```lean
TauCeti.Algebra.WeilRestriction.mapBialgHom.{u_1, u_2, u_4, u_5} (A : Type u_1) (B : Type u_2)
  [CommRing A] [CommRing B] [Algebra A B] [Module.Finite A B] [Module.Projective A B]
  {H₁ : Type u_4} {H₂ : Type u_5} [CommRing H₁] [CommRing H₂] [Bialgebra B H₁] [Bialgebra B H₂]
  [Algebra.FinitePresentation B H₁] [Algebra.FinitePresentation B H₂] (φ : H₁ →ₐc[B] H₂) :
  TauCeti.Algebra.WeilRestriction A B H₁ →ₐc[A] TauCeti.Algebra.WeilRestriction A B H₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.WeilRestriction.mapBialgHom`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.mapBialgHom).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.WeilRestriction.mapBialgHom`](https://taucetiproject.org/docs/TauCeti/Algebra/HopfAlgebra/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.mapBialgHom)
- [Source of `TauCeti.Algebra.WeilRestriction.mapBialgHom` in TauCeti/Algebra/HopfAlgebra/WeilRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/HopfAlgebra/WeilRestriction.lean#L269)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
