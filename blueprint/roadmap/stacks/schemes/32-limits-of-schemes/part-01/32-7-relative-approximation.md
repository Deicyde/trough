---
declaration: section
origin: cited
lean: AlgebraicGeometry.LimitFPObjectDescent.exists_isLimit_finiteType_arrow, AlgebraicGeometry.exists_isLimit_finitePresentation, Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation
statement: formalized
proof: formalized
---

# 32.7 Relative approximation

Section 32.7 of the Stacks Project, [Tag 09MU](https://stacks.math.columbia.edu/tag/09MU). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GS1, a lemma

[Tag 0GS1](https://stacks.math.columbia.edu/tag/0GS1) in the Stacks Project.

**`AlgebraicGeometry.LimitFPObjectDescent.exists_isLimit_finiteType_arrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitFPObjectDescent/Approximation.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitFPObjectDescent/Approximation.lean#L459).

> A morphism between quasi-compact and quasi-separated schemes is a limit of morphisms between
> schemes of finite type over `ℤ`, with affine transition morphisms on sources and targets.

```lean
theorem exists_isLimit_finiteType_arrow
    {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace X] [QuasiSeparatedSpace X]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirectedOrder I)
      (D : Iᵒᵖ ⥤ Arrow Scheme.{u}) (c : Cone D),
      (∀ i,
        LocallyOfFiniteType (terminal.from (D.obj i).left) ∧
          QuasiCompact (terminal.from (D.obj i).left)) ∧
      (∀ i,
        LocallyOfFiniteType (terminal.from (D.obj i).right) ∧
          QuasiCompact (terminal.from (D.obj i).right)) ∧
      (∀ {i j : Iᵒᵖ} (g : i ⟶ j),
        IsAffineHom (D.map g).left ∧ IsAffineHom (D.map g).right) ∧
      Nonempty (IsLimit c) ∧ Nonempty (c.pt ≅ Arrow.mk f)
```

## Tag 09MV, a lemma

[Tag 09MV](https://stacks.math.columbia.edu/tag/09MV) in the Stacks Project.

**`AlgebraicGeometry.exists_isLimit_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/Basic.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/Basic.lean#L475).

> **Stacks Project, Tag 09MV.** A quasi-compact and quasi-separated scheme over a
> quasi-separated base is a directed inverse limit of quasi-compact and quasi-separated schemes of
> finite presentation over that base, with affine transition morphisms over the base.

```lean
theorem exists_isLimit_finitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace X] [QuasiSeparatedSpace X] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I)
      (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
      (t : D ⟶ (Functor.const Iᵒᵖ).obj S)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (_ : IsLimit (Cone.mk X p)),
      p ≫ t = (Functor.const Iᵒᵖ).map f ∧
        (∀ i, FinitePresentation (t.app i)) ∧
        (∀ i, CompactSpace (D.obj i) ∧ QuasiSeparatedSpace (D.obj i)) ∧
        ∀ {i j : Iᵒᵖ} (g : i ⟶ j), IsAffineHom (D.map g)
```

## Tag 09YZ, a lemma

[Tag 09YZ](https://stacks.math.columbia.edu/tag/09YZ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwoResidue/Complete.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwoResidue/Complete.lean#L164). The attribute's comment: “an integral morphism over a quasi-compact and quasi-separated base is the limit of a directed inverse system of schemes finite and of finite presentation over that base”.

> **Stacks Project, Tag 09YZ.**  An integral morphism to a quasi-compact and quasi-separated
> scheme exhibits its source as the limit of a directed inverse system of schemes finite and of
> finite presentation over that target.
>
> This is the tag's own proof.  The quasi-coherent algebra `f_* 𝒪_X` ([Stacks, Tag 01LC], here
> `Stacks.AffineAlgebraEquivalence.isQuasicoherent_pushforwardAlgebra`) is integral, part (2) of
> [Stacks, Tag 0817] — `exists_small_index_finite_finitePresentation` above, packaged as
> `integralAlgebraHasFiniteFinitePresentationColimit` — writes it as a filtered colimit of finite,
> finitely presented quasi-coherent `𝒪_S`-algebras, and the relative spectrum turns that colimit
> into the required limit of schemes, with the finiteness and the finite presentation of each stage
> read off its algebra.  That last passage is
> `Stacks.IntegralLimit.nonempty_integralLimitPresentation_of_algebraColimit`, whose only hypothesis
> was part (2).
>
> The base is quasi-compact and quasi-separated, as the tag asks; the affine-base case
> `AlgebraicGeometry.nonempty_integralLimitPresentation_of_isAffine` is strictly weaker and is
> subsumed by this.

```lean
theorem nonempty_integralLimitPresentation {X S : Scheme.{u}} (f : X ⟶ S) [IsIntegralHom f]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    Nonempty (_root_.AlgebraicGeometry.IntegralLimitPresentation f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.7, Tag 09MU](https://stacks.math.columbia.edu/tag/09MU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
