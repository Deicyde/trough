---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.OfflineCaching.CacheEvent, Cslib.Algorithms.Lean.OfflineCaching.cacheLTS, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_nil, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_cons, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_legal, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_zero_capacity, Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_min_misses
statement: formalized
proof: formalized
---

# Furthest-in-future caching

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html).

## Offline Caching

## Cache events

A cache event over a type $\alpha$ of blocks records how one request is
served: either a hit on the requested block $r \in \alpha$, or a miss on the requested block $r$
together with an optional evicted block $v \in \alpha$, absent when nothing is evicted.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.CacheEvent`, an inductive type declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#cache-event).

## Legal cache transitions

For a capacity $k \in \mathbb{N}$, this is the labelled
transition system whose states are lists of blocks (the cache contents, in any order) and whose
labels are cache events. Write $|C|$ for the length of a list $C$, $x :: C$ for $C$ with $x$
prepended, and $C \setminus v$ for $C$ with the first occurrence of $v$ removed. There is a
transition from $C$ to $C'$ labelled by a hit on $r$ when $r \in C$ and $C'$ is a permutation of
$C$; labelled by a miss on $r$ with no eviction when $r \notin C$ and either $k = 0$ and $C$ and
$C'$ are both empty, or $|C| < k$ and $C'$ is a permutation of $r :: C$; and labelled by a miss on
$r$ evicting $v$ when $k > 0$, $r \notin C$, $|C| = k$, $v \in C$ and $C'$ is a permutation of
$r :: (C \setminus v)$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.cacheLTS`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#cache-lts).

## Furthest-in-future caching

Given a capacity $k$, a sequence of requested pages and an
initial cache (a list of pages), the furthest-in-future manager serves the requests in order
and returns the list of emitted cache events together with the final cache. A request for a
page $r$ already in the cache is a hit and leaves the cache unchanged. Otherwise it is a miss:
if $k = 0$, nothing is evicted and the cache becomes empty; if the cache holds fewer than $k$
pages, nothing is evicted and $r$ is added at the front; otherwise the manager evicts the cached
page whose next occurrence among the later requests is furthest away (a page never requested
again counts as infinitely far, and ties go to the page listed first in the cache), removes it
and adds $r$ at the front.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future).

## Furthest-in-future on no requests

For every capacity $k$ and every list $C$ of blocks,
the furthest-in-future manager with capacity $k$ on the empty request list from the initial
cache $C$ emits no events and ends with the cache $C$, unchanged.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-nil).

## One step of the furthest-in-future manager

Write $x :: L$ for the list $L$ with $x$
prepended, $[\,]$ for the empty list, $|L|$ for the length of $L$, and $L \setminus v$ for $L$
with the first occurrence of $v$ removed. Write $\mathrm{FIF}_k(R, C) = (E, D)$ when the
furthest-in-future manager with capacity $k$ on the requests $R$ from the initial cache $C$ emits
the events $E$ and ends with the cache $D$. Write $\mathrm{hit}(r)$ for a hit on $r$,
$\mathrm{miss}(r)$ for a miss on $r$ with no eviction, and $\mathrm{miss}(r, v)$ for a miss on
$r$ evicting $v$. Let $C$ be a duplicate-free list of blocks with $|C| \le k$, let $r$ be a block
and $f$ a list of blocks, and for a block $b$ let $\nu(b) \in \mathbb{N} \cup \{\infty\}$ be the
position of the first occurrence of $b$ in $f$, or $\infty$ if $b$ does not occur in $f$.
If $r \in C$, then $\mathrm{FIF}_k(r :: f, C) = (\mathrm{hit}(r) :: E, D)$ where
$(E, D) = \mathrm{FIF}_k(f, C)$. If $k = 0$, then
$\mathrm{FIF}_k(r :: f, C) = (\mathrm{miss}(r) :: E, D)$ where $(E, D) = \mathrm{FIF}_k(f, [\,])$.
If $r \notin C$ and $|C| < k$, then $\mathrm{FIF}_k(r :: f, C) = (\mathrm{miss}(r) :: E, D)$
where $(E, D) = \mathrm{FIF}_k(f, r :: C)$. If $r \notin C$, $k > 0$ and $|C| = k$, and $v$ is
the first entry of $C$ at which $\nu$ is maximal on $C$, then
$\mathrm{FIF}_k(r :: f, C) = (\mathrm{miss}(r, v) :: E, D)$ where
$(E, D) = \mathrm{FIF}_k(f, r :: (C \setminus v))$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-cons).

## The furthest-in-future manager produces legal traces

Let $k$ be a capacity, $R$ a list
of requested blocks and $C$ a duplicate-free list of blocks of length at most $k$. Let $E$ be the
events and $D$ the final cache produced by the furthest-in-future manager with capacity $k$ on
$R$ from the initial cache $C$. Then $E$ leads from $C$ to $D$ by legal cache transitions for
capacity $k$, the blocks requested by the events of $E$ are, in order, exactly $R$, and $D$ is
duplicate-free of length at most $k$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_legal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-legal).

## Furthest-in-future caching with zero capacity

Run with capacity $0$ on a request
sequence $r_1, \dots, r_n$ from the empty cache, the furthest-in-future manager emits exactly
the events $\mathrm{miss}(r_1), \dots, \mathrm{miss}(r_n)$, one miss per request in order and
each evicting no page, and its final cache is empty.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_zero_capacity`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-zero-capacity).

## Optimality of furthest-in-future caching

Let $k$ be a capacity, $R$ a list of requested
blocks and $C$ a duplicate-free list of blocks of length at most $k$. Let $E'$ be any list of
cache events that leads from $C$ to some final cache by legal cache transitions for capacity $k$
and whose events request, in order, exactly the blocks of $R$. Then the furthest-in-future
manager with capacity $k$ on $R$ from the initial cache $C$ emits at most as many miss events as
$E'$ contains.

Legal transitions may reorder the list representing the cache, so a competing trace need not
keep the manager's order.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_min_misses`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-min-misses).

## Page served by a cache event

The page served by a cache event is the page it requests,
whether the event is a hit or a miss.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.CacheEvent.request`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#request).

## Miss indicator

The miss indicator of a cache event is true if the event is a miss and
false if it is a hit.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.CacheEvent.isMiss`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#is-miss).

## Number of misses in a trace

The number of misses of a finite list of cache events is the
number of events in the list that are misses.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.misses`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#misses).

## Legal cache transitions preserve valid caches

Let $k$ be a capacity and let $C \to C'$
be a legal cache transition for capacity $k$, labelled by any cache event. If $C$ has no
duplicate entries and length at most $k$, then $C'$ has no duplicate entries and length at
most $k$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.cacheLTS_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#cache-lts-valid).

## Legal cache traces preserve valid caches

Let $k$ be a capacity and suppose a finite
sequence of cache events leads from the cache $C$ to the cache $C'$ by legal cache transitions
for capacity $k$. If $C$ has no duplicate entries and length at most $k$, then $C'$ has no
duplicate entries and length at most $k$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.cacheLTS_mtr_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 719](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L719). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#cache-lts-mtr-valid).

## A legal step caches the served page

Let $k > 0$ be a capacity. If a legal transition for
capacity $k$ takes a cache $C$ to a cache $C'$ by a cache event, then the page served by that
event lies in $C'$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.request_mem_of_tr`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#request-mem-of-tr).

## A legal trace without misses serves only cached pages

Let $k$ be a capacity. If a legal
trace of cache events for capacity $k$ starts from a cache $C$ and contains no miss, then every
page served by an event of the trace lies in $C$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.request_mem_of_misses_eq_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#request-mem-of-misses-eq-zero).

## A legal trace misses at least once

Let $k$ be a capacity and $C$ a cache listing at most
$k$ pages, and consider a legal trace of cache events for capacity $k$ that starts from $C$. Let
$p$ be a page in $C$. If at least $k + 1$ distinct pages are each equal to $p$ or served by some
event of the trace, then the trace contains at least one miss.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.one_le_misses`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#one-le-misses).

## Furthest-in-future caching has the fewest misses

Let $k$ be a capacity, $R$ a list of
requested blocks and $C$ a duplicate-free list of blocks of length at most $k$. Let $E'$ be any
list of cache events that leads from $C$ to some final cache by legal cache transitions for
capacity $k$ and whose events serve, in order, exactly the blocks of $R$. Then the number of
misses among the events emitted by the furthest-in-future manager with capacity $k$ on $R$ from
the initial cache $C$ is at most the number of misses of $E'$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_misses_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-misses-le).

## Furthest-in-future serves exactly the requests

Let $k$ be a capacity, $R$ a list of
requested blocks and $C$ a duplicate-free list of blocks of length at most $k$. Then the events
emitted by the furthest-in-future manager with capacity $k$ on $R$ from the initial cache $C$
serve, in order, exactly the blocks of $R$.

Formalized by `Cslib.Algorithms.Lean.OfflineCaching.furthestInFuture_requests`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean, line 803](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Greedy/OfflineCaching.lean#L803). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html#furthest-in-future-requests).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Furthest-in-future caching](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/greedy-algorithms-and-matroids/furthest-in-future-caching)
