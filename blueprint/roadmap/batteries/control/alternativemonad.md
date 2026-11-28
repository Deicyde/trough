---
catalog: module
lean: AlternativeMonad, LawfulAlternative, mapConst_failure, mapConst_orElse, failure_seqLeft, failure_seqRight, failure_bind, seq_failure, LawfulAlternativeLift
statement: formalized
proof: formalized
---

# Laws for Monads with Failure

`Batteries.Control.AlternativeMonad`, in [Batteries/Control/AlternativeMonad.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean), by Devon Tuma.

> Definitions for monads that also have an `Alternative` instance while sharing the underlying
> `Applicative` instance, and a class `LawfulAlternative` for types where the `failure` and `orElse`
> operations behave in a natural way. More specifically they satisfy:
>
> * `f <$> failure = failure`
> * `failure <*> x = failure`
> * `x <|> failure = x`
> * `failure <|> y = y`
> * `x <|> y <|> z = (x <|> y) <|> z`
> * `f <$> (x <|> y) = (f <$> x <|> f <$> y)`
>
> `Option`/`OptionT` are the most basic examples, but transformers like `StateT` also preserve
> the lawfulness of this on the underlying monad.
>
> The law `x *> failure = failure` is true for monads like `Option` and `List` that don't
> have any "side effects" to execution, but not for something like `OptionT` on some monads,
> so we don't include this condition.
>
> We also define a class `LawfulAlternativeLift` similar to `LawfulMonadLift` that states that
> a lifting between monads preserves `failure` and `orElse`.
>
> ## Tags
>
> monad, alternative, failure

`AlternativeMonad` (class, [line 49](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L49))

> `AlternativeMonad m` means that `m` has both a `Monad` and `Alternative` instance,
> which both share the same underlying `Applicative` instance.
> The main example is `Option`, but many monad transformers also preserve or add this structure.

```lean
class AlternativeMonad (m : Type _ → Type _) extends Alternative m, Monad m
```

`LawfulAlternative` (class, [line 55](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L55))

> `LawfulAlternative m` means that the `failure` operation on `m` behaves naturally
> with respect to `map`, `seq`, and `orElse` operators.

```lean
class LawfulAlternative (m : Type _ → Type _) [Alternative m] : Prop
    extends LawfulApplicative m where
  /-- Mapping the result of a failure is still a failure -/
  map_failure (f : α → β) : f <$> (failure : m α) = failure
  /-- Sequencing a `failure` call results in failure -/
  failure_seq (x : m α) : (failure : m (α → β)) <*> x = failure
  /-- `failure` is a right identity for `orElse`. -/
  orElse_failure (x : m α) : (x <|> failure) = x
  /-- `failure` is a left identity for `orElse`. -/
  failure_orElse (y : m α) : (failure <|> y) = y
  /-- `orElse` is associative. -/
  orElse_assoc (x y z : m α) : (x <|> y <|> z) = ((x <|> y) <|> z)
  /-- `map` commutes with `orElse`. The stronger statement with `bind` generally isn't true -/
  map_orElse (x y : m α) (f : α → β) : f <$> (x <|> y) = (f <$> x <|> f <$> y)
```

`mapConst_failure` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L76))

```lean
theorem mapConst_failure [Alternative m] [LawfulAlternative m] (y : β) :
    Functor.mapConst y (failure : m α) = failure
```

`mapConst_orElse` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L80))

```lean
theorem mapConst_orElse [Alternative m] [LawfulAlternative m] (x x' : m α) (y : β) :
    Functor.mapConst y (x <|> x') = (Functor.mapConst y x <|> Functor.mapConst y x')
```

`failure_seqLeft` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L84))

```lean
theorem failure_seqLeft [Alternative m] [LawfulAlternative m] (x : m α) :
    (failure : m β) <* x = failure
```

`failure_seqRight` (theorem, [line 88](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L88))

```lean
theorem failure_seqRight [Alternative m] [LawfulAlternative m] (x : m α) :
    (failure : m β) *> x = failure
```

`failure_bind` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L96))

```lean
theorem failure_bind [AlternativeMonad m] [LawfulAlternative m] [LawfulMonad m]
    (x : α → m β) : failure >>= x = failure
```

`seq_failure` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L104))

```lean
theorem seq_failure [AlternativeMonad m] [LawfulAlternative m] [LawfulMonad m]
    (x : m (α → β)) : x <*> failure = x *> failure
```

`LawfulAlternativeLift` (class, [line 113](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean#L113))

> Type-class for monad lifts that preserve the `Alternative` operations.

```lean
class LawfulAlternativeLift (m : semiOutParam (Type u → Type v)) (n : Type u → Type w)
    [Alternative m] [Alternative n] [MonadLift m n] : Prop where
  /-- Lifting preserves `failure`. -/
  monadLift_failure : monadLift (failure : m α) = (failure : n α)
  /-- Lifting preserves `orElse`. -/
  monadLift_orElse (x y : m α) : monadLift (x <|> y) = (monadLift x <|> monadLift y : n α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Control/Lemmas](lemmas.md)

## Sources

- [Batteries/Control/AlternativeMonad.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Control/AlternativeMonad.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Control.AlternativeMonad.json)
