---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Fagin.FaginGraph, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEdge, MetaMathlibExt.Complexity.KeyTheorems.Fagin.FaginFO, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEval, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginBase, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginESOSat, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEncodings, MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginIso
statement: formalized
---

# Fagin's theorem

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html).

## Finite graphs as edge tables

A finite graph is a pair $(n, t)$ of a natural number $n$,
the number of vertices, and a finite list $t$ of booleans, read as a row-major edge table. The
length of $t$ is not required to be $n^2$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.FaginGraph`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-graph).

## Edge relation of a graph

Let $G$ be a graph with vertices $0, \dots, n-1$ and edge table
$t$, a finite list of booleans. For vertices $a, b < n$, there is an edge from $a$ to $b$ exactly
when the entry of $t$ at position $an + b$ (counting from $0$) is true; a position beyond the end
of $t$ counts as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEdge`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-edge).

## First-order formulas over graphs

Variables and relation symbols are indexed by natural
numbers. Formulas are built from equations $x_a = x_b$ between variables and atomic formulas
applying a relation symbol $i$ to a finite list of variables, by negation, conjunction,
disjunction and existential quantification $\exists \varphi$, which binds variable $0$ of
$\varphi$ (de Bruijn indexing).

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.FaginFO`, an inductive type declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-fo).

## Evaluation of a first-order formula in a graph

Let $G$ be a graph, let $\rho$ assign a
vertex $\rho(j)$ of $G$ to each variable $x_j$ ($j \in \mathbb{N}$), and let $S$ assign to each
relation symbol $i \in \mathbb{N}$ a predicate $S_i$ on finite lists of vertices of $G$. Truth of a
formula is defined by recursion: $x_a = x_b$ holds when $\rho(a) = \rho(b)$; relation symbol $i$
applied to the variables $x_{a_1}, \dots, x_{a_m}$ holds when $S_i$ holds of the list
$[\rho(a_1), \dots, \rho(a_m)]$; negation, conjunction and disjunction are interpreted as usual;
and $\exists \varphi$ holds when there is a vertex $v$ such that $\varphi$ holds under the
assignment sending $x_0$ to $v$ and $x_{j+1}$ to $\rho(j)$ for each $j$, with $S$ unchanged.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-eval).

## Interpretation of relation symbols in a graph

Let $G$ be a graph and let
$(E_j)_{j \in \mathbb{N}}$ be a family of relations, each a predicate on finite lists of vertices
of $G$. Relation symbol $0$ is interpreted as the edge relation of $G$: it holds of a list exactly
when the list is $[a, b]$ for vertices $a, b$ with an edge from $a$ to $b$. For $i \ge 1$, relation
symbol $i$ is interpreted as $E_{i-1}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginBase`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-base).

## Satisfaction of an existential second-order sentence

Let $G$ be a graph with $n > 0$
vertices, $k$ a natural number and $\varphi$ a first-order formula. Then $G$ satisfies the
existential second-order sentence $(k, \varphi)$ if there are relations $R_0, \dots, R_{k-1}$,
each a predicate on finite lists of vertices of $G$, such that $\varphi$ holds in $G$ when
relation symbol $0$ is interpreted as the edge relation (holding exactly of the lists $[a, b]$
with an edge from $a$ to $b$), relation symbol $j + 1$ as $R_j$ for each $j < k$, every relation
symbol above $k$ as the empty relation, and every variable as vertex $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginESOSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-esosat).

## Encodings of a graph class as a decision problem

For a class $K$ of graphs, this is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of pairs of a natural number and a list of booleans, to a graph $G \in K$ with
$n$ vertices whose edge table has length exactly $n^2$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginEncodings`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-encodings).

## Isomorphic graphs

Graphs $G_1$ and $G_2$ are isomorphic if they have the same number of
vertices and there is a bijection $\sigma$ from the vertices of $G_1$ to the vertices of $G_2$
such that for all vertices $a, b$ of $G_1$, there is an edge from $a$ to $b$ in $G_1$ if and only
if there is an edge from $\sigma(a)$ to $\sigma(b)$ in $G_2$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginIso`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-iso).

## Isomorphism-closed graph classes

A class $K$ of graphs is isomorphism-closed if for every
$G_1 \in K$, every graph $G_2$ isomorphic to $G_1$ also belongs to $K$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginIsoClosed`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-iso-closed).

## Existential second-order definable graph classes

A class $K$ of graphs is existential
second-order definable if there are a natural number $k$, a first-order formula $\varphi$ and a
boolean $e$ such that every graph $G$ with $n$ vertices whose edge table has length exactly $n^2$
satisfies the following: if $n > 0$, then $G \in K$ if and only if $G$ satisfies the existential
second-order sentence $(k, \varphi)$; if $n = 0$, then $G \in K$ if and only if $e$ is true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Fagin.faginESODefinable`, a definition declared in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin-esodefinable).

## Fagin's theorem: NP is existential second-order logic

Let $K$ be a class of finite
graphs, each given as a pair $(n, t)$ of a number $n$ of vertices and a row-major edge table $t$
(a list of booleans), and suppose that $K$ is closed under graph isomorphism. Then the decision
problem that accepts exactly the bitstrings decoding to a member $(n, t)$ of $K$ whose edge table
has length $n^2$ is in NP if and only if $K$ is definable in existential second-order logic:
there are a first-order formula $\varphi$, a number $k$ and a boolean $b$ such that a graph
$(n, t)$ whose edge table has length $n^2$ belongs to $K$ exactly when either $n > 0$ and some
$k$ relations on its vertices, together with its edge relation, make $\varphi$ true (with every
free variable of $\varphi$ denoting vertex $0$), or $n = 0$ and $b$ is true.

## Sources

- R. Fagin, "Generalized first-order spectra and polynomial-time recognizable sets", in Complexity of Computation, SIAM-AMS Proceedings 7 (1974), 43-73.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Fagin.fagin` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/FaginWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/FaginWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html#fagin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fagin's theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/descriptive-complexity/fagin-s-theorem)
