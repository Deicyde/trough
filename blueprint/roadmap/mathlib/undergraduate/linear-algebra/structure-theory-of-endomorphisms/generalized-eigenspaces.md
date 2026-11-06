# Generalized eigenspaces

The submodule `genEigenspace f μ k` for a linear map `f`, a scalar `μ`,
and a number `k : ℕ∞` is the kernel of `(f - μ • id) ^ k` if `k` is a natural number,
or the union of all these kernels if `k = ∞`. (`k = ∞` corresponds to Def 8.19 of [axler2024](https://leanprover-community.github.io/mathlib4_docs/references.html#ref_axler2024).)
A generalized eigenspace for some exponent `k` is contained in
the generalized eigenspace for exponents larger than `k`.

```lean
Module.End.genEigenspace.{v, w} {R : Type v} {M : Type w} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] (f : Module.End R M) (μ : R) : ℕ∞ →o Submodule R M
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Kernel of a linear map](../fundamentals/kernel-of-a-linear-map.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Module.End.genEigenspace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Basic.html#Module.End.genEigenspace)
- [Source of `Module.End.genEigenspace` in Mathlib/LinearAlgebra/Eigenspace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Eigenspace/Basic.lean#L67)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L64)
