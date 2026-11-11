---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.OpenAddressing, Cslib.Algorithms.Lean.OpenAddressing.linearProbe, Cslib.Algorithms.Lean.OpenAddressing.doubleHashProbe, Cslib.Algorithms.Lean.OpenAddressing.empty, Cslib.Algorithms.Lean.OpenAddressing.lookupAux, Cslib.Algorithms.Lean.OpenAddressing.lookup, Cslib.Algorithms.Lean.OpenAddressing.insertAux, Cslib.Algorithms.Lean.OpenAddressing.insert
statement: formalized
proof: formalized
---

# Open addressing

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html).

## Open Addressing

## Open-addressing hash table

Let $K$ be a type of keys, $V$ a type of values, $m$ a natural
number, and $p$ a probe sequence assigning to each key $k$ and each $i \in \mathbb{N}$ a slot
$p(k, i) \in \{0, \dots, m - 1\}$. An open-addressing hash table with $m$ slots and probe
sequence $p$ consists of $m$ slots, each either empty or holding a single pair $(k, v)$ with
$k \in K$ and $v \in V$.

No expected constant-time bound is claimed because the model supplies neither a probability
distribution nor a uniform-hashing assumption about the probe sequence.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#open-addressing).

## Linear-probing probe sequence

Given a hash function $h : K \to \mathbb{N}$ and a
number of slots $m > 0$, the $i$-th probe of a key $k$ is the slot $(h(k) + i) \bmod m$ in
$\{0, \dots, m - 1\}$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.linearProbe`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#linear-probe).

## Double-hashing probe sequence

Given hash functions $h_1, h_2 : K \to \mathbb{N}$ and a
number of slots $m > 0$, the $i$-th probe of a key $k$ is the slot
$(h_1(k) + i \cdot h_2(k)) \bmod m$ in $\{0, \dots, m - 1\}$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.doubleHashProbe`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#double-hash-probe).

## Empty open-addressing table

The open-addressing table with $m$ slots and a given probe
sequence in which every slot is empty.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#empty).

## Bounded lookup scan

Given a table with $m$ slots and probe sequence $p$, a key $k$, a
starting index $s$ and a budget $f$ of probes, examine the slots $p(k, s), p(k, s + 1), \dots$ in
order, for at most $f$ probes. The scan returns the value bound to $k$ in the first examined slot
that holds a binding for $k$, and returns no value if it first reaches an empty slot or exhausts
the budget.

This is the helper behind lookup, which starts at index $0$ with budget $m$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookupAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-aux).

## Lookup in an open-addressing table

Let $T$ be an open-addressing hash table with $m$ slots
and probe sequence $p$, and let $k$ be a key. The lookup of $k$ in $T$ inspects the slots
$p(k, 0), p(k, 1), \dots, p(k, m - 1)$ in this order. It returns the value $v$ of the first
inspected slot that holds a pair $(k, v)$, and returns nothing if an empty slot is inspected
first or if none of the $m$ inspected slots holds the key $k$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup).

## Bounded insertion scan

Given a table with $m$ slots and probe sequence $p$, a key $k$, a
value $v$, a starting index $s$ and a budget $f$ of probes, examine the slots
$p(k, s), p(k, s + 1), \dots$ in order, for at most $f$ probes. At the first examined slot that
is empty or holds a binding for $k$, the scan returns the table with that slot overwritten by the
binding $k \mapsto v$ and every other slot unchanged; if all $f$ examined slots hold bindings for
other keys (in particular if $f = 0$), it fails and returns no table.

This is the helper behind insertion, which starts at index $0$ with budget $m$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.insertAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#insert-aux).

## Insertion into an open-addressing table

To insert the binding $k \mapsto v$ into a table
with $m$ slots and probe sequence $p$, examine the slots $p(k, 0), p(k, 1), \dots, p(k, m - 1)$
in order. At the first one that is empty or already holds a binding for $k$, write $k \mapsto v$
there, leaving every other slot unchanged, and return the updated table. If all $m$ examined
slots hold bindings for other keys, the insertion fails and returns no table.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#insert).

## Valid open-addressing tables

Let $T$ be an open-addressing table with $m$ slots and probe
sequence $p$, where $p(k, i) \in \{0, \dots, m - 1\}$ is the slot visited by the $i$-th probe of
key $k$. Then $T$ is valid when it satisfies two conditions. Probe-closedness: whenever slot $j$
holds a binding $k \mapsto v$, there is an $i < m$ with $p(k, i) = j$ such that the slots
$p(k, i')$ are occupied for all $i' < i$; this is what lets a lookup stop at the first empty
slot. Key uniqueness: if slots $j_1$ and $j_2$ hold bindings with the same key $k$, then
$j_1 = j_2$; so each key has at most one binding and insertion genuinely replaces it.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#valid).

## Stored binding in an open-addressing table

An open-addressing hash table $T$ stores the
binding $k \mapsto v$ when some slot of $T$ holds the pair $(k, v)$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.Stored`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#stored).

## The empty open-addressing table is valid

For all types $K$ and $V$, every number of
slots $m$ and every probe sequence $p$, which assigns to each key $k$ and each $i \in \mathbb{N}$
a slot $p(k, i) \in \{0, \dots, m - 1\}$, the empty table with $m$ slots and probe sequence $p$,
in which every slot is vacant, is valid: it is probe-closed and no key is stored in two
different slots.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#valid-empty).

## Lookup in the empty open-addressing table

For every key $k$, looking up $k$ in the empty
open-addressing table returns no value.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-empty).

## Lookup after a successful open-addressing insertion

If inserting the binding $k \mapsto v$
into an open-addressing hash table $T$ succeeds and yields the table $T'$, then looking up $k$
in $T'$ returns $v$. No validity assumption on $T$ is needed.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-insert).

## Insertion preserves validity of an open-addressing table

Let $T$ be a valid table with $m$
slots and probe sequence $p$, whose keys have decidable equality. If inserting the binding
$k \mapsto v$ into $T$ (adding it, or replacing the binding already stored for $k$) succeeds and
returns the table $T'$, then $T'$ is valid: it is probe-closed and no key is stored in two
different slots.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#valid-insert).

## Open-addressing lookup returns only stored bindings

If looking up a key $k$ in an
open-addressing hash table $T$ returns the value $v$, then $T$ stores the binding $k \mapsto v$.
No validity assumption is needed.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.stored_of_lookup_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#stored-of-lookup-eq-some).

## Lookup of an absent key fails

Let $T$ be an open-addressing table and $k$ a key such that
no slot of $T$ stores a binding $k \mapsto v$ for any value $v$. Then looking up $k$ in $T$ returns
no value. No validity assumption on $T$ is needed.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_eq_none_of_not_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-eq-none-of-not-stored).

## Valid open-addressing tables find every stored key

If a valid open-addressing hash table
$T$ stores the binding $k \mapsto v$, then looking up $k$ in $T$ returns some value.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_isSome_of_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-is-some-of-stored).

## Open-addressing lookup succeeds exactly on stored keys

Let $T$ be a valid open-addressing
hash table and $k$ a key. Looking up $k$ in $T$ returns a value if and only if $T$ stores a
binding $k \mapsto v$ for some value $v$.

This membership characterization is used in place of a finite-map abstraction of the table.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_isSome_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-is-some-iff).

## Bindings in a valid open-addressing table are unique

If a valid open-addressing hash
table $T$ stores both $k \mapsto v_1$ and $k \mapsto v_2$, then $v_1 = v_2$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.stored_unique`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#stored-unique).

## Lookup in a valid table returns exactly the stored binding

Let $T$ be a valid
open-addressing table, $k$ a key and $v$ a value. Then looking up $k$ in $T$ returns $v$ if and
only if the binding $k \mapsto v$ is stored in some slot of $T$.

Together with the fact that lookup after a successful insertion of $k \mapsto v$ returns $v$, this
says that a successful insertion really replaces the old binding: no other value for $k$ remains
stored afterwards.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 709](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-eq-some-iff).

## Open-addressing insertion leaves other keys' bindings unchanged

Let $T$ be an
open-addressing hash table, and suppose that inserting the binding $k \mapsto v$ into $T$
succeeds and yields the table $T'$. Then for every key $k' \neq k$ and every value $v'$, the
table $T'$ stores $k' \mapsto v'$ if and only if $T$ stores $k' \mapsto v'$.

No validity assumption is needed: the insertion writes a single slot, previously empty or
previously holding $k$, and leaves every other slot unchanged.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.stored_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#stored-insert-of-ne).

## Insertion does not affect lookups of other keys

Let $T$ be a valid open-addressing table and
suppose inserting the binding $k \mapsto v$ into $T$ succeeds with result $T'$. Then for every key
$k' \ne k$, looking up $k'$ in $T'$ gives the same result as looking up $k'$ in $T$.

Together with the fact that looking up $k$ in $T'$ returns $v$, this is the map-update
specification of insertion, matching the corresponding statement for separate chaining.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#lookup-insert-of-ne).

## Failed open-addressing insertion finds every probed slot taken

Let $T$ be an
open-addressing hash table with $m$ slots and probe sequence $p$. If inserting a binding
$k \mapsto v$ into $T$ fails, then for every $i < m$ the slot $p(k, i)$ holds a pair
$(k', v')$ with $k' \neq k$.

For probe sequences that are permutations of the slots, this says that every slot of the table
holds a key other than $k$.

Formalized by `Cslib.Algorithms.Lean.OpenAddressing.occupied_of_insert_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean, line 807](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/OpenAddressing.lean#L807). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html#occupied-of-insert-eq-none).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Open addressing](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/open-addressing/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/hashing/open-addressing)
