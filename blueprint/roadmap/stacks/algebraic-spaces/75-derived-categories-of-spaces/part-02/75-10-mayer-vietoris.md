---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.etaleModulePullbackStalkIso, AlgebraicGeometry.Space.etaleModulePullbackStalkIso_hom_app_moduleGerm, AlgebraicGeometry.Space.modulePullbackStalkIso, AlgebraicGeometry.Space.modulePullbackStalkIso_hom_app_moduleGerm, AlgebraicGeometry.Space.modulePullbackStalkIso_germ_add, AlgebraicGeometry.Space.modulePullbackStalkIso_germ_smul, AlgebraicGeometry.Space.restrictionPresheafFiberIso, AlgebraicGeometry.Space.restrictionPresheafFiberIso_toPresheafFiber
statement: formalized
proof: formalized
---

# 75.10 Mayer-Vietoris

Section 75.10 of the Stacks Project, [Tag 08GS](https://stacks.math.columbia.edu/tag/08GS). 10 tags here are carried by 54 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08GT, an equation

[Tag 08GT](https://stacks.math.columbia.edu/tag/08GT) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleModulePullbackStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L137). The attribute's comment: “the stalks of an étale restriction”.

> **Stacks 08GT** in its restriction reading.  The stalk at a geometric point `ū` of `U` of
> the étale restriction of an `𝒪_X`-module along an étale `j : U ⟶ X` is the stalk of that module
> at the image point `x̄ = j ∘ ū`, naturally in the module.
>
> Restriction reindexes sections along postcomposition of charts with `j`, and postcomposition is
> initial on small étale neighbourhoods, so the comparison is the germ map.

```lean
def etaleModulePullbackStalkIso (j : U ⟶ X) (hj : IsEtale B S hS j.hom)
    (y : GeometricPoint B S hS U.1) :
    etaleModulePullback.{u, m} B S hS j hj ⋙
        moduleUnderlyingPresheaf.{u, m} B S hS U.1 U.2 ⋙ stalkSetFunctor y ≅
      moduleUnderlyingPresheaf.{u, m} B S hS X.1 X.2 ⋙
        stalkSetFunctor (geometricPointMap j.hom y)
```

**`AlgebraicGeometry.Space.etaleModulePullbackStalkIso_hom_app_moduleGerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L160). The attribute's comment: “the étale restriction comparison on germs”.

> The comparison of Stacks 08GT for étale restriction is the germ map: it carries the germ at
> `ū` of a section over a chart of `U` to the germ at `x̄` of the same section, read over the
> composite chart of `X`.

```lean
theorem etaleModulePullbackStalkIso_hom_app_moduleGerm (j : U ⟶ X)
    (hj : IsEtale B S hS j.hom) (y : GeometricPoint B S hS U.1)
    (M : Modules.{u, m} B S hS X.1 X.2) (W : SmallEtaleNeighborhood y)
    (a : ((etaleModulePullback.{u, m} B S hS j hj).obj M).val.obj (Opposite.op W.chart)) :
    (etaleModulePullbackStalkIso.{u, m} B S hS j hj y).hom.app M
        (moduleGerm.{u, m} B S hS U.1 U.2
          ((etaleModulePullback.{u, m} B S hS j hj).obj M) W a) =
      moduleGerm.{u, m} B S hS X.1 X.2 M
        ((SmallEtaleNeighborhood.postcomp B S hS j hj y).obj W) a
```

**`AlgebraicGeometry.Space.modulePullbackStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L181).

> **Stacks' Equation 08GT.**  Let `j : U ⟶ X` be an étale morphism of algebraic spaces over
> `S`, let `F` be an `𝒪_X`-module and let `ū` be a geometric point of `U` with image `x̄` in `X`.
> Then the stalk of the restriction `F|_U = j^*F` at `ū` is the stalk of `F` at `x̄`, naturally
> in `F`:
>
> `(F|_U)_ū = F_x̄`.
>
> The pullback of modules is étale restriction by clause (2) of Stacks 03LV, and the stalks of an
> étale restriction are `AlgebraicGeometry.Space.etaleModulePullbackStalkIso`.

```lean
def modulePullbackStalkIso (j : U ⟶ X) (hj : IsEtale B S hS j.hom)
    (y : GeometricPoint B S hS U.1) :
    modulePullback B S hS j ⋙
        moduleUnderlyingPresheaf.{u, u} B S hS U.1 U.2 ⋙ stalkSetFunctor y ≅
      moduleUnderlyingPresheaf.{u, u} B S hS X.1 X.2 ⋙
        stalkSetFunctor (geometricPointMap j.hom y)
```

**`AlgebraicGeometry.Space.modulePullbackStalkIso_hom_app_moduleGerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L196). The attribute's comment: “the comparison on germs”.

> **Stacks 08GT, canonicity.**  The comparison `(F|_U)_ū = F_x̄` sends the germ at `ū` of a
> section of `j^*F` over a chart of `U` to the germ at `x̄` of its image under the identification
> of Stacks 03LV of the pullback with étale restriction.  So it is the canonical identification
> and not merely some natural isomorphism of the two stalk functors.

```lean
theorem modulePullbackStalkIso_hom_app_moduleGerm (j : U ⟶ X) (hj : IsEtale B S hS j.hom)
    (y : GeometricPoint B S hS U.1) (M : Modules.{u, u} B S hS X.1 X.2)
    (W : SmallEtaleNeighborhood y)
    (a : ((modulePullback B S hS j).obj M).val.obj (Opposite.op W.chart)) :
    (modulePullbackStalkIso B S hS j hj y).hom.app M
        (moduleGerm.{u, u} B S hS U.1 U.2 ((modulePullback B S hS j).obj M) W a) =
      moduleGerm.{u, u} B S hS X.1 X.2 M
        ((SmallEtaleNeighborhood.postcomp B S hS j hj y).obj W)
        (((modulePullbackIsoEtaleModulePullback B S hS j hj).hom.app M).val.app
          (Opposite.op W.chart) a)
```

**`AlgebraicGeometry.Space.modulePullbackStalkIso_germ_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L212). The attribute's comment: “additivity on germs”.

> **Stacks 08GT** is an identification of modules and not merely of sets: on germs the
> comparison respects addition, the sum being taken in the sections of `j^*F` over a chart of `U`
> on one side and in the sections of `F` over the composite chart of `X` on the other.

```lean
theorem modulePullbackStalkIso_germ_add (j : U ⟶ X) (hj : IsEtale B S hS j.hom)
    (y : GeometricPoint B S hS U.1) (M : Modules.{u, u} B S hS X.1 X.2)
    (W : SmallEtaleNeighborhood y)
    (a b : ((modulePullback B S hS j).obj M).val.obj (Opposite.op W.chart)) :
    (modulePullbackStalkIso B S hS j hj y).hom.app M
        (moduleGerm.{u, u} B S hS U.1 U.2 ((modulePullback B S hS j).obj M) W (a + b)) =
      moduleGerm.{u, u} B S hS X.1 X.2 M
        ((SmallEtaleNeighborhood.postcomp B S hS j hj y).obj W)
        (((modulePullbackIsoEtaleModulePullback B S hS j hj).hom.app M).val.app
            (Opposite.op W.chart) a +
          ((modulePullbackIsoEtaleModulePullback B S hS j hj).hom.app M).val.app
            (Opposite.op W.chart) b)
```

**`AlgebraicGeometry.Space.modulePullbackStalkIso_germ_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictionStalk.lean#L232). The attribute's comment: “action on germs”.

> **Stacks 08GT** is an identification of modules and not merely of abelian groups: on germs
> the comparison respects the action of the structure sheaf.  The scalar is a section of `𝒪_U`
> over a chart of `U`, which is a section of `𝒪_X` over the composite chart of `X` — étale
> postcomposition leaves the underlying scheme of a chart, hence its regular functions,
> unchanged.

```lean
theorem modulePullbackStalkIso_germ_smul (j : U ⟶ X) (hj : IsEtale B S hS j.hom)
    (y : GeometricPoint B S hS U.1) (M : Modules.{u, u} B S hS X.1 X.2)
    (W : SmallEtaleNeighborhood y)
    (r : ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS U.1 U.2).O)).obj.obj
      (Opposite.op W.chart))
    (a : ((modulePullback B S hS j).obj M).val.obj (Opposite.op W.chart)) :
    (modulePullbackStalkIso B S hS j hj y).hom.app M
        (moduleGerm.{u, u} B S hS U.1 U.2 ((modulePullback B S hS j).obj M) W (r • a)) =
      moduleGerm.{u, u} B S hS X.1 X.2 M
        ((SmallEtaleNeighborhood.postcomp B S hS j hj y).obj W)
        (r • ((modulePullbackIsoEtaleModulePullback B S hS j hj).hom.app M).val.app
          (Opposite.op W.chart) a)
```

**`AlgebraicGeometry.Space.restrictionPresheafFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean#L155). The attribute's comment: “the fibre of a restriction at a lift”.

> For the fibre functors of points of the small étale site, the fibre at the point attached to
> a lift `t` of `x̄` of the restriction along `f` of a presheaf on the small étale site of `Y` is
> the fibre of that presheaf at `x̄`, naturally in the presheaf.

```lean
def restrictionPresheafFiberIso (t : GeometricPointLift B S hS f.hom x) :
    (Functor.whiskeringLeft (SmallEtale B S hS X.1)ᵒᵖ (SmallEtale B S hS Y.1)ᵒᵖ A).obj
          (smallEtalePostcomp B S hS f hf).op ⋙
        (liftSitePoint B S hS f t).presheafFiber ≅
      (etaleSitePoint B S hS Y.1 x Y.2).presheafFiber
```

**`AlgebraicGeometry.Space.restrictionPresheafFiberIso_toPresheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean#L168). The attribute's comment: “the comparison on germs”.

> On germs, `AlgebraicGeometry.Space.restrictionPresheafFiberIso` carries the germ at the lift
> `t` of a section over an étale chart `W` of `X` to the germ at `x̄` of the same section, read over
> the chart `W` of `Y` and at the induced lift.

```lean
theorem restrictionPresheafFiberIso_toPresheafFiber (t : GeometricPointLift B S hS f.hom x)
    (P : (SmallEtale B S hS Y.1)ᵒᵖ ⥤ A) (W : SmallEtale B S hS X.1)
    (w : (liftSitePoint B S hS f t).fiber.obj W) :
    (liftSitePoint B S hS f t).toPresheafFiber W w
          ((smallEtalePostcomp B S hS f hf).op ⋙ P) ≫
        (restrictionPresheafFiberIso B S hS f hf t).hom.app P =
      (etaleSitePoint B S hS Y.1 x Y.2).toPresheafFiber
        ((smallEtalePostcomp B S hS f hf).obj W) (pushLift B S hS f hf W t w) P
```

**`AlgebraicGeometry.Space.restrictionSheafFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean#L186). The attribute's comment: “the fibre of a restriction of abelian sheaves at a lift”.

> For abelian sheaves, the fibre at the point attached to a lift
> `t` of `x̄` of the restriction along `f` of an abelian sheaf on the small étale site of `Y` is
> its fibre at `x̄`, naturally in the sheaf.

```lean
def restrictionSheafFiberIso (t : GeometricPointLift B S hS f.hom x) :
    abelianEtaleRestriction B S hS f hf ⋙ (liftSitePoint B S hS f t).sheafFiber ≅
      (etaleSitePoint B S hS Y.1 x Y.2).sheafFiber (A := AddCommGrpCat.{u})
```

**`AlgebraicGeometry.Space.restrictionSheafFiberIso_toPresheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionFiber.lean#L197). The attribute's comment: “the comparison of abelian sheaf fibres on germs”.

> On germs, `AlgebraicGeometry.Space.restrictionSheafFiberIso` carries the germ at
> the lift `t` of a section over an étale chart `W` of `X` to the germ at `x̄` of the same section
> over `W` read as a chart of `Y`, at the induced lift.

```lean
theorem restrictionSheafFiberIso_toPresheafFiber (t : GeometricPointLift B S hS f.hom x)
    (G : Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{u})
    (W : SmallEtale B S hS X.1) (w : (liftSitePoint B S hS f t).fiber.obj W) :
    (liftSitePoint B S hS f t).toPresheafFiber W w
          ((abelianEtaleRestriction B S hS f hf).obj G).obj ≫
        (restrictionSheafFiberIso B S hS f hf t).hom.app G =
      (etaleSitePoint B S hS Y.1 x Y.2).toPresheafFiber
        ((smallEtalePostcomp B S hS f hf).obj W) (pushLift B S hS f hf W t w) G.obj
```

## Tag 08GU, an equation

[Tag 08GU](https://stacks.math.columbia.edu/tag/08GU) in the Stacks Project.

**`AlgebraicGeometry.Space.ExtensionByZeroStalk.stalkExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean#L175). References: SGA 4 IV (11.3.5), “special case”.

> **Stacks 08GU.** Equation 75.10.0.2: for an étale morphism `j_U : U ⟶ X` of algebraic
> spaces, a sheaf of `𝒪_U`-modules `𝒢` and a geometric point `x̄ : Spec(k) ⟶ X`, the stalk of
> the extension by zero `j_{U!}𝒢` at `x̄` is the direct sum of the stalks of `𝒢` at the
> geometric points `ū : Spec(k) ⟶ U` with `j_U ∘ ū = x̄`.

```lean
def stalkExtensionByZeroIso (V : (spacesEtaleRingedSite B S hS X).C) (x : GeometricPoint B S hS X.1)
    (G : SheafOfModules.{u + 1}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (spacesEtaleRingedSite B S hS X).O).over V)) :
    moduleStalk x ((extensionByZero V).obj G) ≅ ∐ fun v : Lifts V x => liftedStalk v G
```

**`AlgebraicGeometry.Space.ExtensionByZeroStalk.isZero_moduleStalk_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean#L200). The attribute's comment: “vanishing away from the image”.

> **Stacks 08GU.** At a geometric point of `X` admitting no lift to `U` the stalk of
> `j_{U!}𝒢` vanishes.

```lean
theorem isZero_moduleStalk_extensionByZero (V : (spacesEtaleRingedSite B S hS X).C)
    (x : GeometricPoint B S hS X.1)
    (G : SheafOfModules.{u + 1}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (spacesEtaleRingedSite B S hS X).O).over V))
    [IsEmpty (Lifts V x)] :
    IsZero (moduleStalk x ((extensionByZero V).obj G))
```

**`AlgebraicGeometry.Space.ExtensionByZeroStalk.liftsEquivGeometricPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroStalk.lean#L234). The attribute's comment: “the index set”.

> **Stacks 08GU.** The index set of Equation 08GU is the set of geometric points of `U`
> lying over the given geometric point of `X`.

```lean
def liftsEquivGeometricPoints (V : (spacesEtaleRingedSite B S hS X).C)
    (x : GeometricPoint B S hS X.1) :
    Lifts V x ≃
      {y : GeometricPoint B S hS ((SpacesEtale.toSpaces B S hS X).obj V).1 //
        geometricPointMap ((SpacesEtale.inclusion B S hS X).obj V).hom.hom y = x}
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.liftedStalkι_stalkExtensionByZeroIso_inv_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroCounit.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroCounit.lean#L166). The attribute's comment: “the counit on one summand of the stalk”.

> Under the decomposition of the stalk of `f_!(G|_X)` as the direct sum over the lifts of `x̄`
> of the stalks of `G|_X`, the stalk of the counit `f_!(G|_X) ⟶ G` restricts on the summand of a
> lift `t` to the identification of the stalk of `G|_X` at `t` with the stalk of `G` at `x̄`.

```lean
theorem liftedStalkι_stalkExtensionByZeroIso_inv_counit
    (t : GeometricPointLift B S hS f.hom x) :
    liftedStalkι B S hS f x ((abelianEtaleRestriction B S hS f hf).obj G) t ≫
        (stalkExtensionByZeroIso B S hS f hf x
            ((abelianEtaleRestriction B S hS f hf).obj G)).inv ≫
          (etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
            ((abelianEtaleExtensionByZeroAdjunction B S hS f hf).counit.app G) =
      (restrictionSheafFiberIso B S hS f hf t).hom.app G
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.stalkExtensionByZeroIso_inv_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroCounit.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroCounit.lean#L182). The attribute's comment: “the counit on stalks”.

> The stalk of the counit of extension by zero is the fold map: under the decomposition of the
> stalk of `f_!(G|_X)` as the direct sum over the lifts `t` of `x̄` of the stalks of `G|_X` at
> those lifts, and the identification of each of those with the stalk of `G` at `x̄`, the counit
> `f_!(G|_X) ⟶ G` becomes the map out of the direct sum whose component at every lift is that
> identification.

```lean
theorem stalkExtensionByZeroIso_inv_counit :
    (stalkExtensionByZeroIso B S hS f hf x
          ((abelianEtaleRestriction B S hS f hf).obj G)).inv ≫
        (etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
          ((abelianEtaleExtensionByZeroAdjunction B S hS f hf).counit.app G) =
      Sigma.desc fun t : GeometricPointLift B S hS f.hom x =>
        (restrictionSheafFiberIso B S hS f hf t).hom.app G
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.mono_sheafFiber_extensionByZero_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean#L56). The attribute's comment: “the stalk of an extension by zero of a monomorphism”.

> If a morphism of abelian sheaves on `X` has monomorphic stalks at every lift of a geometric
> point `x` of `Y`, then the stalk at `x` of its extension by zero is a monomorphism.

```lean
theorem mono_sheafFiber_extensionByZero_map
    {G H : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u}} (ψ : G ⟶ H)
    (hψ : ∀ t : GeometricPointLift B S hS f.hom x,
      Mono ((liftSitePoint B S hS f t).sheafFiber.map ψ)) :
    Mono ((etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
      ((abelianEtaleExtensionByZero B S hS f hf).map ψ))
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.stalkExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean#L406). The attribute's comment: “the stalk of an extension by zero of abelian sheaves”.

> The stalk at a geometric point `x̄` of `Y` of the extension by zero of an abelian étale sheaf
> on `X` is the direct sum of its stalks at the lifts of `x̄` to `X`.

```lean
def stalkExtensionByZeroIso
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u}) :
    (etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.obj
        ((abelianEtaleExtensionByZero B S hS f hf).obj F) ≅
      (∐ fun t : GeometricPointLift B S hS f.hom x =>
        (liftSitePoint B S hS f t).sheafFiber.obj F)
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.stalkExtensionByZeroIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean#L418). The attribute's comment: “the germ computation”.

> The stalk isomorphism sends the germ of a section over an étale chart `W` of `X`, viewed in
> the extension by zero through the adjunction unit, to its germ at the induced lift, in the
> corresponding summand.

```lean
theorem stalkExtensionByZeroIso_germ
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u})
    (W : SmallEtale B S hS X.1) (t : GeometricPointLift B S hS f.hom x)
    (w : (liftSitePoint B S hS f t).fiber.obj W) :
    extensionByZeroUnitApp B S hS f hf F W ≫
        (etaleSitePoint B S hS Y.1 x Y.2).toPresheafFiber
          ((smallEtalePostcomp B S hS f hf).obj W) (pushLift B S hS f hf W t w)
          ((abelianEtaleExtensionByZero B S hS f hf).obj F).obj ≫
        (stalkExtensionByZeroIso B S hS f hf x F).hom =
      liftedGerm B S hS f x F t W w ≫ liftedStalkι B S hS f x F t
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.stalkExtensionByZeroIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean#L441). The attribute's comment: “naturality”.

> The stalk decomposition `stalkExtensionByZeroIso` is natural in the abelian sheaf.

```lean
theorem stalkExtensionByZeroIso_naturality
    {F G : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u}} (a : F ⟶ G) :
    (etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
          ((abelianEtaleExtensionByZero B S hS f hf).map a) ≫
        (stalkExtensionByZeroIso B S hS f hf x G).hom =
      (stalkExtensionByZeroIso B S hS f hf x F).hom ≫
        (stalkFamily B S hS f x ⋙
          Sigma.functor (GeometricPointLift B S hS f.hom x)).map a
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.isZero_stalkExtensionByZero_of_isEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalk.lean#L461). The attribute's comment: “vanishing away from the image”.

> The extension by zero has zero stalk at every geometric point of `Y` with no lift to `X`.

```lean
theorem isZero_stalkExtensionByZero_of_isEmpty
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u})
    [IsEmpty (GeometricPointLift B S hS f.hom x)] :
    IsZero ((etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.obj
      ((abelianEtaleExtensionByZero B S hS f hf).obj F))
```

**`AlgebraicGeometry.Space.EtaleShriekStalk.isIso_sheafFiber_extensionByZero_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalkMap.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroStalkMap.lean#L61). The attribute's comment: “the stalk of an extension by zero of a map”.

> **The stalk of an extension by zero of a map of abelian sheaves is the direct sum of the
> stalks of that map at the lifts**, hence invertible as soon as all of those are.

```lean
theorem isIso_sheafFiber_extensionByZero_map
    {G H : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u}} (ψ : G ⟶ H)
    (hψ : ∀ t : GeometricPointLift B S hS f.hom x,
      IsIso ((liftSitePoint B S hS f t).sheafFiber.map ψ)) :
    IsIso ((etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
      ((abelianEtaleExtensionByZero B S hS f hf).map ψ))
```

**`AlgebraicGeometry.Space.isIso_sheafFiber_toSheaf_etaleModuleShriek_map_of_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekStalkMap.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekStalkMap.lean#L39). The attribute's comment: “the stalk of an extension by zero of a map of modules”.

> **The stalk of the extension by zero of a map of modules is invertible as soon as the stalks
> of that map at all the lifts of the point are.**

```lean
theorem isIso_sheafFiber_toSheaf_etaleModuleShriek_map_of_lifts
    {M N : Modules.{u, u} B S hS X.1 X.2} (α : M ⟶ N)
    (hα : ∀ t : GeometricPointLift B S hS f.hom x,
      IsIso ((liftSitePoint B S hS f t).sheafFiber.map
        ((SheafOfModules.toSheaf (etaleRingSheaf B S hS X)).map α))) :
    IsIso ((etaleSitePoint B S hS Y.1 x Y.2).sheafFiber.map
      ((SheafOfModules.toSheaf (etaleRingSheaf B S hS Y)).map
        ((etaleModuleLowerShriek B S hS f hf).map α)))
```

**`AlgebraicGeometry.Space.cohomologySupportedOn_mapDerivedCategory_etaleModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekSupport.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekSupport.lean#L156). The attribute's comment: “the support of an extension by zero of an object of the derived category”.

> If an object `K` of `D(𝒪_X)` is supported on `|f|⁻¹T` in the sense of Stacks 08GF, then its
> extension by zero along the étale morphism `f` is supported on `T`.

```lean
theorem cohomologySupportedOn_mapDerivedCategory_etaleModuleLowerShriek
    (K : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (T : Set (points B S hS Y.1))
    (hK : CohomologySupportedOn B S hS X.1 X.2 (pointsMap B S hS X.1 f.hom ⁻¹' T) K) :
    CohomologySupportedOn B S hS Y.1 Y.2 T
      ((etaleModuleLowerShriek B S hS f hf).mapDerivedCategory.obj K)
```

## Tag 08GV, a lemma

[Tag 08GV](https://stacks.math.columbia.edu/tag/08GV) in the Stacks Project.

**`AlgebraicGeometry.Space.mayerVietoris_shortExact_and_mem_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisTag.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisTag.lean#L195).

> **Stacks 08GV.**  Let `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of
> algebraic spaces over a scheme `S` and let `P = U ×_X V`.  Write `(-)|_Y` for restriction of
> modules along an étale morphism `j_Y : Y ⟶ X` and `j_{Y!}` for its extension by zero,
> `AlgebraicGeometry.Space.etaleModuleLowerShriek`, with counit `j_{Y!}(F|_Y) ⟶ F`, and let `a`
> and `b` be the two comparisons out of the intersection attached to its two factorizations.
> Then
>
> 1. for every sheaf of `𝒪_X`-modules `F` the sequence
>
>    `0 ⟶ j_{P!}F|_P ⟶ j_{U!}F|_U ⊕ j_{V!}F|_V ⟶ F ⟶ 0`,
>
>    with maps `(a, -b)` and the sum of the two counits, is short exact, and
> 2. every object `E` of the unbounded derived category `D(𝒪_X)` sits in a distinguished triangle
>
>    `j_{P!}E|_P ⟶ j_{U!}E|_U ⊕ j_{V!}E|_V ⟶ E ⟶ (j_{P!}E|_P)[1]`,
>
>    whose first two maps are the derived transformations of `(a, -b)` and of the two counits.
>
> The exactness of the three extensions by zero, Stacks 03DJ, is the theorem
> `AlgebraicGeometry.Space.preservesFiniteLimits_etaleModuleLowerShriek` together with
> `AlgebraicGeometry.Space.etaleModuleLowerShriek_additive` and
> `AlgebraicGeometry.Space.preservesFiniteColimits_etaleModuleLowerShriek`, which is what makes
> their derived functors available; it is proved, not assumed.

```lean
theorem mayerVietoris_shortExact_and_mem_distTriang :
    (∀ F : Modules.{u, u} B S hS W.1 W.2,
        (ShortComplex.mayerVietoris
          ((edsShriekOpenComparison B S hS hsq
              (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
                (isEtale_edsOpenHom B S hS hsq))
              (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                (isEtale_edsInterHom B S hS hsq))).app F)
          ((edsShriekEtaleComparison B S hS hsq
              (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
                (isEtale_edsEtaleHom B S hS hsq))
              (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                (isEtale_edsInterHom B S hS hsq))).app F)
          ((etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
            (isEtale_edsOpenHom B S hS hsq)).counit.app F)
          ((etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
            (isEtale_edsEtaleHom B S hS hsq)).counit.app F)
          (zero_edsShriekMayerVietoris B S hS hsq
            (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
              (isEtale_edsOpenHom B S hS hsq))
            (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
              (isEtale_edsEtaleHom B S hS hsq))
            (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
              (isEtale_edsInterHom B S hS hsq)) F)).ShortExact) ∧
      ∀ E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2),
        ∃ δ, Triangle.mk
            (biprod.lift
              ((NatTrans.mapDerivedCategory
                (edsShriekOpenComparison B S hS hsq
                  (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
                    (isEtale_edsOpenHom B S hS hsq))
                  (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                    (isEtale_edsInterHom B S hS hsq)))).app E)
              (-((NatTrans.mapDerivedCategory
                (edsShriekEtaleComparison B S hS hsq
                  (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
                    (isEtale_edsEtaleHom B S hS hsq))
                  (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                    (isEtale_edsInterHom B S hS hsq)))).app E)))
            (biprod.desc
                ((NatTrans.mapDerivedCategory
                  (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
                    (isEtale_edsOpenHom B S hS hsq)).counit).app E)
                ((NatTrans.mapDerivedCategory
                  (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
                    (isEtale_edsEtaleHom B S hS hsq)).counit).app E) ≫
              (Functor.mapDerivedCategoryIdIso
                (Modules.{u, u} B S hS W.1 W.2)).hom.app E) δ ∈
          distTriang (DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
```

## Tag 08GW, a lemma

[Tag 08GW](https://stacks.math.columbia.edu/tag/08GW) in the Stacks Project.

**`AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietorisLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisPushforwardTag.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisPushforwardTag.lean#L598). The attribute's comment: “part (1)”.

> **Stacks 08GW part (1), with nothing assumed.**  Let `(U ⊆ X, j_V : V ⟶ X)` be an elementary
> distinguished square of algebraic spaces over a scheme `S`, let `P = U ×_X V`, write `(-)|_Y`
> for restriction of modules along `j_Y : Y ⟶ X` and `j_{Y,*}` for the direct image of Stacks
> 03LU.  Then for every sheaf of `𝒪_X`-modules `F` the sequence
>
> `0 ⟶ F ⟶ j_{U,*}F|_U ⊕ j_{V,*}F|_V ⟶ j_{P,*}F|_P ⟶ 0`
>
> is short exact.  Its first map is the pair of canonical units `F ⟶ j_{Y,*}F|_Y` of the
> adjunctions `(-)|_Y ⊣ j_{Y,*}` and its second is the difference of the conjugates, under the
> adjunctions `j_{Y!}((-)|_Y) ⊣ j_{Y,*}((-)|_Y)`, of the two extension-by-zero comparisons
> `AlgebraicGeometry.Space.edsShriekOpenComparison` and
> `AlgebraicGeometry.Space.edsShriekEtaleComparison` of Stacks 08GV.
>
> This is `AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietorisComparison` at the
> extension by zero the library constructs, `AlgebraicGeometry.Space.etaleModuleLowerShriek` with
> its adjunction `AlgebraicGeometry.Space.etaleModuleLowerShriekAdjunction`, so nothing is a
> parameter beyond the square itself: the exactness of extension by zero (Stacks 03DJ) is the
> theorem `AlgebraicGeometry.Space.preservesFiniteLimits_etaleModuleLowerShriek` with its two
> companions, the two sheafification hypotheses of the ambient site are the theorems
> `AlgebraicGeometry.Space.smallEtaleRingedSite_hasSheafify_addCommGrpCat` and
> `AlgebraicGeometry.Space.smallEtaleRingedSite_wEqualsLocallyBijective_addCommGrpCat`, part (1)
> of Stacks 08GV is
> `AlgebraicGeometry.Space.shortExact_edsShriekMayerVietoris`, and the surjectivity on the right
> is `AlgebraicGeometry.Space.epi_edsRestrictPushMayerVietorisComparison`.

```lean
theorem shortExact_edsRestrictPushMayerVietorisLowerShriek
    (F : Modules.{u, u} B S hS W.1 W.2) :
    (ShortComplex.mk
      (biprod.lift ((edsAdjOpen B S hS hsq).unit.app F)
        ((edsAdjEtale B S hS hsq).unit.app F))
      (biprod.desc ((conjugateEquiv ((edsAdjOpen B S hS hsq).comp
            (edsLowerShriekAdjOpen B S hS hsq))
          ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
          (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
            (edsLowerShriekAdjInter B S hS hsq))).app F)
        (-((conjugateEquiv ((edsAdjEtale B S hS hsq).comp
            (edsLowerShriekAdjEtale B S hS hsq))
          ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
          (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
            (edsLowerShriekAdjInter B S hS hsq))).app F)))
      (zero_edsRestrictPushMayerVietorisLowerShriek B S hS hsq F)).ShortExact
```

**`AlgebraicGeometry.Space.exists_mem_distTriang_edsDerivedRestrictPushMayerVietorisLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisPushforwardTag.lean, line 704](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisPushforwardTag.lean#L704). The attribute's comment: “part (2)”.

> **Stacks 08GW part (2), with nothing assumed and with the canonical triangle.**  Let
> `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a scheme
> `S`, let `P = U ×_X V` and write `Rj_{Y,*}((-)|_Y)` for the total right derived functor of
> `j_{Y,*}((-)|_Y)`.  Then every object `E` of the unbounded derived category `D(𝒪_X)` sits in a
> distinguished triangle
>
> `E ⟶ Rj_{U,*}E|_U ⊕ Rj_{V,*}E|_V ⟶ Rj_{P,*}E|_P ⟶ E[1]`.
>
> **Its maps are the canonical ones, not existentially quantified.**  The first is the pair of
> derived units `CategoryTheory.PushforwardMayerVietoris.derivedUnitOfNatTrans` of the units
> `F ⟶ j_{Y,*}F|_Y` of the adjunctions `(-)|_Y ⊣ j_{Y,*}` of Stacks 03LU, and the second is the
> difference of the derived transformations `CategoryTheory.Functor.rightDerivedNatTrans` of the
> two comparisons of part (1) — the conjugates, under `j_{Y!}((-)|_Y) ⊣ j_{Y,*}((-)|_Y)`, of the
> extension-by-zero comparisons of Stacks 08GV.  Only the connecting map
> `Rj_{P,*}E|_P ⟶ E[1]` is existentially quantified, the library attaching no canonical such map
> to an object of `D(𝒪_X)`; the source likewise asserts only that the triangle is distinguished,
> and `δ` is existential in Stacks 08GV part (2) as well.
>
> Nothing is a parameter beyond the square: part (1) is the unqualified
> `AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietorisLowerShriek`, the K-injective
> resolutions are `AlgebraicGeometry.Space.exists_quasiIso_isKInjective_modules` (Stacks 079P),
> and the three derived functors are the chosen ones, which exist by
> `AlgebraicGeometry.Space.hasRightDerivedFunctor_mapHomotopyCategory_modules`.

```lean
theorem exists_mem_distTriang_edsDerivedRestrictPushMayerVietorisLowerShriek
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ δ, Triangle.mk
        (biprod.lift
          ((derivedUnitOfNatTrans (edsAdjOpen B S hS hsq).unit
            (edsDerivedRestrictPushOpen B S hS hsq)
            (edsTotalRightDerivedUnitOpen B S hS hsq)).app E)
          ((derivedUnitOfNatTrans (edsAdjEtale B S hS hsq).unit
            (edsDerivedRestrictPushEtale B S hS hsq)
            (edsTotalRightDerivedUnitEtale B S hS hsq)).app E))
        (biprod.desc
          ((Functor.rightDerivedNatTrans (edsDerivedRestrictPushOpen B S hS hsq)
            (edsDerivedRestrictPushInter B S hS hsq)
            (edsTotalRightDerivedUnitOpen B S hS hsq)
            (edsTotalRightDerivedUnitInter B S hS hsq)
            (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
            (Functor.whiskerRight (NatTrans.mapHomotopyCategory
              (conjugateEquiv ((edsAdjOpen B S hS hsq).comp
                  (edsLowerShriekAdjOpen B S hS hsq))
                ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                  (edsLowerShriekAdjInter B S hS hsq)))
              (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
          (-((Functor.rightDerivedNatTrans (edsDerivedRestrictPushEtale B S hS hsq)
            (edsDerivedRestrictPushInter B S hS hsq)
            (edsTotalRightDerivedUnitEtale B S hS hsq)
            (edsTotalRightDerivedUnitInter B S hS hsq)
            (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
            (Functor.whiskerRight (NatTrans.mapHomotopyCategory
              (conjugateEquiv ((edsAdjEtale B S hS hsq).comp
                  (edsLowerShriekAdjEtale B S hS hsq))
                ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                  (edsLowerShriekAdjInter B S hS hsq)))
              (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))) δ ∈
      distTriang (DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
```

## Tag 08JK, a lemma

[Tag 08JK](https://stacks.math.columbia.edu/tag/08JK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_mem_distTriang_edsRelativeMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisRelative.lean, line 996](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisRelative.lean#L996). The attribute's comment: “FIRST ASSERTION: for every E of D(O\_X) a distinguished triangle Rf\_*E -> Ra\_*(E|\_U) ⊕ Rb\_*(E|\_V) -> Rc\_*(E|\_\{U x\_X V}) -> (Rf\_*E)[1] in D(O\_Y), with no hypothesis beyond the square, f and the four derived functors. The SECOND ASSERTION, functoriality in E, is exists\_natTrans\_mem\_distTriang\_edsRelativeMayerVietoris\_unconditional in the sibling module. Proof route and provenance are in this theorem's docstring”.

> **Stacks 08JK, the distinguished triangle.**  This declaration is the `@[stacks 08JK]`
> registration of the first of the tag's two assertions, and it takes no hypothesis.
>
> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, let
> `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square on `X`, let `P = U ×_X V` and let
> `a = f|_U`, `b = f|_V`, `c = f|_P` be the restrictions of `f` to the three.  Let `Rf_*`,
> `Ra_*((-)|_U)`, `Rb_*((-)|_V)` and `Rc_*((-)|_P)` be right derived functors of `f_*`,
> `a_*((-)|_U)`, `b_*((-)|_V)` and `c_*((-)|_P)`, with their comparisons.  Then every object `E`
> of `D(𝒪_X)` sits in a distinguished triangle
>
> `Rf_*E ⟶ Ra_*(E|_U) ⊕ Rb_*(E|_V) ⟶ Rc_*(E|_{U ×_X V}) ⟶ (Rf_*E)[1]`
>
> in `D(𝒪_Y)`.
>
> The conclusion is that of the untagged
> `AlgebraicGeometry.Space.exists_mem_distTriang_edsRelativeMayerVietoris` verbatim, with that
> statement's one hypothesis discharged by a route the source does not take.  The source
> deduces the direct-image Mayer–Vietoris sequence of Stacks 08GW part (1) at every module, and
> gets surjectivity on the right from the étale-local vanishing of an obstruction class.  Only the
> sequence at an *injective* module is used here — the representative of `E` may be taken
> termwise injective, by Stacks 079P — and there the obstruction vanishes for a formal reason:
> `CategoryTheory.PushforwardMayerVietoris.epi_conjugate_of_injective` splits the sequence by
> extending a counit along the monomorphism that part (1) of Stacks 08GV provides
> (`AlgebraicGeometry.Space.shortExact_edsShriekMayerVietoris`).  So nothing beyond Stacks 08GV
> part (1), which the library proves, and Stacks 079P is needed.
>
> The three extensions by zero are the ones the library constructs,
> `AlgebraicGeometry.Space.etaleModuleLowerShriek`, with their adjunctions; nothing about them is
> assumed, and they do not appear in the statement.  The five morphisms are existentially
> quantified at each `E`; the tag's second assertion, that the triangle is in addition
> *functorial in `E`*, is registered on
> `AlgebraicGeometry.Space.exists_natTrans_mem_distTriang_edsRelativeMayerVietoris_`
> `unconditional` in the sibling module.  Those two declarations are the only two
> `@[stacks 08JK]` registrations.

```lean
theorem exists_mem_distTriang_edsRelativeMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Z.1 Z.2))
    (αX : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
          (isEtale_edsOpenHom B S hS hsq) ⋙
        modulePushforward B S hS (edsOpenHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
          (isEtale_edsEtaleHom B S hS hsq) ⋙
        modulePushforward B S hS (edsEtaleHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
          (isEtale_edsInterHom B S hS hsq) ⋙
        modulePushforward B S hS (edsInterHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ (fU : RX.obj E ⟶ RU.obj E) (fV : RX.obj E ⟶ RV.obj E) (gU : RU.obj E ⟶ RP.obj E)
      (gV : RV.obj E ⟶ RP.obj E) (δ : RP.obj E ⟶ (RX.obj E)⟦(1 : ℤ)⟧),
      Triangle.mk (biprod.lift fU fV) (biprod.desc gU (-gV)) δ ∈
        distTriang (DerivedCategory (Modules.{u, u} B S hS Z.1 Z.2))
```

**`AlgebraicGeometry.Space.exists_natTrans_mem_distTriang_edsRelativeMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisRelativeFunctorial.lean, line 710](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisRelativeFunctorial.lean#L710). The attribute's comment: “SECOND ASSERTION: the distinguished triangle is FUNCTORIAL IN E. The five morphisms are natural transformations of the four right derived functors D(O\_X) -> D(O\_Y) and the triangle is distinguished at EVERY E, with no hypothesis beyond the square, f and those functors. The FIRST ASSERTION is exists\_mem\_distTriang\_edsRelativeMayerVietoris\_unconditional in the sibling module. Proof route and provenance are in this theorem's docstring”.

> **Stacks 08JK, the functoriality in `E`.**
>
> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, let
> `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square on `X`, let `P = U ×_X V`, and let
> `Rf_*`, `Ra_*((-)|_U)`, `Rb_*((-)|_V)`, `Rc_*((-)|_P)` be right derived functors of the four
> functors of the square, with their comparisons.  Then the five morphisms of the Mayer–Vietoris
> triangle
>
> `Rf_*E ⟶ Ra_*(E|_U) ⊕ Rb_*(E|_V) ⟶ Rc_*(E|_{U ×_X V}) ⟶ (Rf_*E)[1]`
>
> are **natural transformations** of the four derived functors `D(𝒪_X) ⥤ D(𝒪_Y)`, and the triangle
> is distinguished at every object `E` of `D(𝒪_X)`.  So a morphism `φ : E ⟶ E'` induces a
> morphism of the two triangles.
>
> The direct-image Mayer–Vietoris sequence is used only at *injective* modules — the functorial
> resolution of Stacks 079P is termwise injective — where it is proved from part (1) of
> Stacks 08GV: `AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietoris_of_injective`.  The
> first assertion of Stacks 08JK is
> `AlgebraicGeometry.Space.exists_mem_distTriang_edsRelativeMayerVietoris_unconditional`.

```lean
theorem exists_natTrans_mem_distTriang_edsRelativeMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Z.1 Z.2))
    (αX : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
          (isEtale_edsOpenHom B S hS hsq) ⋙
        modulePushforward B S hS (edsOpenHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
          (isEtale_edsEtaleHom B S hS hsq) ⋙
        modulePushforward B S hS (edsEtaleHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
          (isEtale_edsInterHom B S hS hsq) ⋙
        modulePushforward B S hS (edsInterHom B S hS hsq ≫ f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))) :
    ∃ (fU : RX ⟶ RU) (fV : RX ⟶ RV) (gU : RU ⟶ RP) (gV : RV ⟶ RP)
      (δ : RP ⟶ RX ⋙ shiftFunctor (DerivedCategory (Modules.{u, u} B S hS Z.1 Z.2)) (1 : ℤ)),
      ∀ E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2),
        Triangle.mk (biprod.lift (fU.app E) (fV.app E))
            (biprod.desc (gU.app E) (-(gV.app E))) (δ.app E) ∈
          distTriang (DerivedCategory (Modules.{u, u} B S hS Z.1 Z.2))
```

## Tag 08H9, a lemma

[Tag 08H9](https://stacks.math.columbia.edu/tag/08H9) in the Stacks Project.

**`AlgebraicGeometry.Space.mayerVietoris_derivedHom_longExactSequence_of_eds_lowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisExtTag.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisExtTag.lean#L303). The attribute's comment: “the whole tag, and its one library registration: the Mayer-Vietoris sequence of an elementary distinguished square is exact at each of its three kinds of spot and in every integer degree, its first map being the pair of the two derived restrictions of a shifted morphism, its second the difference of the two restrictions to the intersection, and its connecting map that of the triangle of 08GV part (2); the square is the only binder”.

> **Stacks 08H9, with nothing assumed and with every map of the sequence named.**  Let
> `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a scheme
> `S`, let `P = U ×_X V` and write `(-)|_Y` for restriction of modules along `j_Y : Y ⟶ X`.  Then
> for all objects `E` and `F` of `D(𝒪_X)` the Mayer–Vietoris sequence
>
> `⋯ ⟶ Ext⁻¹(E|_P, F|_P) ⟶ Hom(E, F) ⟶ Hom(E|_U, F|_U) ⊕ Hom(E|_V, F|_V) ⟶ Hom(E|_P, F|_P) ⟶ ⋯`
>
> is exact at each of its three kinds of spot and in every integer degree, the homomorphism groups
> of the restrictions being taken in the derived categories of `U`, of `V` and of `P`.
>
> Every map of the sequence is named; none of the three is quantified over.
>
> * **The restriction map is the restriction map.**  In degree `n` it carries `x : E ⟶ F⟦n⟧` to the
>   pair of the actions `CategoryTheory.ShiftedHom.map` of the two derived restrictions on it, so
>   neither a choice nor an extension by zero enters it.
> * **The second map is the difference of the two restrictions to the intersection.**  It is
>   `AlgebraicGeometry.Space.edsDerivedHomRestrictionOpen` on the first summand minus
>   `AlgebraicGeometry.Space.edsDerivedHomRestrictionEtale` on the second; each of those is the map
>   induced by the comparison of the square attached to the corresponding factorization of `j_P`,
>   and the two clauses below record that each carries the restriction of a morphism of `D(𝒪_X)` to
>   the restriction of that morphism to `P`.
> * **The connecting homomorphism is the one of the Mayer–Vietoris triangle.**  The morphism `δ` is
>   bound as the third map of the distinguished triangle of part (2) of Stacks 08GV, read at the
>   composites of the derived functors, and `AlgebraicGeometry.Space.edsDerivedHomBoundary` is
>   composition with that same `δ`, as the third clause below records.
>
> Nothing beyond the square is assumed: the extension-by-zero data is not quantified over but is
> `AlgebraicGeometry.Space.etaleModuleLowerShriek` with its adjunctions
> `AlgebraicGeometry.Space.etaleModuleLowerShriekAdjunction`, its exactness is the theorem
> `AlgebraicGeometry.Space.preservesFiniteLimits_etaleModuleLowerShriek` (Stacks 03DJ) with its two
> companions, and the two sheafification hypotheses of the ambient site are discharged by
> `AlgebraicGeometry.Space.smallEtaleRingedSite_hasSheafify_addCommGrpCat` and
> `AlgebraicGeometry.Space.smallEtaleRingedSite_wEqualsLocallyBijective_addCommGrpCat`.
>
> This is the one library registration of Tag 08H9, and the elementary distinguished square is its
> only binder.

```lean
theorem mayerVietoris_derivedHom_longExactSequence_of_eds_lowerShriek
    (E F : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ δ : E ⟶ ((etaleModuleLowerShriek B S hS (edsInterHom B S hS hsq)
        (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory.obj
        ((etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
            (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory.obj E))⟦(1 : ℤ)⟧,
      Triangle.mk
          (biprod.lift
            ((Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                  (edsInterHom B S hS hsq) (isEtale_edsInterHom B S hS hsq))
                      (etaleModuleLowerShriek B S hS (edsInterHom B S hS hsq)
                        (isEtale_edsInterHom B S hS hsq))).inv.app E ≫
              (NatTrans.mapDerivedCategory
                (edsShriekOpenComparison B S hS hsq
                    (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
                      (isEtale_edsOpenHom B S hS hsq))
                          (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                            (isEtale_edsInterHom B S hS hsq)))).app E ≫
              (Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                (edsOpenHom B S hS hsq) (isEtale_edsOpenHom B S hS hsq))
                    (etaleModuleLowerShriek B S hS (edsOpenHom B S hS hsq)
                      (isEtale_edsOpenHom B S hS hsq))).hom.app E)
            (-((Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                  (edsInterHom B S hS hsq) (isEtale_edsInterHom B S hS hsq))
                      (etaleModuleLowerShriek B S hS (edsInterHom B S hS hsq)
                        (isEtale_edsInterHom B S hS hsq))).inv.app E ≫
              (NatTrans.mapDerivedCategory
                (edsShriekEtaleComparison B S hS hsq
                    (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
                      (isEtale_edsEtaleHom B S hS hsq))
                          (etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                            (isEtale_edsInterHom B S hS hsq)))).app E ≫
              (Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                (edsEtaleHom B S hS hsq) (isEtale_edsEtaleHom B S hS hsq))
                    (etaleModuleLowerShriek B S hS (edsEtaleHom B S hS hsq)
                      (isEtale_edsEtaleHom B S hS hsq))).hom.app E)))
          (biprod.desc
            ((Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                  (edsOpenHom B S hS hsq) (isEtale_edsOpenHom B S hS hsq))
                      (etaleModuleLowerShriek B S hS (edsOpenHom B S hS hsq)
                        (isEtale_edsOpenHom B S hS hsq))).inv.app E ≫
              (NatTrans.mapDerivedCategory
                  (etaleModuleLowerShriekAdjunction B S hS (edsOpenHom B S hS hsq)
                    (isEtale_edsOpenHom B S hS hsq)).counit).app E ≫
              (Functor.mapDerivedCategoryIdIso _).hom.app E)
            ((Functor.mapDerivedCategoryComp (etaleModulePullback.{u, u} B S hS
                  (edsEtaleHom B S hS hsq) (isEtale_edsEtaleHom B S hS hsq))
                      (etaleModuleLowerShriek B S hS (edsEtaleHom B S hS hsq)
                        (isEtale_edsEtaleHom B S hS hsq))).inv.app E ≫
              (NatTrans.mapDerivedCategory
                  (etaleModuleLowerShriekAdjunction B S hS (edsEtaleHom B S hS hsq)
                    (isEtale_edsEtaleHom B S hS hsq)).counit).app E ≫
              (Functor.mapDerivedCategoryIdIso _).hom.app E)) δ ∈
        distTriang (DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) ∧
      (∀ (n : ℤ) (x : E ⟶ F⟦n⟧),
        edsDerivedHomRestrictionOpen B S hS hsq E F n
            (ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
              (isEtale_edsOpenHom B S hS hsq)).mapDerivedCategory) =
          ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
            (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory) ∧
      (∀ (n : ℤ) (x : E ⟶ F⟦n⟧),
        edsDerivedHomRestrictionEtale B S hS hsq E F n
            (ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
              (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory) =
          ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
            (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory) ∧
      (∀ (n : ℤ) (z : ((etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
          (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory.obj E ⟶
          ((etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
              (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory.obj F)⟦n⟧)),
        edsDerivedHomBoundary B S hS hsq E F δ n z =
          δ ≫ (((etaleModuleLowerShriekAdjunction B S hS (edsInterHom B S hS hsq)
                  (isEtale_edsInterHom B S hS hsq)).shiftedHomMapDerivedCategoryEquiv
                ((etaleModulePullback.{u, u} B S hS (edsInterHom B S hS hsq)
                  (isEtale_edsInterHom B S hS hsq)).mapDerivedCategory.obj E) F n).symm
              z)⟦(1 : ℤ)⟧' ≫
            (shiftFunctorAdd' (DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
              n 1 (n + 1) rfl).inv.app F) ∧
      ∀ n : ℤ,
        Function.Exact
            (fun x : E ⟶ F⟦n⟧ =>
              (ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
                (isEtale_edsOpenHom B S hS hsq)).mapDerivedCategory,
                ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
                  (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory))
            (fun w => edsDerivedHomRestrictionOpen B S hS hsq E F n w.1 -
              edsDerivedHomRestrictionEtale B S hS hsq E F n w.2) ∧
          Function.Exact
            (fun w : ((etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
                (isEtale_edsOpenHom B S hS hsq)).mapDerivedCategory.obj E ⟶
                ((etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
                    (isEtale_edsOpenHom B S hS hsq)).mapDerivedCategory.obj F)⟦n⟧) ×
                ((etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
                    (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory.obj E ⟶
                    ((etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
                        (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory.obj F)⟦n⟧) =>
              edsDerivedHomRestrictionOpen B S hS hsq E F n w.1 -
                edsDerivedHomRestrictionEtale B S hS hsq E F n w.2)
            (edsDerivedHomBoundary B S hS hsq E F δ n) ∧
          Function.Exact (edsDerivedHomBoundary B S hS hsq E F δ n)
            (fun x : E ⟶ F⟦n + 1⟧ =>
              (ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsOpenHom B S hS hsq)
                (isEtale_edsOpenHom B S hS hsq)).mapDerivedCategory,
                ShiftedHom.map x (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
                  (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory))
```

## Tag 0CRS, a lemma

[Tag 0CRS](https://stacks.math.columbia.edu/tag/0CRS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean, line 1112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean#L1112). The attribute's comment: “THIRD CLAUSE: functoriality in E of the distinguished triangle and of its long exact cohomology sequence. The five maps are components of natural transformations of functors on D(O\_X); no hypothesis beyond the square and the four derived functors presenting RGamma. The other two clauses are exists\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional and exists\_homologySequence\_exact\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, functoriality in `E`, with nothing granted.**
>
> Let `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and let `P = U ×_X V`.  Write `Γ(X, -)` for global sections of `𝒪_X`-modules on the
> small étale ringed site, `Φ_Y = j_{Y,*}((-)|_Y)` for the three restrict-then-push composites of
> the square, and let `RΓ(X, -)`, `RΓ(U, -)`, `RΓ(V, -)`, `RΓ(P, -)` be right derived functors of
> `Γ(X, -)`, `Γ(X, -) ∘ Φ_U`, `Γ(X, -) ∘ Φ_V` and `Γ(X, -) ∘ Φ_P`.  Then the five maps of the
> Mayer–Vietoris triangle
>
> `RΓ(X, E) ⟶ RΓ(U, E) ⊕ RΓ(V, E) ⟶ RΓ(U ×_X V, E) ⟶ RΓ(X, E)[1]`
>
> are the components of *natural transformations* of functors on `D(𝒪_X)`, every component
> triangle is distinguished, and its homology sequence is exact at every `n`.  So a morphism
> `E ⟶ E'` induces a morphism of the two triangles and of the two long exact sequences.
>
> As in the conditional statements, the three outer terms are the derived functors of
> `Γ(X, -) ∘ j_{Y,*} ∘ (-)|_Y` in that factored form; that this is `RΓ(Y, E|_Y)` is the
> adjunction of Stacks 03LU, `Stacks.Cohomology.SiteModules.globalSectionsPushforwardIso`, and is
> not transported here.

```lean
theorem exists_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))) :
    ∃ (aU : RX ⟶ RU) (aV : RX ⟶ RV) (bU : RU ⟶ RP) (bV : RV ⟶ RP)
      (δ : RP ⟶ RX ⋙ shiftFunctor (DerivedCategory (ModuleCat.{u + 1}
        (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) (1 : ℤ)),
      ∀ E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2),
        Triangle.mk (biprod.lift (aU.app E) (aV.app E))
            (biprod.desc (bU.app E) (-(bV.app E))) (δ.app E) ∈
          distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) ∧
        ∀ n : ℤ, ((DerivedCategory.homologyFunctor (ModuleCat.{u + 1} (RingCat.sectionsSubring
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))
            0).homologySequenceComposableArrows₅
          (Triangle.mk (biprod.lift (aU.app E) (aV.app E))
            (biprod.desc (bU.app E) (-(bV.app E))) (δ.app E)) n (n + 1) rfl).Exact
```

**`AlgebraicGeometry.Space.exists_mem_distTriang_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean#L1180). The attribute's comment: “FIRST CLAUSE: every E of D(O\_X) sits in a distinguished triangle RGamma(X,E) -> RGamma(U,E) (+) RGamma(V,E) -> RGamma(U x\_X V,E) -> RGamma(X,E)[1]; no hypothesis beyond the square and the four derived functors presenting RGamma. The other two clauses are exists\_homologySequence\_exact\_edsSectionsMayerVietoris\_unconditional and exists\_natTrans\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, the distinguished triangle, with nothing granted.**
>
> In the situation of
> `AlgebraicGeometry.Space.exists_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional`,
> every object `E` of `D(𝒪_X)` sits in a distinguished triangle
>
> `RΓ(X, E) ⟶ RΓ(U, E) ⊕ RΓ(V, E) ⟶ RΓ(U ×_X V, E) ⟶ RΓ(X, E)[1]`.

```lean
theorem exists_mem_distTriang_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ (fU : RX.obj E ⟶ RU.obj E) (fV : RX.obj E ⟶ RV.obj E) (gU : RU.obj E ⟶ RP.obj E)
      (gV : RV.obj E ⟶ RP.obj E) (δ : RP.obj E ⟶ (RX.obj E)⟦(1 : ℤ)⟧),
      Triangle.mk (biprod.lift fU fV) (biprod.desc gU (-gV)) δ ∈
        distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
```

**`AlgebraicGeometry.Space.exists_homologySequence_exact_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean, line 1243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSections.lean#L1243). The attribute's comment: “SECOND CLAUSE: every E of D(O\_X) sits in a long exact cohomology sequence ... -> H^n(X,E) -> H^n(U,E) (+) H^n(V,E) -> H^n(U x\_X V,E) -> H^\{n+1}(X,E) -> ...; no hypothesis beyond the square and the four derived functors presenting RGamma. It is the homology sequence of the triangle of exists\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional; functoriality is exists\_natTrans\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, the long exact cohomology sequence, with nothing granted.**
>
> The distinguished triangle of
> `AlgebraicGeometry.Space.exists_mem_distTriang_edsSectionsMayerVietoris_unconditional` has an
> exact homology sequence, which at each `n` is the six-term exact sequence
>
> `H^n(X,E) ⟶ H^n(U,E) ⊕ H^n(V,E) ⟶ H^n(U ×\_X V,E) ⟶ H^\{n+1}(X,E) ⟶ H^\{n+1}(U,E) ⊕ H^\{n+1}(V,E)
> ⟶ H^\{n+1}(U ×\_X V,E)`
>
> — the Mayer–Vietoris long exact sequence of the source, since the homology functor is additive
> and so carries the biproduct `RΓ(U,E) ⊕ RΓ(V,E)` to `H^n(U,E) ⊕ H^n(V,E)`.

```lean
theorem exists_homologySequence_exact_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ (fU : RX.obj E ⟶ RU.obj E) (fV : RX.obj E ⟶ RV.obj E) (gU : RU.obj E ⟶ RP.obj E)
      (gV : RV.obj E ⟶ RP.obj E) (δ : RP.obj E ⟶ (RX.obj E)⟦(1 : ℤ)⟧),
      Triangle.mk (biprod.lift fU fV) (biprod.desc gU (-gV)) δ ∈
        distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) ∧
      ∀ n : ℤ, ((DerivedCategory.homologyFunctor (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))
          0).homologySequenceComposableArrows₅
        (Triangle.mk (biprod.lift fU fV) (biprod.desc gU (-gV)) δ) n (n + 1) rfl).Exact
```

**`AlgebraicGeometry.Space.exists_delta_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean#L548). The attribute's comment: “THIRD CLAUSE: functoriality in E of the distinguished triangle and of its long exact cohomology sequence. The four maps are NAMED in the statement -- the right derived transformations of the restriction maps RGamma(X,-) -> RGamma(U,-), RGamma(V,-) and RGamma(U,-) -> RGamma(U x\_X V,-), RGamma(V,-) -> RGamma(U x\_X V,-) -- and are components of natural transformations of functors on D(O\_X); only the connecting delta is existential, as in the source. No hypothesis beyond the square and the four derived functors presenting RGamma. The other two clauses are exists\_delta\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional and exists\_delta\_homologySequence\_exact\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, functoriality in `E`, with nothing granted.**
>
> Let `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and let `P = U ×_X V`.  Write `Γ(X, -)` for global sections of `𝒪_X`-modules on the
> small étale ringed site, `Φ_Y = j_{Y,*}((-)|_Y)` for the three restrict-then-push composites of
> the square, and let `RΓ(X, -)`, `RΓ(U, -)`, `RΓ(V, -)`, `RΓ(P, -)` be right derived functors of
> `Γ(X, -)`, `Γ(X, -) ∘ Φ_U`, `Γ(X, -) ∘ Φ_V` and `Γ(X, -) ∘ Φ_P`.  Then the five maps of the
> Mayer–Vietoris triangle
>
> `RΓ(X, E) ⟶ RΓ(U, E) ⊕ RΓ(V, E) ⟶ RΓ(U ×_X V, E) ⟶ RΓ(X, E)[1]`
>
> are the components of *natural transformations* of functors on `D(𝒪_X)`, every component
> triangle is distinguished, and its homology sequence is exact at every `n`.  So a morphism
> `E ⟶ E'` induces a morphism of the two triangles and of the two long exact sequences.
>
> **The four maps are the restriction maps, written out in the statement and not existentially
> quantified.**  The two out of `RΓ(X, -)` are `CategoryTheory.Functor.rightDerivedNatTrans` of
> `Γ(X, -)` applied to the units `F ⟶ j_{U,*}F|_U` and `F ⟶ j_{V,*}F|_V` of the adjunctions
> `(-)|_Y ⊣ j_{Y,*}` of Stacks 03LU — that is, of the restriction maps
> `Γ(X, F) ⟶ Γ(X, j_{U,*}F|_U) = Γ(U, F|_U)` and `Γ(X, F) ⟶ Γ(V, F|_V)` — and the two into
> `RΓ(U ×_X V, -)` are `CategoryTheory.Functor.rightDerivedNatTrans` of `Γ(X, -)` applied to the
> two comparisons `j_{U,*}F|_U ⟶ j_{P,*}F|_P` and `j_{V,*}F|_V ⟶ j_{P,*}F|_P` of Stacks 08GW
> part (1): the conjugates, under the adjunctions `j_{Y!}((-)|_Y) ⊣ j_{Y,*}((-)|_Y)`, of the
> extension-by-zero comparisons `AlgebraicGeometry.Space.edsShriekOpenComparison` and
> `AlgebraicGeometry.Space.edsShriekEtaleComparison` of Stacks 08GV, at the extension by zero the
> library constructs (`AlgebraicGeometry.Space.edsLowerShriekAdjOpen` and its two companions).
> They are the same four maps as in Stacks 08GW part (2),
> `AlgebraicGeometry.Space.exists_mem_distTriang_edsDerivedRestrictPushMayerVietorisLowerShriek`.
>
> Only the connecting transformation `δ : RΓ(P, -) ⟶ RΓ(X, -) ⋙ (-)[1]` is existentially
> quantified: the library attaches no canonical such map to an object of `D(𝒪_X)`, and the source
> likewise asserts only that a triangle with these three terms and these four maps is
> distinguished, as Stacks 08GV part (2) and Stacks 08GW part (2) do.
>
> This is `AlgebraicGeometry.Space.exists_natTrans_mem_distTriang_edsSectionsMayerVietoris` with
> its hypothesis `hMV` — part (1) of Stacks 08GW — discharged and its four maps named.  The
> sequence
> `0 ⟶ M ⟶ Φ_U M ⊕ Φ_V M ⟶ Φ_P M ⟶ 0` enters the proof only at the terms of a termwise injective
> K-injective resolution of `E` (Stacks 079P,
> `AlgebraicGeometry.Space.exists_quasiIso_isKInjective_injective_modules`), and at an *injective*
> module it is proved outright from part (1) of Stacks 08GV:
> `AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietoris_of_injective`.  So the
> surjectivity on the right, which at a general module is the étale-local vanishing of an
> obstruction in `Ext¹(𝒪_X, F) = H¹(X, F)` (Stacks 01FW) and is still the hypothesis `hepi` of
> `AlgebraicGeometry.Space.shortExact_edsRestrictPushMayerVietoris`, is not needed here at all.
>
> As in the conditional statements, the three outer terms are the derived functors of
> `Γ(X, -) ∘ j_{Y,*} ∘ (-)|_Y` in that factored form; that this is `RΓ(Y, E|_Y)` is the
> adjunction of Stacks 03LU, `Stacks.Cohomology.SiteModules.globalSectionsPushforwardIso`, and is
> not transported here.

```lean
theorem exists_delta_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))) :
    ∃ δ : RP ⟶ RX ⋙ shiftFunctor (DerivedCategory (ModuleCat.{u + 1}
        (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) (1 : ℤ),
      ∀ E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2),
        Triangle.mk
            (biprod.lift
              ((Functor.rightDerivedNatTrans RX RU αX αU
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (mapUnit (edsAdjOpen B S hS hsq).unit
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
              ((Functor.rightDerivedNatTrans RX RV αX αV
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (mapUnit (edsAdjEtale B S hS hsq).unit
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))
            (biprod.desc
              ((Functor.rightDerivedNatTrans RU RP αU αP
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (Functor.whiskerRight (conjugateEquiv
                      ((edsAdjOpen B S hS hsq).comp (edsLowerShriekAdjOpen B S hS hsq))
                      ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                      (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                        (edsLowerShriekAdjInter B S hS hsq)))
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
              (-((Functor.rightDerivedNatTrans RV RP αV αP
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (Functor.whiskerRight (conjugateEquiv
                      ((edsAdjEtale B S hS hsq).comp (edsLowerShriekAdjEtale B S hS hsq))
                      ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                      (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                        (edsLowerShriekAdjInter B S hS hsq)))
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)))
            (δ.app E) ∈
          distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
            ((Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) ∧
        ∀ n : ℤ, ((DerivedCategory.homologyFunctor (ModuleCat.{u + 1} (RingCat.sectionsSubring
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))
            0).homologySequenceComposableArrows₅
          (Triangle.mk
            (biprod.lift
              ((Functor.rightDerivedNatTrans RX RU αX αU
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (mapUnit (edsAdjOpen B S hS hsq).unit
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
              ((Functor.rightDerivedNatTrans RX RV αX αV
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (mapUnit (edsAdjEtale B S hS hsq).unit
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))
            (biprod.desc
              ((Functor.rightDerivedNatTrans RU RP αU αP
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (Functor.whiskerRight (conjugateEquiv
                      ((edsAdjOpen B S hS hsq).comp (edsLowerShriekAdjOpen B S hS hsq))
                      ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                      (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                        (edsLowerShriekAdjInter B S hS hsq)))
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
              (-((Functor.rightDerivedNatTrans RV RP αV αP
                (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
                (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                  (Functor.whiskerRight (conjugateEquiv
                      ((edsAdjEtale B S hS hsq).comp (edsLowerShriekAdjEtale B S hS hsq))
                      ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                      (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                        (edsLowerShriekAdjInter B S hS hsq)))
                    (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                      ((Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS W.1 W.2).O))))
                  (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)))
            (δ.app E)) n (n + 1) rfl).Exact
```

**`AlgebraicGeometry.Space.exists_delta_mem_distTriang_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean, line 709](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean#L709). The attribute's comment: “FIRST CLAUSE: every E of D(O\_X) sits in a distinguished triangle RGamma(X,E) -> RGamma(U,E) (+) RGamma(V,E) -> RGamma(U x\_X V,E) -> RGamma(X,E)[1] whose four first maps are NAMED in the statement: the right derived transformations of the restriction maps RGamma(X,-) -> RGamma(U,-), RGamma(V,-) and RGamma(U,-), RGamma(V,-) -> RGamma(U x\_X V,-). Only the connecting delta is existential, as in the source. No hypothesis beyond the square and the four derived functors presenting RGamma. The other two clauses are exists\_delta\_homologySequence\_exact\_edsSectionsMayerVietoris\_unconditional and exists\_delta\_natTrans\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, the distinguished triangle, with nothing granted.**
>
> In the situation of `exists_delta_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional`,
> every object `E` of `D(𝒪_X)` sits in a distinguished triangle
>
> `RΓ(X, E) ⟶ RΓ(U, E) ⊕ RΓ(V, E) ⟶ RΓ(U ×_X V, E) ⟶ RΓ(X, E)[1]`.
>
> **Its four first maps are the restriction maps, written out in the statement and not
> existentially quantified**, exactly as in
> `exists_delta_natTrans_mem_distTriang_edsSectionsMayerVietoris_unconditional`, whose component
> at `E` this is: the right derived transformations of `Γ(X, -)` applied to the units
> `F ⟶ j_{U,*}F|_U`, `F ⟶ j_{V,*}F|_V` of Stacks 03LU and to the two comparisons
> `j_{U,*}F|_U ⟶ j_{P,*}F|_P`, `j_{V,*}F|_V ⟶ j_{P,*}F|_P` of Stacks 08GW part (1).  Only the
> connecting map `δ : RΓ(P, E) ⟶ RΓ(X, E)[1]` is existentially quantified, as it is in the source
> and in Stacks 08GV part (2) and Stacks 08GW part (2).
>
> This is `AlgebraicGeometry.Space.exists_mem_distTriang_edsSectionsMayerVietoris` with its
> hypothesis `hMV` — part (1) of Stacks 08GW — discharged, by the same observation: the sequence
> is used at an injective module only, and there it is a theorem; and with its four maps named.

```lean
theorem exists_delta_mem_distTriang_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ δ : RP.obj E ⟶ (RX.obj E)⟦(1 : ℤ)⟧,
      Triangle.mk
          (biprod.lift
            ((Functor.rightDerivedNatTrans RX RU αX αU
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjOpen B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            ((Functor.rightDerivedNatTrans RX RV αX αV
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjEtale B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))
          (biprod.desc
            ((Functor.rightDerivedNatTrans RU RP αU αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjOpen B S hS hsq).comp (edsLowerShriekAdjOpen B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            (-((Functor.rightDerivedNatTrans RV RP αV αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjEtale B S hS hsq).comp (edsLowerShriekAdjEtale B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))) δ ∈
        distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
```

**`AlgebraicGeometry.Space.exists_delta_homologySequence_exact_edsSectionsMayerVietoris_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean, line 823](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisSectionsNamed.lean#L823). The attribute's comment: “SECOND CLAUSE: every E of D(O\_X) sits in a long exact cohomology sequence ... -> H^n(X,E) -> H^n(U,E) (+) H^n(V,E) -> H^n(U x\_X V,E) -> H^\{n+1}(X,E) -> ... whose maps are H^n of the NAMED restriction maps -- the triangle it is the homology sequence of has its four first maps written out, the right derived transformations of RGamma(X,-) -> RGamma(U,-), RGamma(V,-) and RGamma(U,-), RGamma(V,-) -> RGamma(U x\_X V,-); only the connecting delta is existential, as in the source. No hypothesis beyond the square and the four derived functors presenting RGamma. It is the homology sequence of the triangle of exists\_delta\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional; functoriality is exists\_delta\_natTrans\_mem\_distTriang\_edsSectionsMayerVietoris\_unconditional”.

> **Stacks 0CRS, the long exact cohomology sequence, with nothing granted.**
>
> The distinguished triangle of
> `AlgebraicGeometry.Space.exists_delta_mem_distTriang_edsSectionsMayerVietoris_unconditional` has an
> exact homology sequence, which at each `n` is the six-term exact sequence
>
> `H^n(X,E) ⟶ H^n(U,E) ⊕ H^n(V,E) ⟶ H^n(U ×\_X V,E) ⟶ H^\{n+1}(X,E) ⟶ H^\{n+1}(U,E) ⊕ H^\{n+1}(V,E)
> ⟶ H^\{n+1}(U ×\_X V,E)`
>
> — the Mayer–Vietoris long exact sequence of the source, since the homology functor is additive
> and so carries the biproduct `RΓ(U,E) ⊕ RΓ(V,E)` to `H^n(U,E) ⊕ H^n(V,E)`.
>
> **Its maps are the restriction maps on cohomology**, because the triangle whose homology
> sequence this is carries its four maps written out: they are the right derived transformations
> of `Γ(X, -)` applied to the units `F ⟶ j_{U,*}F|_U`, `F ⟶ j_{V,*}F|_V` of Stacks 03LU and to
> the two comparisons `j_{U,*}F|_U ⟶ j_{P,*}F|_P`, `j_{V,*}F|_V ⟶ j_{P,*}F|_P` of Stacks 08GW
> part (1), so the maps of the long exact sequence are `H^n` of them.  Only the connecting map
> `δ`, and with it `H^n(U ×_X V,E) ⟶ H^{n+1}(X,E)`, is existentially quantified, as in the
> source.
>
> This is `AlgebraicGeometry.Space.exists_homologySequence_exact_edsSectionsMayerVietoris` with
> its hypothesis `hMV` — part (1) of Stacks 08GW — discharged and its four maps named.

```lean
theorem exists_delta_homologySequence_exact_edsSectionsMayerVietoris_unconditional
    (RX RU RV RP : DerivedCategory (Modules.{u, u} B S hS W.1 W.2) ⥤
      DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj)))
    (αX : (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RX)
    (αU : (edsRestrictPushOpen B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RU)
    (αV : (edsRestrictPushEtale B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RV)
    (αP : (edsRestrictPushInter B S hS hsq ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    (hRX : RX.IsRightDerivedFunctor αX
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRU : RU.IsRightDerivedFunctor αU
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRV : RV.IsRightDerivedFunctor αV
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (hRP : RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ)))
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2)) :
    ∃ δ : RP.obj E ⟶ (RX.obj E)⟦(1 : ℤ)⟧,
      Triangle.mk
          (biprod.lift
            ((Functor.rightDerivedNatTrans RX RU αX αU
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjOpen B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            ((Functor.rightDerivedNatTrans RX RV αX αV
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjEtale B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))
          (biprod.desc
            ((Functor.rightDerivedNatTrans RU RP αU αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjOpen B S hS hsq).comp (edsLowerShriekAdjOpen B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            (-((Functor.rightDerivedNatTrans RV RP αV αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjEtale B S hS hsq).comp (edsLowerShriekAdjEtale B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))) δ ∈
        distTriang (DerivedCategory (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))) ∧
      ∀ n : ℤ, ((DerivedCategory.homologyFunctor (ModuleCat.{u + 1} (RingCat.sectionsSubring
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS W.1 W.2).O)).obj))
          0).homologySequenceComposableArrows₅
        (Triangle.mk
          (biprod.lift
            ((Functor.rightDerivedNatTrans RX RU αX αU
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjOpen B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            ((Functor.rightDerivedNatTrans RX RV αX αV
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (mapUnit (edsAdjEtale B S hS hsq).unit
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))
          (biprod.desc
            ((Functor.rightDerivedNatTrans RU RP αU αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjOpen B S hS hsq).comp (edsLowerShriekAdjOpen B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekOpenComparison B S hS hsq (edsLowerShriekAdjOpen B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E)
            (-((Functor.rightDerivedNatTrans RV RP αV αP
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS W.1 W.2) (ComplexShape.up ℤ))
              (Functor.whiskerRight (NatTrans.mapHomotopyCategory
                (Functor.whiskerRight (conjugateEquiv
                    ((edsAdjEtale B S hS hsq).comp (edsLowerShriekAdjEtale B S hS hsq))
                    ((edsAdjInter B S hS hsq).comp (edsLowerShriekAdjInter B S hS hsq))
                    (edsShriekEtaleComparison B S hS hsq (edsLowerShriekAdjEtale B S hS hsq)
                      (edsLowerShriekAdjInter B S hS hsq)))
                  (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{u + 1, u, u, u}
                    ((Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS W.1 W.2).O))))
                (ComplexShape.up ℤ)) DerivedCategory.Qh)).app E))) δ) n (n + 1) rfl).Exact
```

## Tag 08HA, a lemma

[Tag 08HA](https://stacks.math.columbia.edu/tag/08HA) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_restrictEtaleModuleLowerShriekMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictEtaleModuleLowerShriek.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictEtaleModuleLowerShriek.lean#L79). The attribute's comment: “on modules, for the constructed extension by zero”.

> **Stacks 08HA**, on sheaves of modules. Let `j : U ⟶ X` and `j_V : V ⟶ X` be étale morphisms of
> algebraic spaces, let `W = V ×_X U` with projections `j_W : W ⟶ V` and `p : W ⟶ U`, and let `F` be
> a sheaf of `𝒪_U`-modules. Then the canonical map `j_{W!}(F|_W) ⟶ (j_!F)|_V` is an isomorphism, that
> is, `(j_!F)|_V = j_{W!}(F|_W)`, where `j_!` and `j_{W!}` are the extensions by zero
> `AlgebraicGeometry.Space.etaleModuleLowerShriek`.

```lean
theorem isIso_restrictEtaleModuleLowerShriekMap :
    IsIso (restrictExtensionByZeroMap B S hS sq hj hjV
      (etaleModuleLowerShriekAdjunction B S hS j hj)
      (etaleModuleLowerShriekAdjunction B S hS jW
        (isEtale_of_isPullback B S hS p jW j jV sq.flip hj)))
```

**`AlgebraicGeometry.Space.isIso_derivedRestrictEtaleModuleLowerShriekMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictEtaleModuleLowerShriek.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictEtaleModuleLowerShriek.lean#L135). The attribute's comment: “for the constructed extension by zero, on any model of the derived categories”.

> **Stacks 08HA.** Let `j : U ⟶ X` and `j_V : V ⟶ X` be étale morphisms of algebraic spaces, let
> `W = V ×_X U` with projections `j_W : W ⟶ V` and `p : W ⟶ U`, and let `E` be an object of the
> unbounded derived category of `𝒪_U`-modules. Then the canonical map `j_{W!}(E|_W) ⟶ (j_!E)|_V` is
> an isomorphism, that is, `(j_!E)|_V = j_{W!}(E|_W)`, where `j_!` and `j_{W!}` are the derived
> functors of the exact extensions by zero `AlgebraicGeometry.Space.etaleModuleLowerShriek`.

```lean
theorem isIso_derivedRestrictEtaleModuleLowerShriekMap :
    IsIso (derivedRestrictEtaleModuleLowerShriekMap B S hS sq hj hjV)
```

**`AlgebraicGeometry.Space.isIso_restrictExtensionByZeroMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictExtensionByZero.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictExtensionByZero.lean#L211). The attribute's comment: “on modules”.

> **Stacks 08HA**, on sheaves of modules.  Let `j : U ⟶ X` and `j_V : V ⟶ X` be étale
> morphisms of algebraic spaces, let `W = V ×_X U` with projections `j_W : W ⟶ V` and `p : W ⟶ U`,
> and let `F` be a sheaf of `𝒪_U`-modules.  Then the canonical map
> `j_{W!}(F|_W) ⟶ (j_!F)|_V` is an isomorphism, that is, `(j_!F)|_V = j_{W!}(F|_W)`.

```lean
theorem isIso_restrictExtensionByZeroMap :
    IsIso (restrictExtensionByZeroMap B S hS sq hj hjV adj adjW)
```

**`AlgebraicGeometry.Space.isIso_derivedRestrictExtensionByZeroMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictExtensionByZero.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RestrictExtensionByZero.lean#L250).

> **Stacks 08HA.**  Let `j : U ⟶ X` and `j_V : V ⟶ X` be étale morphisms of algebraic spaces,
> let `W = V ×_X U` with projections `j_W : W ⟶ V` and `p : W ⟶ U`, and let `E` be an object of
> the unbounded derived category of `𝒪_U`-modules.  Then the canonical map
> `j_{W!}(E|_W) ⟶ (j_!E)|_V` is an isomorphism, that is, `(j_!E)|_V = j_{W!}(E|_W)`.

```lean
theorem isIso_derivedRestrictExtensionByZeroMap :
    IsIso (derivedRestrictExtensionByZeroMap B S hS sq hj hjV adj adjW)
```

## Tag 08GG, a lemma

[Tag 08GG](https://stacks.math.columbia.edu/tag/08GG) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_edsEtaleDerivedAdjunction_unit_app_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroSupported.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtensionByZeroSupported.lean#L517). The attribute's comment: “clause (2)(a): F ⟶ (j\_!F)|\_V is an isomorphism for F supported on j^\{-1}T”.

> **Stacks 08GG, clause (2)(a).**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished
> square of algebraic spaces and `T = |X| \ |U|`.  For an object `F` of `D(𝒪_V)` supported on
> `j^{-1}T` the unit `F ⟶ (j_!F)|_V` of the derived adjunction `j_! ⊣ (-)|_V` is an
> isomorphism.
>
> Both functors are exact, so on cohomology the derived unit is the unit at `Hⁱ(F)`, which is an
> isomorphism by the stalk computation of Equation 08GU, the square having exactly one lift of
> each geometric point over `T`.

```lean
theorem isIso_edsEtaleDerivedAdjunction_unit_app_of_cohomologySupportedOn
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso ((edsEtaleDerivedAdjunction B S hS hsq).unit.app F)
```

**`AlgebraicGeometry.Space.isIso_derivedCounit_edsEtale_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedExtensionByZero.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedExtensionByZero.lean#L126). The attribute's comment: “clause (1)(b): the derived counit j\_!(E|\_V) ⟶ E is an isomorphism for E in D(O\_X) supported on T = |X| \ |U|, unconditionally”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  For `E` in `D(𝒪_X)` supported on `T`, the counit
> `j_!(E|_V) ⟶ E` is an isomorphism.

```lean
theorem isIso_derivedCounit_edsEtale_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso ((NatTrans.mapDerivedCategory (edsEtaleShriekAdjunction B S hS hsq).counit).app E)
```

**`AlgebraicGeometry.Space.isIso_derivedUnit_edsEtale_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedExtensionByZero.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedExtensionByZero.lean#L150). The attribute's comment: “clause (2)(a): the unit F ⟶ (j\_!F)|\_V is an isomorphism for F in D(O\_V) supported on j^\{-1}T, unconditionally”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  For `F` in `D(𝒪_V)` supported on `j⁻¹T`, the unit
> `F ⟶ (j_!F)|_V` is an isomorphism.

```lean
theorem isIso_derivedUnit_edsEtale_of_cohomologySupportedOn
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso ((Adjunction.mapDerivedCategory (edsEtaleShriekAdjunction B S hS hsq)).unit.app F)
```

**`AlgebraicGeometry.Space.isIso_derivedUnit_edsDerivedRestrictPushEtale_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementCanonical.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementCanonical.lean#L130). The attribute's comment: “clause (1)(a): the canonical map E ⟶ Rj\_*(E|\_V) is an isomorphism for E supported on |X| \ |U|, at the chosen total right derived functors”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`. For an object `E` of `D(𝒪_X)` supported on `T`, the
> canonical map `E ⟶ Rj_{V,*}(E|_V)` into the chosen total right derived direct image is an
> isomorphism.

```lean
theorem isIso_derivedUnit_edsDerivedRestrictPushEtale_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso ((derivedUnitOfNatTrans (edsAdjEtale B S hS hsq).unit
      (edsDerivedRestrictPushEtale B S hS hsq)
      (edsTotalRightDerivedUnitEtale B S hS hsq)).app E)
```

**`AlgebraicGeometry.Space.isIso_unit_derivedRestrict_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L282). The attribute's comment: “clause (1)(a): for E in D(O\_X) supported on T = |X| \ |U| the map E ⟶ Rj\_*(E|\_V), the unit of the adjunction between derived restriction and the derived direct image, is an isomorphism. Rj\_* is any right adjoint of derived restriction, which pins it and its unit; a total right derived functor of j\_* is one, by etaleModulePullbackDerivedPushforwardAdjunction”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  Let `Rj_*` be a right adjoint of derived restriction
> `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.  If `E` in `D(𝒪_X)` is supported on `T`, then the unit
> `E ⟶ Rj_*(E|_V)` is an isomorphism.

```lean
theorem isIso_unit_derivedRestrict_of_cohomologySupportedOn
    {RpushD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjPush : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory ⊣ RpushD)
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso (adjPush.unit.app E)
```

**`AlgebraicGeometry.Space.isIso_counit_derivedRestrict_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L302). The attribute's comment: “clause (1)(b): for E in D(O\_X) supported on T = |X| \ |U| the map j\_!(E|\_V) ⟶ E, the counit of the adjunction between derived extension by zero and derived restriction, is an isomorphism. j\_! is any left adjoint of derived restriction, which pins it and its counit; the derived functor of etaleModuleLowerShriek is one”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  Let `j_!` be a left adjoint of derived restriction
> `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.  If `E` in `D(𝒪_X)` is supported on `T`, then the counit
> `j_!(E|_V) ⟶ E` is an isomorphism.

```lean
theorem isIso_counit_derivedRestrict_of_cohomologySupportedOn
    {shriekD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjShriek : shriekD ⊣ (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory)
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso (adjShriek.counit.app E)
```

**`AlgebraicGeometry.Space.isIso_unit_derivedShriek_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L401). The attribute's comment: “clause (2)(a): for F in D(O\_V) supported on the preimage of T = |X| \ |U| the map F ⟶ (j\_!F)|\_V, the unit of the adjunction between derived extension by zero and derived restriction, is an isomorphism. j\_! is any left adjoint of derived restriction, which pins it and its unit; the derived functor of etaleModuleLowerShriek is one”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  Let `j_!` be a left adjoint of derived restriction
> `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.  If `F` in `D(𝒪_V)` is supported on `j^{-1}T`, then the unit
> `F ⟶ (j_!F)|_V` is an isomorphism.

```lean
theorem isIso_unit_derivedShriek_of_cohomologySupportedOn
    {shriekD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjShriek : shriekD ⊣ (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory)
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso (adjShriek.unit.app F)
```

**`AlgebraicGeometry.Space.isIso_counit_derivedPushforward_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L448). The attribute's comment: “clause (2)(b): for F in D(O\_V) supported on the preimage of T = |X| \ |U| the map (Rj\_*F)|\_V ⟶ F, the counit of the adjunction between derived restriction and the derived direct image, is an isomorphism. Rj\_* is any right adjoint of derived restriction, which pins it and its counit; a total right derived functor of j\_* is one, by etaleModulePullbackDerivedPushforwardAdjunction”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  Let `Rj_*` be a right adjoint of derived restriction
> `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.  If `F` in `D(𝒪_V)` is supported on `j^{-1}T`, then the counit
> `(Rj_*F)|_V ⟶ F` is an isomorphism.

```lean
theorem isIso_counit_derivedPushforward_of_cohomologySupportedOn
    {RpushD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjPush : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory ⊣ RpushD)
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso (adjPush.counit.app F)
```

**`AlgebraicGeometry.Space.isIso_supportedShriekToPushforward_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L480). The attribute's comment: “clause (2)(c): for F in D(O\_V) supported on the preimage of T = |X| \ |U| the comparison j\_!F ⟶ Rj\_*F is an isomorphism. The comparison is supportedShriekToPushforward, the adjunct under derived restriction ⊣ Rj\_* of the inverse of the unit F ⟶ (j\_!F)|\_V, which is invertible by clause (2)(a), isIso\_unit\_derivedShriek\_of\_cohomologySupportedOn. j\_! and Rj\_* are any left and right adjoints of derived restriction”.

> Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of algebraic spaces over a
> scheme `S` and set `T = |X| \ |U|`.  Let `j_!` and `Rj_*` be a left and a right adjoint of
> derived restriction `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.  If `F` in `D(𝒪_V)` is supported on `j^{-1}T`,
> then the comparison `j_!F ⟶ Rj_*F` (`AlgebraicGeometry.Space.supportedShriekToPushforward`) is
> an isomorphism.

```lean
theorem isIso_supportedShriekToPushforward_of_supported
    {shriekD RpushD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjShriek : shriekD ⊣ (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory)
    (adjPush : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory ⊣ RpushD)
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
      (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso (supportedShriekToPushforward B S hS hsq adjShriek adjPush F
      (isIso_unit_derivedShriek_of_cohomologySupportedOn B S hS hsq adjShriek F hF))
```

**`AlgebraicGeometry.Space.isIso_of_cohomologySupportedOn_edsEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementClauses.lean#L517). The attribute's comment: “all five clauses: for E in D(O\_X) supported on T = |X| \ |U| the unit E ⟶ Rj\_*(E|\_V) and the counit j\_!(E|\_V) ⟶ E are isomorphisms, and for F in D(O\_V) supported on the preimage of T the unit F ⟶ (j\_!F)|\_V, the counit (Rj\_*F)|\_V ⟶ F and the comparison j\_!F ⟶ Rj\_*F are isomorphisms. j\_! and Rj\_* are any left and right adjoints of derived restriction, which pins them and their units and counits; the derived functor of etaleModuleLowerShriek and a total right derived functor of j\_* are such adjoints”.

> Let `S` be a scheme, let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished square of
> algebraic spaces over `S` and set `T = |X| \ |U|`.  Let `j_!` and `Rj_*` be a left and a right
> adjoint of derived restriction `(-)|_V : D(𝒪_X) ⥤ D(𝒪_V)`.
>
> 1. If `E` in `D(𝒪_X)` is supported on `T`, then (a) `E ⟶ Rj_*(E|_V)` and (b) `j_!(E|_V) ⟶ E`
>    are isomorphisms.
> 2. If `F` in `D(𝒪_V)` is supported on `j^{-1}T`, then (a) `F ⟶ (j_!F)|_V`, (b)
>    `(Rj_*F)|_V ⟶ F` and (c) `j_!F ⟶ Rj_*F` are isomorphisms.
>
> The maps of (1)(a), (1)(b), (2)(a), (2)(b) are the units and counits of the two adjunctions,
> and the map of (2)(c) is `AlgebraicGeometry.Space.supportedShriekToPushforward`.

```lean
theorem isIso_of_cohomologySupportedOn_edsEtale
    {shriekD RpushD : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2) ⥤ DerivedCategory (Modules.{u, u} B S hS W.1 W.2)}
    (adjShriek : shriekD ⊣ (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory)
    (adjPush : (etaleModulePullback.{u, u} B S hS (edsEtaleHom B S hS hsq)
      (isEtale_edsEtaleHom B S hS hsq)).mapDerivedCategory ⊣ RpushD) :
    (∀ E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2),
      CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E →
        IsIso (adjPush.unit.app E) ∧ IsIso (adjShriek.counit.app E)) ∧
    (∀ (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1
        (edsEtale B S hS hsq).2))
      (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
        (edsEtalePreimageComplementPoints B S hS hsq) F),
        IsIso (adjShriek.unit.app F) ∧ IsIso (adjPush.counit.app F) ∧
          IsIso (supportedShriekToPushforward B S hS hsq adjShriek adjPush F
            (isIso_unit_derivedShriek_of_cohomologySupportedOn B S hS hsq adjShriek F hF)))
```

**`AlgebraicGeometry.Space.isIso_derivedCounit_etaleModuleLowerShriek_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementUnconditional.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedOnComplementUnconditional.lean#L132). The attribute's comment: “clause (1)(b): the derived counit j\_!(E|\_V) ⟶ E is an isomorphism for E supported on |X| \ |U|”.

> **Stacks 08GG, clause (1)(b).**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished
> square of algebraic spaces over a scheme `S` and set `T = |X| \ |U|`.  Let `E` be an object of
> `D(𝒪_X)` supported on `T`.  Then the derived counit `j_!(E|_V) ⟶ E` of the adjunction
> `j_! ⊣ (-)|_V` is an isomorphism.
>
> The extension by zero is the one the library constructs, part (1) of Stacks 08GV for it is
> `AlgebraicGeometry.Space.shortExact_edsShriekMayerVietoris`, and the vanishing of the
> restrictions to `U` and to `P = U ×_X V` is
> `AlgebraicGeometry.Space.isZero_etaleModulePullback_mapDerivedCategory_of_cohomologySupportedOn`.
> The deduction itself is
> `AlgebraicGeometry.Space.isIso_counit_mapDerivedCategory_of_cohomologySupportedOn`.

```lean
theorem isIso_derivedCounit_etaleModuleLowerShriek_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso ((NatTrans.mapDerivedCategory
      (edsLowerShriekAdjEtale B S hS hsq).counit).app E)
```

**`AlgebraicGeometry.Space.isIso_counit_edsEtale_rightAdjoint_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean#L267). The attribute's comment: “clause (2)(b): the counit (Rj\_*F)|\_V ⟶ F is an isomorphism for F in D(O\_V) supported on j^\{-1}T, unconditionally; Rj\_* is a right adjoint of derived restriction, given with its adjunction”.

> **Stacks 08GG, clause (2)(b).**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished
> square of algebraic spaces over a scheme `S` and set `T = |X| \ |U|`.  For `F` in `D(𝒪_V)`
> supported on `j⁻¹T`, the counit `(Rj_*F)|_V ⟶ F` is an isomorphism.
>
> `Rj_*` is a right adjoint of derived restriction, given with its adjunction.  The proof is
> `CategoryTheory.Adjunction.isIso_counit_of_isIso_unit_of_isIso_counit` applied to
> `j_! ⊣ (-)|_V ⊣ Rj_*`; its three inputs are clause (2)(a) at `F` and at `(Rj_*F)|_V`, and
> clause (1)(b) at `Rj_*F`, which is supported on `T` because it vanishes on `U`
> (`isZero_edsDerivedRestrictOpen_rightAdjoint_of_cohomologySupportedOn`).

```lean
theorem isIso_counit_edsEtale_rightAdjoint_of_cohomologySupportedOn
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso (adjPush.counit.app F)
```

**`AlgebraicGeometry.Space.isIso_unit_edsEtale_rightAdjoint_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean#L315). The attribute's comment: “clause (1)(a): the unit E ⟶ Rj\_*(E|\_V) is an isomorphism for E in D(O\_X) supported on T = |X| \ |U|, unconditionally; Rj\_* is a right adjoint of derived restriction, given with its adjunction”.

> **Stacks 08GG, clause (1)(a).**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished
> square of algebraic spaces over a scheme `S` and set `T = |X| \ |U|`.  For `E` in `D(𝒪_X)`
> supported on `T`, the unit `E ⟶ Rj_*(E|_V)` is an isomorphism.
>
> Its restriction to `V` is a section of the counit at `E|_V`, which is invertible by clause
> (2)(b); both `E` and `Rj_*(E|_V)` are supported on `T`, and a map between such objects which is
> invertible on `V` is invertible (`isIso_of_isIso_edsDerivedRestrictEtale_map`).

```lean
theorem isIso_unit_edsEtale_rightAdjoint_of_cohomologySupportedOn
    (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
    (hE : CohomologySupportedOn B S hS W.1 W.2 (edsComplementPoints B S hS Uo) E) :
    IsIso (adjPush.unit.app E)
```

**`AlgebraicGeometry.Space.isIso_supportedShriekToPushforward_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPushforwardPerfect.lean#L344). The attribute's comment: “clause (2)(c): the comparison j\_!F ⟶ Rj\_*F is an isomorphism for F in D(O\_V) supported on j^\{-1}T, unconditionally; j\_! and Rj\_* are the left and right adjoints of derived restriction, given with their adjunctions”.

> **Stacks 08GG, clause (2)(c).**  Let `(U ⊆ X, j : V ⟶ X)` be an elementary distinguished
> square of algebraic spaces over a scheme `S` and set `T = |X| \ |U|`.  For `F` in `D(𝒪_V)`
> supported on `j⁻¹T`, the comparison `j_!F ⟶ Rj_*F` is an isomorphism.
>
> The comparison is the library's `AlgebraicGeometry.Space.supportedShriekToPushforward`, the
> adjunct of the inverse of the unit of clause (2)(a); its invertibility is
> `AlgebraicGeometry.Space.isIso_supportedShriekToPushforward` with all four of its inputs, clauses
> (2)(a), (2)(b) and (1)(a) at `j_!F` and at `Rj_*F`, now theorems.

```lean
theorem isIso_supportedShriekToPushforward_of_cohomologySupportedOn
    (F : DerivedCategory (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (hF : CohomologySupportedOn B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2
      (edsEtalePreimageComplementPoints B S hS hsq) F) :
    IsIso (supportedShriekToPushforward B S hS hsq
      (Adjunction.mapDerivedCategory (edsEtaleShriekAdjunction B S hS hsq)) adjPush F
      (isIso_derivedUnit_edsEtale_of_cohomologySupportedOn B S hS hsq F hF))
```

## Tag 08HB, a lemma

[Tag 08HB](https://stacks.math.columbia.edu/tag/08HB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_glued_object_and_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisGlueingTag.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/MayerVietorisGlueingTag.lean#L241). The attribute's comment: “both assertions, for an elementary distinguished square (U ⊆ X, j\_V : V ⟶ X) of algebraic spaces over a scheme S with intersection P = U ×\_X V and nothing else bound: for an object A of D(O\_U), an object Bo of D(O\_V) and an isomorphism c : A|\_P ≅ Bo|\_P, an object F of D(O\_X) with isomorphisms f : F|\_U ≅ A and g : F|\_V ≅ Bo satisfying c = g|\_P ∘ f⁻¹|\_P, and, for every object E of D(O\_X) and all morphisms a : A ⟶ E|\_U and b : Bo ⟶ E|\_V with a|\_P = b|\_P ∘ c, a morphism φ : F ⟶ E whose restriction to U is a ∘ f and whose restriction to V is b ∘ g. The compatibility over P is written with the identifications edsDerivedRestrictCompOpen and edsDerivedRestrictCompEtale of the iterated restrictions with the restriction to P”.

> **Stacks 08HB.**  Let `(U ⊆ X, j_V : V ⟶ X)` be an elementary distinguished square of
> algebraic spaces over a scheme `S`, let `P = U ×_X V` be its intersection and write `(-)|_Y`
> for restriction of modules along the étale morphism `j_Y : Y ⟶ X`.  Then an object `A` of
> `D(𝒪_U)`, an object `Bo` of `D(𝒪_V)` and an isomorphism `c : A|_P ⟶ Bo|_P` are glued by an
> object `F` of `D(𝒪_X)` together with isomorphisms `f : F|_U ⟶ A` and `g : F|_V ⟶ Bo`
> satisfying `c = g|_P ∘ f^{-1}|_P`; and moreover, for every object `E` of `D(𝒪_X)` and all
> morphisms `a : A ⟶ E|_U` and `b : Bo ⟶ E|_V` with `a|_P = b|_P ∘ c`, there is a morphism
> `φ : F ⟶ E` restricting to `a ∘ f` on `U` and to `b ∘ g` on `V`.
>
> The glued object is the source's own, the fibre of
> `Rj_{U,*}A ⊕ Rj_{V,*}Bo ⟶ Rj_{P,*}(Bo|_P)`, built in
> `AlgebraicGeometry.Space.exists_glued_object`; the induced morphism is
> `AlgebraicGeometry.Space.exists_hom_of_glueData_of_isElementaryDistinguishedSquare` at the
> canonical extension by zero, whose hypothesis `hc` is in exactly the shape the first conclusion
> has.  The compatibility over `P` is written with the identifications
> `AlgebraicGeometry.Space.edsDerivedRestrictCompOpen` and `…edsDerivedRestrictCompEtale` of the
> iterated restrictions with the restriction to `P`, which the source writes silently.
>
> The source's object `B` of `D(𝒪_V)` is written `Bo` here, the letter `B` being the big fppf
> site.

```lean
theorem exists_glued_object_and_hom
    (A : DerivedCategory
      (Modules.{u, u} B S hS (edsOpen B S hS hsq).1 (edsOpen B S hS hsq).2))
    (Bo : DerivedCategory
      (Modules.{u, u} B S hS (edsEtale B S hS hsq).1 (edsEtale B S hS hsq).2))
    (c : (edsRestrictFst B S hS hsq).mapDerivedCategory.obj A ≅
      (edsRestrictSnd B S hS hsq).mapDerivedCategory.obj Bo) :
    ∃ (F : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
      (f : (edsRestrictOpen B S hS hsq).mapDerivedCategory.obj F ≅ A)
      (g : (edsRestrictEtale B S hS hsq).mapDerivedCategory.obj F ≅ Bo),
      c.hom = (edsRestrictFst B S hS hsq).mapDerivedCategory.map f.inv ≫
          (edsDerivedRestrictCompOpen B S hS hsq).hom.app F ≫
            (edsDerivedRestrictCompEtale B S hS hsq).inv.app F ≫
            (edsRestrictSnd B S hS hsq).mapDerivedCategory.map g.hom ∧
        ∀ (E : DerivedCategory (Modules.{u, u} B S hS W.1 W.2))
          (a : A ⟶ (edsRestrictOpen B S hS hsq).mapDerivedCategory.obj E)
          (b : Bo ⟶ (edsRestrictEtale B S hS hsq).mapDerivedCategory.obj E),
          (edsRestrictFst B S hS hsq).mapDerivedCategory.map a ≫
              (edsDerivedRestrictCompOpen B S hS hsq).hom.app E =
            c.hom ≫ (edsRestrictSnd B S hS hsq).mapDerivedCategory.map b ≫
              (edsDerivedRestrictCompEtale B S hS hsq).hom.app E →
          ∃ φ : F ⟶ E,
            (edsRestrictOpen B S hS hsq).mapDerivedCategory.map φ = f.hom ≫ a ∧
              (edsRestrictEtale B S hS hsq).mapDerivedCategory.map φ = g.hom ≫ b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.10, Tag 08GS](https://stacks.math.columbia.edu/tag/08GS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
