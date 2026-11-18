---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.preservation, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.progress
statement: formalized
proof: formalized
---

# λ-calculus (Fsub/Safety)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Safety`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file proves type safety.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.preservation` (lemma, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean#L37))

> Any reduction step preserves typing.

```lean
lemma Typing.preservation (der : Typing Γ t τ) (step : t ⭢βᵛ t') : Typing Γ t' τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.progress` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean#L76))

> Any typable term either has a reduction step or is a value.

```lean
lemma Typing.progress (der : Typing [] t τ) : t.Value ∨ ∃ t', t ⭢βᵛ t'
```

## Depends on

- [λ-calculus (Typing)](typing.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Safety.lean)
