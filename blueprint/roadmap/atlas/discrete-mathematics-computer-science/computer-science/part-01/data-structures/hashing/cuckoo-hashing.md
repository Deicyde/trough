---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.CuckooHashing, Cslib.Algorithms.Lean.CuckooHashing.empty, Cslib.Algorithms.Lean.CuckooHashing.Valid, Cslib.Algorithms.Lean.CuckooHashing.Stored, Cslib.Algorithms.Lean.CuckooHashing.KeyDet, Cslib.Algorithms.Lean.CuckooHashing.valid_empty, Cslib.Algorithms.Lean.CuckooHashing.keyDet_empty, Cslib.Algorithms.Lean.CuckooHashing.insertAux
statement: formalized
proof: formalized
---

# Cuckoo hashing

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html).

## Cuckoo Hashing

## Cuckoo hash table

Given a type $K$ of keys, a type $V$ of values, a number $m$ of slots,
and two hash functions $h_1, h_2 : K \to \{0, \dots, m - 1\}$, a cuckoo hash table consists of
two tables, each a vector of $m$ slots; every slot is either empty or holds a key–value pair
$(k, v)$ with $k \in K$ and $v \in V$. The structure itself does not require a pair $(k, v)$ to
sit at slot $h_1(k)$ of the first table or at slot $h_2(k)$ of the second.

No expected constant-time bound is claimed because the model supplies neither a probability
distribution nor an independence assumption about the hashes.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#cuckoo-hashing).

## Empty cuckoo hash table

The empty cuckoo hash table has every slot of both tables
vacant.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#empty).

## Placement invariant of a cuckoo hash table

A cuckoo hash table with hash functions
$h_1, h_2$ satisfies the placement invariant when every pair $(k, v)$ in slot $i$ of the first
table has $i = h_1(k)$, and every pair $(k, v)$ in slot $i$ of the second table has
$i = h_2(k)$.

This is what lets lookup check only two slots.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#valid).

## Binding stored in a cuckoo hash table

A key $k$ is stored with value $v$ in a cuckoo hash
table when the pair $(k, v)$ occupies some slot of the first table or some slot of the second
table.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.Stored`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#stored).

## Key determinism of a cuckoo hash table

A cuckoo hash table is key-deterministic when each
key is stored with at most one value: for every key $k$ and values $v_1, v_2$, if the bindings
$k \mapsto v_1$ and $k \mapsto v_2$ are both stored in the table, then $v_1 = v_2$. Duplicate
copies of the same pair are allowed.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.KeyDet`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#key-det).

## The empty cuckoo hash table satisfies the placement invariant

For any hash functions
$h_1, h_2$ into $m$ slots, the empty cuckoo hash table, with every slot of both tables vacant,
satisfies the placement invariant.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#valid-empty).

## The empty cuckoo hash table is key-deterministic

No key is stored with two different
values in the empty cuckoo hash table, vacuously.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.keyDet_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#key-det-empty).

## Cuckoo eviction loop

The eviction loop takes a cuckoo hash table with hash functions $h_1$
and $h_2$, a key–value pair $(k, v)$, a choice of the first or second table, and a natural
number as fuel, and either returns a table or fails. With fuel $0$ it fails. With fuel $n + 1$
and the first table chosen, it writes $(k, v)$ into slot $h_1(k)$ of the first table; if that
slot was empty it returns the resulting table, and otherwise it repeats on the resulting table
with the evicted pair, the second table and fuel $n$. With the second table chosen it does the
same at slot $h_2(k)$ of the second table and continues with the first table.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.insertAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#insert-aux).

## Cuckoo hash table lookup

For a cuckoo hash table $T$ with hash functions $h_1$ and $h_2$ and a
key $k$, the lookup of $k$ in $T$ returns $v$ if slot $h_1(k)$ of the first table holds a pair
$(k, v)$; otherwise it returns $v$ if slot $h_2(k)$ of the second table holds a pair $(k, v)$;
otherwise it returns nothing. No other slot is examined.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup).

## Lookup in the empty cuckoo hash table

Looking up any key in the empty cuckoo hash table
finds no value.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-empty).

## Cuckoo lookup finds a key in its first-table slot

Let $T$ be a cuckoo hash table with hash
functions $h_1$ and $h_2$, let $k$ be a key and $v$ a value. If slot $h_1(k)$ of the first table of
$T$ holds the pair $(k, v)$, then looking up $k$ in $T$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_eq_some_of_table1`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-eq-some-of-table1).

## Cuckoo lookup finds a key in its second-table slot

Let $T$ be a cuckoo hash table with hash
functions $h_1$ and $h_2$, let $k$ be a key and $v$ a value. If slot $h_2(k)$ of the second table
of $T$ holds the pair $(k, v)$ and slot $h_1(k)$ of the first table of $T$ holds no pair whose key
is $k$, then looking up $k$ in $T$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_eq_some_of_table2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-eq-some-of-table2).

## Soundness of cuckoo lookup

Let $T$ be a cuckoo hash table with hash functions $h_1$ and $h_2$,
let $k$ be a key and $v$ a value. If looking up $k$ in $T$ returns $v$, then the binding
$k \mapsto v$ is stored in some slot of the first or the second table of $T$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-sound).

## Cuckoo lookup finds every stored key

Let $T$ be a cuckoo hash table with hash functions $h_1$
and $h_2$ that satisfies the placement invariant, and let $k$ be a key and $v$ a value. If the
binding $k \mapsto v$ is stored in some slot of either table of $T$, then looking up $k$ in $T$
returns some value.

The returned value may differ from $v$ when $k$ is stored with two different values; when $T$
stores each key with at most one value, it is $v$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_isSome_of_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-is-some-of-stored).

## Cuckoo lookup finds every stored binding

Let $T$ be a cuckoo hash table that satisfies
the placement invariant and is key-deterministic. For every key $k$ and value $v$, if the
binding $k \mapsto v$ is stored in $T$, then looking up $k$ in $T$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_eq_some_of_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-eq-some-of-stored).

## Cuckoo lookup finds exactly the stored bindings

Let $T$ be a cuckoo hash table that
satisfies the placement invariant and is key-deterministic. For every key $k$ and value $v$,
looking up $k$ in $T$ returns $v$ if and only if the binding $k \mapsto v$ is stored in $T$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_eq_some_iff_stored`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-eq-some-iff-stored).

## Slot holds a key

A slot of a cuckoo hash table is either empty or holds a pair $(k, v)$ of a
key and a value. For a slot $s$ and a key $k'$, this test is true when $s$ holds a pair whose key
is $k'$, and false when $s$ is empty or holds a pair with a different key.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.slotHasKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#slot-has-key).

## Cuckoo hash insertion

Inserting a key $k$ with value $v$ into a cuckoo hash table with hash
functions $h_1$ and $h_2$, with fuel $n$, either returns a table or fails. If slot $h_1(k)$ of
the first table holds a binding for $k$, that slot is overwritten with $(k, v)$, and slot
$h_2(k)$ of the second table is cleared if it also holds a binding for $k$, so no stale
competing value remains. Otherwise, if slot $h_2(k)$ of the second table holds a binding for
$k$, that slot is overwritten with $(k, v)$. Otherwise the eviction loop runs on $(k, v)$,
starting with the first table, with fuel $n$, and its result is returned. Failure, when the
loop exhausts its fuel, models the rehash trigger of the classical algorithm.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#insert).

## Cuckoo insertion stores the inserted binding

Let $T$ be a cuckoo hash table with hash
functions $h_1$ and $h_2$. If inserting (or replacing) the binding $k \mapsto v$ in $T$ with fuel
$f$ succeeds and returns the table $T'$, then the binding $k \mapsto v$ is stored in some slot of
either table of $T'$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.stored_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#stored-insert).

## Cuckoo insertion preserves the placement invariant

Let $T$ be a cuckoo hash table that
satisfies the placement invariant. If inserting the binding $k \mapsto v$ into $T$ (which
replaces an existing binding for $k$ in place) with some fuel bound succeeds and returns the
table $T'$, then $T'$ satisfies the placement invariant.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#valid-insert).

## Cuckoo insertion preserves key determinism

Let $T$ be a cuckoo hash table that
satisfies the placement invariant and is key-deterministic. If inserting a key $k$ with value
$v$ into $T$ with some fuel succeeds with result $T'$, then $T'$ is key-deterministic. In
particular, replacement leaves no stale copy of $k$ with a different value in the other slot.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.keyDet_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 814](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L814). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#key-det-insert).

## Cuckoo lookup returns an inserted value

Let $T$ be a cuckoo hash table with hash functions
$h_1$ and $h_2$ that satisfies the placement invariant and stores each key with at most one value.
If inserting (or replacing) the binding $k \mapsto v$ in $T$ with fuel $f$ succeeds and returns the
table $T'$, then looking up $k$ in $T'$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 891](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L891). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-insert).

## Cuckoo insertion preserves the bindings of other keys

Let $T$ be a cuckoo hash table with hash
functions $h_1$ and $h_2$ that satisfies the placement invariant. Suppose inserting (or replacing)
the binding $k \mapsto v$ in $T$ with fuel $f$ succeeds and returns the table $T'$. Then for every
key $k' \ne k$ and every value $v'$, the binding $k' \mapsto v'$ is stored in $T'$ if and only if
it is stored in $T$.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.stored_insert_iff_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 963](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L963). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#stored-insert-iff-of-ne).

## Cuckoo insertion leaves lookups of other keys unchanged

Let $T$ be a cuckoo hash table with
hash functions $h_1$ and $h_2$ that satisfies the placement invariant and stores each key with at
most one value. If inserting (or replacing) the binding $k \mapsto v$ in $T$ with fuel $f$ succeeds
and returns the table $T'$, then for every key $k' \ne k$, looking up $k'$ in $T'$ gives the same
result as looking up $k'$ in $T$: either both return nothing or both return the same value.

Formalized by `Cslib.Algorithms.Lean.CuckooHashing.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean, line 1053](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CuckooHashing.lean#L1053). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html#lookup-insert-of-ne).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cuckoo hashing](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/hashing/cuckoo-hashing)
