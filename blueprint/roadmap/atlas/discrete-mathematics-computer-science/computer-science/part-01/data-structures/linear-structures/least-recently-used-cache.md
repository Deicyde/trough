---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.LruCache, Cslib.Algorithms.Lean.LruCache.ext, Cslib.Algorithms.Lean.LruCache.eraseKey, Cslib.Algorithms.Lean.LruCache.empty, Cslib.Algorithms.Lean.LruCache.keys, Cslib.Algorithms.Lean.LruCache.size, Cslib.Algorithms.Lean.LruCache.get, Cslib.Algorithms.Lean.LruCache.put
statement: formalized
proof: formalized
---

# Least-recently-used cache

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html).

## LRU cache

## Least-recently-used cache

For a type $K$ of keys, a type $V$ of values and a
natural number $c$, an LRU cache of capacity $c$ is a list of key-value pairs in $K \times V$,
ordered from most to least recently used, whose keys are pairwise distinct and whose length
is at most $c$.

Formalized by `Cslib.Algorithms.Lean.LruCache`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#lru-cache).

## Extensionality of LRU caches

Two LRU caches with the same key type, value type and
capacity are equal if their lists of entries are equal.

Formalized by `Cslib.Algorithms.Lean.LruCache.ext`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#ext).

## Erasing a key from a list of entries

Given a key $k$ and a list of key–value pairs,
erasing $k$ deletes every pair whose key is $k$ and keeps the other pairs in their original
order. When the keys in the list are pairwise distinct, at most one pair is deleted.

Formalized by `Cslib.Algorithms.Lean.LruCache.eraseKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#erase-key).

## Empty LRU cache

For every capacity $c$, the empty LRU cache of capacity $c$ is the cache
with no entries.

Formalized by `Cslib.Algorithms.Lean.LruCache.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#empty).

## Key list of an LRU cache

The key list of an LRU cache is the list of the keys of its
entries in the order of the cache, so the most recently used key comes first.

Formalized by `Cslib.Algorithms.Lean.LruCache.keys`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#keys).

## Size of an LRU cache

The size of an LRU cache is the number of entries it stores.

Formalized by `Cslib.Algorithms.Lean.LruCache.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#size).

## LRU cache lookup

Looking up a key $k$ in an LRU cache returns an optional value
together with a cache. If the cache stores a binding $(k, v)$, the result is $v$ together
with the cache in which that binding is moved to the front and the other entries keep their
order; otherwise the result is no value together with the unchanged cache.

Formalized by `Cslib.Algorithms.Lean.LruCache.get`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get).

## Insertion into an LRU cache

Putting the binding $(k, v)$ into an LRU cache of capacity $c$
removes any entry with key $k$, places $(k, v)$ at the front as the most recently used entry,
and then keeps only the first $c$ entries, so the least recently used entries beyond the
capacity are evicted.

Formalized by `Cslib.Algorithms.Lean.LruCache.put`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#put).

## Keys of an LRU cache are distinct

The keys stored in any LRU cache are pairwise
distinct.

Formalized by `Cslib.Algorithms.Lean.LruCache.keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#keys-nodup).

## An LRU cache never exceeds its capacity

Every LRU cache of capacity $c$ has size at most
$c$.

Formalized by `Cslib.Algorithms.Lean.LruCache.size_le_cap`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#size-le-cap).

## A lookup of an absent key misses

If the key $k$ is not stored in an LRU cache, then
looking up $k$ returns no value and leaves the cache unchanged.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_miss`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-miss).

## A lookup of a stored key returns its value

If an LRU cache stores the pair $(k, v)$,
then looking up $k$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_hit`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-hit).

## A successful lookup moves the entry to the front

If an LRU cache stores the pair
$(k, v)$, then after looking up $k$ the most recently used (first) entry of the cache is
$(k, v)$.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_promotes`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-promotes).

## Lookup after insertion into an LRU cache

For every LRU cache of positive capacity, every key
$k$ and every value $v$, looking up $k$ in the cache obtained by putting the binding $(k, v)$
returns $v$.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_put`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-put).

## Insertion respects the capacity of an LRU cache

For every LRU cache $C$ of capacity
$c$, key $k$ and value $v$, the cache obtained by putting the binding $(k, v)$ into $C$ has
size at most $c$.

Formalized by `Cslib.Algorithms.Lean.LruCache.put_size_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#put-size-le).

## Insertion keeps the keys of an LRU cache distinct

For every LRU cache $C$, key $k$
and value $v$, the keys of the cache obtained by putting the binding $(k, v)$ into $C$ are
pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.LruCache.put_keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#put-keys-nodup).

## Lookup respects the capacity

For every LRU cache of capacity $c$ and every key
$k$, the cache after looking up $k$ holds at most $c$ entries.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_size_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-size-le).

## Lookups keep keys distinct

For every LRU cache and every key $k$, the keys of the cache
obtained by looking up $k$ are pairwise distinct.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-keys-nodup).

## Entries after insertion

For every LRU cache, key $k$ and value $v$, every
key-value pair $p$ stored in the cache after putting the binding $(k, v)$ either equals
$(k, v)$, or was stored before and has a key different from $k$.

Formalized by `Cslib.Algorithms.Lean.LruCache.mem_put_entries`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#mem-put-entries).

## Lookup preserves the stored bindings

For every LRU cache and every key $k$, a
key-value pair is stored in the cache after looking up $k$ if and only if it was stored in
the cache before the lookup.

Formalized by `Cslib.Algorithms.Lean.LruCache.mem_get_entries_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#mem-get-entries-iff).

## A lookup permutes the entries

For every LRU cache and every key $k$, the list of
entries of the cache after looking up $k$ is a permutation of the list of entries before.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-perm).

## Lookup preserves the size

For every LRU cache and every key $k$, the cache after
looking up $k$ holds exactly as many entries as before.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-size).

## Insertion without eviction

Let an LRU cache of capacity $c$ hold fewer than $c$
entries or already store a binding for the key $k$, and let $v$ be a value. Then a key-value
pair $p$ is stored in the cache after putting the binding $(k, v)$ if and only if $p = (k, v)$,
or $p$ was stored before and the key of $p$ differs from $k$.

Formalized by `Cslib.Algorithms.Lean.LruCache.mem_put_entries_iff_of_not_full`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#mem-put-entries-iff-of-not-full).

## With positive capacity, the inserted binding becomes the most recent entry

Let $C$
be an LRU cache of positive capacity, $k$ a key and $v$ a value. After the binding $(k, v)$
is put into $C$, the first entry of the resulting cache, its most recently used entry, is
$(k, v)$.

Formalized by `Cslib.Algorithms.Lean.LruCache.put_head?`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#put-head).

## A put without eviction preserves lookups of other keys

Let $C$ be an LRU cache of
capacity $c$ that holds fewer than $c$ entries or already stores the key $k$. Then for every
key $k' \ne k$ and every value $v$, looking up $k'$ in the cache obtained by putting the binding
$(k, v)$ into $C$ returns the same optional value as looking up $k'$ in $C$.

Formalized by `Cslib.Algorithms.Lean.LruCache.get_put_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#get-put-of-ne).

## The evicted key is the least recently used one

Let $C$ be an LRU cache of capacity $c$,
let $k'$ be a key not stored in $C$, and let $k$ be a key stored in $C$. If $k$ is no longer
stored after putting $k'$ with any value $v$ into $C$, then $C$ held exactly $c$ entries and $k$
is the last key of $C$, that is, the least recently used one.

Formalized by `Cslib.Algorithms.Lean.LruCache.evicted_is_least_recent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/LruCache.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html#evicted-is-least-recent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Least-recently-used cache](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/least-recently-used-cache)
