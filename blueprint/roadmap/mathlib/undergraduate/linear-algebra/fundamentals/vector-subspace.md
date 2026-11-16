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
- [Source of `Subspace` in Mathlib/Algebra/Module/Submodule/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Module/Submodule/Basic.lean#L178)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L9)
