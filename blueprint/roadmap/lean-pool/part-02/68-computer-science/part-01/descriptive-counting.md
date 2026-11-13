---
declaration: theorem
origin: cited
lean: DescriptiveComplexity.sharpSat_sharpTseitin, DescriptiveComplexity.sharpSat_sharpP_parsimoniousComplete, DescriptiveComplexity.sharpSat_sharpP_complete
statement: formalized
proof: formalized
---

# Descriptive counting complexity and parsimonious completeness of \#SAT

> Defines counting problems on finite nonempty relational structures, existential second-order witness counts, and first-order counting reductions. Constructs a parsimonious Tseitin interpretation and proves that the number of satisfying assignments of its CNF equals the number of witnesses of the source formula. Consequently \#SAT is complete for the library's logically defined \#P under parsimonious reductions. Includes the supporting first-order interpretation, second-order definability, fixed-point, and counting-reduction infrastructure. The scope is descriptive complexity; no equivalence with a string-based resource-bounded machine model is claimed by this import.

*Quoted from the card [LeanPool/projects/descriptive-counting.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/descriptive-counting.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DescriptiveComplexity.sharpSat_sharpTseitin`](https://leanpool.github.io/lean-pool/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.html#DescriptiveComplexity.sharpSat_sharpTseitin) (theorem; a main declaration), declared in [LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean, line 392](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean#L392): “For every finite nonempty ordered source structure, the CNF produced by the parsimonious Tseitin interpretation has exactly as many satisfying assignments as the source second-order block has witnesses satisfying its first-order kernel.”
- [`DescriptiveComplexity.sharpSat_sharpP_parsimoniousComplete`](https://leanpool.github.io/lean-pool/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.html#DescriptiveComplexity.sharpSat_sharpP_parsimoniousComplete) (theorem; a main declaration), declared in [LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean, line 461](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean#L461): “Counting the satisfying assignments of a CNF is complete under parsimonious first-order reductions for counting problems defined by existential second-order witness counts on finite nonempty relational structures.”
- [`DescriptiveComplexity.sharpSat_sharpP_complete`](https://leanpool.github.io/lean-pool/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.html#DescriptiveComplexity.sharpSat_sharpP_complete) (theorem; a main declaration), declared in [LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean, line 466](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DescriptiveCounting/Problems/Sat/CountingHardness.lean#L466): “The same counting problem is complete for the library's \#P under its subtractive reduction notion.”

## Project

- Authors: Pierre Senellart.
- Source: *Descriptive Complexity counting release v1.4.0*.
- Project repository: [PierreSenellart/descriptive-complexity](https://github.com/PierreSenellart/descriptive-complexity), at commit [2d853cdd](https://github.com/PierreSenellart/descriptive-complexity/tree/2d853cdde85a1b5c3d855b6f20b5f07f4c1a73e8).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q15, 03C13, 68V15.
- In Lean Pool: [LeanPool/DescriptiveCounting](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DescriptiveCounting), from the card [LeanPool/projects/descriptive-counting.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/descriptive-counting.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/descriptive-counting.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/descriptive-counting.yaml)
- [Lean Pool at 701389c0: LeanPool/DescriptiveCounting](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DescriptiveCounting)
