---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.NonabelianH1.equivSheafH
statement: formalized
---

# CategoryTheory.Sheaf.NonabelianH1.equivSheafH

The classes of torsors under an abelian sheaf `F` are in bijection with the sheaf cohomology
`H¹(F)` (Stacks, Lemma 21.4.3 (03AJ)). The bijection is characterised by
`equivSheafH_connecting`: for every short exact sequence `0 → F → B → Q → 0`, the class of the
torsor of lifts of a global section of `Q` goes to its image under the connecting map
`δ : H⁰(Q) → H¹(F)`; in particular it does not depend on the injective embedding of `F` used to
construct it.

```lean
CategoryTheory.Sheaf.NonabelianH1.equivSheafH.{w', w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] {J : CategoryTheory.GrothendieckTopology C}
  [CategoryTheory.HasSheafify J AddCommGrpCat]
  [CategoryTheory.HasExt (CategoryTheory.Sheaf J AddCommGrpCat)]
  [J.WEqualsLocallyBijective AddCommGrpCat]
  [CategoryTheory.EnoughInjectives (CategoryTheory.Sheaf J AddCommGrpCat)]
  (F : CategoryTheory.Sheaf J AddCommGrpCat) :
  ((CategoryTheory.abelianSheafToGrpSheaf J).obj F).NonabelianH1 ≃ F.H 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.NonabelianH1.equivSheafH`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/NonabelianCohomology/SheafH.html#CategoryTheory.Sheaf.NonabelianH1.equivSheafH).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.NonabelianH1.equivSheafH`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/NonabelianCohomology/SheafH.html#CategoryTheory.Sheaf.NonabelianH1.equivSheafH)
- [Source of `CategoryTheory.Sheaf.NonabelianH1.equivSheafH` in TauCeti/CategoryTheory/Sites/NonabelianCohomology/SheafH.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Sites/NonabelianCohomology/SheafH.lean#L196)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
