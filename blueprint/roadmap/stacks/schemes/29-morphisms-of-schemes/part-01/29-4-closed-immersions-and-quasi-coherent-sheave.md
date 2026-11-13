---
declaration: section
origin: cited
lean: Stacks.ClosedImmersion.pushforwardQcoh_exact, Stacks.ClosedImmersion.fullyFaithfulPushforwardQcoh, Stacks.ClosedImmersion.pushforwardQcoh_full, Stacks.ClosedImmersion.pushforwardQcoh_faithful, Stacks.ClosedImmersion.pushforwardQcoh_essImage_iff, AlgebraicGeometry.existsUnique_quasicoherentSubobject, Stacks.ClosedImmersion.quasicoherentUpperShriek, Stacks.ClosedImmersion.pushforwardQcohUpperShriekAdjunction
statement: formalized
proof: formalized
---

# 29.4 Closed immersions and quasi-coherent sheaves

Section 29.4 of the Stacks Project, [Tag 01QX](https://stacks.math.columbia.edu/tag/01QX). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01QY, a lemma

[Tag 01QY](https://stacks.math.columbia.edu/tag/01QY) in the Stacks Project.

**`Stacks.ClosedImmersion.pushforwardQcoh_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean#L102). The attribute's comment: “exactness”. References: EGA I (1.6.4), “closed immersion”.

> **[Stacks, Tag 01QY], exactness.** Direct image along a closed immersion is an exact functor
> on quasi-coherent modules.

```lean
theorem pushforwardQcoh_exact :
    exactFunctor (SheafOfModules.isQuasicoherent Z.ringCatSheaf).FullSubcategory
      (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory
      (Stacks.Modules.pushforwardQcoh i)
```

**`Stacks.ClosedImmersion.fullyFaithfulPushforwardQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean#L112). The attribute's comment: “full faithfulness”.

> **[Stacks, Tag 01QY], full faithfulness.** Direct image along a closed immersion is fully
> faithful on quasi-coherent modules: it is fully faithful on all modules, and the inclusion of
> the quasi-coherent modules is faithful.

```lean
def fullyFaithfulPushforwardQcoh : (Stacks.Modules.pushforwardQcoh i).FullyFaithful
```

**`Stacks.ClosedImmersion.pushforwardQcoh_full`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean#L123). The attribute's comment: “fullness”.

> **[Stacks, Tag 01QY], fullness.** Direct image along a closed immersion is full on
> quasi-coherent modules.

```lean
instance pushforwardQcoh_full : (Stacks.Modules.pushforwardQcoh i).Full
```

**`Stacks.ClosedImmersion.pushforwardQcoh_faithful`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean#L129). The attribute's comment: “faithfulness”.

> **[Stacks, Tag 01QY], faithfulness.** Direct image along a closed immersion is faithful on
> quasi-coherent modules.

```lean
instance pushforwardQcoh_faithful : (Stacks.Modules.pushforwardQcoh i).Faithful
```

**`Stacks.ClosedImmersion.pushforwardQcoh_essImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/Quasicoherent.lean#L136). The attribute's comment: “essential image”.

> **[Stacks, Tag 01QY], the essential image.** A quasi-coherent `𝒪_X`-module is a direct image
> of a quasi-coherent `𝒪_Z`-module exactly when the kernel of the comorphism of `i` annihilates it
> section by section, that is, when the ideal cutting out `Z` kills it.

```lean
theorem pushforwardQcoh_essImage_iff (G : X.Modules) (hG : G.IsQuasicoherent) :
    (Stacks.Modules.pushforwardQcoh i).essImage ⟨G, hG⟩ ↔
      ∀ (U : X.Opens) (a : Γ(X, U)), (i.app U).hom a = 0 → ∀ m : Γ(G, U), a • m = 0
```

## Tag 01QZ, a lemma

[Tag 01QZ](https://stacks.math.columbia.edu/tag/01QZ) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_quasicoherentSubobject`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LargestSubsheaf.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/LargestSubsheaf.lean#L81).

> A subobject of a quasi-coherent module on a scheme contains a unique
> quasi-coherent subobject through which every morphism from a quasi-coherent
> module factors uniquely.

```lean
public lemma existsUnique_quasicoherentSubobject (X : AlgebraicGeometry.Scheme.{u})
    (F : X.Modules) [F.IsQuasicoherent] (G : Subobject F) :
    ∃! G' : { G' : Subobject (G : X.Modules) // (G' : X.Modules).IsQuasicoherent },
      ∀ (H : X.Modules) [H.IsQuasicoherent],
        Function.Bijective (fun f : H ⟶ (G'.1 : X.Modules) ↦ f ≫ G'.1.arrow)
```

## Tag 01R0, a lemma

[Tag 01R0](https://stacks.math.columbia.edu/tag/01R0) in the Stacks Project.

**`Stacks.ClosedImmersion.quasicoherentUpperShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean#L91). The attribute's comment: “the functor”.

> **`i^!` for a closed immersion, on quasi-coherent modules.** It is the composite of the
> inclusion of quasi-coherent `𝒪_X`-modules, the right adjoint of direct image on all modules,
> and the coherator on `Z`.

```lean
def quasicoherentUpperShriek :
    (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherent Z.ringCatSheaf).FullSubcategory
```

**`Stacks.ClosedImmersion.pushforwardQcohUpperShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean#L100). The attribute's comment: “the adjunction”.

> **[Stacks, Tag 01R0].** Direct image of quasi-coherent modules along a closed immersion of
> schemes is left adjoint to `i^!`.

```lean
def pushforwardQcohUpperShriekAdjunction :
    Stacks.Modules.pushforwardQcoh i ⊣ quasicoherentUpperShriek i
```

**`Stacks.ClosedImmersion.pushforwardQcoh_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedPushforward/QuasicoherentAdjoint.lean#L112). The attribute's comment: “existence of the right adjoint”.

> **[Stacks, Tag 01R0], as an existence statement.** Direct image of quasi-coherent modules
> along a closed immersion of schemes has a right adjoint.

```lean
theorem pushforwardQcoh_isLeftAdjoint :
    (Stacks.Modules.pushforwardQcoh i).IsLeftAdjoint
```

## Tag 0C4I, a lemma

[Tag 0C4I](https://stacks.math.columbia.edu/tag/0C4I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.isClosedImmersion_inclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean#L65). The attribute's comment: “closed immersions into the two factors”.

> **Stacks Project, Tag 0C4I** and **Tag 0C4J.** An inclusion `I ≤ J` of quasi-coherent
> sheaves of ideals induces a closed immersion of the associated closed subschemes.
>
> Applied to `I ≤ I ⊔ J` and `J ≤ I ⊔ J` this gives the closed immersions of the scheme theoretic
> intersection into either of the two subschemes, and applied to `I ⊓ J ≤ I` and `I ⊓ J ≤ J` it
> gives the closed immersions of either subscheme into their scheme theoretic union.

```lean
instance isClosedImmersion_inclusion {X : Scheme.{u}} {I J : X.IdealSheafData} (h : I ≤ J) :
    IsClosedImmersion (inclusion h)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isPullback_subscheme_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean#L75). The attribute's comment: “cartesian intersection square”.

> The subscheme cut out by the sum of two ideal sheaves is the fibre product of the
> corresponding closed subschemes over the ambient scheme.

```lean
theorem isPullback_subscheme_sup (X : Scheme.{u}) (I J : X.IdealSheafData) :
    IsPullback (I.inclusion le_sup_left : (I ⊔ J).subscheme ⟶ I.subscheme)
      (J.inclusion le_sup_right : (I ⊔ J).subscheme ⟶ J.subscheme)
      I.subschemeι J.subschemeι
```

## Tag 0C4J, a lemma

[Tag 0C4J](https://stacks.math.columbia.edu/tag/0C4J) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.isClosedImmersion_inclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/ClosedImmersionIdealSheaves.lean#L65). The attribute's comment: “union\_closed\_immersions”.

> **Stacks Project, Tag 0C4I** and **Tag 0C4J.** An inclusion `I ≤ J` of quasi-coherent
> sheaves of ideals induces a closed immersion of the associated closed subschemes.
>
> Applied to `I ≤ I ⊔ J` and `J ≤ I ⊔ J` this gives the closed immersions of the scheme theoretic
> intersection into either of the two subschemes, and applied to `I ⊓ J ≤ I` and `I ⊓ J ≤ J` it
> gives the closed immersions of either subscheme into their scheme theoretic union.

```lean
instance isClosedImmersion_inclusion {X : Scheme.{u}} {I J : X.IdealSheafData} (h : I ≤ J) :
    IsClosedImmersion (inclusion h)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.unionIntersection_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/ClosedUnionExactSequence.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/ClosedUnionExactSequence.lean#L440). The attribute's comment: “union\_exact\_sequence”.

> **Stacks Project, Tag 0C4J.** The canonical sequence of structure sheaves of the
> scheme-theoretic union, the two closed subschemes and their scheme-theoretic intersection,
> whose last nonzero arrow is the difference of the two restriction maps, is short exact.

```lean
theorem unionIntersection_shortExact {S : Scheme.{u}} (I J : S.IdealSheafData) :
    ∃ zero : unionToBiprod I J ≫ biprodToIntersection I J = 0,
      (ShortComplex.mk (unionToBiprod I J) (biprodToIntersection I J) zero).ShortExact
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isPushout_subscheme_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/ClosedUnionPushout.lean, line 911](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/QuasiCoherent/ClosedUnionPushout.lean#L911). The attribute's comment: “union\_pushout”.

> The canonical square from the scheme-theoretic intersection of two closed subschemes
> to the two subschemes and then to their scheme-theoretic union is a pushout square.

```lean
theorem isPushout_subscheme_inf {S : Scheme.{u}} (I J : S.IdealSheafData) :
    IsPushout
      (Scheme.IdealSheafData.inclusion (I := I) (J := I ⊔ J) le_sup_left)
      (Scheme.IdealSheafData.inclusion (I := J) (J := I ⊔ J) le_sup_right)
      (Scheme.IdealSheafData.inclusion (I := I ⊓ J) (J := I) inf_le_left)
      (Scheme.IdealSheafData.inclusion (I := I ⊓ J) (J := J) inf_le_right)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.4, Tag 01QX](https://stacks.math.columbia.edu/tag/01QX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
