---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.NC1SubsetL.nc1_subset_logspace, MetaMathlibExt.Complexity.KeyTheorems.NCSubsetP.nc_subset_p
statement: formalized
---

# Parallel complexity class NC

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/parallel-complexity-class-nc/index.html).

## NC^1 is contained in L

Every decision problem in $\mathsf{NC}^1$ belongs to the class
$\mathsf{L}$ of decision problems decidable in deterministic logarithmic space.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 6.22 (NC¹ ⊆ L); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Theorem 9.21 (NC¹ ⊆ L).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NC1SubsetL.nc1_subset_logspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NC1SubsetLWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NC1SubsetLWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/parallel-complexity-class-nc/index.html#nc1-subset-logspace).

## NC is contained in P

Every decision problem in $\mathsf{NC}$ belongs to $\mathsf{P}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 6.22 (NC ⊆ P); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Theorem 9.21.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NCSubsetP.nc_subset_p` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NCSubsetPWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NCSubsetPWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/parallel-complexity-class-nc/index.html#nc-subset-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parallel complexity class NC](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/parallel-complexity-class-nc/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity/parallel-complexity-class-nc)
