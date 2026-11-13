---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.IsTournament, MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.IsTransitiveOn, MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumber, MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumberEqLogTwo, MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumberEqLogTwo_refuted, MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStarBackArcs, MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStar, MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.ContainsTStar
statement: formalized
---

# Transitive subtournaments

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html).

## Tournaments

Let $n \in \mathbb{N}$. A relation $T$ on $\{0, \dots, n-1\}$ is a
tournament when $T(x, x)$ holds for no $x$ and, for all distinct $x$ and $y$, exactly one of
$T(x, y)$ and $T(y, x)$ holds.

Formalized by `MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.IsTournament`, a definition declared in [WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#is-tournament).

## Transitivity on a vertex set

Let $n \in \mathbb{N}$, let $T$ be a relation on
$\{0, \dots, n-1\}$ and let $S$ be a set of its elements. Then $T$ is transitive on $S$ when, for
all $x, y, z \in S$, $T(x, y)$ and $T(y, z)$ imply $T(x, z)$. For a tournament $T$ this says that
the subtournament of $T$ on $S$ is transitive.

Formalized by `MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.IsTransitiveOn`, a definition declared in [WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#is-transitive-on).

## Transitive subtournament number

For $n \in \mathbb{N}$, $f(n)$ is the largest $m$ such
that every tournament $T$ on $\{0, \dots, n-1\}$ is transitive on some set of exactly $m$
vertices, that is, contains a transitive subtournament on $m$ vertices.

Such $m$ exist (for instance $m = 0$) and are at most $n$, so the largest one exists.

Formalized by `MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumber`, a definition declared in [WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#transitive-subtournament-number).

## Erdős Problem 1216 (the Erdős–Moser formula)

For every $n \ge 1$,
$f(n) = \lfloor \log_2 n \rfloor + 1$, where $f(n)$ is the largest $m$ such that every tournament
on $n$ vertices contains a transitive subtournament on $m$ vertices.

Formalized by `MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumberEqLogTwo`, a definition declared in [WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#transitive-subtournament-number-eq-log-t).

## Erdős Problem 1216 is false

It is not the case that $f(n) = \lfloor \log_2 n \rfloor + 1$ for
every $n \ge 1$, where $f(n)$ is the largest $m$ such that every tournament on $n$ vertices
contains a transitive subtournament on $m$ vertices.

Reid and Parker proved $f(n) \ge \lfloor \log_2 n + 4 - \log_2 7 \rfloor$ for all $n \ge 14$; at
$n = 14$ this gives $f(14) \ge 5 > 4 = \lfloor \log_2 14 \rfloor + 1$, while Stearns' bound
$f(n) \ge \lfloor \log_2 n \rfloor + 1$ holds for every $n \ge 1$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1216, https://www.erdosproblems.com/1216 (status DISPROVED); resolution: K. B. Reid and E. T. Parker, Disproof of a conjecture of Erdős and Moser on tournaments, J. Combinatorial Theory 9 (1970), 225-238, erdosproblems.com/1216: f(n) ≥ ⌊log₂ n + 4 - log₂ 7⌋ for all n ≥ 14, so f(14) ≥ 5 > ⌊log₂ 14⌋ + 1.

Stated but not proved: `MathlibExt.Combinatorics.TransitiveSubtournamentLogErdosProblem1216Wanted.transitiveSubtournamentNumberEqLogTwo_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TransitiveSubtournamentLogErdosProblem1216Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#transitive-subtournament-number-eq-log-t-2).

## The backward arcs of $T^*$

**The backward arcs of $T^*$.** The list of ordered pairs $(5, 0)$, $(5, 2)$, $(4, 1)$,
$(3, 0)$ of vertices in $\{0, \dots, 5\}$. These are the arcs of the six-vertex tournament $T^*$
that go from a larger to a smaller vertex: $6 \to 1$, $6 \to 3$, $5 \to 2$ and $4 \to 1$ in the
source's labelling $1, \dots, 6$, with every vertex lowered by one.

Formalized by `MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStarBackArcs`, a definition declared in [WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#t-star-back-arcs).

## The six-vertex tournament $T^*$

**The six-vertex tournament $T^*$.** The tournament $T^*$ is the relation on the vertex set
$\{0, \dots, 5\}$ with an arc $i \to j$ if and only if either $(i, j)$ is one of the backward
arcs $(5, 0)$, $(5, 2)$, $(4, 1)$, $(3, 0)$, or $i < j$ and $(j, i)$ is not a backward arc.

Formalized by `MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStar`, a definition declared in [WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#t-star).

## Containing $T^*$ as a subtournament

**Containing $T^*$ as a subtournament.** A relation $T$ on the vertex set
$\{0, \dots, n-1\}$ contains $T^*$ when there is an injective map $f$ from the vertex set
$\{0, \dots, 5\}$ of $T^*$ to $\{0, \dots, n-1\}$ such that for all vertices $i, j$ of $T^*$,
$i \to j$ in $T^*$ if and only if $T(f(i), f(j))$ holds.

Formalized by `MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.ContainsTStar`, a definition declared in [WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#contains-tstar).

## The Erdős–Hajnal problem for the tournament $T^*$

**The Erdős–Hajnal problem for the tournament $T^*$.** There is a real number
$\varepsilon > 0$ such that for every natural number $n$ and every tournament $T$ on the vertex
set $\{0, \dots, n-1\}$ that does not contain $T^*$ as a subtournament, there is a set $S$ of
vertices on which $T$ is transitive with $|S| \ge n^{\varepsilon}$.

This is Problem 1.12 of the AimPL problem list on graph Ramsey theory.

Formalized by `MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStarErdosHajnal`, a definition declared in [WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#t-star-erdos-hajnal).

## Nguyen–Scott–Seymour: $T^*$ has the Erdős–Hajnal property

**Nguyen–Scott–Seymour: $T^*$ has the Erdős–Hajnal property.** There is a real number
$\varepsilon > 0$ such that for every natural number $n$ and every tournament $T$ on the vertex
set $\{0, \dots, n-1\}$ that does not contain $T^*$ as a subtournament, there is a set $S$ of
vertices on which $T$ is transitive with $|S| \ge n^{\varepsilon}$.

Resolved true: Nguyen, Scott and Seymour prove that every two-colourable tournament has the
Erdős–Hajnal property, "which completes the verification of the conjecture for six-vertex
tournaments"; Berger, Choromanski and Chudnovsky had proved it for every tournament on at most six
vertices except `T*` (the remark recorded with the problem), and `T*` is two-colourable (`{1, 2, 3}`
and `{4, 5, 6}` are transitive).

## Sources

- AimPL: Graph Ramsey Theory, Problem 1.12 [Maria Chudnovsky], http://aimpl.org/graphramsey/1/; resolution: T. Nguyen, A. Scott and P. Seymour, Induced subgraph density. VI. Bounded VC-dimension, Adv. Math. 482 (2025), 110601, arXiv:2312.15572, abstract and introduction, https://arxiv.org/abs/2312.15572.

Stated but not proved: `MathlibExt.Combinatorics.TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.tStarErdosHajnal_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TournamentErdosHajnalSixVertexAIMCombinatoricsProblem55Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html#t-star-erdos-hajnal-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transitive subtournaments](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/transitive-subtournaments/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/directed-graphs/transitive-subtournaments)
