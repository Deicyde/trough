---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsFormalModification, AlgebraicGeometry.FormalSpace.artinConditions_comparison, AlgebraicGeometry.FormalSpace.isFormalModification_of_factorsAdicCompleteDvrPoints, AlgebraicGeometry.FormalSpace.isFormalModification_completionSheafMap, AlgebraicGeometry.FormalSpace.isFormalModification_pullback_snd_of_isAdicMorphism
statement: formalized
proof: formalized
---

# 88.24 Formal modifications

Section 88.24 of the Stacks Project, [Tag 0GDJ](https://stacks.math.columbia.edu/tag/0GDJ). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GDK, a definition

[Tag 0GDK](https://stacks.math.columbia.edu/tag/0GDK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsFormalModification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L323).

> **Stacks 0GDK.** A morphism `f : X ⟶ Y` of locally Noetherian formal algebraic spaces over
> `S` is a *formal modification* when (1) `f` is proper, (2) `f` is rig-étale, (3) `f` is
> rig-surjective, and (4) the relative diagonal `Δ_f : X ⟶ X ×_Y X` is rig-surjective. The
> hypothesis that `X` and `Y` be locally Noetherian formal algebraic spaces is recorded in the
> first two fields, so the condition is stated for an arbitrary morphism of fppf sheaves on the
> big fppf site of `S`.

```lean
structure IsFormalModification {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GDL, a remark

[Tag 0GDL](https://stacks.math.columbia.edu/tag/0GDL) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.artinConditions_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationArtinComparison.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationArtinComparison.lean#L249).

> **Stacks 0GDL.** Let `f : X ⟶ Y` be a proper morphism of locally Noetherian formal
> algebraic spaces over `S`, and compare the conditions of Artin's Definition 1.7 of a formal
> modification — (i) the Jacobian and the Cramer ideal of `f` each contain an ideal of definition
> of `X`, (ii) the ideal of the relative diagonal `Δ_f : X ⟶ X ×_Y X` is annihilated by an ideal
> of definition of `X ×_Y X`, (iii) every adic morphism `Spf R ⟶ Y` with `R` a complete discrete
> valuation ring lifts to `X` — with those of Definition 0GDK:
>
> * Ad (i): condition (i) holds if and only if `f` is rig-étale;
> * Ad (ii): if `f` is rig-étale, then `Δ_f` is rig-étale, and condition (ii) holds if and only
>   if `Δ_f` is rig-surjective;
> * Ad (iii): if conditions (i) and (ii) hold, condition (iii) holds if and only if `f` is
>   rig-surjective.
>
> Conditions (i) and (ii) are read on the affine étale charts of `f` and of `X ×_Y X`, as
> `AlgebraicGeometry.FormalSpace.HasJacobianCramerIdealOfDefinition` and
> `AlgebraicGeometry.FormalSpace.HasAnnihilatedKerOnPullbackCharts`.

```lean
theorem artinConditions_comparison {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hproper : IsProper B S hS f) :
    (HasJacobianCramerIdealOfDefinition B S hS f ↔ IsRigEtale B S hS f) ∧
      (IsRigEtale B S hS f →
        IsRigEtale B S hS (pullback.diagonal f) ∧
          (HasAnnihilatedKerOnPullbackCharts B S hS (pullback.diagonal f) ↔
            IsRigSurjective B S hS (pullback.diagonal f))) ∧
      (HasJacobianCramerIdealOfDefinition B S hS f →
        HasAnnihilatedKerOnPullbackCharts B S hS (pullback.diagonal f) →
          (FactorsAdicCompleteDvrPoints B S hS f ↔ IsRigSurjective B S hS f))
```

**`AlgebraicGeometry.FormalSpace.isFormalModification_of_factorsAdicCompleteDvrPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationArtinConditions.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationArtinConditions.lean#L115). The attribute's comment: “the implication of Ad (iii) that needs no further input: Artin's condition (iii), a lift of every adic point over the complete discrete valuation ring itself, implies rig-surjectivity, which asks only for a lift over an extension of that ring. Together with the remaining conditions of Artin's Definition 1.7 in the translated form the remark gives them — properness, rig-étaleness for condition (i) by Ad (i), and rig-surjectivity of the relative diagonal for condition (ii) by Ad (ii) — this is the comparison with Definition 0GDK. Not covered: the converse implication of Ad (iii), which the remark obtains from Stacks 0GDA; the two implications of Ad (ii), which it obtains from Stacks 0GD1, Stacks 0GD3 and Stacks 0GD6; and Ad (i), whose equivalence of condition (i) with rig-étaleness is part (7) of Lemma 0AJU, that is Stacks 0AJY, and whose Cramer and Jacobian ideals of a morphism of formal algebraic spaces this library does not have”.

> **Stacks 0GDL.** Let `f : X ⟶ Y` be a proper rig-étale morphism of locally Noetherian
> formal algebraic spaces over `S` whose relative diagonal `Δ_f : X ⟶ X ×_Y X` is rig-surjective.
> If every adic morphism `Spf R ⟶ Y` with `R` a complete discrete valuation ring factors through
> `f` over `R` itself, then `f` is a formal modification in the sense of Definition 0GDK: such a
> factorisation is in particular one over the trivial extension of `R`, so `f` is
> rig-surjective.

```lean
theorem isFormalModification_of_factorsAdicCompleteDvrPoints {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hproper : IsProper B S hS f) (hetale : IsRigEtale B S hS f)
    (hdiagSurj : IsRigSurjective B S hS (pullback.diagonal f))
    (hlift : FactorsAdicCompleteDvrPoints B S hS f) :
    IsFormalModification B S hS f
```

## Tag 0GDM, a lemma

[Tag 0GDM](https://stacks.math.columbia.edu/tag/0GDM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalModification_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalModification.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalModification.lean#L52).

> **Stacks 0GDM.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S`, let `T ⊆ |X|`
> be closed and let `U ⊆ X` be the open subspace with `|U| = |X| ∖ T`. If `X` is locally
> Noetherian, `f` is proper and `U' = f⁻¹U ⟶ U` is an isomorphism, then
> `f_{/T} : X'_{/T'} ⟶ X_{/T}` is a formal modification.

```lean
theorem isFormalModification_completionSheafMap {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X) (f : X' ⟶ X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) (hf : Space.IsProper B S hS f)
    (hfU : IsIso (pullback.snd f (Space.openSubspaceOfPoints B S hS X Tᶜ).ι)) :
    IsFormalModification B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GDN, a lemma

[Tag 0GDN](https://stacks.math.columbia.edu/tag/0GDN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalModification_pullback_snd_of_isAdicMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationBaseChangeAdic.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationBaseChangeAdic.lean#L130).

> **Stacks 0GDN.** Let `f : X ⟶ Y` be a morphism of locally Noetherian formal algebraic spaces
> over `S` which is a formal modification. Then for any adic morphism `g : Z ⟶ Y` of locally
> Noetherian formal algebraic spaces, the base change `X ×_Y Z ⟶ Z` is a formal modification.
>
> The fibre product is locally Noetherian by
> `AlgebraicGeometry.FormalSpace.isLocallyNoetherian_pullback_of_isRigEtale`; properness is
> Stacks 0GBT, rig-étaleness Stacks 0GD1, and the rig-surjectivity of the base change and of its
> diagonal Stacks 0AQS, the diagonal being the base change of `Δ_f` along the adic comparison
> morphism `X' ×_Z X' ⟶ X ×_Y X` of `AlgebraicGeometry.FormalSpace.isPullback_selfPullbackMap`.
> No hypothesis beyond those of the source is made: `g` is adic in the sense of Definition 0AQ3,
> and neither `g` nor `Δ_f` is assumed locally of finite type.

```lean
theorem isFormalModification_pullback_snd_of_isAdicMorphism {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hZ : IsLocallyNoetherian B S hS Z)
    (hg : IsAdicMorphism B S hS g) (hf : IsFormalModification B S hS f) :
    IsFormalModification B S hS (pullback.snd f g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.24, Tag 0GDJ](https://stacks.math.columbia.edu/tag/0GDJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
