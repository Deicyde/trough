---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType
statement: formalized
---

# Morphisms locally of +weakly finite type (Huber 1996, Definition 1.2.1(ii))

a morphism
`f : X ⟶ Y` of adic spaces is *locally of +weakly finite type* when every point `x` of `X` has an
open neighbourhood `U`, mapped by `f` into an open `V` of `Y`, together with Huber pairs `(A, A⁺)`
and `(B, B⁺)`, `B` complete and Hausdorff with `Spa(B, B⁺)` having a sheaf as structure presheaf,
a morphism `φ : (A, A⁺) → (B, B⁺)` of +weakly finite type, and isomorphisms identifying `X`
restricted to `U` with `Spa(B, B⁺)` and `Y` restricted to `V` with `Spa(A, A⁺)`, under which `f`
becomes the morphism induced by `φ`; that is, `f` is chart-locally of +weakly finite type
(`TauCeti.PreAdicSpace.chartLocally`).

```lean
TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType.{u} :
  CategoryTheory.MorphismProperty TauCeti.AdicSpace
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/PlusWeaklyFiniteType.html#TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/PlusWeaklyFiniteType.html#TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType)
- [Source of `TauCeti.AdicSpace.LocallyOfPlusWeaklyFiniteType` in TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/PlusWeaklyFiniteType.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Morphisms/PlusWeaklyFiniteType.lean#L75)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
