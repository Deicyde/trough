---
declaration: section
origin: cited
lean: Cslib.Logic.PL.Proposition.atoms, Cslib.Logic.PL.Proposition.evalBool_congr, Cslib.Logic.PL.Proposition.fixAtom, Cslib.Logic.PL.Proposition.elimAtom, Cslib.Logic.PL.Proposition.elimAtoms, Cslib.Logic.PL.Proposition.evalBool_elimAtoms, Cslib.Logic.PL.exists_interpolant, Cslib.Logic.PL.exists_interpolant_cpl
statement: formalized
proof: formalized
---

# Craig interpolation

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html).

## Proposition

## Atoms of a proposition

The atoms of a proposition $A$ form the finite set of atoms
occurring in $A$: an atom $x$ has the single atom $x$, and the atoms of $B \wedge C$,
$B \vee C$ and $B \to C$ are the atoms of $B$ together with the atoms of $C$.

Formalized by `Cslib.Logic.PL.Proposition.atoms`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#atoms).

## The truth value depends only on the atoms

If two Boolean valuations $v$ and $w$ agree on
every atom of a proposition $A$, then $A$ has the same truth-table value under $v$ as under
$w$.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_congr`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#eval-bool-congr).

## Substituting a truth value for an atom

For an atom $p$, a Boolean $b$ and a proposition
$A$, the proposition $A[p := b]$ is obtained from $A$ by replacing every occurrence of the atom
$p$ by the constant $\top$, written $\bot \to \bot$, if $b$ is true, and by $\bot$ if $b$ is
false.

Formalized by `Cslib.Logic.PL.Proposition.fixAtom`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#fix-atom).

## Boolean quantification over an atom

For an atom $p$ and a proposition $A$, the Boolean
quantification $\exists p.\, A$ is the disjunction $A[p := \top] \vee A[p := \bot]$, where
$A[p := \top]$ and $A[p := \bot]$ replace the atom $p$ in $A$ by the constant
$\top = (\bot \to \bot)$ and by $\bot$ respectively.

Formalized by `Cslib.Logic.PL.Proposition.elimAtom`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#elim-atom).

## Boolean quantification over a list of atoms

For a list of atoms $p_1, \dots, p_n$ and a
proposition $A$, the iterated Boolean quantification $\exists p_1 \cdots p_n.\, A$ is
$\exists p_1.\, \exists p_2.\, \cdots \exists p_n.\, A$: $A$ is quantified over $p_n$ first and over
$p_1$ last, and for the empty list the result is $A$ itself.

Formalized by `Cslib.Logic.PL.Proposition.elimAtoms`, a definition declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#elim-atoms).

## Truth of a Boolean quantification over a list of atoms

Let $p_1, \dots, p_n$ be a list
of atoms that does not contain $\bot$, let $A$ be a proposition and let $v$ be a Boolean
valuation with $v(\bot)$ false. Then the iterated Boolean quantification
$\exists p_1 \cdots p_n.\, A$ is true under $v$ if and only if $A$ is true under some valuation
$w$ that agrees with $v$ on every atom not in the list.

Formalized by `Cslib.Logic.PL.Proposition.evalBool_elimAtoms`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#eval-bool-elim-atoms).

## Craig interpolation, semantic form

Let $A$ and $B$ be propositions such that every
Boolean valuation $v$ with $v(\bot)$ false that makes $A$ true also makes $B$ true. Then there is
a proposition $I$ whose atoms all lie among the atoms common to $A$ and $B$ together with $\bot$,
such that every valuation $v$ with $v(\bot)$ false that makes $A$ true makes $I$ true, and every
valuation $v$ with $v(\bot)$ false that makes $I$ true makes $B$ true.

Formalized by `Cslib.Logic.PL.exists_interpolant`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#exists-interpolant).

## Craig interpolation for classical natural deduction

Let $A$ and $B$ be propositions such
that $A \to B$ is derivable without assumptions in classical propositional logic $\mathrm{CPL}$
(natural deduction with the axioms $\neg\neg C \to C$). Then there is a proposition $I$ whose
atoms all lie among the atoms common to $A$ and $B$ together with $\bot$, such that $A \to I$
and $I \to B$ are both derivable without assumptions in $\mathrm{CPL}$.

Formalized by `Cslib.Logic.PL.exists_interpolant_cpl`, a theorem declared in [CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/NaturalDeduction/Interpolation.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html#exists-interpolant-cpl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Craig interpolation](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/craig-interpolation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/craig-interpolation)
