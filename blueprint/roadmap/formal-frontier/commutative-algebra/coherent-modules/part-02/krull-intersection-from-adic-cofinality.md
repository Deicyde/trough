---
declaration: theorem
origin: cited
lean: Ideal.HasFiniteSubmoduleAdicCofinality.mem_iInf_pow_smul_top_iff
statement: formalized
proof: formalized
---

# Krull intersection from adic cofinality

For a finite module `M` and an
ideal `I` satisfying finite-submodule adic cofinality,
[`Ideal.HasFiniteSubmoduleAdicCofinality.mem_iInf_pow_smul_top_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean)
characterizes membership in `⨅ n, I ^ n • ⊤` by a scalar `a ∈ I` fixing
the element. The relative bound `I ≤ (Module.annihilator R M).jacobson`
makes this intersection zero. For any submodule `N` with finite quotient,
membership in `⨅ n, N ⊔ I ^ n • ⊤` is equivalent to
`(1 - a) • x ∈ N` for some `a ∈ I`; a Jacobson bound relative to the
quotient annihilator makes the intersection equal to `N`.
The ambient module and `N` need not be finite in the quotient statements.
No ideal-FG, finite-presentation or Noetherian hypothesis is added, and the
ring and module universes are independent. These are algebraic intersection
results, not assertions of topological closedness or completeness.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.HasFiniteSubmoduleAdicCofinality.mem_iInf_pow_smul_top_iff` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicKrull.lean, line 76](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean#L76).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.HasFiniteSubmoduleAdicCofinality.mem_iInf_pow_smul_top_iff` in CoherentModules/RingTheory/Ideal/AdicKrull.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean#L76)
