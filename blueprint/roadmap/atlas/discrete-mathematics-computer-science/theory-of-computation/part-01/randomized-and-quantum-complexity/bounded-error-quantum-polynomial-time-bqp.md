---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.BQPSubsetPP.bqp_subset_pp, MetaMathlibExt.Complexity.KeyTheorems.BQPSubsetPSPACE.bqp_subset_pspace
statement: formalized
---

# Bounded-error quantum polynomial time (BQP)

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-quantum-polynomial-time-bqp/index.html).

## BQP is contained in PP

Every decision problem in BQP lies in PP.

## Sources

- E. Bernstein and U. Vazirani, "Quantum complexity theory", SIAM Journal on Computing 26 (1997), 1411-1473 (BQP ⊆ PP); L. Adleman, J. DeMarrais, and M.-D. Huang, "Quantum computability", SIAM Journal on Computing 26 (1997), 1524-1540; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 10.2.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.BQPSubsetPP.bqp_subset_pp` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/BQPSubsetPPWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/BQPSubsetPPWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-quantum-polynomial-time-bqp/index.html#bqp-subset-pp).

## BQP is contained in PSPACE

Every decision problem in BQP, the class of bounded-error
quantum polynomial-time decision problems, lies in PSPACE, the class of decision problems
decidable in polynomial space.

## Sources

- E. Bernstein and U. Vazirani, "Quantum complexity theory", SIAM Journal on Computing 26 (1997), 1411-1473 (BQP ⊆ PSPACE); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 10.2.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.BQPSubsetPSPACE.bqp_subset_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/BQPSubsetPSPACEWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/BQPSubsetPSPACEWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-quantum-polynomial-time-bqp/index.html#bqp-subset-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded-error quantum polynomial time (BQP)](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-quantum-polynomial-time-bqp/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/bounded-error-quantum-polynomial-time-bqp)
