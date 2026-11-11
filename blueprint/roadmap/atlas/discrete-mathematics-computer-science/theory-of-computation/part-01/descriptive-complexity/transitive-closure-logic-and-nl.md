---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.FOTC.TCOrderedGraph, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcEdge, MetaMathlibExt.Complexity.KeyTheorems.FOTC.TCFO, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcBase, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcEval, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcParamExample, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcPairExample, MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcSat
statement: formalized
---

# Transitive closure logic and NL

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html).

## Ordered graphs for first-order logic with transitive closure

An ordered graph is
encoded as a pair $(n, e)$ of a natural number $n$, the domain size, and a finite list $e$ of
booleans of arbitrary length, the edge table in row-major order. It is read as the graph on
$\{0, \dots, n - 1\}$, ordered numerically, with an edge from $a$ to $b$ when the entry of $e$ at
position $an + b$ is true; a missing entry counts as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.TCOrderedGraph`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tcordered-graph).

## Edge relation of an ordered graph for FO + TC

For an ordered graph $(n, T)$ with edge
table $T$ and elements $a, b < n$, there is an edge from $a$ to $b$ when the entry of $T$ at
position $a n + b$ is true; positions beyond the end of $T$ count as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcEdge`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-edge).

## Formulas of first-order logic with transitive closure

FO + TC formulas, with variables
and relation symbols indexed by natural numbers, are built from equations between two variables
and relation symbols applied to lists of variables by negation, conjunction, disjunction,
existential quantification (which binds variable $0$, de Bruijn style) and transitive closure
$\mathrm{TC}(\varphi; \bar u, \bar v)$ of a formula $\varphi$ applied to two lists $\bar u$,
$\bar v$ of variables. With $a = |\bar u| = |\bar v|$, the body $\varphi$ defines a step
relation on $a$-tuples: its variables $0, \dots, a - 1$ are the source tuple, $a, \dots, 2a - 1$
the target tuple, and each variable $j \ge 2a$ is outer variable $j - 2a$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.TCFO`, an inductive type declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tcfo).

## Order and edge relations as FO + TC relation symbols

In an ordered graph with domain
$\{0, \dots, n - 1\}$, relation symbol $0$ holds of a list of elements exactly when the list is
$[a, b]$ with $a < b$, relation symbol $1$ holds exactly when the list is $[a, b]$ and there is
an edge from $a$ to $b$, and every other relation symbol holds of no list.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcBase`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-base).

## Evaluation of FO + TC formulas

Fix an ordered graph with domain
$D = \{0, \dots, n - 1\}$, an assignment $\rho$ of an element of $D$ to each variable index and
an assignment $S$ of a relation on lists of elements of $D$ to each relation symbol. The truth
value of a formula is defined by recursion. The equation between variables $i$ and $j$ holds
when $\rho(i) = \rho(j)$. Relation symbol $i$ applied to variables $j_1, \dots, j_k$ holds when
$S_i$ holds of the list $[\rho(j_1), \dots, \rho(j_k)]$. Negation, conjunction and disjunction
are interpreted as usual. An existential formula $\exists \varphi$ holds when $\varphi$ holds
under the assignment sending $0$ to some $d \in D$ and $j + 1$ to $\rho(j)$. A transitive
closure $\mathrm{TC}(\varphi; \bar u, \bar v)$ is false when the index lists $\bar u$ and
$\bar v$ have different lengths. Otherwise, with $a$ their common length, it holds when the
tuple $(\rho(v_0), \dots, \rho(v_{a-1}))$ is reachable from $(\rho(u_0), \dots, \rho(u_{a-1}))$
in zero or more steps, where a step from $s \in D^a$ to $t \in D^a$ means that $\varphi$ holds
under the assignment sending $j < a$ to $s_j$, $a \le j < 2a$ to $t_{j - a}$, and $j \ge 2a$ to
$\rho(j - 2a)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-eval).

## Example: parameterized transitive closure in FO + TC

The FO + TC formula
$\mathrm{TC}(\varphi; (1), (2))$ of arity $1$ whose body $\varphi$ is
$E(0, 1) \lor (E(0, 2) \land E(2, 1))$, where $E$ is relation symbol $1$ (the edge relation).
In the body, variable $0$ is the source, variable $1$ the target, and variable $2$ is outer
variable $0$, shifted by $2$; the endpoint arguments $1$ and $2$ are outer variables, not
shifted. So the formula expresses that outer variable $2$ is reachable from outer variable $1$
by steps that are either an edge or a path of two edges through outer variable $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcParamExample`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-param-example).

## Example: simultaneous reachability of pairs in FO + TC

The FO + TC formula
$\mathrm{TC}(\varphi; (0, 1), (2, 3))$ of arity $2$ whose body $\varphi$ states that relation
symbol $1$ (the edge relation) holds of variables $0, 2$ and of variables $1, 3$. In the body,
variables $0, 1$ are the source pair and $2, 3$ the target pair, so a step moves both components
along an edge at the same time, and the formula expresses that the pair of outer variables
$(2, 3)$ is reachable from the pair $(0, 1)$ by such steps.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcPairExample`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-pair-example).

## Satisfaction of an FO + TC formula in an ordered graph

An ordered graph with nonempty
domain $\{0, \dots, n - 1\}$ satisfies an FO + TC formula $\varphi$ when $\varphi$ evaluates to
true with every variable assigned the element $0$, relation symbol $0$ interpreted as the order
$<$ and relation symbol $1$ as the edge relation (both only on two-element lists), and every
other relation symbol interpreted as the empty relation.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-sat).

## Encodings of a class of ordered graphs

For a set $K$ of ordered graphs, this is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of pairs of a natural number and a list of booleans, to some ordered graph
$(n, T) \in K$ whose edge table $T$ has length exactly $n^2$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcEncodings`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-encodings).

## Definability in FO + TC

A set $K$ of ordered graphs is FO + TC-definable when there
are an FO + TC formula $\varphi$ and a boolean $b$ such that for every ordered graph $(n, T)$
whose edge table $T$ has length exactly $n^2$: if $n > 0$, then $(n, T) \in K$ exactly when
$(n, T)$ satisfies $\varphi$, and if $n = 0$, then $(n, T) \in K$ exactly when $b$ is true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FOTC.tcDefinable`, a definition declared in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#tc-definable).

## Immerman: FO + transitive closure is NL on ordered structures

For every set $K$ of
finite ordered graphs, the decision problem of the encodings of $K$ (the bitstrings that decode
to a member $(n, T)$ of $K$ whose edge table $T$ has length exactly $n^2$) belongs to
$\mathrm{NL}$ if and only if $K$ is definable in first-order logic with transitive closure.

## Sources

- N. Immerman, "Languages that capture complexity classes", SIAM Journal on Computing 16 (1987), 760-778 (STOC 1983).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.FOTC.fo_tc_eq_nl` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/FOTCWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FOTCWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html#fo-tc-eq-nl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transitive closure logic and NL](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/descriptive-complexity/transitive-closure-logic-and-nl)
