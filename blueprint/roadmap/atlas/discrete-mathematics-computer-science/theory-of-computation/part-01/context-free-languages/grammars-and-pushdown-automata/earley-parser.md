---
declaration: section
origin: cited
lean: Cslib.Language.EarleyItem, Cslib.Language.EarleyChart, Cslib.Language.EarleyChartItem, Cslib.Language.earleyAccepts, Cslib.Language.dot_le_of_earleyChart, Cslib.Language.yields_take_of_earleyChart, Cslib.Language.earleyChart_complete_of_yields, Cslib.Language.exists_rule_of_yields_singleton
statement: formalized
proof: formalized
---

# Earley parser

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html).

## Earley item

An Earley item: a production with a dot after `dot` symbols of its
output, recognizing input that starts at the end of `pre` and whose
recognized prefix is `consumed`. The full input is `pre ++ consumed
++ rest` for some `rest`.

Formalized by `Cslib.Language.EarleyItem`, a structure declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-item).

## Earley chart

The Earley chart for input `w`: the least set of items closed
under initialization, prediction, scanning, and completion.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.EarleyChart`, an inductive type declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-chart).

## Earley chart as a predicate on items

The chart as a predicate on `EarleyItem`s.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.EarleyChartItem`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-chart-item).

## Acceptance by the Earley recognizer

Acceptance by the Earley recognizer: some completed item for a
production of the initial nonterminal consumes the whole input.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.earleyAccepts`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-accepts).

## Earley item dot stays within its production

The dot of a chart item never passes the end of its production.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.dot_le_of_earleyChart`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#dot-le-of-earley-chart).

## Soundness of the Earley chart

Soundness: the recognized prefix of a chart item yields the input
it consumed.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.yields_take_of_earleyChart`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#yields-take-of-earley-chart).

## Completeness of the Earley chart

Completeness: if a chart item waits on a sentential form and that
form yields a word fitting in the remaining input, the chart contains
the item completed by that word.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.earleyChart_complete_of_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-chart-complete-of-yields).

## A yield from one nonterminal starts with one of its productions

Inversion of a yield from a single nonterminal: it begins with
one production of that nonterminal.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.exists_rule_of_yields_singleton`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#exists-rule-of-yields-singleton).

## Correctness of the Earley recognizer

The Earley recognizer accepts exactly the grammar's language.

## Sources

- Earley, "An efficient context-free parsing algorithm", Communications of the ACM 13 (1970), 94-102.

Formalized by `Cslib.Language.earleyAccepts_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Earley.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Earley.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html#earley-accepts-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Earley parser](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/earley-parser)
