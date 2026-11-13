---
declaration: section
origin: cited
lean: Cslib.Language.IsRegular.isContextFree
statement: formalized
proof: formalized
---

# Grammars, parsing and pushdown automata: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/index.html).

Grammar basics and derivation forests, Chomsky and Greibach normal forms, ε- and unit-production elimination, CYK and Earley recognizers, leftmost derivations and (inherent) ambiguity, pushdown automata, deterministic context-free languages, and the grammar–PDA equivalence.

## Regular languages over a finite alphabet are context-free

Over a finite alphabet,
every regular language is context-free.

Finiteness of the alphabet is necessary: a grammar has finitely many
productions, hence mentions only finitely many terminal symbols, but a DFA
over an infinite alphabet may accept every one-letter word.

Formalized by `Cslib.Language.IsRegular.isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Regular.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Regular.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/index.html#is-context-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Grammars, parsing and pushdown automata](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata)
