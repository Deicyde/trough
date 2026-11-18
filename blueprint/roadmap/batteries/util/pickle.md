---
catalog: module
lean: pickle, unpickle, withUnpickle
statement: formalized
proof: formalized
---

# Pickling and unpickling objects

`Batteries.Util.Pickle`, in [Batteries/Util/Pickle.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Pickle.lean), by Mario Carneiro.

> By abusing `saveModuleData` and `readModuleData` we can pickle and unpickle objects to disk.

`pickle` (definition, [line 25](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Pickle.lean#L25))

> Save an object to disk.
> If you need to write multiple objects from within a single declaration,
> you will need to provide a unique `key` for each.

```lean
def pickle {α : Type} (path : FilePath) (x : α) (key : Name := by exact decl_name%) : IO Unit
```

`unpickle` (definition, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Pickle.lean#L38))

> Load an object from disk.
> Note: The returned `CompactedRegion` can be used to free the memory behind the value
> of type `α`, using `CompactedRegion.free` (which is only safe once all references to the `α` are
> released). Ignoring the `CompactedRegion` results in the data being leaked.
> Use `withUnpickle` to call `CompactedRegion.free` automatically.
>
> This function is unsafe because the data being loaded may not actually have type `α`, and this
> may cause crashes or other bad behavior.

```lean
unsafe def unpickle (α : Type) (path : FilePath) : IO (α × CompactedRegion)
```

`withUnpickle` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Pickle.lean#L42))

> Load an object from disk and run some continuation on it, freeing memory afterwards.

```lean
unsafe def withUnpickle [Monad m] [MonadLiftT IO m] {α β : Type}
    (path : FilePath) (f : α → m β) : m β
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/Pickle.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Pickle.lean)
