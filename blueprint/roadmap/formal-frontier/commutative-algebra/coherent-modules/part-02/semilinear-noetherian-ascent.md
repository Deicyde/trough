---
declaration: theorem
origin: cited
lean: isNoetherian_of_left_inv_smul_mem_range
statement: formalized
proof: formalized
---

# Semilinear Noetherian ascent

For arbitrary semirings `R`, `S`, additive
commutative semimodules `M`, `N` and `f : M →ₛₗ[φ] N`,
[`isNoetherian_of_left_inv_smul_mem_range`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean)
transfers `IsNoetherian R M` to `IsNoetherian S N` if each `n` admits
`m, a, b` with `b * a = 1` and `f m = a • n`. The four universes are
independent; neither `φ` nor `f` must be surjective. The
`isNoetherian_of_unit_smul_mem_range` corollary retains the familiar
unit-clearing hypothesis, while `isNoetherian_of_surjective_semilinear`
requires only function-surjectivity of `f`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `isNoetherian_of_left_inv_smul_mem_range` (theorem), declared in [CoherentModules/RingTheory/Noetherian.lean, line 110](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L110).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `isNoetherian_of_left_inv_smul_mem_range` in CoherentModules/RingTheory/Noetherian.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L110)
