---
catalog: module
lean: Relation.preserves_reflGen_iff, Relation.preserves_transGen_iff, Relation.preserves_reflTransGen_iff
statement: formalized
proof: formalized
---

# Relations: preservation of properties

`Cslib.Foundations.Relation.Preserves`, in [Cslib/Foundations/Relation/Preserves.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Preserves.lean), by Fabrizio Montesi.

`Relation.preserves_reflGen_iff` (theorem, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Preserves.lean#L22))

> A predicate preserved by a relation is also preserved by its reflexive closure.

```lean
theorem preserves_reflGen_iff : Preserves (ReflGen r) P  ↔ Preserves r P
```

`Relation.preserves_transGen_iff` (theorem, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Preserves.lean#L26))

> A predicate preserved by a relation is also preserved by its transitive closure.

```lean
theorem preserves_transGen_iff : Preserves (TransGen r) P ↔ Preserves r P
```

`Relation.preserves_reflTransGen_iff` (theorem, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Preserves.lean#L35))

> A predicate is preserved by a relation iff it is preserves by its reflexive and transitive
> closure.

```lean
theorem preserves_reflTransGen_iff : Preserves (ReflTransGen r) P ↔ Preserves r P
```

## Depends on

- [Relations: Definitions](defs.md)

## Sources

- [Cslib/Foundations/Relation/Preserves.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Preserves.lean)
