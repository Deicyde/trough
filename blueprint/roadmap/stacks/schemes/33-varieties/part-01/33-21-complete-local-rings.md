---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_no_quotient_mvPowerSeries_algEquiv_completedLocalRing, AlgebraicGeometry.exists_quotient_mvPowerSeries_algEquiv_adicCompletion, AlgebraicGeometry.exists_powerSeries_quotient_ringEquiv_adicCompletion, AlgebraicGeometry.exists_powerSeries_quotient_ringEquiv_adicCompletion_of_isSeparableExtension, AlgebraicGeometry.exists_baseChanged_powerSeries_quotient_algEquiv_adicCompletion
statement: formalized
proof: formalized
---

# 33.21 Complete local rings

Section 33.21 of the Stacks Project, [Tag 0C51](https://stacks.math.columbia.edu/tag/0C51). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C52, a lemma

[Tag 0C52](https://stacks.math.columbia.edu/tag/0C52) in the Stacks Project.

**`AlgebraicGeometry.exists_no_quotient_mvPowerSeries_algEquiv_completedLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/NoBasePresentation.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/NoBasePresentation.lean#L487). The attribute's comment: “presentation\_not\_always\_over\_base\_field”. References: EGA IV (18.11.6), “counterexample”; EGA 0 (19.6.5.2), “not k-iso to K[[T]]”.

> A completed local ring can admit no presentation over its residue field compatible with
> the ground field, even when the scheme is locally Noetherian.

```lean
public theorem exists_no_quotient_mvPowerSeries_algEquiv_completedLocalRing :
    ∃ (k : Type u) (_ : Field k) (X : Scheme.{u})
      (f : X ⟶ Spec (.of k)) (_ : IsLocallyNoetherian X) (x : X),
      letI : Algebra k (X.residueField x) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      letI : Algebra k (Scheme.completedLocalRing X x) :=
        Scheme.completedLocalRingAlgebra f x
      ¬ ∃ (n : ℕ) (I : Ideal (MvPowerSeries (Fin n) (X.residueField x))),
          Nonempty ((MvPowerSeries (Fin n) (X.residueField x) ⧸ I) ≃ₐ[k]
            Scheme.completedLocalRing X x)
```

**`AlgebraicGeometry.exists_quotient_mvPowerSeries_algEquiv_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/SeparablePresentation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/SeparablePresentation.lean#L56). The attribute's comment: “separable\_completed\_local\_ring\_presentation”. References: EGA 0 (19.6.3), “(a) ⇒ (c), special case”; EGA 0 (19.8.8), “(i), special case”.

> If the residue field at a point of a locally Noetherian scheme over `k` is separable over
> `k`, then the completed local ring is a quotient of a formal power series ring over the residue
> field, as a `k`-algebra, and the equivalence induces the identity on residue fields.

```lean
public theorem exists_quotient_mvPowerSeries_algEquiv_adicCompletion
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsLocallyNoetherian X] (x : X) :
    let R := X.presheaf.stalk x
    let κ := X.residueField x
    letI : Algebra k R :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.presheaf.germ ⊤ x (by simp)).hom.toAlgebra
    letI : Algebra k κ :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    Algebra.IsSeparableExtension k κ →
      ∃ (n : ℕ) (I : Ideal (MvPowerSeries (Fin n) κ))
        (hI : I ≤ RingHom.ker
          (MvPowerSeries.constantCoeff : MvPowerSeries (Fin n) κ →+* κ)),
        ∃ e : (MvPowerSeries (Fin n) κ ⧸ I) ≃ₐ[k]
            AdicCompletion (maximalIdeal R) R,
          (AdicCompletion.evalOneₐ (maximalIdeal R)).toRingHom.comp
              e.toRingEquiv.toRingHom =
            Ideal.Quotient.lift I
              (MvPowerSeries.constantCoeff : MvPowerSeries (Fin n) κ →+* κ) hI
```

Declarations registered for the tag:

- [`AlgebraicGeometry.exists_powerSeries_quotient_ringEquiv_adicCompletion`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean#L149), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean#L320) (StacksFrontier): “completed\_local\_ring\_presentation”.

## Tag 0C53, an equation

[Tag 0C53](https://stacks.math.columbia.edu/tag/0C53) in the Stacks Project.

**`AlgebraicGeometry.exists_powerSeries_quotient_ringEquiv_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean#L149). The attribute's comment: “power-series presentation”.

> The completed local ring at a point of a locally Noetherian scheme is a quotient of a
> formal power series ring over its residue field, with the presentation inducing the canonical
> identification on residue fields.

```lean
theorem exists_powerSeries_quotient_ringEquiv_adicCompletion
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsLocallyNoetherian X] (x : X) :
    ∃ (n : ℕ) (I : Ideal (MvPowerSeries (Fin n) (X.residueField x)))
      (e : (MvPowerSeries (Fin n) (X.residueField x) ⧸ I) ≃+*
        AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)),
      ∀ a : X.residueField x,
        residue (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
            (X.presheaf.stalk x))
            (e (Ideal.Quotient.mk I (MvPowerSeries.C a))) =
          IsLocalRing.ResidueField.map
            (algebraMap (X.presheaf.stalk x)
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
                (X.presheaf.stalk x))) a
```

**`AlgebraicGeometry.exists_powerSeries_quotient_ringEquiv_adicCompletion_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CompleteLocal/PowerSeriesPresentation.lean#L197). The attribute's comment: “separable ground-field compatibility: separability is Stacks 030O (`Algebra.IsSeparableExtension`), and the `k`-algebra compatibility is stated as equality on elements of `k`”.

> If the residue field at the point is separable over the ground field, in the sense of
> Stacks 030O (`Algebra.IsSeparableExtension`, which allows transcendental extensions), the
> power-series presentation of the completed local ring can be chosen to respect the ground-field
> maps, that is, to be an isomorphism of `k`-algebras inducing the identity on residue fields.

```lean
theorem exists_powerSeries_quotient_ringEquiv_adicCompletion_of_isSeparableExtension
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsLocallyNoetherian X] (x : X)
    (hsep :
      let kToStalk : k →+* X.presheaf.stalk x :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.presheaf.germ ⊤ x trivial).hom
      letI : Algebra k (X.residueField x) :=
        ((X.residue x).hom.comp kToStalk).toAlgebra
      Algebra.IsSeparableExtension k (X.residueField x)) :
    let kToStalk : k →+* X.presheaf.stalk x :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.presheaf.germ ⊤ x trivial).hom
    let kToResidue : k →+* X.residueField x := (X.residue x).hom.comp kToStalk
    ∃ (n : ℕ) (I : Ideal (MvPowerSeries (Fin n) (X.residueField x)))
      (e : (MvPowerSeries (Fin n) (X.residueField x) ⧸ I) ≃+*
        AdicCompletion (maximalIdeal (X.presheaf.stalk x)) (X.presheaf.stalk x)),
      (∀ a : X.residueField x,
        residue (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
            (X.presheaf.stalk x))
            (e (Ideal.Quotient.mk I (MvPowerSeries.C a))) =
          IsLocalRing.ResidueField.map
            (algebraMap (X.presheaf.stalk x)
              (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
                (X.presheaf.stalk x))) a) ∧
      (∀ a : k,
        e (Ideal.Quotient.mk I (MvPowerSeries.C (kToResidue a))) =
          algebraMap (X.presheaf.stalk x)
            (AdicCompletion (maximalIdeal (X.presheaf.stalk x))
              (X.presheaf.stalk x)) (kToStalk a))
```

## Tag 0C54, a lemma

[Tag 0C54](https://stacks.math.columbia.edu/tag/0C54) in the Stacks Project.

**`AlgebraicGeometry.exists_baseChanged_powerSeries_quotient_algEquiv_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/CompletedLocalRingFieldChange.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/SmoothOverField/CompletedLocalRingFieldChange.lean#L525).

> A power-series presentation of a completed local ring over `k` gives, after extending
> scalars to `K`, the presentation by the same equations over the residue field upstairs.

```lean
theorem exists_baseChanged_powerSeries_quotient_algEquiv_adicCompletion
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hdim :
      ringKrullDim
          (X.presheaf.stalk
            ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)) =
        ringKrullDim
          ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).presheaf.stalk y))
    (hsep :
      let x :=
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y
      letI : Algebra k (X.residueField x) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      Algebra.IsSeparableExtension k (X.residueField x))
    (n : ℕ)
    (I : Ideal
      (MvPowerSeries (Fin n)
        (X.residueField
          ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y))))
    (hI : I ≤ RingHom.ker
      (MvPowerSeries.constantCoeff :
        MvPowerSeries (Fin n)
            (X.residueField
              ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)) →+*
          X.residueField
            ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)))
    (e :
      let x :=
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y
      let R := X.presheaf.stalk x
      let κ := X.residueField x
      letI : Algebra k R :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.presheaf.germ ⊤ x (by simp)).hom.toAlgebra
      letI : Algebra k κ :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      (MvPowerSeries (Fin n) κ ⧸ I) ≃ₐ[k]
        AdicCompletion (maximalIdeal R) R)
    (he :
      let x :=
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y
      let R := X.presheaf.stalk x
      let κ := X.residueField x
      letI : Algebra k R :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.presheaf.germ ⊤ x (by simp)).hom.toAlgebra
      letI : Algebra k κ :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      (AdicCompletion.evalOneₐ (maximalIdeal R)).toRingHom.comp
          e.toRingEquiv.toRingHom =
        Ideal.Quotient.lift I
          (MvPowerSeries.constantCoeff : MvPowerSeries (Fin n) κ →+* κ) hI) :
    let Y := pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let p : Y ⟶ X := pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let g : Y ⟶ Spec (.of K) := pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let x := p.base y
    let RY := Y.presheaf.stalk y
    let κy := Y.residueField y
    let κMap : X.residueField x →+* κy := (p.residueFieldMap y).hom
    let J : Ideal (MvPowerSeries (Fin n) κy) := I.map (MvPowerSeries.map κMap)
    let : Algebra K RY :=
      ((Scheme.ΓSpecIso (.of K)).inv ≫ g.appTop ≫ Y.presheaf.germ ⊤ y (by simp)).hom.toAlgebra
    let : Algebra K κy :=
      ((Scheme.ΓSpecIso (.of K)).inv ≫ g.appTop ≫ Y.Γevaluation y).hom.toAlgebra
    ∃ (hJ : J ≤ RingHom.ker
        (MvPowerSeries.constantCoeff : MvPowerSeries (Fin n) κy →+* κy))
      (eY : (MvPowerSeries (Fin n) κy ⧸ J) ≃ₐ[K]
        AdicCompletion (maximalIdeal RY) RY),
      (AdicCompletion.evalOneₐ (maximalIdeal RY)).toRingHom.comp
          eY.toRingEquiv.toRingHom =
        Ideal.Quotient.lift J
          (MvPowerSeries.constantCoeff : MvPowerSeries (Fin n) κy →+* κy) hJ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.21, Tag 0C51](https://stacks.math.columbia.edu/tag/0C51)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
