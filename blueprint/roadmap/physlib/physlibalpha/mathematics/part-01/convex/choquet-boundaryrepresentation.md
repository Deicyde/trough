---
declaration: module
origin: cited
lean: Choquet.IsBoundaryRepresentation, Choquet.HasBoundaryDecomposition, Choquet.HasUniqueBoundaryDecomposition, Choquet.IsSimplexRepresentation
statement: formalized
proof: formalized
---

# Representations by measures on a boundary

The module `PhyslibAlpha.Mathematics.Convex.Choquet.BoundaryRepresentation`, [PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean): 4 declarations, 4 with a docstring.

> Boundary representations of points by regular probability measures, and simplices.

## i. Overview

> A family of real-valued tests observes points of a space `X`. A boundary representation of a
> point `x` is a regular probability measure on a boundary space `B` whose averages agree with the
> tests at `x`. This formulation contains no physical structure: the tests may later be observables,
> the points states, and the boundary points pure states.
>
> A point has a boundary decomposition when at least one such measure exists, and a unique boundary
> decomposition when exactly one exists. The tested space is a simplex when every point has a unique
> boundary decomposition.

## ii. Key results

> - `Choquet.IsBoundaryRepresentation` states that a boundary measure represents a point.
> - `Choquet.HasBoundaryDecomposition` states existence of a boundary representation.
> - `Choquet.HasUniqueBoundaryDecomposition` states existence and uniqueness.
> - `Choquet.IsSimplexRepresentation` states that every point has a unique representation.

## iv. References

> * None.

## A. Boundary representations

**`Choquet.IsBoundaryRepresentation`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean#L57).

> A regular probability measure on `B` represents `x` when the average of every test over the
> boundary agrees with its value at `x`.

```lean
def IsBoundaryRepresentation (test : A → X → ℝ) (boundary : B → X) (x : X)
    (μ : Measure B) : Prop
```

**`Choquet.HasBoundaryDecomposition`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean#L64).

> A point has a boundary decomposition when some regular probability measure on the boundary
> represents it.

```lean
def HasBoundaryDecomposition (test : A → X → ℝ) (boundary : B → X) (x : X) : Prop
```

**`Choquet.HasUniqueBoundaryDecomposition`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean#L69).

> A point has a unique boundary decomposition when exactly one regular probability measure on
> the boundary represents it.

```lean
def HasUniqueBoundaryDecomposition (test : A → X → ℝ) (boundary : B → X)
    (x : X) : Prop
```

## B. Simplices

**`Choquet.IsSimplexRepresentation`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean#L77).

> A tested space is a simplex with boundary `B` when every point has a unique boundary
> decomposition.

```lean
def IsSimplexRepresentation (test : A → X → ℝ) (boundary : B → X) : Prop
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/BoundaryRepresentation.lean)
