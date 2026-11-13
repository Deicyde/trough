---
declaration: module
origin: cited
lean: ParametricDimensionExamples.Info, ParametricDimensionExamples.bitDim, ParametricDimensionExamples.symbolDim
statement: formalized
proof: formalized
---

# Examples: parametric dimensions and comparing dimensioned quantities

The module `Physlib.Units.ParametricDimensionExamples`, [Physlib/Units/ParametricDimensionExamples.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean): 4 declarations (1 instance with no name), 3 with a docstring.

> `Dimension B` is parameterised by a basis `B` of base dimensions. This module
> illustrates two consequences.

## Comparing a length with a velocity times a time

> A recurring question is how to compare a quantity of dimension `length` with a
> product of a quantity of dimension `length / time` and a quantity of dimension
> `time`. In the fixed-tuple representation of `LTMCTDimensionBase`, reducible exponent
> arithmetic makes this concrete cancellation a definitional equality:
>
> * `(L𝓭 / T𝓭) * T𝓭 = L𝓭` is closed by `rfl`.
> * `WithDim ((L𝓭 / T𝓭) * T𝓭) ℝ` and `WithDim L𝓭 ℝ` are therefore definitionally
>   equal types.
>
> Consequently a bare `x = v * t` is well-typed for these concrete dimensions. For a
> representation where the same cancellation holds only propositionally, `WithDim.cast`
> bridges the two dimension-indexed types.

## A non-standard basis

> Because `Dimension` is parametric, the same dimensional algebra and `cast`-based
> comparison are available over any represented basis, not just the physical
> `LTMCTDimensionBase`. The unit-scaling layer (`LTMCTUnitChoices`, `dimScale`) is not
> needed for either the algebra or the comparison, so neither is referenced here.
>
> This module is illustrative and should not be imported by other modules.

## The same comparison over a non-standard basis

> A basis with two base dimensions of its own — `bit` and `symbol` — that
> `LTMCTDimensionBase` does not have. Nothing in the standard units system is involved.

**`ParametricDimensionExamples.Info`**, an inductive, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean#L83).

> A basis of information-theoretic base dimensions.

```lean
inductive Info
  /-- The information base dimension (bits). -/
  | bit
  /-- The symbol base dimension. -/
  | symbol
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean#L89).

```lean
instance : DimensionBasis Info
```

**`ParametricDimensionExamples.bitDim`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean#L92).

> The `bit` base dimension.

```lean
def bitDim : Dimension Info
```

**`ParametricDimensionExamples.symbolDim`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean#L95).

> The `symbol` base dimension.

```lean
def symbolDim : Dimension Info
```

## Depends on

- [Dimension](dimension.md)

## Sources

- [Physlib/Units/ParametricDimensionExamples.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/ParametricDimensionExamples.lean)
