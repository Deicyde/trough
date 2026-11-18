# First-order formula

`Formula α` is the type of formulas with free variables indexed by `α` and no bound variables in
scope.

```lean
FirstOrder.Language.Formula.{u, v, u'} (L : FirstOrder.Language) (α : Type u') : Type (max u v u')
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Formula`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Syntax.html#FirstOrder.Language.Formula)
- [Source of `FirstOrder.Language.Formula` in Mathlib/ModelTheory/Syntax.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/ModelTheory/Syntax.lean#L318)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L637)
