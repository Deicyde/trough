---
declaration: theorem
origin: cited
lean: Module.FinitePresentation.of_piRing
statement: formalized
proof: formalized
---

# Finite presentation over product coefficient rings

For any dependent family
of possibly noncommutative rings `R i` and additive commutative monoids `M i`
with their given `R i`-module structures,
[`Module.FinitePresentation.of_piRing`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean)
reflects finite presentation of `Π i, M i` over `Π i, R i` to each coordinate.
This direction allows an arbitrary index type. For `[Finite ι]`,
`Module.FinitePresentation.piRing_iff` gives the converse as well:
```lean
Module.FinitePresentation (∀ i, R i) (∀ i, M i) ↔
  ∀ i, Module.FinitePresentation (R i) (M i)
```
The action is `(r • m) i = r i • m i`; the index, coefficient and module
universes are independent. No supplied additive group structure, coherence,
Noetherianity, commutativity or nontriviality is required. Empty products and
zero factors are allowed. The
[varying-rank client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/FinitePresentationPi.lean) combines
free modules over the integers and a noncommutative integer matrix ring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FinitePresentation.of_piRing` (theorem), declared in [CoherentModules/RingTheory/Pi.lean, line 282](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean#L282).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FinitePresentation.of_piRing` in CoherentModules/RingTheory/Pi.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Pi.lean#L282)
