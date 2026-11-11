---
declaration: section
origin: cited
lean: Cslib.Language.Yields.ne_nil_of_forall_output_ne_nil, Cslib.Language.Nullable, Cslib.Language.nullableDeletions, Cslib.Language.evalForm_le_of_mem_nullableDeletions, Cslib.Language.epsGrammar, Cslib.Language.mem_epsGrammar_rules, Cslib.Language.cases_of_mem_epsGrammar_rules, Cslib.Language.epsGrammar_output_ne_nil
statement: formalized
proof: formalized
---

# Elimination of empty and unit productions

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html).

## No empty words without empty productions

In a context-free grammar in which no
production has an empty right-hand side, every nonempty sentential form yields only nonempty
words.

Formalized by `Cslib.Language.Yields.ne_nil_of_forall_output_ne_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#ne-nil-of-forall-output-ne-nil).

## Nullable nonterminal

A nonterminal $A$ of a context-free grammar $g$ is nullable when $g$
derives the empty word from $A$.

Formalized by `Cslib.Language.Nullable`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#nullable).

## Nullable deletions

For a context-free grammar $g$ and a sentential form $u$, the nullable
deletions of $u$ are the forms obtained from $u$ by deleting any selection of occurrences of
nullable nonterminals, possibly none and possibly all, keeping the remaining symbols in order.
They form a finite set.

Formalized by `Cslib.Language.nullableDeletions`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#nullable-deletions).

## Deleting nullable nonterminals shrinks the denoted language

Let $g$ be a context-free
grammar and $V$ an assignment of a language $V(A)$ to each nonterminal $A$ of $g$ such that the
empty word belongs to $V(A)$ whenever $A$ is nullable (derives the empty word in $g$). If a
sentential form $\alpha'$ is obtained from a sentential form $u$ by deleting some occurrences of
nullable nonterminals, then the language denoted by $\alpha'$ under $V$ is contained in the
language denoted by $u$ under $V$.

Formalized by `Cslib.Language.evalForm_le_of_mem_nullableDeletions`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#eval-form-le-of-mem-nullable-deletions).

## Elimination of $\varepsilon$-productions

For a context-free grammar $g$, the grammar
obtained from $g$ by eliminating $\varepsilon$-productions has the same nonterminals and the
same initial nonterminal as $g$. Its productions are the productions $A \to \alpha'$ such that
$g$ has a production $A \to \alpha$, the form $\alpha'$ is obtained from $\alpha$ by deleting
some (possibly no) occurrences of nullable nonterminals (those deriving the empty word in $g$),
and $\alpha'$ is nonempty.

Formalized by `Cslib.Language.epsGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#eps-grammar).

## Productions of the ε-free grammar

Let $g$ be a context-free grammar with a production
$A \to u$, and let $\alpha$ be a nonempty form obtained from $u$ by deleting some (possibly no)
occurrences of nullable nonterminals. Then $A \to \alpha$ is a production of the grammar obtained
from $g$ by eliminating ε-productions.

Formalized by `Cslib.Language.mem_epsGrammar_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#mem-eps-grammar-rules).

## Productions of the $\varepsilon$-eliminated grammar come from productions of $g$

Let $g$ be a context-free grammar. Every production $A \to \alpha'$ of the grammar obtained
from $g$ by eliminating $\varepsilon$-productions arises from a production $A \to \alpha$ of $g$
with the same left-hand side $A$, such that $\alpha'$ is obtained from $\alpha$ by deleting some
occurrences of nullable nonterminals and $\alpha'$ is nonempty.

Formalized by `Cslib.Language.cases_of_mem_epsGrammar_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#cases-of-mem-eps-grammar-rules).

## The $\varepsilon$-eliminated grammar has no empty productions

For a context-free
grammar $g$, no production of the grammar obtained from $g$ by eliminating
$\varepsilon$-productions has empty right-hand side.

Formalized by `Cslib.Language.epsGrammar_output_ne_nil`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#eps-grammar-output-ne-nil).

## Soundness of ε-production elimination

Let $g$ be a context-free grammar and, for each
nonterminal $A$, let $L_g(A)$ be the language of words $g$ derives from $A$. Then $L_g$ is a
valuation of the grammar obtained from $g$ by eliminating ε-productions: for every production
$A \to \alpha$ of that grammar, the language of $\alpha$ under $L_g$ (the concatenation of the
languages of its symbols, a terminal $a$ denoting $\{a\}$) is contained in $L_g(A)$.

Formalized by `Cslib.Language.isValuation_epsGrammar`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#is-valuation-eps-grammar).

## Completeness of eliminating empty productions

Let $g$ be a context-free grammar.
If a sentential form $\alpha$ of $g$ yields a terminal word $w$ in $g$, then some form
$\alpha'$ obtained from $\alpha$ by deleting some occurrences of nullable nonterminals
yields $w$ in the grammar obtained from $g$ by eliminating $\varepsilon$-productions, and
$w$ is empty if $\alpha'$ is empty.

Formalized by `Cslib.Language.yields_epsGrammar_of_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#yields-eps-grammar-of-yields).

## The $\varepsilon$-eliminated grammar generates the nonempty words of $g$

For a
context-free grammar $g$ and every word $w$ over its terminals, $w$ is generated by the grammar
obtained from $g$ by eliminating $\varepsilon$-productions if and only if $w$ is generated by
$g$ and $w$ is nonempty.

Formalized by `Cslib.Language.epsGrammar_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#eps-grammar-language).

## Reachability by unit productions

Let $g$ be a context-free grammar. A nonterminal
$A$ of $g$ reaches a nonterminal $B$ by unit productions when there is a chain
$A = A_0, A_1, \dots, A_n = B$ with $n \ge 0$ such that each $A_{i-1} \to A_i$ is a
production of $g$. In particular, every nonterminal reaches itself.

Formalized by `Cslib.Language.UnitSteps`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#unit-steps).

## Unit output

A sentential form is a unit output when it consists of a single
nonterminal.

Formalized by `Cslib.Language.IsUnitOutput`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#is-unit-output).

## Nonterminals of a sentential form

For a sentential form $u$, a finite word of terminal
and nonterminal symbols, the nonterminals of $u$ form the finite set of all nonterminals that
occur in $u$.

Formalized by `Cslib.Language.formNTs`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#form-nts).

## Set of nonterminals mentioned by a grammar

The nonterminals mentioned by a context-free
grammar $g$ form the finite set consisting of the initial nonterminal of $g$, the left-hand side
of every production of $g$, and every nonterminal occurring in the right-hand side of a
production of $g$.

Formalized by `Cslib.Language.grammarNTs`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#grammar-nts).

## Unit chains start at mentioned nonterminals

Let $g$ be a context-free grammar and let $B$
be reachable from $A$ by a chain of zero or more unit productions of $g$. If $B$ is the left-hand
side of some production of $g$, then $A$ is among the nonterminals mentioned by $g$ (its initial
nonterminal, the left-hand sides of its productions, and the nonterminals in their right-hand
sides).

Formalized by `Cslib.Language.mem_grammarNTs_of_unitSteps`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#mem-grammar-nts-of-unit-steps).

## Eliminating unit productions

A unit production is one whose output is a single
nonterminal. For a context-free grammar $g$, the grammar obtained by eliminating unit
productions has the same nonterminals and the same start symbol as $g$. Its productions
are the $A \to \alpha$ such that $A$ is a nonterminal mentioned by $g$ (its start symbol
or one occurring in a production of $g$), $g$ has a production $B \to \alpha$ that is not
a unit production, and $A$ reaches $B$ by a chain of zero or more unit productions of $g$.

Formalized by `Cslib.Language.unitGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#unit-grammar).

## Productions of the unit-free grammar

Let $g$ be a context-free grammar, let $B$ be
reachable from $A$ by a chain of zero or more unit productions of $g$, and let $B \to \beta$ be a
production of $g$ whose right-hand side $\beta$ is not a single nonterminal. If $A$ is among the
nonterminals mentioned by $g$, then $A \to \beta$ is a production of the grammar obtained from
$g$ by eliminating unit productions.

Formalized by `Cslib.Language.mem_unitGrammar_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#mem-unit-grammar-rules).

## Productions of the unit-eliminated grammar come from non-unit productions of $g$

Let $g$ be a context-free grammar. For every production $A \to \beta$ of the grammar obtained
from $g$ by eliminating unit productions, there are a nonterminal $B$ and a production
$B \to \beta$ of $g$ such that $\beta$ is not a single nonterminal and $B$ is reachable from $A$
by a possibly empty chain of unit productions of $g$.

Formalized by `Cslib.Language.cases_of_mem_unitGrammar_rules`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#cases-of-mem-unit-grammar-rules).

## Eliminating unit productions leaves no unit production

For every context-free
grammar $g$, no production of the grammar obtained from $g$ by eliminating unit
productions has an output consisting of a single nonterminal.

Formalized by `Cslib.Language.unitGrammar_not_isUnitOutput`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#unit-grammar-not-is-unit-output).

## Eliminating unit productions creates no new outputs

Let $g$ be a context-free
grammar. For every production of the grammar obtained from $g$ by eliminating unit
productions, some production of $g$ has the same output.

In particular, empty outputs are not created.

Formalized by `Cslib.Language.unitGrammar_output_of_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#unit-grammar-output-of-mem).

## Languages along unit chains

Let $g$ be a context-free grammar and, for each nonterminal
$A$, let $L_g(A)$ be the language of words $g$ derives from $A$. If $B$ is reachable from $A$ by
a chain of zero or more unit productions $A \to A_1 \to \dots \to B$ of $g$, then
$L_g(B) \subseteq L_g(A)$.

Formalized by `Cslib.Language.languageFrom_le_of_unitSteps`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#language-from-le-of-unit-steps).

## Soundness of unit-production elimination

Let $g$ be a context-free grammar and, for
each nonterminal $A$, let $L_g(A)$ be the language of words $g$ derives from $A$. Then $L_g$ is a
valuation of the grammar obtained from $g$ by eliminating unit productions: for every production
$A \to \alpha$ of that grammar, the language of $\alpha$ under $L_g$ (the concatenation of the
languages of its symbols, a terminal $a$ denoting $\{a\}$) is contained in $L_g(A)$.

Formalized by `Cslib.Language.isValuation_unitGrammar`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#is-valuation-unit-grammar).

## Eliminating unit productions keeps every yield

Let $g$ be a context-free grammar.
If a sentential form $\alpha$ of $g$ yields a terminal word $w$ in $g$, then $\alpha$
yields $w$ in the grammar obtained from $g$ by eliminating unit productions.

Formalized by `Cslib.Language.yields_unitGrammar_of_yields`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#yields-unit-grammar-of-yields).

## Eliminating unit productions preserves the language

For every context-free
grammar $g$, the grammar obtained from $g$ by eliminating unit productions generates
the same language as $g$.

Formalized by `Cslib.Language.unitGrammar_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#unit-grammar-language).

## Reduced grammars

A context-free grammar is reduced when no production has empty
right-hand side and no production has a single nonterminal as its right-hand side.

This is the sense used for the pumping lemma and normal forms. It does not assert that every
nonterminal is reachable or productive.

Formalized by `Cslib.Language.IsReduced`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#is-reduced).

## Existence of reduced grammars

For every context-free grammar $g$ over an alphabet $T$
there is a context-free grammar $g'$ over $T$ that generates exactly the nonempty words
generated by $g$, such that no production of $g'$ has empty right-hand side and no production
of $g'$ has a single nonterminal as its right-hand side.

Formalized by `Cslib.Language.exists_reduced_grammar`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Reduced.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/Reduced.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html#exists-reduced-grammar).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elimination of empty and unit productions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/elimination-of-empty-and-unit-productions)
