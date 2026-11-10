---
declaration: theorem
origin: cited
lean: Module.FinitePresentation.isCoherent_restrictScalars
statement: formalized
proof: formalized
---

# Coherence under scalar restriction

For possibly noncommutative rings `R`
and `S`, if `S` is coherent as an `R`-module, then
[`Module.FinitePresentation.isCoherent_restrictScalars`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean)
makes every finitely presented `S`-module `N` coherent for its given `R`-action.
The additive commutative group `N` has its given module structures and scalar
towers `R → S → S` and `R → S → N`; the three universes are independent.
Under these hypotheses, coherence over `R`, coherence over `S`, and finite
presentation over `S` are equivalent. No coherence assumption on `R`,
Noetherianity, centrality or faithfulness is required. The identity-scalar
specialization [`Module.isCoherent_iff_finitePresentation`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean)
identifies the two properties over an `IsCoherentRing R`, yielding finite
presentation of kernels between finitely presented modules. The
[`of_exact_five` criterion](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean) gives finite
presentation of `M₃` in `M₁ → M₂ → M₃ → M₄ → M₅` when the sequence is exact
at `M₂`, `M₃`, `M₄`, `M₁` is finite, and `M₂`, `M₄`, `M₅` are finitely
presented. It requires neither endpoint injectivity nor surjectivity.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FinitePresentation.isCoherent_restrictScalars` (theorem), declared in [CoherentModules/FinitePresentation.lean, line 346](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L346).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FinitePresentation.isCoherent_restrictScalars` in CoherentModules/FinitePresentation.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L346)
