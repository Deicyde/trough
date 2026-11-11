---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.AMSubsetPi2.am_subset_pi2, MetaMathlibExt.Complexity.KeyTheorems.MASubsetAM.ma_subset_am, MetaMathlibExt.Complexity.KeyTheorems.MASubsetPH.ma_subset_ph
statement: formalized
---

# Arthur–Merlin and Merlin–Arthur classes

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes/index.html).

## AM is contained in $\Pi_2^p$ (Babai)

Every decision problem in the Arthur–Merlin class
$\mathsf{AM}$ lies in $\Pi_2^p$, the second universal level of the polynomial hierarchy.

## Sources

- L. Babai, "Trading group theory for randomness", Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing (STOC 1985), 421-429; see also O. Goldreich and D. Zuckerman and the set lower-bound protocol of Goldwasser-Sipser.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.AMSubsetPi2.am_subset_pi2` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/AMSubsetPi2Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AMSubsetPi2Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes/index.html#am-subset-pi2).

## MA is contained in AM

Every decision problem in the class $\mathsf{MA}$ is in the class
$\mathsf{AM}$.

## Sources

- L. Babai, "Trading group theory for randomness", Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing (STOC 1985), 421-429; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 8.2 (MA ⊆ AM).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MASubsetAM.ma_subset_am` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MASubsetAMWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MASubsetAMWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes/index.html#ma-subset-am).

## MA is contained in PH

Every decision problem in the class $\mathsf{MA}$ is in the
polynomial hierarchy $\mathsf{PH}$.

## Sources

- L. Babai, "Trading group theory for randomness", Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing (STOC 1985), 421-429 (MA ⊆ AM, AM ⊆ Π₂); L. J. Stockmeyer, "The polynomial-time hierarchy", Theoretical Computer Science 3 (1977), 1-22 (PH); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 5.4 (PH ⊆ PSPACE) and Chapter 8.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MASubsetPH.ma_subset_ph` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MASubsetPHWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MASubsetPHWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes/index.html#ma-subset-ph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arthur–Merlin and Merlin–Arthur classes](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/arthur-merlin-and-merlin-arthur-classes)
