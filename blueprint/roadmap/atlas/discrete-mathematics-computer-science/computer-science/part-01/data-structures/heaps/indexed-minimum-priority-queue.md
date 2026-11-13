---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.IndexedMinQueue.IndexedMinQueue, Cslib.Algorithms.Lean.IndexedMinQueue.empty, Cslib.Algorithms.Lean.IndexedMinQueue.member, Cslib.Algorithms.Lean.IndexedMinQueue.insert, Cslib.Algorithms.Lean.IndexedMinQueue.decreaseKey, Cslib.Algorithms.Lean.IndexedMinQueue.extractMin, Cslib.Algorithms.Lean.IndexedMinQueue.position_valid, Cslib.Algorithms.Lean.IndexedMinQueue.position_eq_none_iff
statement: formalized
proof: formalized
---

# Indexed minimum priority queue

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html).

## Indexed minimum queue

Let $W$ be a linearly ordered type, let $W \cup \{\top\}$ be $W$
with a new greatest element $\top$ adjoined, and let $n$ be a natural number. An indexed
minimum queue over the identities $0, \dots, n-1$ consists of a binary min-heap whose entries are
pairs $(k, v)$ of a key $k \in W \cup \{\top\}$ and an identity $v < n$, ordered lexicographically
(first by key, then by identity), together with a position vector assigning to each identity
$v < n$ either nothing or an index $i < n$. It is required that the heap has at most $n$ entries
and that, for all identities $v < n$ and indices $i < n$, the position of $v$ is $i$ exactly
when $i$ is a slot of the heap whose entry has identity $v$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.IndexedMinQueue`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#indexed-min-queue).

## Empty indexed minimum queue

For every linearly ordered type $W$ and every natural number
$n$, the empty indexed minimum queue over the identities $0, \dots, n-1$, with keys in $W$ with a
new greatest element adjoined, has the empty min-heap and a position vector that assigns nothing
to each of the $n$ identities, so no identity is present.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#empty).

## Membership test in an indexed minimum queue

Costs are counted as five event counts:
comparisons, swaps, reads of the position vector, writes to the position vector, and entry
appends, pops or replacements. For an indexed minimum queue $q$ over the identities
$0, \dots, n-1$ and an identity $v < n$, the membership test returns true exactly when the
position vector of $q$ assigns an index to $v$, and its cost is one position read and no other
event.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.member`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#member).

## Insertion into an indexed minimum queue

Let $W$ be a linearly ordered type and let
$W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined. Costs are counted as five
event counts: comparisons, swaps, reads of the position vector, writes to the position vector,
and entry appends, pops or replacements. Given an indexed minimum queue $q$ over the identities
$0, \dots, n-1$ with keys in $W \cup \{\top\}$, whose heap entries (pairs of a key and an
identity) are ordered lexicographically, first by key and then by identity, an identity $v < n$
and a key $k \in W \cup \{\top\}$, insertion fails (returns nothing) when the position vector of
$q$ assigns an index to $v$, at the cost of one position read. Otherwise it appends the entry
$(k, v)$ at the end of the heap, sets the position of $v$ to that slot, and sifts the entry up:
while it is not at the root and is smaller than its parent, it is swapped with its parent and
the positions of both swapped identities are updated. It returns the resulting queue, at the
cost of one position read, one position write and one entry append, plus one comparison for
each comparison with a parent and one swap and two position writes for each swap.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#insert).

## Decrease-key in an indexed minimum queue

Let $W$ be a linearly ordered type and let
$W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined. Costs are counted as five
event counts: comparisons, swaps, reads of the position vector, writes to the position vector,
and entry appends, pops or replacements. Given an indexed minimum queue $q$ over the identities
$0, \dots, n-1$ with keys in $W \cup \{\top\}$, whose heap entries (pairs of a key and an
identity) are ordered lexicographically, first by key and then by identity, an identity $v < n$
and a finite key $k \in W$, decrease-key fails (returns nothing) when the position vector of $q$
assigns no index to $v$, at the cost of one position read, and when $k$ is not strictly smaller
than the current key of $v$, at the cost of one position read and one comparison. Otherwise it
replaces the entry of $v$ by $(k, v)$ in the same slot and sifts it up: while it is not at the
root and is smaller than its parent, it is swapped with its parent and the positions of both
swapped identities are updated. It returns the resulting queue, at the cost of one position
read, one comparison and one entry replacement, plus one comparison for each comparison with a
parent and one swap and two position writes for each swap.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.decreaseKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#decrease-key).

## Extract-min in an indexed minimum queue

Costs are counted as five event counts:
comparisons, swaps, reads of the position vector, writes to the position vector, and entry
appends, pops or replacements. Given an indexed minimum queue $q$, extract-min fails (returns
nothing) exactly when the heap of $q$ is empty, at zero cost. Otherwise let $(k, v)$ be the root
entry of the heap. If the heap has one entry, extract-min returns $(k, v)$ together with the
queue whose heap is empty and in which $v$ has no position, at the cost of one position write
and one entry pop. If the heap has at least two entries, the root is swapped with the last entry
and the positions of both are updated, the last slot is removed, the position of $v$ is cleared,
and the new root is sifted down: while it has a child, let $c$ be its smaller child (the left
one on ties); if $c$ is smaller than it, the two are swapped and the positions of both are
updated, otherwise the sift stops. It returns $(k, v)$ together with the resulting queue, at the
cost of one swap, three position writes and one entry pop, plus, at each sift-down step, one
comparison between the two children when both exist, one comparison with $c$, and one swap and
two position writes when a swap is made.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.extractMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean, line 552](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Basic.lean#L552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#extract-min).

## Recorded positions lie inside the heap

Let $W$ be a linearly ordered type and let $q$
be an indexed min-queue over $W$ with identities in $\{0, \dots, n-1\}$. If the position
table of $q$ records slot $i$ for an identity $v$, then $i$ is less than the number of
entries currently stored in the heap array of $q$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.position_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#position-valid).

## Absent identities carry no heap entry

Let $q$ be an indexed min queue over a linear
order $W$ with identities in $\{0, \dots, n-1\}$ and let $v$ be an identity. The position
vector of $q$ records no slot for $v$ if and only if no entry of the heap array of $q$ has
identity $v$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.position_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#position-eq-none-iff).

## The empty indexed min queue has no present identity

For every linear order $W$, every
$n$ and every identity $v \in \{0, \dots, n-1\}$, the position vector of the empty indexed min
queue over $W$ with identities in $\{0, \dots, n-1\}$ records no slot for $v$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.empty_position`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#empty-position).

## Insertion fails exactly on present identities

Let $q$ be an indexed min queue over a
linear order $W$ with identities in $\{0, \dots, n-1\}$, let $v$ be an identity and let
$k \in W \cup \{\top\}$. Inserting $v$ with key $k$ into $q$ returns no queue if and only if
the position vector of $q$ records a slot for $v$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.insert_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#insert-eq-none-iff).

## Extraction from an indexed min queue fails exactly when it is empty

Let $q$ be an
indexed min queue over a linear order $W$ with identities in $\{0, \dots, n-1\}$. Extracting
the minimum of $q$ returns no result if and only if the heap array of $q$ has size $0$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.extractMin_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#extract-min-eq-none-iff).

## Membership reads the position vector

Let $q$ be an indexed min queue over a linear
order $W$ with identities in $\{0, \dots, n-1\}$ and let $v$ be an identity. The membership
test for $v$ in $q$ returns true if and only if the position vector of $q$ records a slot for
$v$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.member_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#member-ret).

## Membership costs one position read

Let $q$ be an indexed min queue over a linear
order $W$ with identities in $\{0, \dots, n-1\}$ and let $v$ be an identity. The cost of the
membership test for $v$ in $q$, counted in five event classes (comparisons, swaps,
position-vector reads, position-vector writes, and entry appends, pops or replacements), is
exactly one position-vector read and no event of any other class.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.member_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#member-time).

## Successful insertion into an indexed min queue

Let $q$ be an indexed min queue over a
linear order $W$ with identities in $\{0, \dots, n-1\}$, let $v$ be an identity and let
$k \in W \cup \{\top\}$, and suppose that inserting $v$ with key $k$ into $q$ returns the
queue $q'$. Then the heap of $q'$ is the binary min-heap push of the entry $(k, v)$ onto the
heap of $q$; the position vector of $q'$ records a slot $i$ for $v$, with $i$ less than the
size of the heap array of $q'$, and that array holds $(k, v)$ at index $i$; and every identity
$w \neq v$ has a recorded slot in $q'$ if and only if it has one in $q$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.insert_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#insert-ret).

## Decrease-key fails exactly on absent identities and non-decreases

Let $q$ be an
indexed min queue over a linear order $W$ with identities in $\{0, \dots, n-1\}$, let $v$ be
an identity and let $k \in W$. Decreasing the key of $v$ to $k$ in $q$ returns no queue if and
only if either the position vector of $q$ records no slot for $v$, or it records a slot $i$
for $v$ with $i$ less than the size of the heap array of $q$ and $k$ is not strictly less, in
$W \cup \{\top\}$, than the key of the heap entry at index $i$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.decreaseKey_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#decrease-key-eq-none-iff).

## Successful decrease-key

Let $q$ be an indexed min queue over a linear order $W$ with
identities in $\{0, \dots, n-1\}$, let $v$ be an identity and let $k \in W$, and suppose that
decreasing the key of $v$ to $k$ in $q$ returns the queue $q'$. Let $a$ be the heap array of
$q$. Then the position vector of $q$ records a slot $i$ for $v$ with $i$ less than the size of
$a$, $k$ is strictly less, in $W \cup \{\top\}$, than the key of the entry $a_i$, and the heap
array of $q'$ is obtained by sifting up from index $i$ the array that agrees with $a$ except
that $a_i$ is replaced by $(k, v)$. Moreover, every identity has a recorded slot in $q'$ if and
only if it has one in $q$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.decreaseKey_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#decrease-key-ret).

## Successful extraction from an indexed min queue

Let $q$ be an indexed min queue over a
linear order $W$ with identities in $\{0, \dots, n-1\}$, and suppose that extracting the
minimum of $q$ returns the heap entry $e = (k, u)$, with key $k \in W \cup \{\top\}$ and
identity $u$, together with the queue $q'$. Then binary min-heap extraction on the heap of $q$
returns $e$ together with the heap of $q'$; the position vector of $q'$ records no slot for
$u$; and every identity $w \neq u$ has a recorded slot in $q'$ if and only if it has one in
$q$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.extractMin_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Correctness.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#extract-min-ret).

## Logarithmic event bound for indexed-queue insertion

Let $W$ be a linearly ordered type
and let $W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined. Let $q$ be an
indexed minimum queue over the identities $0, \dots, n-1$ with keys in $W \cup \{\top\}$ whose
heap has $s$ entries, let $v < n$ be an identity and let $k \in W \cup \{\top\}$ be a key. For
each of the five counted events (comparisons, swaps, position reads, position writes, and entry
appends, pops or replacements), the number of times that event occurs when inserting $v$ with
key $k$ into $q$ is at most $20 (\lfloor \log_2 (s + 1) \rfloor + 1)$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.insert_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#insert-time).

## Logarithmic event bound for indexed-queue decrease-key

Let $W$ be a linearly ordered
type and let $W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined. Let $q$ be an
indexed minimum queue over the identities $0, \dots, n-1$ with keys in $W \cup \{\top\}$ whose
heap has $s$ entries, let $v < n$ be an identity and let $k \in W$ be a key. For each of the five
counted events (comparisons, swaps, position reads, position writes, and entry appends, pops or
replacements), the number of times that event occurs when decreasing the key of $v$ to $k$ in
$q$ is at most $20 (\lfloor \log_2 (s + 1) \rfloor + 1)$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.decreaseKey_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#decrease-key-time).

## Logarithmic event bound for indexed-queue extract-min

Let $q$ be an indexed minimum
queue whose heap has $s$ entries. For each of the five counted events (comparisons, swaps,
position reads, position writes, and entry appends, pops or replacements), the number of times
that event occurs when extracting the minimum of $q$ is at most
$20 (\lfloor \log_2 (s + 1) \rfloor + 1)$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.extractMin_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#extract-min-time).

## Event bound for building an indexed queue by repeated insertion

Let $W$ be a linearly
ordered type and let $W \cup \{\top\}$ be $W$ with a new greatest element $\top$ adjoined. Let
$q_0, \dots, q_n$ be indexed minimum queues over the identities $0, \dots, n-1$ with keys in
$W \cup \{\top\}$, and let $k_0, \dots, k_{n-1}$ be keys in $W \cup \{\top\}$. Suppose $q_0$ is
the empty queue and, for each $i < n$, inserting identity $i$ with key $k_i$ into $q_i$ succeeds
and returns $q_{i+1}$. Then for each of the five counted events (comparisons, swaps, position
reads, position writes, and entry appends, pops or replacements), the total number of times that
event occurs over these $n$ insertions is at most $20 n (\lfloor \log_2 (n + 1) \rfloor + 1)$.

Formalized by `Cslib.Algorithms.Lean.IndexedMinQueue.repeated_insert_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/IndexedMinQueue/Complexity.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html#repeated-insert-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Indexed minimum priority queue](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/heaps/indexed-minimum-priority-queue)
