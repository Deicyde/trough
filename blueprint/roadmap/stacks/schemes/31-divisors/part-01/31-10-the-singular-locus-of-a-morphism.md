---
declaration: section
origin: cited
lean: AlgebraicGeometry.fittingIdeal_relativeDifferentials_comap, Stacks.Discriminant.range_kaehlerDifferent_subschemeι, AlgebraicGeometry.mem_fittingIdeal_relativeDifferentials_iff_not_smoothAt, AlgebraicGeometry.range_subschemeι_fittingIdeal_relativeDifferentials
statement: formalized
proof: formalized
---

# 31.10 The singular locus of a morphism

Section 31.10 of the Stacks Project, [Tag 0C3H](https://stacks.math.columbia.edu/tag/0C3H). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C3I, a lemma

[Tag 0C3I](https://stacks.math.columbia.edu/tag/0C3I) in the Stacks Project.

**`AlgebraicGeometry.fittingIdeal_relativeDifferentials_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdealsDifferentials.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/FittingIdealsDifferentials.lean#L44). References: SGA 7 VI (5.3), “(1)”.

> For a cartesian square of schemes with right edge `f : X ⟶ S` locally of finite type, left
> edge `f' : X' ⟶ S'` and top edge `g' : X' ⟶ X`, the inverse image along `g'` of the `r`-th
> Fitting ideal sheaf of `Ω_{X/S}` is the `r`-th Fitting ideal sheaf of `Ω_{X'/S'}`: the closed
> subschemes cut out by the Fitting ideals of the relative differentials commute with arbitrary
> base change.

```lean
public theorem fittingIdeal_relativeDifferentials_comap {X' X S' S : Scheme.{u}} (g' : X' ⟶ X)
    (f' : X' ⟶ S') (f : X ⟶ S) (g : S' ⟶ S) (h : IsPullback g' f' f g)
    [LocallyOfFiniteType f] (r : ℤ) :
    (fittingIdeal (Scheme.Hom.relativeDifferentials f) r).comap g' =
      fittingIdeal (Scheme.Hom.relativeDifferentials f') r
```

## Tag 0C3J, a lemma

[Tag 0C3J](https://stacks.math.columbia.edu/tag/0C3J) in the Stacks Project.

**`Stacks.Discriminant.range_kaehlerDifferent_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/UnramifiedLocus.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/KaehlerDifferent/UnramifiedLocus.lean#L88).

> **Stacks Project, Tag 0BVY** and **Stacks Project, Tag 0C3J.** For a morphism of schemes
> `f : Y ⟶ X` locally of finite type, the closed subscheme `R ⊆ Y` cut out by the Kähler different
> of `f` — equivalently, by the zeroth Fitting ideal of `Ω_{Y/X}`, which is what the Kähler
> different is — has as its underlying subset of `Y` exactly the set of points at which `f` is not
> unramified.

```lean
theorem range_kaehlerDifferent_subschemeι {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] :
    Set.range (kaehlerDifferent f).subschemeι = {y : Y | ¬ UnramifiedAt f y}
```

## Tag 0C3K, a lemma

[Tag 0C3K](https://stacks.math.columbia.edu/tag/0C3K) in the Stacks Project.

**`AlgebraicGeometry.mem_fittingIdeal_relativeDifferentials_iff_not_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/SingularLocus.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/SingularLocus.lean#L551). The attribute's comment: “pointwise characterisation of the nonsmooth locus”.

> **The nonsmooth locus is cut out by the `d`-th Fitting ideal of the relative
> differentials.** For `f : X ⟶ S` flat and locally of finite presentation whose nonempty fibres
> are all equidimensional of dimension `d`, a point of `X` lies in the closed subscheme defined by
> the `d`-th Fitting ideal of `Ω_{X/S}` exactly when `f` is not smooth at that point.

```lean
theorem mem_fittingIdeal_relativeDifferentials_iff_not_smoothAt
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (d : ℕ)
    (hd : ∀ s : S, Nonempty (f.fiber s) →
      (TopologicalSpace.Equidimensional (f.fiber s) ∧
        topologicalKrullDim (f.fiber s) = (d : WithBot ℕ∞)))
    (x : X) :
    x ∈ Set.range
      (fittingIdeal (Scheme.Hom.relativeDifferentials f) (d : ℤ)).subschemeι ↔
      ¬ InfinitesimalLifting.SmoothAt f x
```

**`AlgebraicGeometry.range_subschemeι_fittingIdeal_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/SingularLocus.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/FittingIdeals/SingularLocus.lean#L592).

> **The closed subscheme cut out by the `d`-th Fitting ideal of `Ω_{X/S}` is the nonsmooth
> locus.** For `f : X ⟶ S` flat and locally of finite presentation whose nonempty fibres are all
> equidimensional of dimension `d`, that closed subscheme has as its underlying subset of `X`
> exactly the set of points at which `f` is not smooth.

```lean
theorem range_subschemeι_fittingIdeal_relativeDifferentials
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (d : ℕ)
    (hd : ∀ s : S, Nonempty (f.fiber s) →
      (TopologicalSpace.Equidimensional (f.fiber s) ∧
        topologicalKrullDim (f.fiber s) = (d : WithBot ℕ∞))) :
    Set.range (fittingIdeal (Scheme.Hom.relativeDifferentials f) (d : ℤ)).subschemeι =
      {x : X | ¬ InfinitesimalLifting.SmoothAt f x}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.10, Tag 0C3H](https://stacks.math.columbia.edu/tag/0C3H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
