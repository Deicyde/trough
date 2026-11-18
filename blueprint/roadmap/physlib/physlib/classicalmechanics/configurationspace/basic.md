---
declaration: module
origin: cited
lean: ClassicalMechanics.ConfigurationSpace
statement: formalized
proof: formalized
---

# Configuration spaces

The module `Physlib.ClassicalMechanics.ConfigurationSpace.Basic`, [Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean): 2 declarations (1 instance with no name), 1 with a docstring.

> Smooth manifolds without boundary.

## i. Overview

> The configuration space of a mechanical system is the manifold of its configurations.

## ii. Key results

> - `ConfigurationSpace` : a smooth manifold without boundary.

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]

## A. Configuration spaces

**`ClassicalMechanics.ConfigurationSpace`**, a structure, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean#L46).

> A smooth manifold without boundary.

```lean
structure ConfigurationSpace (I : ModelWithCorners ℝ E H) where
  /-- The configurations. -/
  carrier : Type*
  [topologicalSpace : TopologicalSpace carrier]
  [chartedSpace : ChartedSpace H carrier]
  [isManifold : IsManifold I ∞ carrier]
  [boundarylessManifold : BoundarylessManifold I carrier]
```

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean#L56).

```lean
instance : CoeSort (ConfigurationSpace I) (Type _)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Basic.lean)
