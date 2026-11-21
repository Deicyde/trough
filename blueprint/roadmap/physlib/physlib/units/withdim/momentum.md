---
declaration: module
origin: cited
lean: Momentum
statement: formalized
proof: formalized
---

# Momentum

The module `Physlib.Units.WithDim.Momentum`, [Physlib/Units/WithDim/Momentum.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Units/WithDim/Momentum.lean): 1 declaration, 1 with a docstring.

> In this module we define the type `Momentum`, which represents the momentum of a particle
> in `d`-dimensional space, in an arbitrary (but given) set of units.

**`Momentum`**, an abbrev, [line 23](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Units/WithDim/Momentum.lean#L23).

> Momentum in `d`-dimensional space in an arbitrary, but given, set of units.
> In `(3+1)d` space time this corresponds to `3`-momentum not `4`-momentum.

```lean
abbrev Momentum (d : ℕ := 3) : Type
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Momentum.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Units/WithDim/Momentum.lean)
