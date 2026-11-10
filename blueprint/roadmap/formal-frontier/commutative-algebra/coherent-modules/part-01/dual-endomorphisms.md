---
declaration: def
origin: cited
lean: Module.End.dualMapAlgHom
statement: formalized
---

# Dual endomorphisms

Over a commutative semiring `R`,
[`Module.End.dualMapAlgHom`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/End.lean)
bundles dualization as an algebra homomorphism from the opposite endomorphism
algebra of any `R`-semimodule. For a possibly noncommutative `R`-algebra `A`,
`Module.Dual.rightRegularAlgHom` gives named operators
`F_a(φ)(x) = φ(a * x)`, with `F_a.comp F_b = F_(b * a)` and the original
pointwise `R`-scalar structure on the dual. No finiteness or freeness is required.
Over a commutative ring `R` and a possibly noncommutative ring algebra `A`,
[`Module.Dual.coextensionEquiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/Coextension.lean)
identifies opposite-algebra coextension of `R`, restricted to `R`, with the
original dual, intertwining coextension translation with these named operators.
Its generic [pointwise Hom comparison](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/ChangeOfRings.lean)
retains the given algebra action and allows independent scalar and module universes.
For self-pairings,
[`LinearMap.nondegenerate_of_surjective_of_separatingLeft`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/Nondegenerate.lean)
proves both separating directions from surjectivity and left separation;
a bijective map to the dual is consequently nondegenerate, even for semimodules.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.End.dualMapAlgHom` (def), declared in [CoherentModules/LinearAlgebra/Dual/End.lean, line 35](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/End.lean#L35).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.End.dualMapAlgHom` in CoherentModules/LinearAlgebra/Dual/End.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Dual/End.lean#L35)
