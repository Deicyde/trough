---
declaration: section
origin: cited
lean: TopologicalSpace.isImmediateSpecialization_iff, TopologicalSpace.exists_dimensionFunction_iff, isCatenarySpace_and_topCodim_eq_of_isDimensionFunction, TopologicalSpace.DimensionFunction.isLocallyConstant_sub, TopologicalSpace.exists_open_nhd_with_dimension_function, TopologicalSpace.DimensionFunction.nonempty_dimensionFunction_iff_dimensionObstruction_eq_zero, TopologicalSpace.DimensionFunction.nonempty_dimensionFunction_iff_dimensionObstructionExt_eq_zero
statement: formalized
proof: formalized
---

# 5.20 Dimension functions

Section 5.20 of the Stacks Project, [Tag 02I8](https://stacks.math.columbia.edu/tag/02I8). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02I9, a definition

[Tag 02I9](https://stacks.math.columbia.edu/tag/02I9) in the Stacks Project.

**`TopologicalSpace.isImmediateSpecialization_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunction.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunction.lean#L35).

> A specialization is immediate exactly when it is non-trivial and admits no intermediate
> point: every `z` with `x ⤳ z ⤳ y` is one of the two endpoints.

```lean
theorem isImmediateSpecialization_iff (x y : X) :
    IsImmediateSpecialization x y ↔
      x ⤳ y ∧ x ≠ y ∧ ∀ z : X, x ⤳ z → z ⤳ y → z = x ∨ z = y
```

**`TopologicalSpace.exists_dimensionFunction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunction.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunction.lean#L44).

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

**`isCatenarySpace_and_topCodim_eq_of_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/CatenaryOfDimensionFunction.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/CatenaryOfDimensionFunction.lean#L468).

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

**`TopologicalSpace.DimensionFunction.isLocallyConstant_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionDifference.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunctionDifference.lean#L160).

> **Stacks 02IB.** On a locally Noetherian sober topological space `X`, the difference of two
> dimension functions `δ, δ' : X → ℤ` is locally constant.

```lean
theorem DimensionFunction.isLocallyConstant_sub [QuasiSober X] [T0Space X]
    (hX : IsLocallyNoetherianSpace X) (δ δ' : DimensionFunction X) :
    IsLocallyConstant (fun x : X => δ x - δ' x)
```

## Tag 02IC, a lemma

[Tag 02IC](https://stacks.math.columbia.edu/tag/02IC) in the Stacks Project.

**`TopologicalSpace.exists_open_nhd_with_dimension_function`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean, line 771](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean#L771).

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

**`TopologicalSpace.DimensionFunction.nonempty_dimensionFunction_iff_dimensionObstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionObstructionCohomology.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunctionObstructionCohomology.lean#L215). The attribute's comment: “the obstruction element of H¹(X, ℤ), first right-derived global sections of the constant sheaf ℤ, independent of all choices, vanishes iff a dimension function exists”.

> **Stacks 02ID.** On a catenary, locally Noetherian, sober topological space `X`, the
> obstruction to having a dimension function is an element of `H¹(X, ℤ)`: the element
> `dimensionObstruction` of first sheaf cohomology of the constant sheaf `ℤ`, which does not depend
> on any choice (`obstructionH1_eq_dimensionObstruction`), vanishes if and only if `X` has a
> dimension function.
>
> The element is the image of the Čech class of the cocycle `δ i - δ j` of local dimension
> functions (tags 02IC and 02IB) under the injective comparison `Ȟ¹(𝒰, ℤ) → H¹(X, ℤ)`.

```lean
theorem nonempty_dimensionFunction_iff_dimensionObstruction_eq_zero
    (hLN : IsLocallyNoetherianSpace X) (hCat : IsTopologicallyCatenary X) :
    Nonempty (DimensionFunction X) ↔ dimensionObstruction hLN hCat = 0
```

**`TopologicalSpace.DimensionFunction.nonempty_dimensionFunction_iff_dimensionObstructionExt_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/DimensionFunctionObstructionCohomology.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunctionObstructionCohomology.lean#L237). The attribute's comment: “the same statement with H¹(X, ℤ) read as Mathlib's Ext-group cohomology Sheaf.H”.

> **Stacks 02ID**, with `H¹(X, ℤ)` read as Mathlib's `Sheaf.H`: on a catenary, locally
> Noetherian, sober topological space a dimension function exists if and only if the obstruction
> element of `Sheaf.H ℤ 1` vanishes.

```lean
theorem nonempty_dimensionFunction_iff_dimensionObstructionExt_eq_zero
    (hLN : IsLocallyNoetherianSpace X) (hCat : IsTopologicallyCatenary X) :
    Nonempty (DimensionFunction X) ↔ dimensionObstructionExt hLN hCat = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.20, Tag 02I8](https://stacks.math.columbia.edu/tag/02I8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
