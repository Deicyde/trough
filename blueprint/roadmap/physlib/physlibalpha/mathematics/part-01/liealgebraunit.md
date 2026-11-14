---
declaration: module
origin: cited
lean: instLieRingUnit, instLieAlgebraUnit
statement: formalized
proof: formalized
---

# The zero Lie algebra on `Unit`

The module `PhyslibAlpha.Mathematics.LieAlgebraUnit`, [PhyslibAlpha/Mathematics/LieAlgebraUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LieAlgebraUnit.lean): 3 declarations (1 instance with no name), none with a docstring.

## i. Overview

> `Unit` with the zero bracket is a Lie ring, and a Lie algebra over any commutative ring.
> It is the Lie algebra of the trivial group, for example the gauge data of an empty list of
> gauge factors.

## ii. Key results

> - `instLieRingUnit`, `instLieAlgebraUnit` : the zero Lie algebra on `Unit`.

## iv. References

> * None.

## A. The zero Lie algebra

**An instance with no name**, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LieAlgebraUnit.lean#L40).

```lean
instance : Bracket Unit Unit
```

**`instLieRingUnit`**, an instance, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LieAlgebraUnit.lean#L42).

```lean
instance instLieRingUnit : LieRing Unit
```

**`instLieAlgebraUnit`**, an instance, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LieAlgebraUnit.lean#L48).

```lean
instance instLieAlgebraUnit {R : Type*} [CommRing R] : LieAlgebra R Unit
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/LieAlgebraUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LieAlgebraUnit.lean)
