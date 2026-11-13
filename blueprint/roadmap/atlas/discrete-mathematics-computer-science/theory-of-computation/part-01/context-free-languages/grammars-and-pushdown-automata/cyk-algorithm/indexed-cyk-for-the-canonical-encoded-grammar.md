---
declaration: section
origin: cited
lean: Cslib.Language.CYKIndexed.decodeSymbols, Cslib.Language.CYKIndexed.decodeSymbols_ret, Cslib.Language.CYKIndexed.decodeRules, Cslib.Language.CYKIndexed.decodeRules_ret, Cslib.Language.CYKIndexed.recognizesEncoded, Cslib.Language.CYKIndexed.recognizesEncoded_iff, Cslib.Language.CYKIndexed.decodeSymbols_time, Cslib.Language.CYKIndexed.decodeRules_time
statement: formalized
proof: formalized
---

# Indexed CYK for the canonical encoded grammar

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html).

## Charged decoding of encoded grammar symbols

Decode symbols with a charge for each constructor test and output cons.

Formalized by `Cslib.Language.CYKIndexed.decodeSymbols`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-symbols).

## Charged symbol decoding agrees with canonical decoding

The charged conversion is exactly the canonical symbol decoding.

Formalized by `Cslib.Language.CYKIndexed.decodeSymbols_ret`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-symbols-ret).

## Charged decoding of encoded grammar rules

Decode every rule, charging all right-hand-side traversals.

Formalized by `Cslib.Language.CYKIndexed.decodeRules`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-rules).

## Charged rule decoding agrees with the decoded grammar

The charged rule conversion agrees with the existing decoded grammar.

Formalized by `Cslib.Language.CYKIndexed.decodeRules_ret`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-rules-ret).

## Indexed CYK recognizer for encoded grammars

Run indexed CYK on the existing encoded grammar, including preparation.

Formalized by `Cslib.Language.CYKIndexed.recognizesEncoded`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#recognizes-encoded).

## Correctness of indexed CYK on encoded grammars

Correctness for the canonical encoded language, including epsilon.

Formalized by `Cslib.Language.CYKIndexed.recognizesEncoded_iff`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#recognizes-encoded-iff).

## Exact cost of grammar symbol decoding

Exact symbol-decoding traversal cost.

Formalized by `Cslib.Language.CYKIndexed.decodeSymbols_time`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-symbols-time).

## Exact cost of grammar rule decoding

Exact grammar-preparation cost, including all production symbols.

Formalized by `Cslib.Language.CYKIndexed.decodeRules_time`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#decode-rules-time).

## Cubic cost bound for indexed CYK on encoded grammars

Cubic word-length bound including canonical grammar preparation.
All dependence on the fixed grammar and symbol-equality model is explicit.

Formalized by `Cslib.Language.CYKIndexed.recognizesEncoded_time_le`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/CYKIndexed/Encoded.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html#recognizes-encoded-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Indexed CYK for the canonical encoded grammar](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/cyk-algorithm/indexed-cyk-for-the-canonical-encoded-grammar)
