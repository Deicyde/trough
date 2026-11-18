---
catalog: module
lean: MLList, MLList.nil, MLList.cons, MLList.thunk, MLList.squash, MLList.uncons, MLList.uncons?, MLList.forIn, MLList.singletonM, MLList.singleton, MLList.fix, MLList.fix?', MLList.fix?, MLList.iterate, MLList.fixlWith, MLList.fixl, MLList.isEmpty, MLList.ofList, MLList.ofListM, MLList.force, MLList.asArray, MLList.casesM, MLList.cases, MLList.foldsM, MLList.folds, MLList.takeAsList, MLList.takeAsArray, MLList.take, MLList.drop, MLList.mapM, MLList.map, MLList.filterM, MLList.filter, MLList.filterMapM, MLList.filterMap, MLList.takeWhileM, MLList.takeWhile, MLList.append, MLList.join, MLList.enumFrom, MLList.enum, MLList.range, MLList.fin, MLList.ofArray, MLList.chunk, MLList.concat, MLList.zip, MLList.bind, MLList.monadLift, MLList.liftM, MLList.runState, MLList.runState', MLList.runReader, MLList.runStateRef, MLList.head?, MLList.takeUpToFirstM, MLList.takeUpToFirst, MLList.getLast?, MLList.getLast!, MLList.foldM, MLList.fold, MLList.head, MLList.firstM, MLList.first
statement: formalized
proof: formalized
---

# Monadic lazy lists

`Batteries.Data.MLList.Basic`, in [Batteries/Data/MLList/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean), by Mario Carneiro, Keeley Hoek, Simon Hudon, Kim Morrison.

> Lazy lists with "laziness" controlled by an arbitrary monad.

> In an initial section we describe the specification of `MLList`,
> and provide a private unsafe implementation,
> and then a public `opaque` wrapper of this implementation, satisfying the specification.

`MLList` (definition, [line 76](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L76))

> A monadic lazy list, controlled by an arbitrary monad.

```lean
def MLList (m : Type u → Type u) (α : Type u) : Type u
```

`MLList.nil` (definition, [line 81](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L81))

> The empty `MLList`.

```lean
def nil : MLList m α
```

`MLList.cons` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L86))

> Constructs a `MLList` from head and tail.

```lean
def cons : α → MLList m α → MLList m α
```

`MLList.thunk` (definition, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L89))

> Embed a non-monadic thunk as a lazy list.

```lean
def thunk : (Unit → MLList m α) → MLList m α
```

`MLList.squash` (definition, [line 92](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L92))

> Lift a monadic lazy list inside the monad to a monadic lazy list.

```lean
def squash : (Unit → m (MLList m α)) → MLList m α
```

`MLList.uncons` (definition, [line 96](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L96))

> Deconstruct a `MLList`, returning inside the monad an optional pair `α × MLList m α`
> representing the head and tail of the list.

```lean
def uncons [Monad m] : MLList.{u} m α → m (Option (α × MLList m α))
```

`MLList.uncons?` (definition, [line 101](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L101))

> Try to deconstruct a `MLList`, returning an optional pair `α × MLList m α`
> representing the head and tail of the list if it is already evaluated, and `none` otherwise.

```lean
def uncons? : MLList.{u} m α → Option (Option (α × MLList m α))
```

`MLList.forIn` (definition, [line 110](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L110))

> The implementation of `ForIn`, which enables `for a in L do ...` notation.

```lean
protected partial def forIn [Monad m] [Monad n] [MonadLiftT m n]
    (as : MLList m α) (init : δ) (f : α → δ → n (ForInStep δ)) : n δ
```

`MLList.singletonM` (definition, [line 122](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L122))

> Construct a singleton monadic lazy list from a single monadic value.

```lean
def singletonM [Monad m] (x : m α) : MLList m α
```

`MLList.singleton` (definition, [line 126](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L126))

> Construct a singleton monadic lazy list from a single value.

```lean
def singleton [Monad m] (x : α) : MLList m α
```

`MLList.fix` (definition, [line 130](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L130))

> Construct a `MLList` recursively. Failures from `f` will result in `uncons` failing.

```lean
partial def fix [Monad m] (f : α → m α) (x : α) : MLList m α
```

`MLList.fix?'` (definition, [line 139](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L139))

> Constructs an `MLList` recursively, with state in `α`, recording terms from `β`.
> If `f` returns `none` the list will terminate.
>
> Variant of `MLList.fix?` that allows returning values of a different type.

```lean
partial def fix?' [Monad m] (f : α → m (Option (β × α))) (init : α) : MLList m β
```

`MLList.fix?` (definition, [line 150](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L150))

> Constructs an `MLList` recursively. If `f` returns `none` the list will terminate.
>
> Returns the initial value as the first element.

```lean
partial def fix? [Monad m] (f : α → m (Option α)) (x : α) : MLList m α
```

`MLList.iterate` (definition, [line 157](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L157))

> Construct a `MLList` by iteration. (`m` must be a stateful monad for this to be useful.)

```lean
partial def iterate [Monad m] (f : m α) : MLList m α
```

`MLList.fixlWith` (definition, [line 164](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L164))

> Repeatedly apply a function `f : α → m (α × List β)` to an initial `a : α`,
> accumulating the elements of the resulting `List β` as a single monadic lazy list.
>
> (This variant allows starting with a specified `List β` of elements, as well. )

```lean
partial def fixlWith [Monad m] {α β : Type u} (f : α → m (α × List β))
    (s : α) (l : List β) : MLList m β
```

`MLList.fixl` (definition, [line 177](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L177))

> Repeatedly apply a function `f : α → m (α × List β)` to an initial `a : α`,
> accumulating the elements of the resulting `List β` as a single monadic lazy list.

```lean
def fixl [Monad m] {α β : Type u} (f : α → m (α × List β)) (s : α) : MLList m β
```

`MLList.isEmpty` (definition, [line 181](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L181))

> Compute, inside the monad, whether a `MLList` is empty.

```lean
def isEmpty [Monad m] (xs : MLList m α) : m (ULift Bool)
```

`MLList.ofList` (definition, [line 185](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L185))

> Convert a `List` to a `MLList`.

```lean
def ofList : List α → MLList m α
```

`MLList.ofListM` (definition, [line 190](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L190))

> Convert a `List` of values inside the monad into a `MLList`.

```lean
def ofListM [Monad m] : List (m α) → MLList m α
```

`MLList.force` (definition, [line 195](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L195))

> Extract a list inside the monad from a `MLList`.

```lean
partial def force [Monad m] (L : MLList m α) : m (List α)
```

`MLList.asArray` (definition, [line 201](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L201))

> Extract an array inside the monad from a `MLList`.

```lean
def asArray [Monad m] (L : MLList m α) : m (Array α)
```

`MLList.casesM` (definition, [line 209](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L209))

> Performs a monadic case distinction on a `MLList` when the motive is a `MLList` as well.

```lean
def casesM [Monad m] (xs : MLList m α)
    (hnil : Unit → m (MLList m β)) (hcons : α → MLList m α → m (MLList m β)) : MLList m β
```

`MLList.cases` (definition, [line 221](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L221))

> Performs a case distinction on a `MLList` when the motive is a `MLList` as well.
> (We need to be in a monadic context to distinguish a nil from a cons.)

```lean
def cases [Monad m] (xs : MLList m α)
    (hnil : Unit → MLList m β) (hcons : α → MLList m α → MLList m β) : MLList m β
```

`MLList.foldsM` (definition, [line 230](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L230))

> Gives the monadic lazy list consisting all of folds of a function on a given initial element.
> Thus `[a₀, a₁, ...].foldsM f b` will give `[b, ← f b a₀, ← f (← f b a₀) a₁, ...]`.

```lean
partial def foldsM [Monad m] (f : β → α → m β) (init : β) (L : MLList m α) : MLList m β
```

`MLList.folds` (definition, [line 238](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L238))

> Gives the monadic lazy list consisting all of folds of a function on a given initial element.
> Thus `[a₀, a₁, ...].foldsM f b` will give `[b, f b a₀, f (f b a₀) a₁, ...]`.

```lean
def folds [Monad m] (f : β → α → β) (init : β) (L : MLList m α) : MLList m β
```

`MLList.takeAsList` (definition, [line 242](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L242))

> Take the first `n` elements, as a list inside the monad.

```lean
partial def takeAsList [Monad m] (xs : MLList m α) (n : Nat) : m (List α)
```

`MLList.takeAsArray` (definition, [line 254](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L254))

> Take the first `n` elements, as an array inside the monad.

```lean
partial def takeAsArray [Monad m] (xs : MLList m α) (n : Nat) : m (Array α)
```

`MLList.take` (definition, [line 266](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L266))

> Take the first `n` elements.

```lean
partial def take [Monad m] (xs : MLList m α) : Nat → MLList m α
```

`MLList.drop` (definition, [line 271](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L271))

> Drop the first `n` elements.

```lean
def drop [Monad m] (xs : MLList m α) : Nat → MLList m α
```

`MLList.mapM` (definition, [line 276](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L276))

> Apply a function which returns values in the monad to every element of a `MLList`.

```lean
partial def mapM [Monad m] (f : α → m β) (xs : MLList m α) : MLList m β
```

`MLList.map` (definition, [line 280](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L280))

> Apply a function to every element of a `MLList`.

```lean
def map [Monad m] (f : α → β) (L : MLList m α) : MLList m β
```

`MLList.filterM` (definition, [line 284](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L284))

> Filter a `MLList` using a monadic function.

```lean
partial def filterM [Monad m] (p : α → m (ULift Bool)) (L : MLList m α) : MLList m α
```

`MLList.filter` (definition, [line 289](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L289))

> Filter a `MLList`.

```lean
def filter [Monad m] (p : α → Bool) (L : MLList m α) : MLList m α
```

`MLList.filterMapM` (definition, [line 295](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L295))

> Filter and transform a `MLList` using a function that returns values inside the monad.

```lean
partial def filterMapM [Monad m] (f : α → m (Option β)) (xs : MLList m α) : MLList m β
```

`MLList.filterMap` (definition, [line 302](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L302))

> Filter and transform a `MLList` using an `Option` valued function.

```lean
def filterMap [Monad m] (f : α → Option β) : MLList m α → MLList m β
```

`MLList.takeWhileM` (definition, [line 306](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L306))

> Take the initial segment of the lazy list, until the function `f` first returns `false`.

```lean
partial def takeWhileM [Monad m] (f : α → m (ULift Bool)) (L : MLList m α) : MLList m α
```

`MLList.takeWhile` (definition, [line 311](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L311))

> Take the initial segment of the lazy list, until the function `f` first returns `false`.

```lean
def takeWhile [Monad m] (f : α → Bool) : MLList m α → MLList m α
```

`MLList.append` (definition, [line 315](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L315))

> Concatenate two monadic lazy lists.

```lean
partial def append [Monad m] (xs : MLList m α) (ys : Unit → MLList m α) : MLList m α
```

`MLList.join` (definition, [line 319](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L319))

> Join a monadic lazy list of monadic lazy lists into a single monadic lazy list.

```lean
partial def join [Monad m] (xs : MLList m (MLList m α)) : MLList m α
```

`MLList.enumFrom` (definition, [line 323](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L323))

> Enumerate the elements of a monadic lazy list, starting at a specified offset.

```lean
partial def enumFrom [Monad m] (n : Nat) (xs : MLList m α) : MLList m (Nat × α)
```

`MLList.enum` (definition, [line 327](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L327))

> Enumerate the elements of a monadic lazy list.

```lean
def enum [Monad m] : MLList m α → MLList m (Nat × α)
```

`MLList.range` (definition, [line 330](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L330))

> The infinite monadic lazy list of natural numbers.

```lean
def range [Monad m] : MLList m Nat
```

`MLList.fin` (definition, [line 333](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L333))

> Iterate through the elements of `Fin n`.

```lean
partial def fin (n : Nat) : MLList m (Fin n)
```

`MLList.ofArray` (definition, [line 339](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L339))

> Convert an array to a monadic lazy list.

```lean
partial def ofArray {α : Type} (L : Array α) : MLList m α
```

`MLList.chunk` (definition, [line 346](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L346))

> Group the elements of a lazy list into chunks of a given size.
> If the lazy list is finite, the last chunk may be smaller (possibly even length 0).

```lean
partial def chunk [Monad m] (L : MLList m α) (n : Nat) : MLList m (Array α)
```

`MLList.concat` (definition, [line 357](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L357))

> Add one element to the end of a monadic lazy list.

```lean
def concat [Monad m] (L : MLList m α) (a : α) : MLList m α
```

`MLList.zip` (definition, [line 360](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L360))

> Take the product of two monadic lazy lists.

```lean
partial def zip [Monad m] (L : MLList m α) (M : MLList m β) : MLList.{u} m (α × β)
```

`MLList.bind` (definition, [line 367](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L367))

> Apply a function returning a monadic lazy list to each element of a monadic lazy list,
> joining the results.

```lean
partial def bind [Monad m] (xs : MLList m α) (f : α → MLList m β) : MLList m β
```

`MLList.monadLift` (definition, [line 374](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L374))

> Convert any value in the monad to the singleton monadic lazy list.

```lean
def monadLift [Monad m] (x : m α) : MLList m α
```

`MLList.liftM` (definition, [line 378](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L378))

> Lift the monad of a lazy list.

```lean
partial def liftM [Monad m] [Monad n] [MonadLiftT m n] (L : MLList m α) : MLList n α
```

`MLList.runState` (definition, [line 385](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L385))

> Given a lazy list in a state monad, run it on some initial state, recording the states.

```lean
partial def runState [Monad m] (L : MLList (StateT.{u} σ m) α) (s : σ) : MLList m (α × σ)
```

`MLList.runState'` (definition, [line 392](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L392))

> Given a lazy list in a state monad, run it on some initial state.

```lean
def runState' [Monad m] (L : MLList (StateT.{u} σ m) α) (s : σ) : MLList m α
```

`MLList.runReader` (definition, [line 396](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L396))

> Run a lazy list in a `ReaderT` monad on some fixed state.

```lean
partial def runReader [Monad m] (L : MLList (ReaderT.{u, u} ρ m) α) (r : ρ) :
    MLList m α
```

`MLList.runStateRef` (definition, [line 404](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L404))

> Run a lazy list in a `StateRefT'` monad on some initial state.

```lean
partial def runStateRef [Monad m] [MonadLiftT (ST ω) m] (L : MLList (StateRefT' ω σ m) α) (s : σ) :
    MLList m α
```

`MLList.head?` (definition, [line 412](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L412))

> Return the head of a monadic lazy list if it exists, as an `Option` in the monad.

```lean
def head? [Monad m] (L : MLList m α) : m (Option α)
```

`MLList.takeUpToFirstM` (definition, [line 416](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L416))

> Take the initial segment of the lazy list,
> up to and including the first place where `f` gives `true`.

```lean
partial def takeUpToFirstM [Monad m] (L : MLList m α) (f : α → m (ULift Bool)) : MLList m α
```

`MLList.takeUpToFirst` (definition, [line 422](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L422))

> Take the initial segment of the lazy list,
> up to and including the first place where `f` gives `true`.

```lean
def takeUpToFirst [Monad m] (L : MLList m α) (f : α → Bool) : MLList m α
```

`MLList.getLast?` (definition, [line 427](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L427))

> Gets the last element of a monadic lazy list, as an option in the monad.
> This will run forever if the list is infinite.

```lean
partial def getLast? [Monad m] (L : MLList m α) : m (Option α)
```

`MLList.getLast!` (definition, [line 440](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L440))

> Gets the last element of a monadic lazy list, or the default value if the list is empty.
> This will run forever if the list is infinite.

```lean
partial def getLast! [Monad m] [Inhabited α] (L : MLList m α) : m α
```

`MLList.foldM` (definition, [line 444](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L444))

> Folds a binary function across a monadic lazy list, from an initial starting value.
> This will run forever if the list is infinite.

```lean
partial def foldM [Monad m] (f : β → α → m β) (init : β) (L : MLList m α) : m β
```

`MLList.fold` (definition, [line 449](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L449))

> Folds a binary function across a monadic lazy list, from an initial starting value.
> This will run forever if the list is infinite.

```lean
partial def fold [Monad m] (f : β → α → β) (init : β) (L : MLList m α) : m β
```

`MLList.head` (definition, [line 456](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L456))

> Return the head of a monadic lazy list, as a value in the monad.
> Fails if the list is empty.

```lean
def head [AlternativeMonad m] (L : MLList m α) : m α
```

`MLList.firstM` (definition, [line 464](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L464))

> Apply a function returning values inside the monad to a monadic lazy list,
> returning only the first successful result.

```lean
def firstM [AlternativeMonad m] (L : MLList m α) (f : α → m (Option β)) : m β
```

`MLList.first` (definition, [line 468](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean#L468))

> Return the first value on which a predicate returns true.

```lean
def first [AlternativeMonad m] (L : MLList m α) (p : α → Bool) : m α
```

## Depends on

- [Laws for Monads with Failure](../../../control/alternativemonad.md)

## Sources

- [Batteries/Data/MLList/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Basic.lean)
