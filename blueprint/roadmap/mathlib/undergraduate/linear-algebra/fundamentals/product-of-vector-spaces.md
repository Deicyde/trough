# Product of vector spaces

Mathlib states this as `Prod.instModule`.

```lean
Prod.instModule.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2} {N : Type u_3} [Semiring R]
  [AddCommMonoid M] [AddCommMonoid N] [_root_.Module R M] [_root_.Module R N] :
  _root_.Module R (M × N)
```

## Depends on

- [Module](../../../overview/linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Prod.instModule`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Prod.html#Prod.instModule)
- [Source of `Prod.instModule` in Mathlib/Algebra/Module/Prod.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Module/Prod.lean#L24)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L8)
