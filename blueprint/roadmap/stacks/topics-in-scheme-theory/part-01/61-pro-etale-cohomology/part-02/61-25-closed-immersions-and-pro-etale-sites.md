---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.appBaseChange, AlgebraicGeometry.ProEtale.appProetaleBaseChange, AlgebraicGeometry.ProEtale.isClosedImmersion_pullback_fst, AlgebraicGeometry.ProEtale.appProetaleLift, AlgebraicGeometry.ProEtale.appProetaleBaseChange_hasLeftAdjoint, AlgebraicGeometry.ProEtale.appProetaleLift_fullyFaithful, AlgebraicGeometry.ProEtale.appProetaleLift_baseChangeIso, AlgebraicGeometry.ProEtale.appProetaleBaseChange_isCovering
statement: formalized
proof: formalized
---

# 61.25 Closed immersions and pro-étale sites

Section 61.25 of the Stacks Project, [Tag 09A9](https://stacks.math.columbia.edu/tag/09A9). 6 tags here are carried by 55 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09BK, a lemma

[Tag 09BK](https://stacks.math.columbia.edu/tag/09BK) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.appBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AppProetaleSite.lean#L223). The attribute's comment: “the base-change functor”.

> The functor `u`: pro-étale base change along a morphism of affine schemes `i : Z ⟶ X`, as a
> functor `X_app ⥤ Z_app` between the affine ind-étale sites. On underlying schemes it is
> `U ↦ U ×_X Z`.

```lean
public noncomputable def appBaseChange {Z X : Scheme.{u}} [IsAffine X] [IsAffine Z]
    (i : Z ⟶ X) : AppProetale X ⥤ AppProetale Z
```

**`AlgebraicGeometry.ProEtale.appProetaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L428). The attribute's comment: “the base change functor”.

> **The base change functor.** For a morphism `i : Z ⟶ X` of affine schemes,
> pulling back along `i` carries an affine object of the small pro-étale site of `X` with
> ind-étale ring of global sections to one over `Z`, giving a functor `X_app ⥤ Z_app`,
> `U ↦ U ×_X Z`.

```lean
public noncomputable def appProetaleBaseChange : AppSmallProetale X ⥤ AppSmallProetale Z
```

**`AlgebraicGeometry.ProEtale.isClosedImmersion_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L489). The attribute's comment: “the closed immersion V → v(V)”.

> **The closed immersion `V → v(V)`.** The first projection of the fibre product
> `U ×_X Z` is a closed immersion, being the base change of `i`; combined with the identification
> of `V` with `v(V) ×_X Z` this exhibits `V → v(V)` as a closed immersion.

```lean
public theorem isClosedImmersion_pullback_fst (U : AppSmallProetale X) :
    IsClosedImmersion (pullback.fst U.obj.hom i)
```

**`AlgebraicGeometry.ProEtale.appProetaleLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L506). The attribute's comment: “the left adjoint”.

> **The left adjoint `v` of base change.** For a closed immersion `i : Z ⟶ X` of affine
> schemes, the lift of an object of `Z_app` to `X_app`: it is the right-adjoint lift of
> Stacks 097P on ind-étale algebras, read through the identification of each site with the
> opposite of a category of ind-étale algebras.

```lean
public noncomputable def appProetaleLift : AppSmallProetale Z ⥤ AppSmallProetale X
```

**`AlgebraicGeometry.ProEtale.appProetaleBaseChange_hasLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L514). The attribute's comment: “the adjunction”.

> **The adjunction.** The base change functor `U ↦ U ×_X Z` along a closed
> immersion of affine schemes has a left adjoint.

```lean
public theorem appProetaleBaseChange_hasLeftAdjoint :
    Nonempty (appProetaleLift i ⊣ appProetaleBaseChange i)
```

**`AlgebraicGeometry.ProEtale.appProetaleLift_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L523). The attribute's comment: “full faithfulness of the left adjoint”.

> **Full faithfulness of the left adjoint.**

```lean
public theorem appProetaleLift_fullyFaithful :
    Nonempty (appProetaleLift i).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.appProetaleLift_baseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersion.lean#L533). The attribute's comment: “the identification of V with u(v(V))”.

> **The identification of `V` with `u(v(V))`.** For `V` in `Z_app` the unit of
> the adjunction identifies `V` with the fibre product `v(V) ×_X Z`.

```lean
public theorem appProetaleLift_baseChangeIso :
    Nonempty (𝟭 (AppSmallProetale Z) ≅ appProetaleLift i ⋙ appProetaleBaseChange i)
```

**`AlgebraicGeometry.ProEtale.appProetaleBaseChange_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteContinuous.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteContinuous.lean#L73). The attribute's comment: “the base change functor is continuous”.

> **Stacks 09BK, continuity of the base change functor: coverings.** For a morphism
> `i : Z ⟶ X` of affine schemes, the base change functor `U ↦ U ×_X Z` from `X_app` to `Z_app`
> carries a standard pro-étale covering family to a standard pro-étale covering family.

```lean
public theorem appProetaleBaseChange_isCovering {X Z : Scheme.{u}} [IsAffine X] [IsAffine Z]
    (i : Z ⟶ X) {U : AppSmallProetale X} (E : PreZeroHypercover.{u + 1} U)
    (hE : AppSmallProetale.IsCovering X ⟨U, E⟩) :
    AppSmallProetale.IsCovering Z
      ⟨(appProetaleBaseChange i).obj U, E.map (appProetaleBaseChange i)⟩
```

**`AlgebraicGeometry.ProEtale.appProetaleLift_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteContinuous.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteContinuous.lean#L103). The attribute's comment: “the functor v is cocontinuous”.

> **Stacks 09BK, cocontinuity of the left adjoint.** For a closed immersion `i : Z ⟶ X` of
> affine schemes the left adjoint `v : Z_app ⥤ X_app` of the base change functor is cocontinuous:
> it pulls covering sieves back to covering sieves.

```lean
public theorem appProetaleLift_isCocontinuous {X Z : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [IsAffine X] [IsAffine Z] :
    (appProetaleLift i).IsCocontinuous (AppSmallProetale.topology Z)
      (AppSmallProetale.topology X)
```

**`AlgebraicGeometry.ProEtale.appProetaleBaseChange_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSitePullback.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSitePullback.lean#L190). The attribute's comment: “the base change functor is continuous”.

> **Stacks 09BK, continuity of the base change functor: fibre products.** For a morphism
> `i : Z ⟶ X` of affine schemes the functor `U ↦ U ×_X Z` from `X_app` to `Z_app` preserves fibre
> products, which is the second half of continuity in the sense of the Stacks Project.

```lean
public noncomputable instance appProetaleBaseChange_preservesPullbacks {X Z : Scheme.{u}}
    [IsAffine X] [IsAffine Z] (i : Z ⟶ X) :
    PreservesLimitsOfShape WalkingCospan (appProetaleBaseChange i)
```

**`AlgebraicGeometry.ProEtale.indEtaleQuotientLift_exists_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteSpecialization.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteSpecialization.lean#L72). The attribute's comment: “every point of v(V) specialises to a point of V”.

> **Stacks 09BK, specialization to a point of `V`.** Let `A` be a ring, `I ⊆ A` an ideal and
> `V` an ind-étale `A ⧸ I`-algebra. Writing `C` for the lift of `V` to an ind-étale `A`-algebra,
> so that `v(V) = Spec C` and `V = Spec (C ⧸ I C)` is the closed subscheme of `v(V)` cut out by
> the ideal generated by the image of `I`, every point of `v(V)` specializes to a point of `V`.

```lean
public theorem indEtaleQuotientLift_exists_specializes (A : Type u) [CommRing A] (I : Ideal A)
    (V : IndEtaleAlgebra (A ⧸ I))
    (p : PrimeSpectrum ((indEtaleQuotientLift A I).obj V).obj.right) :
    ∃ q : PrimeSpectrum ((indEtaleQuotientLift A I).obj V).obj.right, p ⤳ q ∧
      I.map ((indEtaleQuotientLift A I).obj V).obj.hom.hom ≤ q.asIdeal
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L517). The attribute's comment: “the base-change functor”.

> Pullback along a morphism of the base, on affine ind-étale pro-étale sites.

```lean
public noncomputable def affineIndEtaleBaseChange (i : Z ⟶ X)
    [IsAffine X.obj] [IsAffine Z.obj] :
    AffineIndEtaleProetale B X ⥤ AffineIndEtaleProetale B Z
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleBaseChange_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L614).

> Base change on the affine ind-étale sites is continuous.

```lean
public instance affineIndEtaleBaseChange_isContinuous (i : Z ⟶ X)
    [IsAffine X.obj] [IsAffine Z.obj] :
    (affineIndEtaleBaseChange B i).IsContinuous (AffineIndEtaleProetale.topology B X)
      (AffineIndEtaleProetale.topology B Z)
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleBaseChange_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 963](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L963). The attribute's comment: “the base-change comparison”.

> On underlying schemes, affine ind-étale base change is ordinary fibre product.

```lean
public theorem affineIndEtaleBaseChange_comp_forget :
    Nonempty ((affineIndEtaleBaseChange B i ⋙ AffineIndEtaleProetale.inclusion B Z ⋙
      SmallProetale.inclusion B Z.obj Z.property) ≅
      (AffineIndEtaleProetale.inclusion B X ⋙ SmallProetale.inclusion B X.obj X.property ⋙
        Over.pullback i))
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleLift_adj_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 1697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L1697).

> The lift is left adjoint to base change.

```lean
public theorem affineIndEtaleLift_adj_baseChange :
    Nonempty (affineIndEtaleLift B i ⊣ affineIndEtaleBaseChange B i)
```

**`AlgebraicGeometry.ProEtale.closedFiberInclusion_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 1806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L1806).

> The natural inclusion identifies an object with the closed fibre of its lift.

```lean
public theorem closedFiberInclusion_isPullback
    (V : AffineIndEtaleProetale B Z) :
    IsPullback ((closedFiberInclusion B i).app V) (B.inclusion.map V.obj.obj.hom)
      (B.inclusion.map ((affineIndEtaleLift B i).obj V).obj.obj.hom) (B.inclusion.map i)
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleLift_baseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 1936](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L1936).

> Base change of the lift is canonically the original object, naturally in that object.

```lean
public theorem affineIndEtaleLift_baseChangeIso :
    Nonempty (affineIndEtaleLift B i ⋙ affineIndEtaleBaseChange B i ≅
      𝟭 (AffineIndEtaleProetale B Z))
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleLift_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 2048](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L2048).

> The left-adjoint lift is fully faithful.

```lean
public theorem affineIndEtaleLift_fullyFaithful :
    Nonempty (affineIndEtaleLift B i).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.closedFiberInclusion_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 2058](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L2058).

> The natural map from an object to its lift is a closed immersion.

```lean
public instance closedFiberInclusion_isClosedImmersion
    (V : AffineIndEtaleProetale B Z) :
    IsClosedImmersion ((closedFiberInclusion B i).app V)
```

**`AlgebraicGeometry.ProEtale.exists_specialization_closedFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 2083](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L2083).

> Every point of the lift specializes to a point of its closed fibre.

```lean
public theorem exists_specialization_closedFiber
    (V : AffineIndEtaleProetale B Z)
    (x : ((affineIndEtaleLift B i).obj V).obj.obj.left.obj) :
    ∃ z : V.obj.obj.left.obj,
      x ⤳ ((closedFiberInclusion B i).app V).base z
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleLift_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 2124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L2124).

> The lift is cocontinuous for the affine ind-étale topologies.

```lean
public instance affineIndEtaleLift_isCocontinuous :
    (affineIndEtaleLift B i).IsCocontinuous (AffineIndEtaleProetale.topology B Z)
      (AffineIndEtaleProetale.topology B X)
```

**`AlgebraicGeometry.ProEtale.affineIndEtaleLift_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean, line 2133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/AffineIndEtaleLift.lean#L2133).

> The lift takes finite standard pro-étale coverings to such coverings.

```lean
public theorem affineIndEtaleLift_isCovering
    (E : Covering (AffineIndEtaleProetale B Z))
    (hE : AffineIndEtaleProetale.IsCovering B Z E) :
    AffineIndEtaleProetale.IsCovering B X
      ⟨(affineIndEtaleLift B i).obj E.1, E.2.map (affineIndEtaleLift B i)⟩
```

## Tag 09BL, a lemma

[Tag 09BL](https://stacks.math.columbia.edu/tag/09BL) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.abelianSmallProetalePushforward_fullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean#L262). The attribute's comment: “(6), full faithfulness of the direct image i\_* on abelian sheaves, for the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (6) for the direct image on abelian sheaves.** For a closed immersion of
> affine schemes the direct image `i_*` on abelian sheaves on the small pro-étale sites is fully
> faithful.

```lean
def abelianSmallProetalePushforward_fullyFaithful :
    ((smallProetaleBaseChange B Z X i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
      (SmallProetale.topology B X.obj X.property)
      (SmallProetale.topology B Z.obj Z.property)).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.abelianSmallProetale_isIso_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean#L290). The attribute's comment: “(5), the map i^\{-1} i\_* -> id is an isomorphism on abelian sheaves, for the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (5) for the direct image on abelian sheaves.** For a closed immersion of
> affine schemes the counit `i^{-1} i_* ⟶ id` on abelian sheaves on the small pro-étale sites is
> an isomorphism, its right adjoint `i_*` being fully faithful.

```lean
theorem abelianSmallProetale_isIso_counit :
    IsIso (Functor.sheafPullbackConstruction.sheafAdjunctionContinuous
      (smallProetaleBaseChange B Z X i) AddCommGrpCat.{u + 1}
      (SmallProetale.topology B X.obj X.property)
      (SmallProetale.topology B Z.obj Z.property)).counit
```

**`AlgebraicGeometry.ProEtale.isRightAdjoint_abelianSmallProetaleSheafPullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean#L332). The attribute's comment: “(4), the inverse image i^\{-1} : Ab(X\_proetale) -> Ab(Z\_proetale) of a closed immersion of affine objects of a chosen big pro-etale site has a left adjoint i\_!”.

> **Stacks 09BL (4).** The inverse image `i^{-1}` on abelian sheaves on the small pro-étale
> sites of a closed immersion of affine schemes has a left adjoint `i_!`.

```lean
instance isRightAdjoint_abelianSmallProetaleSheafPullback :
    (Functor.sheafPullbackConstruction.sheafPullback (smallProetaleBaseChange B Z X i)
      AddCommGrpCat.{u + 1} (SmallProetale.topology B X.obj X.property)
      (SmallProetale.topology B Z.obj Z.property)).IsRightAdjoint
```

**`AlgebraicGeometry.ProEtale.abelianSmallProetaleLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean#L380). The attribute's comment: “(5), the map id -> i^\{-1} i\_! is an isomorphism, for abelian sheaves on the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (5), the unit of lower shriek on abelian sheaves.** For a closed immersion of
> affine schemes the unit `id ⟶ i^{-1} i_!` of the adjunction `i_! ⊣ i^{-1}` on abelian sheaves on
> the small pro-étale sites is an isomorphism.
>
> In the adjoint triple `i_! ⊣ i^{-1} ⊣ i_*` the unit of the left adjunction is invertible exactly
> when the counit of the right one is, and the latter is
> `abelianSmallProetale_isIso_counit`.

```lean
theorem abelianSmallProetaleLowerShriek_unit_isIso :
    IsIso (abelianSmallProetaleLowerShriekAdjunction B i).unit
```

**`AlgebraicGeometry.ProEtale.abelianSmallProetaleLowerShriek_fullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/AbelianLowerShriek.lean#L390). The attribute's comment: “(6), full faithfulness of i\_!, for abelian sheaves on the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (6) for lower shriek on abelian sheaves.** For a closed immersion of affine
> schemes the left adjoint `i_!` of the inverse image on abelian sheaves on the small pro-étale
> sites is fully faithful.

```lean
def abelianSmallProetaleLowerShriek_fullyFaithful :
    (abelianSmallProetaleLowerShriek B i).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.affineIndEtalePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean#L69). The attribute's comment: “topos\_identification”.

> **Stacks 09BL.** The direct image of the small pro-étale morphism of a closed immersion of
> affine schemes, read through the restriction equivalences to the affine ind-étale sites, is the
> direct image attached to the cocontinuous lift.

```lean
def affineIndEtalePushforwardIso :
    (smallProetaleMorphism B Z X i).pushforward ⋙
      (AffineIndEtaleProetale.inclusion B X).sheafPushforwardContinuous (Type (u + 1))
        (AffineIndEtaleProetale.topology B X) (SmallProetale.topology B X.obj X.property) ≅
    (AffineIndEtaleProetale.inclusion B Z).sheafPushforwardContinuous (Type (u + 1))
        (AffineIndEtaleProetale.topology B Z) (SmallProetale.topology B Z.obj Z.property) ⋙
      (affineIndEtaleLift B i).sheafPushforwardCocontinuous (Type (u + 1))
        (AffineIndEtaleProetale.topology B Z) (AffineIndEtaleProetale.topology B X)
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_counit_isIso_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean#L158). The attribute's comment: “pushforward\_counit”.

> **Stacks 09BL.** For a closed immersion of affine schemes, the counit
> `i^{-1} i_* → id` of the small pro-étale adjunction is an isomorphism.

```lean
theorem smallProetaleMorphism_counit_isIso_of_isAffine :
    IsIso (smallProetaleMorphism B Z X i).adj.counit
```

**`AlgebraicGeometry.ProEtale.proetaleInverseImage_sheafify_affineIndEtaleLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersion.lean#L170). The attribute's comment: “inverse\_image\_formula”.

> **Stacks 09BL.** For a closed immersion of affine schemes, the inverse image of a small
> pro-étale sheaf, restricted to the affine ind-étale site of `Z`, is the sheafification of the
> presheaf of its values on the lift, naturally in the sheaf.

```lean
def proetaleInverseImage_sheafify_affineIndEtaleLift :
    (smallProetaleMorphism B Z X i).inverseImage ⋙
        (AffineIndEtaleProetale.inclusion B Z).sheafPushforwardContinuous (Type (u + 1))
          (AffineIndEtaleProetale.topology B Z) (SmallProetale.topology B Z.obj Z.property) ≅
      sheafToPresheaf (SmallProetale.topology B X.obj X.property) (Type (u + 1)) ⋙
        (Functor.whiskeringLeft (AffineIndEtaleProetale B Z)ᵒᵖ
          (SmallProetale B X.obj X.property)ᵒᵖ (Type (u + 1))).obj
            (affineIndEtaleLift B i ⋙ AffineIndEtaleProetale.inclusion B X).op ⋙
        presheafToSheaf (AffineIndEtaleProetale.topology B Z) (Type (u + 1))
```

**`AlgebraicGeometry.ProEtale.isRightAdjoint_smallProetaleMorphism_inverseImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean#L220). The attribute's comment: “(3), the inverse image i^\{-1} : Sh(X\_proetale) -> Sh(Z\_proetale) of a closed immersion of affine objects of a chosen big pro-etale site has a left adjoint i^\{Sh}\_!”.

> **Stacks 09BL (3).** The inverse image `i^{-1}` on small pro-étale sheaves of sets of a
> closed immersion of affine schemes has a left adjoint `i^{Sh}_!`.

```lean
instance isRightAdjoint_smallProetaleMorphism_inverseImage :
    (smallProetaleMorphism B Z X i).inverseImage.IsRightAdjoint
```

**`AlgebraicGeometry.ProEtale.smallProetaleLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean#L270). The attribute's comment: “(5), the map id -> i^\{-1} i^\{Sh}\_! is an isomorphism, for sheaves of sets on the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (5), the unit of lower shriek.** For a closed immersion of affine schemes the
> unit `id ⟶ i^{-1} i^{Sh}_!` of the adjunction `i^{Sh}_! ⊣ i^{-1}` on small pro-étale sheaves of
> sets is an isomorphism.
>
> In an adjoint triple `i^{Sh}_! ⊣ i^{-1} ⊣ i_*` the unit of the left adjunction is invertible
> exactly when the counit of the right one is, and the latter is Stacks 09BL (5) for `i^{-1}i_*`.

```lean
theorem smallProetaleLowerShriek_unit_isIso :
    IsIso (smallProetaleLowerShriekAdjunction B i).unit
```

**`AlgebraicGeometry.ProEtale.smallProetaleLowerShriek_fullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/LowerShriek.lean#L279). The attribute's comment: “(6), full faithfulness of i^\{Sh}\_!, for sheaves of sets on the small pro-etale sites of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (6) for lower shriek.** For a closed immersion of affine schemes the left
> adjoint `i^{Sh}_!` of the inverse image on small pro-étale sheaves of sets is fully faithful.

```lean
def smallProetaleLowerShriek_fullyFaithful :
    (smallProetaleLowerShriek B i).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.proetaleInverseImage_sections_iso_affineIndEtaleLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractible.lean, line 575](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractible.lean#L575). The attribute's comment: “weakly\_contractible\_evaluation”.

> At a weakly contractible affine ind-étale object of the closed fibre, inverse image is
> evaluation at its lift, naturally in the sheaf.

```lean
def proetaleInverseImage_sections_iso_affineIndEtaleLift (V : AffineIndEtaleProetale B Z)
    (hV : (AffineIndEtaleProetale.topology B Z).IsWeaklyContractible V) :
    Functor.sheafPullbackConstruction.sheafPullback (smallProetaleBaseChange B Z X i)
        (Type (max (u + 1) v)) (SmallProetale.topology B X.obj X.property)
        (SmallProetale.topology B Z.obj Z.property) ⋙
      sheafToPresheaf (SmallProetale.topology B Z.obj Z.property)
        (Type (max (u + 1) v)) ⋙
      (evaluation _ _).obj (Opposite.op ((AffineIndEtaleProetale.inclusion B Z).obj V)) ≅
    sheafToPresheaf (SmallProetale.topology B X.obj X.property)
        (Type (max (u + 1) v)) ⋙
      (evaluation _ _).obj
        (Opposite.op ((AffineIndEtaleProetale.inclusion B X).obj
          ((affineIndEtaleLift B i).obj V)))
```

**`AlgebraicGeometry.ProEtale.proetaleInverseImage_sections_iso_affineIndEtaleLiftAddCommGrp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractibleAbelian.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/WeaklyContractibleAbelian.lean#L182). The attribute's comment: “(2) for abelian sheaves: at a weakly contractible object V of Z\_app the inverse image of an abelian sheaf is F(v(V)), for the morphism of topoi of a closed immersion of affine objects of a chosen big pro-etale site”.

> **Stacks 09BL (2) for abelian sheaves.** At a weakly contractible affine ind-étale object of
> the closed fibre, the inverse image of an abelian pro-étale sheaf is evaluation at the lift of
> that object, naturally in the sheaf.

```lean
def proetaleInverseImage_sections_iso_affineIndEtaleLiftAddCommGrp
    (V : AffineIndEtaleProetale B Z)
    (hV : (AffineIndEtaleProetale.topology B Z).IsWeaklyContractible V) :
    Functor.sheafPullbackConstruction.sheafPullback (smallProetaleBaseChange B Z X i)
        AddCommGrpCat.{u + 1} (SmallProetale.topology B X.obj X.property)
        (SmallProetale.topology B Z.obj Z.property) ⋙
      sheafToPresheaf (SmallProetale.topology B Z.obj Z.property) AddCommGrpCat.{u + 1} ⋙
      (evaluation _ _).obj (Opposite.op ((AffineIndEtaleProetale.inclusion B Z).obj V)) ≅
    sheafToPresheaf (SmallProetale.topology B X.obj X.property) AddCommGrpCat.{u + 1} ⋙
      (evaluation _ _).obj
        (Opposite.op ((AffineIndEtaleProetale.inclusion B X).obj
          ((affineIndEtaleLift B i).obj V)))
```

**`AlgebraicGeometry.ProEtale.appProetaleInverseImage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean#L135). The attribute's comment: “(1), the inverse image is the sheafification of the presheaf V -> F(v(V)), for the morphism of topoi induced by the fully faithful cocontinuous functor v of Tag 09BK”.

> **Stacks 09BL (1), the formula.** The inverse image of the morphism of topoi induced by `v`
> is the sheafification of the presheaf `V ↦ F(v(V))` on `Z_app`: it is restriction along `v.op`
> sandwiched between the inclusion of sheaves into presheaves and sheafification.

```lean
public theorem appProetaleInverseImage_eq :
    appProetaleInverseImage i =
      sheafToPresheaf (AppSmallProetale.topology X) (Type (u + 1)) ⋙
        (Functor.whiskeringLeft (AppSmallProetale Z)ᵒᵖ (AppSmallProetale X)ᵒᵖ
            (Type (u + 1))).obj (appProetaleLift i).op ⋙
          presheafToSheaf (AppSmallProetale.topology Z) (Type (u + 1))
```

**`AlgebraicGeometry.ProEtale.appProetaleInverseImageAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean#L148). The attribute's comment: “(1), the sheafification of V -> F(v(V)) is the inverse image, being left adjoint to the direct image of the morphism of topoi induced by the cocontinuous functor v of Tag 09BK”.

> **Stacks 09BL (1), that this is the inverse image.** The sheafification of `V ↦ F(v(V))` is
> left adjoint to the direct image, so it is the inverse image of the morphism of topoi induced
> by `v`.

```lean
public noncomputable def appProetaleInverseImageAdjunction :
    appProetaleInverseImage i ⊣ appProetalePushforward i
```

**`AlgebraicGeometry.ProEtale.appProetalePushforwardFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean#L176). The attribute's comment: “(6), full faithfulness of the direct image i\_*, for the morphism of topoi induced by the fully faithful cocontinuous functor v of Tag 09BK”.

> **Stacks 09BL (6) for the direct image.** The direct image `i_*` of the morphism of topoi
> induced by `v` is fully faithful.
>
> On underlying presheaves `i_*` is restriction along the base change functor `u`, whose left
> adjoint is restriction along `v`; the composite of the two is restriction along `v ⋙ u`, which
> is the identity because `v` is fully faithful.

```lean
public noncomputable def appProetalePushforwardFullyFaithful :
    (appProetalePushforward i).FullyFaithful
```

**`AlgebraicGeometry.ProEtale.appProetale_isIso_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteClosedImmersionTopos.lean#L193). The attribute's comment: “(5), the map i^\{-1} i\_* -> id is an isomorphism, for the morphism of topoi induced by the fully faithful cocontinuous functor v of Tag 09BK”.

> **Stacks 09BL (5) for the direct image.** The counit `i^{-1}i_* ⟶ id` of the morphism of
> topoi induced by `v` is an isomorphism, because its right adjoint `i_*` is fully faithful.

```lean
public theorem appProetale_isIso_counit :
    IsIso (appProetaleInverseImageAdjunction i).counit
```

## Tag 09AA, a lemma

[Tag 09AA](https://stacks.math.columbia.edu/tag/09AA) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_counit_isIso_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean#L174). The attribute's comment: “(3), the counit i^\{-1} i\_* -> id of the morphism of topoi of a closed immersion of objects of a chosen big pro-etale site is an isomorphism”.

> **Stacks 09AA (3).** For a closed immersion `i : Z ⟶ X` of objects of a chosen big pro-étale
> site, the counit `i⁻¹ i_* ⟶ id` of the direct-image adjunction on small pro-étale sheaves of sets
> is an isomorphism.
>
> The assertion is Zariski local on `X` by
> `AlgebraicGeometry.ProEtale.smallProetaleMorphism_counit_isIso_of_affineCounit`, which reduces it
> to the affine objects of the small pro-étale site of `X`; over such an object the base change of
> `i` is a closed immersion of affine objects, where the assertion is Stacks 09BL.

```lean
theorem smallProetaleMorphism_counit_isIso_of_isClosedImmersion
    [IsClosedImmersion (B.inclusion.map i)] :
    IsIso (smallProetaleMorphism B Z X i).adj.counit
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_pushforward_fullyFaithful_of_isClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean#L189). The attribute's comment: “(2), the direct image i\_* of the morphism of topoi of a closed immersion of objects of a chosen big pro-etale site is fully faithful”.

> **Stacks 09AA (2).** For a closed immersion `i : Z ⟶ X` of objects of a chosen big pro-étale
> site, the direct image `i_*` on small pro-étale sheaves of sets is fully faithful.
>
> This is assertion (3) together with the equivalence of Sites 04D6: the right adjoint of an
> adjunction whose counit is invertible is fully faithful.

```lean
def smallProetaleMorphism_pushforward_fullyFaithful_of_isClosedImmersion :
    (smallProetaleMorphism B Z X i).pushforward.FullyFaithful
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_inverseImage_preservesLimits_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedImmersionEmbedding.lean#L207). The attribute's comment: “(1), the inverse image i^\{-1} of the morphism of topoi of a closed immersion of objects of a chosen big pro-etale site commutes with limits”.

> **Stacks 09AA (1).** For a closed immersion `i : Z ⟶ X` of objects of a chosen big pro-étale
> site, the inverse image `i⁻¹` on small pro-étale sheaves of sets commutes with limits.
>
> The base changes along `i` of the affine objects of the small pro-étale site of `X` cover the
> final object of the small pro-étale site of `Z`, so the canonical comparison map from `i⁻¹` of a
> limit to the limit of `i⁻¹` is invertible as soon as it is bijective on the sections over the
> objects lying over one of them, and that is invertibility of its restriction to such a member.
> Restriction commutes with limits, being a right adjoint, and exchanges with `i⁻¹` across the
> base-change square by Beck–Chevalley, so the restricted comparison map is the comparison map for
> the base-changed closed immersion of affine objects, whose inverse image commutes with limits by
> Stacks 09BL (3).

```lean
theorem smallProetaleMorphism_inverseImage_preservesLimits_of_isClosedImmersion :
    PreservesLimits (smallProetaleMorphism B Z X i).inverseImage
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphismPushforwardFullyFaithfulOfAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean#L77). The attribute's comment: “(2), the direct image is fully faithful, given that pro-etale base change admits a fully faithful left adjoint -- the adjoint that Tag 09BK supplies for a closed immersion”.

> **Stacks 09AA (2) given the adjoint of Stacks 09BK.** If small pro-étale base change along
> `f` admits a fully faithful left adjoint, the direct image `f_*` on small pro-étale sheaves of
> sets is fully faithful.
>
> The direct image is restriction along base change, which is fully faithful on presheaves because
> restriction along the left adjoint is a left adjoint of it with invertible counit.

```lean
public noncomputable def smallProetaleMorphismPushforwardFullyFaithfulOfAdjoint
    [v.Full] [v.Faithful] :
    (smallProetaleMorphism B T S f).pushforward.FullyFaithful
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_isIso_counit_of_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean#L92). The attribute's comment: “(3), the counit of the morphism of topoi is an isomorphism, given that pro-etale base change admits a fully faithful left adjoint”.

> **Stacks 09AA (3) given the adjoint of Stacks 09BK.** If small pro-étale base change along
> `f` admits a fully faithful left adjoint, the counit `f⁻¹f_*F ⟶ F` of the morphism of topoi is an
> isomorphism, so `f⁻¹f_*` is the identity on small pro-étale sheaves of sets.

```lean
public theorem smallProetaleMorphism_isIso_counit_of_adjoint [v.Full] [v.Faithful] :
    IsIso (smallProetaleMorphism B T S f).adj.counit
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_inverseImage_preservesLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/SmallBaseChangeAdjoint.lean#L103). The attribute's comment: “(1), the inverse image commutes with limits, given that it admits a left adjoint -- which is clause (3) of Tag 09BL”.

> **Stacks 09AA (1) given the left adjoint of Stacks 09BL (3).** If the inverse image `f⁻¹` on
> small pro-étale sheaves of sets admits a left adjoint, it commutes with limits.

```lean
public theorem smallProetaleMorphism_inverseImage_preservesLimits
    [(smallProetaleMorphism B T S f).inverseImage.IsRightAdjoint] :
    PreservesLimits (smallProetaleMorphism B T S f).inverseImage
```

## Tag 09AB, a lemma

[Tag 09AB](https://stacks.math.columbia.edu/tag/09AB) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.smallProetalePushforward_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance.lean, line 1641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance.lean#L1641). The attribute's comment: “direct image, assuming essential surjectivity of etale pullback (the content of Stacks 04DZ) and Stacks 09YZ over a qcqs base”.

> **Topological invariance of the small pro-étale topos, direct image.** For an integral,
> universally injective and surjective morphism `f : T ⟶ S` in a chosen big pro-étale site, the
> direct image of the induced morphism of small pro-étale topoi is an equivalence.
>
> This is the direct-image half of Stacks Project, Tag 09AB, with the two inputs that this library
> does not have carried as explicit hypotheses: essential surjectivity of base change on small
> étale sites, which is the remaining content of Stacks Project, Tag 04DZ, and
> `AlgebraicGeometry.IntegralHasFinitePresentationLimit`, which is Stacks Project, Tag 09YZ over a
> quasi-compact quasi-separated base and is what Stacks Project, Tag 05YU still needs.

```lean
theorem smallProetalePushforward_isEquivalence
    (hIntegral : IsIntegralHom (B.inclusion.map f))
    (hInjective : UniversallyInjective (B.inclusion.map f))
    (hSurjective : Surjective (B.inclusion.map f)) :
    (smallProetaleMorphism B T S f).pushforward.IsEquivalence
```

**`AlgebraicGeometry.ProEtale.smallProetaleInverseImage_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance.lean, line 1687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance.lean#L1687). The attribute's comment: “inverse image, assuming essential surjectivity of etale pullback (the content of Stacks 04DZ) and Stacks 09YZ over a qcqs base”.

> **Topological invariance of the small pro-étale topos, inverse image.** For an integral,
> universally injective and surjective morphism `f : T ⟶ S` in a chosen big pro-étale site, the
> inverse image of the induced morphism of small pro-étale topoi is an equivalence.
>
> Together with `AlgebraicGeometry.ProEtale.smallProetalePushforward_isEquivalence` and
> `CategoryTheory.Adjunction.toEquivalence` of the adjunction `f⁻¹ ⊣ f_*`, this is Stacks Project,
> Tag 09AB; its two hypotheses are those of the direct-image half.

```lean
theorem smallProetaleInverseImage_isEquivalence
    (hIntegral : IsIntegralHom (B.inclusion.map f))
    (hInjective : UniversallyInjective (B.inclusion.map f))
    (hSurjective : Surjective (B.inclusion.map f)) :
    (smallProetaleMorphism B T S f).inverseImage.IsEquivalence
```

**`AlgebraicGeometry.ProEtale.smallProetaleMorphism_isIso_unit_and_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean#L89). The attribute's comment: “unit and counit of f^\{-1} -| f\_* are isomorphisms; unconditional: only f integral, universally injective, surjective; 04DZ and 09YZ are proved and supplied, not assumed”.

> **Topological invariance of the small pro-étale topos.** Let `f : T ⟶ S` be an integral,
> universally injective and surjective morphism of schemes. Then the direct image `f_*` and the
> inverse image `f⁻¹` of the induced morphism of small pro-étale topoi are quasi-inverse
> equivalences: the unit and the counit of the adjunction `f⁻¹ ⊣ f_*` are isomorphisms.
>
> The only hypotheses are `f` and the three conditions on it. The proof supplies Stacks 04DZ, by
> `Stacks.Etale.etalePullback_isEquivalence`, and Stacks 09YZ, by
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`, to the base's
> conditional `AlgebraicGeometry.ProEtale.smallProetalePushforward_isEquivalence`, so it has no
> further hypotheses.

```lean
theorem smallProetaleMorphism_isIso_unit_and_counit
    (hIntegral : IsIntegralHom (B.inclusion.map f))
    (hInjective : UniversallyInjective (B.inclusion.map f))
    (hSurjective : Surjective (B.inclusion.map f)) :
    IsIso (smallProetaleMorphism B T S f).adj.unit ∧
      IsIso (smallProetaleMorphism B T S f).adj.counit
```

**`AlgebraicGeometry.ProEtale.smallProetalePushforward_isEquivalence_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean#L120). The attribute's comment: “direct image f\_* is an equivalence; unconditional: only f integral, universally injective, surjective; 04DZ and 09YZ are proved and supplied, not assumed”.

> **Topological invariance of the small pro-étale topos, direct image, unconditionally.** Let
> `f : T ⟶ S` be an integral, universally injective and surjective morphism of schemes. Then the
> direct image `f_*` of the induced morphism of small pro-étale topoi is an equivalence.
>
> The only hypotheses are `f` and the three conditions integral, universally injective and
> surjective. The base's `AlgebraicGeometry.ProEtale.smallProetalePushforward_isEquivalence` is the
> same statement taking in addition topological invariance of the étale site (Stacks 04DZ) and
> integral morphisms as limits of finite ones (Stacks 09YZ) as section hypotheses; this theorem is
> that one with both supplied, by `Stacks.Etale.etalePullback_isEquivalence` and
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`, so it has no
> further hypotheses.

```lean
theorem smallProetalePushforward_isEquivalence_of_isIntegralHom
    [IsIntegralHom (B.inclusion.map f)] [UniversallyInjective (B.inclusion.map f)]
    [Surjective (B.inclusion.map f)] :
    (smallProetaleMorphism B T S f).pushforward.IsEquivalence
```

**`AlgebraicGeometry.ProEtale.smallProetaleInverseImage_isEquivalence_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean#L140). The attribute's comment: “inverse image f^\{-1} is an equivalence; unconditional: only f integral, universally injective, surjective; 04DZ and 09YZ are proved and supplied, not assumed”.

> **Topological invariance of the small pro-étale topos, inverse image, unconditionally.** Let
> `f : T ⟶ S` be an integral, universally injective and surjective morphism of schemes. Then the
> inverse image `f⁻¹` of the induced morphism of small pro-étale topoi is an equivalence.
>
> The only hypotheses are `f` and the three conditions integral, universally injective and
> surjective. The base's `AlgebraicGeometry.ProEtale.smallProetaleInverseImage_isEquivalence` is the
> same statement taking in addition Stacks 04DZ and Stacks 09YZ as section hypotheses; this theorem
> is that one with both supplied, by `Stacks.Etale.etalePullback_isEquivalence` and
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`, so it has no
> further hypotheses.

```lean
theorem smallProetaleInverseImage_isEquivalence_of_isIntegralHom
    [IsIntegralHom (B.inclusion.map f)] [UniversallyInjective (B.inclusion.map f)]
    [Surjective (B.inclusion.map f)] :
    (smallProetaleMorphism B T S f).inverseImage.IsEquivalence
```

**`AlgebraicGeometry.ProEtale.smallProetaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/TopologicalInvariance/QuasiInverse.lean#L159). The attribute's comment: “f^\{-1} and f\_* as quasi-inverse equivalences of the small pro-etale topoi; unconditional: only f integral, universally injective, surjective”.

> **The small pro-étale topoi along an integral universal homeomorphism are equivalent.** For
> `f : T ⟶ S` integral, universally injective and surjective, the equivalence between the small
> pro-étale topos of `S` and that of `T` whose functor is the inverse image `f⁻¹` and whose inverse
> is the direct image `f_*`, with unit and counit those of the adjunction `f⁻¹ ⊣ f_*`: these two
> functors are quasi-inverse equivalences.
>
> The only hypotheses are `f` and the three conditions on it; Stacks 04DZ and Stacks 09YZ, which
> the base's conditional statements take as section hypotheses, are supplied by
> `Stacks.Etale.etalePullback_isEquivalence` and
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`.

```lean
noncomputable def smallProetaleEquivalence
    (hIntegral : IsIntegralHom (B.inclusion.map f))
    (hInjective : UniversallyInjective (B.inclusion.map f))
    (hSurjective : Surjective (B.inclusion.map f)) :
    Sheaf (SmallProetale.topology B S.obj S.property) (Type (u + 1)) ≌
      Sheaf (SmallProetale.topology B T.obj T.property) (Type (u + 1))
```

## Tag 09AC, a lemma

[Tag 09AC](https://stacks.math.columbia.edu/tag/09AC) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.abelianProetaleInverseImage_sections_iso_closedFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedFibreInverseImage.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ExtensionByZero/ClosedFibreInverseImage.lean#L193). The attribute's comment: “i^\{-1}F(U x\_X Z) = F(U) for every abelian sheaf F on X\_proetale, naturally in F, for an ARBITRARY closed immersion i : Z -> X and U affine and weakly contractible (in the chosen big pro-etale site, Tag 098H) all of whose points specialize into U x\_X Z”.

> **Stacks 09AC.** Let `i : Z ⟶ X` be a closed immersion of objects of a chosen big pro-étale
> site and let `U` be an object of the small pro-étale site of `X` such that
>
> 1. `U` is affine and weakly contractible, and
> 2. every point of `U` specializes to a point of `U ×_X Z`.
>
> Then `i^{-1}F(U ×_X Z) = F(U)` for every abelian sheaf `F` on the small pro-étale site of `X`,
> naturally in `F`.
>
> Weak contractibility of `U` is taken in the chosen big pro-étale site; for an affine object it
> is equivalent to w-contractibility of its ring of global sections by Stacks 098H, and it implies
> weak contractibility of `U` as an object of the small pro-étale site of `X`.

```lean
def abelianProetaleInverseImage_sections_iso_closedFibre [IsAffine U.obj.left.obj]
    (hU : B.topology.IsWeaklyContractible U.obj.left)
    (hspec : ∀ x : U.obj.left.obj, ∃ w : (pullback U.obj.hom i).obj,
      x ⤳ (B.inclusion.map (pullback.fst U.obj.hom i)).base w) :
    Functor.sheafPullbackConstruction.sheafPullback (smallProetaleBaseChange B Z X i)
        AddCommGrpCat.{u + 1} (SmallProetale.topology B X.obj X.property)
        (SmallProetale.topology B Z.obj Z.property) ⋙
      sheafToPresheaf (SmallProetale.topology B Z.obj Z.property) AddCommGrpCat.{u + 1} ⋙
      (evaluation _ _).obj (op ((smallProetaleBaseChange B Z X i).obj U)) ≅
    sheafToPresheaf (SmallProetale.topology B X.obj X.property) AddCommGrpCat.{u + 1} ⋙
      (evaluation _ _).obj (op U)
```

**`AlgebraicGeometry.ProEtale.existsUnique_algHom_comp_quotientMk_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/JacobsonQuotientRetraction.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/JacobsonQuotientRetraction.lean#L231). The attribute's comment: “the ring-theoretic statement the lemma reduces to: for A w-contractible and I in the Jacobson radical, a factorization A -> B -> A/I with A -> B ind-etale has a unique retraction B -> A compatible with the maps to A/I; the source's B/IB = A/I x R splitting is not used, see the module docstring”.

> **The ring-theoretic content of Stacks 09AC.** Let `A` be a w-contractible ring and `I ⊆ A`
> an ideal contained in the Jacobson radical of `A`. Every `A`-algebra map from an ind-étale
> `A`-algebra `B` to `A ⧸ I` factors through the quotient map `A → A ⧸ I` by a unique `A`-algebra
> map `B → A`.

```lean
theorem existsUnique_algHom_comp_quotientMk_eq (A : Type u) [CommRing A]
    (hA : ProetaleWContractible.IsWContractible.{u, u} A) (I : Ideal A)
    (hI : I ≤ Ring.jacobson A) (B : Type u) [CommRing B] [Algebra A B]
    (hB : StacksDraft.IndEtale A B) (φ : B →ₐ[A] A ⧸ I) :
    ∃! σ : B →ₐ[A] A, (Ideal.Quotient.mkₐ A I).comp σ = φ
```

**`AlgebraicGeometry.ProEtale.appProetaleLiftBaseChangeObjIsoOfIsWContractible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteLiftOfClosedFibre.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/Site/AppSiteLiftOfClosedFibre.lean#L157). The attribute's comment: “the identification v(U x\_X Z) = U, to which Stacks 09BL (1) reduces the lemma; hypothesis (1) is w-contractibility of Gamma(U, O\_U) and hypothesis (2) is containment of the ideal of the closed fibre in its Jacobson radical”.

> **Stacks 09AC.** Let `i : Z ⟶ X` be a closed immersion of affine schemes and let `U` be an
> object of `X_app` which is affine and weakly contractible and every point of which specializes
> to a point of `U ×_X Z`. Then `U` is the lift of its closed fibre: `v(U ×_X Z) ≅ U`.

```lean
public noncomputable def appProetaleLiftBaseChangeObjIsoOfIsWContractible (U : AppSmallProetale X)
    (hU : ProetaleWContractible.IsWContractible.{u, u} (appAlg U).obj.right)
    (hjac : (appTopKer i).map (appAlg U).obj.hom.hom ≤ Ring.jacobson (appAlg U).obj.right) :
    (appProetaleLift i).obj ((appProetaleBaseChange i).obj U) ≅ U
```

## Tag 09BM, a lemma

[Tag 09BM](https://stacks.math.columbia.edu/tag/09BM) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exact_smallProetalePushforward_of_isRetrocompact_compl_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/ClosedImmersionPushforwardExact.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/ClosedImmersionPushforwardExact.lean#L156).

> **Stacks 09BM.** Let `i : Z → X` be a closed immersion of schemes whose open complement is
> retrocompact. Then direct image of abelian sheaves along the induced morphism of small pro-étale
> sites is exact.

```lean
theorem exact_smallProetalePushforward_of_isRetrocompact_compl_range
    (B : BigProetaleSite.{u}) {Z X : B.Scheme} (i : Z ⟶ X)
    [IsClosedImmersion (B.inclusion.map i)]
    (hi : IsRetrocompact ((Set.range (B.inclusion.map i).base)ᶜ)) :
    exactFunctor
      (Sheaf (SmallProetale.topology B Z.obj Z.property) AddCommGrpCat.{u + 1})
      (Sheaf (SmallProetale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      ((smallProetaleBaseChange B Z X i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallProetale.topology B X.obj X.property)
        (SmallProetale.topology B Z.obj Z.property))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.25, Tag 09A9](https://stacks.math.columbia.edu/tag/09A9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
