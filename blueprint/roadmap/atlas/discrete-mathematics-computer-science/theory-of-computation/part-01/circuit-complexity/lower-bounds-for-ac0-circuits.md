---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MajorityNotInAC0.majority_not_in_ac0, MetaMathlibExt.Complexity.KeyTheorems.ParityNotInAC0.parity_not_in_ac0
statement: formalized
---

# Lower bounds for AC0 circuits

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/lower-bounds-for-ac0-circuits/index.html).

## Majority is not in AC0

The majority language is not in the class $\mathsf{AC}^0$.

## Sources

- M. Ajtai, "Σ₁¹-formulae on finite structures", Annals of Pure and Applied Logic 24 (1983), 1-48; J. Håstad, "Almost optimal lower bounds for small depth circuits" (STOC 1986).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MajorityNotInAC0.majority_not_in_ac0` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MajorityNotInAC0Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/MajorityNotInAC0Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/lower-bounds-for-ac0-circuits/index.html#majority-not-in-ac0).

## Parity is not in AC0

The parity language, which accepts a bitstring exactly when an odd
number of its entries are true, is not in the class $\mathsf{AC}^0$.

## Sources

- M. Furst, J. Saxe, and M. Sipser, "Parity, circuits, and the polynomial-time hierarchy", Mathematical Systems Theory 17 (1984), 13-27; M. Ajtai, "Σ₁¹-formulae on finite structures", Annals of Pure and Applied Logic 24 (1983), 1-48; J. Håstad, "Almost optimal lower bounds for small depth circuits", Proceedings of the Eighteenth Annual ACM Symposium on Theory of Computing (STOC 1986), 6-20.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.ParityNotInAC0.parity_not_in_ac0` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ParityNotInAC0Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParityNotInAC0Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/lower-bounds-for-ac0-circuits/index.html#parity-not-in-ac0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lower bounds for AC0 circuits](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/lower-bounds-for-ac0-circuits/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity/lower-bounds-for-ac0-circuits)
