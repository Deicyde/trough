---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Module.Basis.ofVectorSpace
mathlib_file: Mathlib/LinearAlgebra/Basis/VectorSpace.lean
---

# Existence of bases

Each vector space has a basis.

```lean
Module.Basis.ofVectorSpace.{u_3, u_4} (K : Type u_3) (V : Type u_4) [DivisionRing K]
  [AddCommGroup V] [_root_.Module K V] : Module.Basis (↑(Module.Basis.ofVectorSpaceIndex K V)) K V
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Generating sets](generating-sets.md)
- [Linear independence](linear-independence.md)
- [Range of a linear map](range-of-a-linear-map.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `Module.Basis.ofVectorSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis/VectorSpace.html#Module.Basis.ofVectorSpace)
- [Source of `Module.Basis.ofVectorSpace` in Mathlib/LinearAlgebra/Basis/VectorSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Basis/VectorSpace.lean#L151)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L17)
