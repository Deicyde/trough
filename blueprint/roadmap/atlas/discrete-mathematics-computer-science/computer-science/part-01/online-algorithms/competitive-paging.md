---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Online.Paging.lruStep, Cslib.Algorithms.Lean.Online.Paging.lruCache, Cslib.Algorithms.Lean.Online.Paging.lruMisses, Cslib.Algorithms.Lean.Online.Paging.lruStep_take_of_mem, Cslib.Algorithms.Lean.Online.Paging.lruStep_take_of_not_mem, Cslib.Algorithms.Lean.Online.Paging.phaseSplit, Cslib.Algorithms.Lean.Online.Paging.lruMisses_phase, Cslib.Algorithms.Lean.Online.Paging.phaseSplit_snd_cons
statement: formalized
proof: formalized
---

# Competitive paging

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html).

## One LRU step

For a capacity $k$, a cache $c$ (a list of pages, most recently used first)
and a requested page $p$, the LRU step removes the first occurrence of $p$ from $c$ (if any), puts
$p$ at the front, and keeps the first $k$ pages of the result. On a miss with a cache of exactly
$k \ge 1$ pages, this evicts the last page, the least recently used one.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruStep`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-step).

## Cache after LRU serves a request sequence

For a capacity $k$, a cache $c$ (a list of
pages, most recently used first) and a request sequence $\sigma$, this is the cache obtained from
$c$ by applying one LRU step with capacity $k$ for each request of $\sigma$, in order.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruCache`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-cache).

## Number of LRU misses

For a capacity $k$, a cache $c$ and a request sequence $\sigma$, this
is the number of requests of $\sigma$ that are not in the current cache when they are served,
where the cache starts at $c$ and after each request is updated by one LRU step with capacity
$k$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruMisses`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-misses).

## The recency invariant for a repeated page

Let $k$ be a capacity, $c$ a cache (most
recently used first) and $S$ a list of at most $k$ pages equal to the first $|S|$ pages of $c$.
If $p \in S$, then after one LRU step with capacity $k$ serving $p$, the first $|S|$ pages of the
cache are $p$ followed by $S$ with the first occurrence of $p$ removed.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruStep_take_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-step-take-of-mem).

## The recency invariant for a new page

Let $k$ be a capacity, $c$ a cache (most recently
used first) and $S$ a list with $|S| + 1 \le k$ equal to the first $|S|$ pages of $c$. If
$p \notin S$, then after one LRU step with capacity $k$ serving $p$, the first $|S| + 1$ pages of
the cache are $p$ followed by $S$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruStep_take_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-step-take-of-not-mem).

## Splitting off a phase

Given a capacity $k$ and a list $s$ of pages (the pages already in
the current phase, most recent first), a request sequence $\sigma$ is split into a phase and a
remainder as follows. The empty sequence splits into two empty parts. For a sequence $p$
followed by $\sigma'$: if $p$ is in $s$, then $p$ joins the phase and $\sigma'$ is split with $s$
replaced by $p$ followed by $s$ with its first occurrence of $p$ removed; if $p$ is not in $s$
and $s$ has fewer than $k$ entries, then $p$ joins the phase and $\sigma'$ is split with $p$
added at the front of $s$; otherwise the phase is empty and the remainder is the whole sequence.

When $s$ has no repetitions and at most $k$ pages, the phase is the longest prefix of $\sigma$
whose distinct pages, together with those of $s$, number at most $k$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.phaseSplit`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#phase-split).

## LRU misses at most $k - |S|$ times in the rest of a phase

Let $k$ be a capacity, $c$ a
cache (most recently used first) and $S$ a duplicate-free list of at most $k$ pages equal to the
first $|S|$ pages of $c$. For every request sequence $\sigma$, let $\pi$ be the phase that the
phase split cuts from $\sigma$ with $S$ as the pages already in the phase: the longest prefix of
$\sigma$ whose distinct pages, together with those of $S$, number at most $k$. Then the number of
LRU misses with capacity $k$ serving $\pi$ from $c$, plus $|S|$, is at most $k$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruMisses_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-misses-phase).

## A phase ends only on a $(k + 1)$-st distinct page

Let $k$ be a capacity, let $s$ be a
list of pages without repetitions with at most $k$ pages (the pages already in the current
phase), and let $\sigma$ be a request sequence. If the remainder left after splitting off a phase
from $\sigma$ given $s$ starts with a page $q$, then there is a list $S$ of exactly $k$ pairwise
distinct pages, none equal to $q$, each of which lies in $s$ or in that phase.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.phaseSplit_snd_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#phase-split-snd-cons).

## The event of an LRU step

For a capacity $k$, a cache $c$ (a list of pages, most recently
used first) and a requested page $p$, the LRU event is a hit on $p$ if $p \in c$. Otherwise it is
a miss on $p$ that evicts the last page of $c$ (the least recently used one) if $c$ is nonempty,
$k > 0$ and $c$ has at least $k$ pages, and a miss on $p$ without eviction in all other cases.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruEvent`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-event).

## The LRU trace

Given a capacity $k$, a cache $c$ and a request sequence $\sigma$, the
events LRU emits on $\sigma$ from $c$: nothing on the empty sequence, and on a sequence $p$
followed by $\sigma'$, the event LRU emits when serving $p$ from $c$, followed by the events LRU
emits on $\sigma'$ from the cache after one LRU step with capacity $k$ serving $p$ from $c$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruTrace`, a definition declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-trace).

## Each LRU step is a legal transition

Let $k$ be a capacity and $c$ a duplicate-free cache
with at most $k$ pages. For every page $p$, the cache system with capacity $k$ has a transition
from $c$, labelled by the LRU event for $p$ at $c$, to the cache produced by one LRU step with
capacity $k$ serving $p$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lru_tr`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-tr).

## LRU is a legal cache manager

Let $k$ be a capacity, $c$ a cache given as a list of pages
without repetitions with at most $k$ pages, and $\sigma$ a request sequence. Then the sequence of
events that LRU emits when serving $\sigma$ from $c$ is a run of the cache system with capacity
$k$ from $c$ to the cache LRU holds after serving $\sigma$; the pages requested by these events are
exactly $\sigma$, in order; and the number of misses among these events equals the number of
misses of LRU on $\sigma$ from $c$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruTrace_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-trace-spec).

## LRU is $k$-competitive

Let $k \ge 1$ and let $c$ be a duplicate-free cache with at most
$k$ pages. Let $e$ be a legal trace of the cache system with capacity $k$ that starts from a
duplicate-free cache with at most $k$ pages, and let $m$ be its number of misses. Then the trace
that LRU with capacity $k$ emits when serving, from $c$, the requests of $e$ in order has at most
$k m + k$ misses.

This is the bound of Sleator and Tarjan for an online and an offline cache of the same size.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruMisses_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-misses-le).

## LRU is $k$-competitive against the offline optimum

Let $k \ge 1$, and let $c$ and $c_0$
be duplicate-free caches with at most $k$ pages each. For every request sequence $\sigma$, the
trace that LRU with capacity $k$ emits when serving $\sigma$ from $c$ has at most $k m + k$
misses, where $m$ is the number of misses of the furthest-in-future manager with capacity $k$
serving $\sigma$ from $c_0$.

Furthest-in-future misses no more often than any legal trace serving the same requests from the
same cache, so it is the offline optimum.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruMisses_le_furthestInFuture`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/Paging.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/Paging.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-misses-le-furthest-in-future).

## Deterministic online paging algorithm

A deterministic online paging algorithm with cache size `k`: a state machine whose cache
never holds more than `k` pages. Its moves need not be legal transitions; the lower bound holds
for any such machine.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.OnlinePager`, a structure declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#deterministic-online-paging-algorithm).

## Misses of an online pager

For an online pager $A$, a state $q$ and a request sequence
$\sigma$, the number of misses of $A$ from $q$ on $\sigma$ counts the requests of $\sigma$ that
are not in the cache of the current state, where the run starts at $q$ and each request moves
$A$ to its next state.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.OnlinePager.misses`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#misses).

## LRU as an online pager

LRU as an online pager.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruPager`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-as-an-online-pager).

## LRU as an online pager has LRU's miss count

For every cache $c$ of at most $k$ pages and
every request sequence $\sigma$, the number of misses of LRU with capacity $k$, viewed as an
online pager and started in the state with cache $c$, on $\sigma$ equals the number of misses of
LRU with capacity $k$ started with cache $c$ on $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.lruPager_misses`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#lru-pager-misses).

## Outside page of a cache

For a natural number $k$ and a list $c$ of pages from
$\{0, \dots, k\}$, the outside page of $c$ is the smallest $x \in \{0, \dots, k\}$ that does not
occur in $c$, or $0$ if every page of $\{0, \dots, k\}$ occurs in $c$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.outside`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#outside).

## The outside page is not cached

Let $k$ be a natural number and let $c$ be a list of at
most $k$ pages from $\{0, \dots, k\}$. Then the outside page of $c$ does not occur in $c$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.outside_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#outside-not-mem).

## The paging adversary

Let $A$ be a deterministic online pager with cache size $k$ on the
$k + 1$ pages $0, \dots, k$. From a state $q$ of $A$, the adversary's sequence of $n$ requests is
empty for $n = 0$; for $n + 1$ it first requests the smallest page not in the cache of $q$ (page
$0$ if there is none) and then continues with the adversary's sequence of $n$ requests from the
state that $A$ reaches from $q$ by serving that request.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.adversary`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#adversary).

## The pager misses every request

**The pager misses every request** of the adversary's sequence.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.misses_adversary`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#misses-adversary).

## Offline paging step

Given a cache size $k$, a cache $c$ (a list of pages), a requested
page $p$ and the list $f$ of future requests, the offline step returns an event and a new cache.
If $p \in c$, it is a hit on $p$ and the cache is unchanged. Otherwise, if $c$ has fewer than $k$
pages, it is a miss on $p$ with no eviction and the new cache is $p$ followed by $c$. Otherwise,
if some page of $c$ does not occur among the first $k - 1$ entries of $f$ (no entries at all when
$k = 0$, and all of $f$ when $f$ is shorter), it is a miss on $p$ evicting the first such page $v$
in $c$, and the new cache is $p$ followed by $c$ with the first occurrence of $v$ removed. If
there is no such page, it is a miss on $p$ with no eviction and the new cache is $p$ followed by
$c$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.optStep`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#opt-step).

## Offline paging trace

Given a cache size $k$, the offline trace from a cache $c$ on a list
of requests is defined by recursion on the list: on the empty list it is empty, and on a list
with first request $p$ and remaining requests $r$ it is the event of the offline step with cache
size $k$ on $c$, $p$ and $r$, followed by the offline trace on $r$ from the new cache of that
step.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.optTrace`, a definition declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#opt-trace).

## A full cache has a page outside the next $k - 1$ requests

Let $k \ge 1$, let $c$ be a
list of $k$ distinct pages and let $f$ be any list of requests. Then the search through $c$ for
the first page that does not occur among the first $k - 1$ entries of $f$ succeeds; in
particular, some page of $c$ does not occur there.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.find?_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#find-is-some).

## Each offline step is a legal transition

Let $k \ge 1$, let $c$ be a cache of at most $k$
distinct pages, let $p$ be a requested page and let $f$ be the list of future requests. Then the
event and the new cache produced by the offline step with cache size $k$ on $c$, $p$ and $f$
form a legal transition from $c$ of the caching system with capacity $k$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.optStep_tr`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#opt-step-tr).

## The offline trace is legal

Let $k \ge 1$, let $c$ be a cache of at most $k$ distinct
pages and let $\sigma$ be a list of requests. Then the offline trace with cache size $k$ from
$c$ on $\sigma$ is a legal run of the caching system with capacity $k$ from $c$ to some final
cache, and the pages served by its events are, in order, exactly $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.optTrace_legal`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#opt-trace-legal).

## Hits do not change the offline strategy's misses

Let $k$ be a capacity, let $c$ be a
cache and let $w$ be a request sequence all of whose requests lie in $c$. Then for every request
sequence $\tau$, the offline strategy with capacity $k$ (on a miss with a full cache, evict the
first cached page not among the next $k - 1$ requests, if there is one) started with cache $c$
misses as many times on $w$ followed by $\tau$ as on $\tau$ alone.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.misses_optTrace_hits`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#misses-opt-trace-hits).

## After a miss on a full cache, every page except the evicted one is present

Let $c$ be a
list of $k$ distinct pages among the $k + 1$ pages $0, \dots, k$, let $p$ be a page not in $c$,
and let $v$ be any page. Then every page $x \neq v$ lies in the cache obtained from $c$ by
removing $v$ and adding $p$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.mem_of_full`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#mem-of-full).

## The offline trace misses at most once every $k$ requests

Let $k \ge 1$ and consider the
$k + 1$ pages $0, 1, \dots, k$. Let $N$ be a natural number, $\sigma$ a sequence of $n \le N$
requests to these pages, and $c$ a cache of $|c| \le k$ distinct pages. Then the number of misses
of the offline trace with cache size $k$ from $c$ on $\sigma$ is at most
$(k - |c|) + \lfloor (n + k - 1) / k \rfloor = (k - |c|) + \lceil n / k \rceil$: after at most
$k - |c|$ misses filling the cache, at most one miss every $k$ requests.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.misses_optTrace_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#misses-opt-trace-le).

## The adversary forces $n$ misses while the optimum misses at most $k + \lceil n / k \rceil$ times

**The adversary forces $n$ misses while the optimum misses at most $k + \lceil n / k \rceil$
times.** Let $k \ge 1$ and let $A$ be a deterministic online pager with cache size $k$ on the
$k + 1$ pages $0, \dots, k$. For every $n$, on the adversary's sequence of $n$ requests started
from the initial state of $A$, the pager $A$ started in its initial state misses exactly $n$
times, and the furthest-in-future strategy with capacity $k$ started with an empty cache misses
at most $k + \lceil n / k \rceil$ times.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.adversary_vs_optimum`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#adversary-vs-optimum).

## No deterministic online pager is better than $k$-competitive

Let $k \ge 1$ and let $A$
be a deterministic online pager with cache size $k$ on the $k + 1$ pages $0, \dots, k$. For a
request sequence $\sigma$, write $A(\sigma)$ for the number of misses of $A$ started in its
initial state on $\sigma$, and $\mathrm{OPT}(\sigma)$ for the number of misses of the
furthest-in-future strategy with capacity $k$ started with an empty cache on $\sigma$. Then for
all natural numbers $c$, $d$ with $c < kd$ and every natural number $b$, there is a request
sequence $\sigma$ with $c \cdot \mathrm{OPT}(\sigma) + b < d \cdot A(\sigma)$. That is, the pager
misses more than $c / d$ times the optimum plus $b / d$.

Formalized by `Cslib.Algorithms.Lean.Online.Paging.not_competitive_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/PagingLowerBound.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#not-competitive-of-lt).

## Misses of a paging policy on list caches

Let a paging policy be given by its step
function, which maps a cache (a list of pages) and a requested page to the next cache. Starting
from a cache $c$, the policy serves a request sequence $p_1, \dots, p_n$ by setting $c_0 = c$ and
$c_i = \mathrm{step}(c_{i-1}, p_i)$ for each $i$; its number of misses is the number of indices
$i$ with $p_i \notin c_{i-1}$.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.policyMisses`, a definition declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#policy-misses).

## A policy that misses at most $k$ times per phase is $k$-competitive

Let $k \ge 1$ and
consider a paging policy on list caches, given by its step function. Suppose that, started from
any cache, the policy misses at most $k$ times on the first phase of every request sequence (the
longest prefix of the sequence with at most $k$ distinct pages). Let $T$ be a legal trace of
caching with capacity $k$ (a run of the cache transition system) whose initial cache is a list of
at most $k$ pages with no page repeated, and let $m$ be the number of misses in $T$. Then, started
from any cache, the policy misses at most $km + k$ times on the sequence of requests served by
$T$.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.policyMisses_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#policy-misses-le).

## LRU as a policy on list caches

For every capacity $k$, the misses of the paging policy
whose step is the LRU step with capacity $k$ coincide with the LRU misses with capacity $k$, from
every starting cache and on every request sequence.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.policyMisses_lruStep`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#policy-misses-lru-step).

## One step of FIFO paging

The cache is a list of pages, oldest first, and $k$ is the
capacity. On a request for a page $p$ already in the cache $c$, the cache stays $c$. Otherwise
$p$ is appended at the back of $c$; if $c$ had fewer than $k$ pages, that is the new cache, and
if not, the front page, the one loaded earliest, is removed as well.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoStep`, a definition declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-step).

## One FIFO step keeps the cache legal

If a list $c$ of pages has no duplicates and at most
$k$ entries, then for every page $p$ the cache produced from $c$ by one FIFO step with capacity
$k$ on request $p$ also has no duplicates and at most $k$ entries.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoStep_legal`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-step-legal).

## FIFO misses at most `k` times per phase

Let $S$ be a list of at most $k$ distinct pages
(the pages already in the current phase), let $c$ be any list of pages (a FIFO cache, oldest page
first), and let $L$ be a list of distinct pages, each of them in $S$, that is a suffix of $c$. For
every request sequence $\sigma$, let $P$ be the phase split off from $\sigma$ given $S$: the
longest prefix of $\sigma$ whose distinct pages, together with those of $S$, number at most $k$.
Then the number of misses of the FIFO step policy with capacity $k$ serving $P$ from $c$, plus the
length of $L$, is at most $k$.

The pages loaded so far in the phase ($L$, in load order) stay at the back of the queue: each
miss appends one, and an eviction removes the front, which is not among them while at most $k$
pages have been loaded. So a page of the phase is missed at most once, and a phase has at most
$k$ distinct pages.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoMisses_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-misses-phase).

## Legal cache

For a type $\alpha$ of pages and a capacity $k \in \mathbb{N}$, a legal cache
is a list of pages of $\alpha$ with no duplicates and at most $k$ entries.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.LegalCache`, an abbreviation declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#legal-cache).

## FIFO keeps the cache legal on every request sequence

If a list $c$ of pages has no
duplicates and at most $k$ entries, then for every finite request sequence $\sigma$ the cache
obtained from $c$ by serving the requests of $\sigma$ in order, each with one FIFO step of
capacity $k$, also has no duplicates and at most $k$ entries.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoCache_legal`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-cache-legal).

## FIFO paging as an online pager

The online pager with capacity $k$ whose states are the
legal caches of capacity $k$ (lists of at most $k$ distinct pages, oldest first), whose initial
state is the empty cache, whose cache in a state is that list itself, and which serves a request
$p$ by one FIFO step with capacity $k$.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoPager`, a definition declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-pager).

## FIFO as an online pager misses as often as the FIFO step policy

For every legal cache
$q$ of capacity $k$ (at most $k$ distinct pages) and every request sequence $\sigma$, the number
of misses of the FIFO online pager started in $q$ and serving $\sigma$ equals the number of misses
of the policy given by the FIFO step with capacity $k$ serving $\sigma$ from the cache $q$.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoPager_misses`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-pager-misses).

## FIFO is `k`-competitive

**FIFO is `k`-competitive** (Sleator and Tarjan). Let $k \ge 1$, and let $\tau$ be a legal
trace of the caching system with capacity $k$ that starts from a cache $c_0$ of at most $k$
distinct pages; let $m$ be its number of misses. Then the FIFO online pager with capacity $k$,
started in any legal cache (at most $k$ distinct pages) and serving the requests of $\tau$ in
order, misses at most $k m + k$ times.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoMisses_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-misses-le).

## FIFO is `k`-competitive against the offline optimum

Let $k \ge 1$, let $\sigma$ be a
finite request sequence, and let $c_0$ be a list of at most $k$ distinct pages. Let $m$ be the
number of misses of the furthest-in-future manager with capacity $k$ serving $\sigma$ from the
cache $c_0$. Then the FIFO online pager with capacity $k$, started in any legal cache (at most
$k$ distinct pages), misses at most $k m + k$ of the requests of $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifoMisses_le_furthestInFuture`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-misses-le-furthest-in-future).

## The ratio `k` is tight for FIFO

Let $k \ge 1$ and let $c$ and $d$ be natural numbers
with $c < k d$. For every natural number $b$ there is a finite request sequence $\sigma$ over
$k + 1$ pages with $c \cdot m + b < d \cdot f$, where $m$ is the number of misses of the
furthest-in-future manager with capacity $k$ serving $\sigma$ from the empty cache, and $f$ is
the number of misses of the FIFO online pager with capacity $k$ serving $\sigma$ from its initial,
empty cache.

So no ratio $c / d < k$ makes FIFO $c / d$-competitive, whatever the additive constant.

Formalized by `Cslib.Algorithms.Lean.Online.FifoPaging.fifo_not_competitive_of_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/Online/FifoPaging.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Online/FifoPaging.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html#fifo-not-competitive-of-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Competitive paging](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/online-algorithms/competitive-paging/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/online-algorithms/competitive-paging)
