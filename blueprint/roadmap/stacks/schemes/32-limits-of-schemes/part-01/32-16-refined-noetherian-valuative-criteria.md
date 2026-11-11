---
declaration: section
origin: cited
lean: AlgebraicGeometry.isProper_of_denseRange_of_exists_discreteLift, AlgebraicGeometry.isSeparated_of_denseRange_of_subsingleton_discreteLift, AlgebraicGeometry.isProper_of_denseRange_of_unique_discreteLift
statement: formalized
proof: formalized
---

# 32.16 Refined Noetherian valuative criteria

Section 32.16 of the Stacks Project, [Tag 0H1P](https://stacks.math.columbia.edu/tag/0H1P). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CM3, a lemma

[Tag 0CM3](https://stacks.math.columbia.edu/tag/0CM3) in the Stacks Project.

**`AlgebraicGeometry.isProper_of_denseRange_of_exists_discreteLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean#L369). References: EGA II (7.3.8), “(b)⇒(a)”; EGA IV (15.7.5), “c⇒a”; EGA IV (18.10.20), “partial”.

> **Stacks Project, Tag 0CM3.** Let `f : X ⟶ S` and `h : U ⟶ X` be morphisms of schemes with
> `S` locally Noetherian, `f` and `h` of finite type, `f` separated and `h(U)` dense in `X`. If
> every commutative solid diagram with `Spec(K) ⟶ U ⟶ X` along the top and `Spec(A) ⟶ S` along the
> bottom, where `A` is a discrete valuation ring with field of fractions `K`, admits a dotted arrow
> `Spec(A) ⟶ X` making it commute, then `f` is proper.
>
> This is `isProper_of_exists_discreteLift_of_denseRange` with its hypothesis `h0208` discharged by
> `isProper_of_genericDiscreteValuativeCriterion'`.

```lean
theorem isProper_of_denseRange_of_exists_discreteLift
    {U X S : Scheme.{u}} (h : U ⟶ X) (f : X ⟶ S)
    [IsLocallyNoetherian S]
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [LocallyOfFiniteType h] [QuasiCompact h] (hdense : DenseRange h)
    (hvaluative : ∀ (D : ValuativeCommSq f) (_ : IsDiscreteValuationRing D.R)
      (g : Spec (.of D.K) ⟶ U), g ≫ h = D.i₁ → D.commSq.HasLift) :
    IsProper f
```

## Tag 0CM4, a lemma

[Tag 0CM4](https://stacks.math.columbia.edu/tag/0CM4) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_of_denseRange_of_subsingleton_discreteLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean#L450).

> **Stacks Project, Tag 0CM4.** Let `f : X ⟶ S` be locally of finite type with `S` locally
> Noetherian, and let `h : U ⟶ X` be of finite type with `h(U)` dense in `X`. If every valuative
> diagram for `f` over a discrete valuation ring whose generic arrow factors through `h` has at
> most one dotted arrow, then `f` is separated.

```lean
theorem isSeparated_of_denseRange_of_subsingleton_discreteLift
    {U X S : Scheme.{u}} (h : U ⟶ X) (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f]
    [LocallyOfFiniteType h] [QuasiCompact h] (hdense : DenseRange h)
    (hvaluative : ∀ (D : ValuativeCommSq f) (_ : IsDiscreteValuationRing D.R)
      (g : Spec (.of D.K) ⟶ U), g ≫ h = D.i₁ → Subsingleton D.commSq.LiftStruct) :
    IsSeparated f
```

## Tag 0CM5, a lemma

[Tag 0CM5](https://stacks.math.columbia.edu/tag/0CM5) in the Stacks Project.

**`AlgebraicGeometry.isProper_of_denseRange_of_unique_discreteLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/RefinedProperness.lean#L572). References: EGA II (7.3.8), “(b)⇒(a)”.

> **Stacks Project, Tag 0CM5.** Let `f : X ⟶ S` and `h : U ⟶ X` be of finite type with `S`
> locally Noetherian and `h(U)` dense in `X`. If every valuative diagram for `f` over a discrete
> valuation ring whose generic arrow factors through `h` has a unique dotted arrow, then `f` is
> proper.
>
> There is no separatedness hypothesis on `f`: separatedness is what the uniqueness of the dotted
> arrow buys, through Stacks 0CM4.

```lean
theorem isProper_of_denseRange_of_unique_discreteLift
    {U X S : Scheme.{u}} (h : U ⟶ X) (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [QuasiCompact f]
    [LocallyOfFiniteType h] [QuasiCompact h] (hdense : DenseRange h)
    (hvaluative : ∀ (D : ValuativeCommSq f) (_ : IsDiscreteValuationRing D.R)
      (g : Spec (.of D.K) ⟶ U), g ≫ h = D.i₁ → Nonempty (Unique D.commSq.LiftStruct)) :
    IsProper f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.16, Tag 0H1P](https://stacks.math.columbia.edu/tag/0H1P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
