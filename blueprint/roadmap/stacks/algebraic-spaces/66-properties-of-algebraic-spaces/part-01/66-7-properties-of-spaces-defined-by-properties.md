---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_atlas_iff_forall_etale, AlgebraicGeometry.Space.exists_atlas_iff_of_representable, AlgebraicGeometry.Space.HasEtaleLocalProperty, AlgebraicGeometry.jacobsonSpace_isLocal_etale, AlgebraicGeometry.isLocallyNoetherian_and_hasPropertySk_isLocal_etale, AlgebraicGeometry.isCohenMacaulay_isLocal_etale, AlgebraicGeometry.isGorenstein_isLocal_etale, AlgebraicGeometry.isLocallyNoetherian_and_isRegularInCodimension_isLocal_etale
statement: formalized
proof: formalized
---

# 66.7 Properties of Spaces defined by properties of schemes

Section 66.7 of the Stacks Project, [Tag 03E5](https://stacks.math.columbia.edu/tag/03E5). 6 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03E8, a lemma

[Tag 03E8](https://stacks.math.columbia.edu/tag/03E8) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_atlas_iff_forall_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean#L150). The attribute's comment: “equivalence of atlas conditions”.

> **Stacks 03E8.** An étale-local property holds on some surjective étale atlas exactly
> when it holds on every étale scheme over the algebraic space.

```lean
theorem exists_atlas_iff_forall_etale (hF : IsAlgebraicSpace B S hS F) :
    HasEtaleLocalProperty B S hS F P ↔
    (∀ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) g →
      P ((BigFppfOver.toScheme B S hS).obj V))
```

**`AlgebraicGeometry.Space.exists_atlas_iff_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean#L196). The attribute's comment: “representable case”.

> **Stacks 03E8.** For a represented algebraic space, the atlas condition is equivalent
> to the property of its representing scheme.

```lean
theorem exists_atlas_iff_of_representable
    (X : BigFppfOver B S hS) (e : F ≅ yoneda.obj X) :
    HasEtaleLocalProperty B S hS F P ↔ P ((BigFppfOver.toScheme B S hS).obj X)
```

## Tag 03E6, a definition

[Tag 03E6](https://stacks.math.columbia.edu/tag/03E6) in the Stacks Project.

**`AlgebraicGeometry.Space.HasEtaleLocalProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean#L137).

> **Stacks 03E6.** An algebraic space has an étale-local property of schemes if it has a
> surjective étale atlas by a scheme with that property.

```lean
abbrev HasEtaleLocalProperty : Prop
```

## Tag 03E7, a remark

[Tag 03E7](https://stacks.math.columbia.edu/tag/03E7) in the Stacks Project.

**`AlgebraicGeometry.jacobsonSpace_isLocal_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L110). The attribute's comment: “item (2): Jacobson, by Stacks 0368”.

> **Stacks Project, Tag 03E7, item (2).** Being a Jacobson scheme is local for étale
> coverings of schemes: a scheme is Jacobson if and only if the members of an étale covering
> family are.
>
> This is Stacks 0368, which gives the fppf case, read through the inclusion of the étale
> precoverage in the fppf one.

```lean
instance jacobsonSpace_isLocal_etale :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => JacobsonSpace X) Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isLocallyNoetherian_and_hasPropertySk_isLocal_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L122). The attribute's comment: “item (3): locally Noetherian and (S\_k), by Stacks 036A”.

> **Stacks Project, Tag 03E7, item (3).** Being locally Noetherian and satisfying Serre's
> condition `(S_k)` is local for étale coverings of schemes.
>
> This is Stacks 036A, which gives the syntomic case, read through the inclusion of the étale
> precoverage in the syntomic one.

```lean
instance isLocallyNoetherian_and_hasPropertySk_isLocal_etale (k : ℕ) :
    ObjectProperty.IsLocal
      (fun X : Scheme.{u} => ∃ h : IsLocallyNoetherian X, @HasPropertySk X h k)
      Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isCohenMacaulay_isLocal_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L136). The attribute's comment: “item (4): Cohen-Macaulay, by Stacks 036B”.

> **Stacks Project, Tag 03E7, item (4).** Being a Cohen-Macaulay scheme is local for étale
> coverings of schemes.
>
> This is Stacks 036B, which gives the syntomic case, read through the inclusion of the étale
> precoverage in the syntomic one.

```lean
instance isCohenMacaulay_isLocal_etale :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsCohenMacaulay X) Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isGorenstein_isLocal_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L169). The attribute's comment: “item (5): Gorenstein, the étale case of Stacks 0C01”.

> **Stacks Project, Tag 03E7, item (5).** Being a Gorenstein scheme is local for étale
> coverings of schemes: a scheme is Gorenstein if and only if the members of an étale covering
> family are.
>
> The source cites Stacks 0C01, which states the syntomic case; only the étale case is proved
> here. Ascent is `AlgebraicGeometry.isGorenstein_of_etale`. For descent, local Noetherianity
> of the base is item (1), and the Gorenstein condition on the stalk at a point of the base is
> transported from a point of a member of the family above it.

```lean
instance isGorenstein_isLocal_etale :
    ObjectProperty.IsLocal (fun X : Scheme.{u} => IsGorenstein X) Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isLocallyNoetherian_and_isRegularInCodimension_isLocal_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L206). The attribute's comment: “item (8): locally Noetherian and (R\_k), by Stacks 036C”. References: EGA IV (17.5.8), “(iii), special case”.

> **Stacks Project, Tag 03E7, item (8).** Being locally Noetherian and regular in
> codimension `k` is local for étale coverings of schemes.
>
> This is Stacks 036C, which gives the smooth case, read through the inclusion of the étale
> precoverage in the smooth one.

```lean
instance isLocallyNoetherian_and_isRegularInCodimension_isLocal_etale (k : ℕ) :
    ObjectProperty.IsLocal
      (fun X : Scheme.{u} => IsLocallyNoetherian X ∧ IsRegularInCodimension X k)
      Scheme.etalePrecoverage
```

Declarations registered for the tag:

- [`isLocallyNoetherian_isLocal_etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isLocallyNoetherian_isLocal_etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L99) (StacksFrontier): “item (1): locally Noetherian, by Stacks 034C”.
- [`isReduced_isLocal_etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isReduced_isLocal_etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L191) (StacksFrontier): “item (6): reduced, by Stacks 034E”.
- [`isLocal_isNormal_etalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isLocal_isNormal_etalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L195) (StacksFrontier): “item (7): normal, by Stacks 034F”.
- [`isRegular_isLocal_etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isRegular_isLocal_etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L214) (StacksFrontier): “item (9): regular, by Stacks 036D”.
- [`isNagataScheme_isLocal_etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isNagataScheme_isLocal_etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/EtaleLocalList.lean#L218) (StacksFrontier): “item (10): Nagata, by Stacks 036E”.

## Tag 04N2, a lemma

[Tag 04N2](https://stacks.math.columbia.edu/tag/04N2) in the Stacks Project.

**`AlgebraicGeometry.Space.forall_etale_chart_iff_exists_etale_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean#L208). The attribute's comment: “equivalence of chart conditions”.

> **Stacks 04N2, conditions (1) and (2).** An étale-local property of germs of schemes
> holds at every étale scheme chart over a point of an algebraic space exactly when it holds at
> some such chart.

```lean
theorem forall_etale_chart_iff_exists_etale_chart (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F)
    (P : GermOfScheme.{u} → Prop) (hP : GermOfScheme.IsEtaleLocal P) :
    (∀ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a →
      ∀ p : FieldValuedPoint B S hS (yoneda.obj U),
        pointsMap B S hS (yoneda.obj U) a (p.class B S hS (yoneda.obj U)) = x →
        P ⟨(BigFppfOver.toScheme B S hS).obj U, schemePoint B S hS U p⟩) ↔
    (∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      ∃ p : FieldValuedPoint B S hS (yoneda.obj U),
        pointsMap B S hS (yoneda.obj U) a (p.class B S hS (yoneda.obj U)) = x ∧
        P ⟨(BigFppfOver.toScheme B S hS).obj U, schemePoint B S hS U p⟩)
```

**`AlgebraicGeometry.Space.forall_etale_chart_iff_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean#L247). The attribute's comment: “representable case”.

> **Stacks 04N2, the representable case.** For a represented algebraic space the
> every-chart condition is the property of the germ of its representing scheme at the
> corresponding scheme point.

```lean
theorem forall_etale_chart_iff_of_representable (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (X : BigFppfOver B S hS)
    (e : yoneda.obj X ≅ F) (p : FieldValuedPoint B S hS (yoneda.obj X))
    (P : GermOfScheme.{u} → Prop) (hP : GermOfScheme.IsEtaleLocal P) :
    (∀ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a →
      ∀ q : FieldValuedPoint B S hS (yoneda.obj U),
        pointsMap B S hS (yoneda.obj U) a (q.class B S hS (yoneda.obj U)) =
          pointsMap B S hS (yoneda.obj X) e.hom (p.class B S hS (yoneda.obj X)) →
        P ⟨(BigFppfOver.toScheme B S hS).obj U, schemePoint B S hS U q⟩) ↔
      P ⟨(BigFppfOver.toScheme B S hS).obj X, schemePoint B S hS X p⟩
```

**`AlgebraicGeometry.Space.exists_etale_chart_iff_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean#L271). The attribute's comment: “representable case, existential condition”.

> **Stacks 04N2, the representable case.** For a represented algebraic space the one-chart
> condition is the property of the germ of its representing scheme at the corresponding scheme
> point.

```lean
theorem exists_etale_chart_iff_of_representable (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (X : BigFppfOver B S hS)
    (e : yoneda.obj X ≅ F) (p : FieldValuedPoint B S hS (yoneda.obj X))
    (P : GermOfScheme.{u} → Prop) (hP : GermOfScheme.IsEtaleLocal P) :
    (∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      ∃ q : FieldValuedPoint B S hS (yoneda.obj U),
        pointsMap B S hS (yoneda.obj U) a (q.class B S hS (yoneda.obj U)) =
          pointsMap B S hS (yoneda.obj X) e.hom (p.class B S hS (yoneda.obj X)) ∧
        P ⟨(BigFppfOver.toScheme B S hS).obj U, schemePoint B S hS U q⟩) ↔
      P ⟨(BigFppfOver.toScheme B S hS).obj X, schemePoint B S hS X p⟩
```

## Tag 04RC, a definition

[Tag 04RC](https://stacks.math.columbia.edu/tag/04RC) in the Stacks Project.

**`AlgebraicGeometry.Space.HasPropertyAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GermPropertyAtPoint.lean#L79).

> **Stacks 04RC.** A property `P` of germs of schemes holds at a point `x` of an algebraic
> space `F` when it holds at the germ of some étale scheme chart `yoneda.obj U ⟶ F` at some
> field-valued point of `U` lying over `x`. For an étale-local property the choice of chart is
> immaterial, by `AlgebraicGeometry.Space.forall_etale_chart_iff_exists_etale_chart`; stating
> this one-chart condition needs neither that hypothesis nor that `F` is an algebraic space.

```lean
abbrev HasPropertyAtPoint (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (x : points B S hS F)
    (P : GermOfScheme.{u} → Prop) : Prop
```

## Tag 0BBL, a remark

[Tag 0BBL](https://stacks.math.columbia.edu/tag/0BBL) in the Stacks Project.

**`AlgebraicGeometry.GermOfScheme.isEtaleLocal_stalk_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/LocalRingProperty.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germ/LocalRingProperty.lean#L50). The attribute's comment: “germ\_criterion”.

> **Stacks 0BBL, the germ criterion.** A property of local rings which is invariant under
> isomorphisms and unchanged on passing to a prime above it along an étale ring map induces an
> étale-local property of germs of schemes, by evaluation on the local ring at the marked
> point.

```lean
theorem GermOfScheme.isEtaleLocal_stalk_property (P : (R : Type u) → [CommRing R] → Prop)
    (hP : ∀ {A B : Type u} [CommRing A] [CommRing B] [Algebra A B] [Algebra.Etale A B]
      (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime],
      q.comap (algebraMap A B) = p →
        (P (Localization.AtPrime p) ↔ P (Localization.AtPrime q)))
    (hP_iso : ∀ {R S : Type u} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S],
      (R ≃+* S) → (P R ↔ P S)) :
    GermOfScheme.IsEtaleLocal (fun g => P (g.scheme.presheaf.stalk g.point))
```

**`AlgebraicGeometry.Space.HasLocalRingPropertyAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedLocalRings.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedLocalRings.lean#L72). The attribute's comment: “local\_ring\_of\_an\_algebraic\_space\_has\_p”.

> **Stacks 0BBL, the local ring of an algebraic space.** A property `P` of local rings which
> is invariant under étale localization holds for the local ring of an algebraic space `F` at a
> point `x` when it holds for the stalk of some étale scheme chart at some point above `x`. By
> Stacks 04N2 the chart is immaterial, and the invariance hypothesis `_hP` is what makes that
> so; it is carried as an argument of the predicate rather than assumed of `P` globally.

```lean
abbrev HasLocalRingPropertyAtPoint (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hF : IsAlgebraicSpace B S hS F) (x : points B S hS F)
    (P : (R : Type u) → [CommRing R] → Prop)
    (_hP : ∀ {A C : Type u} [CommRing A] [CommRing C] [Algebra A C] [Algebra.Etale A C]
      (p : Ideal A) [p.IsPrime] (q : Ideal C) [q.IsPrime],
      q.comap (algebraMap A C) = p →
        (P (Localization.AtPrime p) ↔ P (Localization.AtPrime q))) : Prop
```

**`isNoetherianRing_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L150). The attribute's comment: “Noetherian”.

> **Stacks 0BBL, Noetherian.** For prime ideals `p` and `q` corresponding under an étale map
> `A → B`, the local ring of `A` at `p` is Noetherian if and only if the local ring of `B` at `q`
> is Noetherian.

```lean
theorem isNoetherianRing_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    IsNoetherianRing (Localization.AtPrime p) ↔ IsNoetherianRing (Localization.AtPrime q)
```

**`ringKrullDim_eq_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L167). The attribute's comment: “dimension d”.

> **Stacks 0BBL, dimension `d`.** For prime ideals `p` and `q` corresponding under an étale
> map `A → B`, the local ring of `A` at `p` has dimension `d` if and only if the local ring of `B`
> at `q` has dimension `d`.

```lean
theorem ringKrullDim_eq_localizationAtPrime_iff_of_etale (d : WithBot ℕ∞)
    (hq : q.comap (algebraMap A B) = p) :
    ringKrullDim (Localization.AtPrime p) = d ↔ ringKrullDim (Localization.AtPrime q) = d
```

**`isRegularLocalRing_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L176). The attribute's comment: “regular”.

> **Stacks 0BBL, regular.** For prime ideals `p` and `q` corresponding under an étale map
> `A → B`, the local ring of `A` at `p` is regular if and only if the local ring of `B` at `q` is
> regular.

```lean
theorem isRegularLocalRing_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    IsRegularLocalRing (Localization.AtPrime p) ↔
      IsRegularLocalRing (Localization.AtPrime q)
```

**`isDiscreteValuationRing_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L188). The attribute's comment: “discrete valuation ring”.

> **Stacks 0BBL, discrete valuation ring.** For prime ideals `p` and `q` corresponding under
> an étale map `A → B`, the local ring of `A` at `p` is a discrete valuation ring if and only if
> the local ring of `B` at `q` is one. This is regularity together with dimension one, through
> item (3) of the characterisation of Tag 00PD.

```lean
theorem isDiscreteValuationRing_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    (∃ _ : IsDomain (Localization.AtPrime p),
        IsDiscreteValuationRing (Localization.AtPrime p)) ↔
      (∃ _ : IsDomain (Localization.AtPrime q),
        IsDiscreteValuationRing (Localization.AtPrime q))
```

**`isNormalDomain_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L203). The attribute's comment: “normal”.

> **Stacks 0BBL, normal.** For prime ideals `p` and `q` corresponding under an étale map
> `A → B`, the local ring of `A` at `p` is a normal domain if and only if the local ring of `B` at
> `q` is one. Neither ring is assumed Noetherian.

```lean
theorem isNormalDomain_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    IsNormalDomain (Localization.AtPrime p) ↔ IsNormalDomain (Localization.AtPrime q)
```

**`isNoetherianRing_and_ringDepth_eq_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L250). The attribute's comment: “Noetherian and depth k”.

> **Stacks 0BBL, Noetherian and depth `k`.** For prime ideals `p` and `q` corresponding under
> an étale map `A → B`, the local ring of `A` at `p` is Noetherian of depth `k` if and only if the
> local ring of `B` at `q` is.

```lean
theorem isNoetherianRing_and_ringDepth_eq_localizationAtPrime_iff_of_etale (k : ℕ∞)
    (hq : q.comap (algebraMap A B) = p) :
    (IsNoetherianRing (Localization.AtPrime p) ∧ ringDepth (Localization.AtPrime p) = k) ↔
      (IsNoetherianRing (Localization.AtPrime q) ∧ ringDepth (Localization.AtPrime q) = k)
```

**`isCohenMacaulayLocalRing_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L263). The attribute's comment: “Noetherian and Cohen-Macaulay”.

> **Stacks 0BBL, Noetherian and Cohen-Macaulay.** For prime ideals `p` and `q` corresponding
> under an étale map `A → B`, the local ring of `A` at `p` is Noetherian and Cohen-Macaulay if and
> only if the local ring of `B` at `q` is.

```lean
theorem isCohenMacaulayLocalRing_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    (∃ h : IsNoetherianRing (Localization.AtPrime p),
        @IsCohenMacaulayLocalRing (Localization.AtPrime p) _ h _) ↔
      (∃ h : IsNoetherianRing (Localization.AtPrime q),
        @IsCohenMacaulayLocalRing (Localization.AtPrime q) _ h _)
```

**`isGorensteinLocalRing_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalRingPropertyList.lean#L277). The attribute's comment: “Noetherian and Gorenstein”.

> **Stacks 0BBL, Noetherian and Gorenstein.** For prime ideals `p` and `q` corresponding
> under an étale map `A → B`, the local ring of `A` at `p` is Noetherian and Gorenstein if and
> only if the local ring of `B` at `q` is.

```lean
theorem isGorensteinLocalRing_localizationAtPrime_iff_of_etale
    (hq : q.comap (algebraMap A B) = p) :
    (∃ h : IsNoetherianRing (Localization.AtPrime p),
        @Dualizing.IsGorensteinLocalRing (Localization.AtPrime p) _ h _) ↔
      (∃ h : IsNoetherianRing (Localization.AtPrime q),
        @Dualizing.IsGorensteinLocalRing (Localization.AtPrime q) _ h _)
```

**`isReduced_localizationAtPrime_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ReducedLocalization.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/ReducedLocalization.lean#L87). The attribute's comment: “reduced”.

> **Stacks 0BBL, reducedness.** For prime ideals `p` and `q` corresponding under an étale
> map `A → B`, the local ring of `A` at `p` is reduced if and only if the local ring of `B` at
> `q` is reduced.

```lean
theorem isReduced_localizationAtPrime_iff_of_etale {A : Type u} {B : Type v} [CommRing A]
    [CommRing B] [Algebra A B] [Algebra.Etale A B] (p : Ideal A) [p.IsPrime] (q : Ideal B)
    [q.IsPrime] (hq : q.comap (algebraMap A B) = p) :
    IsReduced (Localization.AtPrime p) ↔ IsReduced (Localization.AtPrime q)
```

Declarations registered for the tag:

- [`RingHom.Etale.ringKrullDim_localization_atPrime_eq`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Height.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/EtaleLocalProperty.lean#L216) (StacksFrontier): “dimension”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.7, Tag 03E5](https://stacks.math.columbia.edu/tag/03E5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
