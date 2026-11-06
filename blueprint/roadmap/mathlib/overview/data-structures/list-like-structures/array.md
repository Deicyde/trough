# Array

`Array α` is the type of [dynamic arrays](https://en.wikipedia.org/wiki/Dynamic_array) with elements
from `α`. This type has special support in the runtime.

Arrays perform best when unshared. As long as there is never more than one reference to an array,
all updates will be performed _destructively_. This results in performance comparable to mutable
arrays in imperative programming languages.

An array has a size and a capacity. The size is the number of elements present in the array, while
the capacity is the amount of memory currently allocated for elements. The size is accessible via
`Array.size`, but the capacity is not observable from Lean code. `Array.emptyWithCapacity n` creates
an array which is equal to `#[]`, but internally allocates an array of capacity `n`. When the size
exceeds the capacity, allocation is required to grow the array.

From the point of view of proofs, `Array α` is just a wrapper around `List α`.

```lean
Array.{u} (α : Type u) : Type u
```

## Depends on

- [List](list.md)

## Sources

- [Mathlib documentation: `Array`](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Array)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L570)
