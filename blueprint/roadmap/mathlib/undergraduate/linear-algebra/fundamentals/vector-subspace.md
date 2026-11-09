# Vector subspace

Subspace of a vector space. Defined to equal `Submodule`.

```lean
Subspace.{u, v} (R : Type u) (M : Type v) [DivisionRing R] [AddCommGroup M] [_root_.Module R M] :
  Type v
```

## Depends on

- [Module](../../../overview/linear-algebra/fundamentals/module.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Subspace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Submodule/Basic.html#Subspace)
- [Source of `Subspace` in Mathlib/Algebra/Module/Submodule/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Module/Submodule/Basic.lean#L177)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L9)
