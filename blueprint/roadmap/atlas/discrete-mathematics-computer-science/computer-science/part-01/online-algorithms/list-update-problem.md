---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Online.ListUpdate.accessCost, Cslib.Algorithms.Lean.Online.ListUpdate.mtf, Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost, Cslib.Algorithms.Lean.Online.ListUpdate.mtfFinal, Cslib.Algorithms.Lean.Online.ListUpdate.invSet, Cslib.Algorithms.Lean.Online.ListUpdate.inv, Cslib.Algorithms.Lean.Online.ListUpdate.offlineCost, Cslib.Algorithms.Lean.Online.ListUpdate.freeMove
statement: formalized
proof: formalized
---

# List update problem

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html).

## Costs

## Access cost

The cost of accessing an item $x$ in a list $L$ is its position in $L$,
counting from $1$: one more than the index of the first occurrence of $x$ in $L$. If $x$ does not
occur in $L$, the cost is the length of $L$ plus one.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.accessCost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#access-cost).

## Move-to-front

For a list $L$ and an item $x$, moving $x$ to the front gives the list
consisting of $x$ followed by $L$ with its first occurrence of $x$ removed; if $x$ does not
occur in $L$, this is $x$ followed by $L$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtf`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf).

## Cost of move-to-front

Starting from a list $L$, move-to-front serves a request sequence
$\sigma$ one request at a time: a request $x$ costs the position of $x$ in the current list,
counting from $1$ (an item not in the list costs its length plus one), and then $x$ is moved to
the front (inserted at the front if absent). The cost of move-to-front on $\sigma$ from $L$ is
the sum of these access costs.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost).

## Final list of move-to-front

Starting from a list $L$ and serving a request sequence
$\sigma$, move-to-front moves each request $x$ in turn to the front of the current list
(inserting it at the front if it is absent). The final list of move-to-front on $\sigma$ from
$L$ is the list it ends with.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfFinal`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-final).

## Inversion set of two lists

For lists $M$ and $L$, the inversion set is the set of pairs
$(a, b)$ of items of $M$ with $a$ before $b$ in $M$ and $b$ before $a$ in $L$, that is, the pairs
that $M$ and $L$ order differently. Here the position of an item in a list is the index of its
first occurrence, and an item that does not occur in the list sits at the position equal to the
length of the list.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.invSet`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#inv-set).

## Number of inversions between two lists

For lists $M$ and $L$, the number of inversions
of $L$ against $M$ is the size of their inversion set: the number of pairs $(a, b)$ of items of
$M$ with $a$ before $b$ in $M$ and $b$ before $a$ in $L$, where the position of an item in a list
is the index of its first occurrence, or the length of the list if it does not occur.

When $L$ is a rearrangement of a list $M$ without duplicates, this is the Kendall tau distance
between them.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.inv`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#inv).

## Offline cost without free exchanges

Given lists $L_0, L_1, L_2, \dots$, the offline cost
of a request sequence $\sigma = x_0 x_1 \cdots x_{m-1}$ is the sum over $t < m$ of the access cost
of $x_t$ in $L_t$ (its position, counting from $1$) plus the number of inversions between $L_t$
and $L_{t+1}$. That is, the algorithm serves request $t$ with $L_t$ and then rearranges it into
$L_{t+1}$, paying one for each pair of items whose relative order it changes.

Adding free exchanges gives the offline cost with free exchanges.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.offlineCost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#offline-cost).

## Free move

A free exchange (Sleator and Tarjan): right after accessing $x$ in a list $L$,
move $x$ forward to index $j$ (indices counted from $0$), at no charge. If the index of $x$ in
$L$ is at most $j$, the list is unchanged, so $x$ never moves backward for free; otherwise the
result is obtained by erasing the first occurrence of $x$ from $L$ and inserting $x$ back so that
it has index $j$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.freeMove`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#free-move).

## Offline cost with free exchanges

Given lists $L_0, L_1, L_2, \dots$, target indices
$J_0, J_1, J_2, \dots$ and a request sequence $\sigma = x_0 x_1 \cdots x_{m-1}$, let $L_t'$ be the
list obtained from $L_t$ by the free exchange that moves $x_t$ forward to index $J_t$ (counting
from $0$); it equals $L_t$ if $x_t$ already has index at most $J_t$. The offline cost with free
exchanges of $\sigma$ is the sum over $t < m$ of the access cost of $x_t$ in $L_t$ (its position,
counting from $1$) plus the number of inversions between $L_t'$ and $L_{t+1}$.

This is the model of Sleator and Tarjan: the free exchange costs nothing, and each pair of items
whose relative order changes from $L_t'$ to $L_{t+1}$ costs one. With no free moves it is the
offline cost without free exchanges.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.offlineCostFree`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#offline-cost-free).

## Indices after erasing an entry

Let $M$ be a list with no repeated entries and let
$a \ne x$ be entries of $M$. After erasing $x$ from $M$, the index of $a$ is unchanged if $a$
comes before $x$ in $M$, and is one less if $a$ comes after $x$ (indices counted from $0$).

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.idxOf_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#idx-of-erase).

## Move-to-front keeps the relative order of the other items

Let $M$ be a list without
duplicates, $x$ an item of $M$, and let $M'$ be the list obtained from $M$ by moving $x$ to the
front. For any items $a \ne x$ and $b \ne x$ of $M$, $a$ comes before $b$ in $M'$ if and only if
$a$ comes before $b$ in $M$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.idxOf_mtf_lt_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#idx-of-mtf-lt-iff).

## Counting the entries before an entry

If $L$ is a list with no repeated entries and $x$
is an entry of $L$, then the number of entries of $L$ whose index is less than the index of $x$
equals the index of $x$ (indices counted from $0$).

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.card_before`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#card-before).

## Members of the inversion set

Let $M$ and $L$ be lists. If a pair $(a, b)$ belongs to the
inversion set of $M$ and $L$, then $a$ and $b$ are items of $M$, $a$ comes before $b$ in $M$, and
$b$ comes before $a$ in $L$. Here the position of an item in a list is the index of its first
occurrence, and an item that does not occur in the list sits at the position equal to the length
of the list.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mem_of_mem_invSet`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mem-of-mem-inv-set).

## Triangle inequality for inversions

Let $M$, $L$ and $L'$ be lists with $L$ a
rearrangement of $M$. Then the number of inversions of $L'$ against $M$ is at most the number of
inversions of $L$ against $M$ plus the number of inversions of $L'$ against $L$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.inv_triangle`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#inv-triangle).

## The amortized cost of a move-to-front step

Let $M$ be a list of distinct items, $L$ a
rearrangement of $M$ (the offline list), and $x$ an item of $M$ at position $k$ in $M$ and
position $i$ in $L$, counting from $1$. Let $\Phi$ be the number of inversions between $M$ and
$L$ (the pairs of items that the two lists order differently), and $\Phi'$ the number of
inversions between the list obtained from $M$ by moving $x$ to the front and $L$. Then
$k + \Phi' \le \Phi + 2i - 1$.

This is the amortized step of Sleator and Tarjan's analysis, with potential $\Phi$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtf_step`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-step).

## Move-to-front rearranges the list

If $x$ is an item of a list $M$, then the list
obtained from $M$ by moving $x$ to the front is a rearrangement (permutation) of $M$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtf_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-perm).

## A free move rearranges the list

If $x$ is an item of a list $L$, then for every index
$j$ (counting from $0$), the list obtained from $L$ by the free move of $x$ to index $j$ is a
rearrangement (permutation) of $L$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.freeMove_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#free-move-perm).

## Free moves never add inversions against a list headed by the moved item

Let $L$ be a list
without duplicates, $x$ an item of $L$, and $N$ a list that is empty or starts with $x$, all of
whose items occur in $L$. For every $j \in \mathbb{N}$, let $L'$ be the list obtained from $L$ by
moving $x$ forward for free so that exactly $j$ items precede it, where $L' = L$ if at most $j$
items already precede $x$ in $L$. Then the number of inversions of $L'$ against $N$ is at most the
number of inversions of $L$ against $N$.

This applies to move-to-front's list right after accessing $x$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.inv_freeMove_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#inv-free-move-le).

## Amortized bound for move-to-front over a request sequence, with free exchanges

Let $M$ be
a list without duplicates, $\sigma$ a sequence of $m$ requests, each an item of $M$, $L_0, L_1,
\dots$ lists that are each a rearrangement of $M$, and $J_0, J_1, \dots$ natural numbers.
Accessing the item at position $i$ of a list, counting from $1$, costs $i$. Let $C$ be the total
access cost of move-to-front on $\sigma$ starting from $M$, $F$ the list it ends with, and $D$
the cost on $\sigma$ of the offline algorithm with free exchanges that serves the $t$-th request
(counting from $0$) with list $L_t$, paying its access cost, then moves the accessed item forward
for free so that exactly $J_t$ items precede it (no move if at most $J_t$ items already precede
it), and finally rearranges the resulting list into $L_{t+1}$, paying one for each pair of items
whose relative order changes. Writing $\mathrm{inv}(N, K)$ for the number of inversions of $K$
against $N$,

$$C + \mathrm{inv}(F, L_m) + m \le 2D + \mathrm{inv}(M, L_0).$$

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost_add_inv_le_free`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost-add-inv-le-free).

## Without free moves the two offline costs agree

Let $K$ be a natural number and let
$L_0, L_1, L_2, \dots$ be lists, each of length at most $K$. Take every free-exchange target to be
$K$; this moves nothing, since every item already has index at most $K$. Then for every request
sequence $\sigma$, the offline cost with free exchanges of serving $\sigma$ with $L_0, L_1, \dots$
equals the offline cost without free exchanges of serving $\sigma$ with $L_0, L_1, \dots$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.offlineCostFree_noMove`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#offline-cost-free-no-move).

## Amortized bound for move-to-front over a request sequence

Let $M$ be a list without
duplicates, $\sigma$ a sequence of $m$ requests, each an item of $M$, and $L_0, L_1, \dots$ lists
that are each a rearrangement of $M$. Accessing the item at position $i$ of a list, counting from
$1$, costs $i$. Let $C$ be the total access cost of move-to-front on $\sigma$ starting from $M$,
$F$ the list it ends with, and $D$ the cost on $\sigma$ of the offline algorithm without free
exchanges that serves the $t$-th request (counting from $0$) with list $L_t$, paying its access
cost, and then rearranges it into $L_{t+1}$, paying one for each pair of items whose relative
order changes. Writing $\mathrm{inv}(N, K)$ for the number of inversions of $K$ against $N$,

$$C + \mathrm{inv}(F, L_m) + m \le 2D + \mathrm{inv}(M, L_0).$$

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost_add_inv_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost-add-inv-le).

## Move-to-front is 2-competitive

In the model of Sleator and Tarjan (1985) with free
exchanges, let $M$ be a list of distinct items and $\sigma$ a sequence of $m$ requests, each an
item of $M$. Consider an offline algorithm given by lists $L_0, L_1, \ldots$, each a
rearrangement of $M$ with $L_0 = M$, and natural numbers $J_0, J_1, \ldots$. It serves request
$t$ (counting from $0$) with the list $L_t$ and pays the position of the request in $L_t$
(counting from $1$). If more than $J_t$ items precede the request in $L_t$, it then moves the
request forward for free so that exactly $J_t$ items precede it, keeping the order of the other
items. Finally it pays one for each pair of items whose relative order differs between the
resulting list and $L_{t+1}$. Then the access cost of move-to-front on $\sigma$ starting from
$M$, plus $m$, is at most twice the total cost of the offline algorithm.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost_le_free`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost-le-free).

## Move-to-front is 2-competitive without free exchanges

Let $M$ be a list of distinct
items and $\sigma$ a sequence of $m$ requests, each an item of $M$. Consider an offline
algorithm that serves request $t$ with a list $L_t$, where every $L_t$ is a rearrangement of
$M$ and $L_0 = M$: it pays the position of the request in $L_t$ (counting from $1$), and then
one for each pair of items whose relative order differs between $L_t$ and $L_{t+1}$. Then the
access cost of move-to-front on $\sigma$ starting from $M$, plus $m$, is at most twice the
total cost of the offline algorithm.

This is the special case of the model with free exchanges in which no free exchange is made.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost-le).

## Move-to-front against a static list

Let $M$ be a list of distinct items, $L$ a
rearrangement of $M$, and $\sigma$ a sequence of $m$ requests, each an item of $M$. Then the
access cost of move-to-front on $\sigma$ starting from $M$, plus $m$, is at most twice the cost
of serving $\sigma$ with the fixed list $L$ (the sum over the requests of their positions in $L$,
counting from $1$), plus the number of inversions between $M$ and $L$ (the pairs of items that
$M$ and $L$ order differently).

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfCost_le_static`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-cost-le-static).

## Deterministic online list-update algorithm

A deterministic online list-update algorithm on the items of `M`: a state machine whose list
is always a rearrangement of `M`. Its rearrangements are free, which only strengthens the lower
bound.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.OnlineListUpdate`, a structure declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#deterministic-online-list-update-algorit).

## Cost of an online list-update algorithm

The cost of a deterministic online list-update
algorithm $A$ on a request sequence $x_1, \dots, x_m$ from a state $q_0$ is
$c_1 + \dots + c_m$, where $q_i$ is the state $A$ moves to from $q_{i-1}$ on request $x_i$ and
$c_i$ is the access cost of $x_i$ in the list of state $q_{i-1}$. The empty sequence costs $0$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.OnlineListUpdate.cost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#cost).

## The list-update adversary

Given a deterministic online list-update algorithm $A$, a
default item $d$, a number $n$ and a state $q$ of $A$, the adversary's sequence is the sequence of
$n$ requests that starts in state $q$, always requests the last item of $A$'s current list, and
then moves $A$ to its next state on that request. If the current list is empty, the default item
$d$ is requested instead.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.OnlineListUpdate.adversary`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#adversary).

## The list of an algorithm on a nonempty list is never empty

Let $A$ be a deterministic
online list-update algorithm on the items of a nonempty list $M$. Then in every state of $A$, the
list of $A$ is nonempty.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.OnlineListUpdate.list_ne_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#list-ne-nil).

## The adversary makes every access cost the full length of the list

Let $M$ be a nonempty
list of $\ell$ distinct items and let $A$ be a deterministic online list-update algorithm on the
items of $M$. For every default item $d$, every natural number $n$ and every state $q$ of $A$,
the cost of $A$ from state $q$ on the adversary's sequence of $n$ requests from $q$ with default
item $d$ is $n \ell$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.OnlineListUpdate.cost_adversary`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#cost-adversary).

## Online move-to-front

For a list $M$, online move-to-front is the online list-update
algorithm on the items of $M$ whose states are the rearrangements of $M$, starting from $M$
itself: on a request $x$ that is in the current list it moves $x$ to the front, and it ignores
requests that are not in the current list.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfOnline`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-online).

## Online move-to-front pays the move-to-front cost

Let $M$ be a list and $\sigma$ a
request sequence whose requests are all items of $M$. From any state of online move-to-front
on $M$, its access cost on $\sigma$ equals the cost of move-to-front on $\sigma$ starting from
the list of that state.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.mtfOnline_cost`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#mtf-online-cost).

## Static cost

The static cost of serving a request sequence $\sigma = x_0 x_1 \cdots x_{m-1}$
with a fixed list $L$ is the sum over $t < m$ of the access cost of $x_t$ in $L$, its position in
$L$ counting from $1$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.staticCost`, a definition declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#static-cost).

## The static cost is the offline cost of a constant list

For every list $L$ and every
request sequence $\sigma$, the offline cost (without free exchanges) of serving $\sigma$ with the
constant sequence of lists $L, L, L, \dots$ equals the static cost of serving $\sigma$ with $L$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.offlineCost_const`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#offline-cost-const).

## Positions in a list and in its reverse

If $L$ is a list of length $\ell$ with no
repeated entries and $x$ is an entry of $L$, then the access cost of $x$ in $L$ plus the access
cost of $x$ in the reverse of $L$ equals $\ell + 1$: the positions of $x$ in $L$ and in its
reverse, counting from $1$, add up to $\ell + 1$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.accessCost_add_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#access-cost-add-reverse).

## A list or its reverse serves any sequence at average cost at most $(\ell + 1)/2$

Let $L$
be a list of $\ell$ distinct items. For every request sequence $\sigma$ of $m$ items of $L$, the
static cost of serving $\sigma$ with $L$ plus the static cost of serving $\sigma$ with the reverse
of $L$ equals $m(\ell + 1)$.

In particular, one of the two static costs is at most $m(\ell + 1)/2$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.staticCost_add_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#static-cost-add-reverse).

## Inversions are at most the squared length

For any lists $M$ and $L$, the number of
inversions of $L$ against $M$ is at most $\ell^2$, where $\ell$ is the length of $M$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.inv_le_sq`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#inv-le-sq).

## Switching lists after the first request

Let $M$ be a list of length $\ell$ and $R$ a list,
and write $\mathrm{inv}(M, R)$ for the number of inversions between $M$ and $R$. For every request
sequence $\sigma$ of items of $M$, the offline cost (without free exchanges) of serving $\sigma$
with the lists $M, R, R, R, \dots$ is at most $\ell + \mathrm{inv}(M, R)$ plus the static cost of
serving $\sigma$ with $R$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.offlineCost_switch_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 552](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#offline-cost-switch-le).

## Online and offline costs on the adversary's sequence

Let $M$ be a nonempty list of $\ell$
distinct items, let $A$ be a deterministic online list-update algorithm on the items of $M$, let
$d$ be an item and $n$ a natural number, and let $\sigma$ be the adversary's sequence of $n$
requests against $A$ from its initial state, with default item $d$. Then the cost of $A$ on
$\sigma$ from its initial state is $n \ell$, and there are lists $L_0, L_1, L_2, \dots$, each a
rearrangement of $M$, with $L_0 = M$ such that the offline cost $C$ of this sequence of lists on
$\sigma$ satisfies $2 C \le n (\ell + 1) + 2 (\ell + \ell^2)$.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.adversary_vs_offline`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#adversary-vs-offline).

## No deterministic online list-update algorithm beats $2 - 2/(\ell + 1)$

Let $M$ be a
nonempty list of $\ell$ distinct items and let $A$ be a deterministic online list-update
algorithm on the items of $M$. Let $c$, $d$ and $b$ be natural numbers with
$c (\ell + 1) < 2 \ell d$ (so $d \ge 1$ and $c / d < 2\ell / (\ell + 1) = 2 - 2/(\ell + 1)$).
Then there are a request sequence $\sigma$, each request an item of $M$, and lists
$L_0, L_1, L_2, \dots$, each a rearrangement of $M$, with $L_0 = M$, such that
$c \cdot C + d \cdot b < d \cdot K$, where $C$ is the offline cost without free exchanges of
$L_0, L_1, \dots$ on $\sigma$ and $K$ is the cost of $A$ on $\sigma$ from its initial state.

The offline lists make no free exchanges, so the same holds with the offline cost with free
exchanges in place of $C$.

## Sources

- Karp and Raghavan, see Irani, *Two results on the list update problem*, IPL 38, 1991; Borodin and El-Yaniv, Chapter 1.

Formalized by `Cslib.Algorithms.Lean.Online.ListUpdate.not_competitive`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/ListUpdate.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/ListUpdate.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html#not-competitive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List update problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/list-update-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/online-algorithms/list-update-problem)
