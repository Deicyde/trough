---
declaration: theorem
origin: cited
lean: Module.Flat.semilinearEquiv_iff
statement: formalized
proof: formalized
---

# Semilinear invariance of flatness

For equivalent commutative semirings
`e : R ≃+* S` and a compatible semilinear equivalence from an additive
commutative `R`-module `M` to an additive commutative `S`-module `N`,
[`Module.Flat.semilinearEquiv_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Equiv.lean)
gives `Module.Flat R M ↔ Module.Flat S N` for both given scalar actions.
`Module.Flat.of_semilinearEquiv e E` takes flatness of `N` to flatness of `M`.
The four carrier universes are independent. Over semirings, this is Mathlib's
mono-flatness (tensoring preserves injective linear maps); over rings it is
usual flatness. No faithful action, finiteness or additive cancellation is
required. The identity coefficient equivalence accepts the same ordinary
linear equivalence as Mathlib's fixed-ring flatness API.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.Flat.semilinearEquiv_iff` (theorem), declared in [CoherentModules/RingTheory/Flat/Equiv.lean, line 82](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Equiv.lean#L82).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.Flat.semilinearEquiv_iff` in CoherentModules/RingTheory/Flat/Equiv.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Equiv.lean#L82)
