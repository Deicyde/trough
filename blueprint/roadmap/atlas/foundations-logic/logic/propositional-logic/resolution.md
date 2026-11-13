---
declaration: section
origin: cited
lean: Cslib.Logic.PL.CNFClause.resolvent, Cslib.Logic.PL.CNFClause.satisfies_resolvent, Cslib.Logic.PL.CNF.ResolutionDerivable, Cslib.Logic.PL.CNF.ResolutionDerivable.satisfies, Cslib.Logic.PL.CNF.not_cnfSat_of_resolutionDerivable_nil, Cslib.Logic.PL.CNF.mem_restrict_iff, Cslib.Logic.PL.CNF.ResolutionDerivable.lift_restrict, Cslib.Logic.PL.CNF.nil_mem_of_vars_eq_empty
statement: formalized
proof: formalized
---

# Resolution

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html).

## Resolvent of two clauses

Let $x$ be a variable and $C$, $D$ clauses. The resolvent of $C$
and $D$ on $x$ is the clause consisting of the literals of $C$ other than $(x, \mathrm{true})$,
in order, followed by the literals of $D$ other than $(x, \mathrm{false})$, in order.

Formalized by `Cslib.Logic.PL.CNFClause.resolvent`, a definition declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#resolvent).

## Resolution rule soundness

Let $x$ be a variable and $C$, $D$ clauses. Every assignment
that satisfies both $C$ and $D$ satisfies the resolvent of $C$ and $D$ on $x$.

Formalized by `Cslib.Logic.PL.CNFClause.satisfies_resolvent`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#satisfies-resolvent).

## Resolution derivability

Given a CNF formula $\varphi$, the clauses derivable from
$\varphi$ by resolution form the smallest set $S$ of clauses that contains every clause of
$\varphi$ and, for every variable $x$ and all clauses $C, D \in S$ such that $C$ contains the
literal $(x, \mathrm{true})$ and $D$ contains the literal $(x, \mathrm{false})$, contains the
resolvent of $C$ and $D$ on $x$.

Formalized by `Cslib.Logic.PL.CNF.ResolutionDerivable`, an inductive type declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#resolution-derivable).

## Soundness of resolution

Let $\varphi$ be a CNF formula. Every clause derivable by
resolution from $\varphi$ is satisfied by every assignment that satisfies $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.ResolutionDerivable.satisfies`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#satisfies).

## Refutable formulas are unsatisfiable

If the empty clause is derivable by resolution
from a CNF formula $\varphi$, then $\varphi$ is not satisfiable.

Formalized by `Cslib.Logic.PL.CNF.not_cnfSat_of_resolutionDerivable_nil`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#not-cnf-sat-of-resolution-derivable-nil).

## Clauses of a restricted formula

Let $\varphi$ be a CNF formula and $\ell$ a literal. A
clause $C$ belongs to the restriction of $\varphi$ by $\ell$ if and only if there is a clause $C_0$
of $\varphi$ that does not contain $\ell$ such that $C$ is the restriction of $C_0$ by $\ell$.

Formalized by `Cslib.Logic.PL.CNF.mem_restrict_iff`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#mem-restrict-iff).

## Lifting lemma

Let $\varphi$ be a CNF formula, $x$ a variable and $b$ a Boolean value. If a
clause $D$ is derivable by resolution from the restriction of $\varphi$ by the literal $(x, b)$,
then some clause $D_0$ is derivable by resolution from $\varphi$ such that every literal of $D_0$
is either a literal of $D$ or the complementary literal $(x, \lnot b)$.

Formalized by `Cslib.Logic.PL.CNF.ResolutionDerivable.lift_restrict`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#lift-restrict).

## Unsatisfiable formulas without variables contain the empty clause

If a CNF formula
$\varphi$ has no variables and is not satisfiable, then the empty clause is one of the clauses
of $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.nil_mem_of_vars_eq_empty`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#nil-mem-of-vars-eq-empty).

## Refutation completeness

**Refutation completeness** of resolution: every unsatisfiable CNF formula has a
resolution derivation of the empty clause.

Formalized by `Cslib.Logic.PL.CNF.resolutionDerivable_nil_of_not_cnfSat`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#resolution-derivable-nil-of-not-cnf-sat).

## Soundness and refutation completeness

A CNF formula has a resolution refutation
iff it is unsatisfiable.

Formalized by `Cslib.Logic.PL.CNF.resolutionDerivable_nil_iff_not_cnfSat`, a theorem declared in [CSLibExt/Logics/Propositional/CNF/Resolution.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/CNF/Resolution.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html#resolution-derivable-nil-iff-not-cnf-sat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Resolution](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/resolution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/resolution)
