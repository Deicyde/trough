# First-order structure

A first-order structure on a type `M` consists of interpretations of all the symbols in a given
language. Each function of arity `n` is interpreted as a function sending tuples of length `n`
(modeled as `(Fin n → M)`) to `M`, and a relation of arity `n` is a function from tuples of length
`n` to `Prop`.

```lean
FirstOrder.Language.Structure.{u, v, w} (L : FirstOrder.Language) (M : Type w) :
  Type (max (max u v) w)
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Structure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Basic.html#FirstOrder.Language.Structure)
- [Source of `FirstOrder.Language.Structure` in Mathlib/ModelTheory/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/ModelTheory/Basic.lean#L150)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L636)
