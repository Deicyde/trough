# Orthogonality

The `dualAnnihilator` of a submodule `W` is the set of linear maps `φ` such
that `φ w = 0` for all `w ∈ W`.

```lean
Submodule.dualAnnihilator.{u_3, u_4} {R : Type u_3} {M : Type u_4} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] (W : Submodule R M) : Submodule R (Module.Dual R M)
```

## Depends on

- [Dual vector space](../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Kernel of a linear map](../fundamentals/kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Submodule.dualAnnihilator`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Defs.html#Submodule.dualAnnihilator)
- [Source of `Submodule.dualAnnihilator` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Dual/Defs.lean#L325)
- [Mathlib undergraduate list: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L27)
