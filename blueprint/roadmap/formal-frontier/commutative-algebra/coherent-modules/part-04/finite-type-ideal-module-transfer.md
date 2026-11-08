---
declaration: theorem
origin: cited
lean: Ideal.ideal_property_iff_module_property
statement: formalized
proof: formalized
---

# Finite-type ideal/module transfer

Over a commutative base ring,
[`Ideal.ideal_property_iff_module_property`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/FiniteModuleTransfer.lean)
equates a property on all finitely generated ideals with one on all finite
modules over finite-type algebras. The property must be invariant under
compatible algebra/module isomorphisms and descend along **every** compatible
surjective square-zero algebra map for finite source modules. The base universe
is independent of the common algebra/module universe. Finite type does not
mean module-finite over the base, and arbitrary ideals need not be finitely
generated.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.ideal_property_iff_module_property` (theorem), declared in [CoherentModules/RingTheory/Ideal/FiniteModuleTransfer.lean, line 37](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/FiniteModuleTransfer.lean#L37).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.ideal_property_iff_module_property` in CoherentModules/RingTheory/Ideal/FiniteModuleTransfer.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/FiniteModuleTransfer.lean#L37)
