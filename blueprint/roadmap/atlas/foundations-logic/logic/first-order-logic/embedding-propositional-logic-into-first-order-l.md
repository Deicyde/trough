---
declaration: section
origin: cited
lean: Cslib.Logic.FOL.PropRelations, Cslib.Logic.FOL.propLanguage, Cslib.Logic.FOL.Proposition.embed, Cslib.Logic.FOL.Proposition.boolStructure, Cslib.Logic.FOL.Proposition.realize_embed_iff_evalBool
statement: formalized
proof: formalized
---

# Embedding propositional logic into first-order logic

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html).

## FOL

## Relation symbols of the propositional language

For a type of atoms, the family of
relation symbols indexed by arity that consists of one nullary relation symbol for each atom
$a$ and has no relation symbols of positive arity.

Formalized by `Cslib.Logic.FOL.PropRelations`, an inductive type declared in [CSLibExt/Logics/FirstOrder/PropositionalBridge.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/PropositionalBridge.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html#prop-relations).

## First-order language of propositional atoms

For a type of atoms, the first-order
language whose relation symbols are exactly one nullary relation symbol for each atom, with
no relation symbols of positive arity and no function symbols.

Formalized by `Cslib.Logic.FOL.propLanguage`, a definition declared in [CSLibExt/Logics/FirstOrder/PropositionalBridge.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/PropositionalBridge.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html#prop-language).

## Embedding propositions as first-order sentences

The translation of propositions over a
type of atoms into sentences of the first-order language of propositional atoms, defined by
recursion: an atom $a$ becomes the atomic sentence given by the nullary relation symbol of $a$,
and $A \wedge B$, $A \vee B$ and $A \to B$ become the conjunction, the disjunction and the
implication of the translations of $A$ and $B$.

Formalized by `Cslib.Logic.FOL.Proposition.embed`, a definition declared in [CSLibExt/Logics/FirstOrder/PropositionalBridge.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/PropositionalBridge.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html#embed).

## Boolean structure of a valuation

Given a valuation $v$ assigning a Boolean to each
atom, the Boolean structure of $v$ is the structure for the first-order language of
propositional atoms whose domain is the set of Booleans $\{\mathrm{false}, \mathrm{true}\}$
and in which the nullary relation symbol of an atom $a$ holds exactly when $v(a)$ is true.
The language has no function symbols, so nothing else needs to be interpreted.

Formalized by `Cslib.Logic.FOL.Proposition.boolStructure`, a definition declared in [CSLibExt/Logics/FirstOrder/PropositionalBridge.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/PropositionalBridge.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html#bool-structure).

## The embedding of propositions preserves truth-table semantics

For every valuation $v$
assigning a Boolean to each atom and every proposition $A$, the first-order sentence obtained
by embedding $A$ is true in the Boolean structure of $v$ if and only if the truth-table value
of $A$ under $v$ is true.

Formalized by `Cslib.Logic.FOL.Proposition.realize_embed_iff_evalBool`, a theorem declared in [CSLibExt/Logics/FirstOrder/PropositionalBridge.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/PropositionalBridge.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html#realize-embed-iff-eval-bool).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Embedding propositional logic into first-order logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/first-order-logic/embedding-propositional-logic-into-first-order-l)
