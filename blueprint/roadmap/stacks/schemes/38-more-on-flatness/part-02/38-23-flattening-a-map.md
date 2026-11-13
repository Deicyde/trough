---
declaration: section
origin: cited
lean: AlgebraicGeometry.mono_pullbackPushforwardUnit_of_relativeAssassin_subset_range, AlgebraicGeometry.mono_baseChange_pullbackPushforwardUnit_of_relativeAssassin_subset_range, Module.exists_ideal_bijective_rTensor_iff_map_eq_bot, Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor_finitePresentation, Stacks.Flatness.weilRestriction_representableBy_closedImmersion_of_affineTests, Stacks.Flatness.finitePresentation_hom_of_representableBy_weilRestrictionFunctor
statement: formalized
proof: formalized
---

# 38.23 Flattening a map

Section 38.23 of the Stacks Project, [Tag 05PC](https://stacks.math.columbia.edu/tag/05PC). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05PD, a lemma

[Tag 05PD](https://stacks.math.columbia.edu/tag/05PD) in the Stacks Project.

**`AlgebraicGeometry.mono_pullbackPushforwardUnit_of_relativeAssassin_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean#L88). The attribute's comment: “injectivity”.

> **Stacks Project, Tag 05PD.** Let `S` be a scheme, let `g : X' ⟶ X` be a flat morphism of
> schemes over `S` with `X` locally of finite type over `S`, and let `F` be a finite type
> quasi-coherent `𝒪_X`-module which is flat over `S`. If `Ass_{X/S}(F) ⊆ g(X')`, then the
> canonical map `F ⟶ g_* g^* F` is injective.

```lean
theorem mono_pullbackPushforwardUnit_of_relativeAssassin_subset_range
    {X' X S : Scheme.{u}} (f : X ⟶ S) (g : X' ⟶ X)
    [LocallyOfFiniteType f] [Flat g]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hF : IsFlatOver f.toLRSHom.toShHom F)
    (hAss : Stacks.Divisors.relativeAssassin f F ⊆ Set.range g.base) :
    Mono ((Scheme.Modules.pullbackPushforwardAdjunction g).unit.app F)
```

**`AlgebraicGeometry.mono_baseChange_pullbackPushforwardUnit_of_relativeAssassin_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean#L102). The attribute's comment: “after arbitrary base change”.

> **Stacks Project, Tag 05PD.** The canonical map of the preceding statement remains injective
> after an arbitrary base change `h : T ⟶ S`: the map
> `F_T ⟶ (g_T)_* (g_T)^* F_T` on `X ×_S T` is injective as well.

```lean
theorem mono_baseChange_pullbackPushforwardUnit_of_relativeAssassin_subset_range
    {X' X S : Scheme.{u}} (f : X ⟶ S) (g : X' ⟶ X)
    [LocallyOfFiniteType f] [Flat g]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hF : IsFlatOver f.toLRSHom.toShHom F)
    (hAss : Stacks.Divisors.relativeAssassin f F ⊆ Set.range g.base) :
    ∀ (T : Scheme.{u}) (h : T ⟶ S),
      Mono ((Scheme.Modules.pullbackPushforwardAdjunction (compBaseChangeMap f g h)).unit.app
        ((Scheme.Modules.pullback (pullback.fst f h)).obj F))
```

## Tag 05PE, a lemma

[Tag 05PE](https://stacks.math.columbia.edu/tag/05PE) in the Stacks Project.

**`Module.exists_ideal_bijective_rTensor_iff_map_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean#L91).

> **Stacks Project, Tag 05PE.** A surjection from a projective module has a
> flattening ideal: after every base change, the map is an isomorphism exactly
> when the image of this ideal vanishes.

```lean
theorem exists_ideal_bijective_rTensor_iff_map_eq_bot
    (u : M →ₗ[A] N) (hu : Function.Surjective u) [Module.Projective A M] :
    ∃ I : Ideal A, ∀ (B : Type*) [CommRing B] [Algebra A B],
      Function.Bijective (u.rTensor B) ↔ Ideal.map (algebraMap A B) I = ⊥
```

## Tag 05PF, a theorem

[Tag 05PF](https://stacks.math.columbia.edu/tag/05PF) in the Stacks Project.

**`Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean#L188). The attribute's comment: “both assertions: representability by a closed immersion, which is of finite presentation when `G` is”.

> **Stacks Project, Tag 05PF.** Let `f : X ⟶ S` be a morphism of finite presentation (locally
> of finite presentation, quasi-compact and quasi-separated, Tag 01TP) and let `u : F ⟶ G` be a
> surjection of quasi-coherent modules on `X` with `F` of finite presentation, flat over `S` and
> pure relative to `S`.  Then the functor `F_iso` on schemes over `S`, whose value at
> `T` is a point exactly when the base change `u_T` is an isomorphism, is represented by a closed
> immersion `Z ⟶ S`; moreover `Z ⟶ S` is of finite presentation if `G` is of finite presentation.
>
> The representing closed immersion comes from the étale-local devissage
> `Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor`: purity reduces the
> question étale locally on `S` to an affine situation with projective sections, cut out by the
> flattening ideal of Tag 05PE, and the local closed subschemes glue by fpqc descent (Tags 05MJ,
> 03I0).  Its finite presentation is
> `Stacks.Flatness.finitePresentation_hom_of_representableBy_isomorphismFunctor`, from Tag 05MJ(4)
> and Tag 05LX.
>
> The instance `F.IsFiniteType` is part of the statement because purity relative to `S` is phrased
> for modules of finite type; it follows from `F.IsFinitePresentation` by
> `Stacks.AlgebraicGeometry.CoherentTFAE.isQuasicoherent_isFiniteType_of_isFinitePresentation`, so
> it adds nothing to the source's assumptions.

```lean
theorem exists_closedImmersion_representableBy_isomorphismFunctor_finitePresentation
    (D : ModuleMapBaseChangeSituation.{u})
    [LocallyOfFinitePresentation D.f] [QuasiCompact D.f] [QuasiSeparated D.f]
    [D.F.IsFinitePresentation] [D.F.IsFiniteType] [Epi D.hom]
    (hflat : IsFlatOver D.f.toLRSHom.toShHom D.F)
    (hpure : IsPureRelative D.f D.F) :
    ∃ W : Over D.S, IsClosedImmersion W.hom ∧
      Nonempty (D.isomorphismFunctor.RepresentableBy W) ∧
      (D.G.IsFinitePresentation → FinitePresentation W.hom)
```

## Tag 07AI, a lemma

[Tag 07AI](https://stacks.math.columbia.edu/tag/07AI) in the Stacks Project.

**`Stacks.Flatness.weilRestriction_representableBy_closedImmersion_of_affineTests`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean#L434). The attribute's comment: “representability by a closed immersion”.

> **Stacks Project, Tag 07AI.** The Weil restriction `f_* Y` of a closed subscheme `Y` of `X`
> along a morphism `f : X ⟶ S` which is of finite presentation, flat and pure is represented by a
> closed immersion `Z ⟶ S`.
>
> By the equivalence
> `Stacks.Flatness.WeilRestriction.isIsomorphismAfterBaseChange_iff_isIso_closedSubschemeBaseChange`
> the functor is the isomorphism functor of the surjection `u : 𝒪_X ⟶ 𝒪_X/I` cutting out `Y`, whose
> hypotheses in Tag 05PF are exactly the ones assumed here: `𝒪_X` is of finite type and of finite
> presentation over itself, it is flat over `S` because `f` is flat, and it is pure relative to `S`
> because `X` is.

```lean
theorem weilRestriction_representableBy_closedImmersion_of_affineTests
    (i : Y ⟶ X) (f : X ⟶ S) [IsClosedImmersion i]
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f] [Flat f]
    (hpure : AlgebraicGeometry.IsSchemePureRelative f) :
    ∃ W : Over S, IsClosedImmersion W.hom ∧
      Nonempty ((weilRestrictionFunctor i f).RepresentableBy W)
```

**`Stacks.Flatness.finitePresentation_hom_of_representableBy_weilRestrictionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean#L469). The attribute's comment: “finite presentation of the representing closed immersion”. References: SGA 3 VIB (6.2.3), “(ii)”; SGA 3 VIB (6.5.2), “special case”; SGA 3 XI (6.8), “special case”.

> **Stacks Project, Tag 07AI.** If the closed subscheme `Y` is of finite presentation over `S`,
> every closed immersion representing the Weil restriction `f_* Y` is of finite presentation.
>
> The quotient `𝒪_X/I` is then of finite presentation, by Tag 01TV and
> `Stacks.Flatness.WeilRestriction.isFinitePresentation_pushforwardUnit`, which is the hypothesis
> Tag 05PF's second assertion needs; the assertion itself is
> `Stacks.Flatness.finitePresentation_hom_of_representableBy_isomorphismFunctor`, and needs no
> flattening ideal.  Unlike the first assertion this one constructs no representative: it applies
> to any representing closed immersion, and such a one exists by the first assertion.

```lean
theorem finitePresentation_hom_of_representableBy_weilRestrictionFunctor
    (i : Y ⟶ X) (f : X ⟶ S) [IsClosedImmersion i]
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (hY : AlgebraicGeometry.FinitePresentation (i ≫ f))
    {Z : Scheme.{u}} (p : Z ⟶ S) [AlgebraicGeometry.IsClosedImmersion p]
    (e : (weilRestrictionFunctor i f).RepresentableBy (Over.mk p)) :
    AlgebraicGeometry.FinitePresentation p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.23, Tag 05PC](https://stacks.math.columbia.edu/tag/05PC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
