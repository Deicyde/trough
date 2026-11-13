---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSemiRepresentable.faithful_situationTotalInverseImage, CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage, CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage, CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage, CategoryTheory.SimplicialSemiRepresentable.isCartesianSheaf_of_mem_essImage, CategoryTheory.SimplicialSemiRepresentable.isCartesianAbSheaf_of_mem_essImage, CategoryTheory.SimplicialSemiRepresentable.full_inverseImage, CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulInverseImageHypercovering
statement: formalized
proof: formalized
---

# 85.17 Cohomological descent for hypercoverings

Section 85.17 of the Stacks Project, [Tag 0D8D](https://stacks.math.columbia.edu/tag/0D8D). 6 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D8E, a lemma

[Tag 0D8E](https://stacks.math.columbia.edu/tag/0D8E) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.faithful_situationTotalInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDegreeZeroFaithful.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDegreeZeroFaithful.lean#L86). The attribute's comment: “part (1): a^\{-1} of Stacks 0D70 on sheaves of sets is faithful, for the simplicial-site situation attached to a hypercovering”.

> **Stacks 0D8E (1), the faithfulness half**, for the inverse image of the total augmentation
> as Stacks 0D70 constructs it from the simplicial-site situation of a hypercovering: that inverse
> image is faithful.

```lean
theorem faithful_situationTotalInverseImage :
    (SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi
      (situation P.toGrothendieck H.toSimplicialObject) (Cat.of C) P.toGrothendieck
      (situationAugmentation P.toGrothendieck H.toSimplicialObject)).inverseImage.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L273). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is faithful”.

> **Stacks 0D8E (1), the faithfulness half.** For a hypercovering `K` the inverse image
> `a^{-1} : Sh(C) ⥤ Sh((C/K)_total)` of the augmentation is faithful.
>
> The inverse image is restriction along `j_total`, which is continuous and cover dense, and
> restriction along such a functor is faithful by Stacks 04D9.

```lean
theorem faithful_inverseImage [HasEqualizers C] [HasPullbacks C] (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P) :
    (totalLocalizationMorphism P.toGrothendieck H.toSimplicialObject).inverseImage.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L283). The attribute's comment: “part (1): a^\{-1} of Stacks 0D70 on sheaves of sets is faithful”.

> **Stacks 0D8E (1), the faithfulness half**, for the inverse image of the morphism of topoi
> which Stacks 0D70 attaches to the augmentation. By Stacks 0D8B that functor is isomorphic to
> restriction along `j_total`, and faithfulness is invariant under isomorphism of functors.

```lean
theorem faithful_totalInverseImage [HasEqualizers C] [HasPullbacks C] (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P) :
    Functor.Faithful
      (augmentation P.toGrothendieck H.toSimplicialObject).totalMorphismOfTopoi.inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L297). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is faithful”.

> **Stacks 0D8E (2), the faithfulness half.** For a hypercovering `K` the inverse image
> `a^{-1} : Ab(C) ⥤ Ab((C/K)_total)` of the augmentation — restriction along `j_total` on abelian
> sheaves, as in Stacks 09WM (2) — is faithful.
>
> Cover density of `j_total` is a statement about the site, so the argument of
> `faithful_inverseImage` applies at any coefficient category.

```lean
theorem faithful_abelianInverseImage [HasEqualizers C] [HasPullbacks C] (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P) :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
      ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
      P.toGrothendieck).Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianSheaf_of_mem_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L328). The attribute's comment: “part (1): the essential image of a^\{-1} consists of cartesian sheaves of sets”.

> **Stacks 0D8E (1), the inclusion of the essential image in the cartesian sheaves.** Every
> sheaf of sets on the total site isomorphic to an inverse image along the augmentation is
> cartesian.
>
> This is Stacks 0D7H (1) together with invariance of cartesianness under isomorphism, and uses no
> condition on the simplicial semi-representable object `K`.

```lean
theorem isCartesianSheaf_of_mem_essImage {F : Sheaf (situation J K).totalTopology (Type u)}
    (hF : (totalLocalizationMorphism J K).inverseImage.essImage F) :
    (situation J K).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianAbSheaf_of_mem_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L343). The attribute's comment: “part (2): the essential image of a^\{-1} consists of cartesian abelian sheaves”.

> **Stacks 0D8E (2), the inclusion of the essential image in the cartesian sheaves.** Every
> sheaf of abelian groups on the total site isomorphic to an inverse image along the augmentation is
> cartesian.
>
> Cartesianness of an abelian sheaf is cartesianness of its underlying sheaf of sets, and the
> underlying sheaf of the restriction of `𝒢` along `j_total` is the restriction of the underlying
> sheaf of `𝒢`, both being a composition of functors. So the abelian statement follows from the
> statement for sheaves of sets applied to the underlying sheaf.

```lean
theorem isCartesianAbSheaf_of_mem_essImage {F : Sheaf (situation J K).totalTopology Ab.{u}}
    (hF : ((totalForget K).sheafPushforwardContinuous Ab.{u}
      ((situation J K).totalTopology) J).essImage F) :
    (situation J K).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L466). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is full, carrying local fullness of j\_total”.

> **Stacks 0D8E (1), fullness**, carrying local fullness of `j_total`.
>
> For a hypercovering `K` the inverse image `a^{-1} : Sh(C) ⥤ Sh((C/K)_total)` of the augmentation
> is full as soon as the localization functor `j_total` is locally full for the topology of `C`.
> That local fullness — unwound at two objects of the total site, the local existence of a simplex
> of `K` carrying two prescribed charts on two of its faces — is the input the degree-zero
> condition does not supply, and it is carried here as a hypothesis.

```lean
theorem full_inverseImage
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    (totalLocalizationMorphism P.toGrothendieck H.toSimplicialObject).inverseImage.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulInverseImageHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L474). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is fully faithful, carrying local fullness”.

> **Stacks 0D8E (1), full faithfulness**, carrying local fullness of `j_total`.

```lean
def fullyFaithfulInverseImageHypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    (totalLocalizationMorphism P.toGrothendieck
      H.toSimplicialObject).inverseImage.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L485). The attribute's comment: “part (1): E = a\_* a^\{-1} E on sheaves of sets, carrying local fullness”.

> **Stacks 0D8E (1), the unit is invertible**, carrying local fullness of `j_total`: for every
> sheaf of sets `E` on `C` the canonical map `E ⟶ a_* a^{-1} E` is an isomorphism. This is the
> half of "`a_*` is a quasi-inverse" that holds on all of `Sh(C)`.

```lean
theorem isIso_unit_hypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    IsIso (totalLocalizationMorphism P.toGrothendieck H.toSimplicialObject).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L495). The attribute's comment: “part (1): essential image = cartesian sheaves of sets, carrying surjectivity”.

> **Stacks 0D8E (1), the essential image is exactly the cartesian sheaves**, carrying
> essential surjectivity onto them. One inclusion is `isCartesianSheaf_of_mem_essImage`; the other
> is the clause the degree-zero condition does not supply, and it is carried as a hypothesis.

```lean
theorem mem_essImage_iff_isCartesianSheaf
    (hsurj : ∀ G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology
        (Type u),
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf G →
        (totalLocalizationMorphism P.toGrothendieck
          H.toSimplicialObject).inverseImage.essImage G)
    (F : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u)) :
    (totalLocalizationMorphism P.toGrothendieck
        H.toSimplicialObject).inverseImage.essImage F ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L513). The attribute's comment: “part (1): a^\{-1} a\_* F = F for cartesian F, carrying both remaining clauses”.

> **Stacks 0D8E (1), the counit is invertible on cartesian sheaves**, carrying both of the two
> clauses: for a cartesian sheaf of sets `F` on the total site the canonical map
> `a^{-1} a_* F ⟶ F` is an isomorphism. This is the half of "`a_*` is a quasi-inverse" that holds
> on the cartesian sheaves; the two carried hypotheses supply full faithfulness of `a^{-1}` and
> membership of `F` in its essential image.

```lean
theorem isIso_counit_app_hypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck)
    (hsurj : ∀ G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology
        (Type u),
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf G →
        (totalLocalizationMorphism P.toGrothendieck
          H.toSimplicialObject).inverseImage.essImage G)
    {F : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u)}
    (hF : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf F) :
    IsIso ((totalLocalizationMorphism P.toGrothendieck
      H.toSimplicialObject).adj.counit.app F)
```

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L530). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is full, carrying local fullness of j\_total”.

> **Stacks 0D8E (2), fullness**, carrying local fullness of `j_total`. Local fullness is a
> condition on the site, so the same input serves at abelian coefficients.

```lean
theorem full_abelianInverseImage
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
      ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
      P.toGrothendieck).Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulAbelianInverseImageHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L540). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is fully faithful, carrying local fullness”.

> **Stacks 0D8E (2), full faithfulness**, carrying local fullness of `j_total`.

```lean
def fullyFaithfulAbelianInverseImageHypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
      ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
      P.toGrothendieck).FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L551). The attribute's comment: “part (2): E = a\_* a^\{-1} E on abelian sheaves, carrying local fullness”.

> **Stacks 0D8E (2), the unit is invertible**, carrying local fullness of `j_total`: for every
> sheaf of abelian groups `E` on `C` the canonical map `E ⟶ a_* a^{-1} E` is an isomorphism.

```lean
theorem isIso_abelianUnit_hypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck) :
    IsIso (abelianTotalAdjunction P.toGrothendieck H.toSimplicialObject).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianAbSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L560). The attribute's comment: “part (2): essential image = cartesian abelian sheaves, carrying surjectivity”.

> **Stacks 0D8E (2), the essential image is exactly the cartesian abelian sheaves**, carrying
> essential surjectivity onto them.

```lean
theorem mem_essImage_iff_isCartesianAbSheaf
    (hsurj : ∀ G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u},
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G →
        ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
          ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
          P.toGrothendieck).essImage G)
    (F : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u}) :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
        ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
        P.toGrothendieck).essImage F ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDescent.lean#L577). The attribute's comment: “part (2): a^\{-1} a\_* F = F for cartesian F, carrying both remaining clauses”.

> **Stacks 0D8E (2), the counit is invertible on cartesian abelian sheaves**, carrying both of
> the two clauses: for a cartesian sheaf of abelian groups `F` on the total site the canonical map
> `a^{-1} a_* F ⟶ F` is an isomorphism.

```lean
theorem isIso_abelianCounit_app_hypercovering
    (hlf : (totalForget H.toSimplicialObject).IsLocallyFull P.toGrothendieck)
    (hsurj : ∀ G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u},
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G →
        ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
          ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
          P.toGrothendieck).essImage G)
    {F : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u}}
    (hF : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf F) :
    IsIso ((abelianTotalAdjunction P.toGrothendieck
      H.toSimplicialObject).counit.app F)
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurj.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurj.lean#L522). The attribute's comment: “part (1): essential image = cartesian sheaves of sets”.

> **Stacks 0D8E (1), the essential image is exactly the cartesian sheaves of sets.** A sheaf of
> sets on the total site of a hypercovering of the final presheaf lies in the essential image of
> restriction along the localization functor `j_total` if and only if it is cartesian.

```lean
theorem mem_essImage_iff_isCartesianSheaf' (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (E : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u)) :
    (totalLocalizationMorphism P.toGrothendieck
        H.toSimplicialObject).inverseImage.essImage E ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf E
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_hypercovering'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurj.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurj.lean#L535). The attribute's comment: “part (1): a^\{-1} a\_* F = F for cartesian F”.

> **Stacks 0D8E (1), `a⁻¹ a_* F = F` for cartesian `F`.** For a cartesian sheaf of sets `E` on
> the total site of a hypercovering of the final presheaf, the counit `a⁻¹ a_* E ⟶ E` is an
> isomorphism.

```lean
theorem isIso_counit_app_hypercovering' (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (E : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u))
    (hE : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf E) :
    IsIso ((totalLocalizationMorphism P.toGrothendieck
      H.toSimplicialObject).adj.counit.app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianAbSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurjAb.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurjAb.lean#L198). The attribute's comment: “part (2): essential image = cartesian abelian sheaves”.

> **Stacks 0D8E (2), the essential image is exactly the cartesian abelian sheaves.** One
> inclusion is `isCartesianAbSheaf_of_mem_essImage`, the other is
> `essImage_of_isCartesianAbSheaf`.

```lean
theorem mem_essImage_iff_isCartesianAbSheaf' (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u}) :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
        ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
        P.toGrothendieck).essImage G ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_hypercovering'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurjAb.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringEssSurjAb.lean#L214). The attribute's comment: “part (2): a^\{-1} a\_* F = F for cartesian abelian F”.

> **Stacks 0D8E (2), `a⁻¹ a_* F = F` for cartesian `F`.** For a cartesian sheaf of abelian
> groups `F` on the total site the canonical map `a⁻¹ a_* F ⟶ F` is an isomorphism. This is the
> half of "`a_*` is a quasi-inverse" that holds on the cartesian abelian sheaves: `a⁻¹` is fully
> faithful, so its counit is invertible exactly on its essential image, and
> `essImage_of_isCartesianAbSheaf` puts `F` there.

```lean
theorem isIso_abelianCounit_app_hypercovering' (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u})
    (hG : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G) :
    IsIso ((abelianTotalAdjunction P.toGrothendieck
      H.toSimplicialObject).counit.app G)
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImage_of_isCartesianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L106). The attribute's comment: “part (1): every cartesian sheaf of sets is an a^\{-1}E for the a of Stacks 0D70 at the simplicial-site situation”.

> **Stacks 0D8E (1), essential surjectivity onto the cartesian sheaves of sets**, for the
> inverse image of the morphism of topoi which Stacks 0D70 attaches to the augmentation of the
> simplicial-site situation of a hypercovering.
>
> By Stacks 0D8B that inverse image is restriction along `j_total`, for which every cartesian sheaf
> of sets is an inverse image by
> `CategoryTheory.SimplicialSemiRepresentable.essImage_of_isCartesianSheaf`.

```lean
theorem essImage_situationTotalInverseImage_of_isCartesianSheaf
    (E : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u))
    (hE : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf E) :
    (Augmentation.totalMorphismOfTopoi
      (situation P.toGrothendieck H.toSimplicialObject) (Cat.of C) P.toGrothendieck
      (situationAugmentation P.toGrothendieck H.toSimplicialObject)).inverseImage.essImage E
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImage_iff_isCartesianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L124). The attribute's comment: “part (1): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation is exactly the cartesian sheaves of sets”.

> **Stacks 0D8E (1), the essential image is exactly the cartesian sheaves of sets**, for the
> inverse image of the morphism of topoi of Stacks 0D70 at the simplicial-site situation. One
> inclusion is `mem_essImage_iff_isCartesianSheaf'` carried across Stacks 0D8B, the other is
> `essImage_situationTotalInverseImage_of_isCartesianSheaf`.

```lean
theorem mem_essImage_situationTotalInverseImage_iff_isCartesianSheaf
    (E : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology (Type u)) :
    (Augmentation.totalMorphismOfTopoi
        (situation P.toGrothendieck H.toSimplicialObject) (Cat.of C) P.toGrothendieck
        (situationAugmentation P.toGrothendieck H.toSimplicialObject)).inverseImage.essImage E ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianSheaf E
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L140). The attribute's comment: “part (2): every cartesian abelian sheaf is an a^\{-1}G for the a of Stacks 0D70 at the simplicial-site situation”.

> Every cartesian abelian sheaf on the total site lies in the essential image of the abelian
> inverse image of the morphism of topoi which Stacks 0D70 attaches to the augmentation of the
> simplicial-site situation of a hypercovering.

```lean
theorem essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u})
    (hG : (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G) :
    (Augmentation.totalInverseImageAb (situation P.toGrothendieck H.toSimplicialObject)
      (Cat.of C) P.toGrothendieck
      (situationAugmentation P.toGrothendieck H.toSimplicialObject)).essImage G
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImageAb_iff_isCartesianAbSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L155). The attribute's comment: “part (2): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation is exactly the cartesian abelian sheaves”.

> The essential image of the abelian inverse image of the morphism of topoi of Stacks 0D70 at
> the simplicial-site situation of a hypercovering is exactly the cartesian abelian sheaves.

```lean
theorem mem_essImage_situationTotalInverseImageAb_iff_isCartesianAbSheaf (P : Pretopology C)
    (H : HypercoveringOfTerminal.{u, u, u} P)
    (G : Sheaf (situation P.toGrothendieck H.toSimplicialObject).totalTopology Ab.{u}) :
    (Augmentation.totalInverseImageAb (situation P.toGrothendieck H.toSimplicialObject)
        (Cat.of C) P.toGrothendieck
        (situationAugmentation P.toGrothendieck H.toSimplicialObject)).essImage G ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsCartesianAbSheaf G
```

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L212). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is full”.

> **Stacks 0D8E (1), fullness.** For a hypercovering `K` the inverse image
> `a^{-1} : Sh(C) ⥤ Sh((C/K)_total)` of the augmentation is full.
>
> The localization functor `j_total` is cover dense by `isCoverDense_totalForget` and locally full
> by `isLocallyFull_totalForget`, and restriction along a continuous functor which is both is
> full.

```lean
theorem full_inverseImage' :
    (totalLocalizationMorphism P.toGrothendieck H.toSimplicialObject).inverseImage.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulInverseImageHypercovering'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L221). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is fully faithful”.

> **Stacks 0D8E (1), full faithfulness.** For a hypercovering `K` the inverse image
> `a^{-1} : Sh(C) ⥤ Sh((C/K)_total)` of the augmentation is fully faithful: it is faithful by
> `faithful_inverseImage_of_isCoverDense` and full by `full_inverseImage'`.

```lean
def fullyFaithfulInverseImageHypercovering' :
    (totalLocalizationMorphism P.toGrothendieck
      H.toSimplicialObject).inverseImage.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_hypercovering'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L232). The attribute's comment: “part (1): E = a\_* a^\{-1} E on sheaves of sets”.

> **Stacks 0D8E (1), `E = a_* a^{-1} E`.** For every sheaf of sets `E` on `C` the canonical
> map `E ⟶ a_* a^{-1} E` is an isomorphism, `a^{-1}` being restriction along `j_total`. This is the
> half of "`a_*` is a quasi-inverse" that holds on all of `Sh(C)`: the unit of an adjunction with
> fully faithful left adjoint is invertible.

```lean
theorem isIso_unit_hypercovering' :
    IsIso (totalLocalizationMorphism P.toGrothendieck H.toSimplicialObject).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L241). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is full”.

> **Stacks 0D8E (2), fullness.** For a hypercovering `K` the inverse image
> `a^{-1} : Ab(C) ⥤ Ab((C/K)_total)` of the augmentation is full. Cover density and local fullness
> of `j_total` are conditions on the site, so the same input serves at abelian coefficients.

```lean
theorem full_abelianInverseImage' :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
      ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
      P.toGrothendieck).Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulAbelianInverseImageHypercovering'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L251). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is fully faithful”.

> **Stacks 0D8E (2), full faithfulness.** For a hypercovering `K` the inverse image
> `a^{-1} : Ab(C) ⥤ Ab((C/K)_total)` of the augmentation is fully faithful.

```lean
def fullyFaithfulAbelianInverseImageHypercovering' :
    ((totalForget H.toSimplicialObject).sheafPushforwardContinuous Ab.{u}
      ((situation P.toGrothendieck H.toSimplicialObject).totalTopology)
      P.toGrothendieck).FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_hypercovering'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L262). The attribute's comment: “part (2): E = a\_* a^\{-1} E on abelian sheaves”.

> **Stacks 0D8E (2), `E = a_* a^{-1} E`.** For every sheaf of abelian groups `E` on `C` the
> canonical map `E ⟶ a_* a^{-1} E` is an isomorphism, `a^{-1}` being restriction along
> `j_total`.

```lean
theorem isIso_abelianUnit_hypercovering' :
    IsIso (abelianTotalAdjunction P.toGrothendieck H.toSimplicialObject).unit
```

## Tag 0D8F, a lemma

[Tag 0D8F](https://stacks.math.columbia.edu/tag/0D8F) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.cechComplexIsoSheafHomComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringForkVertexCosimplicial.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringForkVertexCosimplicial.lean#L442).

> **Stacks 0D8F.** The Čech complex of Stacks 0D79 associated to `a⁻¹F`,
>
> `a_{0,*}a_0⁻¹F ⟶ a_{1,*}a_1⁻¹F ⟶ a_{2,*}a_2⁻¹F ⟶ …`
>
> is canonically isomorphic — the source says equal, and the comparison is indeed the identity in
> every degree once the terms are identified — to the cochain complex
> `SheafHom(s(ℤ_{F(K)}^#), F)` obtained by applying the abelian internal hom `ℋom(-, F)` to the
> complex of free abelian sheaves of Stacks 01GB.
>
> The differentials of both complexes are the alternating sums induced by the simplicial structure
> of `K`, so a cosimplicial identification of the terms suffices; that is the whole of the source's
> argument. The identification of the terms itself,
> `a_{n,*}a_n⁻¹F = ℋom'(F(K_n)^#, F) = ℋom(ℤ_{F(K_n)}^#, F)`, is
> `cechCosimplicialObjectIsoSheafHomCosimplicialObject`.

```lean
def cechComplexIsoSheafHomComplex (F : Sheaf J AddCommGrpCat.{u}) :
    cechComplex J K F ≅ sheafHomComplex J K F
```

## Tag 0D8G, a lemma

[Tag 0D8G](https://stacks.math.columbia.edu/tag/0D8G) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnit_app_of_hypercovering_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean#L189).

> For a site `C` with equalizers and fibre products, a hypercovering `K` of it and the
> augmentation `a : Sh((C/K)_total) ⟶ Sh(C)` of Stacks 0D8B, the canonical map `E ⟶ Ra_* a⁻¹ E` is
> an isomorphism at every object `E` of the unbounded derived category of abelian sheaves on `C`.
>
> No boundedness is assumed on `E`, as in the source. The untagged forms
> `Stacks.CategoryTheory.Hypercovering.isIso_derivedAugmentationUnit_app_of_hypercovering'` and
> `Stacks.CategoryTheory.Hypercovering.isIso_derivedAugmentationUnit_app_of_hypercovering` take the
> `Ra_*`-acyclicity of `a⁻¹` of a K-injective complex (and, for the latter, Stacks 0D8E) as
> hypotheses; here the acyclicity is
> `inverseImageComputesDerivedPushforward_of_hypercoveringOfTerminal`.

```lean
theorem isIso_derivedAugmentationUnit_app_of_hypercovering_unconditional
    (E : DerivedCategory (Sheaf P.toGrothendieck AddCommGrpCat.{u})) :
    IsIso ((Augmentation.derivedAugmentationUnit (hypercoveringSituation P H) (Cat.of C)
      P.toGrothendieck (hypercoveringAugmentation P H)).app E)
```

## Tag 0D8H, a lemma

[Tag 0D8H](https://stacks.math.columbia.edu/tag/0D8H) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.derivedGlobalSectionsInverseImageIsoOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDerivedGlobalSections.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDerivedGlobalSections.lean#L225). The attribute's comment: “for the augmentation of Tag 0D8B attached to a hypercovering”.

> **Stacks 0D8H.** For a site `C` with equalizers and fibre products, a hypercovering `K` of
> it, and the augmentation `a : Sh((C/K)_total) ⟶ Sh(C)` of Stacks 0D8B, derived global sections on
> `C` are derived global sections on the total site of the inverse image:
>
> `RΓ(C, E) = RΓ((C/K)_total, a⁻¹E)`.
>
> The statement is an isomorphism of functors on the *unbounded* derived category of abelian
> sheaves on `C`, so it holds at every object `E` with no boundedness assumption, which is the form
> the source states.
>
> No hypothesis beyond the hypercovering conditions on `K` is carried: the three inputs of the
> general `CategoryTheory.SimplicialSiteSituation.Augmentation.derivedGlobalSectionsInverseImageIso`
> are proved for this augmentation. The underived unit `F ⟶ a_*a⁻¹F` is invertible by
> `CategoryTheory.SimplicialSemiRepresentable.isIso_situationAbelianTotalAdjunctionUnit` (Stacks
> 0D8E in its abelian form), `a⁻¹` of a K-injective complex computes `R a_*` by
> `SimplicialSemiRepresentable.inverseImageComputesDerivedPushforward_of_hypercoveringOfTerminal`,
> and the underived identity `Γ(C, a_*F) = Γ((C/K)_total, F)` is
> `CategoryTheory.SimplicialSemiRepresentable.abelianTotalPushforwardGammaIso`.

```lean
def derivedGlobalSectionsInverseImageIsoOfHypercovering :
    Augmentation.derivedGlobalSectionsBase (Cat.of C) J.toGrothendieck ≅
      Augmentation.derivedTotalInverseImage (hypercoveringSituation J H) (Cat.of C)
          J.toGrothendieck (hypercoveringAugmentation J H) ⋙
        Augmentation.derivedGlobalSectionsTotal (hypercoveringSituation J H)
```

**`Stacks.CategoryTheory.Hypercovering.derivedGlobalSectionsInverseImageIsoOfHypercovering'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDerivedGlobalSectionsUnconditional.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringDerivedGlobalSectionsUnconditional.lean#L158).

> **Stacks 0D8H.** For a site `C` with equalizers
> and fibre products, a hypercovering `K` of it, and the augmentation
> `a : Sh((C/K)_total) ⟶ Sh(C)` of Stacks 0D8B, derived global sections on `C` are derived global
> sections on the total site of the inverse image:
>
> `RΓ(C, E) = RΓ((C/K)_total, a⁻¹E)`.
>
> The statement is an isomorphism of functors on the *unbounded* derived category of abelian
> sheaves on `C`, so it holds at every object `E` with no boundedness assumption, which is the form
> the source states.
>
> No hypothesis beyond the hypercovering conditions on `K` is carried. The `R a_*`-acyclicity of
> `a⁻¹` of a K-injective complex, which is the one remaining input of Stacks 0D8G, is
> `CategoryTheory.SimplicialSemiRepresentable`
> `.inverseImageComputesDerivedPushforward_of_hypercoveringOfTerminal`. The other input of
> Stacks 0D8G, that the underived unit `F ⟶ a_*a⁻¹F` is an isomorphism, is Stacks 0D8E in its
> abelian form, which
> `CategoryTheory.SimplicialSemiRepresentable.isIso_situationAbelianTotalAdjunctionUnit` proves for
> this augmentation. The underived identity `Γ(C, a_*F) = Γ((C/K)_total, F)` on which the
> factorisation of Stacks 08J6 rests is
> `CategoryTheory.SimplicialSemiRepresentable.abelianTotalPushforwardGammaIso`. The derived content
> of Stacks 08J6 is *not* assumed: see the module docstring.

```lean
def derivedGlobalSectionsInverseImageIsoOfHypercovering' :
    Augmentation.derivedGlobalSectionsBase (Cat.of C) J.toGrothendieck ≅
      Augmentation.derivedTotalInverseImage (hypercoveringSituation J H) (Cat.of C)
          J.toGrothendieck (hypercoveringAugmentation J H) ⋙
        Augmentation.derivedGlobalSectionsTotal (hypercoveringSituation J H)
```

## Tag 0D8I, a lemma

[Tag 0D8I](https://stacks.math.columbia.edu/tag/0D8I) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.derivedTotalInverseImageEquivalenceOfHypercovering'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean#L114). References: SGA 4 Vbis (2.2.7), “special case”.

> **Stacks 0D8I.** For a site `C` with
> equalizers and fibre products, a hypercovering `K` of it, the augmentation `a` of Stacks 0D8B and
> the weak Serre subcategory `𝒜 ⊂ Ab((C/K)_total)` of cartesian abelian sheaves of Stacks 0D7J, the
> derived inverse image is an equivalence
>
> `a⁻¹ : D⁺(C) ⟶ D⁺_𝒜((C/K)_total)`
>
> with quasi-inverse `R a_*`. Both functors of the equivalence are the restrictions of `a⁻¹` and
> of `R a_*` on the nose, since the equivalence is the restricted adjunction.
>
> The `Ra_*`-acyclicity input of Stacks 0D8G, that `a⁻¹` of a K-injective complex computes
> `R a_*`, is `CategoryTheory.SimplicialSemiRepresentable`
> `.inverseImageComputesDerivedPushforward_of_hypercoveringOfTerminal`. The other input of
> Stacks 0D8G, that the underived unit `F ⟶ a_*a⁻¹F` is an isomorphism, is Stacks 0D8E in its
> abelian form, which
> `CategoryTheory.SimplicialSemiRepresentable.isIso_situationAbelianTotalAdjunctionUnit` proves for
> this augmentation. The essential surjectivity input of
> `Augmentation.isIso_derivedCounit_app_of_isCartesian`, that every cartesian abelian sheaf on the
> total site lies in the essential image of `a⁻¹`, is discharged here by
> `CategoryTheory.SimplicialSemiRepresentable`
> `.essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf`,
> the Stacks 0D8E (2) clause in the spelling of `a⁻¹` as `Augmentation.totalInverseImageAb`.

```lean
def derivedTotalInverseImageEquivalenceOfHypercovering' :
    (DerivedCategoryB.derivedCategoryBPlus
        (⊤ : ObjectProperty (Sheaf J.toGrothendieck AddCommGrpCat.{u}))).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus
        ((hypercoveringSituation J H).IsCartesianAbSheaf)).FullSubcategory
```

**`Stacks.CategoryTheory.Hypercovering.derivedTotalInverseImageEquivalenceOfHypercovering_functor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean#L132). The attribute's comment: “the forward functor of the equivalence is a⁻¹”.

> **Stacks 0D8I, the forward functor of the equivalence is `a⁻¹`:** it is the restriction of
> the derived inverse image to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOfHypercovering_functor' :
    (derivedTotalInverseImageEquivalenceOfHypercovering' J H).functor =
      Augmentation.derivedTotalInverseImagePlus (hypercoveringSituation J H) (Cat.of C)
        J.toGrothendieck (hypercoveringAugmentation J H)
```

**`Stacks.CategoryTheory.Hypercovering.derivedTotalInverseImageEquivalenceOfHypercovering_inverse'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBoundedBelowEquivalenceUnconditional.lean#L141). The attribute's comment: “the quasi-inverse of the equivalence is Ra\_*”.

> **Stacks 0D8I, the quasi-inverse of the equivalence is `R a_*`:** it is the restriction of
> the derived direct image to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOfHypercovering_inverse' :
    (derivedTotalInverseImageEquivalenceOfHypercovering' J H).inverse =
      Augmentation.derivedTotalPushforwardPlus (hypercoveringSituation J H) (Cat.of C)
        J.toGrothendieck (hypercoveringAugmentation J H)
```

## Tag 09X6, a remark

[Tag 09X6](https://stacks.math.columbia.edu/tag/09X6) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.hasPullbacks_and_hasEqualizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheaf.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheaf.lean#L332). The attribute's comment: “the site `C/G` of pairs `(U, s)`, `s ∈ G(U)`, has fibre products and equalizers”.

> **Stacks 09X6, the site `C/G` has fibre products and equalizers.** If `C` has fibre products
> and equalizers, so does the localization `C/G` of `C` at a presheaf of sets `G`: the projection
> `C/G ⥤ C` creates connected limits.

```lean
theorem hasPullbacks_and_hasEqualizers [HasPullbacks C] [HasEqualizers C] :
    HasPullbacks (CostructuredArrow (yoneda (C := C)) G) ∧
      HasEqualizers (CostructuredArrow (yoneda (C := C)) G)
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.sectionsOverPresheafSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean#L116). The attribute's comment: “`H⁰(G, -) = H⁰(G^#, -)`, the functor whose derived functor is `RΓ(G, -)`”.

> **`H⁰(G, -) = H⁰(G^#, -)`** (Stacks 079X, observation (1), quoted in Stacks 09X6): the free
> abelian sheaf functor inverts the sheafification map `G ⟶ G^#`.

```lean
def sectionsOverPresheafSheafifyIso :
    sectionsOverPresheaf J G ≅
      sectionsOverPresheaf J (sheafify J G)
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.derivedSectionsOverPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean#L342). The attribute's comment: “`RΓ(G, E) = RΓ(C/G, j⁻¹E)` for the localization functor `j : C/G → C`, the analogue of Tag 03F3; an isomorphism of functors on the unbounded derived category”.

> **Stacks 09X6, `RΓ(G, E) = RΓ(C/G, j⁻¹E)`.** Let `C` be a site and `G` a presheaf of sets on
> `C`, let `RΓ(G, -)` be the derived functor of `H⁰(G, -) = H⁰(G^#, -)`, maps out of `G` (Stacks
> 079X), and let `j : C/G ⥤ C` be the localization functor of Stacks 0791. Then
>
> `RΓ(G, E) = RΓ(C/G, j⁻¹E)`
>
> naturally in `E` in the unbounded derived category of abelian sheaves on `C`: the analogue of
> Stacks 03F3 for the localization at `G`.

```lean
def derivedSectionsOverPresheafIso [HasDerivedCategory (Sheaf J AddCommGrpCat.{u})]
    [HasDerivedCategory (Sheaf (localizationTopology J G) AddCommGrpCat.{u})]
    [HasDerivedCategory AddCommGrpCat.{u}] :
    derivedSectionsOverPresheaf J G ≅
      ((CostructuredArrow.proj yoneda G).sheafPushforwardContinuous AddCommGrpCat.{u}
          (localizationTopology J G) J).mapDerivedCategory ⋙
        Stacks.DerivedFunctor.totalRightDerived
          (Sheaf.Γ (localizationTopology J G) AddCommGrpCat.{u})
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.derivedGlobalSectionsLocalizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean#L413). The attribute's comment: “for a hypercovering `K` of `G`, `RΓ(C/G, E) = RΓ((C/K)_total, a⁻¹E)` with `a` the canonical augmentation; an isomorphism of functors on the unbounded derived category, which contains `D⁺(C/G)`”.

> **Stacks 09X6, `RΓ(C/G, E) = RΓ((C/K)_total, a⁻¹E)`.** For a hypercovering `K` of a presheaf
> of sets `G` on a site `C` with equalizers and fibre products, regarded as a hypercovering of the
> site `C/G`, and the canonical augmentation `a : Sh((C/K)_total) ⟶ Sh(C/G)`, derived global
> sections on `C/G` are derived global sections on the total site of the inverse image. This is
> Stacks 0D8H for the site `C/G`, as the remark says.

```lean
def derivedGlobalSectionsLocalizationIso :
    Augmentation.derivedGlobalSectionsBase (Cat.of (CostructuredArrow (yoneda (C := C)) G))
        (localizationPretopology G P).toGrothendieck ≅
      Augmentation.derivedTotalInverseImage
          (hypercoveringSituation (localizationPretopology G P) (localizedHypercovering G P H))
          (Cat.of (CostructuredArrow (yoneda (C := C)) G))
          (localizationPretopology G P).toGrothendieck
          (hypercoveringAugmentation (localizationPretopology G P)
            (localizedHypercovering G P H)) ⋙
        Augmentation.derivedGlobalSectionsTotal
          (hypercoveringSituation (localizationPretopology G P) (localizedHypercovering G P H))
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.derivedSectionsOverPresheafInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean#L429). The attribute's comment: “`RΓ(G, E) = RΓ((C/K)_total, a⁻¹j⁻¹E)` for a hypercovering `K` of `G`”.

> **Stacks 09X6, `RΓ(G, E) = RΓ((C/K)_total, a⁻¹j⁻¹E)`.**

```lean
def derivedSectionsOverPresheafInverseImageIso :
    derivedSectionsOverPresheaf P.toGrothendieck G ≅
      (localizationInverseImage G P).mapDerivedCategory ⋙
        Augmentation.derivedTotalInverseImage
            (hypercoveringSituation (localizationPretopology G P) (localizedHypercovering G P H))
            (Cat.of (CostructuredArrow (yoneda (C := C)) G))
            (localizationPretopology G P).toGrothendieck
            (hypercoveringAugmentation (localizationPretopology G P)
              (localizedHypercovering G P H)) ⋙
          Augmentation.derivedGlobalSectionsTotal
            (hypercoveringSituation (localizationPretopology G P) (localizedHypercovering G P H))
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.derivedSectionsOverPresheafCompositeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafCohomology.lean#L563). The attribute's comment: “for a hypercovering `K` of `G`, `RΓ(G, E) = RΓ((C/K)_total, g⁻¹E)` with `g` the composition of `a` and `j`; an isomorphism of functors on the unbounded derived category, which contains `D⁺(C)`”.

> **Stacks 09X6, `RΓ(G, E) = RΓ((C/K)_total, g⁻¹E)`.** Let `C` be a site with equalizers and
> fibre products, `G` a presheaf of sets on `C` and `K` a hypercovering of `G`. Let
> `g : Sh((C/K)_total) ⟶ Sh(C)` be the composition of the canonical augmentation
> `a : Sh((C/K)_total) ⟶ Sh(C/G)` and of the localization morphism `j : Sh(C/G) ⟶ Sh(C)`. Then
>
> `RΓ(G, E) = RΓ((C/K)_total, g⁻¹E)`
>
> naturally in `E` in the unbounded derived category of abelian sheaves on `C`, in particular for
> `E ∈ D⁺(C)`.

```lean
def derivedSectionsOverPresheafCompositeIso :
    derivedSectionsOverPresheaf P.toGrothendieck G ≅
      (compositeInverseImage G P H).mapDerivedCategory ⋙
        Augmentation.derivedGlobalSectionsTotal
          (hypercoveringSituation (localizationPretopology G P) (localizedHypercovering G P H))
```

**`Stacks.CategoryTheory.Hypercovering.LocalizationAtPresheaf.hypercoveringOfEquivLocalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafHypercovering.lean, line 745](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/LocalizationAtPresheafHypercovering.lean#L745). The attribute's comment: “a hypercovering of `G` in `C` is the same thing as a hypercovering for the site `C/G`, for the site `C/G` of Stacks 0791 (coverings: families whose image generates a covering sieve of `C`)”.

> **A hypercovering of `G` is the same thing as a hypercovering of the site `C/G`.** Let `C` be a
> site, given by a pretopology `J`, with equalizers and fibre products, and let `G` be a presheaf of
> sets on `C`. Hypercoverings of `G` in `C` (Stacks 09VU) correspond bijectively to hypercoverings of
> the localized site `C/G` of Stacks 0791: a hypercovering `K` of `G` goes to the simplicial object
> `n ↦ {(K_{n,i}, s_{n,i})}` of `SR(C/G)`, where `s_{n,i}` is the restriction of the augmentation
> `F(K_n) ⟶ G` to the summand `h_{K_{n,i}}`, and the three conditions of Stacks 09VU for `K` over `G`
> are the three conditions for it over the final presheaf of `C/G`.

```lean
def hypercoveringOfEquivLocalization :
    HypercoveringOf.{v, w} J G ≃ HypercoveringOfTerminal.{w} (localizationPretopology G J)
```

**`Stacks.Sites.PresheafLocalization.mem_restrictedTopology_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PresheafLocalization.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PresheafLocalization.lean#L85). The attribute's comment: “The remark's instruction to define `C/G` for a PRESHEAF of sets `G` exactly as in Stacks 0791: the coverings of `C/G` are those coming from coverings of `C`, and the topology they generate is already `j.restrictedTopology J`, with no sheaf hypothesis on `G`. Carried: nothing. Claimed: this covering characterisation, which is what fixes the topology appearing in `nonempty_sheafEquiv_over_sheafification`. Disclaimed: fibre products and equalizers of `C/G` (Mathlib's `CostructuredArrow.hasLimitsOfShape_of_isConnected`), the hypercovering correspondence, and the `RΓ` transfer statements.”.

> **Stacks 09X6**, the covering sieves of the localization of `C` at a presheaf `G`: a sieve of
> an object `(U, s)` of `C/G` belongs to `j.restrictedTopology J`, for
> `j = CostructuredArrow.proj yoneda G`, exactly when its image under `j` is a covering sieve of
> `U`.

```lean
lemma mem_restrictedTopology_iff (X : CostructuredArrow (yoneda (C := C)) G) (S : Sieve X) :
    S ∈ (CostructuredArrow.proj yoneda G).restrictedTopology J X ↔
      S.functorPushforward (CostructuredArrow.proj yoneda G) ∈ J X.left
```

**`Stacks.Sites.PresheafLocalization.nonempty_sheafEquiv_over_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PresheafLocalization.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PresheafLocalization.lean#L255). The attribute's comment: “The parenthetical claim of the remark: the site `C/G` of pairs `(U, s)` with `s ∈ G(U)` for a PRESHEAF of sets `G`, with the coverings of `C`, satisfies `Sh(C/G) = Sh(C)/G^#`. Carried: Stacks 0791 (`Presheaf.IsSheaf.exists_sheafEquivalence_costructuredArrow_yoneda`) for the SHEAF `G^#`, supplying the right-hand equivalence. Claimed: the equivalence of categories, for a small site. Disclaimed: the rest of the remark — that `C/G` is a site with fibre products and equalizers (Mathlib's `CostructuredArrow.hasLimitsOfShape_of_isConnected`), that hypercoverings of `G` (Stacks 09VU) correspond to hypercoverings of `C/G`, and every `RΓ` transfer statement.”. References: SGA 3 IV (4.5.4), “more general”; SGA 4 III (5.4), “partial”.

> **Stacks 09X6**, the parenthetical claim: on a small site, the topos of sheaves on the
> localization of `C` at a presheaf of sets `G` is the localization of the topos `Sh(C)` at the sheaf
> `G^#`, that is, `Sh(C/G)` is equivalent to the slice category `Sh(C)/G^#`.

```lean
theorem nonempty_sheafEquiv_over_sheafification :
    Nonempty (Sheaf ((CostructuredArrow.proj yoneda G).restrictedTopology J) (Type u) ≌
      Over ((presheafToSheaf J (Type u)).obj G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.17, Tag 0D8D](https://stacks.math.columbia.edu/tag/0D8D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
