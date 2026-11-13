---
declaration: theorem
origin: cited
lean: GenLimit.FiniteWitness.Simplified.ordinary_iff_finiteWitnesses
statement: formalized
proof: formalized
---

# Finite witnesses and the width hierarchy for language generation

> Characterizes generation in the limit for arbitrary families of infinite languages over any countably infinite universe by finite positive witnesses. Ordered-history generators admit a single set-driven normalization, chosen before the target language. The separation-width invariant takes every value 0, 1, 2, ..., omega, omega+1; generation is equivalent to width at most omega. Reusable infrastructure includes locking witnesses, positive separation, bounded diagonal capture over arbitrary universes, transport under equivalences, and finite-query normalization on natural numbers. The formalized scope is the semantic characterization and hierarchy, not the paper's additional density-one or Turing-computability results in Appendices D and E.

*Quoted from the card [LeanPool/projects/language-generation-characterization.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/language-generation-characterization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GenLimit.FiniteWitness.Simplified.ordinary_iff_finiteWitnesses`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.html#GenLimit.FiniteWitness.Simplified.ordinary_iff_finiteWitnesses) (theorem; a main declaration), declared in [LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.lean, line 172](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.lean#L172): “For any family H of infinite languages over a countably infinite universe, there exists one ordered-history generator that eventually outputs an unseen target element on every exact presentation of every target in H if and only if H admits a finite positive witness assignment whose nonempty active subfamilies always have infinite common intersection.”
- [`GenLimit.FiniteWitness.Simplified.universal_normalization`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.html#GenLimit.FiniteWitness.Simplified.universal_normalization) (theorem), declared in [LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.lean, line 153](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Simplified/Normalization.lean#L153): “Every ordered-history generator over a countably infinite universe has one set-driven normalization that locks on every infinite target on which the original generator succeeds on all exact presentations. The normalization is chosen before the target.”
- [`GenLimit.FiniteWitness.ordinary_iff_width`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Width/Value.html#GenLimit.FiniteWitness.ordinary_iff_width) (theorem), declared in [LeanPool/LanguageGeneration/FiniteWitness/Width/Value.lean, line 76](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Width/Value.lean#L76): “A family of infinite languages over a countably infinite universe is generatable in the limit exactly when its separation width is at most omega.”
- [`GenLimit.FiniteWitness.full_range`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Width/Endpoints.html#GenLimit.FiniteWitness.full_range) (theorem), declared in [LeanPool/LanguageGeneration/FiniteWitness/Width/Endpoints.lean, line 101](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Width/Endpoints.lean#L101): “Over every countably infinite universe, every value in WithTop (WithTop Nat), representing 0, 1, 2, ..., omega, omega+1, is the separation width of some family of infinite languages.”
- [`GenLimit.FiniteWitness.bounded_capture`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Width/Capture.html#GenLimit.FiniteWitness.bounded_capture) (theorem), declared in [LeanPool/LanguageGeneration/FiniteWitness/Width/Capture.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Width/Capture.lean#L27): “Over an arbitrary universe, every sequence of uniformly bounded finite sets has infinitely many terms contained in one set D such that D contains none of a prescribed countable list of infinite cores.”
- [`GenLimit.FiniteWitness.executable_universal_normalization`](https://leanpool.github.io/lean-pool/LeanPool/LanguageGeneration/FiniteWitness/Width/Executable.html#GenLimit.FiniteWitness.executable_universal_normalization) (theorem), declared in [LeanPool/LanguageGeneration/FiniteWitness/Width/Executable.lean, line 155](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration/FiniteWitness/Width/Executable.lean#L155): “The finite-search normalization on natural numbers locks on every infinite language on which the supplied generator eventually succeeds on every exact presentation. This is a semantic correctness theorem for the defined procedure, without a formal Turing-computability claim.”

## Project

- Authors: Xiaoyu Li, Andi Han, Jiaojiao Jiang, Junbin Gao, Shuangping Li, Peng Zhang.
- Source: *Characterizing Language Generation in the Limit: Finite Witnesses and a Separation-Width Hierarchy* by Xiaoyu Li, Andi Han, Jiaojiao Jiang, Junbin Gao, [arXiv:2609.10525](https://arxiv.org/abs/2609.10525).
- Project repository: [xiaoyulics/language-generation-characterization](https://github.com/xiaoyulics/language-generation-characterization), at commit [4f7d3f21](https://github.com/xiaoyulics/language-generation-characterization/tree/4f7d3f2148017ae15135ba39ddc4d655bb175ab6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q32, 68Q45.
- In Lean Pool: [LeanPool/LanguageGeneration](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration), from the card [LeanPool/projects/language-generation-characterization.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/language-generation-characterization.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/language-generation-characterization.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/language-generation-characterization.yaml)
- [Lean Pool at 701389c0: LeanPool/LanguageGeneration](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LanguageGeneration)
