---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.NonabelianH1.map
statement: formalized
---

# CategoryTheory.Sheaf.NonabelianH1.map

The map `H¹(G) → H¹(G')` induced by a morphism `φ : G ⟶ G'` of sheaves of groups, sending
the class of a `G`-torsor `P` to the class of the contracted product `P ×^G G'`.

```lean
CategoryTheory.Sheaf.NonabelianH1.map.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  {J : CategoryTheory.GrothendieckTopology C} {G G' : CategoryTheory.Sheaf J GrpCat}
  [CategoryTheory.HasWeakSheafify J (Type w)] [J.WEqualsLocallyBijective (Type w)] (φ : G ⟶ G') :
  G.NonabelianH1 → G'.NonabelianH1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.NonabelianH1.map`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/NonabelianCohomology/Map.html#CategoryTheory.Sheaf.NonabelianH1.map).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.NonabelianH1.map`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/NonabelianCohomology/Map.html#CategoryTheory.Sheaf.NonabelianH1.map)
- [Source of `CategoryTheory.Sheaf.NonabelianH1.map` in TauCeti/CategoryTheory/Sites/NonabelianCohomology/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Sites/NonabelianCohomology/Map.lean#L223)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
