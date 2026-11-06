# Algebra of endomorphisms of a vector space

Mathlib states this as `Module.End.instAlgebra`.

```lean
Module.End.instAlgebra.{u, v, w} (R : Type u) (S : Type v) (M : Type w) [CommSemiring R]
  [Semiring S] [AddCommMonoid M] [_root_.Module R M] [_root_.Module S M] [SMulCommClass S R M]
  [SMul R S] [IsScalarTower R S M] : Algebra R (Module.End S M)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `Module.End.instAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Basic.html#Module.End.instAlgebra)
- [Source of `Module.End.instAlgebra` in Mathlib/Algebra/Algebra/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Algebra/Basic.lean#L204)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L21)
