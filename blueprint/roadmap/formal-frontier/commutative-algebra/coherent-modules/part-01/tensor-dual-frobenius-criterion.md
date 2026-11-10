---
declaration: theorem
origin: cited
lean: Module.Dual.exists_nondegenerate_mul_of_tensorProduct_equiv
statement: formalized
proof: formalized
---

# Tensor–dual Frobenius criterion

For a finite-dimensional, possibly
noncommutative or zero algebra `A` over a field `K`,
[`Module.Dual.exists_nondegenerate_mul_of_tensorProduct_equiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/TensorProduct.lean)
produces a functional `λ` with both-sided nondegenerate pairing `λ(a * x)`
from a subspace `C` of the original dual and an equivalence
`e : C ⊗[K] A ≃ₗ[K] Module.Dual K A` satisfying
`e (c ⊗ₜ a) x = c (a * x)`. The algebra needs only `Semiring A`;
finiteness of `C` is derived, and the scalar and algebra universes are independent.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.Dual.exists_nondegenerate_mul_of_tensorProduct_equiv` (theorem), declared in [CoherentModules/LinearAlgebra/Dual/TensorProduct.lean, line 38](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/TensorProduct.lean#L38).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.Dual.exists_nondegenerate_mul_of_tensorProduct_equiv` in CoherentModules/LinearAlgebra/Dual/TensorProduct.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/TensorProduct.lean#L38)
