---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Algebra.TensorProduct.instAlgebra
mathlib_file: Mathlib/RingTheory/TensorProduct/Basic.lean
---

# Tensor product of algebras

The tensor product of two `R`-algebras is an `R`-algebra.

```lean
Algebra.TensorProduct.instAlgebra.{uR, uA, uB} {R : Type uR} {A : Type uA} {B : Type uB}
  [CommSemiring R] [Semiring A] [Algebra R A] [Semiring B] [Algebra R B] :
  Algebra R (TensorProduct R A B)
```

## Depends on

- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Tensor product](../../linear-algebra/fundamentals/tensor-product.md)

## Sources

- [Mathlib documentation: `Algebra.TensorProduct.instAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.instAlgebra)
- [Source of `Algebra.TensorProduct.instAlgebra` in Mathlib/RingTheory/TensorProduct/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/TensorProduct/Basic.lean#L247)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L113)
