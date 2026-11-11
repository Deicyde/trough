---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OrderedGraph, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogEdge, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OGFO, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.PositiveIn, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.NegativeIn, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.AllLFPPositive, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogBase, MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OGWellFormed
statement: formalized
---

# Immerman–Vardi theorem

13 results, 12 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html).

## Finite ordered graphs

A finite ordered graph is a pair $(n, t)$ of a natural number $n$
and a finite list $t$ of booleans of any length. Here $n$ is the size of the domain
$\{0, \dots, n - 1\}$, ordered numerically, and $t$ is read as a row-major edge table.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OrderedGraph`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#ordered-graph).

## Edge relation of an ordered graph

Let $G$ be an ordered graph with vertices
$0, \dots, n - 1$ and edge table $t$, a list of booleans. There is an edge from $a$ to $b$ when
the entry of $t$ at position $a n + b$ is true; positions beyond the end of $t$ count as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogEdge`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-edge).

## Formulas of first-order logic with least fixed points

Variables and relation symbols are
natural numbers. Formulas are built from equalities $x_a = x_b$ and atoms
$R_i(x_{a_1}, \dots, x_{a_k})$ by negation, conjunction, disjunction, existential quantification
and least-fixed-point formulas $\mathrm{lfp}(R, k, \varphi, (a_1, \dots, a_m))$, the least fixed
point of the operator defined by $\varphi$ (with $R$ as the recursive relation, of arity $k$)
applied to the tuple of variables $(a_1, \dots, a_m)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OGFO`, an inductive type declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#ogfo).

## Positive occurrence of a relation symbol

A relation symbol $R$ occurs only positively in
a first-order formula with least fixed points over ordered graphs when every atomic formula with
relation symbol $R$ in it, including those inside least-fixed-point subformulas whatever symbol
they bind, lies under an even number of negations.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.PositiveIn`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#positive-in).

## Negative occurrence of a relation symbol

A relation symbol $R$ occurs only negatively
in a formula $\varphi$ of first-order logic with least fixed points when every atomic formula
$R(x_{a_1}, \dots, x_{a_k})$ in $\varphi$, including those inside least-fixed-point subformulas,
lies under an odd number of negations.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.NegativeIn`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#negative-in).

## Formulas whose fixed points are all positive

Let $\varphi$ be a formula of first-order
logic with least fixed points, whose relation symbols are natural numbers. All fixed points of
$\varphi$ are positive when every least-fixed-point subformula of $\varphi$, nested ones included,
binds a relation symbol $R \ge 2$ (so neither the order symbol $0$ nor the edge symbol $1$) and
$R$ occurs only positively in the body of that subformula.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.AllLFPPositive`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#all-lfppositive).

## Interpretation of relation symbols in an ordered graph

Let $G$ be an ordered graph with
vertices $0, \dots, n - 1$ and let $(E_i)_{i \in \mathbb{N}}$ be predicates on lists of vertices.
Relation symbol $0$ holds of a list exactly when it is a pair $(a, b)$ with $a < b$, relation
symbol $1$ holds of a list exactly when it is a pair $(a, b)$ with an edge from $a$ to $b$ in $G$,
and relation symbol $i + 2$ is interpreted as $E_i$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogBase`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-base).

## Well-formed FO + LFP formulas

Let $e$ assign to each relation symbol (a natural number)
either an arity or nothing. Whether a first-order formula with least fixed points over ordered
graphs is well-formed relative to $e$ is defined by recursion on the formula. An equality of two
variables is well-formed. An atomic formula $R(x_1, \dots, x_k)$ is well-formed when $k = a$ if
$e(R) = a$; when $k = 2$ if $e$ assigns nothing to $R$ and $R$ is $0$ (the order) or $1$ (the edge
relation); and always otherwise. A negation or an existential quantification is well-formed when
its body is, and a conjunction or a disjunction when both of its parts are. A least-fixed-point
formula that binds the symbol $R$ with arity $a$, has body $\varphi$ and is applied to the
variables $y_1, \dots, y_k$ is well-formed when $R \ge 2$, $k = a$, and $\varphi$ is well-formed
relative to the assignment that agrees with $e$ except that it gives $R$ the arity $a$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.OGWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#ogwell-formed).

## Evaluation of FO + LFP formulas in an ordered graph

Let $G$ be an ordered graph with
vertex set $V = \{0, \dots, n - 1\}$, let $\rho$ assign a vertex to each variable
$0, 1, 2, \dots$, and let $S$ assign to each relation symbol $i$ a predicate $S_i$ on lists of
vertices. The truth of a formula is defined by recursion: $x_a = x_b$ holds when
$\rho(a) = \rho(b)$; the atom $R_i(x_{a_1}, \dots, x_{a_k})$ holds when $S_i$ holds of
$(\rho(a_1), \dots, \rho(a_k))$; negation, conjunction and disjunction are evaluated as usual;
$\exists \varphi$ holds when $\varphi$ holds for some $v \in V$ under the assignment sending
variable $0$ to $v$ and variable $j + 1$ to $\rho(j)$. The least-fixed-point formula with bound
symbol $R$, arity $k$, body $\varphi$ and argument variables $a_1, \dots, a_m$ holds when
$(\rho(a_1), \dots, \rho(a_m))$ lies in $X_{n^k}$, where $X_0$ is empty and a list $t$ lies in
$X_{s+1}$ when $\varphi$ holds with $R$ reinterpreted as $X_s$ (the other symbols keeping their
interpretation under $S$) and with variable $j$ assigned the $j$-th entry of $t$ (or $\rho(0)$
if $t$ has no such entry) for $j < k$ and $\rho(j - k)$ for $j \ge k$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-eval).

## Satisfaction of an FO + LFP formula by an ordered graph

An ordered graph $G$ with $n > 0$
vertices satisfies a formula $\varphi$ of first-order logic with least fixed points when $\varphi$
is well-formed in the environment where no relation symbol is bound, all fixed points of
$\varphi$ are positive, and $\varphi$ is true in $G$ with every variable assigned the vertex $0$,
relation symbol $0$ interpreted as the order $<$, relation symbol $1$ as the edge relation, and
every other relation symbol as the empty relation.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogLFPSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-lfpsat).

## Encodings of a class of ordered graphs

For a class $K$ of ordered graphs, this is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of pairs of a natural number and a list of booleans, to some $G \in K$ whose
edge table has length exactly $n^2$, where $n$ is the number of vertices of $G$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogEncodings`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-encodings).

## Definability in FO + LFP

A class $K$ of ordered graphs is definable in first-order logic
with least fixed points when there are a formula $\varphi$ and a boolean $b$ such that every
ordered graph $G$ with $n$ vertices whose edge table has length $n^2$ lies in $K$ exactly when
either $n > 0$ and $G$ satisfies $\varphi$, or $n = 0$ and $b$ is true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.ogLFPDefinable`, a definition declared in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#og-lfpdefinable).

## Immerman-Vardi: FO + least fixed point is P on ordered structures

Source: N.
Immerman, "Relational queries definable in polynomial time", Information and Control 68
(1986), 193-243 (STOC 1983); M. Y. Vardi, "The complexity of relational query languages",
Proceedings of the Fourteenth Annual ACM Symposium on Theory of Computing (STOC 1982),
137-146.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.ImmermanVardi.immerman_vardi` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ImmermanVardiWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html#immerman-vardi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Immerman–Vardi theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/descriptive-complexity/immerman-vardi-theorem)
