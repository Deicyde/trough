---
declaration: theorem
origin: cited
lean: Module.forall_maximal_smul_top_ne_top_iff_forall_finite_tensorProduct
statement: formalized
proof: formalized
---

# Finite-module tensor zero detection

For an arbitrary additive commutative
`R`-module `P` over a `CommRing R`,
[`Module.forall_maximal_smul_top_ne_top_iff_forall_finite_tensorProduct`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean)
characterizes zero-object detection on all finite modules by
`m • (⊤ : Submodule R P) ≠ ⊤` for every maximal ideal `m`.
[`Module.subsingleton_tensorProduct_iff_of_finite`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean)
gives `Subsingleton (P ⊗[R] M) ↔ Subsingleton M` for a single finite module
in an independent universe. No flatness, faithfulness or finiteness of `P`
is required. This detects zero objects, not zero maps or isomorphisms. The
[clients](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/LinearAlgebra/TensorProduct/FiniteDetection.lean)
recover the finite faithfully-flat and local residue-field criteria and use
a countable direct sum of residue fields.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.forall_maximal_smul_top_ne_top_iff_forall_finite_tensorProduct` (theorem), declared in [CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean, line 76](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean#L76).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.forall_maximal_smul_top_ne_top_iff_forall_finite_tensorProduct` in CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/FiniteDetection.lean#L76)
