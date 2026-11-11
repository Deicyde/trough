---
declaration: section
origin: cited
lean: Cslib.Logic.PL.CNF.posClauses, Cslib.Logic.PL.CNF.negClauses, Cslib.Logic.PL.CNF.eliminate, Cslib.Logic.PL.CNF.fst_ne_of_mem_resolvent, Cslib.Logic.PL.CNF.satisfies_eliminate, Cslib.Logic.PL.CNF.exists_satisfies_update_of_satisfies_eliminate, Cslib.Logic.PL.CNF.cnfSat_eliminate_iff, Cslib.Logic.PL.CNF.eliminateAll
statement: formalized
proof: formalized
---

# Davis–Putnam algorithm

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html).

## Clauses containing a variable only positively

For a variable $x$ and a CNF formula
$\varphi$, the formula consisting of the clauses of $\varphi$, in their order, that contain the
literal $x$ and do not contain the literal $\neg x$.

Formalized by `Cslib.Logic.PL.CNF.posClauses`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#pos-clauses).

## Clauses containing a variable only negatively

For a variable $x$ and a CNF formula
$\varphi$, the formula consisting of the clauses of $\varphi$, in their order, that contain the
literal $\neg x$ and do not contain the literal $x$.

Formalized by `Cslib.Logic.PL.CNF.negClauses`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#neg-clauses).

## Davis-Putnam elimination of a variable

Eliminating a variable $x$ from a CNF formula
$\varphi$ gives the formula consisting of the clauses of $\varphi$ that contain neither $x$ nor
$\neg x$, followed by the resolvents on $x$ of $C$ and $D$, for every clause $C$ of $\varphi$ that
contains $x$ but not $\neg x$ and every clause $D$ of $\varphi$ that contains $\neg x$ but not $x$.
Clauses containing both $x$ and $\neg x$ are dropped.

Formalized by `Cslib.Logic.PL.CNF.eliminate`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#eliminate).

## Resolvents do not mention the resolved variable

Let $x$ be a variable and let $C$ and $D$
be clauses such that $C$ does not contain $\neg x$ and $D$ does not contain $x$. Then no literal
of the resolvent of $C$ and $D$ on $x$ has variable $x$.

In particular, the resolvents added when eliminating $x$ do not mention $x$.

Formalized by `Cslib.Logic.PL.CNF.fst_ne_of_mem_resolvent`, a theorem declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#fst-ne-of-mem-resolvent).

## Soundness of a Davis-Putnam step

Let $x$ be a variable and $\varphi$ a CNF formula. Every
assignment that satisfies $\varphi$ also satisfies the formula obtained from $\varphi$ by
eliminating $x$.

Formalized by `Cslib.Logic.PL.CNF.satisfies_eliminate`, a theorem declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#satisfies-eliminate).

## Completeness of a Davis-Putnam step

Let $x$ be a variable, $\varphi$ a CNF formula and
$\sigma$ an assignment that satisfies the formula obtained from $\varphi$ by eliminating $x$. Then
there is a truth value $b$ such that the assignment that agrees with $\sigma$ except that it sends
$x$ to $b$ satisfies $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.exists_satisfies_update_of_satisfies_eliminate`, a theorem declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#exists-satisfies-update-of-satisfies-eli).

## Davis-Putnam elimination preserves satisfiability

For every variable $x$ and every CNF
formula $\varphi$, the formula obtained from $\varphi$ by eliminating $x$ is satisfiable if and
only if $\varphi$ is satisfiable.

Formalized by `Cslib.Logic.PL.CNF.cnfSat_eliminate_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#cnf-sat-eliminate-iff).

## Successive elimination of a list of variables

Given a list $x_1, \dots, x_n$ of variables
and a CNF formula $\varphi$, eliminate $x_1$ from $\varphi$, then $x_2$ from the result, and so on
up to $x_n$. For the empty list the result is $\varphi$.

Formalized by `Cslib.Logic.PL.CNF.eliminateAll`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#eliminate-all).

## Variable list for Davis–Putnam elimination

For a CNF formula $\varphi$, the list of the
variables occurring in the literals of $\varphi$, each listed exactly once, in order of first
occurrence when the clauses of $\varphi$, and the literals within each clause, are read from left
to right.

Removing the repetitions takes time quadratic in the number of literal occurrences, which the
eliminations dominate.

Formalized by `Cslib.Logic.PL.CNF.varList`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#var-list).

## The Davis-Putnam procedure

Given a CNF formula $\varphi$, eliminate the variables
that occur in $\varphi$ one after another, each exactly once, in the order of their first
occurrence in $\varphi$, each elimination being applied to the result of the previous one. The
procedure returns true if the resulting formula does not contain the empty clause, and false if
it does.

Formalized by `Cslib.Logic.PL.CNF.davisPutnam`, a definition declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#davis-putnam).

## Correctness of the Davis-Putnam procedure

For every CNF formula $\varphi$, the
Davis-Putnam procedure returns true on $\varphi$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Logic.PL.CNF.davisPutnam_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/DavisPutnam/Basic.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html#davis-putnam-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Davis–Putnam algorithm](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/davis-putnam-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/propositional-logic/davis-putnam-algorithm)
