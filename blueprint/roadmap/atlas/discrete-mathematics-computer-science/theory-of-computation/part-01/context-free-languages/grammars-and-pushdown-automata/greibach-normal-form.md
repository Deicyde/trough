---
declaration: section
origin: cited
lean: Cslib.Language.IsGreibachNormalForm, Cslib.Language.exists_terminal_head_of_output_ne_nil
statement: formalized
proof: formalized
---

# Greibach normal form

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/greibach-normal-form/index.html).

## Greibach normal form

A grammar is in Greibach normal form when every production has
output either a single terminal followed by nonterminals, or the
empty word with the initial nonterminal on the left; and either the
initial nonterminal occurs in no output (so an empty production
cannot leak the empty word to other nonterminals) or there are no
empty outputs at all.

## Sources

- Hopcroft and Ullman, Introduction to Automata Theory, Languages, and Computation, Addison-Wesley, 1979, Chapter 7 (Greibach normal form); Harrison, Introduction to Formal Language Theory, Addison-Wesley, 1978, Chapter 4.

Formalized by `Cslib.Language.IsGreibachNormalForm`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/GreibachNormalForm.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/GreibachNormalForm.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/greibach-normal-form/index.html#is-greibach-normal-form).

## Nonempty Greibach productions begin with a terminal

In Greibach normal form, every nonempty production output begins
with a terminal followed by nonterminals.

## Sources

- Hopcroft and Ullman, Introduction to Automata Theory, Languages, and Computation, Addison-Wesley, 1979, Chapter 7 (Greibach normal form); Harrison, Introduction to Formal Language Theory, Addison-Wesley, 1978, Chapter 4.

Formalized by `Cslib.Language.exists_terminal_head_of_output_ne_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/GreibachNormalForm.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/GreibachNormalForm.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/greibach-normal-form/index.html#exists-terminal-head-of-output-ne-nil).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Greibach normal form](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/greibach-normal-form/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/greibach-normal-form)
