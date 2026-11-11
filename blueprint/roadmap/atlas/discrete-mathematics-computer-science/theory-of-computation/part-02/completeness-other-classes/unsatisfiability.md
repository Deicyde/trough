---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.UNSATCoNPComplete.unsatDec, MetaMathlibExt.Complexity.KeyTheorems.UNSATCoNPComplete.unsat_conp_complete
statement: formalized
---

# Unsatisfiability

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/unsatisfiability/index.html).

## UNSAT as a decision problem

The UNSAT decision problem accepts a bitstring $x$ exactly
when $x$ decodes, under the canonical bitstring encoding, to a pair $(n, \varphi)$ of a natural
number $n$ and a CNF formula $\varphi$ such that every variable occurring in $\varphi$ is less
than $n$ and, for every assignment $a$ of booleans to the variables $0, \dots, n - 1$, the
assignment that agrees with $a$ below $n$ and sends every variable $v \ge n$ to false does not
satisfy $\varphi$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.UNSATCoNPComplete.unsatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/UNSATCoNPCompleteWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/UNSATCoNPCompleteWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/unsatisfiability/index.html#unsat-dec).

## UNSAT is coNP-complete

The UNSAT decision problem lies in coNP, and every decision
problem in coNP has a polynomial-time many-one reduction to it.

## Sources

- S. A. Cook, "The complexity of theorem-proving procedures", Proceedings of the Third Annual ACM Symposium on Theory of Computing (STOC 1971), 151-158; L. A. Levin, "Universal search problems", Problems of Information Transmission 9 (1973), 265-266.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.UNSATCoNPComplete.unsat_conp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/UNSATCoNPCompleteWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/UNSATCoNPCompleteWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/unsatisfiability/index.html#unsat-conp-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unsatisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/unsatisfiability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/unsatisfiability)
