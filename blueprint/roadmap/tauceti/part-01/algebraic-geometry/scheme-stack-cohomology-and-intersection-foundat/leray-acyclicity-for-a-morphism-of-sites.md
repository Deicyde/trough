---
declaration: theorem
origin: cited
lean: CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective
statement: formalized
proof: formalized
---

# Leray acyclicity for a morphism of sites

For a morphism of sites given by `u : C ⥤ D`,
with pushforward `f_* = u.sheafPushforwardContinuous` and exact inverse image
`f⁻¹ = u.sheafPullback`, if an abelian sheaf `F` on `D` has no higher direct images,
`Rᵠ f_* F = 0` for `q > 0`, then the edge map `Hⁿ(C, f_* F) ⟶ Hⁿ(D, F)` is bijective in every
degree (Stacks, Lemma 21.14.6 (0733)).

```lean
CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective.{w, w₁, w₂, v_1, u_1, v_2, u_2}
  {C : Type u_1} [CategoryTheory.Category.{v_1, u_1} C] {J : CategoryTheory.GrothendieckTopology C}
  {D : Type u_2} [CategoryTheory.Category.{v_2, u_2} D] {K : CategoryTheory.GrothendieckTopology D}
  [CategoryTheory.HasSheafify J AddCommGrpCat] [CategoryTheory.HasSheafify K AddCommGrpCat]
  [CategoryTheory.HasExt (CategoryTheory.Sheaf J AddCommGrpCat)]
  [CategoryTheory.HasExt (CategoryTheory.Sheaf K AddCommGrpCat)] (u : CategoryTheory.Functor C D)
  [u.IsContinuous J K] [(u.sheafPushforwardContinuous AddCommGrpCat J K).IsRightAdjoint] [u.Final]
  [CategoryTheory.Limits.PreservesFiniteLimits (u.sheafPullback AddCommGrpCat J K)]
  [CategoryTheory.EnoughInjectives (CategoryTheory.Sheaf K AddCommGrpCat)]
  {F : CategoryTheory.Sheaf K AddCommGrpCat}
  (hF :
    ∀ (q : ℕ),
      CategoryTheory.Limits.IsZero ((u.sheafHigherDirectImage AddCommGrpCat J K (q + 1)).obj F))
  (n : ℕ) :
  Function.Bijective
    ⇑(CategoryTheory.Sheaf.H.lerayEdge (u.sheafAdjunctionContinuous AddCommGrpCat J K)
        (u.sheafPullbackConstantSheafIso AddCommGrpCat J K ↧(ULift.{w, 0} ℤ)).inv F n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Leray/Edge.html#CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Leray/Edge.html#CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective)
- [Source of `CategoryTheory.Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective` in TauCeti/CategoryTheory/Sites/SheafCohomology/Leray/Edge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Sites/SheafCohomology/Leray/Edge.lean#L328)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
