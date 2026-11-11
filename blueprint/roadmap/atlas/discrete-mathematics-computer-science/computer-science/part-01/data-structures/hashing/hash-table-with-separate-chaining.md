---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.HashTable, Cslib.Algorithms.Lean.HashTable.empty, Cslib.Algorithms.Lean.HashTable.lookup, Cslib.Algorithms.Lean.HashTable.insert, Cslib.Algorithms.Lean.HashTable.Valid, Cslib.Algorithms.Lean.HashTable.abstraction, Cslib.Algorithms.Lean.HashTable.valid_empty, Cslib.Algorithms.Lean.HashTable.lookup_empty
statement: formalized
proof: formalized
---

# Hash table with separate chaining

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html).

## Hash Table

## Hash table with separate chaining

For a key type $\alpha$, a value type $\beta$ and a hash
function $h : \alpha \to \mathbb{N}$, a hash table with hash function $h$ consists of a positive
number $m$ of buckets and, for each bucket index $i < m$, a chain stored at bucket $i$: an
association list of key–value pairs whose keys are pairwise distinct. The structure itself does
not require keys to lie in their hash-selected bucket.

No expected constant-time bound is claimed because the model supplies neither a probability
distribution nor a probabilistic assumption about the hash function.

Formalized by `Cslib.Algorithms.Lean.HashTable`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#hash-table).

## Empty hash table

For a hash function $h$ and a positive integer $m$, the empty hash table
with hash function $h$ has $m$ buckets, each holding the empty chain.

Formalized by `Cslib.Algorithms.Lean.HashTable.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#empty).

## Hash table lookup

For a hash table with hash function $h$ and $m$ buckets, looking up
a key $k$ searches only the bucket with index $h(k) \bmod m$: the result is the value bound to
$k$ in that bucket's association list, or nothing if $k$ has no binding there.

Formalized by `Cslib.Algorithms.Lean.HashTable.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#lookup).

## Insertion into a hash table

Inserting a key $k$ with value $v$ into a hash table with $m$
buckets and hash function $h$ keeps the bucket count and every bucket other than bucket
$h(k) \bmod m$, and replaces the chain at bucket $h(k) \bmod m$ by that chain with $k$ bound to
$v$: any earlier binding of $k$ in that chain is removed and the binding of $k$ to $v$ is added.

Formalized by `Cslib.Algorithms.Lean.HashTable.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#insert).

## Valid hash table

A hash table with hash function $h$ and $m$ buckets is valid when every
binding lies in its hash-selected bucket: for every bucket index $i < m$ and every key $k$, if
$k$ has a binding in bucket $i$, then $h(k) \bmod m = i$.

Keys within a single bucket are distinct automatically, since each bucket is an association list.

Formalized by `Cslib.Algorithms.Lean.HashTable.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#valid).

## Finite map represented by a hash table

The finite map represented by a hash table with
$m$ buckets is built from the list of all bindings of buckets $0, 1, \dots, m - 1$, concatenated
in this order: it binds exactly the keys occurring in this list, and binds each such key to the
value of its first binding in the list.

Formalized by `Cslib.Algorithms.Lean.HashTable.abstraction`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#abstraction).

## The empty hash table is valid

For every hash function $h$ and every positive bucket
count $m$, the empty hash table with hash function $h$ and $m$ buckets is valid.

Formalized by `Cslib.Algorithms.Lean.HashTable.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#valid-empty).

## Lookup in the empty hash table

For every hash function $h$, every positive bucket count
$m$ and every key $k$, looking up $k$ in the empty hash table with hash function $h$ and $m$
buckets finds no value.

Formalized by `Cslib.Algorithms.Lean.HashTable.lookup_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#lookup-empty).

## The empty hash table represents the empty map

For every hash function $h$ and every
positive bucket count $m$, the finite map represented by the empty hash table with hash function
$h$ and $m$ buckets is the empty finite map.

Formalized by `Cslib.Algorithms.Lean.HashTable.abstraction_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#abstraction-empty).

## Hash table lookup after insertion

For every hash table $T$, every key $k$ and every
value $v$, looking up $k$ in the table obtained by inserting $k$ with value $v$ into $T$ returns
$v$.

Formalized by `Cslib.Algorithms.Lean.HashTable.lookup_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#lookup-insert).

## Insertion does not affect other keys

For every hash table $T$, all keys $k \ne k'$ and
every value $v$, looking up $k'$ in the table obtained by inserting $k$ with value $v$ into $T$
gives the same result as looking up $k'$ in $T$, also when $k$ and $k'$ lie in the same bucket.

Formalized by `Cslib.Algorithms.Lean.HashTable.lookup_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#lookup-insert-of-ne).

## Insertion preserves validity of a hash table

If a hash table is valid, then the table
obtained from it by inserting a key $k$ with value $v$ (adding a new binding for $k$, or
replacing the existing one) is again valid.

Formalized by `Cslib.Algorithms.Lean.HashTable.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#valid-insert).

## Lookup agrees with the abstraction

For every valid hash table $T$ and every key $k$,
looking up $k$ in the finite map represented by $T$ gives the same result as looking up $k$ in
$T$.

Formalized by `Cslib.Algorithms.Lean.HashTable.lookup_abstraction`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#lookup-abstraction).

## Insertion commutes with the abstraction

For every valid hash table $T$, every key $k$ and
every value $v$, the finite map represented by the table obtained by inserting $k$ with value $v$
into $T$ equals the finite map represented by $T$ with $k$ bound to $v$, replacing any earlier
binding of $k$.

Formalized by `Cslib.Algorithms.Lean.HashTable.abstraction_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/HashTable.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html#abstraction-insert).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hash table with separate chaining](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/hashing/hash-table-with-separate-chaining)
