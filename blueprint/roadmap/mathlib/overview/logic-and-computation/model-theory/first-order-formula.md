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
- [Source of `FirstOrder.Language.Formula` in Mathlib/ModelTheory/Syntax.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/ModelTheory/Syntax.lean#L318)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L637)
