---
declaration: theorem
origin: cited
lean: Ideal.hasSubmoduleAdicCofinality_iff_forall_map_evalRingHom
statement: formalized
proof: formalized
---

# Adic cofinality on finite products

For an arbitrary ideal `I` of
`Π i, R i`, with `[Finite ι]` and commutative rings `R i`,
[`Ideal.hasSubmoduleAdicCofinality_iff_forall_map_evalRingHom`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicProducts.lean)
gives (AP) for `I` iff each projection image `I.map (Pi.evalRingHom R i)`
has (AP). The companion
`hasFiniteSubmoduleAdicCofinality_iff_forall_map_evalRingHom` does the same
for (APf). The [characteristic criteria](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicProducts.lean)
also cover unary `Ideal.pi` and binary `Ideal.prod`, with independent binary
ring universes. Empty products and zero factors are allowed. Full (AP)
covers every submodule of every finite module; (APf) requires only the
submodule to be finitely generated. No ideal-FG, Noetherian or ambient
finite-presentation hypothesis is added. Infinite products are not covered
by these equivalences.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.hasSubmoduleAdicCofinality_iff_forall_map_evalRingHom` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicProducts.lean, line 104](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicProducts.lean#L104).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.hasSubmoduleAdicCofinality_iff_forall_map_evalRingHom` in CoherentModules/RingTheory/Ideal/AdicProducts.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicProducts.lean#L104)
