---
declaration: section
origin: cited
lean: Cslib.Algorithms.SAT.TwoSAT.IsTwoCNF, Cslib.Algorithms.SAT.TwoSAT.neg, Cslib.Algorithms.SAT.TwoSAT.eq_or_eq_of_length_le_two, Cslib.Algorithms.SAT.TwoSAT.ImpEdge, Cslib.Algorithms.SAT.TwoSAT.ImpReach, Cslib.Algorithms.SAT.TwoSAT.ImpEdge.skew, Cslib.Algorithms.SAT.TwoSAT.satisfies_of_impEdge, Cslib.Algorithms.SAT.TwoSAT.Inv
statement: formalized
proof: formalized
---

# 2-satisfiability

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html).

## 2-CNF formulas

A CNF formula is a 2-CNF formula when each of its clauses, viewed as a
list of literals, has length at most $2$ (repeated literals are counted with multiplicity).

Formalized by `Cslib.Algorithms.SAT.TwoSAT.IsTwoCNF`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#is-two-cnf).

## Complement of a literal

The complement of a literal $(x, b)$, with variable index
$x \in \mathbb{N}$ and polarity $b$, is the literal $(x, \lnot b)$: same variable, opposite
polarity.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.neg`, an abbreviation declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#neg).

## Clauses with at most two literals

In a clause with at most two literals, any two different
members $a$ and $b$ are all of its members: every member $c$ of the clause equals $a$ or $b$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.eq_or_eq_of_length_le_two`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#eq-or-eq-of-length-le-two).

## Implication edge

For a CNF formula $\varphi$ and literals $l$ and $m$, there is an
implication edge from $l$ to $m$ when some clause of $\varphi$ contains both $\neg l$ and $m$,
either as two different literals or with $m$ as its only literal (so a unit clause $m$ gives
the edge from $\neg m$ to $m$).

Formalized by `Cslib.Algorithms.SAT.TwoSAT.ImpEdge`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#imp-edge).

## Reachability in the implication graph

For a CNF formula $\varphi$, a literal $l$ reaches
a literal $m$ when there is a path of zero or more implication edges of $\varphi$ from $l$ to
$m$; that is, reachability is the reflexive-transitive closure of the implication edge
relation.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.ImpReach`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#imp-reach).

## Skew symmetry of the implication graph

For a CNF formula $\varphi$ and literals $l$ and
$m$, if the implication graph of $\varphi$ has an edge from $l$ to $m$, then it also has the
contrapositive edge from $\lnot m$ to $\lnot l$, where $\lnot$ denotes the complementary
literal.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.ImpEdge.skew`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#skew).

## Satisfying assignments respect implication edges

Let $\varphi$ be a 2-CNF formula and
$\sigma$ an assignment of truth values to the variables that satisfies $\varphi$. If the
implication graph of $\varphi$ has an edge from a literal $l$ to a literal $m$ and $\sigma$
satisfies $l$, then $\sigma$ satisfies $m$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.satisfies_of_impEdge`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#satisfies-of-imp-edge).

## Resolution invariant of the implication graph

A clause $C$ satisfies the invariant
with respect to a CNF formula $\varphi$ when for every literal $a$ of $C$ there is a literal
$b$ of $C$ such that the complementary literal $\lnot a$ reaches $b$ in the implication graph
of $\varphi$ (by a path of zero or more edges).

Every clause derivable from $\varphi$ by resolution satisfies this invariant.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.Inv`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#inv).

## Resolution refutations give contradictory cycles

If a CNF formula $\varphi$ does not
contain the empty clause and the empty clause is derivable from $\varphi$ by resolution, then
there is a variable $x$ such that the literals $x$ and $\neg x$ reach each other in the
implication graph of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.exists_contradictory_of_resolutionDerivable_nil`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#exists-contradictory-of-resolution-deriv).

## 2-SAT characterization

**2-SAT characterization** (Aspvall, Plass, Tarjan): a 2-CNF formula is satisfiable iff
it has no empty clause and no variable `x` such that `x` and `¬x` reach each other in the
implication graph.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.cnfSat_iff_of_isTwoCNF`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#cnf-sat-iff-of-is-two-cnf).

## Literals over the variables of a formula

For a CNF formula $\varphi$, a literal over
$\varphi$ is a pair $(x, b)$ of a variable index $x \in \mathbb{N}$ and a polarity
$b \in \{\mathrm{true}, \mathrm{false}\}$ such that the variable $x$ occurs in $\varphi$.
These literals are the vertices of the implication graph of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.Lit`, an abbreviation declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#lit).

## Complement of a literal over a formula

For a CNF formula $\varphi$, the complement of a
literal $(x, b)$ over the variables of $\varphi$ is the literal $(x, \lnot b)$, which is again a
literal over the variables of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.Lit.neg`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#neg-2).

## Duplicate-free list of the variables of a CNF formula

For a CNF formula $\varphi$,
this is the list of the variables occurring in the literals of $\varphi$, each exactly once,
in the order of their last occurrences when the clauses of $\varphi$ and their literals are
read from first to last.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.varList`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#var-list).

## List of the literals of a CNF formula

For a CNF formula $\varphi$, this is the list of
all literals over the variables of $\varphi$, each appearing exactly once, arranged variable by
variable: for each variable $x$ of $\varphi$, the positive literal $(x, \mathrm{true})$ is
immediately followed by the negative literal $(x, \mathrm{false})$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.litList`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#lit-list).

## Successors in the implication graph

Let $\varphi$ be a CNF formula and $l$ a literal
over the variables of $\varphi$, and write $\neg l$ for the complementary literal. The
successors of $l$ are the literals $m$ over the variables of $\varphi$ such that the
implication graph of $\varphi$ has an edge from $l$ to $m$: some clause of $\varphi$ contains
$\neg l$ and $m$, either as two different literals or as its only literal. They are listed
without repetition, in the order of the list of all literals over the variables of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.successors`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#successors).

## Adjacency table of the implication graph

For a CNF formula $\varphi$, the hash map that
sends each literal over the variables of $\varphi$ to the list of its implication-graph
successors, that is, of the literals $m$ over the variables of $\varphi$ with an implication edge
from it to $m$.

The table is computed once so that the SCC traversal looks successor lists up in expected
constant time.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.adjacencyTable`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#adjacency-table).

## Implication graph as a finite directed graph

For a CNF formula $\varphi$, the finite
directed graph whose vertices are the literals over the variables of $\varphi$, listed without
repetition, and whose out-neighbours of a literal $l$ are the literals $m$ over the variables of
$\varphi$ with an implication edge from $l$ to $m$, read from the adjacency table of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.implicationGraph`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#implication-graph).

## Implication edges end over variables of the formula

For a CNF formula $\varphi$ and
literals $l$ and $m$, if the implication graph of $\varphi$ has an edge from $l$ to $m$, then
the variable of $m$ occurs in $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.mem_vars_of_impEdge`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#mem-vars-of-imp-edge).

## Reachability in the finite implication graph

For a CNF formula $\varphi$ and literals
$l$ and $m$ over the variables of $\varphi$, $m$ is reachable from $l$ in the implication graph
of $\varphi$, viewed as a finite directed graph on these literals, if and only if $l$ reaches $m$
by implication edges of $\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.implicationGraph_reachable_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#implication-graph-reachable-iff).

## SCC-based 2-SAT decision procedure

For a CNF formula $\varphi$, the procedure returns
false if $\varphi$ contains the empty clause; otherwise it returns true if and only if no block
of the strongly connected components computed for the implication graph of $\varphi$ contains a
literal together with its complementary literal.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.decide2SAT`, a definition declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#decide2-sat).

## A positive literal reaching its complement lies over a variable of the formula

For a CNF
formula $\varphi$ and a variable $x$, if the positive literal $(x, \mathrm{true})$ reaches the
negative literal $(x, \mathrm{false})$ in the implication graph of $\varphi$, then $x$ occurs in
$\varphi$.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.mem_vars_of_impReach_true_false`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#mem-vars-of-imp-reach-true-false).

## Correctness of the SCC-based 2-SAT procedure

For every CNF formula $\varphi$ in which
every clause has at most two literals, the SCC-based 2-SAT decision procedure returns true on
$\varphi$ if and only if $\varphi$ is satisfiable.

Formalized by `Cslib.Algorithms.SAT.TwoSAT.decide2SAT_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/SAT/TwoSAT/Basic.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html#decide2-sat-eq-true-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-satisfiability](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/2-satisfiability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/propositional-logic/2-satisfiability)
