---
declaration: theorem
origin: cited
lean: UnconditionalCriterion.exists_unconditionalSchauderBasis_of_finiteSignBound
statement: formalized
proof: formalized
---

# Unconditional Schauder Bases

> Develops an API for Schauder bases and unconditional Schauder bases of complete normed spaces, including ordered partial-sum convergence, rearrangement criteria for unconditionality, and an arbitrary-index variant built on unconditional summability, then proves a finite sign criterion: a family with dense closed span, nonzero vectors, and a uniform finite sign bound is the basis of an unconditional Schauder basis.

*Quoted from the card [LeanPool/projects/unconditional-schauder-basis.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/unconditional-schauder-basis.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`UnconditionalCriterion.exists_unconditionalSchauderBasis_of_finiteSignBound`](https://leanpool.github.io/lean-pool/LeanPool/UnconditionalSchauderBasis.html#UnconditionalCriterion.exists_unconditionalSchauderBasis_of_finiteSignBound) (theorem; a main declaration), declared in [LeanPool/UnconditionalSchauderBasis.lean, line 1429](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/UnconditionalSchauderBasis.lean#L1429): “Finite sign criterion for sequences: if `x : ℕ → E` has dense closed linear span, every `x n` is nonzero, and finite sign changes are uniformly bounded by `C`, then `x` is the basis sequence of an unconditional Schauder basis.” Its source, as the card gives it: “J. Lindenstrauss and L. Tzafriri, Classical Banach Spaces I and II, Chapter 1, Section c, unconditional bases, doi:10.1007/978-3-662-53294-2.”
- [`UnconditionalCriterion.exists_unconditionalSchauderBasisAbstractIndex_of_finiteSignBound`](https://leanpool.github.io/lean-pool/LeanPool/UnconditionalSchauderBasis.html#UnconditionalCriterion.exists_unconditionalSchauderBasisAbstractIndex_of_finiteSignBound) (theorem), declared in [LeanPool/UnconditionalSchauderBasis.lean, line 1405](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/UnconditionalSchauderBasis.lean#L1405): “Abstract-index form of the finite sign criterion: under the same dense span, nonzero, and uniform finite sign bound hypotheses for an arbitrarily indexed family, there is an abstractly indexed unconditional Schauder basis whose basis family is exactly `x`.” Its source, as the card gives it: “J. Lindenstrauss and L. Tzafriri, Classical Banach Spaces I and II, Chapter 1, Section c, unconditional bases, doi:10.1007/978-3-662-53294-2.”

## Project

- Authors: Daniel Smania.
- Source: *Classical Banach Spaces I and II* by Joram Lindenstrauss, Lior Tzafriri, [doi:10.1007/978-3-662-53294-2](https://doi.org/10.1007/978-3-662-53294-2).
- Project repository: [SmaniaD/UnconditionalSchauderBasis](https://github.com/SmaniaD/UnconditionalSchauderBasis).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 46B15.
- In Lean Pool: [LeanPool/UnconditionalSchauderBasis](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/UnconditionalSchauderBasis), from the card [LeanPool/projects/unconditional-schauder-basis.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/unconditional-schauder-basis.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/unconditional-schauder-basis.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/unconditional-schauder-basis.yaml)
- [Lean Pool at 701389c0: LeanPool/UnconditionalSchauderBasis](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/UnconditionalSchauderBasis)
