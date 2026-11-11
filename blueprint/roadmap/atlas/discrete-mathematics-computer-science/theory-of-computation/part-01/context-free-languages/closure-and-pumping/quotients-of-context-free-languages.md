---
declaration: section
origin: cited
lean: Cslib.Language.rightQuotientLang, Cslib.Language.RightQuotientLang.leftWords, Cslib.Language.RightQuotientLang.rightWords, Cslib.Language.RightQuotientLang.leftDFA, Cslib.Language.RightQuotientLang.rightDFA, Cslib.Language.RightQuotientLang.unmark, Cslib.Language.IsContextFree.rightQuotientLang, Cslib.Language.IsContextFree.leftQuotientLang
statement: formalized
proof: formalized
---

# Quotients of context-free languages

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html).

## Right quotient of a language by a language

For languages $L$ and $R$ over an alphabet $T$,
the right quotient of $L$ by $R$ is the language of all words $x$ over $T$ such that the
concatenation $xy$ lies in $L$ for some word $y \in R$.

Formalized by `Cslib.Language.rightQuotientLang`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#right-quotient-lang).

## Words over the left copy of a doubled alphabet

For an alphabet $T$, write $T \sqcup T$ for
the disjoint union of a left and a right copy of $T$. This is the language over $T \sqcup T$ of the
words obtained from a word $x$ over $T$ by replacing each letter with its left copy.

Formalized by `Cslib.Language.RightQuotientLang.leftWords`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#left-words).

## Words of a language marked by the right copy

For a language $R$ over an alphabet $T$, write
$T \sqcup T$ for the disjoint union of a left and a right copy of $T$. This is the language over
$T \sqcup T$ of the words obtained from a word $y \in R$ by replacing each letter with its right
copy.

Formalized by `Cslib.Language.RightQuotientLang.rightWords`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#right-words).

## Automaton for words over the left copy

For an alphabet $T$, write $T \sqcup T$ for the
disjoint union of a left and a right copy of $T$. This is the deterministic automaton over
$T \sqcup T$ with the two states true and false, whose start state and only accepting state are
true, and which moves from state $b$ on a letter $c$ to true exactly when $b$ is true and $c$ lies
in the left copy, and to false otherwise.

Formalized by `Cslib.Language.RightQuotientLang.leftDFA`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#left-dfa).

## Automaton running a deterministic automaton on the right copy

Let $D$ be a deterministic
automaton over an alphabet $T$, and write $T \sqcup T$ for the disjoint union of a left and a right
copy of $T$. This is the deterministic automaton over $T \sqcup T$ whose states are the states of
$D$ together with one extra dead state $\bot$. From a state $p$ of $D$, on the right copy of a
letter $a$ it moves to the state that $D$ reaches from $p$ on $a$; on a letter of the left copy,
and from $\bot$ on any letter, it moves to $\bot$. Its start state is the start state of $D$, and
its accepting states are the accepting states of $D$.

Formalized by `Cslib.Language.RightQuotientLang.rightDFA`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#right-dfa).

## Forgetting the copy of a letter

For an alphabet $T$, write $T \sqcup T$ for the disjoint
union of a left and a right copy of $T$. This map sends the left copy and the right copy of a
letter $a \in T$ to the one-letter word $a$ over $T$.

Formalized by `Cslib.Language.RightQuotientLang.unmark`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#unmark).

## The right quotient of a context-free language by a regular language is context-free

**The right quotient of a context-free language by a regular language is context-free**, over
a finite alphabet.

Formalized by `Cslib.Language.IsContextFree.rightQuotientLang`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/ContextFree/RightQuotient.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#right-quotient-lang-2).

## The left quotient of a context-free language by a regular language is context-free

**The left quotient of a context-free language by a regular language is context-free**, over
a finite alphabet.

Formalized by `Cslib.Language.IsContextFree.leftQuotientLang`, a theorem declared in [CSLibExt/Computability/Languages/QuotientClosures.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Languages/QuotientClosures.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html#left-quotient-lang).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quotients of context-free languages](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/context-free-languages/closure-and-pumping/quotients-of-context-free-languages)
