---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Karger.State, Cslib.Algorithms.Lean.Karger.State.Valid, Cslib.Algorithms.Lean.Karger.cutSize, Cslib.Algorithms.Lean.Karger.IsCut, Cslib.Algorithms.Lean.Karger.IsMinCut, Cslib.Algorithms.Lean.Karger.rename, Cslib.Algorithms.Lean.Karger.contract, Cslib.Algorithms.Lean.Karger.successProb
statement: formalized
proof: formalized
---

# Karger's algorithm

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html).

## Multigraph state of Karger's algorithm

A state over a vertex type $V$ consists of a
list of current (super-)vertices in $V$ and a list of edges, each an ordered pair of elements
of $V$; repeated pairs are parallel edges.

Formalized by `Cslib.Algorithms.Lean.Karger.State`, a structure declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#state).

## Valid multigraph

A multigraph, given by a list of vertices and a list of edges (pairs of
vertices, with multiplicity), is valid when its vertex list has no repeated entries and every
edge joins two distinct vertices of the list.

Formalized by `Cslib.Algorithms.Lean.Karger.State.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#valid).

## Size of a cut

For a list of edges (pairs of vertices, repeated pairs counted with
multiplicity) and a map $X$ from vertices to booleans, the size of the cut $X$ is the number of
edges $(u, v)$ in the list with $X(u) \ne X(v)$.

Formalized by `Cslib.Algorithms.Lean.Karger.cutSize`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#cut-size).

## Cuts of a multigraph

A map $X$ from vertices to booleans is a cut of a multigraph state
$G$ when some vertex $v$ of $G$ has $X(v) = \mathrm{true}$ and some vertex $w$ of $G$ has
$X(w) = \mathrm{false}$.

Formalized by `Cslib.Algorithms.Lean.Karger.IsCut`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#is-cut).

## Minimum cut size

A natural number $k$ is the minimum cut size of a multigraph state $G$
when some cut of $G$ has size $k$ and every cut of $G$ has size at least $k$.

Formalized by `Cslib.Algorithms.Lean.Karger.IsMinCut`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#is-min-cut).

## Renaming a vertex

For vertices $a$ and $b$, renaming $b$ to $a$ is the map on vertices
that sends $b$ to $a$ and fixes every other vertex.

Formalized by `Cslib.Algorithms.Lean.Karger.rename`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#rename).

## Edge contraction

For a multigraph state $G$ and a pair of vertices $e = (a, b)$, the
contraction of $G$ along $e$ deletes the first occurrence of $b$ from the vertex list, replaces
$b$ by $a$ in both endpoints of every edge, and then deletes every edge whose two endpoints are
equal.

Formalized by `Cslib.Algorithms.Lean.Karger.contract`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#contract).

## Success probability of the contraction process

For a natural number $k$, a number $f$
of allowed contractions and a multigraph $G$ with edge list $E_G$, the probability $P_k(f, G)$
that the contraction process on $G$ returns $k$ is defined by recursion on $f$. If $f = 0$, or
$G$ has at most two vertices, or $G$ has no edges, then $P_k(f, G)$ is $1$ when $G$ has exactly
$k$ edges and $0$ otherwise. Otherwise
$P_k(f, G) = \frac{1}{|E_G|} \sum_{e \in E_G} P_k(f - 1, G/e)$, where $G/e$ is the contraction of
$G$ along $e$ and the sum runs over the edges with multiplicity.

This models contracting a uniformly random edge while more than two vertices remain and counting
the edges between the last two vertices.

Formalized by `Cslib.Algorithms.Lean.Karger.successProb`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#success-prob).

## Cut sizes under contraction

Let $G$ be a multigraph state, $e = (a, b)$ a pair of
vertices and $Y$ a map from vertices to booleans, and let $\rho$ send $b$ to $a$ and fix every
other vertex. The size of the cut $Y$ in the contraction of $G$ along $e$ equals the size of the
cut $Y \circ \rho$ in $G$.

Formalized by `Cslib.Algorithms.Lean.Karger.cutSize_contract`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#cut-size-contract).

## Contraction preserves the minimum cut size

Let $G$ be a valid multigraph state with
minimum cut size $k$, and let $X$ be a cut of $G$ of size $k$. If $e = (a, b)$ is an edge of $G$
with $X(a) = X(b)$, then the contraction of $G$ along $e$ also has minimum cut size $k$.

Formalized by `Cslib.Algorithms.Lean.Karger.isMinCut_contract`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#is-min-cut-contract).

## Contraction preserves validity and removes one vertex

If a multigraph $G$ is valid and
$e$ is one of its edges, then the contraction of $G$ along $e$ is valid and has exactly one
vertex fewer than $G$.

Formalized by `Cslib.Algorithms.Lean.Karger.valid_contract`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#valid-contract).

## Handshake lemma

For a valid multigraph $G$, the sum over the vertices $v$ of $G$ of the
number of edges crossing the singleton cut $\{v\}$ equals twice the number of edges of $G$.

Formalized by `Cslib.Algorithms.Lean.Karger.sum_degree`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#sum-degree).

## Minimum cut size bounds the number of edges

Let $G$ be a valid multigraph state with
$n \ge 2$ vertices, $m$ edges (counted with multiplicity) and minimum cut size $k$. Then
$n k \le 2m$: every vertex has degree at least $k$, since its singleton is a cut.

Formalized by `Cslib.Algorithms.Lean.Karger.card_mul_le_two_mul_edges`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#card-mul-le-two-mul-edges).

## The success probability is nonnegative

For every natural number $k$, every number $f$
of allowed contractions and every multigraph state $G$, the probability $P_k(f, G)$ that the
contraction process on $G$ returns $k$ satisfies $0 \le P_k(f, G)$.

Formalized by `Cslib.Algorithms.Lean.Karger.successProb_nonneg`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#success-prob-nonneg).

## The success probability is at most one

For every natural number $k$, every number of
allowed contractions and every multigraph $G$, the probability that the contraction process on
$G$ returns $k$ is at most $1$.

Formalized by `Cslib.Algorithms.Lean.Karger.successProb_le_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#success-prob-le-one).

## Karger's bound

Let $G$ be a valid multigraph with $n \ge 2$ vertices and minimum cut
size $k$. Then the contraction process on $G$, with $n$ contractions allowed, returns $k$ with
probability at least $2 / (n(n-1))$.

Formalized by `Cslib.Algorithms.Lean.Karger.successProb_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#success-prob-ge).

## Success probability of repeated runs

For a multigraph $G$ with $n$ vertices and
natural numbers $k$ and $t$, let $p$ be the probability that one run of the contraction process
on $G$, with $n$ contractions allowed, returns $k$. The repeated success probability is
$1 - (1 - p)^t$, the probability that at least one of $t$ independent runs returns $k$.

Formalized by `Cslib.Algorithms.Lean.Karger.repeatSuccessProb`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#repeat-success-prob).

## Repeating Karger's algorithm succeeds with probability at least one half

Let $G$ be a
valid multigraph state with $n \ge 2$ vertices and minimum cut size $k$, and let $t$ be a natural
number with $n(n-1) \le 2t$. Then the probability that at least one of $t$ independent runs of
the contraction process returns $k$ is at least $1/2$.

Formalized by `Cslib.Algorithms.Lean.Karger.repeatSuccessProb_ge_half`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#repeat-success-prob-ge-half).

## Amplification with high probability

Let $G$ be a valid multigraph with $n \ge 2$
vertices and minimum cut size $k$, and let $c$ and $t$ be natural numbers with
$c \cdot n(n-1) \le 2t$. Then the probability that at least one of $t$ independent runs of the
contraction process on $G$ returns $k$ is at least $1 - (1/2)^c$.

Formalized by `Cslib.Algorithms.Lean.Karger.repeatSuccessProb_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#repeat-success-prob-ge).

## Karger's algorithm succeeds with high probability

Let $G$ be a valid multigraph with
$n \ge 2$ vertices and minimum cut size $k$, and let $t$ be a natural number with
$\lceil \log_2 n \rceil \cdot n(n-1) \le 2t$. Then the probability that at least one of $t$
independent runs of the contraction process on $G$ returns $k$ is at least $1 - 1/n$.

Thus $O(n^2 \log n)$ runs find the minimum cut size with high probability.

Formalized by `Cslib.Algorithms.Lean.Karger.repeatSuccessProb_ge_one_sub_inv`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#repeat-success-prob-ge-one-sub-inv).

## Probability that a run outputs a given cut

For a map $X$ from vertices to booleans, a
fuel bound $f$ and a multigraph $G$, this is the probability that the contraction process on $G$
(contract an edge chosen uniformly at random, counted with multiplicity, while more than two
vertices and at least one edge remain, making at most $f$ contractions) never contracts an edge
whose endpoints $X$ separates and ends with exactly two vertices on which $X$ takes both values.

Explicitly: if $f = 0$, or $G$ has at most two vertices, or $G$ has no edges, the value is $1$
when $G$ has exactly two vertices and $X$ is a cut of $G$, and $0$ otherwise. Otherwise it is the
average over the edges $e$ of $G$, counted with multiplicity, of the value for fuel $f - 1$ on
the contraction of $G$ along $e$ when $X$ agrees on the two endpoints of $e$, and of $0$ when it
does not.

Formalized by `Cslib.Algorithms.Lean.Karger.surviveProb`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#survive-prob).

## Cuts distinct as partitions

Two maps $X, Y$ from vertices to booleans are distinct on a
list of vertices $S$ when some $v \in S$ has $X(v) \ne Y(v)$ and some $w \in S$ has
$X(w) = Y(w)$; so on $S$ neither cut is the other or its complement.

Formalized by `Cslib.Algorithms.Lean.Karger.DistinctOn`, a definition declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#distinct-on).

## Each minimum cut survives with probability at least $2/(n(n-1))$

Let $G$ be a valid
multigraph with $n \ge 2$ vertices whose minimum cut size $k$ is at least $1$, and let $X$ be a
cut of $G$ with exactly $k$ crossing edges. Then the probability that the contraction process on
$G$, allowed up to $n$ contractions, outputs the cut $X$ is at least $2/(n(n-1))$.

Formalized by `Cslib.Algorithms.Lean.Karger.surviveProb_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#survive-prob-ge).

## Survival probabilities of distinct cuts sum to at most one

Let $G$ be a valid multigraph
with vertex list $S$, let $f$ be a number of allowed contractions, and let $X_1, \dots, X_m$ be
Boolean functions on the vertex type that are pairwise distinct as partitions of $S$. Then the
probabilities that the contraction process on $G$, with $f$ contractions allowed, outputs
$X_1, \dots, X_m$ add up to at most $1$.

The survival events are disjoint: a run outputs at most one partition.

Formalized by `Cslib.Algorithms.Lean.Karger.sum_surviveProb_le_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#sum-survive-prob-le-one).

## At most $n(n-1)/2$ minimum cuts

**At most $n(n-1)/2$ minimum cuts** (Karger; Kleinberg and Tardos, Section 13.2). Let $G$ be a
valid multigraph with $n \ge 2$ vertices whose minimum cut size $k$ is at least $1$. If
$X_1, \dots, X_m$ are cuts of $G$, each with exactly $k$ crossing edges, that are pairwise
distinct as partitions of the vertices of $G$, then $2m \le n(n-1)$, that is, $m \le n(n-1)/2$.

Each of these cuts is output by a run of the contraction process with probability at least
$2/(n(n-1))$, and the runs that output distinct partitions are disjoint.

Formalized by `Cslib.Algorithms.Lean.Karger.two_mul_length_minCuts_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean, line 735](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/KargerMinCut.lean#L735). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html#two-mul-length-min-cuts-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Karger's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/randomized-algorithms/karger-s-algorithm)
