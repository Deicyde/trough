---
catalog: module
lean: EIO.adapt_pure, EIO.adapt_bind, StateRefT'.lift_pure, StateRefT'.lift_bind
statement: formalized
proof: formalized
---

# Lawful instances of `MonadLift` for the Lean monad stack

`Batteries.Lean.LawfulMonadLift`, in [Batteries/Lean/LawfulMonadLift.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean), by Quang Dao.

> ### `EIO.adapt` simp lemmas

`EIO.adapt_pure` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean#L31))

```lean
theorem EIO.adapt_pure (f : ε₁ → ε₂) (a : α) :
    EIO.adapt f (pure a : EIO ε₁ α) = (pure a : EIO ε₂ α)
```

`EIO.adapt_bind` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean#L44))

```lean
theorem EIO.adapt_bind (f : ε₁ → ε₂) (ma : EIO ε₁ α) (g : α → EIO ε₁ β) :
    EIO.adapt f (ma >>= g) = EIO.adapt f ma >>= fun a => EIO.adapt f (g a)
```

> ### `StateRefT'.lift` simp lemmas

`StateRefT'.lift_pure` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean#L50))

```lean
theorem StateRefT'.lift_pure [Monad m] (a : α) :
    (StateRefT'.lift (pure a) : StateRefT' ω σ m α) = pure a
```

`StateRefT'.lift_bind` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean#L53))

```lean
theorem StateRefT'.lift_bind [Monad m] (ma : m α) (f : α → m β) :
    (StateRefT'.lift (ma >>= f) : StateRefT' ω σ m β) =
      StateRefT'.lift ma >>= fun a => StateRefT'.lift (f a)
```

> ### `LawfulMonadLift IO CoreM`

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/LawfulMonadLift.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/LawfulMonadLift.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.LawfulMonadLift.json)
