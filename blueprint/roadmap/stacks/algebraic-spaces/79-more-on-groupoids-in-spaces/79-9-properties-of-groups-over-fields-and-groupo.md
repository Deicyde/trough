---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.GroupAlgebraicSpace, AlgebraicGeometry.GroupoidOverField, AlgebraicGeometry.Space.groupoidOfGroupOverField, AlgebraicGeometry.Space.isFlat_mul, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_comp_of_objects_eq_spec_field, AlgebraicGeometry.Space.isAbsolutelySeparated_groupAlgebraicSpace_of_isDecentSpace, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isAbsolutelySeparated_arrows_of_isDecentSpace, AlgebraicGeometry.Space.isSurjective_of_restrictionDiagramMap
statement: formalized
proof: formalized
---

# 79.9 Properties of groups over fields and groupoids on fields

Section 79.9 of the Stacks Project, [Tag 06DW](https://stacks.math.columbia.edu/tag/06DW). 12 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06DX, a situation

[Tag 06DX](https://stacks.math.columbia.edu/tag/06DX) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L101). The attribute's comment: “the situation: this notion at the base Spec k for a field k over S”.

> **Stacks Project, Tag 043H.** Group algebraic spaces over an algebraic space `B`.  An
> object is a group object in presheaves over `B` whose underlying presheaf is an algebraic
> space; morphisms are group-object morphisms over `B`.

```lean
noncomputable abbrev GroupAlgebraicSpace (𝒞 : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : 𝒞.Contains S) (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (_hB : IsAlgebraicSpace 𝒞 S hS B)
```

## Tag 06DY, a situation

[Tag 06DY](https://stacks.math.columbia.edu/tag/06DY) in the Stacks Project.

**`AlgebraicGeometry.GroupoidOverField`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidOverField.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidOverField.lean#L53). The attribute's comment: “groupoid in algebraic spaces over a field”.

> **Stacks 06DY.** A groupoid in algebraic spaces over an algebraic space `B` over a scheme
> `S`, whose space of objects is the spectrum of a field `k` regarded as an algebraic space over
> `S` through Yoneda.

```lean
structure GroupoidOverField (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
```

## Tag 06DZ, an equation

[Tag 06DZ](https://stacks.math.columbia.edu/tag/06DZ) in the Stacks Project.

**`AlgebraicGeometry.Space.groupoidOfGroupOverField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/GroupoidOfGroup.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/GroupoidOfGroup.lean#L185). The attribute's comment: “the groupoid `(Spec k, G, p, p, m)` over `Spec k` of a group over a field”.

> **Stacks 06DZ.** In the situation of Stacks 06DX — a scheme `S`, a field `k` over `S` and a
> group algebraic space `(G, m)` over `Spec k` — the quintuple `(Spec k, G, p, p, m)`, where
> `p : G ⟶ Spec k` is the structure morphism, is a groupoid in algebraic spaces over `Spec k`.
> Its five pieces are identified by `AlgebraicGeometry.Space.groupoidOfGroup_objects`,
> `groupoidOfGroup_arrows`, `groupoidOfGroup_source`, `groupoidOfGroup_target` and
> `groupoidOfGroup_comp`.

```lean
abbrev groupoidOfGroupOverField
    (G : GroupAlgebraicSpace C S hS (fieldSpace C hS hk structureMap).obj
      (fieldSpace C hS hk structureMap).property) :
    GroupoidInAlgebraicSpaces C S hS (fieldSpace C hS hk structureMap)
```

## Tag 06E0, a lemma

[Tag 06E0](https://stacks.math.columbia.edu/tag/06E0) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FlatMultiplication.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/FlatMultiplication.lean#L219). The attribute's comment: “second assertion: the group law of a group space over a field”. References: SGA 3 XVIII (2.2), “special case”.

> **Stacks 06E0**, second assertion. For a field `k` over the scheme `S`, the multiplication
> of a group algebraic space over `Spec k` is flat and universally open.
>
> The first assertion of the same tag, for the composition of a groupoid in algebraic spaces whose
> object space is the spectrum of a field, is
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_comp_of_objects_eq_spec_field`.

```lean
theorem isFlat_mul {k : Type u} [Field k] (C : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : C.Contains S) (structureMap : Spec (.of k) ⟶ S) (hk : C.Contains (Spec (.of k)))
    (G : GroupAlgebraicSpace C S hS
      (schemeSpace (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS))).obj
      (schemeSpace (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS))).property) :
    IsFlat C S hS μ[G.obj.X].left ∧ UniversallyOpen C S hS μ[G.obj.X].left
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_comp_of_objects_eq_spec_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FlatComposition.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FlatComposition.lean#L184). The attribute's comment: “first assertion: the composition of a groupoid over a field”.

> **Stacks 06E0**, first assertion. Composition in a groupoid in algebraic spaces whose
> object space is the spectrum of a field is flat and universally open.

```lean
theorem isFlat_comp_of_objects_eq_spec_field {k : Type u} [Field k]
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (structureMap : Spec (.of k) ⟶ S) (hk : C.Contains (Spec (.of k)))
    (B : AlgebraicSpaces C S hS) (G : GroupoidInAlgebraicSpaces C S hS B)
    (objects_eq : G.objects =
      schemeSpace (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS))) :
    Space.IsFlat C S hS G.comp.hom ∧ Space.UniversallyOpen C S hS G.comp.hom
```

## Tag 08BH, a lemma

[Tag 08BH](https://stacks.math.columbia.edu/tag/08BH) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelySeparated_groupAlgebraicSpace_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/DecentSeparated.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/DecentSeparated.lean#L348). The attribute's comment: “a decent group algebraic space over a field”.

> **Stacks 08BH.** A decent group algebraic space over the spectrum of a field is a separated
> algebraic space.
>
> By Stacks 06P6 separatedness of the structure morphism is the identity section being a closed
> immersion, and the identity section is a section of the structure morphism, hence a closed
> immersion because the space is decent. The base is separated because the spectrum of a field is
> affine, so Stacks 04ZH part (1) upgrades separatedness of the structure morphism to
> separatedness of the group space.

```lean
theorem isAbsolutelySeparated_groupAlgebraicSpace_of_isDecentSpace (k : Type u) [Field k]
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (structureMap : Spec (.of k) ⟶ S) (hk : C.Contains (Spec (.of k)))
    (hZ : C.Contains (⊤_ Scheme.{u}))
    (G : GroupAlgebraicSpace C S hS
      (yoneda.obj (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS)))
      (isAlgebraicSpace_yoneda C S hS
        (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS))))
    (hG : IsDecentSpace C S hS G.obj.X.left) :
    IsAbsolutelySeparated C S hS hZ G.obj.X.left
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isAbsolutelySeparated_arrows_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/DecentSeparated.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/DecentSeparated.lean#L514). The attribute's comment: “the arrows of a decent groupoid on a field”.

> **Stacks 08BH.** The arrow space of a groupoid in algebraic spaces whose object space is
> the algebraic space of the spectrum of a field and whose arrow space is decent is a separated
> algebraic space.
>
> The unit of the groupoid is a section of the source morphism, hence a closed immersion because
> the arrow space is decent; the target morphism is then separated, and the object space is
> separated because the spectrum of a field is affine, so Stacks 04ZH part (1) applies.

```lean
theorem isAbsolutelySeparated_arrows_of_isDecentSpace (k : Type u) [Field k]
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (structureMap : Spec (.of k) ⟶ S) (hk : C.Contains (Spec (.of k)))
    (hZ : C.Contains (⊤_ Scheme.{u})) (B : AlgebraicSpaces C S hS)
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (hU : G.objects.obj =
      yoneda.obj (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS)))
    (hR : Space.IsDecentSpace C S hS G.arrows.obj) :
    Space.IsAbsolutelySeparated C S hS hZ G.arrows.obj
```

## Tag 06E1, a lemma

[Tag 06E1](https://stacks.math.columbia.edu/tag/06E1) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_of_restrictionDiagramMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean#L531). The attribute's comment: “surjective”.

> **Stacks 06E1.** Every arrow of the diagram defining the restriction of a groupoid in
> algebraic spaces whose object space is the spectrum of a field, over a field extension, is
> surjective.

```lean
theorem isSurjective_of_restrictionDiagramMap
    {X Y : AlgebraicSpaces C S hS} (f : X ⟶ Y)
    (hf : RestrictionDiagramMap C hS hk hk' structureMap i G hU f) :
    IsSurjective C S hS f.hom
```

**`AlgebraicGeometry.Space.isFlat_of_restrictionDiagramMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean#L545). The attribute's comment: “flat”.

> **Stacks 06E1.** Every arrow of the diagram defining the restriction of a groupoid in
> algebraic spaces whose object space is the spectrum of a field, over a field extension, is
> flat.

```lean
theorem isFlat_of_restrictionDiagramMap
    {X Y : AlgebraicSpaces C S hS} (f : X ⟶ Y)
    (hf : RestrictionDiagramMap C hS hk hk' structureMap i G hU f) :
    IsFlat C S hS f.hom
```

**`AlgebraicGeometry.Space.universallyOpen_of_restrictionDiagramMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean#L561). The attribute's comment: “universally open”.

> **Stacks 06E1.** Every arrow of the diagram defining the restriction of a groupoid in
> algebraic spaces whose object space is the spectrum of a field, over a field extension, is
> universally open.

```lean
theorem universallyOpen_of_restrictionDiagramMap
    {X Y : AlgebraicSpaces C S hS} (f : X ⟶ Y)
    (hf : RestrictionDiagramMap C hS hk hk' structureMap i G hU f) :
    UniversallyOpen C S hS f.hom
```

**`AlgebraicGeometry.Space.isAffineHom_restrictionArrowsToArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionFieldExtension.lean#L577). The attribute's comment: “affine dotted arrow”.

> **Stacks 06E1.** The canonical map from the arrows of the restriction of a groupoid in
> algebraic spaces over a field extension to the arrows of the groupoid is affine.

```lean
theorem isAffineHom_restrictionArrowsToArrows :
    IsAffineHom C S hS
      (restrictionArrowsToArrows G
        (restrictionObjectMap C hS hk hk' structureMap i G hU)).hom
```

## Tag 06E2, a lemma

[Tag 06E2](https://stacks.math.columbia.edu/tag/06E2) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.exists_isIso_source_target_over_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/GeometricArrows.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/GeometricArrows.lean#L337).

> **Stacks 06E2.** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `B` whose
> object space `U` is the algebraic space represented by the spectrum of a field `k`. Every
> point `r` of the arrow space `R` has, after an algebraically closed field extension `k'/k`,
> a representative `r'` in the arrow space of the restriction `(U', R', s', t', c')` of the
> groupoid along `Spec k' ⟶ Spec k`: it maps to `r` in the points of `R`, and both its source
> `s' ∘ r'` and its target `t' ∘ r'` are automorphisms of `Spec k'`.

```lean
theorem exists_isIso_source_target_over_isAlgClosed {k : Type u} [Field k]
    (C : BigFppfSite.{u}) {S : Scheme.{u}} (hS : C.Contains S)
    (structureMap : Spec (CommRingCat.of k) ⟶ S)
    (hk : C.Contains (Spec (CommRingCat.of k))) (B : AlgebraicSpaces C S hS)
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (objects_eq : G.objects = schemeSpace
      (Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS)))
    (r : Space.points C S hS G.arrows.obj) :
    ∃ (k' : Type u) (field' : Field k') (_ : IsAlgClosed k')
      (i : k →+* k') (hk' : C.Contains (Spec (CommRingCat.of k'))),
      let T : BigFppfOver C S hS :=
        Over.mk (⟨structureMap⟩ : C.obj hk ⟶ C.obj hS)
      let T' : BigFppfOver C S hS :=
        Over.mk (⟨Scheme.Spec.map (CommRingCat.ofHom i).op ≫ structureMap⟩ :
          C.obj hk' ⟶ C.obj hS)
      let g : schemeSpace T' ⟶ G.objects :=
        schemeSpaceMap
          (Over.homMk (⟨Scheme.Spec.map (CommRingCat.ofHom i).op⟩ :
            C.obj hk' ⟶ C.obj hk) rfl : T' ⟶ T) ≫
          eqToHom objects_eq.symm
      ∃ r' : (restrictionArrows G g).obj.obj (Opposite.op T'),
        let p : Space.FieldValuedPoint C S hS G.arrows.obj :=
          { carrier := k'
            field := field'
            contained := hk'
            toBase := Scheme.Spec.map (CommRingCat.ofHom i).op ≫ structureMap
            value := (restrictionArrowsToArrows G g).hom.app (Opposite.op T') r' }
        let sourceEnd : T' ⟶ T' := (restrictionSource G g).hom.app (Opposite.op T') r'
        let targetEnd : T' ⟶ T' := (restrictionTarget G g).hom.app (Opposite.op T') r'
        p.class C S hS G.arrows.obj = r ∧ IsIso sourceEnd ∧ IsIso targetEnd
```

## Tag 06E3, a lemma

[Tag 06E3](https://stacks.math.columbia.edu/tag/06E3) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.translationByArrow_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Translation.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Translation.lean#L256). The attribute's comment: “the automorphism”.

> **Stacks 06E3.** Translation by a family of arrows whose source and target are both
> isomorphisms of the object space is an automorphism of the arrow space.

```lean
theorem translationByArrow_isIso (G : GroupoidInAlgebraicSpaces C S hS B)
    (r : G.objects ⟶ G.arrows) [IsIso (r ≫ G.source)] [IsIso (r ≫ G.target)] :
    IsIso (translationByArrow G r)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.translationByArrow_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Translation.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Translation.lean#L288). The attribute's comment: “image of the identity”.

> **Stacks 06E3.** Translation by `r` takes the identity arrow at the source of `r` to `r`
> itself.

```lean
theorem translationByArrow_identity (G : GroupoidInAlgebraicSpaces C S hS B)
    (r : G.objects ⟶ G.arrows) [IsIso (r ≫ G.source)]
    (T : (BigFppfOver C S hS)ᵒᵖ) (x : G.toGroupoidInFunctors.Evaluation T) :
    (translationByArrow G r).hom.app T
      (G.toGroupoidInFunctors.identity T ((r ≫ G.source).hom.app T x)) = r.hom.app T x
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.identityArrow_comp_translationByArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/UnibranchIdentityArrow.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/UnibranchIdentityArrow.lean#L117). The attribute's comment: “image of the identity, as an equation of morphisms”.

> **Stacks 06E3, as an equation of morphisms.**  Left translation by a family `r` of arrows
> whose source is an isomorphism, precomposed with the identity arrow at the source of `r`, is `r`
> itself.

```lean
theorem identityArrow_comp_translationByArrow (H : GroupoidInAlgebraicSpaces C S hS B)
    (r : H.objects ⟶ H.arrows) [IsIso (r ≫ H.source)] :
    ((r ≫ H.source) ≫ identityArrow H) ≫ translationByArrow H r = r
```

## Tag 06E4, a lemma

[Tag 06E4](https://stacks.math.columbia.edu/tag/06E4) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isGeometricallyUnibranch_arrows_of_splitAtIds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean#L103). The attribute's comment: “groupoid case, for a groupoid whose object space is the spectrum of a field”.

> **Stacks 06E4, the groupoid case.**  The arrow space of a groupoid in algebraic spaces whose
> object space is the spectrum of a field is geometrically unibranch.
>
> The last step of the source proof is [Stacks Project, Tag 06DU] for the étale local rings
> `𝒪_{R, e}` and `𝒪_{R ×_{s, U, t} R, (e, e)}` of each restriction of the groupoid along an
> algebraically closed extension of the field; it is
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.minimalPrimesSplitAtIdentityArrow_restriction`.

```lean
theorem isGeometricallyUnibranch_arrows_of_splitAtIds :
    Space.IsGeometricallyUnibranch C S hS G.arrows.obj
```

**`AlgebraicGeometry.GroupoidOverField.isGeometricallyUnibranch_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean#L129). The attribute's comment: “groupoid case, in the situation 06DY”.

> **Stacks 06E4, the groupoid case.**  In the situation of [Stacks Project, Tag 06DY] — a
> groupoid in algebraic spaces `(U, R, s, t, c)` whose object space `U` is the spectrum of a field
> `k` — the arrow space `R` is geometrically unibranch.

```lean
theorem isGeometricallyUnibranch_arrows (G : GroupoidOverField C S hS B) :
    Space.IsGeometricallyUnibranch C S hS G.arrows.obj
```

**`AlgebraicGeometry.Space.isGeometricallyUnibranch_groupAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GroupoidArrowsUnibranch.lean#L200). The attribute's comment: “group case, in the situation 06DX”.

> **Stacks 06E4, the group case.**  A group algebraic space over a field is geometrically
> unibranch.
>
> A group `G` over `Spec k` is the arrow space of a groupoid in algebraic spaces whose object space
> is `Spec k`: the group acts trivially on the base, and the arrow space of the resulting action
> groupoid is `G ×_{Spec k} Spec k`, which the first projection identifies with `G`.

```lean
theorem isGeometricallyUnibranch_groupAlgebraicSpace :
    IsGeometricallyUnibranch C (Spec (.of k)) hk G.obj.X.left
```

## Tag 06FD, a lemma

[Tag 06FD](https://stacks.math.columbia.edu/tag/06FD) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_eq_dimensionAtPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean#L355). The attribute's comment: “constant dimension of the arrow space”.

> **Stacks 06FD.** Let `G` be a groupoid in algebraic spaces over `S` whose space of objects
> is the spectrum of a field `k`, viewed as an algebraic space through Yoneda, and whose source
> and target are locally of finite type. Then the dimension of the space of arrows of `G` equals
> its dimension at every one of its points.

```lean
theorem dimension_eq_dimensionAtPoint
    {k : Type u} [Field k] (hk : B.Contains (Spec (.of k)))
    (structureMap : Spec (.of k) ⟶ S)
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (objects_eq : G.objects = _root_.AlgebraicGeometry.schemeSpace
      (Over.mk (⟨structureMap⟩ : B.obj hk ⟶ B.obj hS)))
    (_hs : IsLocallyOfFiniteType B S hS G.source.hom)
    (ht : IsLocallyOfFiniteType B S hS G.target.hom)
    (r : points B S hS G.arrows.obj) :
    dimension B S hS G.arrows.obj G.arrows.property =
      dimensionAtPoint B S hS G.arrows.obj G.arrows.property r
```

**`AlgebraicGeometry.Space.hasTranscendenceDegreeAt_source_iff_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean#L444). The attribute's comment: “part (2): the transcendence degree through the source and through the target”.

> **Stacks 06FD, part (2).** Let `G` be a groupoid in algebraic spaces over `S` whose space
> of objects is the spectrum of a field `k`, viewed as an algebraic space through Yoneda, and
> whose source and target are locally of finite type. Then the transcendence degree over `k` of a
> point of the space of arrows is the same whether it is measured through the source or through
> the target.
>
> Both are read on one étale chart of the arrow space whose chart of the object space is the
> field spectrum itself, where they become the two transcendence degrees of the residue field at
> a point of a scheme over two morphisms to the spectrum of a field.

```lean
theorem hasTranscendenceDegreeAt_source_iff_target
    {k : Type u} [Field k] (hk : B.Contains (Spec (.of k)))
    (structureMap : Spec (.of k) ⟶ S)
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (objects_eq : G.objects = _root_.AlgebraicGeometry.schemeSpace
      (Over.mk (⟨structureMap⟩ : B.obj hk ⟶ B.obj hS)))
    (hs : IsLocallyOfFiniteType B S hS G.source.hom)
    (ht : IsLocallyOfFiniteType B S hS G.target.hom)
    (r : points B S hS G.arrows.obj) (n : ℕ∞) :
    HasTranscendenceDegreeAt B S hS G.source.hom r n ↔
      HasTranscendenceDegreeAt B S hS G.target.hom r n
```

**`AlgebraicGeometry.Space.dimension_eq_localRingDimension_of_hasTranscendenceDegreeAt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/ConstantDimensionOverField.lean#L535). The attribute's comment: “part (3): the dimension of the local ring at a point of transcendence degree 0”.

> **Stacks 06FD, part (3).** Let `G` be a groupoid in algebraic spaces over `S` whose space of
> objects is the spectrum of a field `k`, viewed as an algebraic space through Yoneda, and whose
> source and target are locally of finite type. At a point of the space of arrows whose
> transcendence degree over `k` is zero, the dimension of the space of arrows is the dimension of
> the local ring there.

```lean
theorem dimension_eq_localRingDimension_of_hasTranscendenceDegreeAt_zero
    {k : Type u} [Field k] (hk : B.Contains (Spec (.of k)))
    (structureMap : Spec (.of k) ⟶ S)
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (objects_eq : G.objects = _root_.AlgebraicGeometry.schemeSpace
      (Over.mk (⟨structureMap⟩ : B.obj hk ⟶ B.obj hS)))
    (hs : IsLocallyOfFiniteType B S hS G.source.hom)
    (ht : IsLocallyOfFiniteType B S hS G.target.hom)
    (r : points B S hS G.arrows.obj)
    (htr : HasTranscendenceDegreeAt B S hS G.source.hom r 0) :
    dimension B S hS G.arrows.obj G.arrows.property =
      (localRingDimension B S hS r : WithBot ℕ∞)
```

## Tag 06FE, a lemma

[Tag 06FE](https://stacks.math.columbia.edu/tag/06FE) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_eq_dimensionAtPoint_of_groupAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantDimension.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantDimension.lean#L163). The attribute's comment: “part (1): dimension at every point”.

> **Stacks 06FE, part (1).** A group algebraic space over a field which is locally of finite
> type has the same dimension at every one of its points, namely its dimension.
>
> Constant dimension of the arrow space of a groupoid in algebraic spaces whose object space is
> the spectrum of a field is `AlgebraicGeometry.Space.dimension_eq_dimensionAtPoint`.

```lean
theorem dimension_eq_dimensionAtPoint_of_groupAlgebraicSpace {k : Type u} [Field k]
    (C : BigFppfSite.{u}) (hk : C.Contains (Spec (.of k)))
    (G : GroupAlgebraicSpace C (Spec (.of k)) hk (terminalSpace C (Spec (.of k)) hk).obj
      (terminalSpace C (Spec (.of k)) hk).property)
    (hG : IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (g : points C (Spec (.of k)) hk G.obj.X.left) :
    dimension C (Spec (.of k)) hk G.obj.X.left G.property =
      dimensionAtPoint C (Spec (.of k)) hk G.obj.X.left G.property g
```

**`AlgebraicGeometry.Space.dimension_eq_localRingDimension_of_groupAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantDimension.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ConstantDimension.lean#L214). The attribute's comment: “part (2): dimension of the local ring at a point of transcendence degree zero”.

> **Stacks 06FE, part (2).** At a point of a group algebraic space locally of finite type over
> a field whose transcendence degree over that field is zero, the dimension of the group is the
> dimension of the local ring.

```lean
theorem dimension_eq_localRingDimension_of_groupAlgebraicSpace {k : Type u} [Field k]
    (C : BigFppfSite.{u}) (hk : C.Contains (Spec (.of k)))
    (G : GroupAlgebraicSpace C (Spec (.of k)) hk (terminalSpace C (Spec (.of k)) hk).obj
      (terminalSpace C (Spec (.of k)) hk).property)
    (hG : IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom)
    (g : points C (Spec (.of k)) hk G.obj.X.left)
    (htr : HasTranscendenceDegreeAt C (Spec (.of k)) hk G.obj.X.hom g 0) :
    dimension C (Spec (.of k)) hk G.obj.X.left G.property =
      (localRingDimension C (Spec (.of k)) hk g : WithBot ℕ∞)
```

## Tag 06FF, a lemma

[Tag 06FF](https://stacks.math.columbia.edu/tag/06FF) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_arrows_eq_dimension_stabilizer_of_objects_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/StabilizerDimensionObjectsIso.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/StabilizerDimensionObjectsIso.lean#L57). The attribute's comment: “with the space of objects isomorphic to the spectrum of the field”.

> **Stacks 06FF.** Let `G` be a groupoid in algebraic spaces over `S` whose space of objects
> is the spectrum of a field `k`, viewed as an algebraic space through Yoneda, and whose source
> and target are locally of finite type. Then the space of arrows of `G` and the stabilizer of `G`
> have the same dimension.
>
> The hypothesis is an *isomorphism* of the object space with the spectrum of the field, not an
> equality of algebraic spaces; the equality case is
> `AlgebraicGeometry.Space.dimension_arrows_eq_dimension_stabilizer`.

```lean
theorem dimension_arrows_eq_dimension_stabilizer_of_objects_iso {k : Type u} [Field k]
    (hk : B.Contains (Spec (.of k))) (structureMap : Spec (.of k) ⟶ S)
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (objects_iso : G.objects ≅ _root_.AlgebraicGeometry.schemeSpace
      (Over.mk (⟨structureMap⟩ : B.obj hk ⟶ B.obj hS)))
    (hs : IsLocallyOfFiniteType B S hS G.source.hom)
    (ht : IsLocallyOfFiniteType B S hS G.target.hom) :
    dimension B S hS G.arrows.obj G.arrows.property =
      dimension B S hS (GroupoidInAlgebraicSpaces.stabilizerOverBase G).obj
        (GroupoidInAlgebraicSpaces.stabilizerOverBase G).property
```

**`AlgebraicGeometry.Space.dimension_arrows_eq_dimension_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/StabilizerDimensionOverField.lean, line 666](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/StabilizerDimensionOverField.lean#L666).

> Let `G` be a groupoid in algebraic spaces over `S` whose space of objects
> is the spectrum of a field `k`, viewed as an algebraic space through Yoneda, and whose source
> and target are locally of finite type. Then the space of arrows of `G` and the stabilizer of `G`
> have the same dimension.

```lean
theorem dimension_arrows_eq_dimension_stabilizer {k : Type u} [Field k]
    (hk : B.Contains (Spec (.of k))) (structureMap : Spec (.of k) ⟶ S)
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (objects_eq : G.objects = _root_.AlgebraicGeometry.schemeSpace
      (Over.mk (⟨structureMap⟩ : B.obj hk ⟶ B.obj hS)))
    (hs : IsLocallyOfFiniteType B S hS G.source.hom)
    (ht : IsLocallyOfFiniteType B S hS G.target.hom) :
    dimension B S hS G.arrows.obj G.arrows.property =
      dimension B S hS (GroupoidInAlgebraicSpaces.stabilizerOverBase G).obj
        (GroupoidInAlgebraicSpaces.stabilizerOverBase G).property
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.9, Tag 06DW](https://stacks.math.columbia.edu/tag/06DW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
