---
declaration: section
origin: cited
lean: Symbol.isNonterminal, Cslib.Language.CSGrammar, Cslib.Language.Rewrites, Cslib.Language.Derives, Cslib.Language.language, Cslib.Language.IsContextSensitive, Cslib.Language.ABC, Cslib.Language.ABCNT
statement: formalized
proof: formalized
---

# Context-sensitive grammars

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html).

## Nonterminal grammar symbols

Whether a grammar symbol (`Mathlib.Computability.Language.Symbol`,
shared with the context-free development) is a nonterminal.

Formalized by `Symbol.isNonterminal`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#is-nonterminal).

## Unrestricted grammar

An unrestricted grammar: a finite list of productions and an
initial nonterminal.

Formalized by `Cslib.Language.CSGrammar`, a structure declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#csgrammar).

## One rewriting step of a grammar

One rewriting step: apply a production in a sentential form
context. This is the generic `Cslib.Decidability.Rewriting.Step` at the
grammar's rules, so grammar derivations reuse the string-rewriting API
instead of a second, incompatible copy of it.

Formalized by `Cslib.Language.Rewrites`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#rewrites).

## Derivation in an unrestricted grammar

Derivation: the reflexive-transitive closure of rewriting.

Formalized by `Cslib.Language.Derives`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#derives).

## Language of an unrestricted grammar

The language of a grammar: terminal words derived from the initial
nonterminal.

Formalized by `Cslib.Language.language`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#language).

## Context-sensitive grammar

A grammar is context-sensitive when every production has a
nonterminal on its left side (so the left side is nonempty and not
terminal-only) and no production shrinks. The standard `S → ε`
exception is not used here: the `aⁿbⁿcⁿ` grammar has `n ≥ 1`.

Formalized by `Cslib.Language.IsContextSensitive`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#is-context-sensitive).

## Terminals of the $a^n b^n c^n$ grammar

Terminals of the `aⁿbⁿcⁿ` grammar.

Formalized by `Cslib.Language.ABC`, an inductive type declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#abc).

## Nonterminals of the $a^n b^n c^n$ grammar

Nonterminals of the `aⁿbⁿcⁿ` grammar.

Formalized by `Cslib.Language.ABCNT`, an inductive type declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#abcnt).

## Context-sensitive grammar for $a^n b^n c^n$

The standard context-sensitive grammar for `{aⁿbⁿcⁿ | n ≥ 1}`.

Formalized by `Cslib.Language.abcGrammar`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#abc-grammar).

## Applying a production in context is a grammar step

One grammar step: rewrite `lhs` to `rhs` in context `p, q`.

Formalized by `Cslib.Language.step`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#step).

## The $a^n b^n c^n$ grammar is context-sensitive

Every production of the `aⁿbⁿcⁿ` grammar is length-nondecreasing,
so the grammar is context-sensitive.

Formalized by `Cslib.Language.abcGrammar_contextSensitive`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#abc-grammar-context-sensitive).

## The word abc is generated by the $a^n b^n c^n$ grammar

`abc` is generated.

Formalized by `Cslib.Language.abc_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#abc-mem).

## The word aabbcc is generated by the $a^n b^n c^n$ grammar

`aabbcc` is generated: grow two `a`'s, shuttle the `C`'s right past
the `B`'s, then convert `B`'s and `C`'s to terminals in order.

Formalized by `Cslib.Language.aabbcc_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#aabbcc-mem).

## Symbol count of a sentential form

Count of the symbol `s` in a sentential form (terminals `a`, `b`,
`c`, and the "unborn" `b`/`c` nonterminals `B`, `C`).

Formalized by `Cslib.Language.cnt`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#cnt).

## Count of a's in a sentential form

The `a`-count of a sentential form.

Formalized by `Cslib.Language.cntA`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#cnt-a).

## Count of b's in a sentential form

The `b`-count: terminal `b`'s plus unborn `B`'s.

Formalized by `Cslib.Language.cntB`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#cnt-b).

## Count of c's in a sentential form

The `c`-count: terminal `c`'s plus unborn `C`'s.

Formalized by `Cslib.Language.cntC`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#cnt-c).

## Balanced sentential form

A sentential form is balanced when its `a`-, `b`- and `c`-counts
agree.

Formalized by `Cslib.Language.Balanced`, a definition declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#balanced).

## Symbol counts are additive over concatenation

Counting over a concatenation of three forms splits additively.

Formalized by `Cslib.Language.cnt_concat3`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#cnt-concat3).

## Rewriting steps preserve balancedness

One rewriting step preserves balancedness: every production has
the same imbalance on both sides, and the context contributes equally
to all three counts.

Formalized by `Cslib.Language.rewrites_balanced`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#rewrites-balanced).

## Derivations preserve balancedness

Derivations preserve balancedness.

Formalized by `Cslib.Language.derives_balanced`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#derives-balanced).

## The initial sentential form is balanced

The initial form `[S]` is balanced, with all counts zero.

Formalized by `Cslib.Language.balanced_initial`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#balanced-initial).

## Generated words have equally many a's, b's and c's

Every generated terminal word has equally many `a`'s, `b`'s and
`c`'s.

Formalized by `Cslib.Language.language_subset_balanced`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#language-subset-balanced).

## The word aabbc is not generated by the $a^n b^n c^n$ grammar

`aabbc` is not generated: its counts are `2 = 2 ≠ 1`.

Formalized by `Cslib.Language.aabbc_not_mem`, a theorem declared in [CSLibExt/Computability/Languages/ContextSensitive/Basic.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Languages/ContextSensitive/Basic.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html#aabbc-not-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Context-sensitive grammars](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/context-sensitive-languages/context-sensitive-grammars)
