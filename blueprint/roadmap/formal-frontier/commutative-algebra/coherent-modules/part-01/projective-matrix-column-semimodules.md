---
declaration: theorem
origin: cited
lean: Matrix.Module.projective_iff
statement: formalized
proof: formalized
---

# Projective matrix-column semimodules

For a semiring `R`, an additive
commutative monoid `M` with its given `R`-module structure, and a finite type `I`
with decidable equality,
[`Matrix.Module.projective_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/Projective.lean)
characterizes projectivity of the canonical `Matrix I I R`-module on `I → M` by
`IsEmpty I ∨ Module.Projective R M`. In particular, for inhabited `I`, projectivity
is equivalent to that of `M` over `R`. No coefficient commutativity or additive
inverses are required, and the carrier universes are independent.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Matrix.Module.projective_iff` (theorem), declared in [CoherentModules/LinearAlgebra/Matrix/Projective.lean, line 176](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/Projective.lean#L176).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Matrix.Module.projective_iff` in CoherentModules/LinearAlgebra/Matrix/Projective.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/Projective.lean#L176)
