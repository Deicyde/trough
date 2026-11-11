---
declaration: section
origin: cited
lean: CategoryTheory.Stalk.presheafPushforward_stalk_iso, Stacks.Sheaves.StalkInverseImage.stalkAddEquiv, Stacks.Sheaves.StalkInverseImage.stalkAddEquiv_smul, Stacks.Sheaves.StalkInverseImage.stalkNatIso, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv_smul, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkNatIso, point_morphism_sites
statement: formalized
proof: formalized
---

# 7.34 Points and morphisms of topoi

Section 7.34 of the Stacks Project, [Tag 05V0](https://stacks.math.columbia.edu/tag/05V0). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F4F, a lemma

[Tag 0F4F](https://stacks.math.columbia.edu/tag/0F4F) in the Stacks Project.

**`CategoryTheory.Stalk.presheafPushforward_stalk_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkPresheafPushforward.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkPresheafPushforward.lean#L73).

> **Stacks 0F4F**, packaged as the existence of the natural isomorphism
> `(u_p F)_v ≅ F_{v ∘ u}`.

```lean
theorem presheafPushforward_stalk_iso (u : C ⥤ D) (v : D ⥤ Type u) :
    Nonempty (u.op.lan ⋙ presheafStalk v ≅ presheafStalk (u ⋙ v))
```

## Tag 05V1, a lemma

[Tag 05V1](https://stacks.math.columbia.edu/tag/05V1) in the Stacks Project.

**`Stacks.Sheaves.StalkInverseImage.stalkAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L496). The attribute's comment: “for sheaves of modules, at a point of a site, for a morphism of topoi whose stalk functor at the target point is the inverse image followed by the stalk functor at the source point”.

> The stalk at `Φ` of the inverse image along `g` of a sheaf of `O`-modules is the stalk of
> that sheaf at `Ψ`, as an isomorphism of additive groups. It is semilinear over
> `Stacks.Sheaves.StalkInverseImage.stalkRingEquiv`; see
> `Stacks.Sheaves.StalkInverseImage.stalkAddEquiv_smul`.

```lean
def stalkAddEquiv :
    (Stacks.sheafModuleFiber Ψ O).obj G ≃+
      (Stacks.sheafModuleFiber Φ (inverseImageRingSheaf g O)).obj
        ((inverseImageModules g O).obj G)
```

**`Stacks.Sheaves.StalkInverseImage.stalkAddEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L526). The attribute's comment: “semilinearity of the comparison, for sheaves of modules”.

> The isomorphism of stalk modules is semilinear over the isomorphism of stalk rings: the
> stalk at `Φ` of the inverse image of `G` is the stalk of `G` at `Ψ`, with the scalars carried
> along `O_Ψ ≅ (g⁻¹O)_Φ`.

```lean
theorem stalkAddEquiv_smul (r : (Ψ.presheafFiber (A := RingCat.{w})).obj O.obj)
    (m : (Stacks.sheafModuleFiber Ψ O).obj G) :
    stalkAddEquiv g O Φ Ψ e G (r • m) =
      stalkRingEquiv g O Φ Ψ e r • stalkAddEquiv g O Φ Ψ e G m
```

**`Stacks.Sheaves.StalkInverseImage.stalkNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L600). The attribute's comment: “for sheaves of modules, as a natural isomorphism of stalk functors”.

> The stalk functor at `Ψ` is the inverse image of sheaves of modules followed by the stalk
> functor at `Φ` and restriction of scalars along the isomorphism of stalk rings.

```lean
def stalkNatIso :
    Stacks.sheafModuleFiber Ψ O ≅
      inverseImageModules g O ⋙ Stacks.sheafModuleFiber Φ (inverseImageRingSheaf g O) ⋙
        ModuleCat.restrictScalars (stalkRingEquiv g O Φ Ψ e).toRingHom
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L106). The attribute's comment: “for sheaves of modules, at the point of the target site attached to a point of the source site by part (2) of Stacks 00YA”.

> **Module-level Stacks 05V1 at the named point of the target site.**  The stalk at `Φ` of
> the inverse image of a sheaf of `O'`-modules is the stalk of that sheaf at `Ψ`, as an
> isomorphism of additive groups; it is semilinear over `targetStalkRingEquiv`.

```lean
def targetStalkAddEquiv :
    (Stacks.sheafModuleFiber (targetPoint f hu Φ)
        (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj G ≃+
      (Stacks.sheafModuleFiber Φ
          (inverseImageRingSheaf (f.toToposHom hu)
            (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))).obj
        ((inverseImageModules (f.toToposHom hu)
          (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj G)
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L122). The attribute's comment: “semilinearity, at the point of the target site attached to a point of the source site”.

> **Stacks 05V1 for sheaves of modules at the named point.**  The isomorphism of stalk
> modules is semilinear over the isomorphism of stalk rings.

```lean
theorem targetStalkAddEquiv_smul
    (r : ((targetPoint f hu Φ).presheafFiber (A := RingCat.{u})).obj
      (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj)
    (m : (Stacks.sheafModuleFiber (targetPoint f hu Φ)
      (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj G) :
    targetStalkAddEquiv f hu Φ G (r • m) =
      targetStalkRingEquiv f hu Φ r • targetStalkAddEquiv f hu Φ G m
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L162). The attribute's comment: “for sheaves of modules, as a natural isomorphism of stalk functors, at the point of the target site attached to a point of the source site”.

> **Module-level Stacks 05V1 at the named point, as a natural isomorphism of stalk
> functors.**  The stalk functor at `Ψ` is the inverse image of sheaves of modules followed by
> the stalk functor at `Φ` and restriction of scalars along the isomorphism of stalk rings.
>
> This is the form a statement about complexes consumes:
> `CategoryTheory.NatIso.mapHomologicalComplex` carries it to an isomorphism of the degreewise
> functors on cochain complexes.

```lean
def targetStalkNatIso :
    Stacks.sheafModuleFiber (targetPoint f hu Φ) (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ≅
      inverseImageModules (f.toToposHom hu) (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⋙
        Stacks.sheafModuleFiber Φ
            (inverseImageRingSheaf (f.toToposHom hu) (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ⋙
          ModuleCat.restrictScalars (targetStalkRingEquiv f hu Φ).toRingHom
```

**`point_morphism_sites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkAlongMorphism.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/StalkAlongMorphism.lean#L47).

> **Stacks 05V1.** For a point `q` of `(D, K)` and a morphism of sites given by
> `u : C ⥤ D`, the stalk functor at the induced point `q.comap u hu` of `(C, J)` is
> isomorphic to taking the inverse image along `u` and then the stalk at `q`.

```lean
theorem point_morphism_sites
    {C : Type u₁} [Category.{v} C] {D : Type u₂} [Category.{v} D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D}
    (u : C ⥤ D) [RepresentablyFlat u] [u.IsContinuous J K]
    (hu : CoverPreserving J K u)
    (q : Point.{w} K)
    [InitiallySmall (u ⋙ q.fiber).Elements]
    (A : Type*) [Category.{v} A] [HasProducts.{w} A]
    [(u.sheafPushforwardContinuous A J K).IsRightAdjoint]
    [HasColimitsOfSize.{w, w} A] :
    Nonempty ((q.comap u hu).sheafFiber (A := A) ≅ u.sheafPullback A J K ⋙ q.sheafFiber)
```

## Tag 05V2, a lemma

[Tag 05V2](https://stacks.math.columbia.edu/tag/05V2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.sheafFiber_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/DenseSubsite/NatIsoTransport.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/DenseSubsite/NatIsoTransport.lean#L116). The attribute's comment: “at a point of the site”.

> **[Stacks Project, Tag 05V2] at a point of the site.**  For a morphism of topoi `f` from
> `Sh(C, J)` to `Sh(D, K)` and a point `Φ` of the site `(C, J)`, the fibre at `Φ` of the inverse
> image of a sheaf `ℱ` on `(D, K)` is the stalk of `ℱ` at the composed point of `Sh(D, K)`.
>
> No bridge between the two notions of point has to be built: a point of a site already *is* a point
> of its topos, by `CategoryTheory.GrothendieckTopology.Point.pointOfTopos` (Stacks 00YA (1)), whose
> inverse image is the fibre functor on the nose
> (`CategoryTheory.GrothendieckTopology.Point.pointOfTopos_inverseImage`).  So
> `MorphismOfTopoi.stalk_inverseImage` applies verbatim, and this statement is it.

```lean
theorem sheafFiber_inverseImage {D : Type u'} [Category.{v'} D] {K : GrothendieckTopology D}
    (f : MorphismOfTopoi (Sheaf J (Type w)) (Sheaf K (Type w))) (F : Sheaf K (Type w)) :
    Φ.sheafFiber.obj (f.inverseImage.obj F) = (f.compPoint Φ.pointOfTopos).stalk F
```

**`MorphismOfTopoi.stalk_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ToposPoints.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/ToposPoints.lean#L47).

> For a morphism of topoi `f : Sh(D) → Sh(C)`, a point `q` of `Sh(D)` and a sheaf `F` on `C`,
> the stalk `(f⁻¹ F)_q` is the stalk `F_{f ∘ q}` at the composite point `f.compPoint q`.

```lean
theorem stalk_inverseImage (f : MorphismOfTopoi (Sheaf K (Type w)) (Sheaf J (Type w)))
    (q : PointOfTopos.{w, v', u'} K) (F : Sheaf J (Type w)) :
    q.stalk (f.inverseImage.obj F) = (f.compPoint q).stalk F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.34, Tag 05V0](https://stacks.math.columbia.edu/tag/05V0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
