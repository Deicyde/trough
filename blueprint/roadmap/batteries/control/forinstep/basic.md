---
catalog: module
lean: ForInStep.bind, ForInStep.bindM, ForInStep.run, ForInStep.bindList
statement: formalized
proof: formalized
---

# Additional definitions on `ForInStep`

`Batteries.Control.ForInStep.Basic`, in [Batteries/Control/ForInStep/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean), by Mario Carneiro.

`ForInStep.bind` (definition, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean#L16))

> This is similar to a monadic `bind` operator, except that the two type parameters have to be
> the same, which prevents putting a monad instance on `ForInStepT m α := m (ForInStep α)`.

```lean
protected def ForInStep.bind [Monad m]
    (a : ForInStep α) (f : α → m (ForInStep α)) : m (ForInStep α)
```

`ForInStep.bindM` (abbreviation, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean#L22))

```lean
protected abbrev ForInStep.bindM [Monad m]
    (a : m (ForInStep α)) (f : α → m (ForInStep α)) : m (ForInStep α)
```

`ForInStep.run` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean#L29))

> Get the value out of a `ForInStep`.
> This is usually done at the end of a `forIn` loop to scope the early exit to the loop body.

```lean
def ForInStep.run : ForInStep α → α
```

`ForInStep.bindList` (definition, [line 34](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean#L34))

> Applies function `f` to each element of a list to accumulate a `ForInStep` value.

```lean
def ForInStep.bindList [Monad m]
      (f : α → β → m (ForInStep β)) : List α → ForInStep β → m (ForInStep β)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Control/ForInStep/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Basic.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Control.ForInStep.Basic.json)
