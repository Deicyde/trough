---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSeparated_of_isQuasiSeparated_of_discreteValuativeUniqueness, AlgebraicGeometry.Space.isProper_of_isQuasiSeparated_of_discreteValuativeCriterion, AlgebraicGeometry.Space.isSeparated_iff_discreteValuativeUniqueness_of_isCofinal, AlgebraicGeometry.Space.isProper_iff_discreteValuativeCriterion_of_isCofinal, AlgebraicGeometry.Space.isSeparated_iff_completeDiscreteValuativeUniqueness, AlgebraicGeometry.Space.isProper_iff_completeDiscreteValuativeCriterion, AlgebraicGeometry.Space.isSeparated_iff_completeAlgClosedDiscreteValuativeUniqueness, AlgebraicGeometry.Space.isProper_iff_completeAlgClosedDiscreteValuativeCriterion
statement: formalized
proof: formalized
---

# 69.19 Noetherian valuative criterion

Section 69.19 of the Stacks Project, [Tag 0ARI](https://stacks.math.columbia.edu/tag/0ARI). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ARJ, a lemma

[Tag 0ARJ](https://stacks.math.columbia.edu/tag/0ARJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_isQuasiSeparated_of_discreteValuativeUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparated.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeSeparated.lean#L184).

> **Stacks 0ARJ.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally
> Noetherian. If `f` is locally of finite type and quasi-separated, and every valuative square for
> `f` whose valuation ring is a discrete valuation ring admits at most one dotted arrow, then `f`
> is separated.

```lean
theorem isSeparated_of_isQuasiSeparated_of_discreteValuativeUniqueness
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hft : IsLocallyOfFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (hu : ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R → Subsingleton q.Lift) :
    IsSeparated B S hS f
```

## Tag 0ARK, a lemma

[Tag 0ARK](https://stacks.math.columbia.edu/tag/0ARK) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_isQuasiSeparated_of_discreteValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeProper.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeProper.lean#L276).

> **Stacks 0ARK.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y`
> locally Noetherian. If `f` is of finite type and quasi-separated, and every valuative square
> for `f` whose valuation ring is a discrete valuation ring has exactly one dotted arrow, then
> `f` is proper.

```lean
theorem isProper_of_isQuasiSeparated_of_discreteValuativeCriterion
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (hlift : ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      Nonempty q.Lift ∧ Subsingleton q.Lift) :
    IsProper B S hS f
```

## Tag 0ARL, a remark

[Tag 0ARL](https://stacks.math.columbia.edu/tag/0ARL) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_iff_discreteValuativeUniqueness_of_isCofinal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L177). The attribute's comment: “Lemma 69.19.1 (0ARJ) for any class of discrete valuation rings in which every discrete valuation ring has an extension”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is locally of finite type and quasi-separated. Let `P` be a class of discrete valuation
> rings such that every discrete valuation ring has an extension in the class. If every valuative
> square for `f` whose valuation ring is a discrete valuation ring in the class admits at most one
> dotted arrow, then `f` is separated; and conversely.

```lean
theorem isSeparated_iff_discreteValuativeUniqueness_of_isCofinal
    {P : ∀ (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A], Prop}
    (cofinal : IsCofinalDiscreteValuationRingClass B P)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsLocallyOfFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsSeparated B S hS f ↔
      ∀ q : ValuativeSquare f, ∀ _ : IsDiscreteValuationRing q.R, P q.R → Subsingleton q.Lift
```

**`AlgebraicGeometry.Space.isProper_iff_discreteValuativeCriterion_of_isCofinal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L202). The attribute's comment: “Lemma 69.19.2 (0ARK) for any class of discrete valuation rings in which every discrete valuation ring has an extension”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is of finite type and quasi-separated. Let `P` be a class of discrete valuation rings
> such that every discrete valuation ring has an extension in the class. If for every valuative
> square for `f` whose valuation ring `A` is a discrete valuation ring in the class there is an
> extension `A ⊂ A'` of discrete valuation rings in the class, inducing an extension of fraction
> fields, over which the square has exactly one dotted arrow `Spec A' ⟶ X`, then `f` is proper; and
> conversely.

```lean
theorem isProper_iff_discreteValuativeCriterion_of_isCofinal
    {P : ∀ (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A], Prop}
    (cofinal : IsCofinalDiscreteValuationRingClass B P)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔ ∀ q : ValuativeSquare f, ∀ _ : IsDiscreteValuationRing q.R, P q.R →
      ∃ e : q.DominatingExtension, ∃ _ : IsDiscreteValuationRing e.square.R, P e.square.R ∧
        Nonempty e.square.Lift ∧ Subsingleton e.square.Lift
```

**`AlgebraicGeometry.Space.isSeparated_iff_completeDiscreteValuativeUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L235). The attribute's comment: “Lemma 69.19.1 (0ARJ) with complete discrete valuation rings”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is locally of finite type and quasi-separated. If every valuative square for `f` whose
> valuation ring is a complete discrete valuation ring admits at most one dotted arrow, then `f` is
> separated; and conversely.

```lean
theorem isSeparated_iff_completeDiscreteValuativeUniqueness
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsLocallyOfFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsSeparated B S hS f ↔ ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      IsAdicComplete (IsLocalRing.maximalIdeal q.R) q.R → Subsingleton q.Lift
```

**`AlgebraicGeometry.Space.isProper_iff_completeDiscreteValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L252). The attribute's comment: “Lemma 69.19.2 (0ARK) with complete discrete valuation rings”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is of finite type and quasi-separated. If for every valuative square for `f` whose
> valuation ring `A` is a complete discrete valuation ring, with fraction field `K`, there is an
> extension `A ⊂ A'` of complete discrete valuation rings inducing an extension `K ⊂ K'` of fraction
> fields over which the square has exactly one dotted arrow `Spec A' ⟶ X`, then `f` is proper; and
> conversely.

```lean
theorem isProper_iff_completeDiscreteValuativeCriterion
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔ ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      IsAdicComplete (IsLocalRing.maximalIdeal q.R) q.R →
      ∃ e : q.DominatingExtension, IsDiscreteValuationRing e.square.R ∧
        IsAdicComplete (IsLocalRing.maximalIdeal e.square.R) e.square.R ∧
        Nonempty e.square.Lift ∧ Subsingleton e.square.Lift
```

**`AlgebraicGeometry.Space.isSeparated_iff_completeAlgClosedDiscreteValuativeUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L273). The attribute's comment: “Lemma 69.19.1 (0ARJ) with complete discrete valuation rings with algebraically closed residue field”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is locally of finite type and quasi-separated. If every valuative square for `f` whose
> valuation ring is a complete discrete valuation ring with algebraically closed residue field admits
> at most one dotted arrow, then `f` is separated; and conversely.

```lean
theorem isSeparated_iff_completeAlgClosedDiscreteValuativeUniqueness
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsLocallyOfFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsSeparated B S hS f ↔ ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      IsAdicComplete (IsLocalRing.maximalIdeal q.R) q.R →
      IsAlgClosed (IsLocalRing.ResidueField q.R) → Subsingleton q.Lift
```

**`AlgebraicGeometry.Space.isProper_iff_completeAlgClosedDiscreteValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianValuativeComplete.lean#L293). The attribute's comment: “Lemma 69.19.2 (0ARK) with complete discrete valuation rings with algebraically closed residue field”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `Y` locally Noetherian, and
> assume `f` is of finite type and quasi-separated. If for every valuative square for `f` whose
> valuation ring `A` is a complete discrete valuation ring with algebraically closed residue field
> there is an extension `A ⊂ A'` of such rings, inducing an extension of fraction fields, over which
> the square has exactly one dotted arrow `Spec A' ⟶ X`, then `f` is proper; and conversely.

```lean
theorem isProper_iff_completeAlgClosedDiscreteValuativeCriterion
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (algX : IsAlgebraicSpace B S hS X)
    (algY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (noethY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (finf : IsFiniteType B S hS f) (qsepf : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔ ∀ q : ValuativeSquare f, IsDiscreteValuationRing q.R →
      IsAdicComplete (IsLocalRing.maximalIdeal q.R) q.R →
      IsAlgClosed (IsLocalRing.ResidueField q.R) →
      ∃ e : q.DominatingExtension, IsDiscreteValuationRing e.square.R ∧
        IsAdicComplete (IsLocalRing.maximalIdeal e.square.R) e.square.R ∧
        IsAlgClosed (IsLocalRing.ResidueField e.square.R) ∧
        Nonempty e.square.Lift ∧ Subsingleton e.square.Lift
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.19, Tag 0ARI](https://stacks.math.columbia.edu/tag/0ARI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
