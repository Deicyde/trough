# Sum of subspaces

Mathlib states this as `Submodule.completeLattice`.

```lean
Submodule.completeLattice.{u_1, u_3} {R : Type u_1} {M : Type u_3} [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] : CompleteLattice (Submodule R M)
```

## Depends on

- [Module](../../../overview/linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Submodule.completeLattice`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Submodule/Lattice.html#Submodule.completeLattice)
- [Source of `Submodule.completeLattice` in Mathlib/Algebra/Module/Submodule/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Module/Submodule/Lattice.lean#L195)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L11)
