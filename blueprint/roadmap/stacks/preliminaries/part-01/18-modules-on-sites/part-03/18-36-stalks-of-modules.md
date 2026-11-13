---
declaration: section
origin: cited
lean: CategoryTheory.Precoverage.Point.isIso_stalkSheafificationComparison, CategoryTheory.Precoverage.Point.sheafStalk_exact_preservesColimits, CategoryTheory.Precoverage.Point.presheafStalk_exact_preservesColimits, Stacks.exactFunctor_abelianSheafFiber, Stacks.exactFunctor_abelianPresheafFiber, Stacks.isIso_abelianPresheafFiber_map_toSheafify, CategoryTheory.GrothendieckTopology.SitePoint.exactFunctor_abelianSheafStalk, CategoryTheory.GrothendieckTopology.SitePoint.exactFunctor_abelianPresheafStalk
statement: formalized
proof: formalized
---

# 18.36 Stalks of modules

Section 18.36 of the Stacks Project, [Tag 04EM](https://stacks.math.columbia.edu/tag/04EM). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04EN, a lemma

[Tag 04EN](https://stacks.math.columbia.edu/tag/04EN) in the Stacks Project.

**`CategoryTheory.Precoverage.Point.isIso_stalkSheafificationComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean#L194). The attribute's comment: “(1), for a point of a site in the source's sense (Tag 00Y5)”.

> **Stacks 04EN (1).** For a point `p` of the site `(C, K)`, the canonical map `F_p → (F^#)_p`
> from the stalk of a presheaf of sets to the stalk of its sheafification is an isomorphism,
> naturally in `F`.

```lean
theorem isIso_stalkSheafificationComparison : IsIso p.stalkSheafificationComparison
```

**`CategoryTheory.Precoverage.Point.sheafStalk_exact_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean#L230). The attribute's comment: “(2), for a point of a site in the source's sense (Tag 00Y5)”.

> **Stacks 04EN (2).** For a point `p` of the site `(C, K)`, the stalk functor
> `Sh(C) ⥤ Sets`, `F ↦ F_p`, is exact (it commutes with finite limits and finite colimits) and
> commutes with arbitrary colimits.

```lean
theorem sheafStalk_exact_preservesColimits :
    (PreservesFiniteLimits p.sheafStalk ∧ PreservesFiniteColimits p.sheafStalk) ∧
      PreservesColimitsOfSize.{w', w''} p.sheafStalk
```

**`CategoryTheory.Precoverage.Point.presheafStalk_exact_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean#L240). The attribute's comment: “(3), for a point of a site in the source's sense (Tag 00Y5)”.

> **Stacks 04EN (3).** For a point `p` of the site `(C, K)`, the stalk functor
> `PSh(C) ⥤ Sets`, `F ↦ F_p`, is exact (it commutes with finite limits and finite colimits) and
> commutes with arbitrary colimits.

```lean
theorem presheafStalk_exact_preservesColimits :
    (PreservesFiniteLimits p.presheafStalk ∧ PreservesFiniteColimits p.presheafStalk) ∧
      PreservesColimitsOfSize.{w', w''} p.presheafStalk
```

## Tag 04EP, a lemma

[Tag 04EP](https://stacks.math.columbia.edu/tag/04EP) in the Stacks Project.

**`Stacks.exactFunctor_abelianSheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean#L62). The attribute's comment: “(1) for Mathlib's points of a site (SGA 4 IV 6.3 fibre functors)”.

> **Stacks Project, Tag 04EP, part (1).** Taking the stalk at a point of a site in
> Mathlib's sense (`GrothendieckTopology.Point`) is an exact functor from abelian sheaves to
> abelian groups.

```lean
theorem exactFunctor_abelianSheafFiber :
    exactFunctor (Sheaf J AddCommGrpCat.{w}) AddCommGrpCat.{w}
      (Φ.sheafFiber (A := AddCommGrpCat.{w}))
```

**`Stacks.exactFunctor_abelianPresheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean#L71). The attribute's comment: “(2) for Mathlib's points of a site (SGA 4 IV 6.3 fibre functors)”.

> **Stacks Project, Tag 04EP, part (2).** Taking the stalk at a point of a site in
> Mathlib's sense (`GrothendieckTopology.Point`) is an exact functor from abelian presheaves to
> abelian groups.

```lean
theorem exactFunctor_abelianPresheafFiber :
    exactFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{w}) AddCommGrpCat.{w}
      (Φ.presheafFiber (A := AddCommGrpCat.{w}))
```

**`Stacks.isIso_abelianPresheafFiber_map_toSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExact.lean#L82). The attribute's comment: “(3) for Mathlib's points of a site (SGA 4 IV 6.3 fibre functors)”.

> **Stacks Project, Tag 04EP, part (3).** Sheafification of an abelian presheaf `F` does not
> change its stalk: the stalk at `Φ` of the canonical map `F ⟶ F^#` is an isomorphism
> `F_p ≅ (F^#)_p`.

```lean
theorem isIso_abelianPresheafFiber_map_toSheafify [HasWeakSheafify J AddCommGrpCat.{w}]
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{w}) :
    IsIso ((Φ.presheafFiber (A := AddCommGrpCat.{w})).map (toSheafify J F))
```

**`CategoryTheory.GrothendieckTopology.SitePoint.exactFunctor_abelianSheafStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean#L312). The attribute's comment: “(1)”.

> **Stacks 04EP, part (1).** For a point `p` of a site, the stalk functor
> `Ab(C) ⥤ Ab`, `F ↦ F_p`, is exact.

```lean
theorem exactFunctor_abelianSheafStalk :
    exactFunctor (Sheaf J AddCommGrpCat.{w}) AddCommGrpCat.{w}
      (sheafToPresheaf J AddCommGrpCat.{w} ⋙ elementColimit p.fiber AddCommGrpCat.{w})
```

**`CategoryTheory.GrothendieckTopology.SitePoint.exactFunctor_abelianPresheafStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean#L320). The attribute's comment: “(2)”.

> **Stacks 04EP, part (2).** For a point `p` of a site, the stalk functor
> `PAb(C) ⥤ Ab`, `F ↦ F_p`, is exact.

```lean
theorem exactFunctor_abelianPresheafStalk :
    exactFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{w}) AddCommGrpCat.{w}
      (elementColimit p.fiber AddCommGrpCat.{w})
```

**`CategoryTheory.GrothendieckTopology.SitePoint.isIso_abelianPresheafStalk_map_toSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean#L328). The attribute's comment: “(3)”.

> **Stacks 04EP, part (3).** For a point `p` of a site and an abelian presheaf `F`, the stalk
> at `p` of the canonical map `F ⟶ F^#` is an isomorphism `F_p ≅ (F^#)_p`.

```lean
theorem isIso_abelianPresheafStalk_map_toSheafify (F : Cᵒᵖ ⥤ AddCommGrpCat.{w}) :
    IsIso ((elementColimit p.fiber AddCommGrpCat.{w}).map (CategoryTheory.toSheafify J F))
```

## Tag 04EQ, a lemma

[Tag 04EQ](https://stacks.math.columbia.edu/tag/04EQ) in the Stacks Project.

**`Stacks.exactFunctor_presheafModuleFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkPresheafExact.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkPresheafExact.lean#L54). The attribute's comment: “part (2)”.

> **Stacks 04EQ, part (2).** Taking the stalk at a point of a site is an exact functor from
> presheaves of `R`-modules to modules over the stalk of `R`.

```lean
theorem exactFunctor_presheafModuleFiber :
    exactFunctor (PresheafOfModules.{w} R)
      (ModuleCat.{w} ((Φ.presheafFiber (A := RingCat.{w})).obj R))
      (presheafModuleFiber Φ R)
```

**`Stacks.exactFunctor_sheafModuleFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkSheafExact.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkSheafExact.lean#L63). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 04EQ, part (1).** Taking the stalk at a point of a site is an exact
> functor from sheaves of `R`-modules to modules over the stalk of `R`.

```lean
theorem exactFunctor_sheafModuleFiber :
    exactFunctor (SheafOfModules.{w} R)
      (ModuleCat.{w} ((Φ.presheafFiber (A := RingCat.{w})).obj R.obj))
      (sheafModuleFiber Φ R)
```

**`Stacks.isIso_moduleFiberSheafificationComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkSheafExact.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ModuleStalkSheafExact.lean#L113). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 04EQ, part (3).** Sheafification of a presheaf of modules does not
> change its module-valued stalk.

```lean
theorem isIso_moduleFiberSheafificationComparison :
    IsIso (moduleFiberSheafificationComparison Φ R)
```

## Tag 05V5, a lemma

[Tag 05V5](https://stacks.math.columbia.edu/tag/05V5) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.pullbackModulesSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackModulesComp.lean#L141). The attribute's comment: “the formula, for a commutative square of morphisms of ringed topoi; the square over a point `p` and the point `q = f ∘ p` is not constructed”.

> **The formula of Stacks 05V5.** Let
>
> ```
>   P ⟶ X
>   ↓     ↓
>   Q ⟶ Y
> ```
>
> be a commutative square of morphisms of ringed topoi — the hypothesis `h` says that the two
> composites `P ⟶ Y` agree. Then pulling a sheaf of `O_Y`-modules back along the bottom and then
> down the right is the same as pulling it back down the left and then along the top:
>
> `f^* ⋙ π^* ≅ ρ^* ⋙ γ^*`.
>
> Stacks 05V5 is this applied to the square whose left column is a point `p` of `Sh(C)`, whose
> right column is the point `q = f ∘ p` of `Sh(D)`, and whose bottom row is the induced morphism
> of ringed points: the left-hand composite is then `F ↦ (f^*F)_p` and the right-hand one is
> `F ↦ F_q ⊗_{O_{D,q}} O_{C,p}`. The square itself is not constructed here — see the
> module docstring.

```lean
def pullbackModulesSquareIso {P : RingedTopos.{v, u, w}} {Q : RingedTopos.{v', u', w'}}
    [P.J.HasSheafCompose (forget RingCat.{w})]
    [P.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [P.J.HasSheafCompose (forget AddCommGrpCat.{w})]
    [HasWeakSheafify P.J AddCommGrpCat.{w}] [P.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [Q.J.HasSheafCompose (forget RingCat.{w'})]
    [Q.J.HasSheafCompose (forget₂ CommRingCat.{w'} RingCat.{w'})]
    [Q.J.HasSheafCompose (forget AddCommGrpCat.{w'})]
    [HasWeakSheafify Q.J AddCommGrpCat.{w'}] [Q.J.WEqualsLocallyBijective AddCommGrpCat.{w'}]
    (f : RingedToposHom X Y) (π : RingedToposHom P X) (ρ : RingedToposHom Q Y)
    (γ : RingedToposHom P Q) (h : f.comp π = ρ.comp γ) :
    f.toModulesHom.pullbackModules ⋙ π.toModulesHom.pullbackModules ≅
      ρ.toModulesHom.pullbackModules ⋙ γ.toModulesHom.pullbackModules
```

**`Stacks.Sheaves.StalkPullback.pointStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPoint.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPoint.lean#L124). The attribute's comment: “the formula `(f^*𝓕)_p ≅ 𝓕_q ⊗_{𝒪'_q} 𝒪_p`, naturally in `𝓕`, for an arbitrary morphism of ringed topoi and a point `p` of the source site, with `q = f ∘ p` built from the morphism and the point by Stacks 00YA”.

> **Stacks 05V5**, for a morphism of ringed topoi `f : (Sh(C), 𝒪) ⟶ (Sh(D), 𝒪')` and a point
> `Φ` of the source site `C`: the stalk at `Φ` of the pullback of a sheaf of `𝒪'`-modules is the
> extension of scalars along `𝒪'_q ⟶ 𝒪_Φ` of its stalk at the composite point `q = f ∘ Φ`,
> naturally in the module.
>
> The point `q` of the target site is `targetSitePoint`, built from `f` and `Φ` by Stacks 00YA;
> nothing about it is assumed.

```lean
def pointStalkFunctorIso :
    f.pullbackModules ⋙ Stacks.sheafModuleFiberOfCommRing Φ X.O ≅
      Stacks.sheafModuleFiberOfCommRing (targetSitePoint f Φ) Y.O ⋙
        ModuleCat.extendScalars (pointStalkRingMap f Φ)
```

**`Stacks.Sheaves.StalkPullback.toposPointStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPoint.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPoint.lean#L176). The attribute's comment: “the formula `(f^*𝓕)_p ≅ 𝓕_q ⊗_{𝒪'_q} 𝒪_p`, naturally in `𝓕`, for an arbitrary morphism of ringed topoi and a point `p` of the source topos `Sh(C)`, with `q = f ∘ p` built from the morphism and the point by Stacks 00YA”.

> **Stacks 05V5**, for a morphism of ringed topoi and a point `p` of the source *topos*
> `Sh(C)`: the stalk at `p` of the pullback of a sheaf of `𝒪'`-modules is the extension of scalars
> along `𝒪'_q ⟶ 𝒪_p` of its stalk at `q = f ∘ p`, naturally in the module.
>
> The stalk functor on sheaves of modules is taken over a point of the site, so `p` is presented
> by `p.sitePoint` through Stacks 00YA part (2); on sheaves of sets that is `p⁻¹` itself, by
> `CategoryTheory.PointOfTopos.sheafFiberIsoInverseImage`.

```lean
def toposPointStalkFunctorIso :
    f.pullbackModules ⋙ Stacks.sheafModuleFiberOfCommRing p.sitePoint X.O ≅
      Stacks.sheafModuleFiberOfCommRing (toposTargetSitePoint f p) Y.O ⋙
        ModuleCat.extendScalars (toposPointStalkRingMap f p)
```

**`Stacks.Sheaves.StalkPullback.stalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPointPair.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkPullbackAtAPointPair.lean#L375). The attribute's comment: “the formula `(f^*G)_Φ ≅ G_Ψ ⊗_{O'_Ψ} O_Φ`, naturally in the `O'`-module `G`, for a morphism of ringed topoi together with a point `Ψ` of the target site whose stalk functor on sheaves of sets is the inverse image followed by the stalk functor at `Φ`”.

> **Stacks 05V5 at a matched pair of points**, as a natural isomorphism of stalk functors:
> the stalk at `Φ` of the pullback of a sheaf of `𝒪'`-modules is the extension of scalars along
> `𝒪'_Ψ ⟶ 𝒪_Φ` of its stalk at `Ψ`.
>
> This is the clause of Stacks 05V5 that
> `AlgebraicGeometry.RingedToposHom.pullbackModulesSquareIso` states for a commutative square of
> morphisms of ringed topoi without constructing the square over a point; here the point of the
> target topos and the identification of stalk functors are the data `Ψ` and `e`.

```lean
def stalkFunctorIso :
    f.pullbackModules ⋙ Stacks.sheafModuleFiberOfCommRing Φ X.O ≅
      Stacks.sheafModuleFiberOfCommRing Ψ Y.O ⋙
        ModuleCat.extendScalars (stalkRingMap f Φ Ψ e)
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.stalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeAtTheTargetPoint.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeAtTheTargetPoint.lean#L258). The attribute's comment: “the formula `(f^*F)_p ≅ F_q ⊗_{O'_q} O_p` at a point `p` of the source site, naturally in the `O'`-module `F`, with `q = f ∘ p` the point of the target site induced by `p`; for a morphism of ringed topoi whose underlying functor is a morphism of the underlying sites, at `RingedTopos.{u, u, u}`”. References: EGA 0 (4.3.1), “more general”.

> **Stacks 05V5 at the point `Ψ` of the target site**, as a natural isomorphism of stalk
> functors: the stalk at `Φ` of the pullback of a sheaf of `O'`-modules is the extension of
> scalars along `O'_Ψ ⟶ O_Φ` of its stalk at `Ψ`.
>
> This is the clause of Stacks 05V5 that
> `AlgebraicGeometry.RingedToposHom.pullbackModulesSquareIso` names as missing: there the formula
> is proved for a commutative square of morphisms of ringed topoi, with the square over a point
> `p` and the point `q = f ∘ p` left unconstructed, and `Ψ = targetPoint f hu Φ` is that point.

```lean
def stalkFunctorIso :
    f.pullbackTopos ⋙ Stacks.sheafModuleFiberOfCommRing Φ X.O ≅
      Stacks.sheafModuleFiberOfCommRing (targetPoint f hu Φ) Y.O ⋙
        ModuleCat.extendScalars (stalkRingMap f hu Φ)
```

**`Stacks.Sheaves.DerivedPullback.StalkBaseChangeOfToposHom.stalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeOfToposHom.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeOfToposHom.lean#L305). The attribute's comment: “the formula `(f^*F)_p ≅ F_q ⊗_{O'_q} O_p` at a point `p` of the source site, naturally in the `O'`-module `F`, with `q = f ∘ p` the point of the target site induced by `p`; for an arbitrary morphism of ringed topoi, at `RingedTopos.{u, u, u}`”.

> **Stacks 05V5 at the point `Ψ` of the target site, for an arbitrary morphism of ringed
> topoi**, as a natural isomorphism of stalk functors: the stalk at `Φ` of the pullback of a sheaf
> of `O'`-modules is the extension of scalars along `O'_Ψ ⟶ O_Φ` of its stalk at `Ψ`.
>
> Nothing is assumed about the underlying sites: the pullback of Stacks 03D6 part (2) is built
> from the inverse image of Stacks 03D2, so the geometric half of the comparison is the one of
> Stacks 05V1 at `Ψ` and the algebraic half is the stalkwise formula for the extension of
> scalars.

```lean
def stalkFunctorIso :
    g.pullbackModules ⋙ Stacks.sheafModuleFiberOfCommRing Φ X.O ≅
      Stacks.sheafModuleFiberOfCommRing (targetPoint g Φ) Y.O ⋙
        ModuleCat.extendScalars (stalkRingMap g Φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.36, Tag 04EM](https://stacks.math.columbia.edu/tag/04EM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
