---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.iso_of_mono_of_point_eq, AlgebraicGeometry.Space.IsDecentSpace.hasMonomorphicFieldRepresentative, AlgebraicGeometry.Space.residueFieldRepresentative, AlgebraicGeometry.Space.residueField, AlgebraicGeometry.Space.residueFieldRepresentative_unique, AlgebraicGeometry.Space.isIso_residueFieldHom_iff_mono, AlgebraicGeometry.Space.exists_affine_elementaryEtaleNeighborhood', AlgebraicGeometry.Space.ElementaryEtaleNeighborhood
statement: formalized
proof: formalized
---

# 68.11 Residue fields and henselian local rings

Section 68.11 of the Stacks Project, [Tag 0EMV](https://stacks.math.columbia.edu/tag/0EMV). 11 tags here are carried by 36 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03K4, a lemma

[Tag 03K4](https://stacks.math.columbia.edu/tag/03K4) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.iso_of_mono_of_point_eq`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/MonomorphismPoints.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L56) (StacksFrontier): “injectivity”.
- [`AlgebraicGeometry.Space.IsDecentSpace.hasMonomorphicFieldRepresentative`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean#L121), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L57) (StacksFrontier): “surjectivity”.

## Tag 0EMW, a definition

[Tag 0EMW](https://stacks.math.columbia.edu/tag/0EMW) in the Stacks Project.

**`AlgebraicGeometry.Space.residueFieldRepresentative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L68). The attribute's comment: “field-valued monomorphism”.

> The chosen field-valued representative of a point of a decent algebraic space whose morphism
> to the space is a monomorphism.

```lean
noncomputable def residueFieldRepresentative (hDecent : IsDecentSpace B S hS X)
    (x : points B S hS X) :
    {p : FieldValuedPoint B S hS X //
      p.class B S hS X = x ∧ Mono (fieldMorphism B S hS X p)}
```

**`AlgebraicGeometry.Space.residueField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L78). The attribute's comment: “residue field”.

> The residue field of a decent algebraic space at a point: the field of the monomorphism from
> a field spectrum representing that point.

```lean
noncomputable abbrev residueField (hDecent : IsDecentSpace B S hS X)
    (x : points B S hS X) : Type u
```

**`AlgebraicGeometry.Space.residueFieldRepresentative_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L92). The attribute's comment: “uniqueness”.

> A monomorphic field-valued representative of a point of a decent algebraic space is uniquely
> isomorphic, over the space, to the chosen one: the residue field is unique up to unique
> isomorphism.

```lean
theorem residueFieldRepresentative_unique (hX : IsAlgebraicSpace B S hS X)
    (hDecent : IsDecentSpace B S hS X) (x : points B S hS X)
    (q : FieldValuedPoint B S hS X) (hq : q.class B S hS X = x)
    (hmq : Mono (fieldMorphism B S hS X q)) :
    ∃! e : yoneda.obj ((residueFieldRepresentative B S hS X hDecent x).1.siteObject B S hS X) ≅
        yoneda.obj (q.siteObject B S hS X),
      e.hom ≫ fieldMorphism B S hS X q = residueFieldMorphism B S hS X hDecent x
```

## Tag 0EMX, a lemma

[Tag 0EMX](https://stacks.math.columbia.edu/tag/0EMX) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_residueFieldHom_iff_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidueField.lean#L194).

> A morphism of decent algebraic spaces induces an isomorphism of residue fields at a point
> exactly when the morphism from the spectrum of the residue field at that point to the target
> space is a monomorphism.

```lean
theorem isIso_residueFieldHom_iff_mono (hY : IsAlgebraicSpace B S hS Y)
    (hDecentX : IsDecentSpace B S hS X) (hDecentY : IsDecentSpace B S hS Y)
    (f : X ⟶ Y) (x : points B S hS X) :
    IsIso (CommRingCat.ofHom (residueFieldHom B S hS X Y hY hDecentX hDecentY f x)) ↔
      Mono (residueFieldMorphism B S hS X hDecentX x ≫ f)
```

## Tag 0BBP, a lemma

[Tag 0BBP](https://stacks.math.columbia.edu/tag/0BBP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_elementaryEtaleNeighborhood'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/AffineElementaryEtaleNeighborhood.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/AffineElementaryEtaleNeighborhood.lean#L612).

> **Stacks 0BBP.** Every point `x` of a decent algebraic space `X` over `S` has an elementary
> étale neighborhood whose scheme is affine, whose distinguished point is the only point above
> `x`, and whose residue field at that point is the residue field of `X` at `x` through the
> induced homomorphism.

```lean
theorem exists_affine_elementaryEtaleNeighborhood'
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hDecent : IsDecentSpace B S hS X) (x : points B S hS X) :
    ∃ E : ElementaryEtaleNeighborhood B S hS X hX x,
      IsAffine E.scheme.left.1 ∧
      (∀ y : points B S hS (yoneda.obj E.scheme),
        pointsMap B S hS (yoneda.obj E.scheme) E.toSpace y = x →
          y = presheafPoint B S hS E.scheme E.point E.residueField_contained) ∧
      ∃ φ : residueField B S hS X hDecent x →+* E.scheme.left.1.residueField E.point,
        Function.Bijective φ ∧
          ∃ g : residueFieldObject B S hS E.scheme E.point E.residueField_contained ⟶
              (residueFieldRepresentative B S hS X hDecent x).1.siteObject B S hS X,
            B.inclusion.map g.left = Spec.map (CommRingCat.ofHom φ) ∧
              yoneda.map g ≫ residueFieldMorphism B S hS X hDecent x =
                yoneda.map (residueFieldMap B S hS E.scheme E.point
                  E.residueField_contained) ≫ E.toSpace
```

## Tag 0BGU, a definition

[Tag 0BGU](https://stacks.math.columbia.edu/tag/0BGU) in the Stacks Project.

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhood.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhood.lean#L131). The attribute's comment: “elementary étale neighborhoods”.

> **Stacks 0BGU, elementary étale neighborhoods.** A scheme étale over an
> algebraic space, pointed above `x`, for which the residue-field point is a
> monomorphism into the space.

```lean
structure ElementaryEtaleNeighborhood (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F)
```

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhood.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhood.lean#L158). The attribute's comment: “morphisms of elementary étale neighborhoods”.

> **Stacks 0BGU, morphisms.** A map of elementary étale neighborhoods is
> a map over the algebraic space carrying the chosen point to the chosen point.

```lean
structure Hom (V W : ElementaryEtaleNeighborhood B S hS F hF x)
```

## Tag 0BGV, a lemma

[Tag 0BGV](https://stacks.math.columbia.edu/tag/0BGV) in the Stacks Project.

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood.exists_affine_cone_objs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/AffineRefinementOfNeighborhood.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/AffineRefinementOfNeighborhood.lean#L57). The attribute's comment: “two neighbourhoods are refined by a common one whose scheme is affine”.

> Any two elementary étale neighborhoods of a point of an algebraic space are refined by a
> common elementary étale neighborhood whose scheme is affine.

```lean
theorem exists_affine_cone_objs (U V : ElementaryEtaleNeighborhood B S hS X hX x) :
    ∃ (W : ElementaryEtaleNeighborhood B S hS X hX x) (_ : W ⟶ U) (_ : W ⟶ V),
      IsAffine W.scheme.left.1
```

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood.exists_cone_objs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean#L439). The attribute's comment: “common refinements: any two elementary étale neighbourhoods admit a third mapping to both”.

> **Stacks 0BGV, common refinements.** Two elementary étale neighborhoods of `x` admit a
> common refinement.

```lean
theorem exists_cone_objs (V W : ElementaryEtaleNeighborhood B S hS X hX x) :
    ∃ (E : ElementaryEtaleNeighborhood B S hS X hX x) (_ : E ⟶ V) (_ : E ⟶ W), True
```

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood.exists_cone_maps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean, line 541](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean#L541). The attribute's comment: “equalizing refinements: any two parallel morphisms are equalized by a refinement”.

> **Stacks 0BGV, equalizing refinements.** Two morphisms of elementary étale neighborhoods of
> `x` are equalized by a refinement of their source.

```lean
theorem exists_cone_maps {V W : ElementaryEtaleNeighborhood B S hS X hX x} (f g : V ⟶ W) :
    ∃ (E : ElementaryEtaleNeighborhood B S hS X hX x) (h : E ⟶ V), h ≫ f = h ≫ g
```

**`AlgebraicGeometry.Space.ElementaryEtaleNeighborhood.isCofilteredOrEmpty`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean, line 553](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodCofiltered.lean#L553). The attribute's comment: “the category is cofiltered or empty; unconditional”.

> **Stacks 0BGV.** The category of elementary étale neighborhoods of a point of an algebraic
> space is cofiltered as soon as it is nonempty: any two neighborhoods are refined by a third,
> and any two parallel morphisms are equalized by a refinement.

```lean
instance isCofilteredOrEmpty : IsCofilteredOrEmpty (ElementaryEtaleNeighborhood B S hS X hX x)
```

**`AlgebraicGeometry.Space.isCofiltered_elementaryEtaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean#L76). The attribute's comment: “the category of elementary étale neighbourhoods of a point of a decent space is cofiltered; nonemptiness by Tag 0BBP”.

> The category of elementary étale neighborhoods of a point of a decent algebraic space is
> cofiltered.

```lean
theorem isCofiltered_elementaryEtaleNeighborhood :
    IsCofiltered (ElementaryEtaleNeighborhood B S hS X hX x)
```

## Tag 0BGW, a definition

[Tag 0BGW](https://stacks.math.columbia.edu/tag/0BGW) in the Stacks Project.

**`AlgebraicGeometry.Space.henselianLocalRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean#L164). The attribute's comment: “the henselian local ring at a point”.

> The henselian local ring of a decent algebraic space at a point: the
> colimit of the rings of global sections over the elementary étale neighborhoods of the
> point.

```lean
abbrev henselianLocalRing (_hDecent : IsDecentSpace B S hS X) : CommRingCat.{u + 1}
```

**`AlgebraicGeometry.Space.sectionHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean#L170). The attribute's comment: “canonical section homomorphisms”.

> The canonical ring homomorphism from the global sections of an
> elementary étale neighborhood into the henselian local ring.

```lean
def sectionHom (hDecent : IsDecentSpace B S hS X)
    (U : (ElementaryEtaleNeighborhood B S hS X hX x)ᵒᵖ) :
    (globalSections B S hS X hX x).obj U →+* henselianLocalRing B S hS X hX x hDecent
```

**`AlgebraicGeometry.Space.sectionHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean#L179). The attribute's comment: “naturality of section homomorphisms”.

> Restricting a section to a finer elementary étale neighborhood does not
> change its canonical image in the henselian local ring.

```lean
theorem sectionHom_naturality (hDecent : IsDecentSpace B S hS X)
    {U V : (ElementaryEtaleNeighborhood B S hS X hX x)ᵒᵖ} (f : U ⟶ V)
    (s : (globalSections B S hS X hX x).obj U) :
    sectionHom B S hS X hX x hDecent V ((globalSections B S hS X hX x).map f s) =
      sectionHom B S hS X hX x hDecent U s
```

**`AlgebraicGeometry.Space.existsUnique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRing.lean#L191). The attribute's comment: “colimit universal property”.

> A family of ring homomorphisms out of the global sections of the
> elementary étale neighborhoods of a point, compatible with restriction, factors uniquely
> through the henselian local ring.

```lean
theorem existsUnique_lift (hDecent : IsDecentSpace B S hS X) (R : Type v) [CommRing R]
    (φ : ∀ U : (ElementaryEtaleNeighborhood B S hS X hX x)ᵒᵖ,
      (globalSections B S hS X hX x).obj U →+* R)
    (hφ : ∀ {U V} (f : U ⟶ V) (s : (globalSections B S hS X hX x).obj U),
      φ V ((globalSections B S hS X hX x).map f s) = φ U s) :
    ∃! ψ : henselianLocalRing B S hS X hX x hDecent →+* R,
      ∀ U s, ψ (sectionHom B S hS X hX x hDecent U s) = φ U s
```

## Tag 0EMY, a lemma

[Tag 0EMY](https://stacks.math.columbia.edu/tag/0EMY) in the Stacks Project.

**`AlgebraicGeometry.Space.stalkToHenselianLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L603). The attribute's comment: “the canonical map from the stalk of an elementary étale neighbourhood”.

> **Stacks 0EMY.** The canonical homomorphism from the local ring of an elementary étale
> neighborhood at its distinguished point into the henselian local ring of the algebraic space.

```lean
def stalkToHenselianLocalRing (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x) :
    U.scheme.left.1.presheaf.stalk U.point →+*
      (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
```

**`AlgebraicGeometry.Space.stalkToHenselianLocalRing_openGerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L623). The attribute's comment: “the canonical map on germs over a pointed open”.

> **Stacks 0EMY.** The canonical homomorphism sends the germ of a section over a pointed open
> subscheme to the canonical image of that section in the henselian local ring.

```lean
theorem stalkToHenselianLocalRing_openGerm (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x)
    (W : U.scheme.left.1.Opens) (hW : U.point ∈ W)
    (s : U.scheme.left.1.presheaf.obj (op W)) :
    stalkToHenselianLocalRing B S hS X hX x hDecent U
        (U.scheme.left.1.presheaf.germ W U.point hW s) =
      openRestrictionSectionHom B S hS X hX x hDecent U W hW s
```

**`AlgebraicGeometry.Space.stalkToHenselianLocalRing_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 687](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L687). The attribute's comment: “naturality of the canonical map in the neighbourhood”.

> **Stacks 0EMY.** The canonical homomorphisms out of the local rings of the elementary étale
> neighborhoods are compatible with every morphism of neighborhoods.

```lean
theorem stalkToHenselianLocalRing_naturality (hDecent : IsDecentSpace B S hS X)
    {V U : ElementaryEtaleNeighborhood B S hS X hX x} (f : V ⟶ U) :
    (stalkToHenselianLocalRing B S hS X hX x hDecent V).comp
        (neighborhoodStalkMap B S hS X hX x f).hom =
      stalkToHenselianLocalRing B S hS X hX x hDecent U
```

**`AlgebraicGeometry.Space.henselianLocalRing_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L740). The attribute's comment: “O^h is a local ring”.

> **Stacks 0EMY.** The henselian local ring of a decent algebraic space at a point is a local
> ring.

```lean
theorem henselianLocalRing_isLocalRing (hDecent : IsDecentSpace B S hS X) :
    IsLocalRing (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
```

**`AlgebraicGeometry.Space.henselianLocalRing_isHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 1088](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L1088). The attribute's comment: “O^h is a henselization of the stalk”. References: SGA 3 X (4.4), “Case 2°”.

> **Stacks 0EMY.** The henselian local ring of a decent algebraic space at a point is a
> henselization of the local ring of any elementary étale neighborhood at its distinguished
> point.

```lean
theorem henselianLocalRing_isHenselization (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x) :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    letI := stalkAlgebra B S hS X hX x hDecent U
    IsLocalRing.IsHenselization (U.scheme.left.1.presheaf.stalk U.point)
      (IsLocalRing.ResidueField (U.scheme.left.1.presheaf.stalk U.point))
      (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
```

**`AlgebraicGeometry.Space.map_maximalIdeal_stalkToHenselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 1147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L1147). The attribute's comment: “the maximal ideal of O^h”.

> **Stacks 0EMY.** The maximal ideal of the henselian local ring is generated by the image of
> the maximal ideal of the local ring of any elementary étale neighborhood.

```lean
theorem map_maximalIdeal_stalkToHenselianLocalRing (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x) :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    (IsLocalRing.maximalIdeal (U.scheme.left.1.presheaf.stalk U.point)).map
        (stalkToHenselianLocalRing B S hS X hX x hDecent U) =
      IsLocalRing.maximalIdeal (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
```

**`AlgebraicGeometry.Space.exists_residueFieldEquiv_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean, line 1163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingStalk.lean#L1163). The attribute's comment: “the residue field of O^h”.

> **Stacks 0EMY.** The residue field of the henselian local ring is the residue field of the
> local ring of any elementary étale neighborhood at its distinguished point.

```lean
theorem exists_residueFieldEquiv_henselianLocalRing (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x) :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    ∃ e : IsLocalRing.ResidueField (U.scheme.left.1.presheaf.stalk U.point) ≃+*
        IsLocalRing.ResidueField
          (henselianLocalRing B S hS X hX x hDecent : Type (u + 1)),
      ∀ r : U.scheme.left.1.presheaf.stalk U.point,
        e (IsLocalRing.residue _ r) =
          IsLocalRing.residue _ (stalkToHenselianLocalRing B S hS X hX x hDecent U r)
```

**`AlgebraicGeometry.Space.PrimeDivisor.neighborhoodSectionsToGenericHenselianLocalRing_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldChartIndependence.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldChartIndependence.lean#L101). The attribute's comment: “naturality in the neighbourhood of the map from global sections into the henselian local ring”.

> **Stacks 0EMY.** The map from the global sections of an elementary étale neighbourhood of
> the generic point of a prime divisor into the henselian local ring there is compatible with
> every morphism of neighbourhoods.

```lean
theorem PrimeDivisor.neighborhoodSectionsToGenericHenselianLocalRing_naturality
    {V U : ElementaryEtaleNeighborhood B S hS X hX (Z.genericPoint B S hS X)} (f : V ⟶ U)
    (a : Γ(U.scheme.left.1, ⊤)) :
    Z.neighborhoodSectionsToGenericHenselianLocalRing B S hS hX hdec V (f.hom.left.1.appTop a) =
      Z.neighborhoodSectionsToGenericHenselianLocalRing B S hS hX hdec U a
```

**`AlgebraicGeometry.Space.isLocalRing_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean#L83). The attribute's comment: “O^h is a local ring for a decent space”.

> The henselian local ring of a decent algebraic space at a point is a local ring.

```lean
theorem isLocalRing_henselianLocalRing :
    IsLocalRing (henselianLocalRing B S hS X hX x hXdec : Type (u + 1))
```

## Tag 0EMZ, a lemma

[Tag 0EMZ](https://stacks.math.columbia.edu/tag/0EMZ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isHenselization_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingStrictHenselization.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingStrictHenselization.lean#L81). The attribute's comment: “the étale local ring at a geometric point is a strict henselization of the henselian local ring at the point below it, for a chosen separable closure κsep of the residue field. The algebra structures are produced, not assumed; the structure map is pinned by lying over the neighborhood stalk, of which the étale local ring is also a strict henselization”.

> **Stacks 0EMZ.** The étale local ring of a decent algebraic space at a geometric point is a
> strict henselization of the henselian local ring of the space at the point it lies over.

```lean
theorem exists_isHenselization_etaleLocalRing (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x)
    (xbar : GeometricPoint B S hS X) (hxbar : xbar.LiesOver x)
    (κsep : Type u) [Field κsep]
    [Algebra (ResidueField (U.scheme.left.1.presheaf.stalk U.point : Type u)) κsep]
    [IsSepClosure (ResidueField (U.scheme.left.1.presheaf.stalk U.point : Type u)) κsep] :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    letI := isLocalRing_etaleLocalRing B S hS X hX xbar
    ∃ (algU : Algebra (U.scheme.left.1.presheaf.stalk U.point : Type u)
        (etaleLocalRing B S hS X xbar : Type (u + 1)))
      (alg : Algebra (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
        (etaleLocalRing B S hS X xbar : Type (u + 1)))
      (algRes : Algebra (ResidueField
        (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))) κsep),
      (@algebraMap (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))
            (etaleLocalRing B S hS X xbar : Type (u + 1)) _ _ alg).comp
          (stalkToHenselianLocalRing B S hS X hX x hDecent U) =
        @algebraMap (U.scheme.left.1.presheaf.stalk U.point : Type u)
          (etaleLocalRing B S hS X xbar : Type (u + 1)) _ _ algU ∧
      @IsHenselization (U.scheme.left.1.presheaf.stalk U.point : Type u) _ _ κsep _ _
        (etaleLocalRing B S hS X xbar : Type (u + 1)) _ _ algU ∧
      @IsHenselization (henselianLocalRing B S hS X hX x hDecent : Type (u + 1)) _ _
        κsep _ algRes (etaleLocalRing B S hS X xbar : Type (u + 1)) _ _ alg
```

## Tag 0EN0, a lemma

[Tag 0EN0](https://stacks.math.columbia.edu/tag/0EN0) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.genericResidueFieldEquivHenselian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean#L284). The attribute's comment: “the residue field of the henselian local ring at the generic point of a prime divisor is the residue field of the chosen chart, canonically through the henselization map”.

> **The canonical isomorphism `κ(u) ≃+* κ(𝒪^h_{X, ξ})`** induced by the henselization map
> `𝒪_{U, u} → 𝒪^h_{X, ξ}`.

```lean
def PrimeDivisor.genericResidueFieldEquivHenselian :
    letI := henselianLocalRing_isLocalRing B S hS X hX (Z.genericPoint B S hS X) hdec
    Z.genericResidueField B S hS hX hdec ≃+*
      IsLocalRing.ResidueField ↥(Z.genericHenselianLocalRing B S hS hX hdec)
```

**`AlgebraicGeometry.Space.exists_residueFieldEquiv_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingResidueField.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingResidueField.lean#L205). The attribute's comment: “the residue field of the henselian local ring is the residue field of the space. Both fields are determined only up to canonical isomorphism, so the identification is existential, pinned by the isomorphism `eκ` of the neighborhood residue field with the residue field of the space lying over the space (the morphism `g`) and by compatibility with the canonical homomorphism out of the neighborhood stalk. No hypothesis is carried: cofilteredness of the elementary étale neighborhoods comes from Stacks 0BGV, nonemptiness from the given neighborhood”.

> The residue field of the henselian local ring of a decent algebraic space at a point is the
> residue field of the space at that point, through an isomorphism compatible with the canonical
> homomorphism out of the stalk of a given elementary étale neighborhood.

```lean
theorem exists_residueFieldEquiv_residueField (hDecent : IsDecentSpace B S hS X)
    (U : ElementaryEtaleNeighborhood B S hS X hX x) :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    ∃ (eκ : (neighborhoodFieldPoint B S hS X hX x U).carrier ≃+*
        residueField B S hS X hDecent x)
      (g : (residueFieldRepresentative B S hS X hDecent x).1.siteObject B S hS X ⟶
        (neighborhoodFieldPoint B S hS X hX x U).siteObject B S hS X)
      (e : residueField B S hS X hDecent x ≃+*
        IsLocalRing.ResidueField (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))),
      fieldValuedPointHom B S hS X _ _ g = eκ.toRingHom ∧
        yoneda.map g ≫ fieldMorphism B S hS X (neighborhoodFieldPoint B S hS X hX x U) =
          residueFieldMorphism B S hS X hDecent x ∧
        ∀ r : U.scheme.left.1.presheaf.stalk U.point,
          e (eκ (IsLocalRing.residue _ r)) =
            IsLocalRing.residue _ (stalkToHenselianLocalRing B S hS X hX x hDecent U r)
```

**`AlgebraicGeometry.Space.existsUnique_residueFieldEquiv_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingResidueField.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/HenselianLocalRingResidueField.lean#L237). The attribute's comment: “the residue field of the henselian local ring is the residue field of the space, by the canonical isomorphism: the unique one compatible, for every elementary étale neighborhood, with the canonical homomorphism out of its stalk and the homomorphism of residue fields over the space. No neighborhood is assumed; one exists by Stacks 0BBP”.

> The residue field of the henselian local ring of a decent algebraic space at a point is the
> residue field of the space at that point: there is exactly one isomorphism
> between them compatible with every elementary étale neighborhood of the point, namely the one
> carrying the class of the image of a germ `r` of the neighborhood to the value at `r` of the
> homomorphism of residue fields lying over the space.

```lean
theorem existsUnique_residueFieldEquiv_residueField (hDecent : IsDecentSpace B S hS X) :
    letI := henselianLocalRing_isLocalRing B S hS X hX x hDecent
    ∃! e : IsLocalRing.ResidueField
        (henselianLocalRing B S hS X hX x hDecent : Type (u + 1)) ≃+*
          residueField B S hS X hDecent x,
      ∀ (U : ElementaryEtaleNeighborhood B S hS X hX x)
        (g : (residueFieldRepresentative B S hS X hDecent x).1.siteObject B S hS X ⟶
          (neighborhoodFieldPoint B S hS X hX x U).siteObject B S hS X),
        yoneda.map g ≫ fieldMorphism B S hS X (neighborhoodFieldPoint B S hS X hX x U) =
            residueFieldMorphism B S hS X hDecent x →
        ∀ r : U.scheme.left.1.presheaf.stalk U.point,
          e (IsLocalRing.residue _ (stalkToHenselianLocalRing B S hS X hX x hDecent U r)) =
            fieldValuedPointHom B S hS X (residueFieldRepresentative B S hS X hDecent x).1
              (neighborhoodFieldPoint B S hS X hX x U) g (IsLocalRing.residue _ r)
```

## Tag 0EPL, a remark

[Tag 0EPL](https://stacks.math.columbia.edu/tag/0EPL) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_point_over_elementaryEtaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean#L50). The attribute's comment: “the unique point above the two distinguished points”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `X` decent, let `x` be a point
> of `X` and let `V` be an elementary étale neighborhood of the image of `x`. The fibre product
> `V ×_Y X` has exactly one point lying above the distinguished point of `V` and above `x`.

```lean
theorem existsUnique_point_over_elementaryEtaleNeighborhood
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hX : IsDecentSpace B S hS X.1)
    (x : points B S hS X.1)
    (V : ElementaryEtaleNeighborhood B S hS Y.1 Y.property
      (pointsMap B S hS X.1 f.hom x)) :
    ∃! x' : points B S hS (pullback V.toSpace f.hom),
      pointsMap B S hS (pullback V.toSpace f.hom) (pullback.fst V.toSpace f.hom) x' =
          presheafPoint B S hS V.scheme V.point V.residueField_contained ∧
        pointsMap B S hS (pullback V.toSpace f.hom) (pullback.snd V.toSpace f.hom) x' = x
```

**`AlgebraicGeometry.Space.yoneda_map_neighborhoodOver_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L108). The attribute's comment: “the square of charts over f”.

> **Stacks 0EPL.** The two charts form a commutative square over `f`: the chart of the upper
> elementary étale neighborhood maps to the chart of the lower one compatibly with `f`.

```lean
theorem yoneda_map_neighborhoodOver_comp :
    yoneda.map (neighborhoodOver B S hS f V U) ≫ V.toSpace =
      neighborhoodToSource B S hS f V U ≫ f.hom
```

**`AlgebraicGeometry.Space.neighborhoodOver_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L117). The attribute's comment: “the morphism of charts is pointed”.

> **Stacks 0EPL.** The morphism of chart schemes carries the distinguished point of the upper
> elementary étale neighborhood to that of the lower one.

```lean
theorem neighborhoodOver_point
    (hx' : pointsMap B S hS (pullback V.toSpace f.hom) (pullback.fst V.toSpace f.hom) x' =
      presheafPoint B S hS V.scheme V.point V.residueField_contained) :
    (BigFppfOver.toScheme B S hS).map (neighborhoodOver B S hS f V U) U.point = V.point
```

**`AlgebraicGeometry.Space.neighborhoodOverSource`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L178). The attribute's comment: “the upper neighborhood is one of the source”.

> **Stacks 0EPL.** An elementary étale neighborhood of a point `x'` of `V ×_Y X` lying over
> the distinguished point of `V` and over `x` is an elementary étale neighborhood of `x` in `X`.
>
> This is what makes the identifications of the remark available at `(U, u)`: Stacks 0EMY and
> Properties of Spaces, Lemma 04KF both ask for an elementary étale neighborhood of the point of
> the space whose local rings are being computed.

```lean
def neighborhoodOverSource
    (hfst : pointsMap B S hS (pullback V.toSpace f.hom) (pullback.fst V.toSpace f.hom) x' =
      presheafPoint B S hS V.scheme V.point V.residueField_contained)
    (hsnd : pointsMap B S hS (pullback V.toSpace f.hom) (pullback.snd V.toSpace f.hom) x' = x) :
    ElementaryEtaleNeighborhood B S hS X.1 X.property x
```

**`AlgebraicGeometry.Space.exists_henselianLocalRingMap_of_neighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L310). The attribute's comment: “the square of henselian local rings”.

> **Stacks 0EPL.** Let `(U, u)` be an elementary étale neighborhood of a point `x` of a decent
> algebraic space `X`, let `(W, w)` be one of a point `y` of a decent algebraic space `Y` and let
> `j : U ⟶ W` be a morphism of the chart schemes carrying `u` to `w`. Then there is a local
> homomorphism `𝒪^h_{Y, y} ⟶ 𝒪^h_{X, x}` over the map `𝒪_{W, w} ⟶ 𝒪_{U, u}` of neighborhood
> stalks.

```lean
theorem exists_henselianLocalRingMap_of_neighborhood
    (j : U.scheme ⟶ W.scheme) (hj : j.left.1 U.point = W.point) :
    letI := isLocalRing_henselianLocalRing B S hS hX hXdec x
    letI := isLocalRing_henselianLocalRing B S hS hY hYdec y
    ∃ φ : (henselianLocalRing B S hS Y hY y hYdec : Type (u + 1)) →+*
        (henselianLocalRing B S hS X hX x hXdec : Type (u + 1)),
      IsLocalHom φ ∧
      φ.comp (stalkToHenselianLocalRing B S hS Y hY y hYdec W) =
        (stalkToHenselianLocalRing B S hS X hX x hXdec U).comp
          ((W.scheme.left.1.presheaf.stalkCongr (Inseparable.of_eq hj.symm)).hom ≫
            j.left.1.stalkMap U.point).hom
```

**`AlgebraicGeometry.Space.exists_diagram_of_neighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L376). The attribute's comment: “the commutative diagram, as a diagram of ring homomorphisms”.

> **Stacks 0EPL, the commutative diagram.** For a pointed morphism `k : (N, n) ⟶ (M, m)` of
> elementary étale neighborhoods over `g : X ⟶ Y`, the rows
>
> `𝒪_{M, m} ⟶ 𝒪^h_{Y, y} ⟶ 𝒪_{Y, w̄}`  and  `𝒪_{N, n} ⟶ 𝒪^h_{X, z} ⟶ 𝒪_{X, z̄}`
>
> are joined by local homomorphisms making both squares commute, over the map `𝒪_{M, m} ⟶ 𝒪_{N, n}`
> of neighborhood stalks; and the étale and henselian local rings of the two spaces are the strict
> henselization and the henselization of the respective neighborhood stalks.

```lean
theorem exists_diagram_of_neighborhood (hzbar : zbar.LiesOver z)
    (hwbar : wbar.LiesOver (pointsMap B S hS Xs.1 g.hom z)) :
    letI := isLocalRing_henselianLocalRing B S hS Xs.property hXd z
    letI := isLocalRing_henselianLocalRing B S hS Ys.property hYd
      (pointsMap B S hS Xs.1 g.hom z)
    letI := isLocalRing_etaleLocalRing B S hS Xs.1 Xs.property zbar
    letI := isLocalRing_etaleLocalRing B S hS Ys.1 Ys.property wbar
    ∃ (algN : Algebra (N.scheme.left.1.presheaf.stalk N.point : Type u)
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)))
      (algM : Algebra (M.scheme.left.1.presheaf.stalk M.point : Type u)
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)))
      (algHX : Algebra (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)))
      (algHY : Algebra (henselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)))
      (φ : (henselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1)) →+*
          (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1)))
      (ψ : (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) →+*
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1))),
      IsLocalHom φ ∧ IsLocalHom ψ ∧
      φ.comp (stalkToHenselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd M) =
          (stalkToHenselianLocalRing B S hS Xs.1 Xs.property z hXd N).comp
            ((M.scheme.left.1.presheaf.stalkCongr (Inseparable.of_eq hk.symm)).hom ≫
              k.left.1.stalkMap N.point).hom ∧
      (@algebraMap (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
            (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algHX).comp
          (stalkToHenselianLocalRing B S hS Xs.1 Xs.property z hXd N) =
        @algebraMap (N.scheme.left.1.presheaf.stalk N.point : Type u)
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algN ∧
      (@algebraMap (henselianLocalRing B S hS Ys.1 Ys.property
              (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
            (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algHY).comp
          (stalkToHenselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd M) =
        @algebraMap (M.scheme.left.1.presheaf.stalk M.point : Type u)
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algM ∧
      ψ.comp (@algebraMap (henselianLocalRing B S hS Ys.1 Ys.property
              (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
            (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algHY) =
        (@algebraMap (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
            (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algHX).comp φ ∧
      @IsHenselization (N.scheme.left.1.presheaf.stalk N.point : Type u) _ _ κN _ _
        (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algN ∧
      @IsHenselization (M.scheme.left.1.presheaf.stalk M.point : Type u) _ _ κM _ _
        (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algM
```

**`AlgebraicGeometry.Space.exists_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodDiagram.lean#L511). The attribute's comment: “the remark, with both choices made”.

> **Stacks 0EPL.** Let `g : X ⟶ Y` be a morphism of decent algebraic spaces over `S`, let `z`
> be a point of `X` with image `y` in `Y`, and let `z̄` and `w̄` be geometric points of `X` and of
> `Y` lying over `z` and over `y`. Then there are an elementary étale neighborhood `(M, m)` of
> `y`, an elementary étale neighborhood `(N, n)` of `z` and a morphism `k : N ⟶ M` of chart
> schemes over `g` carrying `n` to `m`, for which the two rows
>
> `𝒪_{M, m} ⟶ 𝒪^h_{Y, y} ⟶ 𝒪_{Y, w̄}`  and  `𝒪_{N, n} ⟶ 𝒪^h_{X, z} ⟶ 𝒪_{X, z̄}`
>
> are joined by local homomorphisms making both squares commute, the étale local rings being
> strict henselizations and the henselian local rings henselizations of the two neighborhood
> stalks.
>
> Both choices of the remark are made here: `(M, m)` by Stacks 0BBP, and `(N, n)` together with
> `k` by base change of `(M, m)` along `g`, which runs through the fibre product `M ×_Y X` and
> chooses an elementary étale neighborhood of the point of it above `m` and `z`.

```lean
theorem exists_diagram (hzbar : zbar.LiesOver z)
    (hwbar : wbar.LiesOver (pointsMap B S hS Xs.1 g.hom z)) :
    letI := isLocalRing_henselianLocalRing B S hS Xs.property hXd z
    letI := isLocalRing_henselianLocalRing B S hS Ys.property hYd
      (pointsMap B S hS Xs.1 g.hom z)
    letI := isLocalRing_etaleLocalRing B S hS Xs.1 Xs.property zbar
    letI := isLocalRing_etaleLocalRing B S hS Ys.1 Ys.property wbar
    ∃ (M₀ : ElementaryEtaleNeighborhood B S hS Ys.1 Ys.property
          (pointsMap B S hS Xs.1 g.hom z))
      (N₀ : ElementaryEtaleNeighborhood B S hS Xs.1 Xs.property z)
      (k₀ : N₀.scheme ⟶ M₀.scheme) (hk₀ : k₀.left.1 N₀.point = M₀.point)
      (algN : Algebra (N₀.scheme.left.1.presheaf.stalk N₀.point : Type u)
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)))
      (algM : Algebra (M₀.scheme.left.1.presheaf.stalk M₀.point : Type u)
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)))
      (algHX : Algebra (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)))
      (algHY : Algebra (henselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)))
      (φ : (henselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1)) →+*
          (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1)))
      (ψ : (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) →+*
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1))),
      yoneda.map k₀ ≫ M₀.toSpace = N₀.toSpace ≫ g.hom ∧
      IsLocalHom φ ∧ IsLocalHom ψ ∧
      φ.comp (stalkToHenselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd M₀) =
          (stalkToHenselianLocalRing B S hS Xs.1 Xs.property z hXd N₀).comp
            ((M₀.scheme.left.1.presheaf.stalkCongr (Inseparable.of_eq hk₀.symm)).hom ≫
              k₀.left.1.stalkMap N₀.point).hom ∧
      (@algebraMap (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
            (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algHX).comp
          (stalkToHenselianLocalRing B S hS Xs.1 Xs.property z hXd N₀) =
        @algebraMap (N₀.scheme.left.1.presheaf.stalk N₀.point : Type u)
          (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algN ∧
      (@algebraMap (henselianLocalRing B S hS Ys.1 Ys.property
              (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
            (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algHY).comp
          (stalkToHenselianLocalRing B S hS Ys.1 Ys.property
            (pointsMap B S hS Xs.1 g.hom z) hYd M₀) =
        @algebraMap (M₀.scheme.left.1.presheaf.stalk M₀.point : Type u)
          (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algM ∧
      ψ.comp (@algebraMap (henselianLocalRing B S hS Ys.1 Ys.property
              (pointsMap B S hS Xs.1 g.hom z) hYd : Type (u + 1))
            (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algHY) =
        (@algebraMap (henselianLocalRing B S hS Xs.1 Xs.property z hXd : Type (u + 1))
            (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algHX).comp φ ∧
      @IsHenselization (N₀.scheme.left.1.presheaf.stalk N₀.point : Type u) _ _ (SeparableClosure
          (ResidueField (N₀.scheme.left.1.presheaf.stalk N₀.point : Type u))) _ _
        (etaleLocalRing B S hS Xs.1 zbar : Type (u + 1)) _ _ algN ∧
      @IsHenselization (M₀.scheme.left.1.presheaf.stalk M₀.point : Type u) _ _ (SeparableClosure
          (ResidueField (M₀.scheme.left.1.presheaf.stalk M₀.point : Type u))) _ _
        (etaleLocalRing B S hS Ys.1 wbar : Type (u + 1)) _ _ algM
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAlgebraicSpace_pullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L350), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean#L41) (StacksFrontier): “the fibre product is an algebraic space”.
- [`AlgebraicGeometry.Space.isEtale_of_isPullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L254), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ElementaryEtaleNeighborhoodBaseChange.lean#L43) (StacksFrontier): “the projection to the source is étale”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.11, Tag 0EMV](https://stacks.math.columbia.edu/tag/0EMV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
