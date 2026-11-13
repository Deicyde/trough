---
declaration: section
origin: cited
lean: Cslib.Language.LeftDerivation, Cslib.Language.IsAmbiguous, Cslib.Language.LeftDerivation.derives, Cslib.Language.LeftDerivation.mem_language, Cslib.Language.LeftDerivation.eq_of_terminal, Cslib.Language.inherentlyAmbiguousLang, Cslib.Language.IsInherentlyAmbiguous, Cslib.Language.inherentlyAmbiguousLang_eq
statement: formalized
proof: formalized
---

# Ambiguity of context-free grammars

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html).

## Leftmost derivation

Let $g$ be a context-free grammar, $u$ a sentential form of $g$, $w$ a
word of terminals and $r_1, \dots, r_n$ a list of rules over the terminals and nonterminals of
$g$. The list $r_1, \dots, r_n$ is a leftmost derivation of $w$ from $u$ in $g$ when every $r_i$
is a production of $g$, and, starting from $u$ and for $i = 1, \dots, n$ in turn, the leftmost
nonterminal of the current sentential form is the left-hand side of $r_i$ and is replaced by the
right-hand side of $r_i$, and the sentential form reached after these $n$ steps is $w$, read as a
string of terminals. In particular the empty list is a leftmost derivation of $w$ from $u$
exactly when $u$ is $w$ read as a string of terminals.

Formalized by `Cslib.Language.LeftDerivation`, an inductive type declared in [CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#left-derivation).

## Ambiguous grammar

A context-free grammar $g$ is **ambiguous** if some word of terminals
$w$ has two leftmost derivations from the start symbol of $g$ that use different lists of rules.

Formalized by `Cslib.Language.IsAmbiguous`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#is-ambiguous).

## Leftmost derivations are derivations

Let $g$ be a context-free grammar. If a sentential
form $u$ has a leftmost derivation in $g$ to a word of terminals $w$, then $u$ derives $w$ in $g$
(by zero or more rewriting steps).

Formalized by `Cslib.Language.LeftDerivation.derives`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#derives).

## Words with a leftmost derivation lie in the language

Let $g$ be a context-free grammar.
If a word of terminals $w$ has a leftmost derivation in $g$ from the start symbol of $g$, then $w$
belongs to the language of $g$.

Formalized by `Cslib.Language.LeftDerivation.mem_language`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#mem-language).

## Leftmost derivations from a word of terminals are empty

Let $g$ be a context-free grammar
and $u$ a word of terminals. If $u$ has a leftmost derivation in $g$ with list of rules $\rho$ to a
word of terminals $w$, then $\rho$ is the empty list and $w = u$.

Formalized by `Cslib.Language.LeftDerivation.eq_of_terminal`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/Ambiguity.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#eq-of-terminal).

## Canonical inherently ambiguous context-free language

The language `{a ^ i b ^ j c ^ k | i = j or j = k}` over the alphabet `Fin 3`
(`0, 1, 2` for `a, b, c`): the standard inherently ambiguous context-free language.

## Sources

- S. Ginsburg, The Mathematical Theory of Context-Free Languages, McGraw-Hill, 1966; J. E. Hopcroft and J. D. Ullman, Introduction to Automata Theory, Languages, and Computation, Addison-Wesley, 1979, Chapter 7.

Formalized by `Cslib.Language.inherentlyAmbiguousLang`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#inherently-ambiguous-lang).

## Inherently ambiguous language

A language is inherently ambiguous when it is context-free and every grammar
generating it is ambiguous.

Formalized by `Cslib.Language.IsInherentlyAmbiguous`, a definition declared in [CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#is-inherently-ambiguous).

## Inherently ambiguous example as a union of two languages

The example language is the union of `a ^ n b ^ n c ^ *` and `a ^ * b ^ n c ^ n`.

Formalized by `Cslib.Language.inherentlyAmbiguousLang_eq`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#inherently-ambiguous-lang-eq).

## The example language is context-free

**The example language is context-free.**

Formalized by `Cslib.Language.inherentlyAmbiguousLang_isContextFree`, a theorem declared in [CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextFree/InherentAmbiguity.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html#inherently-ambiguous-lang-is-context-fre).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ambiguity of context-free grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-free-languages/grammars-and-pushdown-automata/ambiguity-of-context-free-grammars)
