---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_isReduction_of_isAffineFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.reduction, AlgebraicGeometry.FormalSpace.exists_isReduction_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.isReduction_formalSpectrum, TopologicalRing.isWeakIdealOfDefinition_topologicalNilradical, TopologicalRing.topologicalNilradical_isRadical, AlgebraicGeometry.FormalSpace.isReduction_pullback_reduction_of_smooth, AlgebraicGeometry.FormalSpace.isIso_of_isReduction_of_isPullback_of_smooth
statement: formalized
proof: formalized
---

# 87.12 The reduction

Section 87.12 of the Stacks Project, [Tag 0GB5](https://stacks.math.columbia.edu/tag/0GB5). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AIN, a lemma

[Tag 0AIN](https://stacks.math.columbia.edu/tag/0AIN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isReduction_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineReduction.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineReduction.lean#L317). The attribute's comment: “affine formal algebraic spaces”.

> **Stacks 0AIN** for an affine formal algebraic space. Let `X` be an affine formal algebraic
> space over `S`. There is a reduced algebraic space `Xred` and a representable morphism
> `Xred ⟶ X` which is a thickening and through which every morphism to `X` from a reduced
> algebraic space factors uniquely.

```lean
theorem exists_isReduction_of_isAffineFormalAlgebraicSpace
    (X : FppfSheaf B S hS) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    ∃ (Xred : FppfSheaf B S hS) (i : Xred ⟶ X), IsReduction B S hS X Xred i
```

**`AlgebraicGeometry.FormalSpace.reduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/GeneralReduction.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/GeneralReduction.lean#L275). The attribute's comment: “general formal algebraic spaces, as a chosen datum”.

> **Stacks 0AIN for a general formal algebraic space, as a construction.** The chosen
> reduction of a formal algebraic space over `S`, in the bundled shape the étale sites of
> Stacks 0DEA consume.

```lean
noncomputable def reduction (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    Reduction B S hS X
```

**`AlgebraicGeometry.FormalSpace.exists_isReduction_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionExistence.lean, line 1299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionExistence.lean#L1299). The attribute's comment: “a general formal algebraic space”.

> Let `X` be a formal algebraic space over `S`. There exists a reduced algebraic space `X_red`
> and a representable morphism `X_red ⟶ X` which is a thickening, and a morphism `U ⟶ X` with `U`
> a reduced algebraic space factors uniquely through `X_red`.

```lean
theorem exists_isReduction_of_isFormalAlgebraicSpace
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    ∃ (Xred : FppfSheaf B S hS) (i : Xred ⟶ X), IsReduction B S hS X Xred i
```

## Tag 0GB6, an example

[Tag 0GB6](https://stacks.math.columbia.edu/tag/0GB6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isReduction_formalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean#L458). The attribute's comment: “the reduction”.

> **Stacks 0GB6.** Let `A` be a weakly admissible topological ring over `S` and let `𝔞` be
> its ideal of topologically nilpotent elements, the largest weak ideal of definition of `A`.
> The stage of `Spf A` at `𝔞` is `Spec (A ⧸ 𝔞)`, and its morphism to `Spf A` exhibits it as the
> reduction of `Spf A`.

```lean
public theorem isReduction_formalSpectrum
    {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] (hA : TopologicalRing.IsWeaklyAdmissible A)
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : QuotientSystem B S hS A) (_hB : D.HasLargeSite) :
    IsReduction B S hS (formalSpectrum D)
      ((formalSpectrumDiagram D).obj (OrderDual.toDual (TopologicalRing.nilIdx hA.1)))
      (formalSpectrumInclusion D (OrderDual.toDual (TopologicalRing.nilIdx hA.1)))
```

Declarations registered for the tag:

- [`TopologicalRing.isWeakIdealOfDefinition_topologicalNilradical`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FiniteTypeOnReductionsIsLocal.lean#L134), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean#L94) (StacksFrontier): “the open ideal”.
- [`TopologicalRing.topologicalNilradical_isRadical`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L130), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumReduction.lean#L97) (StacksFrontier): “radicality”.

## Tag 0GB7, a lemma

[Tag 0GB7](https://stacks.math.columbia.edu/tag/0GB7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isReduction_pullback_reduction_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean#L212). The attribute's comment: “the fibre product X ×\_Y Y\_red is a reduction of X; read against given reductions and a given fibre product rather than chosen ones, exactly as for Stacks 0GB8. Stacks 0AIN supplies the reductions”.

> **Stacks 0GB7.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which is
> representable by algebraic spaces and smooth, let `iY : Yred ⟶ Y` be a reduction of `Y` and let
> `P` with projections `fst : P ⟶ X` and `snd : P ⟶ Yred` be a fibre product `X ×_Y Yred`. Then
> `P`, with the projection `fst`, is a reduction of `X`: this is the assertion
> `X_red = X ×_Y Y_red`.
>
> `P` is an algebraic space by Stacks 03XY, reduced by Stacks 0GB3 applied to the base change
> `snd` of `f`, and `fst` is a representable thickening because `iY` is; a morphism to `X` from a
> reduced algebraic space factors uniquely through `P` because its composite with `f` factors
> uniquely through `Yred`.

```lean
theorem isReduction_pullback_reduction_of_smooth {X Y Yred P : FppfSheaf B S hS}
    (_hX : IsFormalAlgebraicSpace B S hS X) (_hY : IsFormalAlgebraicSpace B S hS Y)
    {f : X ⟶ Y} (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsmooth : Space.HasPropertyULift.{u + 1} B S hS
      (Space.smoothPropertyULift.{u + 1} B S hS) f.hom hf)
    {iY : Yred ⟶ Y} (hiY : IsReduction B S hS Y Yred iY)
    {fst : P ⟶ X} {snd : P ⟶ Yred} (sq : IsPullback fst snd f iY) :
    IsReduction B S hS X P fst
```

**`AlgebraicGeometry.FormalSpace.isIso_of_isReduction_of_isPullback_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean#L258). The attribute's comment: “the comparison morphism X\_red ⟶ X ×\_Y Y\_red over X is an isomorphism; read against given reductions and a given fibre product rather than chosen ones, exactly as for Stacks 0GB8. Stacks 0AIN supplies the reductions”.

> **Stacks 0GB7.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which is
> representable by algebraic spaces and smooth, let `iX : Xred ⟶ X` and `iY : Yred ⟶ Y` be
> reductions and let `P` with projections `fst` and `snd` be a fibre product `X ×_Y Yred`. Then
> every morphism `Xred ⟶ P` over `X` is an isomorphism: the canonical comparison morphism
> `X_red ⟶ X ×_Y Y_red` identifies the two.
>
> `P` is a reduction of `X` by
> `AlgebraicGeometry.FormalSpace.isReduction_pullback_reduction_of_smooth`, and two reductions of
> `X` are isomorphic over `X`.

```lean
theorem isIso_of_isReduction_of_isPullback_of_smooth {X Y Xred Yred P : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    {f : X ⟶ Y} (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsmooth : Space.HasPropertyULift.{u + 1} B S hS
      (Space.smoothPropertyULift.{u + 1} B S hS) f.hom hf)
    {iX : Xred ⟶ X} (hiX : IsReduction B S hS X Xred iX)
    {iY : Yred ⟶ Y} (hiY : IsReduction B S hS Y Yred iY)
    {fst : P ⟶ X} {snd : P ⟶ Yred} (sq : IsPullback fst snd f iY)
    {g : Xred ⟶ P} (hg : g ≫ fst = iX) : IsIso g
```

## Tag 0GB8, a lemma

[Tag 0GB8](https://stacks.math.columbia.edu/tag/0GB8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyULift_isSurjectiveULift_iff_isSurjectiveULift_red`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Reduction.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Reduction.lean#L260).

> **Stacks 0GB8.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S` which is
> representable by algebraic spaces, let `iX : Xred ⟶ X` and `iY : Yred ⟶ Y` be reductions and let
> `fred : Xred ⟶ Yred` be compatible with `f`. Then `f` is surjective in the sense of Stacks 03XZ
> if and only if `fred` is a surjective morphism of algebraic spaces.

```lean
theorem hasPropertyULift_isSurjectiveULift_iff_isSurjectiveULift_red
    {X Y : FppfSheaf B S hS}
    (_hX : IsFormalAlgebraicSpace B S hS X) (_hY : IsFormalAlgebraicSpace B S hS Y)
    {Xred Yred : FppfSheaf B S hS} {iX : Xred ⟶ X} {iY : Yred ⟶ Y}
    (hiX : IsReduction B S hS X Xred iX) (hiY : IsReduction B S hS Y Yred iY)
    {f : X ⟶ Y} (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    {fred : Xred ⟶ Yred} (hfred : fred ≫ iY = iX ≫ f) :
    Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ g ↦ Space.IsSurjectiveULift.{u + 1} B S hS g.hom) f.hom hf ↔
      Space.IsSurjectiveULift.{u + 1} B S hS fred.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.12, Tag 0GB5](https://stacks.math.columbia.edu/tag/0GB5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
