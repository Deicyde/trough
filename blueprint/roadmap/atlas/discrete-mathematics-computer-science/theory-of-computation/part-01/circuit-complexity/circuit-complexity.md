---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Smolensky.smolensky, MetaMathlibExt.Complexity.KeyTheorems.Williams.williams_nexp_not_in_acc0
statement: formalized
---

# Boolean circuit complexity: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/index.html).

Boolean circuits as a model of computation, including arithmetic circuits built from gates (adders, two's complement), parallel classes AC0, NC1 and NC, and circuit lower bounds (parity and majority not in AC0, Smolensky, Razborov's monotone bound, Shannon counting, Williams).

## Smolensky: parity is not in AC0(mod 3)

The parity language, which accepts a bitstring
exactly when an odd number of its entries are true, is not in $\mathsf{AC}^0[3]$, the class
$\mathsf{AC}^0[m]$ for $m = 3$ of decision problems decided by polynomial-size, bounded-depth
families of well-formed flat Boolean circuits in which every mod gate has modulus $3$.

## Sources

- R. Smolensky, "Algebraic methods in the theory of lower bounds for Boolean circuit complexity", Proceedings of the Nineteenth Annual ACM Symposium on Theory of Computing (STOC 1987), 77-82.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Smolensky.smolensky` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SmolenskyWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SmolenskyWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/index.html#smolensky).

## Williams: NEXP is not contained in ACC0

Some decision problem lies in NEXP but not in
$\mathsf{ACC}^0$.

## Sources

- R. Williams, "Non-uniform ACC circuit lower bounds", Journal of the ACM 61 (2014), 1-32 (CCC 2011).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Williams.williams_nexp_not_in_acc0` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/WilliamsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/WilliamsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/index.html#williams-nexp-not-in-acc0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boolean circuit complexity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity)
