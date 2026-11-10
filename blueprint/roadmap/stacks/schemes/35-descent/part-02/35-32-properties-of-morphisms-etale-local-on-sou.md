---
declaration: section
origin: cited
lean: AlgebraicGeometry.targetIsLocallyNoetherian, AlgebraicGeometry.targetIsLocallyNoetherian_not_respectsRight_etale, AlgebraicGeometry.IsNoetherianOnSpecializations, AlgebraicGeometry.isNoetherianOnSpecializations_isLocalAtTarget, AlgebraicGeometry.isNoetherianOnSpecializations_isLocalAtSource, AlgebraicGeometry.ManyVariableExample.exists_commSq_isNoetherianOnSpecializations_not, AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget, AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.of_comp_etale
statement: formalized
proof: formalized
---

# 35.32 Properties of morphisms étale local on source-and-target

Section 35.32 of the Stacks Project, [Tag 04QW](https://stacks.math.columbia.edu/tag/04QW). 10 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04QX, an example

[Tag 04QX](https://stacks.math.columbia.edu/tag/04QX) in the Stacks Project.

**`AlgebraicGeometry.targetIsLocallyNoetherian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L91). The attribute's comment: “target_noetherian_property”.

> **Stacks Project, Tag 04QX.** The property of a morphism of schemes that its target is
> locally Noetherian.

```lean
abbrev targetIsLocallyNoetherian : CategoryTheory.MorphismProperty Scheme.{u}
```

**`AlgebraicGeometry.targetIsLocallyNoetherian_not_respectsRight_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L217). The attribute's comment: “target_noetherian_not_stable_under_etale_postcomposition”.

> The property that the target is locally Noetherian is not stable under postcomposition
> with an étale morphism.

```lean
theorem targetIsLocallyNoetherian_not_respectsRight_etale :
    ¬ (targetIsLocallyNoetherian : MorphismProperty Scheme.{u}).RespectsRight
        (@Etale : MorphismProperty Scheme.{u})
```

## Tag 04QY, an example

[Tag 04QY](https://stacks.math.columbia.edu/tag/04QY) in the Stacks Project.

**`AlgebraicGeometry.IsNoetherianOnSpecializations`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L97). The attribute's comment: “specialization_noetherian_property”.

> **Stacks Project, Tag 04QY.** Every specialization of a point in the image of a scheme
> morphism has a Noetherian local ring on the target.

```lean
abbrev IsNoetherianOnSpecializations {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.isNoetherianOnSpecializations_isLocalAtTarget`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L156). The attribute's comment: “etale_local_target”.

> The specialization-Noetherian property is local on the target for étale coverings.

```lean
instance isNoetherianOnSpecializations_isLocalAtTarget :
    MorphismProperty.IsLocalAtTarget
      (@IsNoetherianOnSpecializations : MorphismProperty Scheme.{u})
      Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isNoetherianOnSpecializations_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L187). The attribute's comment: “etale_local_source”.

> The specialization-Noetherian property is local on the source for étale coverings.

```lean
instance isNoetherianOnSpecializations_isLocalAtSource :
    MorphismProperty.IsLocalAtSource
      (@IsNoetherianOnSpecializations : MorphismProperty Scheme.{u})
      Scheme.etalePrecoverage
```

**`AlgebraicGeometry.ManyVariableExample.exists_commSq_isNoetherianOnSpecializations_not`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Noetherian.lean#L362). The attribute's comment: “counterexample”.

> **Stacks Project, Tag 04QY.** There is a commutative square with surjective étale vertical
> arrows whose top morphism has the specialization-Noetherian property while its bottom morphism
> does not. Together with étale locality on the source and on the target, this is the example's
> point: the two localities do not add up to locality on source-and-target.

```lean
theorem exists_commSq_isNoetherianOnSpecializations_not :
    ∃ (U V X Y : Scheme.{0}) (a : U ⟶ X) (b : V ⟶ Y) (h : U ⟶ V) (f : X ⟶ Y),
      a ≫ f = h ≫ b ∧ Surjective a ∧ Etale a ∧ Surjective b ∧ Etale b ∧
        IsNoetherianOnSpecializations h ∧ ¬ IsNoetherianOnSpecializations f
```

## Tag 04QZ, a definition

[Tag 04QZ](https://stacks.math.columbia.edu/tag/04QZ) in the Stacks Project.

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Defs.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Defs.lean#L46).

> A property of morphisms of schemes is étale local on the source and target if it is
> preserved by étale precomposition and étale base change, and can be checked in a commutative
> square of étale neighbourhoods around every point of the source.

```lean
structure IsEtaleLocalOnSourceAndTarget (P : MorphismProperty Scheme.{u}) : Prop
```

## Tag 04R0, a lemma

[Tag 04R0](https://stacks.math.columbia.edu/tag/04R0) in the Stacks Project.

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.of_comp_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean#L76). The attribute's comment: “cancel_etale”.

> An étale morphism can be cancelled on the right of a composite for a property which is
> étale local on the source and target.

```lean
lemma of_comp_etale {P : MorphismProperty Scheme.{u}}
    (hP : IsEtaleLocalOnSourceAndTarget P)
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : Etale g) (hfg : P (f ≫ g)) : P f
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.postcomp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean#L91). The attribute's comment: “postcompose_etale”.

> A property that is étale local on the source and target is preserved by postcomposition
> with an étale morphism.

```lean
theorem postcomp_of_etale (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P) {X Y Z : Scheme.{u}} (f : X ⟶ Y) (hf : P f)
    (g : Y ⟶ Z) (hg : Etale g) : P (f ≫ g)
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.isLocalAtSource_etalePrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean#L109). The attribute's comment: “local_source”.

> A morphism property étale local on the source and target is étale local on the source.

```lean
theorem isLocalAtSource_etalePrecoverage (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P) :
    P.IsLocalAtSource Scheme.etalePrecoverage
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.isLocalAtTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Basic.lean#L142). The attribute's comment: “local_target”.

> A property of scheme morphisms that is étale local on the source and target is étale local
> on the target.

```lean
theorem isLocalAtTarget (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P) :
    P.IsLocalAtTarget Scheme.etalePrecoverage
```

## Tag 04R1, a lemma

[Tag 04R1](https://stacks.math.columbia.edu/tag/04R1) in the Stacks Project.

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_forall_etale_diagrams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L62). The attribute's comment: “part (c)”.

> A property étale local on source and target holds iff it holds in every commuting square
> whose vertical maps are étale.

```lean
theorem iff_forall_etale_diagrams (hP : IsEtaleLocalOnSourceAndTarget P) :
    P f ↔
      ∀ {U V : Scheme.{u}} (a : U ⟶ X) (b : V ⟶ Y) (h : U ⟶ V),
        Etale a → Etale b → h ≫ b = a ≫ f → P h
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_exists_surjective_etale_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L74). The attribute's comment: “part (d)”.

> It suffices to test one commuting étale square whose map to the source is surjective.

```lean
theorem iff_exists_surjective_etale_diagram (hP : IsEtaleLocalOnSourceAndTarget P) :
    P f ↔
      ∃ (U V : Scheme.{u}) (a : U ⟶ X) (b : V ⟶ Y) (h : U ⟶ V),
        Etale a ∧ Etale b ∧ Function.Surjective a.base ∧
          h ≫ b = a ≫ f ∧ P h
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_exists_etale_target_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L101). The attribute's comment: “part (e)”.

> An étale-local property can be tested after an étale covering of the target.

```lean
theorem iff_exists_etale_target_cover (hP : IsEtaleLocalOnSourceAndTarget P) :
    P f ↔
      ∃ 𝒰 : Y.Cover.{u} Scheme.etalePrecoverage,
      ∀ i : 𝒰.I₀, P (pullback.fst (𝒰.f i) f)
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_exists_etale_source_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L118). The attribute's comment: “part (f)”.

> An étale-local property can be tested after an étale covering of the source.

```lean
theorem iff_exists_etale_source_cover (hP : IsEtaleLocalOnSourceAndTarget P) :
    P f ↔
      ∃ 𝒰 : X.Cover.{u} Scheme.etalePrecoverage,
      ∀ i : 𝒰.I₀, P (𝒰.f i ≫ f)
```

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_exists_bi_etale_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L134). The attribute's comment: “part (g)”.

> An étale-local property can be tested after covering the target and then the base-changed
> source by étale morphisms.

```lean
theorem iff_exists_bi_etale_covers (hP : IsEtaleLocalOnSourceAndTarget P) :
    P f ↔
      ∃ 𝒰 : Y.Cover.{u} Scheme.etalePrecoverage,
        ∀ i : 𝒰.I₀,
          ∃ 𝒱 : (pullback (𝒰.f i) f).Cover.{u} Scheme.etalePrecoverage,
            ∀ j : 𝒱.I₀, P (𝒱.f j ≫ pullback.fst (𝒰.f i) f)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_forall_exists_etale_neighborhood`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_forall_exists_etale_neighborhood#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Characterization.lean#L54) (StacksFrontier): “part (b)”.

## Tag 04R2, a lemma

[Tag 04R2](https://stacks.math.columbia.edu/tag/04R2) in the Stacks Project.

**`AlgebraicGeometry.isEtaleLocalOnSourceAndTarget_of_isLocalAtSource_isLocalAtTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Criterion.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Criterion.lean#L480).

> A morphism property that is étale local on each of the source and target separately,
> and is preserved by postcomposition with open immersions, is étale local on the source
> and target together.

```lean
theorem isEtaleLocalOnSourceAndTarget_of_isLocalAtSource_isLocalAtTarget
    (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.etalePrecoverage]
    [P.IsLocalAtTarget Scheme.etalePrecoverage]
    [P.RespectsRight (@IsOpenImmersion : MorphismProperty Scheme.{u})] :
    IsEtaleLocalOnSourceAndTarget P
```

## Tag 04R3, a remark

[Tag 04R3](https://stacks.math.columbia.edu/tag/04R3) in the Stacks Project.

**`AlgebraicGeometry.etale_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/EtaleLocalAtSource.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/EtaleLocalAtSource.lean#L69). The attribute's comment: “etale”. References: EGA IV (17.3.2), “partial”.

> **Stacks 04R3, the étale case.** Being an étale morphism of schemes is étale local on the
> source and target.
>
> The local criterion is reduced, through
> `AlgebraicGeometry.Etale.iff_flat_and_formallyUnramified`, to the flat and
> locally-of-finite-presentation cases of [Stacks Project, Tag 04R3] together with its unramified
> case, from which formal unramifiedness is extracted by [Stacks Project, Tag 02HE].

```lean
theorem etale_isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@Etale.{u} : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.LocallyOfFinitePresentation.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FinitePresentationLocalAtSource.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FinitePresentationLocalAtSource.lean#L82). The attribute's comment: “locally_finite_presentation”.

> Being a morphism of schemes locally of finite presentation is étale local on the source and
> target.

```lean
theorem LocallyOfFinitePresentation.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget
      (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.LocallyOfFiniteType.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FiniteTypeLocalAtSource.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FiniteTypeLocalAtSource.lean#L156). The attribute's comment: “locally finite type”.

> **Stacks Project, Tag 04R3, the case of being locally of finite type.** Being a morphism of
> schemes locally of finite type is étale local on the source and target.

```lean
theorem LocallyOfFiniteType.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget
      (@LocallyOfFiniteType : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.Flat.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FlatLocalAtSource.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FlatLocalAtSource.lean#L92). The attribute's comment: “flat”.

> **Stacks Project, Tag 04R3, flat case.** Being a flat morphism of schemes is étale local on
> the source and target.

```lean
theorem Flat.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@Flat : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.isEtaleLocalOnSourceAndTarget_gUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Properties.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Properties.lean#L523). The attribute's comment: “g_unramified”. References: EGA IV (17.3.2), “Remark 17.3.2(iii)”.

> **Stacks Project, Tag 04R3, item (10).** Being a G-unramified morphism of schemes is étale
> local on the source and target.
>
> This is the criterion of Tag 04R2 applied to G-unramifiedness: it is étale local on the source
> and on the target by the two instances above, and postcomposition with an open immersion
> preserves it. The source cites Tag 03YV for the first and Tag 02VM for the second; the two
> localities used here are the ones proved in this file, which is enough, since Tag 04R2 asks for
> étale locality only.

```lean
theorem isEtaleLocalOnSourceAndTarget_gUnramified :
    IsEtaleLocalOnSourceAndTarget (@GUnramified.{u} : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.locallyOfFiniteType_inf_locallyQuasiFinite_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/QuasiFiniteLocalAtSource.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/QuasiFiniteLocalAtSource.lean#L96). The attribute's comment: “locally quasi-finite”.

> **Stacks 04R3, the case of being locally quasi-finite.** Being a morphism of schemes
> locally of finite type and locally quasi-finite is étale local on the source and target.

```lean
theorem locallyOfFiniteType_inf_locallyQuasiFinite_isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget
      ((@LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
```

**`AlgebraicGeometry.Smooth.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/SmoothLocalAtSource.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/SmoothLocalAtSource.lean#L108). The attribute's comment: “smooth”. References: SGA 1 II (1.3), “special case”.

> **Stacks Project, Tag 04R3, smooth case.** Being a smooth morphism of schemes is étale
> local on the source and target.

```lean
theorem Smooth.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@Smooth : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.UniversallyOpen.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/UniversallyOpenLocalAtSource.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/UniversallyOpenLocalAtSource.lean#L57). The attribute's comment: “universally open”. References: SGA 4 IV (8.5.5), “special case”.

> Being a universally open morphism of schemes is étale local on the source and target.

```lean
theorem UniversallyOpen.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@UniversallyOpen : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.Unramified.isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/UnramifiedLocalAtSource.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/UnramifiedLocalAtSource.lean#L168). The attribute's comment: “unramified”.

> **Stacks Project, Tag 04R3, unramified case.** Being an unramified morphism of schemes is
> étale local on the source and target.
>
> This is the formal half of Tag 04R2 applied to unramifiedness: it is local on the source for the
> étale topology by the instance above, stable under arbitrary base change by Tag 02GA, and
> preserved by postcomposition with an étale morphism.

```lean
theorem Unramified.isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@Unramified : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.syntomic_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L109). The attribute's comment: “syntomic”.

> **Stacks Project, Tag 04R3, syntomic case.** Being a syntomic morphism of schemes is étale
> local on the source and target.
>
> The geometric content of Tag 04R2 is not needed: postcomposition with an étale morphism
> preserves syntomicity outright, by `AlgebraicGeometry.Syntomic.respectsRight_etale`, and base
> change is Tag 01UI. The local criterion comes from étale source-locality of syntomic morphisms
> of schemes, `AlgebraicGeometry.Syntomic.isLocalAtSource_etalePrecoverage`.

```lean
theorem syntomic_isEtaleLocalOnSourceAndTarget :
    IsEtaleLocalOnSourceAndTarget (@Syntomic.{u} : MorphismProperty Scheme.{u})
```

## Tag 0CEZ, a lemma

[Tag 0CEZ](https://stacks.math.columbia.edu/tag/0CEZ) in the Stacks Project.

**`AlgebraicGeometry.mem_largestOpen_iff_of_etaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpenEtaleSquare.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpenEtaleSquare.lean#L107).

> **Stacks Project, Tag 0CEZ.** Étale morphisms on both sides of a commutative square preserve
> membership in the largest open locus of a property étale local on the source and target.

```lean
public theorem mem_largestOpen_iff_of_etaleAt
    (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P)
    {X' X Y' Y : Scheme.{u}}
    (f : X ⟶ Y) (f' : X' ⟶ Y') (g : Y' ⟶ Y) (g' : X' ⟶ X)
    (hcomm : g' ≫ f = f' ≫ g) (x' : X')
    (hg' : EtaleAt g' x')
    (hg : EtaleAt g (f'.base x')) :
    g'.base x' ∈ largestOpen P f ↔ x' ∈ largestOpen P f'
```

## Tag 0CF0, a lemma

[Tag 0CF0](https://stacks.math.columbia.edu/tag/0CF0) in the Stacks Project.

**`MvPolynomial.eq_univ_or_finite_compl_of_invariant_coordinateShear`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/AffineSpaceOrbits.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/AffineSpaceOrbits.lean#L401).

> A nonempty open subset of affine `n`-space, for `n ≥ 2`, invariant under
> every elementary coordinate shear, is either all of affine space or has finite
> complement consisting of closed points whose coordinates are algebraic over
> the prime field (and in the latter case the field has positive characteristic).

```lean
lemma eq_univ_or_finite_compl_of_invariant_coordinateShear
    {k : Type*} [Field k] {n : ℕ} (hn : 2 ≤ n)
    (W : Set (PrimeSpectrum (MvPolynomial (Fin n) k)))
    (hWopen : IsOpen W) (hWnonempty : W.Nonempty)
    (hWinv : ∀ (i j : Fin n) (hij : i ≠ j) (d : ℕ),
      PrimeSpectrum.comap (coordinateShear (R := k) i j hij d).toRingHom ⁻¹' W = W) :
    W = Set.univ ∨
      (0 < ringChar k ∧ Wᶜ.Finite ∧ ∀ q ∈ Wᶜ, q.asIdeal.IsMaximal ∧
        ∃ ι : ZMod (ringChar k) →+* q.asIdeal.ResidueField,
          ∀ i : Fin n, @IsIntegral (ZMod (ringChar k)) q.asIdeal.ResidueField _ _ ι.toAlgebra
            (algebraMap (MvPolynomial (Fin n) k) q.asIdeal.ResidueField
            (MvPolynomial.X i)))
```

## Tag 0CF1, a lemma

[Tag 0CF1](https://stacks.math.columbia.edu/tag/0CF1) in the Stacks Project.

**`AlgebraicGeometry.mem_largestOpen_iff_of_smoothAt_etaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpenSmoothSquare.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpenSmoothSquare.lean#L634).

> **Stacks Project, Tag 0CF1.** If the right vertical morphism of a commutative square is
> smooth at the relevant point and the comparison morphism to the fibre product is étale at the
> chosen point, the two source points lie in their largest open loci simultaneously.

```lean
public theorem mem_largestOpen_iff_of_smoothAt_etaleAt
    (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.etalePrecoverage]
    [P.IsLocalAtTarget
      (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))]
    [P.RespectsRight (@IsOpenImmersion : MorphismProperty Scheme.{u})]
    {X' X Y' Y : Scheme.{u}}
    (f : X ⟶ Y) (f' : X' ⟶ Y') (g : Y' ⟶ Y) (g' : X' ⟶ X)
    (hcomm : g' ≫ f = f' ≫ g) (x' : X')
    (hg : InfinitesimalLifting.SmoothAt g (f'.base x'))
    (hg' : EtaleAt
      (pullback.lift g' f' hcomm) x') :
    g'.base x' ∈ AlgebraicGeometry.largestOpen P f ↔
      x' ∈ AlgebraicGeometry.largestOpen P f'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.32, Tag 04QW](https://stacks.math.columbia.edu/tag/04QW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
