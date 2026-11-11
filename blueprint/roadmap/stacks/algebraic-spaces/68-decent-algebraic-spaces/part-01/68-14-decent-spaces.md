---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isLocallyNoetherian_of_isDecentSpace, AlgebraicGeometry.Space.isRepresentable_of_subsingleton_points, AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_subsingleton_points, AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction, AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_reduction, AlgebraicGeometry.Space.isClosed_singleton_class_of_isAlgebraic_residueField, AlgebraicGeometry.Space.isFinite_fieldMorphism_of_moduleFinite_residueField, AlgebraicGeometry.Space.isClosedImmersion_fieldMorphism_of_isIso_residueField
statement: formalized
proof: formalized
---

# 68.14 Decent spaces

Section 68.14 of the Stacks Project, [Tag 047Y](https://stacks.math.columbia.edu/tag/047Y). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BB6, a lemma

[Tag 0BB6](https://stacks.math.columbia.edu/tag/0BB6) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isLocallyNoetherian_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/NoetherianQuasiSeparated.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/NoetherianQuasiSeparated.lean#L574).

> A locally Noetherian decent algebraic space is quasi-separated.

```lean
theorem isAbsolutelyQuasiSeparated_of_isLocallyNoetherian_of_isDecentSpace
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hNoeth : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (hdec : IsDecentSpace B S hS X) :
    IsAbsolutelyQuasiSeparated B S hS hZ X
```

## Tag 047Z, a lemma

[Tag 047Z](https://stacks.math.columbia.edu/tag/047Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_subsingleton_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean#L253). The attribute's comment: “part (1)”.

> **Stacks 047Z, part (1).** A decent algebraic space over `S` whose point set is a singleton
> is a scheme.

```lean
theorem isRepresentable_of_subsingleton_points (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (hne : Nonempty (points B S hS X))
    (hsub : Subsingleton (points B S hS X)) : X.IsRepresentable
```

**`AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_subsingleton_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean#L340). The attribute's comment: “part (2)”.

> **Stacks 047Z, part (2).** A reduced decent algebraic space over `S` whose point set is a
> singleton is the spectrum of a field.

```lean
theorem exists_iso_yoneda_spec_of_subsingleton_points (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (hne : Nonempty (points B S hS X))
    (hsub : Subsingleton (points B S hS X))
    (hred : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} ↦ IsReduced Y)) :
    ∃ (M : BigFppfOver B S hS) (k : Type u) (_ : Field k),
      Nonempty ((BigFppfOver.toScheme B S hS).obj M ≅ Spec (.of k)) ∧
        Nonempty (X ≅ yoneda.obj M)
```

## Tag 049D, a remark

[Tag 049D](https://stacks.math.columbia.edu/tag/049D) in the Stacks Project.

**`AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfSchemeReduction.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfSchemeReduction.lean#L167).

> An algebraic space over `S` whose reduction is a scheme is a scheme.

```lean
theorem isRepresentable_of_isRepresentable_reduction {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hred : (reduction B S hS X hX).toFunctor.IsRepresentable) :
    X.IsRepresentable
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_reduction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L337), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijection.lean#L363) (StacksFrontier): “an algebraic space whose reduction is a scheme is a scheme, granted the same three hypotheses `h09YA`, `h07SQ` and `hFinitePresentation` that the Stacks 07VU attribute of this declaration records.”.

## Tag 07U5, a lemma

[Tag 07U5](https://stacks.math.columbia.edu/tag/07U5) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_singleton_class_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ClosedPoints.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ClosedPoints.lean#L278). The attribute's comment: “with decency read as condition (alpha) of Stacks 03JX”.

> Let `X` be an algebraic space over a scheme `S` above every point of which every étale
> chart of `X` by an affine scheme has a finite fibre, which is condition `(α)` of Stacks 03JX —
> in particular a decent one. Let `p` be a field-valued point of `X`
> with field of definition `k`, so a commutative diagram `Spec k ⟶ X ⟶ S`. If the image point
> `s` of `Spec k ⟶ S` is a closed point of `S` and the residue field extension `κ(s) ⟶ k` is
> algebraic, then the image of `Spec k ⟶ X` is a closed point of `|X|`.

```lean
theorem isClosed_singleton_class_of_isAlgebraic_residueField
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdecent : HasFiniteChartFibersAtEveryPoint B S hS X)
    (p : FieldValuedPoint B S hS X)
    (hclosed : IsClosed ({(S.SpecToEquivOfField p.carrier p.toBase).1} : Set S))
    (halg : letI := (S.SpecToEquivOfField p.carrier p.toBase).2.hom.toAlgebra
      Algebra.IsAlgebraic
        (S.residueField (S.SpecToEquivOfField p.carrier p.toBase).1) p.carrier) :
    IsClosed ({p.class B S hS X} : Set (points B S hS X))
```

## Tag 08AL, a lemma

[Tag 08AL](https://stacks.math.columbia.edu/tag/08AL) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_fieldMorphism_of_moduleFinite_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteFieldValuedPoint.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteFieldValuedPoint.lean#L313). The attribute's comment: “finite morphism”.

> **Stacks 08AL, the finite case.** Let `X` be a decent algebraic space over a scheme `S` and
> let `p` be a field-valued point of `X` with field of definition `k`, so a commutative diagram
> `Spec k ⟶ X ⟶ S`. If the image point `s` of `Spec k ⟶ S` is a closed point of `S` and `k` is
> finite over the residue field `κ(s)`, then `Spec k ⟶ X` is a finite morphism.

```lean
theorem isFinite_fieldMorphism_of_moduleFinite_residueField (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (p : FieldValuedPoint B S hS X)
    (hs : IsClosed ({(S.SpecToEquivOfField p.carrier p.toBase).1} : Set S))
    (hfin : letI := (S.SpecToEquivOfField p.carrier p.toBase).2.hom.toAlgebra
      Module.Finite (S.residueField (S.SpecToEquivOfField p.carrier p.toBase).1) p.carrier) :
    IsFinite B S hS (fieldMorphism B S hS X p)
```

**`AlgebraicGeometry.Space.isClosedImmersion_fieldMorphism_of_isIso_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteFieldValuedPoint.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteFieldValuedPoint.lean#L341). The attribute's comment: “closed immersion”.

> **Stacks 08AL, the closed-immersion case.** Let `X` be a decent algebraic space over a
> scheme `S` and let `p` be a field-valued point of `X` with field of definition `k`, so a
> commutative diagram `Spec k ⟶ X ⟶ S`. If the image point `s` of `Spec k ⟶ S` is a closed point
> of `S` and the residue field embedding `κ(s) ⟶ k` is an isomorphism, then `Spec k ⟶ X` is a
> closed immersion.

```lean
theorem isClosedImmersion_fieldMorphism_of_isIso_residueField (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (p : FieldValuedPoint B S hS X)
    (hs : IsClosed ({(S.SpecToEquivOfField p.carrier p.toBase).1} : Set S))
    (hrat : IsIso (S.SpecToEquivOfField p.carrier p.toBase).2) :
    IsClosedImmersion B S hS (fieldMorphism B S hS X p)
```

## Tag 0AHB, a lemma

[Tag 0AHB](https://stacks.math.columbia.edu/tag/0AHB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fieldValuedPoint_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ClosedPoints.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ClosedPoints.lean#L504).

> A closed point of a decent algebraic space `X` over a scheme `S` is represented by a closed
> immersion from the spectrum of a field: there is a field-valued point of `X` whose class is the
> given point and whose presenting morphism `Spec k ⟶ X` is a closed immersion.

```lean
theorem exists_fieldValuedPoint_isClosedImmersion
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (x : points B S hS X)
    (hx : IsClosed ({x} : Set (points B S hS X))) :
    ∃ p : FieldValuedPoint B S hS X,
      p.class B S hS X = x ∧ IsClosedImmersion B S hS (fieldMorphism B S hS X p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.14, Tag 047Y](https://stacks.math.columbia.edu/tag/047Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
