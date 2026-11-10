---
declaration: theorem
origin: cited
lean: Module.IsCoherent.of_piRing
statement: formalized
proof: formalized
---

# Coherence over product coefficient rings

For any dependent family of
possibly noncommutative rings `R i` and additive commutative monoids `M i` with
their given `R i`-module structures,
[`Module.IsCoherent.of_piRing`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean) reflects
coherence of the product to each coordinate. For `[Finite ι]`,
`Module.IsCoherent.piRing_iff` gives the converse as well:
```lean
Module.IsCoherent (∀ i, R i) (∀ i, M i) ↔
  ∀ i, Module.IsCoherent (R i) (M i)
```
The action is `(r • m) i = r i • m i`, with independently variable coordinate
scalars, not a common diagonal scalar ring. The index, coefficient and module
universes are independent. Reflection allows an arbitrary index type; the
equivalence requires only `[Finite ι]`. Empty products, zero rings and zero
modules are allowed. No Noetherianity, commutativity, faithfulness or extra
finite-generation hypothesis is assumed.
The regular-module specialization `isCoherentRing_pi_iff` characterizes
coherence of the product ring by coherence of every factor. Coherence of an
arbitrary coordinate module does not assert coherence of its coefficient ring.
The supporting [`Module.Finite.piRing_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Pi.lean)
proves the corresponding finite-generation equivalence already for semirings
and additive commutative monoids. These equivalences concern finite products;
coordinatewise coherence does not in general imply coherence of an infinite
product module over its product coefficient ring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsCoherent.of_piRing` (theorem), declared in [CoherentModules/RingTheory/Pi.lean, line 367](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean#L367).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.IsCoherent.of_piRing` in CoherentModules/RingTheory/Pi.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean#L367)
