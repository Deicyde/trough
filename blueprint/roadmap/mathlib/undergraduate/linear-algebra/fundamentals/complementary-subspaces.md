# Complementary subspaces

Mathlib states this as `Submodule.exists_isCompl`.

```lean
Submodule.exists_isCompl.{u_3, u_4} {K : Type u_3} {V : Type u_4} [DivisionRing K] [AddCommGroup V]
  [_root_.Module K V] (p : Submodule K V) : ∃ q, IsCompl p q
```

## Depends on

- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Sum of subspaces](sum-of-subspaces.md)

## Proof depends on

- [Existence of bases](existence-of-bases.md)
- [Kernel of a linear map](kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Submodule.exists_isCompl`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis/VectorSpace.html#Submodule.exists_isCompl)
- [Source of `Submodule.exists_isCompl` in Mathlib/LinearAlgebra/Basis/VectorSpace.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Basis/VectorSpace.lean#L280)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L13)
