---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.encodeCNF, Cslib.AutomatedReasoning.StringConstraints.cnfSat_iff_stringSat, Cslib.AutomatedReasoning.StringConstraints.cnfSat_iff_boundedSatSpec
statement: formalized
proof: formalized
---

# SAT and bounded string constraints: reduction correctness

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor/index.html).

## Encoding of CNF formulas as string constraints

SAT as string constraints: each clause is a disjunction of word
equations `x = [b]`, one per literal.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.encodeCNF`, a definition declared in [CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor/index.html#encode-cnf).

## Correctness of the SAT-to-string-constraints translation

**Correctness of the SAT-to-string-constraints translation** at
length bound `1`: Boolean assignments become length-`≤ 1` string
assignments and back.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.cnfSat_iff_stringSat`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor/index.html#cnf-sat-iff-string-sat).

## SAT iff the bounded-search specification holds of the encoding

**SAT iff the bounded-search specification holds of the encoding** at
length bound `1`, for any variable list covering the variables of the
encoding. This is the bridge from the reduction to the bounded-search
specification: `boundedSatSpec_iff` (soundness / completeness of the
finite search) plus the reduction correctness.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.cnfSat_iff_boundedSatSpec`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/AutomatedReasoning/StringConstraints/Complexity.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor/index.html#cnf-sat-iff-bounded-sat-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: SAT and bounded string constraints: reduction correctness](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/sat-and-bounded-string-constraints-reduction-cor)
