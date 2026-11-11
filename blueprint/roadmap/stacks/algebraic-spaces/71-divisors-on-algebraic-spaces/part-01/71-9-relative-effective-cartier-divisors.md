---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPullbackDefined_of_isPullback_of_isFlat, AlgebraicGeometry.Space.IsRelativeEffectiveCartierDivisor
statement: formalized
proof: formalized
---

# 71.9 Relative effective Cartier divisors

Section 71.9 of the Stacks Project, [Tag 0EPM](https://stacks.math.columbia.edu/tag/0EPM). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EPN, a lemma

[Tag 0EPN](https://stacks.math.columbia.edu/tag/0EPN) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullbackDefined_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierBaseChange.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierBaseChange.lean#L177).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces and let `D ⊆ X` be an effective Cartier
> divisor whose structure morphism `D ⟶ Y` is flat.  Then for every morphism `g : Y' ⟶ Y` and
> every fibre product square exhibiting `X'` as `Y' ×_Y X`, the pullback of `D` along the
> projection `g' : X' ⟶ X` is defined: the inverse image of `D` on `X'` is again an effective
> Cartier divisor.
>
> Stacks 0EPN asks `g` to be a morphism of schemes and `X'` to be the chosen fibre product; it is
> stated here for an arbitrary morphism of algebraic spaces and an arbitrary cartesian square.

```lean
theorem isPullbackDefined_of_isPullback_of_isFlat {X Y Y' X' : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y' ⟶ Y) {f' : X' ⟶ Y'} {g' : X' ⟶ X} (hsq : IsPullback f' g' g f)
    (D : ClosedSubspaces B S hS X.1) (hD : IsEffectiveCartierDivisor B S hS X D)
    (hflat : IsFlat B S hS (D.1.ι ≫ f.hom)) :
    IsPullbackDefined B S hS g' D
```

## Tag 0EPP, a definition

[Tag 0EPP](https://stacks.math.columbia.edu/tag/0EPP) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeEffectiveCartierDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L146).

> A closed subspace `D ⊆ X` is a *relative effective Cartier divisor* on `X` over `Y`, for a
> morphism `f : X ⟶ Y` of algebraic spaces, when `D` is an effective Cartier divisor on `X` and the
> structure morphism `D ⟶ Y` is flat.

```lean
noncomputable abbrev IsRelativeEffectiveCartierDivisor {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (D : ClosedSubspaces B S hS X.1) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.9, Tag 0EPM](https://stacks.math.columbia.edu/tag/0EPM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
