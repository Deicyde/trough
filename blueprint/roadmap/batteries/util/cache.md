---
catalog: module
lean: Batteries.Tactic.Cache, Batteries.Tactic.Cache.mk, Lean.Meta.wrapAsync, Batteries.Tactic.Cache.get, Batteries.Tactic.DeclCache, Batteries.Tactic.DeclCache.mk, Batteries.Tactic.DeclCache.get, Batteries.Tactic.DiscrTreeCache, Batteries.Tactic.DiscrTreeCache.mk, Batteries.Tactic.DiscrTreeCache.getMatch
statement: formalized
proof: formalized
---

# Once-per-file cache for tactics

`Batteries.Util.Cache`, in [Batteries/Util/Cache.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean), by Gabriel Ebner.

> This file defines cache data structures for tactics
> that are initialized the first time they are accessed.
> Since Lean 4 starts one process per file, these caches are once-per-file
> and can for example be used to cache information about the imported modules.
>
> The `Cache α` data structure is the most generic version we define.
> It is created using `Cache.mk f` where `f : MetaM α` performs the initialization of the cache:
> ```
> initialize numberOfImports : Cache Nat ← Cache.mk do
>   (← getEnv).imports.size
>
> -- (does not work in the same module where the cache is defined)
> #eval show MetaM Nat from numberOfImports.get
> ```
>
> The `DeclCache α` data structure computes a fold over the environment's constants:
> `DeclCache.mk empty f` constructs such a cache
> where `empty : α` and `f : Name → ConstantInfo → α → MetaM α`.
> The result of the constants in the imports is cached between tactic invocations,
> while for constants defined in the same file `f` is evaluated again every time.
> This kind of cache can be used e.g. to populate discrimination trees.

`Batteries.Tactic.Cache` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L44))

> Once-per-file cache.

```lean
def Cache (α : Type)
```

`Batteries.Tactic.Cache.mk` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L52))

> Creates a cache with an initialization function.

```lean
def Cache.mk (init : MetaM α) : IO (Cache α)
```

`Lean.Meta.wrapAsync` (definition, [line 55](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L55))

```lean
def _root_.Lean.Meta.wrapAsync {α : Type} (act : α → MetaM β)  (cancelTk? : Option IO.CancelToken) :
    MetaM (α → EIO Exception β)
```

`Batteries.Tactic.Cache.get` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L65))

> Access the cache. Calling this function for the first time will initialize the cache
> with the function provided in the constructor.

```lean
def Cache.get (cache : Cache α) : MetaM α
```

`Batteries.Tactic.DeclCache` (structure, [line 80](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L80))

> Cached fold over the environment's declarations,
> where a given function is applied to `α` for every constant.

```lean
structure DeclCache (α : Type) where mk' ::
  /-- The cached data. -/
  cache : Cache α
  /-- Function for adding a declaration from the current file to the cache. -/
  addDecl : Name → ConstantInfo → α → MetaM α
  /-- Function for adding a declaration from the library to the cache.
  Defaults to the same behaviour as adding a declaration from the current file. -/
  addLibraryDecl : Name → ConstantInfo → α → MetaM α := addDecl
  deriving Nonempty
```

`Batteries.Tactic.DeclCache.mk` (definition, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L104))

> Creates a `DeclCache`.
>
> First, if `pre` is nonempty, run that for a value,
> and if successful populate the cache with that value.
>
> If `pre` is empty, or it fails,
> the cached structure `α` is initialized with `empty`,
> and then `addLibraryDecl` is called for every imported constant.
> After all imported constants have been added, we run `post`.
> Finally, the result is cached.
>
> When `get` is called, `addDecl` is also called for every constant in the current file.

```lean
def DeclCache.mk (profilingName : String) (pre : MetaM α := failure) (empty : α)
    (addDecl : Name → ConstantInfo → α → MetaM α)
    (addLibraryDecl : Name → ConstantInfo → α → MetaM α := addDecl)
    (post : α → MetaM α := fun a => pure a) : IO (DeclCache α)
```

`Batteries.Tactic.DeclCache.get` (definition, [line 125](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L125))

> Access the cache. Calling this function for the first time will initialize the cache
> with the function provided in the constructor.

```lean
def DeclCache.get (cache : DeclCache α) : MetaM α
```

`Batteries.Tactic.DiscrTreeCache` (definition, [line 134](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L134))

> A type synonym for a `DeclCache` containing a pair of discrimination trees.
> The first will store declarations in the current file,
> the second will store declarations from imports (and will hopefully be "read-only" after creation).

```lean
def DiscrTreeCache (α : Type) : Type
```

`Batteries.Tactic.DiscrTreeCache.mk` (definition, [line 140](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L140))

> Build a `DiscrTreeCache`,
> from a function that returns a collection of keys and values for each declaration.

```lean
def DiscrTreeCache.mk [BEq α] (profilingName : String)
    (processDecl : Name → ConstantInfo → MetaM (Array (Array DiscrTree.Key × α)))
    (post? : Option (Array α → Array α) := none)
    (init : MetaM (DiscrTree α) := failure) :
    IO (DiscrTreeCache α)
```

`Batteries.Tactic.DiscrTreeCache.getMatch` (definition, [line 167](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean#L167))

> Get matches from both the discrimination tree for declarations in the current file,
> and for the imports.
>
> Note that if you are calling this multiple times with the same environment,
> it will rebuild the discrimination tree for the current file multiple times,
> and it would be more efficient to call `c.get` once,
> and then call `DiscrTree.getMatch` multiple times.

```lean
def DiscrTreeCache.getMatch (c : DiscrTreeCache α) (e : Expr) : MetaM (Array α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/Cache.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/Cache.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.Cache.json)
