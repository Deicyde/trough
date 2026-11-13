---
declaration: section
origin: cited
lean: Stacks.Chow.exteriorProduct_rationallyEquivalentToZero, Stacks.Intersection.ExteriorProductProjections.exteriorProduct_projections
statement: formalized
proof: formalized
---

# 43.18 Exterior product

Section 43.18 of the Stacks Project, [Tag 0B09](https://stacks.math.columbia.edu/tag/0B09). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B0S, a lemma

[Tag 0B0S](https://stacks.math.columbia.edu/tag/0B0S) in the Stacks Project.

**`Stacks.Chow.exteriorProduct_rationallyEquivalentToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalenceZero.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductRationalEquivalenceZero.lean#L83). The attribute's comment: “over a field, unconditionally”.

> **Stacks 0B0S.** Let `X` and `Y` be schemes locally of finite type over the spectrum of a
> field, let `α` be an `r`-cycle on `X` and let `β` be an `s`-cycle on `Y`. If `α` is rationally
> equivalent to zero, or `β` is, then the exterior product `α × β` is rationally equivalent to
> zero.
>
> Each of the two cases is the corresponding well-definedness clause of Stacks 0FBV. The instances
> of Stacks 02S1 along the projections of the products with a point closure that those clauses use
> are supplied internally by
> `Stacks.Chow.flatPullbackFactorsThroughRationalEquivalenceOnPointClosureFibres_holds`, so nothing
> is assumed here.

```lean
theorem exteriorProduct_rationallyEquivalentToZero (C : ChowSituation.{u}) [Subsingleton C.S]
    [IsIntegral C.S] [JacobsonSpace C.S]
    (hδ : ∀ t : C.S, IsClosed ({t} : Set C.S) → C.dimensionFunction t = 0)
    {X Y : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (g : Y ⟶ C.S)
    [LocallyOfFiniteType g] (r s : ℤ)
    (α : CycleGroup C f r) (β : CycleGroup C g s)
    (h : IsRationallyEquivalentToZero C f r α ∨ IsRationallyEquivalentToZero C g s β) :
    IsRationallyEquivalentToZero C (pullback.fst f g ≫ f) (r + s)
      (exteriorProduct C f g r s α β)
```

## Tag 0B0R, a lemma

[Tag 0B0R](https://stacks.math.columbia.edu/tag/0B0R) in the Stacks Project.

**`Stacks.Intersection.ExteriorProductProjections.exteriorProduct_projections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ExteriorProductIntersection.lean, line 935](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ExteriorProductIntersection.lean#L935).

> **Stacks Project, Tag 0B0R.** Let `X` and `Y` be nonsingular varieties over an algebraically
> closed field `k`, let `α ∈ Z_r(X)` and `β ∈ Z_s(Y)`. Then
>
> 1. `pr_Y^*(β) = [X] × β` and `pr_X^*(α) = α × [Y]`,
> 2. `α × [Y]` and `[X] × β` intersect properly on `X × Y`, and
> 3. `α × β = (α × [Y]) · ([X] × β) = pr_X^*(α) · pr_Y^*(β)` in `Z_{r+s}(X × Y)`.
>
> A variety is `AlgebraicGeometry.IsVariety` over `Spec k` and nonsingular is
> `AlgebraicGeometry.IsRegular`, as in Section 43.3; `dX`, `dY` are the dimensions of `X` and `Y`.
> The product `X × Y` is `pullback sX sY` with structure morphism `pullback.fst sX sY ≫ sX`, and
> `pr_X = pullback.fst sX sY`, `pr_Y = pullback.snd sX sY`; `pr_X^*` and `pr_Y^*` are the flat
> pullbacks of cycles of Tag 02RB along these flat morphisms of relative dimension `dY` and `dX`.
> `[X]` and `[Y]` are the fundamental cycles, `×` is the exterior product of Section 43.16, and
> `·` is the intersection product of Section 43.17 on the nonsingular variety `X × Y`. The cycle
> groups `Z_{dX+s}`, `Z_{s+dX}` (and their analogues) are distinct types carrying the same cycles,
> so the identities are equalities of the underlying algebraic cycles.

```lean
theorem exteriorProduct_projections (hX : IsRegular X) (hY : IsRegular Y) (dX dY : ℕ)
    (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞)) (r s : ℕ)
    (α : CycleGroup (fieldChowSituation k) sX (r : ℤ))
    (β : CycleGroup (fieldChowSituation k) sY (s : ℤ)) :
    -- (1)
    ((flatPullback (fieldChowSituation k) (pullback.fst sX sY ≫ sX) sY (pullback.snd sX sY)
        pullback.condition.symm dX (relativeDimension_pullbackSnd sX sY dX hdX) (s : ℤ) β).1 =
      (exteriorProduct (fieldChowSituation k) sX sY (dX : ℤ) (s : ℤ)
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX (𝟙 X) (dX : ℤ)) β).1 ∧
    (flatPullback (fieldChowSituation k) (pullback.fst sX sY ≫ sX) sX (pullback.fst sX sY) rfl dY
        (relativeDimension_pullbackFst sX sY dY hdY) (r : ℤ) α).1 =
      (exteriorProduct (fieldChowSituation k) sX sY (r : ℤ) (dY : ℤ) α
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sY (𝟙 Y) (dY : ℤ))).1) ∧
    -- (2)
    AlgebraicCycle.IntersectProperly
      (exteriorProduct (fieldChowSituation k) sX sY (r : ℤ) (dY : ℤ) α
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sY (𝟙 Y) (dY : ℤ))).1
      (exteriorProduct (fieldChowSituation k) sX sY (dX : ℤ) (s : ℤ)
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX (𝟙 X) (dX : ℤ)) β).1 ∧
    -- (3)
    ((exteriorProduct (fieldChowSituation k) sX sY (r : ℤ) (s : ℤ) α β).1 =
      torFormulaCycleIntersectionProduct (fieldChowSituation k) (pullback.fst sX sY ≫ sX)
        (isRegular_pullback_of_isRegular sX sY hX hY) ((r : ℤ) + (s : ℤ))
        (exteriorProduct (fieldChowSituation k) sX sY (r : ℤ) (dY : ℤ) α
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sY (𝟙 Y) (dY : ℤ))).1
        (exteriorProduct (fieldChowSituation k) sX sY (dX : ℤ) (s : ℤ)
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX (𝟙 X) (dX : ℤ)) β).1 ∧
    (exteriorProduct (fieldChowSituation k) sX sY (r : ℤ) (s : ℤ) α β).1 =
      torFormulaCycleIntersectionProduct (fieldChowSituation k) (pullback.fst sX sY ≫ sX)
        (isRegular_pullback_of_isRegular sX sY hX hY) ((r : ℤ) + (s : ℤ))
        (flatPullback (fieldChowSituation k) (pullback.fst sX sY ≫ sX) sX (pullback.fst sX sY)
          rfl dY (relativeDimension_pullbackFst sX sY dY hdY) (r : ℤ) α).1
        (flatPullback (fieldChowSituation k) (pullback.fst sX sY ≫ sX) sY (pullback.snd sX sY)
          pullback.condition.symm dX (relativeDimension_pullbackSnd sX sY dX hdX) (s : ℤ) β).1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.18, Tag 0B09](https://stacks.math.columbia.edu/tag/0B09)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
