---
declaration: section
origin: cited
lean: CategoryTheory.Stalk.presheafPushforward_stalk_iso, Stacks.Sheaves.StalkInverseImage.stalkAddEquiv, Stacks.Sheaves.StalkInverseImage.stalkAddEquiv_smul, Stacks.Sheaves.StalkInverseImage.stalkNatIso, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv_smul, Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkNatIso, CategoryTheory.Functor.IsMorphismOfSites.exists_point_fiber_eq_and_sheafFiber_iso
statement: formalized
proof: formalized
---

# 7.34 Points and morphisms of topoi

Section 7.34 of the Stacks Project, [Tag 05V0](https://stacks.math.columbia.edu/tag/05V0). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F4F, a lemma

[Tag 0F4F](https://stacks.math.columbia.edu/tag/0F4F) in the Stacks Project.

**`CategoryTheory.Stalk.presheafPushforward_stalk_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkPresheafPushforward.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkPresheafPushforward.lean#L73).

> **Stacks 0F4F**, packaged as the existence of the natural isomorphism
> `(u_p F)_v ≅ F_{v ∘ u}`.

```lean
theorem presheafPushforward_stalk_iso (u : C ⥤ D) (v : D ⥤ Type u) :
    Nonempty (u.op.lan ⋙ presheafStalk v ≅ presheafStalk (u ⋙ v))
```

## Tag 05V1, a lemma

[Tag 05V1](https://stacks.math.columbia.edu/tag/05V1) in the Stacks Project.

**`Stacks.Sheaves.StalkInverseImage.stalkAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L496). The attribute's comment: “for sheaves of modules, at a point of a site, for a morphism of topoi whose stalk functor at the target point is the inverse image followed by the stalk functor at the source point”.

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

**`Stacks.Sheaves.StalkInverseImage.stalkAddEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L526). The attribute's comment: “semilinearity of the comparison, for sheaves of modules”.

> The isomorphism of stalk modules is semilinear over the isomorphism of stalk rings: the
> stalk at `Φ` of the inverse image of `G` is the stalk of `G` at `Ψ`, with the scalars carried
> along `O_Ψ ≅ (g⁻¹O)_Φ`.

```lean
theorem stalkAddEquiv_smul (r : (Ψ.presheafFiber (A := RingCat.{w})).obj O.obj)
    (m : (Stacks.sheafModuleFiber Ψ O).obj G) :
    stalkAddEquiv g O Φ Ψ e G (r • m) =
      stalkRingEquiv g O Φ Ψ e r • stalkAddEquiv g O Φ Ψ e G m
```

**`Stacks.Sheaves.StalkInverseImage.stalkNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkInverseImageModules.lean#L600). The attribute's comment: “for sheaves of modules, as a natural isomorphism of stalk functors”.

> The stalk functor at `Ψ` is the inverse image of sheaves of modules followed by the stalk
> functor at `Φ` and restriction of scalars along the isomorphism of stalk rings.

```lean
def stalkNatIso :
    Stacks.sheafModuleFiber Ψ O ≅
      inverseImageModules g O ⋙ Stacks.sheafModuleFiber Φ (inverseImageRingSheaf g O) ⋙
        ModuleCat.restrictScalars (stalkRingEquiv g O Φ Ψ e).toRingHom
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L106). The attribute's comment: “for sheaves of modules, at the point of the target site attached to a point of the source site by part (2) of Stacks 00YA”.

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

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkAddEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L123). The attribute's comment: “semilinearity, at the point of the target site attached to a point of the source site”.

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

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.targetStalkNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkOfInverseImageAtTheTargetPoint.lean#L163). The attribute's comment: “for sheaves of modules, as a natural isomorphism of stalk functors, at the point of the target site attached to a point of the source site”.

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

**`CategoryTheory.Functor.IsMorphismOfSites.exists_point_fiber_eq_and_sheafFiber_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfMorphismOfSites.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OfMorphismOfSites.lean#L143). The attribute's comment: “Stated for the morphisms of sites of Stacks 00X1 (`Functor.IsMorphismOfSites`), with no flatness or cover-preservation assumption on `u`; the canonical point is `IsMorphismOfSites.comapPoint` and the canonical identification of stalk functors is `IsMorphismOfSites.sheafFiberComapPointIso`.”.

> **Stacks 05V1.** Let `f : D → C` be a morphism of sites given by the continuous functor
> `u : C ⥤ D` (Stacks 00X1: `u_s` is exact) and let `q` be a point of `D` with fiber functor
> `v = q.fiber`. Then `v ∘ u = u ⋙ q.fiber` is the fiber functor of a point `p` of `C`, and
> there is an identification `(f⁻¹ F)_q ≅ F_p`, natural in the sheaf of sets `F` on `C`.
>
> The point is `hu.comapPoint q` and the identification is `hu.sheafFiberComapPointIso q`.

```lean
theorem exists_point_fiber_eq_and_sheafFiber_iso :
    haveI := hu.isContinuous
    ∃ p : Point.{u} J, p.fiber = u ⋙ q.fiber ∧
      Nonempty (p.sheafFiber (A := Type u) ≅
        u.sheafPullback (Type u) J K ⋙ q.sheafFiber (A := Type u))
```

## Tag 05V2, a lemma

[Tag 05V2](https://stacks.math.columbia.edu/tag/05V2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.sheafFiber_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/DenseSubsite/NatIsoTransport.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/DenseSubsite/NatIsoTransport.lean#L116). The attribute's comment: “at a point of the site”.

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

**`MorphismOfTopoi.stalk_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ToposPoints.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ToposPoints.lean#L47).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
