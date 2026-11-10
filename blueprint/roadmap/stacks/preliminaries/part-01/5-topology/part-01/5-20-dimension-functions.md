---
declaration: section
origin: cited
lean: TopologicalSpace.isImmediateSpecialization_iff, TopologicalSpace.exists_dimensionFunction_iff, isCatenarySpace_and_topCodim_eq_of_isDimensionFunction, TopologicalSpace.DimensionFunction.isLocallyConstant_sub, TopologicalSpace.exists_open_nhd_with_dimension_function, TopologicalSpace.DimensionFunction.exists_dimensionFunction_iff_obstruction_eq_zero, TopologicalSpace.DimensionFunction.exists_cover_dimensionFunction_iff_obstruction_eq_zero
statement: formalized
proof: formalized
---

# 5.20 Dimension functions

Section 5.20 of the Stacks Project, [Tag 02I8](https://stacks.math.columbia.edu/tag/02I8). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02I9, a definition

[Tag 02I9](https://stacks.math.columbia.edu/tag/02I9) in the Stacks Project.

**`TopologicalSpace.isImmediateSpecialization_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunction.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunction.lean#L35).

> A specialization is immediate exactly when it is non-trivial and admits no intermediate
> point: every `z` with `x ⤳ z ⤳ y` is one of the two endpoints.

```lean
theorem isImmediateSpecialization_iff (x y : X) :
    IsImmediateSpecialization x y ↔
      x ⤳ y ∧ x ≠ y ∧ ∀ z : X, x ⤳ z → z ⤳ y → z = x ∨ z = y
```

**`TopologicalSpace.exists_dimensionFunction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunction.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunction.lean#L44).

> A function `δ : X → ℤ` is the underlying function of a dimension function exactly when it
> is strictly decreasing along non-trivial specializations and drops by exactly one along
> immediate specializations.

```lean
theorem exists_dimensionFunction_iff (δ : X → ℤ) :
    (∃ d : DimensionFunction X, ∀ x, d x = δ x) ↔
      (∀ x y : X, x ⤳ y → x ≠ y → δ y < δ x) ∧
        (∀ x y : X, IsImmediateSpecialization x y → δ x = δ y + 1)
```

## Tag 02IA, a lemma

[Tag 02IA](https://stacks.math.columbia.edu/tag/02IA) in the Stacks Project.

**`isCatenarySpace_and_topCodim_eq_of_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CatenaryOfDimensionFunction.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/CatenaryOfDimensionFunction.lean#L468).

> A sober topological space `X` admitting a dimension function `δ` is catenary, and for every
> specialization `x ⤳ y` we have `codim(closure {y}, closure {x}) = δ x - δ y`.

```lean
theorem isCatenarySpace_and_topCodim_eq_of_isDimensionFunction (X : Type*) [TopologicalSpace X]
    (hSober : StacksSober X) (δ : X → ℤ) (hδ : IsDimensionFunctionForCatenary δ) :
    IrreducibleClosedsCodim.IsCatenarySpace X ∧
      ∀ x y : X, x ⤳ y →
        IrreducibleClosedsCodim.topCodim (closureSingleton y) (closureSingleton x)
          = ((δ x - δ y).toNat : ℕ∞)
```

## Tag 02IB, a lemma

[Tag 02IB](https://stacks.math.columbia.edu/tag/02IB) in the Stacks Project.

**`TopologicalSpace.DimensionFunction.isLocallyConstant_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionDifference.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunctionDifference.lean#L160).

> **Stacks 02IB.** On a locally Noetherian sober topological space `X`, the difference of two
> dimension functions `δ, δ' : X → ℤ` is locally constant.

```lean
theorem DimensionFunction.isLocallyConstant_sub [QuasiSober X] [T0Space X]
    (hX : IsLocallyNoetherianSpace X) (δ δ' : DimensionFunction X) :
    IsLocallyConstant (fun x : X => δ x - δ' x)
```

## Tag 02IC, a lemma

[Tag 02IC](https://stacks.math.columbia.edu/tag/02IC) in the Stacks Project.

**`TopologicalSpace.exists_open_nhd_with_dimension_function`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean#L771).

> Let `X` be a topological space that is locally Noetherian, sober (i.e. `QuasiSober` and
> `T0Space`), and catenary. Then every point of `X` has an open neighbourhood `U ⊆ X` such that
> the subspace `U` admits a dimension function `δ : U → ℤ`.

```lean
theorem exists_open_nhd_with_dimension_function
    (X : Type*) [TopologicalSpace X]
    [QuasiSober X] [T0Space X]
    (hLN : IsLocallyNoetherianSpace X)
    (hCat : IsTopologicallyCatenary X)
    (x : X) :
    ∃ U : Set X, IsOpen U ∧ x ∈ U ∧ Nonempty (DimensionFunction U)
```

## Tag 02ID, a remark

[Tag 02ID](https://stacks.math.columbia.edu/tag/02ID) in the Stacks Project.

**`TopologicalSpace.DimensionFunction.exists_dimensionFunction_iff_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionObstruction.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunctionObstruction.lean#L348).

> **Stacks 02ID.** For a cover of a locally Noetherian sober space by opens carrying dimension
> functions `δ i`, a global dimension function on `X` exists if and only if the class of the
> discrepancy cocycle `δ i - δ j` vanishes in `Ȟ¹(𝒰, ℤ)`.
>
> Both directions use tag 02IB. Forward: if `d` is global then `d - δ i` is locally constant on
> `U i`, and these functions are a `0`-cochain whose coboundary is the discrepancy. Backward: a
> `0`-cochain `t` with `d⁰ t` the discrepancy makes `δ i + t i` independent of `i`, hence a global
> function; it is a dimension function because an open set is stable under generization (so both
> ends of a specialization lie in a common member of the cover) and because a locally constant
> function is constant along specializations.

```lean
theorem exists_dimensionFunction_iff_obstruction_eq_zero [QuasiSober X] [T0Space X]
    (hX : IsLocallyNoetherianSpace X) (U : I → Opens X) (hcov : ∀ x : X, ∃ i, x ∈ U i)
    (δ : ∀ i, DimensionFunction (U i : Set X)) :
    Nonempty (DimensionFunction X) ↔ obstruction hX U δ = 0
```

**`TopologicalSpace.DimensionFunction.exists_cover_dimensionFunction_iff_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionObstruction.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunctionObstruction.lean#L467).

> **Stacks 02ID.** On a catenary, locally Noetherian, sober topological space there is a cover by
> opens carrying dimension functions (tag 02IC), and a global dimension function exists exactly when
> the obstruction class of that cover vanishes in `Ȟ¹(𝒰, ℤ)`. By `obstruction_eq_zero_congr` the
> vanishing is independent of the cover, so this single class is *the* obstruction.

```lean
theorem exists_cover_dimensionFunction_iff_obstruction_eq_zero [QuasiSober X] [T0Space X]
    (hLN : IsLocallyNoetherianSpace X) (hCat : IsTopologicallyCatenary X) :
    ∃ (U : X → Opens X) (δ : ∀ x, DimensionFunction (U x : Set X)),
      (∀ x, x ∈ U x) ∧ (Nonempty (DimensionFunction X) ↔ obstruction hLN U δ = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.20, Tag 02I8](https://stacks.math.columbia.edu/tag/02I8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
