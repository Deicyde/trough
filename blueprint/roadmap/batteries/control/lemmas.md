---
catalog: module
lean: ReaderT.run_failure, ReaderT.run_orElse, ReaderT.run_throw, ReaderT.run_throwThe, ReaderT.run_tryCatch, ReaderT.run_tryCatchThe, StateT.run_failure, StateT.run_orElse, StateT.run_throw, StateT.run_throwThe, StateT.run_tryCatch, StateT.run_tryCatchThe
statement: formalized
proof: formalized
---

# Control/Lemmas

`Batteries.Control.Lemmas`, in [Batteries/Control/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean), by François G. Dorais, Eric Wieser.

`ReaderT.run_failure` (theorem, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L16))

```lean
theorem run_failure [Monad m] [Alternative m] (ctx : ρ) :
    (failure : ReaderT ρ m α).run ctx = failure
```

`ReaderT.run_orElse` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L19))

```lean
theorem run_orElse [Monad m] [Alternative m] (x y : ReaderT ρ m α) (ctx : ρ) :
    (x <|> y).run ctx = (x.run ctx <|> y.run ctx)
```

`ReaderT.run_throw` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L22))

```lean
theorem run_throw [MonadExceptOf ε m] (e : ε) (ctx : ρ) :
    (throw e : ReaderT ρ m α).run ctx = throw e
```

`ReaderT.run_throwThe` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L25))

```lean
theorem run_throwThe [MonadExceptOf ε m] (e : ε) (ctx : ρ) :
    (throwThe ε e : ReaderT ρ m α).run ctx = throwThe ε e
```

`ReaderT.run_tryCatch` (theorem, [line 28](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L28))

```lean
theorem run_tryCatch [MonadExceptOf ε m]
    (body : ReaderT ρ m α) (handler : ε → ReaderT ρ m α) (ctx : ρ) :
    (tryCatch body handler).run ctx = tryCatch (body.run ctx) (handler · |>.run ctx)
```

`ReaderT.run_tryCatchThe` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L32))

```lean
theorem run_tryCatchThe [MonadExceptOf ε m]
    (body : ReaderT ρ m α) (handler : ε → ReaderT ρ m α) (ctx : ρ) :
    (tryCatchThe ε body handler).run ctx = tryCatchThe ε (body.run ctx) (handler · |>.run ctx)
```

`StateT.run_failure` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L43))

```lean
theorem run_failure {α σ} [Monad m] [Alternative m] (s : σ) :
    (failure : StateT σ m α).run s = failure
```

`StateT.run_orElse` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L46))

```lean
theorem run_orElse {α σ} [Monad m] [Alternative m] (x y : StateT σ m α) (s : σ) :
    (x <|> y).run s = (x.run s <|> y.run s)
```

`StateT.run_throw` (theorem, [line 49](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L49))

```lean
theorem run_throw [Monad m] [MonadExceptOf ε m] (e : ε) (s : σ) :
    (throw e : StateT σ m α).run s = (do let a ← throw e; pure (a, s))
```

`StateT.run_throwThe` (theorem, [line 52](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L52))

```lean
theorem run_throwThe [Monad m] [MonadExceptOf ε m] (e : ε) (s : σ) :
    (throwThe ε e : StateT σ m α).run s = (do let a ← throwThe ε e; pure (a, s))
```

`StateT.run_tryCatch` (theorem, [line 55](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L55))

```lean
theorem run_tryCatch [Monad m] [MonadExceptOf ε m]
    (body : StateT σ m α) (handler : ε → StateT σ m α) (s : σ) :
    (tryCatch body handler).run s = tryCatch (body.run s) (handler · |>.run s)
```

`StateT.run_tryCatchThe` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean#L59))

```lean
theorem run_tryCatchThe [Monad m] [MonadExceptOf ε m]
    (body : StateT σ m α) (handler : ε → StateT σ m α) (s : σ) :
    (tryCatchThe ε body handler).run s = tryCatchThe ε (body.run s) (handler · |>.run s)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Control/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Lemmas.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Control.Lemmas.json)
