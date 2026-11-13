---
declaration: section
origin: cited
lean: Cslib.Logic.PL.Proposition.evalBool, Cslib.Logic.PL.Proposition.evalBool_neg, Cslib.Logic.PL.Theory.BoolEntails, Cslib.Logic.PL.Theory.Derivation.boolSound, Cslib.Logic.PL.DerivableIn.boolSound, Cslib.Logic.PL.evalBool_of_mem_ipl, Cslib.Logic.PL.evalBool_of_mem_cpl, Cslib.Logic.PL.DerivableIn.evalBool_of_cpl
statement: formalized
proof: formalized
---

# Propositional natural deduction

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html).

## Truth-table evaluation

Given a Boolean valuation $v$ of the atoms, the truth value of a
proposition is computed recursively: an atom $x$ has value $v(x)$, $A \wedge B$ is true iff both
$A$ and $B$ are, $A \vee B$ is true iff at least one of them is, and $A \to B$ is true iff $A$ is
false or $B$ is true. Falsum $\bot$, when present, is itself an atom, so its value $v(\bot)$ is
part of the valuation and need not be false.

Formalized by `Cslib.Logic.PL.Proposition.evalBool`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool).

## Truth value of a negation

Suppose the atoms include a distinguished atom $\bot$, and let
$v$ be a Boolean valuation of the atoms with $v(\bot) = \mathrm{false}$. Then for every proposition
$A$, the truth-table value under $v$ of $\neg A$, defined as $A \to \bot$, is the Boolean negation
of the truth-table value of $A$ under $v$.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_neg`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-neg).

## Truth-table consequence

Let $T$ be a theory (a set of propositions), $\Gamma$ a context
(a finite set of propositions) and $A$ a proposition. Then $A$ is a truth-table consequence of
$\Gamma$ in $T$ when every Boolean valuation of the atoms under which all members of $T$ and all
members of $\Gamma$ evaluate to true also makes $A$ evaluate to true.

Formalized by `Cslib.Logic.PL.Theory.BoolEntails`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-entails).

## Soundness of natural deduction for truth tables

Let $T$ be a theory, $\Gamma$ a context and
$A$ a proposition. For every natural-deduction derivation of $\Gamma \vdash A$ with axioms from $T$,
every Boolean valuation of the atoms that makes all members of $T$ and of $\Gamma$ true makes $A$
true.

Formalized by `Cslib.Logic.PL.Theory.Derivation.boolSound`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-sound).

## Truth-table soundness of derivability

Let $T$ be a theory, $\Gamma$ a context and $A$ a
proposition. If the sequent $\Gamma \vdash A$ is derivable in natural deduction with axioms from
$T$, then $A$ is a truth-table consequence of $\Gamma$ in $T$: every Boolean valuation of the
atoms that makes all members of $T$ and of $\Gamma$ true makes $A$ true.

Formalized by `Cslib.Logic.PL.DerivableIn.boolSound`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-sound-2).

## Ex falso is true when falsum is false

Suppose the atoms include a distinguished atom
$\bot$, and let $v$ be a Boolean valuation of the atoms with $v(\bot) = \mathrm{false}$. Then every
instance $\bot \to B$ of ex falso, that is every axiom of intuitionistic propositional logic, is
true under $v$.

Formalized by `Cslib.Logic.PL.evalBool_of_mem_ipl`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-of-mem-ipl).

## Double-negation elimination is true when falsum is false

Suppose the atoms include a
distinguished atom $\bot$, and let $v$ be a Boolean valuation of the atoms with
$v(\bot) = \mathrm{false}$. Then every instance $\neg\neg B \to B$ of double-negation elimination,
that is every axiom of classical propositional logic, is true under $v$.

Formalized by `Cslib.Logic.PL.evalBool_of_mem_cpl`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-of-mem-cpl).

## Classical derivability implies truth under valuations with false falsum

Suppose the atoms
include a distinguished atom $\bot$, and let $v$ be a Boolean valuation of the atoms with
$v(\bot) = \mathrm{false}$. If the sequent $\Gamma \vdash A$ is derivable in classical propositional
logic (natural deduction whose axioms are all instances $\neg\neg B \to B$ of double-negation
elimination) and every member of $\Gamma$ is true under $v$, then $A$ is true under $v$.

Formalized by `Cslib.Logic.PL.DerivableIn.evalBool_of_cpl`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-of-cpl).

## Intuitionistic derivability implies truth under valuations with false falsum

Suppose the
atoms include a distinguished atom $\bot$, and let $v$ be a Boolean valuation of the atoms with
$v(\bot) = \mathrm{false}$. If the sequent $\Gamma \vdash A$ is derivable in intuitionistic
propositional logic (natural deduction whose axioms are all instances $\bot \to B$ of ex falso)
and every member of $\Gamma$ is true under $v$, then $A$ is true under $v$.

Formalized by `Cslib.Logic.PL.DerivableIn.evalBool_of_ipl`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-of-ipl).

## Consistency of classical propositional logic

For every type of atoms with a designated
atom $\bot$, the proposition $\bot$ is not derivable from the empty context in natural deduction
over the classical theory, whose axioms are all instances $\neg\neg A \to A$ of double-negation
elimination, where $\neg A$ abbreviates $A \to \bot$.

Formalized by `Cslib.Logic.PL.not_derivableIn_cpl_bot`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#not-derivable-in-cpl-bot).

## Classical logic proves no atom

Suppose the atoms include a distinguished atom $\bot$. For
every atom $x$, including $\bot$, the proposition $x$ is not derivable from the empty context in
classical propositional logic (natural deduction whose axioms are all instances $\neg\neg B \to B$
of double-negation elimination).

Formalized by `Cslib.Logic.PL.not_derivableIn_cpl_atom`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Semantics.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#not-derivable-in-cpl-atom).

## Satisfiable sets of propositions

A set $S$ of propositions is satisfiable when some
Boolean valuation $v$ of the atoms with $v(\bot) = \mathrm{false}$ makes every member of $S$
true.

Formalized by `Cslib.Logic.PL.BoolSatisfiable`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-satisfiable).

## Consistency relative to a theory

Let $T$ be a theory, that is, a set of propositions. A
set $S$ of propositions is consistent relative to $T$ when there is no finite set
$\Gamma \subseteq S$ such that the sequent $\Gamma \vdash \bot$ is derivable in natural deduction
from $T$.

Formalized by `Cslib.Logic.PL.Theory.ConsistentWith`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#consistent-with).

## Lindenbaum's lemma for propositional natural deduction

Let $T$ be a theory. Every set
$S$ of propositions that is consistent relative to $T$ is contained in a set $M$ that is
consistent relative to $T$ and not properly contained in any other set consistent relative to
$T$.

Formalized by `Cslib.Logic.PL.Theory.exists_maximal_consistentWith`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#exists-maximal-consistent-with).

## Propositions outside a maximal consistent set are refuted by it

Let $T$ be a theory and
$M$ a maximal set of propositions consistent relative to $T$. If a proposition $A$ is not in $M$,
then there is a finite set $\Gamma \subseteq M$ such that the sequent
$\Gamma \cup \{A\} \vdash \bot$ is derivable in natural deduction from $T$.

Formalized by `Cslib.Logic.PL.MaximalConsistent.exists_refutation`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#exists-refutation).

## Maximal consistent sets are deductively closed in propositional natural deduction

Let $T$
be a theory and $M$ a maximal set of propositions consistent relative to $T$. If $\Gamma$ is a
finite subset of $M$ and the sequent $\Gamma \vdash A$ is derivable in natural deduction from $T$,
then $A \in M$.

Formalized by `Cslib.Logic.PL.MaximalConsistent.mem_of_derivableIn`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#mem-of-derivable-in).

## A maximal consistent set contains its theory

Let $T$ be a theory and $M$ a maximal set of
propositions consistent relative to $T$. Then every proposition of $T$ belongs to $M$, that is,
$T \subseteq M$.

Formalized by `Cslib.Logic.PL.MaximalConsistent.subset_theory`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#subset-theory).

## Each proposition or its negation lies in a maximal consistent set

Let $T$ be a theory and
$M$ a maximal set of propositions consistent relative to $T$. Then for every proposition $A$,
either $A \in M$ or $\neg A \in M$, where $\neg A$ is the proposition $A \to \bot$.

Formalized by `Cslib.Logic.PL.MaximalConsistent.mem_or_neg_mem`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#mem-or-neg-mem).

## Truth lemma for propositional natural deduction

Let $T$ be an intuitionistic theory, that
is, one that derives $\bot \to B$ for every proposition $B$. Let $M$ be a set of propositions that
is consistent relative to $T$ and not properly contained in any other set consistent relative to
$T$, and let $v_M$ be the valuation that makes an atom $x$ true exactly when the atomic
proposition $x$ belongs to $M$. Then a proposition $A$ evaluates to true under $v_M$ iff
$A \in M$.

Formalized by `Cslib.Logic.PL.MaximalConsistent.evalBool_eq_true_iff`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#eval-bool-eq-true-iff).

## Model existence for propositional natural deduction

Let $T$ be an intuitionistic theory,
that is, one that derives $\bot \to B$ for every proposition $B$. If a set $S$ of propositions is
consistent relative to $T$, then $T \cup S$ is satisfiable: some Boolean valuation $v$ of the atoms
with $v(\bot) = \mathrm{false}$ makes every member of $T$ and every member of $S$ true.

Formalized by `Cslib.Logic.PL.Theory.ConsistentWith.boolSatisfiable`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-satisfiable-2).

## Strong completeness of classical propositional natural deduction

Let $T$ be a classical
theory, that is, one that derives $\neg\neg B \to B$ for every proposition $B$, where $\neg B$
abbreviates $B \to \bot$. Let $\Gamma$ be a finite set of propositions and $A$ a proposition. If
every Boolean valuation $v$ of the atoms with $v(\bot) = \mathrm{false}$ that makes every member of
$T$ and every member of $\Gamma$ true also makes $A$ true, then the sequent $\Gamma \vdash A$ is
derivable from $T$.

Formalized by `Cslib.Logic.PL.Theory.derivableIn_of_forall_evalBool`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#derivable-in-of-forall-eval-bool).

## Soundness and completeness for classical theories, with ⊥ false

Let $T$ be a classical
theory, that is, one that derives $\neg\neg B \to B$ for every proposition $B$, where $\neg B$
abbreviates $B \to \bot$. For every finite set $\Gamma$ of propositions and every proposition $A$,
the sequent $\Gamma \vdash A$ is derivable from $T$ iff every Boolean valuation $v$ of the atoms
with $v(\bot) = \mathrm{false}$ that makes every member of $T$ and every member of $\Gamma$ true
also makes $A$ true.

Formalized by `Cslib.Logic.PL.Theory.derivableIn_iff_forall_evalBool`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#derivable-in-iff-forall-eval-bool).

## Soundness and completeness for classical theories

Let $T$ be a classical theory, that is,
one that derives $\neg\neg B \to B$ for every proposition $B$, where $\neg B$ abbreviates
$B \to \bot$. For every finite set $\Gamma$ of propositions and every proposition $A$, the sequent
$\Gamma \vdash A$ is derivable from $T$ iff every Boolean valuation of the atoms that makes every
member of $T$ and every member of $\Gamma$ true also makes $A$ true.

Here $\bot$ is a distinguished atom, and these valuations may make it true or false.

Formalized by `Cslib.Logic.PL.Theory.derivableIn_iff_boolEntails`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#derivable-in-iff-bool-entails).

## Completeness for truth tables

Let $\Gamma$ be a finite set of propositions and $A$ a
proposition. The sequent $\Gamma \vdash A$ is derivable in classical propositional logic (natural
deduction with every instance of $\neg\neg B \to B$ as an axiom, where $\neg B$ abbreviates
$B \to \bot$) iff every Boolean valuation $v$ of the atoms with $v(\bot) = \mathrm{false}$ that
makes every member of $\Gamma$ true also makes $A$ true.

Formalized by `Cslib.Logic.PL.derivableIn_cpl_iff`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#derivable-in-cpl-iff).

## Compactness

A set of propositions is satisfiable, with `⊥` false, iff each of its
finite subsets is.

Formalized by `Cslib.Logic.PL.boolSatisfiable_iff_forall_finset`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Completeness.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html#bool-satisfiable-iff-forall-finset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Propositional natural deduction](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/propositional-natural-deduction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/propositional-natural-deduction)
