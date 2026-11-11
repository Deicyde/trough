---
declaration: section
origin: cited
lean: Stacks.Chow.principalDivisorCycle, Stacks.Chow.flatPullback_principalDivisorCycle
statement: formalized
proof: formalized
---

# 42.17 Principal divisors

Section 42.17 of the Stacks Project, [Tag 02RN](https://stacks.math.columbia.edu/tag/02RN). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02RO, a definition

[Tag 02RO](https://stacks.math.columbia.edu/tag/02RO) in the Stacks Project.

**`Stacks.Chow.principalDivisorCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DimensionFunction/PrincipalDivisor.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DimensionFunction/PrincipalDivisor.lean#L62). References: EGA IV (21.6.7), “cyc(div(f))”.

> The principal divisor `div(f) = ∑_Z ord_Z(f) [Z]` of a rational function on an integral
> scheme `X` of delta-dimension `n` locally of finite type over the base, as an element of the
> group `Z_{n-1}(X)` of cycles of delta-dimension `n - 1`.

```lean
def principalDivisorCycle (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] [IsIntegral X] {n : ℤ}
    (hn : schemeDeltaDimension C p = (n : EInt)) (f : X.functionField) :
    CycleGroup C p (n - 1)
```

## Tag 02RR, a lemma

[Tag 02RR](https://stacks.math.columbia.edu/tag/02RR) in the Stacks Project.

**`Stacks.Chow.flatPullback_principalDivisorCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisorIntegral.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisorIntegral.lean#L82).

> Let `C = (S, δ)` be the base situation of chapter 42, let `X` and `Y` be integral and
> locally of finite type over `S` with `n = dim_δ(Y)`, and let `f : X ⟶ Y` be flat of relative
> dimension `r`. For a nonzero rational function `g` on `Y`,
>
>   `f^* div_Y(g) = div_X(g)`
>
> in `Z_{n + r - 1}(X)`, where `g` is read on `X` through the extension `R(Y) ⊆ R(X)` of function
> fields induced by `f`.

```lean
theorem flatPullback_principalDivisorCycle (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    [IsIntegral X] [IsIntegral Y] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sY = sX) (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) {n : ℤ}
    (hY : schemeDeltaDimension C sY = (n : EInt)) (g : Y.functionField) (hg : g ≠ 0) :
    (flatPullback C sX sY f hbase r hf (n - 1) (principalDivisorCycle C sY hY g)).1 =
      (principalDivisorCycle C sX
        (schemeDeltaDimension_eq_add_of_flat C sX sY f hbase r hf hY)
        (dominantFunctionFieldMap f g)).1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.17, Tag 02RN](https://stacks.math.columbia.edu/tag/02RN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
