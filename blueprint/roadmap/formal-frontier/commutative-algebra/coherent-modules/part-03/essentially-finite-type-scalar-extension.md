---
declaration: theorem
origin: cited
lean: Algebra.EssFiniteType.isNoetherian_tensorProduct
statement: formalized
proof: formalized
---

# Essentially finite-type scalar extension

For commutative rings `R`, `S`,
an essentially finite-type `R`-algebra structure on `S`, and a Noetherian
`R`-module `M`,
[`Algebra.EssFiniteType.isNoetherian_tensorProduct`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/Noetherian.lean)
makes `S ⊗[R] M` Noetherian over `S` with its canonical left-factor action.
The three universes are independent, and `M` need only be an additive
commutative monoid with its given module structure. Neither ambient ring
must be Noetherian; no flatness, faithfulness or finite presentation is
assumed. This includes finite-type algebras and arbitrary localizations.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Algebra.EssFiniteType.isNoetherian_tensorProduct` (theorem), declared in [CoherentModules/LinearAlgebra/TensorProduct/Noetherian.lean, line 43](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/Noetherian.lean#L43).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Algebra.EssFiniteType.isNoetherian_tensorProduct` in CoherentModules/LinearAlgebra/TensorProduct/Noetherian.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/TensorProduct/Noetherian.lean#L43)
