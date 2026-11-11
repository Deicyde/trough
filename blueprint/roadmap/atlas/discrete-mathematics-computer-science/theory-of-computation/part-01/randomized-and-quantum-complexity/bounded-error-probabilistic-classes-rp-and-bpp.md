---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.BPPSubsetPSPACE.bpp_subset_pspace, MetaMathlibExt.Complexity.KeyTheorems.RPSubsetBPP.rp_subset_bpp, MetaMathlibExt.Complexity.KeyTheorems.RPSubsetNP.rp_subset_np
statement: formalized
---

# Bounded-error probabilistic classes RP and BPP

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp/index.html).

## BPP is contained in PSPACE

Every decision problem in BPP lies in PSPACE.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009 (BPP ⊆ PSPACE).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.BPPSubsetPSPACE.bpp_subset_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/BPPSubsetPSPACEWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/BPPSubsetPSPACEWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp/index.html#bpp-subset-pspace).

## RP is contained in BPP

Every decision problem in the class $\mathsf{RP}$ of
one-sided-error randomized polynomial-time decision problems also belongs to the class
$\mathsf{BPP}$ of bounded-error probabilistic polynomial-time decision problems.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 7 (error reduction for RP); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Theorem 10.13 (RP ⊆ BPP via amplification).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.RPSubsetBPP.rp_subset_bpp` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/RPSubsetBPPWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/RPSubsetBPPWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp/index.html#rp-subset-bpp).

## RP is contained in NP

Every decision problem in the class $\mathsf{RP}$ of
one-sided-error randomized polynomial-time decision problems also belongs to the class
$\mathsf{NP}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 7.3 (RP ⊆ NP); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Theorem 10.13.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.RPSubsetNP.rp_subset_np` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/RPSubsetNPWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/RPSubsetNPWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp/index.html#rp-subset-np).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded-error probabilistic classes RP and BPP](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-probabilistic-classes-rp-and-bpp)
