---
declaration: section
origin: cited
lean: Stacks.StrictlyHenselian.subsingleton_etaleCohomology_smallEtaleTopology, Stacks.StrictlyHenselian.isIso_globalSectionsToEtaleStalk, Stacks.StrictlyHenselian.globalSections_preservesFiniteColimits, Stacks.StrictlyHenselian.subsingleton_etaleCohomology, AlgebraicGeometry.SmallEtale.etalePushforward_exact_of_isFinite, AlgebraicGeometry.finitePushforwardStalkToProduct_bijective, AlgebraicGeometry.finitePushforwardStalkEquiv, AlgebraicGeometry.finitePushforwardStalkEquiv_apply
statement: formalized
proof: formalized
---

# 59.55 Vanishing of finite higher direct images

Section 59.55 of the Stacks Project, [Tag 03QN](https://stacks.math.columbia.edu/tag/03QN). 6 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03QO, a lemma

[Tag 03QO](https://stacks.math.columbia.edu/tag/03QO) in the Stacks Project.

**`Stacks.StrictlyHenselian.subsingleton_etaleCohomology_smallEtaleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianSmallEtaleVanishing.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianSmallEtaleVanishing.lean#L92). The attribute's comment: “vanishing of positive-degree étale cohomology, on the small étale site”.

> Positive-degree étale cohomology of an abelian sheaf on the small étale site of the
> spectrum of a strictly henselian local ring vanishes.

```lean
public theorem subsingleton_etaleCohomology_smallEtaleTopology
    (R : Type u) [CommRing R] [StrictlyHenselianLocalRing R]
    [HasExt.{w} (Sheaf (Spec (.of R)).smallEtaleTopology AddCommGrpCat.{u + 1})]
    (F : Sheaf (Spec (.of R)).smallEtaleTopology AddCommGrpCat.{u + 1})
    (p : ℕ) (hp : 1 ≤ p) :
    Subsingleton (Sheaf.H.{w, u + 1} F p)
```

**`Stacks.StrictlyHenselian.isIso_globalSectionsToEtaleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean#L560). The attribute's comment: “global sections equal the closed geometric stalk”. References: SGA 4 VIII (8.6), “strictly henselian, n=0”.

> For a strictly henselian local ring, the canonical global-sections-to-stalk
> map is an isomorphism for every sheaf of sets.

```lean
public theorem isIso_globalSectionsToEtaleStalk
    [StrictlyHenselianLocalRing R]
    (hs : s.LiesOver (IsLocalRing.closedPoint R))
    [HasWeakSheafify (SmallEtale.topology B (Spec (.of R)) hS)
      (Type (u + 1))]
    (F : Sheaf (SmallEtale.topology B (Spec (.of R)) hS)
      (Type (u + 1))) :
    IsIso (globalSectionsToEtaleStalk B R hS s F)
```

**`Stacks.StrictlyHenselian.globalSections_preservesFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean#L647). The attribute's comment: “exactness of global sections”.

> Global sections of abelian étale sheaves on a strictly henselian local
> scheme are exact. As a right adjoint, this functor already preserves limits.

```lean
public instance globalSections_preservesFiniteColimits
    [StrictlyHenselianLocalRing R]
    [HasSheafify (SmallEtale.topology B (Spec (.of R)) hS)
      AddCommGrpCat.{u + 1}] :
    PreservesFiniteColimits
      (Sheaf.Γ (SmallEtale.topology B (Spec (.of R)) hS)
        AddCommGrpCat.{u + 1})
```

**`Stacks.StrictlyHenselian.subsingleton_etaleCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianVanishing.lean#L665). The attribute's comment: “vanishing of positive-degree étale cohomology”. References: SGA 4 VIII (8.6), “strictly henselian, p≥1”.

> Positive-degree étale cohomology of an abelian sheaf over a strictly
> henselian local scheme vanishes.

```lean
public theorem subsingleton_etaleCohomology
    [StrictlyHenselianLocalRing R]
    [HasSheafify (SmallEtale.topology B (Spec (.of R)) hS)
      AddCommGrpCat.{u + 1}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B (Spec (.of R)) hS)
      AddCommGrpCat.{u + 1})]
    (F : Sheaf (SmallEtale.topology B (Spec (.of R)) hS)
      AddCommGrpCat.{u + 1}) (p : ℕ) (hp : 1 ≤ p) :
    Subsingleton (Sheaf.H.{w, u + 1} F p)
```

## Tag 03QP, a proposition

[Tag 03QP](https://stacks.math.columbia.edu/tag/03QP) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.etalePushforward_exact_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L264). The attribute's comment: “exactness of direct image along a finite morphism”.

> Direct image of abelian étale sheaves along a finite morphism is exact.

```lean
public theorem etalePushforward_exact_of_isFinite :
    exactFunctor _ _ (etalePushforward.{u, u + 1} B fbar)
```

**`AlgebraicGeometry.finitePushforwardStalkToProduct_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean#L691). The attribute's comment: “part (1): the stalk of a finite pushforward, for sheaves of sets”.

> **Stacks Project, Tag 03QP, part (1), sheaves of sets.** For a finite morphism the
> comparison map from the stalk of a direct image to the product of the stalks over the lifts of
> the geometric point is bijective.

```lean
public theorem finitePushforwardStalkToProduct_bijective
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsFinite (B.inclusion.map f)] (y : GeometricPoint Y.1)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1))) :
    Function.Bijective (finitePushforwardStalkToProduct B f y F)
```

**`AlgebraicGeometry.finitePushforwardStalkEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean#L709). The attribute's comment: “part (1): the stalk of a finite pushforward, for sheaves of sets”. References: SGA 4 VIII (5.5), “partial”.

> **Stacks Project, Tag 03QP, part (1), sheaves of sets.** The stalk at a geometric point `y`
> of the direct image of a sheaf of sets along a finite morphism is the product of the stalks of
> the sheaf over the lifts of `y`.

```lean
public def finitePushforwardStalkEquiv
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsFinite (B.inclusion.map f)] (y : GeometricPoint Y.1)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1))) :
    etaleStalk B Y.1 Y.property y
      (((smallEtaleBaseChange B f).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B Y.1 Y.property)
        (SmallEtale.topology B X.1 X.property)).obj F).obj ≃
      (∀ x : {g : y.source ⟶ X.1 // g ≫ B.inclusion.map f = y.hom},
        etaleStalk B X.1 X.property
          (geometricPointLift (B.inclusion.map f) y x) F.obj)
```

**`AlgebraicGeometry.finitePushforwardStalkEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/Bijectivity.lean#L726). The attribute's comment: “part (1): the stalk of a finite pushforward, for sheaves of sets”.

> **Stacks Project, Tag 03QP, part (1), sheaves of sets.** Each component of the product
> decomposition of the stalk is the canonical stalk map at the corresponding lift.

```lean
public theorem finitePushforwardStalkEquiv_apply
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsFinite (B.inclusion.map f)] (y : GeometricPoint Y.1)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1)))
    (z : etaleStalk B Y.1 Y.property y
      (((smallEtaleBaseChange B f).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B Y.1 Y.property)
        (SmallEtale.topology B X.1 X.property)).obj F).obj)
    (x : {g : y.source ⟶ X.1 // g ≫ B.inclusion.map f = y.hom}) :
    finitePushforwardStalkEquiv B f y F z x =
      finitePushforwardStalkComponent B f y F x z
```

**`AlgebraicGeometry.stalkPushforwardIsoDirectSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean#L560). The attribute's comment: “part (1): the stalk of a finite pushforward, for abelian sheaves”.

> The stalk of a finite direct image is canonically the direct sum of its
> stalks at the geometric lifts.

```lean
public noncomputable def stalkPushforwardIsoDirectSum
    [IsFinite (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1}) :
    AlgebraicGeometry.etaleStalk B Y.1 Y.property y
        (((smallEtaleBaseChange B f).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B Y.1 Y.property)
          (SmallEtale.topology B X.1 X.property)).obj F).obj ≅
      ∐ fun x : GeometricLifts B f y =>
        AlgebraicGeometry.etaleStalk B X.1 X.property
          (geometricPointLift
            (B.inclusion.map f) y x) F.obj
```

**`AlgebraicGeometry.stalkPushforwardIsoDirectSum_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean#L601). The attribute's comment: “part (1): the stalk of a finite pushforward, for abelian sheaves”.

> On each component, the finite direct-image stalk decomposition takes a
> section over a neighborhood of `y` to its germ at a lift `x`, after pulling
> the neighborhood back to `X`. The auxiliary neighborhood `V` is any étale
> neighborhood of `x` mapping to that pullback and carrying the specified point.

```lean
public theorem stalkPushforwardIsoDirectSum_germ
    [IsFinite (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1})
    (x : GeometricLifts B f y)
    (U : (geometricPointFiber B Y.1 Y.property y).Elements)
    (V : (geometricPointFiber B X.1 X.property
      (geometricPointLift
        (B.inclusion.map f) y x)).Elements)
    (t : V.1 ⟶ (smallEtaleBaseChange B f).obj U.1)
    (hU : V.2.1 ≫ (SmallEtale.toScheme B X.1 X.property).map t ≫
        B.inclusion.map (pullback.fst U.1.obj.hom f) = U.2.1)
    (hX : V.2.1 ≫ (SmallEtale.toScheme B X.1 X.property).map t ≫
        B.inclusion.map (pullback.snd U.1.obj.hom f) = x.1) :
    colimit.ι
        ((CategoryOfElements.π (geometricPointFiber B Y.1 Y.property y)).op ⋙
          (((smallEtaleBaseChange B f).sheafPushforwardContinuous
            AddCommGrpCat.{u + 1}
            (SmallEtale.topology B Y.1 Y.property)
            (SmallEtale.topology B X.1 X.property)).obj F).obj)
        (op U) ≫
      (stalkPushforwardIsoDirectSum B f y F).hom ≫
      (by classical exact Limits.Sigma.π _ x) =
    F.obj.map t.op ≫
      colimit.ι
        ((CategoryOfElements.π (geometricPointFiber B X.1 X.property
          (geometricPointLift
            (B.inclusion.map f) y x))).op ⋙ F.obj)
    (op V)
```

**`AlgebraicGeometry.stalkPushforwardIsoDirectSum_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardStalk/DirectSum.lean#L635). The attribute's comment: “part (1): the stalk of a finite pushforward, for abelian sheaves”.

> The finite direct-sum decomposition is natural in the abelian sheaf.

```lean
public theorem stalkPushforwardIsoDirectSum_natural
    [IsFinite (B.inclusion.map f)]
    {F G : Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1}}
    (α : F ⟶ G) :
    etaleStalkMap B Y.1 Y.property y
        (((smallEtaleBaseChange B f).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B Y.1 Y.property)
          (SmallEtale.topology B X.1 X.property)).map α) ≫
        (stalkPushforwardIsoDirectSum B f y G).hom =
      (stalkPushforwardIsoDirectSum B f y F).hom ≫
    Limits.Sigma.map (fun x : GeometricLifts B f y =>
          etaleStalkMap B X.1 X.property
            (geometricPointLift
              (B.inclusion.map f) y x) α)
```

**`Stacks.EtaleCohomology.isZero_rightDerived_smallEtalePushforwardAb_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralHigherDirectImage.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralHigherDirectImage.lean#L55). The attribute's comment: “part (2): vanishing of the positive higher direct images”. References: SGA 4 Vbis (4.3.4); SGA 4½ Arcata (2.3.6).

> **The positive higher direct images along an integral morphism vanish.** For a finite
> morphism this is the acyclicity half of Stacks Project Tag 03QP, finiteness implying
> integrality.

```lean
public theorem isZero_rightDerived_smallEtalePushforwardAb_of_isIntegralHom
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f]
    (F : Sheaf (smallEtaleTopology X) Ab.{u + 1}) (q : ℕ) (hq : 0 < q) :
    IsZero (((smallEtalePushforwardAb f).rightDerived q).obj F)
```

**`Stacks.EtaleCohomology.isZero_rightDerived_etaleAbelianDirectImage_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/IntegralDirectImageAcyclic.lean#L167). The attribute's comment: “part (2) at the coefficients of proper base change”. References: SGA 4 VIII (5.5), “more general”; SGA 4 VIII (5.6); SGA 4 Vbis (4.3.4); SGA 4 XII (5.3bis), “special case”; SGA 4 XIV (1.11), “partial”; SGA 4 XVII (4.3.1), “special case”; SGA 4½ Arcata (2.3.6).

> **Stacks 03QP, part (2), at the coefficients of the proper base change development.** The
> positive higher direct images of an abelian sheaf along an integral morphism of schemes vanish:
> an integral morphism — a finite morphism, for instance — is acyclic for étale cohomology.
>
> Direct image is exact, and applying an exact functor degreewise to an injective resolution
> gives a resolution again, so the homology of the image complex vanishes in positive degrees.

```lean
public theorem isZero_rightDerived_etaleAbelianDirectImage_of_isIntegralHom
    (f : X ⟶ Y) [IsIntegralHom f]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) (q : ℕ) (hq : 0 < q) :
    IsZero (((etaleAbelianDirectImage.{u, v} f).rightDerived q).obj F)
```

**`Stacks.EtaleCohomology.TorsionModules.isZero_rightDerived_modulePushforward_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionModulesCurves/FinitePushforwardAcyclic.lean#L156). The attribute's comment: “part (2), for sheaves of Λ-modules on the small étale sites of Tag 021B”. References: SGA 4 VIII (5.5), “more general”; SGA 4 VIII (5.6), “more general”; SGA 4 Vbis (4.3.4), “more general”; SGA 4 XIV (1.11), “partial”; SGA 4½ Arcata (2.3.6), “more general”.

> **Stacks 03QP, part (2), for sheaves of `Λ`-modules on the small étale sites of Stacks
> 021B.** For `f` with integral underlying morphism of schemes — a finite morphism, for instance —
> the higher direct images of a sheaf of `Λ`-modules along `f` vanish: `R^q f_*ℱ = 0` for every
> `q > 0`. The direct image is exact by `modulePushforward_exact_of_isIntegralHom`, and the higher
> right derived functors of an exact functor vanish.

```lean
theorem isZero_rightDerived_modulePushforward_of_isIntegralHom
    [IsIntegralHom (B.inclusion.map f)]
    (ℱ : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w r} Λ))
    (q : ℕ) (hq : 0 < q) :
    IsZero (((modulePushforward.{u, max w r} B Λ f).rightDerived q).obj ℱ)
```

## Tag 0959, a lemma

[Tag 0959](https://stacks.math.columbia.edu/tag/0959) in the Stacks Project.

**`AlgebraicGeometry.isIso_smallEtaleBaseChangeNatTrans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardBaseChange.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardBaseChange.lean#L709).

> Consider a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> of schemes of a big étale site with `f` finite, and a sheaf of sets `F` on the small étale site
> of `X`. Then the canonical comparison `g⁻¹ f_* F ⟶ f'_* (g')⁻¹ F` is an isomorphism.

```lean
theorem isIso_smallEtaleBaseChangeNatTrans
    (sq : IsPullback (B.inclusion.map g') (B.inclusion.map f') (B.inclusion.map f)
      (B.inclusion.map g))
    [IsFinite (B.inclusion.map f)] (h : g' ≫ f = f' ≫ g)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1))) :
    IsIso ((smallEtaleBaseChangeNatTrans B g' f' f g h).app F)
```

**`Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleBaseChangeAbFinite.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleBaseChangeAbFinite.lean#L307). The attribute's comment: “for abelian sheaves, at the comparison `smallEtaleBaseChangeAb` of [Stacks, Tag 0F02]; the morphism is finite, not merely integral, so this is 0959 and not 0EYP”.

> **Base change of an abelian direct image along a finite morphism, at the comparison
> `Stacks.EtaleCohomology.smallEtaleBaseChangeAb`.** For a cartesian square
> ```
> Y' --π'--> Y
> |e'        |e
> v          v
> T' --π---> T
> ```
> of schemes with `π` finite, the canonical comparison `e⁻¹ π_* ⟶ π'_* (e')⁻¹` of abelian sheaves on
> the small étale sites is an isomorphism.
>
> This is [Stacks, Tag 0959] for abelian coefficients, stated at the comparison which the
> higher-direct-image development of [Stacks, Tag 0F02] uses. The abelian statement at the
> comparison of the proper base change development is
> `Stacks.EtaleCohomology.isIso_etaleAbelianBaseChange_of_isFinite`; the passage between the two
> comparisons is
> `Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_of_isIso_etaleAbelianBaseChange`, and no big
> étale site occurs in the hypotheses.
>
> [Stacks, Tag 0EYP] is this statement with `π` merely *integral*. It does not follow from this one:
> the source's passage from a finite morphism to an integral one presents the comparison as a
> colimit of the comparisons for the finite stages of the integral morphism, and that presentation
> is not available in this library for abelian coefficients.

```lean
public theorem isIso_smallEtaleBaseChangeAb_of_isFinite {Y Y' T T' : Scheme.{u}} (e : Y ⟶ T)
    (π : T' ⟶ T) (π' : Y' ⟶ Y) (e' : Y' ⟶ T') (sq : IsPullback π' e' e π) [IsFinite π] :
    IsIso (smallEtaleBaseChangeAb e π π' e' sq.w)
```

## Tag 0EYP, a lemma

[Tag 0EYP](https://stacks.math.columbia.edu/tag/0EYP) in the Stacks Project.

**`AlgebraicGeometry.isIso_smallEtaleBaseChangeNatTrans_of_isIntegralHom_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralPushforwardBaseChangeLimitUnconditional.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralPushforwardBaseChangeLimitUnconditional.lean#L621). References: SGA 4 VIII (5.5), “more general”.

> **Stacks Project, Tag 0EYP.** Consider a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> of schemes of a big étale site with `f` integral, and a sheaf of sets `F` on the small étale site
> of `X`, with values in `Type (max (u + 1) v)` for any universe `v`. Then the canonical
> comparison `g⁻¹ f_* F ⟶ f'_* (g')⁻¹ F` is an isomorphism.
>
> The comparison is checked on stalks at the geometric points `y'` of `Y'`. Both stalks embed into
> the product of the stalks of `F` over the lifts of `y'`, because for an integral morphism the
> stalk of a direct image is detected at the lifts
> (`AlgebraicGeometry.finitePushforwardStalkComponent_injective_univ`); this gives injectivity. For
> surjectivity, an affine open neighbourhood `V` of the image of `y'` in `Y` is chosen, the integral
> morphism `X ×_Y V ⟶ V` is written as a limit of finite morphisms (Stacks 09YZ), the family of
> germs attached to an element of the target is shown to be given by stage sections on cylinders
> of lifts (`AlgebraicGeometry.exists_stage_forall_cylinderGerm_eq_univ`), finitely many cylinders
> cover the lifts (`AlgebraicGeometry.exists_finset_forall_exists_comp_eq_of_isLimit`), and the
> finite case of the stalk computation, Stacks 03QP, at a common stage produces the required germ of
> `f_* F`.

```lean
theorem isIso_smallEtaleBaseChangeNatTrans_of_isIntegralHom_univ
    (sq : IsPullback (B.inclusion.map g') (B.inclusion.map f') (B.inclusion.map f)
      (B.inclusion.map g))
    [IsIntegralHom (B.inclusion.map f)] (h : g' ≫ f = f' ≫ g)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (max (u + 1) v))) :
    IsIso ((smallEtaleBaseChangeNatTransUniv B g' f' f g h).app F)
```

## Tag 09Z2, a lemma

[Tag 09Z2](https://stacks.math.columbia.edu/tag/09Z2) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_cechSheafSpectralSequence_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteDescent/SpectralSequenceFunctorial.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteDescent/SpectralSequenceFunctorial.lean#L476).

> **[Stacks, Tag 09Z2].** Let `f : X ⟶ Y` be a surjective finite morphism of schemes, let
> `f_n : X_n ⟶ Y` be the structure map of the `(n + 1)`-fold fibre product of `X` over `Y`, and for
> an abelian sheaf `F` on the small étale site of `Y` put `F_n = f_{n,*}f_n^{-1}F`. Then:
>
> * there is an exact sequence `0 → F → F_0 → F_1 → F_2 → ⋯` on `Y_étale`, with augmentation the
>   canonical map `F ⟶ f_*f^{-1}F`;
> * there is a cohomological spectral sequence with
>   `E_1^{p,q} = H^q_étale(X_p, f_p^{-1}F)` converging to `H^{p+q}(Y_étale, F)`, convergence
>   meaning that each `H^n(Y_étale, F)` carries a finite decreasing filtration `Fil` whose graded
>   pieces are the stable terms of the spectral sequence;
> * **this spectral sequence is functorial in `F`**: it is produced by a *functor* `E` of `F`, the
>   first-page identification is an isomorphism of functors of `F`, and the filtration of the
>   abutment is carried into itself by the map a morphism `F ⟶ G` induces on cohomology.
>
> The exact sequence is `Stacks.EtaleCohomology.exists_exact_cechSheafSequence`; the functor is
> `Stacks.EtaleCohomology.cechSpectralSequenceFunctor`, the augmented cobar complex of the monad
> `f_*f^{-1}` followed by the hyper-`Ext` spectral sequence of [Stacks, Tag 0AVI].

```lean
public theorem exists_cechSheafSpectralSequence_functorial [IsFinite f] [Surjective f] :
    (∀ F : Sheaf (smallEtaleTopology Y) Ab.{u + 1},
        ∃ (d : ∀ n : ℕ, cechSheaf f F n ⟶ cechSheaf f F (n + 1))
          (haug : cechAug f F ≫ d 0 = 0) (hdd : ∀ n : ℕ, d n ≫ d (n + 1) = 0),
          Mono (cechAug f F) ∧ (ShortComplex.mk _ _ haug).Exact ∧
            ∀ n : ℕ, (ShortComplex.mk _ _ (hdd n)).Exact) ∧
      ∃ E : Sheaf (smallEtaleTopology Y) Ab.{u + 1} ⥤
          CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 1,
        (∀ p q : ℕ, Nonempty (E ⋙
            CategoryTheory.SpectralSequence.pageFunctor AddCommGrpCat.{u + 1} _ 1 1 (le_refl 1) ⋙
              HomologicalComplex.eval AddCommGrpCat.{u + 1} _ ((p : ℤ), (q : ℤ)) ≅
            smallEtalePullbackAb (cechProjection f p) ⋙
              sheafHFunctor (cechScheme f p) q)) ∧
          ∃ (Fil : ∀ (_p : ℤ) (n : ℕ) (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}),
                Subobject ((sheafHFunctor Y n).obj F))
            (hFil : ∀ (p p' : ℤ) (n : ℕ) (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}),
                p ≤ p' → Fil p' n F ≤ Fil p n F),
            (∀ (p : ℤ) (n : ℕ) (F G : Sheaf (smallEtaleTopology Y) Ab.{u + 1}) (φ : F ⟶ G),
                (Subobject.«exists» ((sheafHFunctor Y n).map φ)).obj (Fil p n F) ≤
                  Fil p n G) ∧
              (∀ (n : ℕ) (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}),
                  ∃ s t : ℤ, s ≤ t ∧ Fil s n F = ⊤ ∧ Fil t n F = ⊥) ∧
                ∀ (p q : ℤ) (n : ℕ) (F : Sheaf (smallEtaleTopology Y) Ab.{u + 1}),
                  p + q = (n : ℤ) → ∃ r₀ : ℤ, 1 ≤ r₀ ∧
                    ∀ (r : ℤ) (hr : 1 ≤ r), r₀ ≤ r →
                      ((E.obj F).page r hr).d (p, q) (p + r, q + 1 - r) = 0 ∧
                        ((E.obj F).page r hr).d (p - r, q + r - 1) (p, q) = 0 ∧
                          Nonempty (((E.obj F).page r hr).X (p, q) ≅
                            cokernel (Subobject.ofLE (Fil (p + 1) n F) (Fil p n F)
                              (hFil p (p + 1) n F (by omega))))
```

**`AlgebraicGeometry.mono_smallEtaleUnitAb_of_isFinite_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteSurjectiveAbelianUnit.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteSurjectiveAbelianUnit.lean#L100). The attribute's comment: “exactness at `ℱ` of `0 → ℱ → ℱ₀ → ℱ₁ → ⋯`, i.e. injectivity of the augmentation `ℱ ⟶ ℱ₀ = f_*f^{-1}ℱ`; exactness in the higher degrees and the spectral sequence are not proved here”.

> **Stacks 09Z2, exactness at `ℱ`.** For a finite surjective morphism of schemes the unit
> `ℱ ⟶ f_* f^{-1}ℱ` of the inverse-image/direct-image adjunction on abelian sheaves on the small
> étale sites is a monomorphism. The zeroth level of the Čech nerve of `f` being `X` itself, this
> is injectivity of the augmentation `ℱ ⟶ ℱ₀`.

```lean
public theorem mono_smallEtaleUnitAb_of_isFinite_of_surjective
    [IsFinite (B.inclusion.map f)] [Surjective (B.inclusion.map f)]
    (G : Sheaf (SmallEtale.topology B Y.1 Y.property) AddCommGrpCat.{u + 1}) :
    Mono (((smallEtaleBaseChange B f).sheafAdjunctionContinuous AddCommGrpCat.{u + 1}
      (SmallEtale.topology B Y.1 Y.property)
      (SmallEtale.topology B X.1 X.property)).unit.app G)
```

## Tag 09Z3, a remark

[Tag 09Z3](https://stacks.math.columbia.edu/tag/09Z3) in the Stacks Project.

**`Stacks.EtaleCohomology.globalSectionsPullback_isEqualizer_of_isFinite_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/FiniteSurjectiveDescent.lean, line 1344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/FiniteSurjectiveDescent.lean#L1344). The attribute's comment: “the displayed equality `Γ(Y, 𝒢) = Equalizer (Γ(X₀, f₀⁻¹𝒢) ⇉ Γ(X₁, f₁⁻¹𝒢))`, for a finite surjective `f : X ⟶ Y` and a sheaf of sets `𝒢` on the small étale site of `Y`, with `X₀ = X`, `f₀ = f`, `X₁ = X ×_Y X` and `f₁` the structure morphism of `X₁`: the canonical comparison on global sections is injective with image exactly the equalizer”. References: SGA 1 XIII (1.11), “partial”.

> **[Stacks, Tag 09Z3].**  Let `f : X ⟶ Y` be a finite surjective morphism of schemes and let
> `𝒢` be a sheaf of sets on the small étale site of `Y`.  The first two levels of the Čech nerve of
> `f` are `X₀ = X` with `f₀ = f`, and `X₁ = X ×_Y X` with `f₁ = pr₀ ≫ f = pr₁ ≫ f`.  Then
>
> `Γ(Y, 𝒢) = Equalizer (Γ(X₀, f₀⁻¹𝒢) ⇉ Γ(X₁, f₁⁻¹𝒢))`:
>
> the canonical comparison `Γ(Y, 𝒢) ⟶ Γ(X₀, f₀⁻¹𝒢)` on global sections is injective, and a
> section of `f₀⁻¹𝒢` over `X₀` is in its image exactly when its two pullbacks to `X₁` agree.
>
> The comparison is `Stacks.EtaleCohomology.etaleGlobalPullback`, which is by definition the
> component at `𝒢` of
> `Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageComparison`;  the two parallel
> arrows are the two instances of `Stacks.EtaleCohomology.relativeGlobalSectionsMap` attached to
> the two factorizations `f₁ = pr₀ ≫ f` and `f₁ = pr₁ ≫ f` of the structure morphism of `X₁`.

```lean
public theorem globalSectionsPullback_isEqualizer_of_isFinite_surjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f] [Surjective f]
    (G : Sheaf (Scheme.smallEtaleTopology Y) (Type (max (u + 1) v))) :
    Function.Injective (etaleGlobalPullback f G) ∧
      ∀ t : (etaleGlobalSections X).obj ((smallEtaleInverseImage.{u, v} f).obj G),
        relativeGlobalSectionsMap f (pullback.fst f f) (pullback.fst f f ≫ f) rfl G t =
            relativeGlobalSectionsMap f (pullback.snd f f) (pullback.fst f f ≫ f)
              pullback.condition G t ↔
          ∃ s : (etaleGlobalSections Y).obj G, etaleGlobalPullback f G s = t
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.55, Tag 03QN](https://stacks.math.columbia.edu/tag/03QN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
