---
catalog: module
lean: OptionT.run_monadLift, OptionT.run_mapConst
statement: formalized
proof: formalized
---

# Lemmas About Option Monad Transformer

`Batteries.Control.OptionT`, in [Batteries/Control/OptionT.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Control/OptionT.lean), by Sebastian Ullrich.

> This file contains lemmas about the behavior of `OptionT` and `OptionT.run`.

`OptionT.run_monadLift` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Control/OptionT.lean#L21))

```lean
theorem run_monadLift [Monad m] [LawfulMonad m] [MonadLiftT n m] (x : n α) :
    (monadLift x : OptionT m α).run = some <$> (monadLift x : m α)
```

`OptionT.run_mapConst` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Control/OptionT.lean#L24))

```lean
theorem run_mapConst [Monad m] [LawfulMonad m] (x : OptionT m α) (y : β) :
    (Functor.mapConst y x).run = Option.map (Function.const α y) <$> x.run
```

## Depends on

- [Laws for Monads with State](lawfulmonadstate.md)

## Sources

- [Batteries/Control/OptionT.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Control/OptionT.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Control.OptionT.json)
