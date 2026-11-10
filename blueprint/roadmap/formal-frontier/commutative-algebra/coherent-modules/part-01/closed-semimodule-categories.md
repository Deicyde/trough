---
declaration: def
origin: cited
lean: SemimoduleCat.tensorLeftHomAdjunction
statement: formalized
---

# Closed semimodule categories

For a `CommSemiring R`,
[`SemimoduleCat.tensorLeftHomAdjunction`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Monoidal/Closed.lean)
makes tensoring with `M` left adjoint to its wrapped-morphism Hom functor.
The Hom functor allows an independent carrier universe; the monoidal closed
structure uses the common scalar and carrier universe of the tensor category.
Currying, uncurrying, evaluation and coevaluation have pure-tensor formulas.
Over a commutative ring, `ModuleCat.ihomSemimoduleIso` compares the chosen
internal Homs and their unit, counit and precomposition maps.
The [finite-basis client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/Algebra/Category/ModuleCat/Monoidal/Closed.lean)
uses a specified basis with finite index type to show that tensoring preserves
existing limits at two independent diagram sizes; the index universe is
independent as well.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `SemimoduleCat.tensorLeftHomAdjunction` (def), declared in [CoherentModules/Algebra/Category/ModuleCat/Monoidal/Closed.lean, line 84](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Monoidal/Closed.lean#L84).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `SemimoduleCat.tensorLeftHomAdjunction` in CoherentModules/Algebra/Category/ModuleCat/Monoidal/Closed.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Monoidal/Closed.lean#L84)
