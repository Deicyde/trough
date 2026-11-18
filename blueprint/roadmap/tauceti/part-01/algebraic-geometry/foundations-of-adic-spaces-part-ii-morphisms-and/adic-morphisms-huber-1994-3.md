---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.IsAdic
statement: formalized
---

# Adic morphisms (Huber 1994, §3)

a morphism `f : X ⟶ Y` of adic spaces is *adic* when
every point `x` of `X` has an open neighbourhood `U`, mapped by `f` into an open `V` of `Y`,
together with Huber pairs `(A, A⁺)` and `(B, B⁺)`, `B` complete and Hausdorff with `Spa(B, B⁺)`
having a sheaf as structure presheaf, a morphism `φ : (A, A⁺) → (B, B⁺)` whose ring homomorphism
is adic, and isomorphisms identifying `X` restricted to `U` with `Spa(B, B⁺)` and `Y` restricted
to `V` with `Spa(A, A⁺)`, under which `f` becomes the morphism induced by `φ`; that is, `f` is
chart-locally adic (`TauCeti.PreAdicSpace.chartLocally`). By
`isAdic_iff_mapsTo_analyticPoints` these are the morphisms sending analytic points to analytic
points.

```lean
TauCeti.AdicSpace.IsAdic.{u} : CategoryTheory.MorphismProperty TauCeti.AdicSpace
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.IsAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.IsAdic).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.IsAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.html#TauCeti.AdicSpace.IsAdic)
- [Source of `TauCeti.AdicSpace.IsAdic` in TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/Adic.lean#L79)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
