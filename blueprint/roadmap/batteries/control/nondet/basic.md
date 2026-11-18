---
catalog: module
lean: Nondet, Nondet.nil, Nondet.squash, Nondet.bind, Nondet.singletonM, Nondet.singleton, Nondet.ofListM, Nondet.ofList, Nondet.mapM, Nondet.map, Nondet.ofOptionM, Nondet.ofOption, Nondet.filterMapM, Nondet.filterMap, Nondet.filterM, Nondet.filter, Nondet.iterate, Nondet.toMLList', Nondet.toList, Nondet.toList', Nondet.head, Nondet.firstM
statement: formalized
proof: formalized
---

# A nondeterminism monad

`Batteries.Control.Nondet.Basic`, in [Batteries/Control/Nondet/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean), by Kim Morrison.

> We represent nondeterministic values in a type `α` as a single field structure containing an
> `MLList m (σ × α)`, i.e. as a monadic lazy list of possible values,
> each equipped with the backtrackable state
> required to run further computations in the ambient monad.
>
> We provide an `Alternative` `Monad` instance, as well as functions `bind`, `mapM`, and `filterMapM`,
> and functions `singletonM`, `ofListM`, `ofOptionM`, and `firstM`
> for entering and leaving the nondeterministic world.
>
> Operations on the nondeterministic value via `bind`, `mapM`, and `filterMapM`
> run with the appropriate backtrackable state, and are responsible for updating the state themselves
> (typically this doesn't need to be done explicitly,
> but just happens as a side effect in the monad `m`).

`Nondet` (structure, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L50))

> `Nondet m α` is variation on `MLList m α` suitable for use with backtrackable monads `m`.
>
> We think of `Nondet m α` as a nondeterministic value in `α`,
> with the possible alternatives stored in a monadic lazy list.
>
> Along with each `a : α` we store the backtrackable state, and ensure that monadic operations
> on alternatives run with the appropriate state.
>
> Operations on the nondeterministic value via `bind`, `mapM`, and `filterMapM`
> run with the appropriate backtrackable state, and are responsible for updating the state themselves
> (typically this doesn't need to be done explicitly,
> but just happens as a side effect in the monad `m`).

```lean
structure Nondet (m : Type → Type) [MonadBacktrack σ m] (α : Type) : Type where
  /--
  Convert a non-deterministic value into a lazy list, keeping the backtrackable state.
  Be careful that monadic operations on the `MLList` will not respect this state!
  -/
  toMLList : MLList m (α × σ)
```

`Nondet.nil` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L64))

> The empty nondeterministic value.

```lean
def nil : Nondet m α
```

`Nondet.squash` (definition, [line 71](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L71))

> Squash a monadic nondeterministic value to a nondeterministic value.

```lean
def squash (L : Unit → m (Nondet m α)) : Nondet m α
```

`Nondet.bind` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L78))

> Bind a nondeterministic function over a nondeterministic value,
> ensuring the function is run with the relevant backtrackable state at each value.

```lean
partial def bind (L : Nondet m α) (f : α → Nondet m β) : Nondet m β
```

`Nondet.singletonM` (definition, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L89))

> Convert any value in the monad to the singleton nondeterministic value.

```lean
def singletonM (x : m α) : Nondet m α
```

`Nondet.singleton` (definition, [line 95](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L95))

> Convert a value to the singleton nondeterministic value.

```lean
def singleton (x : α) : Nondet m α
```

`Nondet.ofListM` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L111))

> Lift a list of monadic values to a nondeterministic value.
> We ensure that each monadic value is evaluated with the same backtrackable state.

```lean
def ofListM (L : List (m α)) : Nondet m α
```

`Nondet.ofList` (definition, [line 124](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L124))

> Lift a list of values to a nondeterministic value.
> (The backtrackable state in each will be identical:
> whatever the state was when we first read from the result.)

```lean
def ofList (L : List α) : Nondet m α
```

`Nondet.mapM` (definition, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L127))

> Apply a function which returns values in the monad to every alternative of a `Nondet m α`.

```lean
def mapM (f : α → m β) (L : Nondet m α) : Nondet m β
```

`Nondet.map` (definition, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L131))

> Apply a function to each alternative in a `Nondet m α` .

```lean
def map (f : α → β) (L : Nondet m α) : Nondet m β
```

`Nondet.ofOptionM` (definition, [line 135](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L135))

> Convert a monadic optional value to a nondeterministic value.

```lean
def ofOptionM (x : m (Option α)) : Nondet m α
```

`Nondet.ofOption` (definition, [line 141](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L141))

> Convert an optional value to a nondeterministic value.

```lean
def ofOption (x : Option α) : Nondet m α
```

`Nondet.filterMapM` (definition, [line 144](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L144))

> Filter and map a nondeterministic value using a monadic function which may return `none`.

```lean
def filterMapM (f : α → m (Option β)) (L : Nondet m α) : Nondet m β
```

`Nondet.filterMap` (definition, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L148))

> Filter and map a nondeterministic value.

```lean
def filterMap (f : α → Option β) (L : Nondet m α) : Nondet m β
```

`Nondet.filterM` (definition, [line 152](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L152))

> Filter a nondeterministic value using a monadic predicate.

```lean
def filterM (p : α → m (ULift Bool)) (L : Nondet m α) : Nondet m α
```

`Nondet.filter` (definition, [line 160](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L160))

> Filter a nondeterministic value.

```lean
def filter (p : α → Bool) (L : Nondet m α) : Nondet m α
```

`Nondet.iterate` (definition, [line 168](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L168))

> All iterations of a non-deterministic function on an initial value.
>
> (That is, depth first search.)

```lean
partial def iterate (f : α → Nondet m α) (a : α) : Nondet m α
```

`Nondet.toMLList'` (definition, [line 174](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L174))

> Convert a non-deterministic value into a lazy list, by discarding the backtrackable state.

```lean
def toMLList' (L : Nondet m α) : MLList m α
```

`Nondet.toList` (definition, [line 179](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L179))

> Convert a non-deterministic value into a list in the monad, retaining the backtrackable state.

```lean
def toList (L : Nondet m α) : m (List (α × σ))
```

`Nondet.toList'` (definition, [line 184](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L184))

> Convert a non-deterministic value into a list in the monad, by discarding the backtrackable state.

```lean
def toList' (L : Nondet m α) : m (List α)
```

`Nondet.head` (definition, [line 194](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L194))

> Find the first alternative in a nondeterministic value, as a monadic value.

```lean
def head (L : Nondet m α) : m α
```

`Nondet.firstM` (definition, [line 203](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean#L203))

> Find the value of a monadic function on the first alternative in a nondeterministic value
> where the function succeeds.

```lean
def firstM (L : Nondet m α) (f : α → m (Option β)) : m β
```

## Depends on

- [Monadic lazy lists](../../data/part-01/mllist/basic.md)

## Sources

- [Batteries/Control/Nondet/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/Nondet/Basic.lean)
