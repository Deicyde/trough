---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Context, Cslib.LambdaCalculus.LocallyNameless.Context.dom, Cslib.LambdaCalculus.LocallyNameless.Context.haswellformed_def, Cslib.LambdaCalculus.LocallyNameless.Context.mapVal, Cslib.LambdaCalculus.LocallyNameless.Context.mapVal_keys, Cslib.LambdaCalculus.LocallyNameless.Context.mapVal_mem
statement: formalized
proof: formalized
---

# λ-calculus (Context)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Context`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean), by Chris Henson.

> Contexts as pairs of free variables and types.

`Cslib.LambdaCalculus.LocallyNameless.Context` (abbreviation, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L33))

> A typing context is a list of free variables and corresponding types.

```lean
abbrev Context (α : Type u) (β : Type v)
```

`Cslib.LambdaCalculus.LocallyNameless.Context.dom` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L58))

> The domain of a context is the finite set of free variables it uses.

```lean
def dom (Γ : Context α β) : Finset α
```

`Cslib.LambdaCalculus.LocallyNameless.Context.haswellformed_def` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L65))

```lean
theorem haswellformed_def (Γ : Context α β) : Γ✓ = Γ.NodupKeys
```

`Cslib.LambdaCalculus.LocallyNameless.Context.mapVal` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L71))

> A mapping of values within a context.

```lean
def mapVal (f : β → β) (Γ : Context α β) : Context α β
```

`Cslib.LambdaCalculus.LocallyNameless.Context.mapVal_keys` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L77))

> A mapping of values preserves keys.

```lean
lemma mapVal_keys (f : β → β) : Γ.keys = (Γ.mapVal f).keys
```

`Cslib.LambdaCalculus.LocallyNameless.Context.mapVal_mem` (lemma, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean#L81))

> A mapping of values maps lookups.

```lean
lemma mapVal_mem {x : α} {σ : β} (mem : σ ∈ Γ.dlookup x) (f : β → β) :
    f σ ∈ (Γ.mapVal f).dlookup x
```

## Depends on

- [HasWellFormed](../../../foundations/syntax/haswellformed.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Context.lean)
