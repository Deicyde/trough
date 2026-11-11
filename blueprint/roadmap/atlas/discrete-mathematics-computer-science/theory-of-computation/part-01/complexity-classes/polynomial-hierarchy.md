---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.PHCollapse.ph_collapses, MetaMathlibExt.Complexity.KeyTheorems.PHSubsetPSPACE.ph_subset_pspace
statement: formalized
---

# Polynomial hierarchy

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-hierarchy/index.html).

## If P = NP then the polynomial hierarchy collapses to P

If the complexity classes P and NP
are equal, then the polynomial hierarchy PH, the union of the classes $\Sigma_k^p$ over all
natural numbers $k$, is equal to P.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009 (PH collapses to P if P = NP); L. J. Stockmeyer, "The polynomial-time hierarchy", Theoretical Computer Science 3 (1977), 1-22.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PHCollapse.ph_collapses` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PHCollapseWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PHCollapseWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-hierarchy/index.html#ph-collapses).

## The polynomial hierarchy is contained in PSPACE

Every decision problem in the polynomial
hierarchy PH belongs to PSPACE.

## Sources

- L. J. Stockmeyer, "The polynomial-time hierarchy", Theoretical Computer Science 3 (1977), 1-22; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 5.4.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PHSubsetPSPACE.ph_subset_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PHSubsetPSPACEWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PHSubsetPSPACEWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-hierarchy/index.html#ph-subset-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial hierarchy](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-hierarchy/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/polynomial-hierarchy)
