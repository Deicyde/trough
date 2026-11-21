---
catalog: module
lean: RatCast, Rat.cast
statement: formalized
proof: formalized
---

# RatCast

`Batteries.Classes.RatCast`, in [Batteries/Classes/RatCast.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/RatCast.lean), by Robert Lewis, Leonardo de Moura, Johannes Hölzl, Mario Carneiro, Gabriel Ebner.

`RatCast` (class, [line 11](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/RatCast.lean#L11))

> Type class for the canonical homomorphism `Rat → K`.

```lean
class RatCast (K : Type u) where
  /-- The canonical homomorphism `Rat → K`. -/
  protected ratCast : Rat → K
```

`Rat.cast` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/RatCast.lean#L20))

> Canonical homomorphism from `Rat` to a division ring `K`.
> This is just the bare function in order to aid in creating instances of `DivisionRing`.

```lean
protected def Rat.cast {K : Type u} [RatCast K] : Rat → K
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Classes/RatCast.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/RatCast.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Classes.RatCast.json)
