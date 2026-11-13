---
declaration: section
origin: cited
lean: Cslib.Logic.PL.Proposition.shannon, Cslib.Logic.PL.Proposition.evalBool_shannon, Cslib.Logic.PL.exists_evalBool_eq, Cslib.Logic.PL.Proposition.IsImpBot, Cslib.Logic.PL.Proposition.toImpBot, Cslib.Logic.PL.Proposition.evalBool_toImpBot, Cslib.Logic.PL.exists_isImpBot_evalBool_eq, Cslib.Logic.PL.derivableIn_cpl_toImpBot_iff
statement: formalized
proof: formalized
---

# Functional completeness

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html).

## Proposition

## Shannon expansion

Let $f$ assign a truth value to every valuation of the atoms. The
Shannon expansion $S(\ell, f)$ of $f$ over a list $\ell$ of atoms is defined by recursion on
$\ell$. For the empty list it is $\bot \to \bot$ if $f$ is true at the valuation that makes every
atom false, and $\bot$ otherwise. For the list $x \cdot \ell$ with head $x$ and tail $\ell$,

$$
S(x \cdot \ell, f) = (x \wedge S(\ell, f_1)) \vee (\neg x \wedge S(\ell, f_0)),
$$

where $\neg x$ is $x \to \bot$, and $f_1(v) = f(v[x \mapsto \mathrm{true}])$ and
$f_0(v) = f(v[x \mapsto \mathrm{false}])$, with $v[x \mapsto b]$ the valuation $v$ changed at $x$
to $b$.

Formalized by `Cslib.Logic.PL.Proposition.shannon`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#shannon).

## Correctness of the Shannon expansion

Let $x_1, \dots, x_n$ be a list of atoms and let
$f$ assign a truth value to every valuation of the atoms, such that $f(v) = f(w)$ whenever $v$
and $w$ agree on $x_1, \dots, x_n$. Then for every valuation $v$ that makes $\bot$ false, the
Shannon expansion of $f$ over $x_1, \dots, x_n$ has truth value $f(v)$ under $v$.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_shannon`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#eval-bool-shannon).

## Functional completeness

Every Boolean function of the atoms in a finite list is the
truth table, on valuations with `⊥` false, of some proposition.

Formalized by `Cslib.Logic.PL.exists_evalBool_eq`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#exists-eval-bool-eq).

## Propositions built from $\to$ and $\bot$

A proposition is built from $\to$ and $\bot$
when it contains no conjunction and no disjunction: every atom (including $\bot$, which is an
atom) is, and $A \to B$ is exactly when both $A$ and $B$ are.

Formalized by `Cslib.Logic.PL.Proposition.IsImpBot`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#is-imp-bot).

## Translation into $\to$ and $\bot$

The translation $A^*$ of a proposition $A$ is defined
by recursion on $A$: each atom is unchanged, $(A \to B)^* = A^* \to B^*$,
$(A \wedge B)^* = (A^* \to (B^* \to \bot)) \to \bot$ and $(A \vee B)^* = (A^* \to \bot) \to B^*$.

Formalized by `Cslib.Logic.PL.Proposition.toImpBot`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#to-imp-bot).

## The translation into $\to$ and $\bot$ preserves truth values

For every proposition $A$
and every valuation $v$ that makes $\bot$ false, the translation of $A$ into $\to$ and $\bot$
has the same truth value under $v$ as $A$.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_toImpBot`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#eval-bool-to-imp-bot).

## Functional completeness of `→` and `⊥`

Every Boolean function of the atoms in a
finite list is the truth table, on valuations with `⊥` false, of a proposition built with
`→` alone.

Formalized by `Cslib.Logic.PL.exists_isImpBot_evalBool_eq`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#exists-is-imp-bot-eval-bool-eq).

## The translation into $\to$ and $\bot$ preserves and reflects classical derivability

For every proposition $A$, let $A^*$ be its translation into $\to$ and $\bot$, which keeps atoms
and implications and recursively replaces each $B \wedge C$ by $(B \to (C \to \bot)) \to \bot$
and each $B \vee C$ by $(B \to \bot) \to C$. Then $A^*$ is derivable from no hypotheses in
classical propositional logic if and only if $A$ is.

Formalized by `Cslib.Logic.PL.derivableIn_cpl_toImpBot_iff`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/FunctionalCompleteness.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html#derivable-in-cpl-to-imp-bot-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Functional completeness](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/functional-completeness/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/functional-completeness)
