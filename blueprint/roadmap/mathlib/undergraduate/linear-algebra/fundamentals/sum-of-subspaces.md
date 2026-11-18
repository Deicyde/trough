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
- [Source of `Submodule.completeLattice` in Mathlib/Algebra/Module/Submodule/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Module/Submodule/Lattice.lean#L194)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L11)
