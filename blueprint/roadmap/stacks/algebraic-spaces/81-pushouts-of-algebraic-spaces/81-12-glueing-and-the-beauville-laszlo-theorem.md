---
declaration: section
origin: cited
lean: BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces, AlgebraicGeometry.Space.exists_etaleCovering_iff_isGlueable, BeauvilleLaszlo.Space.isAffineSpace_components, BeauvilleLaszlo.Space.canonicalAffineGlueableRestriction_isEquivalence, BeauvilleLaszlo.Space.beauvilleLaszloAffineEquivalence, BeauvilleLaszlo.Space.essSurj_affineGlueableRestriction, BeauvilleLaszlo.Space.isFinite_iff_canonicalAffineGlueableRestriction_map, BeauvilleLaszlo.Space.isFinite_affineGlueingEquivalence_inverse_map_iff
statement: formalized
proof: formalized
---

# 81.12 Glueing and the Beauville-Laszlo theorem

Section 81.12 of the Stacks Project, [Tag 0F9M](https://stacks.math.columbia.edu/tag/0F9M). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F9N, an equation

[Tag 0F9N](https://stacks.math.columbia.edu/tag/0F9N) in the Stacks Project.

**`BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueing.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueing.lean#L303).

> The canonical functor from spaces over `X` to cartesian gluing triples, including its natural
> comparison with all three base changes and the two induced arrows.

```lean
noncomputable def beauvilleLaszloGlueingSpaces
    (B : BigFppfSite.{u})
    (U' U X' X : Scheme.{u}) (hU' : B.Contains U')
    (hU : B.Contains U) (hX' : B.Contains X') (hX : B.Contains X)
    (gU : B.obj hU' ⟶ B.obj hU)
    (gX' : B.obj hU' ⟶ B.obj hX')
    (jU : B.obj hU ⟶ B.obj hX)
    (jX' : B.obj hX' ⟶ B.obj hX)
    (hcomm : gU ≫ jU = gX' ≫ jX') :
    GlueingFunctorSpec B U' U X' X hU' hU hX' hX gU gX' jU jX' hcomm
```

## Tag 0F9P, a lemma

[Tag 0F9P](https://stacks.math.columbia.edu/tag/0F9P) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etaleCovering_iff_isGlueable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/BeauvilleLaszlo.lean, line 800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/BeauvilleLaszlo.lean#L800).

> Glueability of an algebraic space can be checked on all affine schemes
> étale over it, or on one étale covering by affine schemes.

```lean
theorem exists_etaleCovering_iff_isGlueable
  {R : Type u} {R' : Type v} [CommRing R] [CommRing R']
  (g : R →+* R') (f : R)
  (_hglue : BeauvilleLaszlo.IsGlueingPair g f)
  (B : BigFppfSite.{u})
  (hX : B.Contains (Spec (.of R)))
  (Y : _root_.AlgebraicGeometry.AlgebraicSpaces B (Spec (.of R)) hX) :
  (∃ (I : Type (u + 1))
      (W : I → BigFppfOver B (Spec (.of R)) hX)
      (p : ∀ i, yoneda.obj (W i) ⟶ Y.1),
      IsEtaleCovering B (Spec (.of R)) hX
        (fun i ↦ yoneda.obj (W i)) p ∧
        ∀ i, IsAffine ((BigFppfOver.toScheme B (Spec (.of R)) hX).obj (W i)) ∧
          IsGlueableGlobalSections g f B hX (W i)) ↔
    IsGlueableAlgebraicSpace g f B hX Y
```

## Tag 0F9Q, a lemma

[Tag 0F9Q](https://stacks.math.columbia.edu/tag/0F9Q) in the Stacks Project.

**`BeauvilleLaszlo.Space.isAffineSpace_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffine.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffine.lean#L110). The attribute's comment: “the functor restricts to the affine subcategories”.

> **The gluing functor of Stacks 0F9N takes affine algebraic spaces to triples with affine
> components.** All four schemes of the square are assumed affine, as they are in the
> Beauville--Laszlo situation, where they are the spectra of `R`, `R_f`, `R'` and `R'_f`.

```lean
theorem isAffineSpace_components
    (B : BigFppfSite.{u})
    (U' U X' X : Scheme.{u}) (hU' : B.Contains U')
    (hU : B.Contains U) (hX' : B.Contains X') (hX : B.Contains X)
    [IsAffine U'] [IsAffine U] [IsAffine X'] [IsAffine X]
    (gU : B.obj hU' ⟶ B.obj hU)
    (gX' : B.obj hU' ⟶ B.obj hX')
    (jU : B.obj hU ⟶ B.obj hX)
    (jX' : B.obj hX' ⟶ B.obj hX)
    (hcomm : gU ≫ jU = gX' ≫ jX')
    (G : GlueingFunctorSpec B U' U X' X hU' hU hX' hX gU gX' jU jX' hcomm)
    (Y : AlgebraicSpaces B X hX)
    (hY : AlgebraicGeometry.Space.IsAffineSpace B X hX Y.1) :
    affineComponents B U' U X' hU' hU hX' gU gX' (G.functor.obj Y)
```

**`BeauvilleLaszlo.Space.canonicalAffineGlueableRestriction_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineCanonicalEquivalence.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineCanonicalEquivalence.lean#L63).

> **Stacks 0F9Q.** For a Beauville--Laszlo glueing pair `(g : R → R', f)`, the glueing functor
> of Stacks 0F9N restricts to an **equivalence** between the category of affine algebraic spaces
> over `X = Spec R` which are glueable for `(g, f)` and the full subcategory of those glueing
> triples `(V, V', Y')` over `U ← U' → X'` whose three components are affine.
>
> The functor in question is `BeauvilleLaszlo.Space.canonicalAffineGlueableRestriction`, which is by
> definition the restriction of `BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces`, the glueing
> functor of Stacks 0F9N, to those two full subcategories.

```lean
theorem canonicalAffineGlueableRestriction_isEquivalence {R R' : Type u} [CommRing R] [CommRing R']
    (g : R →+* R') (f : R) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) :
    (canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).IsEquivalence
```

**`BeauvilleLaszlo.Space.beauvilleLaszloAffineEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineEquivalence.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineEquivalence.lean#L1015).

> **Stacks 0F9Q.** The glueing functor of Stacks 0F9N restricts to an equivalence between the
> affine algebraic spaces over `X = Spec R` which are glueable for the pair `(R → R', f)` and the
> cartesian glueing triples `(V, V', Y')` over `U ← U' → X'` whose three components are affine —
> together with the identification of the forward functor of that equivalence with the restriction
> of the glueing functor itself, which is what the statement of the tag asserts.
>
> Faithfulness is Stacks 0F9S, fullness is
> `BeauvilleLaszlo.Space.full_comp_glueingFunctor` and essential surjectivity is
> `BeauvilleLaszlo.Space.essSurj_affineGlueableRestriction`; the equivalence is the one Mathlib
> builds out of the three, so its forward functor *is* the restricted glueing functor and the
> identification is `BeauvilleLaszlo.Space.affineGlueableRestrictionCompIso`.

```lean
noncomputable def beauvilleLaszloAffineEquivalence (f : R)
    (hpair : _root_.BeauvilleLaszlo.IsGlueingPair (algebraMap R R') f)
    (B : BigFppfSite.{u}) (hX : B.Contains (Spec (.of R)))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R')))
    (hU' : B.Contains (Spec (.of (Localization.Away ((algebraMap R R') f))))) :
    AffineGlueingEquivalenceSpec (algebraMap R R') f B
      (Spec (.of (Localization.Away ((algebraMap R R') f))))
      (Spec (.of (Localization.Away f))) (Spec (.of R')) hU' hU hX' hX
      (AlgebraicGeometry.Space.specSite B hU hU').hom
      (AlgebraicGeometry.Space.specSite B hX' hU').hom
      (beauvilleLaszloGlueingSpaces B (Spec (.of (Localization.Away ((algebraMap R R') f))))
        (Spec (.of (Localization.Away f))) (Spec (.of R')) (Spec (.of R)) hU' hU hX' hX
        (AlgebraicGeometry.Space.specSite B hU hU').hom
        (AlgebraicGeometry.Space.specSite B hX' hU').hom
        (AlgebraicGeometry.Space.specSite B hX hU).hom
        (AlgebraicGeometry.Space.specSite B hX hX').hom
        (specSite_square_comm f B hU' hU hX' hX)).functor
```

**`BeauvilleLaszlo.Space.essSurj_affineGlueableRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineEssSurj.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingAffineEssSurj.lean#L276). The attribute's comment: “the restricted functor is essentially surjective”.

> **Stacks 0F9Q, the essential surjectivity clause.** The restriction of a glueing functor of
> Stacks 0F9N to the affine algebraic spaces over `Spec R` which are glueable for the pair is
> essentially surjective onto the cartesian glueing triples with affine components.

```lean
theorem essSurj_affineGlueableRestriction {R R' : Type u} [CommRing R] [CommRing R']
    [Algebra R R'] (f : R)
    (hpair : _root_.BeauvilleLaszlo.IsGlueingPair (algebraMap R R') f)
    (B : BigFppfSite.{u})
    (hX : B.Contains (Spec (.of R)))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R')))
    (hU' : B.Contains (Spec (.of (Localization.Away ((algebraMap R R') f)))))
    (hcomm : (AlgebraicGeometry.Space.specSite B hU hU').hom ≫
          (AlgebraicGeometry.Space.specSite B hX hU).hom =
        (AlgebraicGeometry.Space.specSite B hX' hU').hom ≫
          (AlgebraicGeometry.Space.specSite B hX hX').hom)
    (G : GlueingFunctorSpec B (Spec (.of (Localization.Away ((algebraMap R R') f))))
      (Spec (.of (Localization.Away f))) (Spec (.of R')) (Spec (.of R)) hU' hU hX' hX
      (AlgebraicGeometry.Space.specSite B hU hU').hom
      (AlgebraicGeometry.Space.specSite B hX' hU').hom
      (AlgebraicGeometry.Space.specSite B hX hU).hom
      (AlgebraicGeometry.Space.specSite B hX hX').hom hcomm) :
    (affineGlueableRestriction (g := algebraMap R R') (f := f) G).EssSurj
```

## Tag 0F9R, a lemma

[Tag 0F9R](https://stacks.math.columbia.edu/tag/0F9R) in the Stacks Project.

**`BeauvilleLaszlo.Space.isFinite_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L503). The attribute's comment: “P = finite; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` finite, on the glueing functor.** Let `(g : R → R', f)` be a glueing pair
> and let `F` be the glueing functor of Stacks 0F9N restricted, as in Stacks 0F9Q, to the affine
> algebraic spaces over `X = Spec R` which are glueable for `(g, f)`. A morphism `φ` of such
> spaces is finite if and only if the three components of the morphism of triples `F.map φ`, over
> `U = Spec R_f`, `U' = Spec R'_{g f}` and `X' = Spec R'`, are finite.

```lean
theorem isFinite_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    AlgebraicGeometry.Space.IsFinite B (Spec (.of R)) hX φ.hom.hom ↔
      AlgebraicGeometry.Space.IsFinite B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map
            ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
              φ).hom).hom ∧
        AlgebraicGeometry.Space.IsFinite B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsFinite B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom
```

**`BeauvilleLaszlo.Space.isFinite_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L542). The attribute's comment: “P = finite; morphisms of triples with affine components”.

> **Stacks 0F9R for `P` finite, on the inverse equivalence.** Let `(g : R → R', f)` be a glueing
> pair. For every morphism `β` of glueing triples over `U ← U' → X'` with affine components, the
> morphism of affine glueable algebraic spaces over `X = Spec R` corresponding to `β` under the
> equivalence of Stacks 0F9Q is finite if and only if the three components of `β` are finite.

```lean
theorem isFinite_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    AlgebraicGeometry.Space.IsFinite B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ↔
      AlgebraicGeometry.Space.IsFinite B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
        AlgebraicGeometry.Space.IsFinite B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsFinite B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom
```

**`BeauvilleLaszlo.Space.isClosedImmersion_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L579). The attribute's comment: “P = closed immersion; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` closed immersion, on the glueing functor.** Let `(g : R → R', f)` be a
> glueing pair and let `F` be the glueing functor of Stacks 0F9N restricted, as in Stacks 0F9Q, to
> the affine algebraic spaces over `X = Spec R` which are glueable for `(g, f)`. A morphism `φ` of
> such spaces is a closed immersion if and only if the three components of the morphism of triples
> `F.map φ`, over `U = Spec R_f`, `U' = Spec R'_{g f}` and `X' = Spec R'`, are closed immersions.

```lean
theorem isClosedImmersion_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of R)) hX φ.hom.hom ↔
      AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map
            ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
              φ).hom).hom ∧
        AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom
```

**`BeauvilleLaszlo.Space.isClosedImmersion_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L619). The attribute's comment: “P = closed immersion; morphisms of triples with affine components”.

> Let `(g : R → R', f)` be a glueing pair. For every morphism `β` of glueing triples over
> `U ← U' → X'` with affine components, the morphism of affine glueable algebraic spaces over
> `X = Spec R` corresponding to `β` under the inverse of the glueing equivalence is a closed
> immersion if and only if the three components of `β` are closed immersions.

```lean
theorem isClosedImmersion_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ↔
      AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
        AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsClosedImmersion B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom
```

**`BeauvilleLaszlo.Space.isFlat_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L657). The attribute's comment: “P = flat; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` flat, on the glueing functor.** Let `(g : R → R', f)` be a glueing pair
> and let `F` be the glueing functor of Stacks 0F9N restricted, as in Stacks 0F9Q, to the affine
> algebraic spaces over `X = Spec R` which are glueable for `(g, f)`. A morphism `φ` of such
> spaces is flat if and only if the three components of the morphism of triples `F.map φ`, over
> `U = Spec R_f`, `U' = Spec R'_{g f}` and `X' = Spec R'`, are flat.

```lean
theorem isFlat_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    AlgebraicGeometry.Space.IsFlat B (Spec (.of R)) hX φ.hom.hom ↔
      AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map
            ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
              φ).hom).hom ∧
        AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsFlat B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom
```

**`BeauvilleLaszlo.Space.isFlat_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L698). The attribute's comment: “P = flat; morphisms of triples with affine components”.

> **Stacks 0F9R for `P` flat, on the inverse equivalence.** Let `(g : R → R', f)` be a glueing
> pair. For every morphism `β` of glueing triples over `U ← U' → X'` with affine components, the
> morphism of affine glueable algebraic spaces over `X = Spec R` corresponding to `β` under the
> equivalence of Stacks 0F9Q is flat if and only if the three components of `β` are flat.

```lean
theorem isFlat_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    AlgebraicGeometry.Space.IsFlat B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ↔
      AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
        AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsFlat B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom
```

**`BeauvilleLaszlo.Space.isFiniteType_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L737). The attribute's comment: “P = finite type; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` finite type, on the glueing functor.** Let `(g : R → R', f)` be a glueing
> pair and let `F` be the glueing functor of Stacks 0F9N restricted, as in Stacks 0F9Q, to the
> affine algebraic spaces over `X = Spec R` which are glueable for `(g, f)`. A morphism `φ` of
> such spaces is of finite type if and only if the three components of the morphism of triples
> `F.map φ`, over `U = Spec R_f`, `U' = Spec R'_{g f}` and `X' = Spec R'`, are of finite type.

```lean
theorem isFiniteType_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    AlgebraicGeometry.Space.IsFiniteType B (Spec (.of R)) hX φ.hom.hom ↔
      AlgebraicGeometry.Space.IsFiniteType B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map
            ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
              φ).hom).hom ∧
        AlgebraicGeometry.Space.IsFiniteType B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsFiniteType B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom
```

**`BeauvilleLaszlo.Space.isFiniteType_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 777](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L777). The attribute's comment: “P = finite type; morphisms of triples with affine components”.

> **Stacks 0F9R for `P` finite type, on the inverse equivalence.** Let `(g : R → R', f)` be a
> glueing pair. For every morphism `β` of glueing triples over `U ← U' → X'` with affine
> components, the morphism of affine glueable algebraic spaces over `X = Spec R` corresponding to
> `β` under the equivalence of Stacks 0F9Q is of finite type if and only if the three components
> of `β` are of finite type.

```lean
theorem isFiniteType_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    AlgebraicGeometry.Space.IsFiniteType B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ↔
      AlgebraicGeometry.Space.IsFiniteType B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
        AlgebraicGeometry.Space.IsFiniteType B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsFiniteType B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom
```

**`BeauvilleLaszlo.Space.isFlat_and_isFinitePresentation_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 815](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L815). The attribute's comment: “P = flat and finite presentation; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` flat and finite presentation, on the glueing functor.** Let
> `(g : R → R', f)` be a glueing pair and let `F` be the glueing functor of Stacks 0F9N
> restricted, as in Stacks 0F9Q, to the affine algebraic spaces over `X = Spec R` which are
> glueable for `(g, f)`. A morphism `φ` of such spaces is flat and of finite presentation if and
> only if the three components of the morphism of triples `F.map φ`, over `U = Spec R_f`,
> `U' = Spec R'_{g f}` and `X' = Spec R'`, are flat and of finite presentation.

```lean
theorem isFlat_and_isFinitePresentation_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    (AlgebraicGeometry.Space.IsFlat B (Spec (.of R)) hX φ.hom.hom ∧
        AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of R)) hX φ.hom.hom) ↔
      (AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away f))) hU
            ((overU B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of (Localization.Away f))) hU
            ((overU B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom) ∧
        (AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away (g f)))) hU'
              ((overU' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom ∧
            AlgebraicGeometry.Space.IsFinitePresentation B
                (Spec (.of (Localization.Away (g f)))) hU'
              ((overU' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom) ∧
          (AlgebraicGeometry.Space.IsFlat B (Spec (.of R')) hX'
                ((overX' B _ _ _ hU' hU hX' _ _).map
                  ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                    φ).hom).hom ∧
              AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of R')) hX'
                ((overX' B _ _ _ hU' hU hX' _ _).map
                  ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                    φ).hom).hom)
```

**`BeauvilleLaszlo.Space.isFlat_and_isFinitePresentation_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L877). The attribute's comment: “P = flat and finite presentation; morphisms of triples with affine components”.

> **Stacks 0F9R for `P` flat and finite presentation, on the inverse equivalence.** Let
> `(g : R → R', f)` be a glueing pair. For every morphism `β` of glueing triples over
> `U ← U' → X'` with affine components, the morphism of affine glueable algebraic spaces over
> `X = Spec R` corresponding to `β` under the equivalence of Stacks 0F9Q is flat and of finite
> presentation if and only if the three components of `β` are flat and of finite presentation.

```lean
theorem isFlat_and_isFinitePresentation_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    (AlgebraicGeometry.Space.IsFlat B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ∧
      AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom) ↔
      (AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away f))) hU
            ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of (Localization.Away f))) hU
            ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom) ∧
        (AlgebraicGeometry.Space.IsFlat B (Spec (.of (Localization.Away (g f)))) hU'
              ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
            AlgebraicGeometry.Space.IsFinitePresentation B
                (Spec (.of (Localization.Away (g f)))) hU'
              ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom) ∧
          (AlgebraicGeometry.Space.IsFlat B (Spec (.of R')) hX'
                ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
              AlgebraicGeometry.Space.IsFinitePresentation B (Spec (.of R')) hX'
                ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom)
```

**`BeauvilleLaszlo.Space.isEtale_iff_canonicalAffineGlueableRestriction_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 932](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L932). The attribute's comment: “P = étale; morphisms of affine glueable spaces”.

> **Stacks 0F9R for `P` étale, on the glueing functor.** Let `(g : R → R', f)` be a glueing pair
> and let `F` be the glueing functor of Stacks 0F9N restricted, as in Stacks 0F9Q, to the affine
> algebraic spaces over `X = Spec R` which are glueable for `(g, f)`. A morphism `φ` of such
> spaces is étale if and only if the three components of the morphism of triples `F.map φ`, over
> `U = Spec R_f`, `U' = Spec R'_{g f}` and `X' = Spec R'`, are étale.

```lean
theorem isEtale_iff_canonicalAffineGlueableRestriction_map
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {Y Z : (affineGlueableSpaces g f B hX).FullSubcategory} (φ : Y ⟶ Z) :
    AlgebraicGeometry.Space.IsEtale B (Spec (.of R)) hX φ.hom.hom ↔
      AlgebraicGeometry.Space.IsEtale B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map
            ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
              φ).hom).hom ∧
        AlgebraicGeometry.Space.IsEtale B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map
              ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                φ).hom).hom ∧
          AlgebraicGeometry.Space.IsEtale B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map
                ((canonicalAffineGlueableRestriction g f B hU' hU hX' hX hcomm).map
                  φ).hom).hom
```

**`BeauvilleLaszlo.Space.isEtale_affineGlueingEquivalence_inverse_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean, line 973](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingEquivalenceProperties.lean#L973). The attribute's comment: “P = étale; morphisms of triples with affine components”.

> **Stacks 0F9R for `P` étale, on the inverse equivalence.** Let `(g : R → R', f)` be a glueing
> pair. For every morphism `β` of glueing triples over `U ← U' → X'` with affine components, the
> morphism of affine glueable algebraic spaces over `X = Spec R` corresponding to `β` under the
> equivalence of Stacks 0F9Q is étale if and only if the three components of `β` are étale.

```lean
theorem isEtale_affineGlueingEquivalence_inverse_map_iff
    {R R' : Type u} [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R)))
    (hcomm : canGU g f B hU' hU ≫ canJU f B hU hX = canGX' g f B hU' hX' ≫ canJX' g B hX' hX)
    {T₁ T₂ : (affineComponents B _ _ _ hU' hU hX' (canGU g f B hU' hU)
      (canGX' g f B hU' hX')).FullSubcategory} (β : T₁ ⟶ T₂) :
    AlgebraicGeometry.Space.IsEtale B (Spec (.of R)) hX
        ((affineGlueingEquivalence g f B hU' hU hX' hX hcomm hglue).equivalence.inverse.map
          β).hom.hom ↔
      AlgebraicGeometry.Space.IsEtale B (Spec (.of (Localization.Away f))) hU
          ((overU B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
        AlgebraicGeometry.Space.IsEtale B (Spec (.of (Localization.Away (g f)))) hU'
            ((overU' B _ _ _ hU' hU hX' _ _).map β.hom).hom ∧
          AlgebraicGeometry.Space.IsEtale B (Spec (.of R')) hX'
              ((overX' B _ _ _ hU' hU hX' _ _).map β.hom).hom
```

**`BeauvilleLaszlo.isFinite_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L191). The attribute's comment: “P = finite”.

> Let `(R → R', f)` be a glueing pair. A morphism `h : Spec B → Spec A` of schemes over
> `X = Spec R` is finite if and only if its base changes to `U = Spec R_f`, `U' = Spec R'_f` and
> `X' = Spec R'`, the three components of its image under the glueing functor of Stacks 0F9N, are
> finite.

```lean
theorem isFinite_iff_baseChange (f : R) (hglue : IsGlueingPair (algebraMap R R') f)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    IsFinite h.left ↔
      IsFinite ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        IsFinite ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
          IsFinite ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R R')))).map h).left
```

**`BeauvilleLaszlo.isClosedImmersion_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L220). The attribute's comment: “P = closed immersion”.

> Let `(R → R', f)` be a glueing pair. A morphism `h : Spec B → Spec A` of schemes over
> `X = Spec R` is a closed immersion if and only if its base changes to `U = Spec R_f`,
> `U' = Spec R'_f` and `X' = Spec R'`, the three components of its image under the glueing functor of
> Stacks 0F9N, are closed immersions.

```lean
theorem isClosedImmersion_iff_baseChange (f : R) (hglue : IsGlueingPair (algebraMap R R') f)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    IsClosedImmersion h.left ↔
      IsClosedImmersion ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        IsClosedImmersion ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
          IsClosedImmersion ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R R')))).map h).left
```

**`BeauvilleLaszlo.flat_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L241). The attribute's comment: “P = flat”.

> Let `(R → R', f)` be a glueing pair and let the `R`-algebra `A` be glueable for it. A morphism
> `h : Spec B → Spec A` of schemes over `X = Spec R` is flat if and only if its base changes to
> `U = Spec R_f`, `U' = Spec R'_f` and `X' = Spec R'`, the three components of its image under the
> glueing functor of Stacks 0F9N, are flat.

```lean
theorem flat_iff_baseChange (f : R) (hglue : IsGlueingPair (algebraMap R R') f)
    (hA : (beauvilleLaszloModuleSequence (S := R') A f).ShortExact)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    Flat h.left ↔
      Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
          Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R R')))).map h).left
```

**`BeauvilleLaszlo.locallyOfFiniteType_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L262). The attribute's comment: “P = finite type”.

> Let `(R → R', f)` be a glueing pair. A morphism `h : Spec B → Spec A` of schemes over
> `X = Spec R` is locally of finite type if and only if its base changes to `U = Spec R_f`,
> `U' = Spec R'_f` and `X' = Spec R'`, the three components of its image under the glueing functor of
> Stacks 0F9N, are. A morphism of affine schemes is of finite type exactly when it is locally of
> finite type, being quasi-compact.

```lean
theorem locallyOfFiniteType_iff_baseChange (f : R) (hglue : IsGlueingPair (algebraMap R R') f)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    LocallyOfFiniteType h.left ↔
      LocallyOfFiniteType ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        LocallyOfFiniteType ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
          LocallyOfFiniteType ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R R')))).map h).left
```

**`BeauvilleLaszlo.flat_and_locallyOfFinitePresentation_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L284). The attribute's comment: “P = flat and finite presentation”.

> Let `(R → R', f)` be a glueing pair and let the `R`-algebra `A` be glueable for it. A morphism
> `h : Spec B → Spec A` of schemes over `X = Spec R` is flat and locally of finite presentation if
> and only if its base changes to `U = Spec R_f`, `U' = Spec R'_f` and `X' = Spec R'`, the three
> components of its image under the glueing functor of Stacks 0F9N, are. A morphism of affine schemes
> is of finite presentation exactly when it is locally of finite presentation, being quasi-compact
> and quasi-separated.

```lean
theorem flat_and_locallyOfFinitePresentation_iff_baseChange (f : R)
    (hglue : IsGlueingPair (algebraMap R R') f)
    (hA : (beauvilleLaszloModuleSequence (S := R') A f).ShortExact)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    (Flat h.left ∧ LocallyOfFinitePresentation h.left) ↔
      (Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        LocallyOfFinitePresentation ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left) ∧
      (Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
        LocallyOfFinitePresentation ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left) ∧
      (Flat ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R R')))).map h).left ∧
        LocallyOfFinitePresentation ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R R')))).map h).left)
```

**`BeauvilleLaszlo.etale_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingProperties.lean#L318). The attribute's comment: “P = étale”.

> Let `(R → R', f)` be a glueing pair and let the `R`-algebra `A` be glueable for it. A morphism
> `h : Spec B → Spec A` of schemes over `X = Spec R` is étale if and only if its base changes to
> `U = Spec R_f`, `U' = Spec R'_f` and `X' = Spec R'`, the three components of its image under the
> glueing functor of Stacks 0F9N, are étale.

```lean
theorem etale_iff_baseChange (f : R) (hglue : IsGlueingPair (algebraMap R R') f)
    (hA : (beauvilleLaszloModuleSequence (S := R') A f).ShortExact)
    (h : Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R B))) ⟶
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap R A)))) :
    Etale h.left ↔
      Etale ((Over.pullback (Spec.map (CommRingCat.ofHom
          (algebraMap R (Localization.Away f))))).map h).left ∧
        Etale ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R (Localization.Away (algebraMap R R' f)))))).map h).left ∧
          Etale ((Over.pullback (Spec.map (CommRingCat.ofHom
            (algebraMap R R')))).map h).left
```

## Tag 0F9S, a lemma

[Tag 0F9S](https://stacks.math.columbia.edu/tag/0F9S) in the Stacks Project.

**`BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces_map_injective_of_isGlueable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFaithful.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFaithful.lean#L670).

> The Beauville--Laszlo gluing functor is faithful on glueable algebraic spaces over `Spec R`.

```lean
theorem beauvilleLaszloGlueingSpaces_map_injective_of_isGlueable
    (R R' : Type u) [CommRing R] [CommRing R']
    (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f)
    (B : AlgebraicGeometry.BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R')))
    (hX : B.Contains (Spec (.of R))) :
    let U' : Scheme.{u} := Spec (.of (Localization.Away (g f)))
    let U : Scheme.{u} := Spec (.of (Localization.Away f))
    let X' : Scheme.{u} := Spec (.of R')
    let X : Scheme.{u} := Spec (.of R)
    let gU : B.obj hU' ⟶ B.obj hU :=
      ⟨Spec.map (CommRingCat.ofHom (Localization.awayMap g f))⟩
    let gX' : B.obj hU' ⟶ B.obj hX' :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R' (Localization.Away (g f))))⟩
    let jU : B.obj hU ⟶ B.obj hX :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R (Localization.Away f)))⟩
    let jX' : B.obj hX' ⟶ B.obj hX :=
      ⟨Spec.map (CommRingCat.ofHom g)⟩
    ∀ (hcomm : gU ≫ jU = gX' ≫ jX')
      (Y Z : _root_.AlgebraicGeometry.AlgebraicSpaces B X hX),
      _root_.AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Y →
      _root_.AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Z →
      Function.Injective (fun (φ : Y ⟶ Z) ↦
        (BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces
          B U' U X' X hU' hU hX' hX gU gX' jU jX' hcomm).functor.map φ)
```

## Tag 0F9T, a lemma

[Tag 0F9T](https://stacks.math.columbia.edu/tag/0F9T) in the Stacks Project.

**`BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces_map_surjective_of_isGlueable_of_isAffineHom_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithfulComplete.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithfulComplete.lean#L316). The attribute's comment: “fullness”.

> **Stacks 0F9T, fullness.** For a Beauville--Laszlo glueing pair `(g : R → R', f)`, a
> morphism of glueing triples between the images of two algebraic spaces over `Spec R` which are
> glueable for `(g, f)` comes from a morphism of algebraic spaces, provided the target has affine
> diagonal.
>
> Nothing beyond the glueing pair and these two conditions is assumed: the equivalence of the
> affine case is `BeauvilleLaszlo.Space.affineGlueingEquivalence` (Stacks 0F9Q) and étaleness of a
> morphism of affine glueable spaces in terms of its components is
> `BeauvilleLaszlo.Space.isEtale_iff_isEtale_glueingComponents` (Stacks 0F9R for the property
> "étale"); both are supplied to
> `beauvilleLaszloGlueingSpaces_map_surjective_of_isGlueable_of_affineDiagonal`.

```lean
theorem beauvilleLaszloGlueingSpaces_map_surjective_of_isGlueable_of_isAffineHom_diag
    (R R' : Type u) [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R))) :
    let U' : Scheme.{u} := Spec (.of (Localization.Away (g f)))
    let U : Scheme.{u} := Spec (.of (Localization.Away f))
    let X' : Scheme.{u} := Spec (.of R')
    let X : Scheme.{u} := Spec (.of R)
    let gU : B.obj hU' ⟶ B.obj hU :=
      ⟨Spec.map (CommRingCat.ofHom (Localization.awayMap g f))⟩
    let gX' : B.obj hU' ⟶ B.obj hX' :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R' (Localization.Away (g f))))⟩
    let jU : B.obj hU ⟶ B.obj hX :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R (Localization.Away f)))⟩
    let jX' : B.obj hX' ⟶ B.obj hX := ⟨Spec.map (CommRingCat.ofHom g)⟩
    ∀ (hcomm : gU ≫ jU = gX' ≫ jX') (Y Z : AlgebraicSpaces B X hX),
      AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Y →
      AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Z →
      AlgebraicGeometry.Space.IsAffineHom B X hX (diag Z.1) →
      Function.Surjective (fun (φ : Y ⟶ Z) ↦
        (beauvilleLaszloGlueingSpaces
          B U' U X' X hU' hU hX' hX gU gX' jU jX' hcomm).functor.map φ)
```

**`BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces_map_bijective_of_isGlueable_of_isAffineHom_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithfulComplete.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithfulComplete.lean#L357).

> **Stacks 0F9T.** For a Beauville--Laszlo glueing pair `(g : R → R', f)`, the glueing functor
> of Stacks 0F9N is fully faithful on the full subcategory of algebraic spaces `Y/X` which are
> glueable for `(g, f)` and have affine diagonal `Y → Y ×_X Y`: the map it induces on each hom-set
> between two such objects is bijective.
>
> Injectivity is Stacks 0F9S, which needs glueability alone; surjectivity needs affineness of the
> diagonal of the target alone, and is
> `beauvilleLaszloGlueingSpaces_map_surjective_of_isGlueable_of_isAffineHom_diag`.

```lean
theorem beauvilleLaszloGlueingSpaces_map_bijective_of_isGlueable_of_isAffineHom_diag
    (R R' : Type u) [CommRing R] [CommRing R'] (g : R →+* R') (f : R)
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f) (B : BigFppfSite.{u})
    (hU' : B.Contains (Spec (.of (Localization.Away (g f)))))
    (hU : B.Contains (Spec (.of (Localization.Away f))))
    (hX' : B.Contains (Spec (.of R'))) (hX : B.Contains (Spec (.of R))) :
    let U' : Scheme.{u} := Spec (.of (Localization.Away (g f)))
    let U : Scheme.{u} := Spec (.of (Localization.Away f))
    let X' : Scheme.{u} := Spec (.of R')
    let X : Scheme.{u} := Spec (.of R)
    let gU : B.obj hU' ⟶ B.obj hU :=
      ⟨Spec.map (CommRingCat.ofHom (Localization.awayMap g f))⟩
    let gX' : B.obj hU' ⟶ B.obj hX' :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R' (Localization.Away (g f))))⟩
    let jU : B.obj hU ⟶ B.obj hX :=
      ⟨Spec.map (CommRingCat.ofHom (algebraMap R (Localization.Away f)))⟩
    let jX' : B.obj hX' ⟶ B.obj hX := ⟨Spec.map (CommRingCat.ofHom g)⟩
    ∀ (hcomm : gU ≫ jU = gX' ≫ jX') (Y Z : AlgebraicSpaces B X hX),
      AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Y →
      AlgebraicGeometry.Space.IsGlueableAlgebraicSpace g f B hX Z →
      AlgebraicGeometry.Space.IsAffineHom B X hX (diag Y.1) →
      AlgebraicGeometry.Space.IsAffineHom B X hX (diag Z.1) →
      Function.Bijective (fun (φ : Y ⟶ Z) ↦
        (beauvilleLaszloGlueingSpaces
          B U' U X' X hU' hU hX' hX gU gX' jU jX' hcomm).functor.map φ)
```

Declarations registered for the tag:

- [`BeauvilleLaszlo.Space.beauvilleLaszloGlueingSpaces_map_injective_of_isGlueable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFaithful.lean#L670), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithful.lean, line 1131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingFullyFaithful.lean#L1131) (StacksFrontier): “faithfulness”.

## Tag 0F9U, a lemma

[Tag 0F9U](https://stacks.math.columbia.edu/tag/0F9U) in the Stacks Project.

**`BeauvilleLaszlo.Space.exists_isSeparatedOver_iso_of_isQuasiAffineComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingQuasiAffineUnconditional.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BeauvilleLaszloGlueingQuasiAffineUnconditional.lean#L116).

> **Stacks 0F9U.** Let `(g : R → R', f)` be a glueing pair, and let `X = Spec R`,
> `U = Spec R_f`, `X' = Spec R'` and `U' = Spec R'_{g f}` be the four corners of its square, all in
> the big fppf site `B`. Any cartesian triple `(V, V', Y')` of algebraic spaces over `U ← U' → X'`
> whose three components are quasi-affine is isomorphic to the image, under the gluing functor of
> Stacks 0F9N, of an algebraic space `Y` over `X` which is separated over `X`.

```lean
theorem exists_isSeparatedOver_iso_of_isQuasiAffineComponents
    (hglue : _root_.BeauvilleLaszlo.IsGlueingPair g f)
    (Z : GlueingData B (Spec (.of (Localization.Away (g f))))
      (Spec (.of (Localization.Away f))) (Spec (.of R')) hU' hU hX'
      (canGU g f B hU' hU) (canGX' g f B hU' hX'))
    (hZ : quasiAffineComponents B (Spec (.of (Localization.Away (g f))))
      (Spec (.of (Localization.Away f))) (Spec (.of R')) hU' hU hX'
      (canGU g f B hU' hU) (canGX' g f B hU' hX') Z) :
    ∃ Y : AlgebraicSpaces B (Spec (.of R)) hX,
      AlgebraicGeometry.Space.IsSeparatedOver B (Spec (.of R)) hX Y.obj ∧
        Nonempty ((beauvilleLaszloGlueingSpaces B _ _ _ _ hU' hU hX' hX
          (canGU g f B hU' hU) (canGX' g f B hU' hX') (canJU f B hU hX) (canJX' g B hX' hX)
          (canonical_comm g f B hU' hU hX' hX)).functor.obj Y ≅ Z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.12, Tag 0F9M](https://stacks.math.columbia.edu/tag/0F9M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
