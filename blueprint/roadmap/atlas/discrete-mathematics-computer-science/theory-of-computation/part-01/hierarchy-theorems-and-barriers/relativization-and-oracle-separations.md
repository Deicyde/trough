---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.BakerGillSolovay.baker_gill_solovay, MetaMathlibExt.Complexity.KeyTheorems.OracleNPCoNPSeparation.oracle_np_co_np_separation
statement: formalized
---

# Relativization and oracle separations

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/relativization-and-oracle-separations/index.html).

## Baker-Gill-Solovay: oracles separate and collapse P vs NP

For an oracle $O$, a function
from bitstrings to booleans, write $\mathsf{P}^O$ and $\mathsf{NP}^O$ for the classes of decision
problems decidable in polynomial time, respectively in nondeterministic polynomial time, by
machines that may query $O$. There is an oracle $O$ such that $\mathsf{P}^O \ne \mathsf{NP}^O$,
and there is an oracle $O$ such that $\mathsf{P}^O = \mathsf{NP}^O$.

## Sources

- T. Baker, J. Gill, and R. Solovay, "Relativizations of the P =? NP question", SIAM Journal on Computing 4 (1975), 431-442.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.BakerGillSolovay.baker_gill_solovay` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/BakerGillSolovayWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/BakerGillSolovayWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/relativization-and-oracle-separations/index.html#baker-gill-solovay).

## An oracle separates NP from coNP

There is an oracle $O$, a function from bitstrings to
booleans, such that $\mathrm{NP}^O$ differs from the class $\mathrm{coNP}^O$ of decision problems
$L$ whose complement, the decision problem that accepts exactly the bitstrings that $L$ rejects,
belongs to $\mathrm{NP}^O$.

## Sources

- T. Baker, J. Gill, and R. Solovay, "Relativizations of the P =? NP question", SIAM Journal on Computing 4 (1975), 431-442 (oracles separating NP from coNP); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 3 (relativization).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.OracleNPCoNPSeparation.oracle_np_co_np_separation` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/OracleNPCoNPSeparationWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/OracleNPCoNPSeparationWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/relativization-and-oracle-separations/index.html#oracle-np-co-np-separation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Relativization and oracle separations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/relativization-and-oracle-separations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/relativization-and-oracle-separations)
