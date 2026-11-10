---
declaration: section
origin: cited
lean: AlgebraicGeometry.mono_pullbackPushforwardUnit_of_relativeAssassin_subset_range, AlgebraicGeometry.mono_baseChange_pullbackPushforwardUnit_of_relativeAssassin_subset_range, Module.exists_ideal_bijective_rTensor_iff_map_eq_bot, Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor, Stacks.Flatness.isomorphismFunctor_representableBy_closedImmersion_of_affineTests, Stacks.Flatness.finitePresentation_hom_of_representableBy_isomorphismFunctor, Stacks.Flatness.isomorphismFunctor_representableBy_closedImmersion_of_projective_sections, Stacks.Flatness.weilRestriction_representableBy_closedImmersion_of_affineTests
statement: formalized
proof: formalized
---

# 38.23 Flattening a map

Section 38.23 of the Stacks Project, [Tag 05PC](https://stacks.math.columbia.edu/tag/05PC). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05PD, a lemma

[Tag 05PD](https://stacks.math.columbia.edu/tag/05PD) in the Stacks Project.

**`AlgebraicGeometry.mono_pullbackPushforwardUnit_of_relativeAssassin_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean#L88). The attribute's comment: “injectivity”.

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

**`AlgebraicGeometry.mono_baseChange_pullbackPushforwardUnit_of_relativeAssassin_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningInjective.lean#L102). The attribute's comment: “after arbitrary base change”.

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

**`Module.exists_ideal_bijective_rTensor_iff_map_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean#L91).

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

**`Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/EtaleLocalRepresentability.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/EtaleLocalRepresentability.lean#L638). The attribute's comment: “representability by a closed immersion”.

> **Stacks Project, Tag 05PF, first assertion.** Let `f : X ⟶ S` be of finite presentation and
> let `u : F ⟶ G` be a surjection of quasi-coherent modules on `X` with `F` of finite presentation,
> flat over `S` and pure relative to `S`.  Then the locus where `u` becomes an isomorphism after
> base change is represented by a closed immersion into `S`.
>
> The source's devissage: purity reduces the question, étale locally on `S`, to an affine situation
> whose module of sections is projective, where the locus is cut out by the flattening ideal of Tag
> 05PE; the étale base changes cover `S` in the fpqc topology and the functor is an fpqc sheaf, so
> the local closed subschemes glue.

```lean
theorem exists_closedImmersion_representableBy_isomorphismFunctor
    (D : ModuleMapBaseChangeSituation.{u})
    [LocallyOfFinitePresentation D.f] [QuasiCompact D.f] [QuasiSeparated D.f]
    [D.F.IsFinitePresentation] [D.F.IsFiniteType] [Epi D.hom]
    (hflat : IsFlatOver D.f.toLRSHom.toShHom D.F)
    (hpure : AlgebraicGeometry.IsPureRelative D.f D.F) :
    ∃ W : Over D.S, IsClosedImmersion W.hom ∧
      Nonempty (D.isomorphismFunctor.RepresentableBy W)
```

**`Stacks.Flatness.isomorphismFunctor_representableBy_closedImmersion_of_affineTests`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean#L121). The attribute's comment: “representability by a closed immersion”.

> **Stacks Project, Tag 05PF.** The isomorphism-after-base-change functor of a surjection from
> a finitely presented, flat and pure module is represented by a closed immersion into the base.
>
> The representing closed subscheme is cut out by an ideal sheaf which it suffices to exhibit on
> *affine* schemes over the base, by
> `Stacks.Flatness.ModuleMapBaseChangeSituation.isFlatteningIdeal_of_isFlatteningIdealOnAffines`;
> étale localization on the base reduces the construction to an affine situation whose module of
> sections is projective, where the ideal sheaf is the flattening ideal of Tag 05PE.  That
> devissage is
> `Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor`.

```lean
theorem isomorphismFunctor_representableBy_closedImmersion_of_affineTests
    (D : ModuleMapBaseChangeSituation.{u})
    [LocallyOfFinitePresentation D.f] [QuasiCompact D.f] [QuasiSeparated D.f]
    [D.F.IsFinitePresentation] [D.F.IsFiniteType] [Epi D.hom]
    (hflat : IsFlatOver D.f.toLRSHom.toShHom D.F)
    (hpure : IsPureRelative D.f D.F) :
    ∃ W : Over D.S, IsClosedImmersion W.hom ∧
      Nonempty (D.isomorphismFunctor.RepresentableBy W)
```

**`Stacks.Flatness.finitePresentation_hom_of_representableBy_isomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusAffineTests.lean#L147). The attribute's comment: “finite presentation of the representing closed immersion”.

> **Stacks Project, Tag 05PF.** A closed immersion `Z ⟶ S` representing the
> isomorphism-after-base-change functor is of finite presentation as soon as the target module `G`
> is of finite presentation.
>
> Local finite presentation is Tag 01ZC: by Tag 05MJ(4) the isomorphism functor turns a cofiltered
> inverse limit of affine schemes over the base into a filtered colimit, so the functor of points
> of `Z` is limit preserving in the sense of Tag 05LX.  Quasi-compactness holds because a closed
> immersion is an affine morphism, and quasi-separatedness because the functor is subterminal, so
> that `Z ⟶ S` is a monomorphism.
>
> The hypotheses are about the morphism `i` at hand, and they are satisfiable: a closed immersion
> representing the functor exists under the source's own hypotheses, by
> `Stacks.Flatness.isomorphismFunctor_representableBy_closedImmersion_of_affineTests`.  Stating the
> assertion for an arbitrary representative rather than for that one is no weaker, since any two
> representatives of a functor are isomorphic over the base.

```lean
theorem finitePresentation_hom_of_representableBy_isomorphismFunctor
    (D : ModuleMapBaseChangeSituation.{u}) [QuasiCompact D.f]
    [D.F.IsFiniteType] [D.G.IsFinitePresentation]
    {Z : Scheme.{u}} (i : Z ⟶ D.S) [IsClosedImmersion i]
    (e : D.isomorphismFunctor.RepresentableBy (Over.mk i)) :
    FinitePresentation i
```

**`Stacks.Flatness.isomorphismFunctor_representableBy_closedImmersion_of_projective_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusProjectiveSections.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/IsoLocusProjectiveSections.lean#L419). The attribute's comment: “representability by a closed immersion, for an affine situation whose source module has projective global sections: this is the terminal case of the source's devissage, Step 4 of its proof together with Tag 05PE. The étale localization of Steps 1-3, which reduces the general case to this one, is `Stacks.Flatness.exists_closedImmersion_representableBy_isomorphismFunctor`”. References: SGA 3 VIB (6.2.3), “(i), special case”; SGA 3 VIII (6.4), “special case”.

> **Stacks Project, Tag 05PF.** The isomorphism-after-base-change functor of a surjection
> `u : F ⟶ G` of quasi-coherent modules on an affine scheme `X` over an affine base `S`, whose
> source has projective module of global sections over `Γ(S, 𝒪_S)`, is represented by a closed
> immersion `Z ⟶ S`.
>
> This is the situation in which the devissage of the source's proof terminates: the representing
> closed subscheme is cut out by the ideal of `Γ(S, 𝒪_S)` supplied by Tag 05PE, which after every
> base change vanishes exactly when `u` becomes an isomorphism.  The hypotheses of the source — that
> `f` and `F` be of finite presentation and that `F` be flat and pure relative to `S` — are what the
> source's étale localization uses to reduce the general case to this one; they are not needed once
> the situation is affine with projective sections, and are therefore absent here.

```lean
theorem isomorphismFunctor_representableBy_closedImmersion_of_projective_sections
    (D : ModuleMapBaseChangeSituation.{u}) [IsAffine D.X] [IsAffine D.S] [Epi D.hom]
    (hproj : letI : Module Γ(D.S, ⊤) Γ(D.F, ⊤) := Module.compHom Γ(D.F, ⊤) D.f.appTop.hom
      Module.Projective Γ(D.S, ⊤) Γ(D.F, ⊤)) :
    ∃ W : Over D.S, IsClosedImmersion W.hom ∧
      Nonempty (D.isomorphismFunctor.RepresentableBy W)
```

## Tag 07AI, a lemma

[Tag 07AI](https://stacks.math.columbia.edu/tag/07AI) in the Stacks Project.

**`Stacks.Flatness.weilRestriction_representableBy_closedImmersion_of_affineTests`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean#L434). The attribute's comment: “representability by a closed immersion”.

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

**`Stacks.Flatness.finitePresentation_hom_of_representableBy_weilRestrictionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningFunctor/WeilRestriction.lean#L469). The attribute's comment: “finite presentation of the representing closed immersion”. References: SGA 3 VIB (6.2.3), “(ii)”; SGA 3 VIB (6.5.2), “special case”; SGA 3 XI (6.8), “special case”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
