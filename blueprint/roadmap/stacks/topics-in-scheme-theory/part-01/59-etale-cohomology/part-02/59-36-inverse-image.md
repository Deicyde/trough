---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtaleInverseImage, Stacks.EtaleCohomology.smallEtaleInverseImageAdjunction, Stacks.EtaleCohomology.smallEtalePullbackAb, Stacks.EtaleCohomology.smallEtaleAdjunctionAb, Stacks.EtaleCohomology.inverseImageIsoSheafifyColimitPresheaf, AlgebraicGeometry.smallEtalePullbackStalkIso, AlgebraicGeometry.smallEtalePullbackStalkIso_germ, AlgebraicGeometry.smallEtalePullbackSheafFiberIso
statement: formalized
proof: formalized
---

# 59.36 Inverse image

Section 59.36 of the Stacks Project, [Tag 03PZ](https://stacks.math.columbia.edu/tag/03PZ). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03Q0, a definition

[Tag 03Q0](https://stacks.math.columbia.edu/tag/03Q0) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.smallEtaleInverseImage`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/InverseImage.lean#L89), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L52) (StacksFrontier): “the inverse image `f⁻¹` on sheaves of sets”.
- [`Stacks.EtaleCohomology.smallEtaleInverseImageAdjunction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedSubschemeSections.lean#L226), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L55) (StacksFrontier): “`f⁻¹` on sheaves of sets is characterised by its adjunction `Hom(f⁻¹ G, F) = Hom(G, f_* F)`”.
- [`Stacks.EtaleCohomology.smallEtalePullbackAb`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/BaseChangeCondition.lean#L158), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L59) (StacksFrontier): “the inverse image `f⁻¹` on sheaves of abelian groups”.
- [`Stacks.EtaleCohomology.smallEtaleAdjunctionAb`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PropertyAPushforward.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L62) (StacksFrontier): “`f⁻¹` on sheaves of abelian groups is characterised by its adjunction `Hom(f⁻¹ G, F) = Hom(G, f_* F)`”.

## Tag 04I3, an equation

[Tag 04I3](https://stacks.math.columbia.edu/tag/04I3) in the Stacks Project.

**`Stacks.EtaleCohomology.inverseImageIsoSheafifyColimitPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L119). The attribute's comment: “for any left adjoint `f⁻¹` of `f_*` on sheaves of sets of the small étale sites, `f⁻¹ G` is the sheafification of `U ↦ colim G(V)` over the pairs `(V, U ⟶ X ×_Y V)`”.

> **Stacks 04I3.** Let `f : X ⟶ Y` be a morphism of schemes and let `f⁻¹` be any left adjoint
> of the direct image `f_*` on sheaves of sets of the small étale sites (Stacks 03Q0). Then for
> every sheaf `G` on `Y_étale`, `f⁻¹ G` is the sheaf associated to the presheaf
> `U ↦ colim_{(V, φ : U ⟶ X ×_Y V)} G(V)`, namely `smallEtaleColimitPresheaf f G`. The isomorphism
> is natural, being the composite of the uniqueness of left adjoints with the uniqueness of left
> Kan extensions.

```lean
def inverseImageIsoSheafifyColimitPresheaf
    {L : Sheaf (smallEtaleTopology Y) (Type (max (u + 1) v)) ⥤
      Sheaf (smallEtaleTopology X) (Type (max (u + 1) v))}
    (adj : L ⊣ (smallEtaleBaseChange f).sheafPushforwardContinuous
      (Type (max (u + 1) v)) (smallEtaleTopology Y) (smallEtaleTopology X))
    (G : Sheaf (smallEtaleTopology Y) (Type (max (u + 1) v))) :
    L.obj G ≅
      (presheafToSheaf (smallEtaleTopology X) (Type (max (u + 1) v))).obj
        (smallEtaleColimitPresheaf.{u, v} f G)
```

## Tag 03Q1, a lemma

[Tag 03Q1](https://stacks.math.columbia.edu/tag/03Q1) in the Stacks Project.

**`AlgebraicGeometry.smallEtalePullbackStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Basic.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Basic.lean#L161). The attribute's comment: “pullback\_stalk”. References: SGA 4½ Arcata (2.3.3), “(f^*F)\_x̄ = F\_f(x̄)”.

> **Stacks 03Q1.** Pullback of an étale sheaf commutes naturally with taking stalks at a
> geometric point.

```lean
public def smallEtalePullbackStalkIso (B : BigEtaleSite.{u})
    {S T : B.Scheme} (f : T ⟶ S) (x : GeometricPoint T.1) :
    (smallEtaleBaseChange B f).sheafPullback (Type (u + 1))
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property) ⋙
      etaleStalkFunctor.{u, u + 1} B T.1 T.property x ≅
    etaleStalkFunctor.{u, u + 1} B S.1 S.property (x.map (B.inclusion.map f))
```

**`AlgebraicGeometry.smallEtalePullbackStalkIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Basic.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Basic.lean#L212). The attribute's comment: “pullback\_stalk”.

> **Stacks 03Q1.** The comparison sends the germ of a section pulled back to a pointed
> étale neighborhood to the germ of the original section.

```lean
public theorem smallEtalePullbackStalkIso_germ (B : BigEtaleSite.{u})
    {S T : B.Scheme} (f : T ⟶ S) (x : GeometricPoint T.1)
    (F : Sheaf (SmallEtale.topology B S.1 S.property) (Type (u + 1)))
    (U : (geometricPointFiber B T.1 T.property x).Elements)
    (V : (geometricPointFiber B S.1 S.property
      (x.map (B.inclusion.map f))).Elements)
    (a : U.1 ⟶ (smallEtaleBaseChange B f).obj V.1)
    (ha : U.2.1 ≫ (SmallEtale.toScheme B T.1 T.property).map a ≫
        B.inclusion.map (pullback.fst V.1.obj.hom f) = V.2.1)
    (t : F.obj.obj (Opposite.op V.1)) :
    ((smallEtalePullbackStalkIso B f x).hom.app F)
      ((colimit.ι
        ((Functor.Elements.π (geometricPointFiber B T.1 T.property x)).op ⋙
          (((smallEtaleBaseChange B f).sheafPullback (Type (u + 1))
            (SmallEtale.topology B S.1 S.property)
            (SmallEtale.topology B T.1 T.property)).obj F).obj)
        (Opposite.op U)) (pullbackSectionAlong B f F V.1 U.1 a t)) =
      (colimit.ι
        ((Functor.Elements.π (geometricPointFiber B S.1 S.property
          (x.map (B.inclusion.map f)))).op ⋙ F.obj)
        (Opposite.op V)) t
```

**`AlgebraicGeometry.smallEtalePullbackSheafFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Coefficients.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/Coefficients.lean#L76). The attribute's comment: “pullback\_stalk, arbitrary coefficients”. References: SGA 4½ Arcata (2.3.3), “(f^*F)\_x̄ = F\_f(x̄)”; SGA 4 VIII (3.4), “(F), special case”.

> **Stacks 03Q1** for arbitrary coefficients. Inverse image of a sheaf on the small étale site
> commutes naturally with the stalk at a geometric point.

```lean
public def smallEtalePullbackSheafFiberIso (B : BigEtaleSite.{u})
    {S T : B.Scheme} (f : T ⟶ S) (x : GeometricPoint T.obj)
    (A : Type uA) [Category.{vA} A] [HasColimitsOfSize.{u, u} A] [HasProducts.{u} A]
    [((smallEtaleBaseChange B f).sheafPushforwardContinuous A
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)).IsRightAdjoint] :
    (smallEtaleBaseChange B f).sheafPullback A
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property) ⋙
      (geometricPointSitePoint B T.obj T.property x).sheafFiber ≅
    (geometricPointSitePoint B S.obj S.property (x.map (B.inclusion.map f))).sheafFiber
```

**`AlgebraicGeometry.smallEtalePullbackSheafFiberIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/CoefficientsGerm.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/CoefficientsGerm.lean#L104). The attribute's comment: “pullback\_stalk on germs, arbitrary coefficients”.

> **Stacks 03Q1** for arbitrary coefficients, on germs: the comparison of the stalk of an
> inverse image with the stalk at the image point sends the germ of a pulled-back section to the
> germ of the original section.

```lean
public theorem smallEtalePullbackSheafFiberIso_germ
    (F : Sheaf (SmallEtale.topology B S.obj S.property) A)
    (U : (geometricPointFiber B T.obj T.property x).Elements)
    (V : (geometricPointFiber B S.obj S.property
      (x.map (B.inclusion.map f))).Elements)
    (a : U.1 ⟶ (smallEtaleBaseChange B f).obj V.1)
    (ha : U.2.1 ≫ (SmallEtale.toScheme B T.obj T.property).map a ≫
      B.inclusion.map (pullback.fst V.1.obj.hom f) = V.2.1) :
    pullbackSectionAlongHom B f A F V.1 U.1 a ≫
        colimit.ι ((Functor.Elements.π (geometricPointFiber B T.obj T.property x)).op ⋙
            (((smallEtaleBaseChange B f).sheafPullback A
              (SmallEtale.topology B S.obj S.property)
              (SmallEtale.topology B T.obj T.property)).obj F).obj) (op U) ≫
          (smallEtalePullbackSheafFiberIso B f x A).hom.app F =
      colimit.ι ((Functor.Elements.π (geometricPointFiber B S.obj S.property
        (x.map (B.inclusion.map f)))).op ⋙ F.obj) (op V)
```

**`AlgebraicGeometry.etaleStalkSmallEtalePullObjIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/CoefficientsGerm.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/CoefficientsGerm.lean#L179). The attribute's comment: “pullback\_stalk on germs, arbitrary coefficients, single sheaf”.

> **Stacks 03Q1** for arbitrary coefficients, on germs and on a single sheaf.

```lean
public theorem etaleStalkSmallEtalePullObjIso_germ
    (F : Sheaf (SmallEtale.topology B S.obj S.property) A)
    (U : (geometricPointFiber B T.obj T.property x).Elements)
    (V : (geometricPointFiber B S.obj S.property
      (x.map (B.inclusion.map f))).Elements)
    (a : U.1 ⟶ (smallEtaleBaseChange B f).obj V.1)
    (ha : U.2.1 ≫ (SmallEtale.toScheme B T.obj T.property).map a ≫
      B.inclusion.map (pullback.fst V.1.obj.hom f) = V.2.1) :
    pullbackSectionAlongHom B f A F V.1 U.1 a ≫
        colimit.ι ((Functor.Elements.π (geometricPointFiber B T.obj T.property x)).op ⋙
            (((smallEtaleBaseChange B f).sheafPullback A
              (SmallEtale.topology B S.obj S.property)
              (SmallEtale.topology B T.obj T.property)).obj F).obj) (op U) ≫
          (etaleStalkSmallEtalePullObjIso B f x A F).hom =
      colimit.ι ((Functor.Elements.π (geometricPointFiber B S.obj S.property
        (x.map (B.inclusion.map f)))).op ⋙ F.obj) (op V)
```

**`AlgebraicGeometry.smallEtalePullbackStalkIsoModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean#L210). The attribute's comment: “module coefficients”.

> **Stacks 03Q1 for sheaves of modules.** Inverse image of sheaves of `Λ`-modules on small
> étale sites commutes with taking stalks at a geometric point: the stalk at `x` of the inverse
> image along `f` is the stalk of the original sheaf at the image geometric point, naturally in the
> sheaf.

```lean
public def smallEtalePullbackStalkIsoModule {S T : B.Scheme} (f : T ⟶ S)
    (x : GeometricPoint T.1) :
    (smallEtaleBaseChange B f).sheafPullback (ModuleCat.{u + 1} Λ)
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property) ⋙
      etaleStalkFunctorModule B T.1 T.property Λ x ≅
    etaleStalkFunctorModule B S.1 S.property Λ (x.map (B.inclusion.map f))
```

**`AlgebraicGeometry.smallEtaleSheafPullback_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L307). The attribute's comment: “exact\_sets”.

> Inverse image along `f : T ⟶ S` between the small étale topoi preserves finite limits:
> being a morphism of sites, base change has an exact left adjoint on sheaves, and that left
> adjoint is the sheaf pullback.

```lean
public instance smallEtaleSheafPullback_preservesFiniteLimits {S T : B.Scheme} (f : T ⟶ S) :
    PreservesFiniteLimits
      ((smallEtaleBaseChange B f).sheafPullback (Type (u + 1))
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property))
```

**`Stacks.EtaleCohomology.smallEtaleAbSheafPullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageAbelian.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageAbelian.lean#L86). The attribute's comment: “exact\_abelian”.

> **Stacks 03Q1.** For a morphism of schemes `f : X ⟶ Y`, the inverse image functor
> `f⁻¹ : Ab(Y_étale) ⥤ Ab(X_étale)` between the categories of abelian sheaves on the small
> étale sites is exact: it preserves finite limits and finite colimits.

```lean
public theorem smallEtaleAbSheafPullback_exact {X Y : Scheme.{u}} (f : X ⟶ Y) :
    exactFunctor
      (Sheaf (smallEtaleTopology Y) Ab.{u + 1})
      (Sheaf (smallEtaleTopology X) Ab.{u + 1})
      ((smallEtaleBaseChange f).sheafPullback Ab.{u + 1}
        (smallEtaleTopology Y) (smallEtaleTopology X))
```

**`Stacks.EtaleCohomology.smallEtalePullbackRepresentableNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageRepresentable.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageRepresentable.lean#L160). The attribute's comment: “pullback\_representable”.

> For a morphism of schemes `f : X ⟶ Y`, the inverse image on the small étale sites carries the
> sheaf represented by an étale `Y`-scheme `V` to the sheaf represented by the base change
> `X ×_Y V`, naturally in `V`: `f⁻¹ h_V ≅ h_{X ×_Y V}` as functors of `V`.

```lean
public def smallEtalePullbackRepresentableNatIso :
    (smallEtaleTopology Y).uliftYoneda.{max (u + 1) v} ⋙
        (smallEtaleBaseChange f).sheafPullback (Type (max (u + 1) v))
          (smallEtaleTopology Y) (smallEtaleTopology X) ≅
      smallEtaleBaseChange f ⋙ (smallEtaleTopology X).uliftYoneda.{max (u + 1) v}
```

**`Stacks.EtaleCohomology.smallEtalePullbackRepresentableNatIso_app_hom_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageRepresentable.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleInverseImageRepresentable.lean#L184). The attribute's comment: “pullback\_representable”.

> Under the inverse-image/direct-image adjunction and the Yoneda bijections for sheaves,
> precomposition with the component of `smallEtalePullbackRepresentableNatIso` at `V` is the
> identity on sections over `X ×_Y V`.

```lean
public lemma smallEtalePullbackRepresentableNatIso_app_hom_comp (V : Y.Etale)
    (F : Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))
    (g : (smallEtaleTopology X).uliftYoneda.{max (u + 1) v}.obj
      ((smallEtaleBaseChange f).obj V) ⟶ F) :
    (smallEtaleTopology Y).uliftYonedaEquiv
        ((((smallEtaleBaseChange f).sheafAdjunctionContinuous (Type (max (u + 1) v))
          (smallEtaleTopology Y) (smallEtaleTopology X)).homEquiv _ _)
            (((smallEtalePullbackRepresentableNatIso.{u, v} f).app V).hom ≫ g)) =
      (smallEtaleTopology X).uliftYonedaEquiv g
```

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.leftAdjoint_preservesColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.leftAdjoint_preservesColimits#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L317) (StacksFrontier): “exact\_sets”. References: SGA 4 I (5.4), “more general”; SGA 4 I (8.7.1.7), “more general”; SGA 4 IV (3.1.3), “partial”; SGA 4 IV (4.5.1), “more general”.

## Tag 03Q2, a remark

[Tag 03Q2](https://stacks.math.columbia.edu/tag/03Q2) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L141) (StacksFrontier): “for a continuous functor `u : C₂ ⥤ C₁` the direct image on sheaves is given by `f_* F (V) = F (u V)`”.
- [`CategoryTheory.Functor.isMorphismOfSites_of_isTerminal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/MorphismOfSitesLimits.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInverseImages.lean#L145) (StacksFrontier): “a continuous `u` carrying a final object to a final object and preserving fibre products has an exact left adjoint `f⁻¹` of `f_*`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.36, Tag 03PZ](https://stacks.math.columbia.edu/tag/03PZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
