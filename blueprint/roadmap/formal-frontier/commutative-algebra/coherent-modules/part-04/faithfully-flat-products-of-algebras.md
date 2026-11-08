---
declaration: theorem
origin: cited
lean: Module.FaithfullyFlat.pi_algebra_iff
statement: formalized
proof: formalized
---

# Faithfully flat products of algebras

Over a `CommRing R`, for an arbitrary
dependent family of unital, possibly noncommutative `R`-algebras `A i`,
[`Module.FaithfullyFlat.pi_algebra_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pi.lean)
characterizes faithful flatness of `Π i, A i` by flatness of the **whole
product** and a nontrivial fiber `(R ⧸ I) ⊗[R] A i` in some component for
every finitely generated proper ideal `I`. The detecting component may depend
on the ideal. Componentwise flatness cannot replace whole-product flatness,
and the components need not individually be faithfully flat. The ring, index
and carrier universes are independent, and empty products are allowed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FaithfullyFlat.pi_algebra_iff` (theorem), declared in [CoherentModules/RingTheory/Flat/Pi.lean, line 44](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pi.lean#L44).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FaithfullyFlat.pi_algebra_iff` in CoherentModules/RingTheory/Flat/Pi.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pi.lean#L44)
