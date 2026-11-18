---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Stlc.PreservesTyping, Cslib.LambdaCalculus.LocallyNameless.Stlc.FullBeta.preservation, Cslib.LambdaCalculus.LocallyNameless.Stlc.FullBeta.progress
statement: formalized
proof: formalized
---

# λ-calculus (Stlc/Safety)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Stlc.Safety`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean), by Chris Henson.

> Type safety of the simply typed λ-calculus, with a locally nameless representation of syntax.
> Theorems in this file are namespaced by their respective reductions.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is partially adapted

`Cslib.LambdaCalculus.LocallyNameless.Stlc.PreservesTyping` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean#L39))

> A relation on terms preserves typing if all related terms have the same type.

```lean
def PreservesTyping (R : Term Var → Term Var → Prop) (Base : Type v)
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.FullBeta.preservation` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean#L51))

> Typing preservation for full beta reduction.

```lean
theorem preservation : PreservesTyping (Var := Var) (· ⭢βᶠ ·) Base
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.FullBeta.progress` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean#L63))

> A typed term either full beta reduces or is a value.

```lean
theorem progress {t : Term Var} {τ : Ty Base} (ht : [] ⊢ t ∶ τ) : t.Value ∨ ∃ t', t ⭢βᶠ t'
```

## Depends on

- [Relations: Definitions](../../../../foundations/relation/defs.md)
- [λ-calculus (Stlc/Basic)](basic.md)
- [β-reduction for the λ-calculus](../untyped/fullbeta.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Safety.lean)
