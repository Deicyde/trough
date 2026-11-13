---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.sheafHomology, CategoryTheory.Presheaf.isZero_sheafHomology_cechNerve_of_isLocallySurjective, CategoryTheory.Presheaf.isIso_cechNerveSheafHomologyZeroAugmentation, CategoryTheory.SimplicialObject.isIso_sheafHomologyFunctor_map_of_coskeletal, CategoryTheory.SimplicialObject.Augmented.isZero_sheafHomology_of_isLocallySurjective_matchingMaps, CategoryTheory.SimplicialObject.Augmented.sheafHomologyZeroIso_of_isLocallySurjective_matchingMaps, Stacks.CategoryTheory.Hypercovering.isZero_sheafHomology_of_isHypercovering, Stacks.CategoryTheory.Hypercovering.sheafHomologyZeroIso_of_isHypercovering
statement: formalized
proof: formalized
---

# 25.4 Acyclicity

Section 25.4 of the Stacks Project, [Tag 01GA](https://stacks.math.columbia.edu/tag/01GA). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01GB, a definition

[Tag 01GB](https://stacks.math.columbia.edu/tag/01GB) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SimplicialObject.sheafHomology`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechNerveHomology.lean#L431), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoskeletalAcyclicity.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoskeletalAcyclicity.lean#L120) (StacksFrontier).

## Tag 01GC, a lemma

[Tag 01GC](https://stacks.math.columbia.edu/tag/01GC) in the Stacks Project.

**`CategoryTheory.Presheaf.isZero_sheafHomology_cechNerve_of_isLocallySurjective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechNerveHomology.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechNerveHomology.lean#L528). The attribute's comment: “positive degrees”.

> The positive homology sheaves of the Čech nerve of a locally surjective morphism of
> presheaves of sets vanish.

```lean
lemma isZero_sheafHomology_cechNerve_of_isLocallySurjective (hf : IsLocallySurjective J f)
    (n : ℕ) (hn : 0 < n) :
    IsZero (SimplicialObject.sheafHomology J (Arrow.mk f).cechNerve n)
```

**`CategoryTheory.Presheaf.isIso_cechNerveSheafHomologyZeroAugmentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CechNerveHomology.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CechNerveHomology.lean#L545). The attribute's comment: “degree zero”.

> The augmentation of the Čech nerve of a locally surjective morphism induces an isomorphism
> from its degree-zero homology sheaf to the free abelian sheaf on the target.

```lean
lemma isIso_cechNerveSheafHomologyZeroAugmentation (hf : IsLocallySurjective J f) :
    IsIso (cechNerveSheafHomologyZeroAugmentation J f)
```

## Tag 01GD, a lemma

[Tag 01GD](https://stacks.math.columbia.edu/tag/01GD) in the Stacks Project.

**`CategoryTheory.SimplicialObject.isIso_sheafHomologyFunctor_map_of_coskeletal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CoskeletalAcyclicity.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CoskeletalAcyclicity.lean#L507). References: SGA 4 V (7.2.1), “homology iso”.

> **Stacks Project, Tag 01GD.** A morphism between `n`-coskeletal simplicial
> presheaves which is an isomorphism in degrees below `n` and locally surjective
> in degree `n` induces an isomorphism on every homology sheaf.

```lean
theorem isIso_sheafHomologyFunctor_map_of_coskeletal
    (J : GrothendieckTopology C) [HasSheafify J AddCommGrpCat.{w}]
    {L K : SimplicialObject (Cᵒᵖ ⥤ Type w)} (f : L ⟶ K) (n i : ℕ)
    (h_lt : ∀ j : ℕ, j < n → IsIso (f.app (op (SimplexCategory.mk j))))
    (h_surjective :
      Presheaf.IsLocallySurjective J (f.app (op (SimplexCategory.mk n))))
    (hL : IsIso ((SimplicialObject.coskAdj n).unit.app L))
    (hK : IsIso ((SimplicialObject.coskAdj n).unit.app K)) :
    IsIso ((sheafHomologyFunctor J i).map f)
```

## Tag 01GE, a lemma

[Tag 01GE](https://stacks.math.columbia.edu/tag/01GE) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Augmented.isZero_sheafHomology_of_isLocallySurjective_matchingMaps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/AugmentedAcyclicity.lean, line 566](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/AugmentedAcyclicity.lean#L566). The attribute's comment: “positive-degree vanishing”. References: SGA 4 V (7.3.2), “more general”.

> **Stacks Project, Tag 01GE (positive degrees).** An augmented simplicial presheaf whose
> degree-zero augmentation, relation map and matching maps are all locally surjective has zero
> homology sheaf in every positive degree.

```lean
theorem isZero_sheafHomology_of_isLocallySurjective_matchingMaps
    (J : GrothendieckTopology C) [HasSheafify J AddCommGrpCat.{w}]
    (K : SimplicialObject.Augmented (Cᵒᵖ ⥤ Type w))
    (h₀ : Presheaf.IsLocallySurjective J
      (K.hom.app (op (SimplexCategory.mk 0))))
    (h₁ : Presheaf.IsLocallySurjective J (edgesToFiberProduct K))
    (hmatching : ∀ n : ℕ, 1 ≤ n → Presheaf.IsLocallySurjective J
      (((SimplicialObject.coskAdj n).unit.app K.left).app
        (op (SimplexCategory.mk (n + 1)))))
    (i : ℕ) (hi : 0 < i) :
    IsZero (SimplicialObject.sheafHomology J K.left i)
```

**`CategoryTheory.SimplicialObject.Augmented.sheafHomologyZeroIso_of_isLocallySurjective_matchingMaps`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/AugmentedAcyclicity.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/AugmentedAcyclicity.lean#L586). The attribute's comment: “degree-zero identification”.

> **Stacks Project, Tag 01GE (degree zero).** The degree-zero homology sheaf of an augmented
> simplicial presheaf whose degree-zero augmentation, relation map and matching maps are all
> locally surjective is the free abelian sheaf on its presheaf of augmentation points.

```lean
noncomputable def sheafHomologyZeroIso_of_isLocallySurjective_matchingMaps
    (J : GrothendieckTopology C) [HasSheafify J AddCommGrpCat.{w}]
    (K : SimplicialObject.Augmented (Cᵒᵖ ⥤ Type w))
    (h₀ : Presheaf.IsLocallySurjective J
      (K.hom.app (op (SimplexCategory.mk 0))))
    (h₁ : Presheaf.IsLocallySurjective J (edgesToFiberProduct K))
    (hmatching : ∀ n : ℕ, 1 ≤ n → Presheaf.IsLocallySurjective J
      (((SimplicialObject.coskAdj n).unit.app K.left).app
        (op (SimplexCategory.mk (n + 1))))) :
    SimplicialObject.sheafHomology J K.left 0 ≅
      (Presheaf.freeAbelianSheaf J).obj K.right
```

## Tag 01GF, a lemma

[Tag 01GF](https://stacks.math.columbia.edu/tag/01GF) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isZero_sheafHomology_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectAcyclicity.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectAcyclicity.lean#L90). The attribute's comment: “positive-degree vanishing”. References: SGA 4 V (7.3.2), “3) positive degrees”.

> **Stacks Project, Tag 01GF (positive degrees).** The homology of the simplicial presheaf
> associated to a hypercovering vanishes in every positive degree.

```lean
theorem isZero_sheafHomology_of_isHypercovering (hK : IsHypercovering J K) (i : ℕ) (hi : 0 < i) :
    IsZero (SimplicialObject.sheafHomology J.toGrothendieck
      (SectionsOver.associatedSimplicialPresheaf.{w} K) i)
```

**`Stacks.CategoryTheory.Hypercovering.sheafHomologyZeroIso_of_isHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectAcyclicity.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectAcyclicity.lean#L100). The attribute's comment: “degree-zero identification”. References: SGA 4 V (7.3.2), “3) degree zero”.

> **Stacks Project, Tag 01GF (degree zero).** The degree-zero homology of the simplicial
> presheaf associated to a hypercovering is the free abelian sheaf on the represented object.

```lean
noncomputable def sheafHomologyZeroIso_of_isHypercovering (hK : IsHypercovering J K) :
    SimplicialObject.sheafHomology J.toGrothendieck
        (SectionsOver.associatedSimplicialPresheaf.{w} K) 0 ≅
      (presheafToSheaf J.toGrothendieck AddCommGrpCat.{max u v w}).obj
        (uliftYoneda.{max u w}.obj X ⋙ AddCommGrpCat.free.{max u v w})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.4, Tag 01GA](https://stacks.math.columbia.edu/tag/01GA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
