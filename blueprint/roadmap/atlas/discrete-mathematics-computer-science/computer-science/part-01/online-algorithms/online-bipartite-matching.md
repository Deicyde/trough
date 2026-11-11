---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Online.BipartiteMatching.step, Cslib.Algorithms.Lean.Online.BipartiteMatching.greedy, Cslib.Algorithms.Lean.Online.BipartiteMatching.step_extends, Cslib.Algorithms.Lean.Online.BipartiteMatching.Done, Cslib.Algorithms.Lean.Online.BipartiteMatching.greedy_spec, Cslib.Algorithms.Lean.Online.BipartiteMatching.toFun, Cslib.Algorithms.Lean.Online.BipartiteMatching.stepArr, Cslib.Algorithms.Lean.Online.BipartiteMatching.greedyArr
statement: formalized
proof: formalized
---

# Online bipartite matching

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html).

## Greedy step of online bipartite matching

Consider a bipartite graph with left vertices
$0, \dots, a-1$ and right vertices $0, \dots, b-1$, and an assignment $m$ giving each right
vertex either a left partner or none. On the arrival of a right vertex $j$, the greedy step
returns the assignment that agrees with $m$ at every right vertex other than $j$, and gives $j$
the smallest left neighbour of $j$ that is free in $m$ (the partner of no right vertex), or no
partner if $j$ has no free neighbour.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.step`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#step).

## Greedy online bipartite matching

Consider a bipartite graph with left vertices
$0, \dots, a-1$ and right vertices $0, \dots, b-1$, an assignment $m$ giving each right vertex
either a left partner or none, and a list $j_1, \dots, j_n$ of right vertices, the arrivals in
order. The greedy matching from $m$ on these arrivals is the assignment obtained from $m$ by
applying the greedy step of online bipartite matching for the arrival of $j_1$, then of $j_2$,
and so on up to $j_n$; if the list is empty, it is $m$.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.greedy`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#greedy).

## Earlier partners survive an arrival

Let $m$ be an assignment giving each right vertex of
a bipartite graph either a left partner or none, and let $j$ be a right vertex with no partner
in $m$. If a right vertex $j'$ has partner $i$ in $m$, then $j'$ still has partner $i$ after
the greedy step for the arrival of $j$.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.step_extends`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#step-extends).

## Done right vertices

Given a partner array, which assigns to each right vertex its partner
on the left if it has one, the right vertices of a list $S$ are done when, for every right vertex
$j$ of $S$ and every left vertex $i$ adjacent to $j$, $j$ is matched or $i$ is matched.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.Done`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#done).

## Invariants of the greedy run

Let $L$ be a list of distinct right vertices, all unmatched
in a valid partner array $m$, and let $S$ be a list of right vertices that are done for $m$. Then
the partner array obtained from $m$ by the greedy run along $L$ is valid, and every right vertex
of $L$ or of $S$ is done for it.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.greedy_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#greedy-spec).

## Partner assignment from an array

An array $A$ whose entries are each a left vertex or
none is read as an assignment of partners to the right vertices $0, \dots, b-1$: right vertex
$j$ gets the entry of $A$ at index $j$ when $j$ is less than the length of $A$, and no partner
otherwise.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.toFun`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#to-fun).

## Greedy step on an array

In a bipartite graph with left vertices $0, \dots, a - 1$ and right
vertices $0, \dots, b - 1$, take an array whose entry $k$ holds the partner of the right vertex $k$,
a missing entry meaning no partner. On the arrival of a right vertex $j$, entry $j$ is set to the
first left neighbour of $j$, in the order $0, \dots, a - 1$, that is free, that is, the partner of
none of the right vertices $0, \dots, b - 1$ in the array, or to none if no neighbour of $j$ is
free; if the array has no entry $j$, it is unchanged.

Storing the partners in an array computes each choice once per arrival; evaluating the composed
function updates of the specification directly would recompute every earlier choice at each
lookup, a cost exponential in the number of right vertices.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.stepArr`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#step-arr).

## Greedy run on an array

In a bipartite graph with left vertices $0, \dots, a - 1$ and right
vertices $0, \dots, b - 1$, start from an array whose entry $k$ holds the partner of the right
vertex $k$, a missing entry meaning no partner, and let the right vertices of a list $L$ arrive one
after another in the order of $L$. Each arrival performs the greedy step on the array: the entry of
the arriving vertex $j$ is set to the first left neighbour of $j$, in the order $0, \dots, a - 1$,
that is free, that is, the partner of none of the right vertices $0, \dots, b - 1$ in the current
array, or to none if no neighbour of $j$ is free; if the array has no entry $j$, it is unchanged.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.greedyArr`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#greedy-arr).

## The greedy online matching

In a bipartite graph with left vertices $0, \dots, a - 1$ and
right vertices $0, \dots, b - 1$, the greedy online matching is the partner array obtained by
starting from the empty matching and letting the right vertices arrive in the order
$0, 1, \dots, b - 1$, each arriving vertex being matched to its first free left neighbour in the
order $0, \dots, a - 1$, or left unmatched if no neighbour is free.

It is computed on arrays, with one array write per arrival.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.greedyAll`, a definition declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#greedy-all).

## The greedy matching is maximal

Every edge has a matched endpoint.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.greedyAll_maximal`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#greedy-all-maximal).

## Greedy online matching is `1/2`-competitive

Every matching has at most twice as many
edges as the greedy one. An edge of the matching whose right vertex the greedy algorithm matched
is charged to that right vertex, any other edge to its left vertex, which the greedy algorithm
matched by maximality; a matching charges each greedy edge at most once on each side.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.card_le_two_mul_greedyAll`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#card-le-two-mul-greedy-all).

## The greedy online matching is a matching

The set of pairs $(i, j)$ such that the greedy
online matching assigns the left vertex $i$ to the right vertex $j$ is a matching of the bipartite
graph.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.isMatching_greedyAll`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#is-matching-greedy-all).

## Greedy online matching is within a factor $2$ of the maximum

In a bipartite graph, the
maximum matching computed by augmenting paths has at most twice as many edges as the greedy online
matching, in which the right vertices arrive in increasing order.

Formalized by `Cslib.Algorithms.Lean.Online.BipartiteMatching.card_maxMatching_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/BipartiteMatching.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#card-max-matching-le).

## Deterministic online bipartite matching algorithm

A deterministic online bipartite
matching algorithm with $a$ offline (left) vertices $0, \dots, a - 1$ is given by a proposal
rule: on each arrival it receives the neighbour lists (lists of left vertices) of all earlier
arrivals, in order, and the neighbour list of the current arrival, and proposes a left vertex to
match the arrival to, or none.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.OnlineMatcher`, a structure declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#online-matcher).

## Number of arrivals an online matcher matches

Let $A$ be an online matcher with $a$ left
vertices, $h$ a history (the neighbour lists of earlier arrivals), $U$ a list of left vertices
already matched, and $\sigma$ a sequence of arrivals, each given by its list of left neighbours.
The run of $A$ on $\sigma$ takes the arrivals in order: on an arrival with neighbour list $N$,
$A$ proposes a left vertex, or none, from the current history and $N$; a proposal $i$ with
$i \in N$ and $i \notin U$ is accepted, counting the arrival as matched and adding $i$ to $U$,
and otherwise the arrival stays unmatched; then $N$ is appended to the history. The value is the
number of arrivals matched.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.matched`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#matched).

## Perfect matchings of a sequence of arrivals

A list $m$ of left vertices is a perfect
matching of a sequence $\sigma$ of arrivals (neighbour lists) when $m$ and $\sigma$ have the same
length, the entries of $m$ are pairwise distinct, and for each $j$ the $j$-th entry of $m$ lies
in the $j$-th neighbour list of $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.IsPerfect`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#is-perfect).

## Graph of a sequence of arrivals

For a sequence $\sigma = (\sigma_0, \dots, \sigma_{k-1})$
of arrivals, each a list of left vertices in $\{0, \dots, a - 1\}$, the bipartite graph of $\sigma$
is given by adjacency lists: left vertex $i$ is sent to the list, in increasing order, of the
arrivals $j < k$ with $i \in \sigma_j$.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.toAdj`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#to-adj).

## Perfect matchings of the arrivals are matchings of their graph

Let $\sigma$ be a sequence
of arrivals (neighbour lists) and $m$ a perfect matching of $\sigma$. Then the bipartite graph of
$\sigma$, in which left vertex $i$ is adjacent to arrival $j$ when $i$ lies in the $j$-th
neighbour list, has a matching with as many edges as $\sigma$ has arrivals.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.exists_isMatching_of_isPerfect`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#exists-is-matching-of-is-perfect).

## The adversary for online bipartite matching

Let $A$ be an online matcher, $h$ a list of
earlier neighbour lists and $ps$ a list of gadgets, pairs $(u, v)$ of left vertices. The
adversary's sequence of arrivals is empty when $ps$ is empty. Otherwise, for the first gadget
$(u, v)$, let $x = v$ if $A$, after the history $h$, proposes $v$ for an arrival with neighbour
list $[u, v]$, and $x = u$ otherwise (a proposal of $u$, of no vertex, or of a non-neighbour).
The sequence is an arrival with neighbour list $[u, v]$, then an arrival with neighbour list
$[x]$, then the adversary's sequence for $A$, the history $h$ extended by $[u, v]$ and $[x]$, and
the remaining gadgets.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.adversary`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#adversary).

## The adversary's offline matching

Let $A$ be an online matcher, $h$ a list of earlier
neighbour lists and $ps$ a list of gadgets, pairs $(u, v)$ of left vertices. The list
$\mathrm{opt}(A, h, ps)$ of left vertices is empty when $ps$ is empty. Otherwise, for the first
gadget $(u, v)$, let $x = v$ if $A$, after the history $h$, proposes $v$ for an arrival with
neighbour list $[u, v]$, and $x = u$ otherwise; the list starts with $u, v$ in the first case and
with $v, u$ in the second, and continues with $\mathrm{opt}(A, h', ps')$, where $h'$ is $h$
extended by the neighbour lists $[u, v]$ and $[x]$ and $ps'$ is the list of remaining gadgets.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.adversaryOpt`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#adversary-opt).

## Gadgets with distinct vertices

A list of gadgets, pairs $(u, v)$ of left vertices, has
distinct vertices when $u \ne v$ for every gadget $(u, v)$ of the list, and any two gadgets
$(u, v)$ and $(u', v')$ at different positions of the list share no vertex:
$u \ne u'$, $u \ne v'$, $v \ne u'$ and $v \ne v'$.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.GadgetsDisjoint`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#gadgets-disjoint).

## The adversary holds every algorithm to one match per gadget

For every online matcher
$A$, every list $h$ of earlier neighbour lists, every list $U$ of left vertices and every list of
$k$ gadgets, the run of $A$ on the adversary's arrivals for $A$, $h$ and the gadgets, after the
history $h$ and with the left vertices of $U$ already matched, matches at most $k$ arrivals.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.matched_adversary_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#matched-adversary-le).

## The adversary's arrivals have a perfect matching

For every online matcher $A$, every
list $h$ of earlier neighbour lists and every list of gadgets with distinct vertices, the
adversary's offline matching for $A$, $h$ and the gadgets is a perfect matching of the
adversary's arrivals for $A$, $h$ and the gadgets. In each gadget, the first arrival takes the
vertex the second one does not.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.isPerfect_adversaryOpt`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#is-perfect-adversary-opt).

## The $n$ gadgets on $2n$ left vertices

For $n \in \mathbb{N}$, the list of gadgets
$(0, 1), (2, 3), \dots, (2n - 2, 2n - 1)$ of left vertices in $\{0, \dots, 2n - 1\}$, that is, the
pairs $(2k, 2k + 1)$ for $k = 0, \dots, n - 1$ in increasing order of $k$.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.gadgets`, a definition declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#gadgets).

## No deterministic online bipartite matching algorithm beats `1/2`

**No deterministic online bipartite matching algorithm beats `1/2`** (Karp, Vazirani and
Vazirani): against every algorithm with `2 n` left vertices, some sequence of `2 n` arrivals has
a perfect matching while the algorithm matches at most `n` of them.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.exists_perfect_matched_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#exists-perfect-matched-le).

## The $1/2$ lower bound with a matching of the arrivals' graph

For every $n \in \mathbb{N}$
and every online matcher $A$ with $2n$ left vertices, there is a sequence $\sigma$ of arrivals
(neighbour lists) such that the bipartite graph of $\sigma$, in which left vertex $i$ is adjacent
to arrival $j$ when $i$ lies in the $j$-th neighbour list, has a matching with $2n$ edges, while
$A$, run on $\sigma$ from the empty history with no left vertex matched, matches at most $n$
arrivals.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.exists_isMatching_matched_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#exists-is-matching-matched-le).

## Finite-size lower bound for deterministic online matching

Let $n$, $b$, $c$, $d$ be
natural numbers with $d < 2c$ and $b < n$. For every online matcher $A$ with $2n$ left vertices
there are a sequence $\sigma$ of arrivals and a perfect matching $m$ of $\sigma$ such that
$d \cdot \mathrm{ALG} + b < c \cdot |m|$, where $\mathrm{ALG}$ is the number of arrivals of
$\sigma$ that $A$ matches when run from the empty history with no left vertex matched, and $|m|$
is the length of $m$.

At a fixed size some additive constant always suffices, which is why $b$ is bounded by $n$;
letting the size grow removes the bound.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.not_competitive_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#not-competitive-of-lt).

## No deterministic online matcher beats ratio $1/2$, with any additive constant

Let
$(A_n)_{n \in \mathbb{N}}$ be a family of online matchers, $A_n$ having $2n$ left vertices, and
let $b$, $c$, $d$ be natural numbers with $d < 2c$. Then for some $n$ there are a sequence
$\sigma$ of arrivals on the left vertices of $A_n$ and a perfect matching $m$ of $\sigma$ such
that $d \cdot \mathrm{ALG} + b < c \cdot |m|$, where $\mathrm{ALG}$ is the number of arrivals of
$\sigma$ that $A_n$ matches when run from the empty history with no left vertex matched, and
$|m|$ is the length of $m$.

For $d > 0$ this says that the family is not $c/d$-competitive, whatever the additive constant.

Formalized by `Cslib.Algorithms.Lean.Online.MatchingLowerBound.not_competitive`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Online/MatchingLowerBound.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html#not-competitive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Online bipartite matching](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/online-bipartite-matching/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/online-algorithms/online-bipartite-matching)
