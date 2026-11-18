---
catalog: module
lean: FloatArray.mapMUnsafe, FloatArray.mapM, FloatArray.map
statement: formalized
proof: formalized
---

# FloatArray

`Batteries.Data.FloatArray`, in [Batteries/Data/FloatArray.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/FloatArray.lean), by François G. Dorais.

`FloatArray.mapMUnsafe` (definition, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/FloatArray.lean#L21))

> Unsafe optimized implementation of `mapM`.
>
> This function is unsafe because it relies on the implementation limit that the size of an array is
> always less than `USize.size`.

```lean
unsafe def mapMUnsafe [Monad m] (a : FloatArray) (f : Float → m Float) : m FloatArray
```

`FloatArray.mapM` (definition, [line 36](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/FloatArray.lean#L36))

> `mapM f a` applies the monadic function `f` to each element of the array.

```lean
def mapM [Monad m] (a : FloatArray) (f : Float → m Float) : m FloatArray
```

`FloatArray.map` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/FloatArray.lean#L44))

> `map f a` applies the function `f` to each element of the array.

```lean
def map (a : FloatArray) (f : Float → Float) : FloatArray
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/FloatArray.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/FloatArray.lean)
