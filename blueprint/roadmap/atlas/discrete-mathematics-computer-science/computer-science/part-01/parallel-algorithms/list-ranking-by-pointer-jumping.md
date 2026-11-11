---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Parallel.ListRanking.jump, Cslib.Algorithms.Lean.Parallel.ListRanking.Terminates, Cslib.Algorithms.Lean.Parallel.ListRanking.rank, Cslib.Algorithms.Lean.Parallel.ListRanking.jump_eq_none_iff, Cslib.Algorithms.Lean.Parallel.ListRanking.rank_of_jump, Cslib.Algorithms.Lean.Parallel.ListRanking.State, Cslib.Algorithms.Lean.Parallel.ListRanking.init, Cslib.Algorithms.Lean.Parallel.ListRanking.round
statement: formalized
proof: formalized
---

# List ranking by pointer jumping

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html).

## Iterated successor

For a successor map $\mathrm{succ}$ on the nodes $0, \dots, n-1$, where
$\mathrm{succ}(v)$ is either a node or undefined, the $k$-step jump from $v$ is the node reached by
applying $\mathrm{succ}$ $k$ times starting at $v$, and is undefined if some step is undefined: the
$0$-step jump from $v$ is $v$, and the $(k+1)$-step jump is $\mathrm{succ}$ of the $k$-step jump.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.jump`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#jump).

## Terminating successor functions

A successor function $\mathrm{succ}$ on the nodes
$0, \dots, n - 1$, mapping each node to its successor or to nothing, terminates when from every
node $v$ the walk of $n$ steps along $\mathrm{succ}$ runs off the end, that is, there is no node
$n$ steps down the list from $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.Terminates`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#terminates).

## Rank of a node in a linked list

Let $\mathrm{succ}$ be a successor map on the nodes
$0, \dots, n-1$ whose lists terminate. The rank of a node $v$ is the least $k$ such that following
$\mathrm{succ}$ for $k + 1$ steps from $v$ runs off the end of the list, that is, the number of
nodes after $v$ in its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.rank`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rank).

## The characteristic property of the rank

Let $\mathrm{succ}$ be a successor map on the
nodes $0, \dots, n-1$ whose lists terminate. For every node $v$ and every $k \in \mathbb{N}$,
following $\mathrm{succ}$ for $k$ steps from $v$ runs off the end of the list if and only if
$k > \operatorname{rank}(v)$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.jump_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#jump-eq-none-iff).

## Rank decreases along jumps

Let $\mathrm{succ}$ be a successor map on the nodes
$0, \dots, n-1$ whose lists terminate. If following $\mathrm{succ}$ for $a$ steps from a node $v$
reaches the node $u$, then $a \le \operatorname{rank}(v)$ and
$\operatorname{rank}(u) = \operatorname{rank}(v) - a$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.rank_of_jump`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rank-of-jump).

## Pointer-jumping state for list ranking

A pointer-jumping state on the nodes
$0, \dots, n - 1$ assigns to each node a pointer, which is either a node or empty (once it points
past the end of the list), and a distance in $\mathbb{N}$, the distance covered by the pointer.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.State`, a structure declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#state-2).

## Initial state of pointer jumping

For a successor map $\mathrm{succ}$ on the nodes
$0, \dots, n-1$, where $\mathrm{succ}(v)$ is either a node or undefined (at the end of a list), the
initial pointer-jumping state gives each node $v$ the pointer $\mathrm{succ}(v)$ and the distance
$0$ if $\mathrm{succ}(v)$ is undefined and $1$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.init`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#init-2).

## One round of pointer jumping

In one parallel round, every node $v$ whose pointer is a node
$u$ adds the distance of $u$ to its own distance and moves its pointer to the pointer of $u$
(undefined if that of $u$ is); a node whose pointer is undefined keeps its distance and its
undefined pointer.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.round`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#round-2).

## The list-ranking state after $t$ rounds

For a successor function $\mathrm{succ}$ on the
nodes $0, \dots, n - 1$, the pointer-jumping state after $t$ rounds is defined by recursion on
$t$: after $0$ rounds it is the initial state of $\mathrm{succ}$, and after $t + 1$ rounds it is
one round of pointer jumping applied to the state after $t$ rounds.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.rounds`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-2).

## The invariant of pointer jumping for list ranking

Let $\mathrm{succ}$ map each of the
nodes $0, \dots, n - 1$ to its successor or to nothing, and suppose the lists terminate: from
every node, $n$ steps run off the end. Write $\mathrm{rank}(v)$ for the number of nodes after
$v$. Then for every $t \ge 0$ and every node $v$, after $t$ rounds of pointer jumping, the
pointer of $v$ is the node $2^t$ steps down the list from $v$ (no node if the list ends before
that), and the distance of $v$ is $\min(2^t, \mathrm{rank}(v))$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.rounds_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-spec-2).

## After enough rounds, the distances are the ranks

Let $\mathrm{succ}$ be a successor map
on the nodes $0, \dots, n-1$ whose lists terminate, and let $t$ be a natural number with
$n \le 2^t$. Then after $t$ rounds of pointer jumping from the initial state, the distance of
every node $v$ is the rank of $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.rounds_dist`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-dist).

## Tabulating a list-ranking state

The tabulation of a pointer-jumping state $s$ on the
nodes $0, \dots, n - 1$ is the pair of arrays of length $n$ whose entries at $v$ are the pointer
and the distance of $v$ in $s$.

Evaluating the state after $t$ rounds directly re-reads earlier rounds' pointers at every query,
a cost growing exponentially with the number of rounds; the tabulated rounds cost $O(n)$ array
operations each.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.tabulate`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#tabulate-2).

## One pointer-jumping round on arrays

Given an array $P$ of pointers (each a node among
$0, \dots, n-1$ or undefined) and an array $D$ of natural-number distances, one round returns
arrays $P'$ and $D'$ of length $n$ where, for each node $v$, $P'[v]$ is $P[u]$ if $P[v] = u$ and is
undefined if $P[v]$ is undefined, and $D'[v] = D[v] + D[u]$ if $P[v] = u$ and $D'[v] = D[v]$ if
$P[v]$ is undefined. Entries missing from the input arrays are read as undefined pointers and
distance $0$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.roundTab`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#round-tab-2).

## List-ranking rounds on arrays

For a successor function $\mathrm{succ}$ on the nodes
$0, \dots, n - 1$ and $t \ge 0$, the arrays after $t$ rounds are a pair of arrays (pointers and
distances) defined by recursion on $t$: after $0$ rounds they are the tabulation of the initial
state of $\mathrm{succ}$, and after $t + 1$ rounds they are one round on arrays applied to the
arrays after $t$ rounds.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.roundsTab`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-tab-2).

## List ranking by pointer jumping

For a successor map $\mathrm{succ}$ on the nodes
$0, \dots, n-1$, list ranking by pointer jumping runs $\lceil \log_2 n \rceil$ rounds of pointer
jumping on arrays, starting from the initial state, and returns the resulting array of distances,
whose entry $v$ is the distance of node $v$.

When the lists terminate, entry $v$ is the rank of node $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.listRanks`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#list-ranks).

## Pointer jumping ranks every list in ⌈log₂ n⌉ rounds

Let $\mathrm{succ}$ be a successor map
on the nodes $0, \dots, n-1$ whose lists terminate. Then for every node $v$, entry $v$ of the table
returned by list ranking by pointer jumping, which runs $\lceil \log_2 n \rceil$ rounds, is the
rank of $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListRanking.listRanks_getD`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListRanking.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#list-ranks-get-d).

## The value $k$ steps ahead

Let $n$ nodes be linked into lists by a partial successor
function, each node $u$ carrying a value $x_u$ in an additive monoid $M$. For $k \in \mathbb{N}$
and a node $v$, this is $x_u$ where $u$ is the node $k$ steps after $v$ along its list, and $0$
if the list ends before $k$ steps.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.stepVal`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#step-val).

## Segment sums

Let $n$ nodes be linked into lists by a partial successor function, and
let each node $v$ carry a value $x_v$ in an additive monoid $M$ (not necessarily commutative).
For $k \in \mathbb{N}$ and a node $v$, the segment sum of length $k$ from $v$ is the sum, in
list order, of the values of the first $k$ nodes of the list starting at $v$ (fewer if the list
ends sooner); for $k = 0$ it is $0$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.segSum`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#seg-sum).

## Segment sums add up

Let $\mathrm{succ}$ be a partial successor function on nodes
$0, \dots, n-1$ and $x_v$ values in an additive monoid $M$. For $k \in \mathbb{N}$ write
$S_k(v)$ for the sum, in list order, of the values of the nodes reached from $v$ in
$0, 1, \dots, k - 1$ steps along $\mathrm{succ}$ (a missing node contributes $0$). Then for all
$a, b \in \mathbb{N}$ and every node $v$, $S_{a+b}(v) = S_a(v) + S_b(u)$ if the node $u$ reached
from $v$ in $a$ steps exists, and $S_{a+b}(v) = S_a(v)$ otherwise.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.segSum_add`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#seg-sum-add).

## Suffix sums

Let $n$ nodes be linked into lists by a partial successor function, each
node $v$ carrying a value $x_v$ in an additive monoid $M$. The suffix sum of a node $v$ is the
segment sum of length $n$ from $v$: the sum, in list order, of the values of the first $n$ nodes
of the list starting at $v$ (fewer if it ends sooner).

When the list from $v$ ends, it has at most $n$ nodes, so this is the sum of the values from $v$
to the end of its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.suffixSum`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#suffix-sum).

## The characteristic property of suffix sums

Let $n$ nodes be linked into lists by a
partial successor function such that, starting from any node, $n$ steps run off the end of its
list, and let each node $v$ carry a value $x_v$ in an additive monoid $M$. Then for every node
$v$, the suffix sum of $v$ is $x_v$ plus the suffix sum of the successor of $v$, or just $x_v$
if $v$ has no successor.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.suffixSum_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#suffix-sum-eq).

## Segment sums of unit values count nodes

Let $n$ nodes be linked into lists by a
partial successor function such that, starting from any node, $n$ steps run off the end of its
list, and give every node the value $1 \in \mathbb{N}$. Then for every $k \in \mathbb{N}$ and
every node $v$, the segment sum of length $k$ from $v$ (the sum of the values of the first $k$
nodes from $v$, fewer at the end of the list) is $\min(k, \operatorname{rank}(v) + 1)$, where
$\operatorname{rank}(v)$ is the number of nodes after $v$ in its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.segSum_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#seg-sum-one).

## List ranking is the special case of unit values

Let $n$ nodes be linked into lists by
a partial successor function such that, starting from any node, $n$ steps run off the end of
its list. If every node has value $1 \in \mathbb{N}$, then the suffix sum of every node $v$ is
$\operatorname{rank}(v) + 1$, where $\operatorname{rank}(v)$ is the number of nodes after $v$ in
its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.suffixSum_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#suffix-sum-one).

## State of pointer jumping for suffix sums

For $n$ nodes and a type $M$, a state assigns
to each node $v$ a pointer, which is either a node or none (past the end of the list), and an
accumulated value in $M$. The accumulated value is meant to be the sum of the node values from
$v$ up to, but not including, the pointer's target.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.State`, a structure declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#state).

## Initial state of pointer jumping for suffix sums

Given nodes $0, \dots, n-1$ with a
partial successor function $\mathrm{succ}$ and values $x_v$ in an additive monoid $M$, the
initial state gives each node $v$ the pointer $\mathrm{succ}(v)$ (undefined at the end of a
list) and the sum $x_v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.init`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#init).

## One round of pointer jumping for suffix sums

Given a state in which each node $v$ has
a pointer $p(v)$, either a node or undefined, and a sum $s(v)$ in an additive monoid $M$, one
round produces a new state as follows. If $p(v)$ is undefined, the pointer of $v$ stays
undefined and its sum stays $s(v)$. If $p(v) = u$, the new pointer of $v$ is $p(u)$ and its new
sum is $s(v) + s(u)$, with $s(u)$ added on the right so that list order is kept.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.round`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#round).

## State after $t$ rounds of pointer jumping for suffix sums

Given a partial successor
function $\mathrm{succ}$ on nodes $0, \dots, n-1$, values $x_v$ in an additive monoid $M$ and
$t \in \mathbb{N}$, the state after $t$ rounds is obtained from the initial state (pointers
$\mathrm{succ}(v)$, sums $x_v$) by applying one round of pointer jumping $t$ times.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.rounds`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds).

## The invariant of pointer jumping for suffix sums

Let $\mathrm{succ}$ be a partial
successor function on nodes $0, \dots, n-1$ and $x_v$ values in an additive monoid $M$. For
every $t \in \mathbb{N}$ and every node $v$, after $t$ rounds of pointer jumping the pointer of
$v$ is the node reached from $v$ in $2^t$ steps along $\mathrm{succ}$ (undefined if the list
ends sooner), and the sum of $v$ is the sum, in list order, of the values of the nodes reached
from $v$ in $0, 1, \dots, 2^t - 1$ steps (a missing node contributes $0$).

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.rounds_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-spec).

## Pointer-jumping sums are the suffix sums once $n \le 2^t$

Let $\mathrm{succ}$ be a
partial successor function on nodes $0, \dots, n-1$ under which every list ends, that is, from
every node, the node reached in $n$ steps along $\mathrm{succ}$ is undefined, and let $x_v$ be
values in an additive monoid $M$. If $t \in \mathbb{N}$ satisfies $n \le 2^t$, then for every
node $v$ the sum of $v$ after $t$ rounds of pointer jumping is the suffix sum of $v$: the sum, in
list order, of the values from $v$ to the end of its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.rounds_acc`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-acc).

## Pointer-jumping state as arrays

A suffix-sum pointer-jumping state on $n$ nodes is
stored as a pair of arrays of length $n$: the array whose entry $v$ is the pointer of node $v$,
and the array whose entry $v$ is the accumulated value of node $v$.

Evaluating the rounds of pointer jumping directly re-reads earlier rounds at every query, a
cost exponential in the number of rounds; on arrays each round costs $O(n)$ operations.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.tabulate`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#tabulate).

## One round of pointer jumping on arrays

Given an array $P$ of pointers (each a node
among $0, \dots, n-1$ or undefined) and an array $S$ of sums in an additive monoid $M$, one
round returns arrays $P'$ and $S'$ of length $n$ where, for each node $v$: if $P[v]$ is
undefined, then $P'[v]$ is undefined and $S'[v] = S[v]$; if $P[v] = u$, then $P'[v] = P[u]$ and
$S'[v] = S[v] + S[u]$. A read outside an array gives an undefined pointer or the sum $0$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.roundTab`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#round-tab).

## Arrays after $t$ rounds of pointer jumping for suffix sums

Given a partial successor
function $\mathrm{succ}$ on nodes $0, \dots, n-1$ and values $x_v$ in an additive monoid $M$,
the pair of arrays after $0$ rounds stores the pointers $\mathrm{succ}(v)$ and the sums $x_v$,
and the pair after $t + 1$ rounds is one round of pointer jumping on arrays applied to the pair
after $t$ rounds.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.roundsTab`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#rounds-tab).

## Suffix sums by pointer jumping on arrays

Given a partial successor function
$\mathrm{succ}$ on nodes $0, \dots, n-1$ and values $x_v$ in an additive monoid $M$, this is
the array of sums obtained after $\lceil \log_2 n \rceil$ rounds (the least $k$ with
$n \le 2^k$) of pointer jumping on arrays, starting from the pointers $\mathrm{succ}(v)$ and the
sums $x_v$.

When every list ends, entry $v$ is the suffix sum of node $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.listSums`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#list-sums).

## Pointer jumping computes all suffix sums in $\lceil \log_2 n \rceil$ rounds

Let
$\mathrm{succ}$ be a partial successor function on nodes $0, \dots, n-1$ under which every list
ends, that is, from every node, the node reached in $n$ steps along $\mathrm{succ}$ is undefined,
and let $x_v$ be values in an additive monoid $M$. Then for every node $v$, entry $v$ of the
array of sums computed by $\lceil \log_2 n \rceil$ rounds of pointer jumping on arrays is the
suffix sum of $v$: the sum, in list order, of the values from $v$ to the end of its list.

Formalized by `Cslib.Algorithms.Lean.Parallel.ListPrefix.listSums_getD`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/ListPrefix.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html#list-sums-get-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List ranking by pointer jumping](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/parallel-algorithms/list-ranking-by-pointer-jumping)
