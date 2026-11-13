---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.PerfectHashing, Cslib.Algorithms.Lean.PerfectHashing.lookup, Cslib.Algorithms.Lean.PerfectHashing.empty, Cslib.Algorithms.Lean.PerfectHashing.Stored, Cslib.Algorithms.Lean.PerfectHashing.entries, Cslib.Algorithms.Lean.PerfectHashing.Valid, Cslib.Algorithms.Lean.PerfectHashing.Valid.injective_of_placed, Cslib.Algorithms.Lean.PerfectHashing.Valid.mk_of_placed
statement: formalized
proof: formalized
---

# Perfect hashing

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html).

## Perfect Hashing

## Two-level perfect hash table

Fix a type $\alpha$ of keys, a type $\beta$ of values and a
primary hash function $h : \alpha \to \mathbb{N}$. A two-level (FKS) perfect hash table consists
of a number $b > 0$ of buckets and, for each bucket $i < b$, a secondary size $m_i \in \mathbb{N}$,
a secondary hash function $h_i : \alpha \to \mathbb{N}$ and a secondary table of $m_i$ slots, each
of which is empty or holds one binding $(k, v)$ with $k \in \alpha$ and $v \in \beta$.

The intended position of a key $k$ is slot $h_i(k) \bmod m_i$ of bucket $i = h(k) \bmod b$. The
structure itself imposes no condition on the hash functions and does not require bindings to sit
at their intended positions; that requirement is the separate validity condition.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#perfect-hashing).

## Lookup in a perfect hash table

To look up a key $k$ in a two-level perfect hash table with
$b$ buckets, primary hash $h$, secondary sizes $m_i$ and secondary hashes $h_i$, let
$i = h(k) \bmod b$. If $m_i = 0$, the lookup returns nothing. Otherwise it inspects the single slot
$h_i(k) \bmod m_i$ of the secondary table of bucket $i$: if that slot holds a binding $(k, v)$, the
lookup returns $v$; if the slot is empty or holds a binding with a different key, the lookup
returns nothing.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#lookup).

## Empty perfect hash table

Given a primary hash function $h$ from keys to natural
numbers, a number of buckets $b > 0$, and for each bucket $i < b$ a secondary table size $m_i$
and a secondary hash function $h_i$, the empty table is the two-level perfect hash table with
primary hash $h$, $b$ buckets, secondary sizes $m_i$ and secondary hashes $h_i$ in which every
slot of every secondary table is vacant.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#empty).

## Bindings stored in a perfect hash table

A key $k$ and a value $v$ are stored in a
two-level perfect hash table $T$ when some secondary slot, in some bucket of $T$, holds the
binding $(k, v)$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.Stored`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#stored).

## Entries of a perfect hash table

The entries of a two-level perfect hash table form
the list of the bindings $(k, v)$ held in its occupied secondary slots, listed bucket by bucket
in increasing bucket order and, within each bucket, in increasing slot order.

A pair $(k, v)$ is a member of this list exactly when it is held in some slot of the table.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.entries`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#entries).

## Valid perfect hash table

Let $T$ be a two-level perfect hash table with primary hash $h$,
$b$ buckets, secondary table sizes $m_i$ and secondary hashes $g_i$. Then $T$ is valid when two
conditions hold. Placement: whenever slot $j$ of bucket $i$ holds a binding $(k, v)$, we have
$i = h(k) \bmod b$ and $j = g_i(k) \bmod m_i$. Injectivity: for every bucket $i$, if keys $k_1$
and $k_2$ both occur in bindings stored in bucket $i$ and $g_i(k_1) \bmod m_i = g_i(k_2) \bmod m_i$,
then $k_1 = k_2$.

The injectivity condition follows from placement. It is recorded separately because choosing
secondary hash functions that are injective on each bucket's keys is the task of the FKS
construction.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.Valid`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#valid).

## Placement implies secondary injectivity

Let $T$ be a two-level perfect hash table
with $b$ buckets and primary hash $h$, and for each bucket $i$ let $m_i$ be its secondary table
size and $h_i$ its secondary hash. Suppose every binding $(k, v)$ held in slot $j$ of bucket $i$
satisfies $h(k) \bmod b = i$ and $j = h_i(k) \bmod m_i$. Then for every bucket $i$ and all keys
$k_1, k_2$ that are each held, with some value, in some slot of bucket $i$, if
$h_i(k_1) \bmod m_i = h_i(k_2) \bmod m_i$, then $k_1 = k_2$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.Valid.injective_of_placed`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#injective-of-placed).

## Placement suffices for validity of a perfect hash table

Let $T$ be a two-level perfect
hash table with $b$ buckets, primary hash $h$, secondary sizes $m_i$ and secondary hashes $h_i$.
If, whenever slot $j$ of the secondary table of bucket $i$ holds a binding $(k, v)$, we have
$h(k) \bmod b = i$ and $j = h_i(k) \bmod m_i$, then $T$ is valid.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.Valid.mk_of_placed`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#mk-of-placed).

## Entries of a perfect hash table are its stored bindings

For every two-level perfect hash
table, every key $k$ and every value $v$, the pair $(k, v)$ belongs to the list of entries of the
table (the contents of its occupied secondary slots, bucket by bucket) if and only if some
secondary slot of the table holds the binding $(k, v)$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.mem_entries_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#mem-entries-iff).

## The empty perfect hash table is valid

For every primary hash function, every positive
number of buckets, and every choice of secondary table sizes and secondary hash functions, the
empty two-level perfect hash table with these parameters is valid: no slot is occupied, so both
conditions of validity hold vacuously.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#valid-empty).

## The empty perfect hash table stores nothing

For every primary hash function, every number
$b > 0$ of buckets, every choice of secondary sizes and secondary hash functions, every key $k$
and every value $v$, no secondary slot of the empty two-level perfect hash table with these data
holds the binding $(k, v)$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.not_stored_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#not-stored-empty).

## Soundness of perfect-hash lookup

For a two-level perfect hash table with decidable equality
on keys, and with no validity hypothesis, if looking up a key $k$ returns a value $v$, then some
secondary slot of the table holds the binding $(k, v)$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.stored_of_lookup_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#stored-of-lookup-eq-some).

## Lookup finds every stored binding

For a valid two-level perfect hash table, if the
binding $(k, v)$ is held in some slot of the table, then looking up $k$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.lookup_eq_some_of_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#lookup-eq-some-of-stored).

## Stored values in a valid perfect hash table are unique

In a valid two-level perfect hash
table, if some secondary slots hold bindings $(k, v_1)$ and $(k, v_2)$ with the same key $k$, then
$v_1 = v_2$.

This is a direct consequence of placement (both bindings would occupy the one slot their shared
key hashes to), so it needs no decidable equality on keys.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.stored_unique`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#stored-unique).

## Lookup fails exactly on unstored keys

For a valid two-level perfect hash table and
any key $k$, looking up $k$ returns no value if and only if there is no value $v$ such that the
binding $(k, v)$ is held in some slot of the table.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.lookup_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#lookup-eq-none-iff).

## Lookup finds every entry

For a valid two-level perfect hash table, if the pair
$(k, v)$ belongs to the list of entries of the table, then looking up $k$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.lookup_eq_some_of_mem_entries`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#lookup-eq-some-of-mem-entries).

## Successful perfect-hash lookups return entries

For a two-level perfect hash table with
decidable equality on keys, if looking up a key $k$ returns a value $v$, then $(k, v)$ belongs to
the list of entries of the table. No validity hypothesis is needed.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.mem_entries_of_lookup_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#mem-entries-of-lookup-eq-some).

## Lookup in the empty perfect hash table fails

For every primary hash function, every
number of buckets $b > 0$, all secondary table sizes and secondary hash functions, and every
key $k$, looking up $k$ in the empty table returns no value.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#lookup-empty).

## The empty perfect hash table has no entries

For every primary hash function, every
number of buckets $b > 0$, and all secondary table sizes and secondary hash functions, the list
of entries of the empty table is the empty list.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.entries_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#entries-empty).

## Occupancy of a perfect-hashing bucket

For a two-level perfect hash table and a bucket
$i$, the occupancy $n_i$ of bucket $i$ is the number of slots of the secondary table of bucket
$i$ that hold a binding. It is the $n_i$ of the Fredman–Komlós–Szemerédi analysis.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.bucketSize`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#bucket-size).

## Total number of keys of a perfect hash table

For a two-level perfect hash table, write
$n_i$ for the number of occupied secondary slots of bucket $i$. The total number of keys of the
table is $\sum_i n_i$, the number of occupied secondary slots over all buckets.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.totalKeys`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#total-keys).

## Total secondary space of a perfect hash table

For a two-level perfect hash table, write
$m_i$ for the number of slots of the secondary table of bucket $i$. The total secondary space of
the table is $\sum_i m_i$, the number of secondary slots over all buckets.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.totalSecondarySpace`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#total-secondary-space).

## FKS square sizing rule

A two-level perfect hash table with $b$ buckets is square-sized when,
for every bucket $i < b$, the size $m_i$ of its secondary table equals $n_i^2$, where $n_i$ is the
number of occupied slots of that secondary table.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.SquareSized`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#square-sized).

## Bucket occupancy is at most the secondary table size

For every two-level perfect
hash table and every bucket $i$, the number $n_i$ of occupied slots of bucket $i$ is at most
the number $m_i$ of slots of the secondary table of bucket $i$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.bucketSize_le_secondarySize`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#bucket-size-le-secondary-size).

## Each secondary table fits in the total secondary space

In a two-level perfect hash table
with $b$ buckets and secondary sizes $m_0, \dots, m_{b-1}$, every bucket $i < b$ satisfies
$m_i \le \sum_{j < b} m_j$, the total secondary space.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.secondarySize_le_totalSecondarySpace`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#secondary-size-le-total-secondary-space).

## Total secondary space under square sizing

Let $T$ be a two-level perfect hash table
satisfying the FKS sizing rule, and write $n_i$ for the number of occupied secondary slots of
bucket $i$. Then the total secondary space of $T$ equals $\sum_i n_i^2$, the sum over all
buckets $i$.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.totalSecondarySpace_eq_sum_sq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#total-secondary-space-eq-sum-sq).

## Quadratic space bound under square sizing

If a two-level perfect hash table satisfies the
FKS sizing rule, then its total secondary space is at most the square of its total number of
keys.

This is weaker than the linear space bound of Fredman, Komlós and Szemerédi, which also depends
on the choice of a good primary hash function.

Formalized by `Cslib.Algorithms.Lean.PerfectHashing.totalSecondarySpace_le_totalKeys_sq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/PerfectHashing.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html#total-secondary-space-le-total-keys-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect hashing](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/perfect-hashing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/hashing/perfect-hashing)
