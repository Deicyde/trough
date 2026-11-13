---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.XFastTrie, Cslib.Algorithms.Lean.XFastTrie.prefixOf, Cslib.Algorithms.Lean.XFastTrie.prefixOf_zero, Cslib.Algorithms.Lean.XFastTrie.prefixOf_full, Cslib.Algorithms.Lean.XFastTrie.prefixOf_lt, Cslib.Algorithms.Lean.XFastTrie.Valid, Cslib.Algorithms.Lean.XFastTrie.empty, Cslib.Algorithms.Lean.XFastTrie.insert
statement: formalized
proof: formalized
---

# X-fast trie

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html).

## X-fast trie

## x-fast trie

An x-fast trie over $w$-bit keys consists of a finite set of stored keys in
$\{0, \dots, 2^w - 1\}$ together with, for each level $l \in \{0, \dots, w\}$, a finite set of
natural numbers, intended to hold the $l$-bit prefixes of the stored keys.

The classical per-level hash tables are modeled as finite sets, so no $O(\log w)$ successor bound
(or any other running-time bound) is claimed.

Formalized by `Cslib.Algorithms.Lean.XFastTrie`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#xfast-trie).

## Bit prefix of a key

For natural numbers $l$ and $w$ and a $w$-bit key $x < 2^w$,
the length-$l$ prefix of $x$ is the natural number $\lfloor x / 2^{w-l} \rfloor$, where
$w - l$ is truncated subtraction (it is $0$ when $l > w$). For $l \le w$ these are the top
$l$ bits of $x$, a number below $2^l$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.prefixOf`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#prefix-of).

## The empty prefix is zero

For every $w$-bit key $x < 2^w$, the length-$0$ prefix
of $x$ (the trie root) is $0$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.prefixOf_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#prefix-of-zero).

## The full-length prefix of a key is the key

For every $w$-bit key $x < 2^w$, the
length-$w$ prefix of $x$ equals $x$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.prefixOf_full`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#prefix-of-full).

## A prefix fits in its length

For natural numbers $l \le w$ and a $w$-bit key
$x < 2^w$, the length-$l$ prefix of $x$ is less than $2^l$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.prefixOf_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#prefix-of-lt).

## Valid x-fast trie

An x-fast trie $t$ over $w$-bit keys is valid when, for every level
$l \in \{0, \dots, w\}$, the level-$l$ set of $t$ equals the set of $l$-bit prefixes (top $l$
bits) of the stored keys of $t$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#valid).

## The empty x-fast trie

The empty x-fast trie over $w$-bit keys stores no keys, and the
prefix set at each of its levels $0, 1, \dots, w$ is empty.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#empty).

## Insertion into an x-fast trie

Inserting a $w$-bit key $x$ into an x-fast trie $t$ adds $x$
to the keys stored in $t$ and, for each level $0 \le l \le w$, adds the $l$-bit prefix of $x$ to
the prefix set at level $l$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#insert).

## The empty x-fast trie is valid

For every $w$, the empty x-fast trie over $w$-bit keys,
which has no stored keys and every level empty, is valid.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#valid-empty).

## Insertion preserves validity of an x-fast trie

If $t$ is a valid x-fast trie over
$w$-bit keys and $x \in \{0, \dots, 2^w - 1\}$, then the x-fast trie obtained from $t$ by
inserting $x$ is valid.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#valid-insert).

## Keys of an x-fast trie after insertion

For every x-fast trie $t$ over $w$-bit keys and
every $w$-bit key $x$, the set of keys stored in the trie obtained by inserting $x$ into $t$ is
the set of keys stored in $t$ with $x$ added.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.contents_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#contents-insert).

## Level probe of an x-fast trie

For an x-fast trie $t$ over $w$-bit keys, a level
$0 \le l \le w$ and a $w$-bit key $x$, the probe of level $l$ of $t$ at $x$ returns true exactly
when the $l$-bit prefix of $x$ belongs to the prefix set stored at level $l$ of $t$.

When $t$ is valid, this holds exactly when some key stored in $t$ has the same $l$-bit prefix
as $x$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.hasPrefix`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#has-prefix).

## Level probes of a valid x-fast trie

Let $t$ be a valid x-fast trie over $w$-bit keys,
let $0 \le l \le w$ and let $x$ be a $w$-bit key. The probe of level $l$ of $t$ at $x$ succeeds if
and only if some key $y$ stored in $t$ has the same $l$-bit prefix as $x$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.hasPrefix_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#has-prefix-iff).

## Membership query in an x-fast trie

For an x-fast trie $t$ over $w$-bit keys
and a key $x < 2^w$, the membership query of $x$ in $t$ answers true exactly when the
length-$w$ prefix of $x$, which is $x$ itself, lies in the prefix set that $t$ stores
for level $w$: a single probe of the deepest level, as in the classical structure.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.member`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#member).

## The membership test of a valid x-fast trie is exact

For a valid x-fast trie $t$ over
$w$-bit keys and a $w$-bit key $x$, the membership test of $t$ at $x$, which probes the deepest
level $w$, returns true if and only if $x$ is stored in $t$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.member_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#member-iff).

## An inserted key passes the membership test

For every x-fast trie $t$ over $w$-bit keys
and every $w$-bit key $x$, the membership test at $x$ of the trie obtained by inserting $x$ into
$t$ returns true.

No validity assumption on $t$ is needed: insertion puts the full-length prefix of $x$ directly
into the deepest level, which is the level the membership test probes.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.member_insert_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#member-insert-self).

## Successor in an x-fast trie

For an x-fast trie $t$ over $w$-bit keys and a key
$x \in \{0, \dots, 2^w - 1\}$, the successor of $x$ in $t$ is the least stored key of $t$ that is
greater than $x$ when some stored key is greater than $x$; otherwise $x$ has no successor in $t$.

It is computed directly from the stored key set rather than by the classical binary search over
the levels, so no $O(\log w)$ time bound is claimed.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.successor`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#successor).

## Predecessor query in an x-fast trie

For an x-fast trie $t$ over $w$-bit keys and
a key $x < 2^w$, the predecessor of $x$ in $t$ is the greatest key stored in $t$ that is
smaller than $x$, if such a key exists; otherwise the query returns no key.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.predecessor`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#predecessor).

## Characterization of the x-fast trie successor

Let $t$ be an x-fast trie over $w$-bit
keys and let $x$ and $y$ be keys in $\{0, \dots, 2^w - 1\}$. The successor of $x$ in $t$ exists
and equals $y$ if and only if $y$ is a stored key of $t$, $x < y$, and $y \le z$ for every stored
key $z$ of $t$ with $x < z$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.successor_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#successor-eq-some-iff).

## When an x-fast trie has no successor

For an x-fast trie $t$ over $w$-bit keys
and a key $x < 2^w$, the successor query of $x$ in $t$ returns no key if and only if no
key stored in $t$ is greater than $x$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.successor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#successor-eq-none-iff).

## Characterization of the x-fast trie predecessor

For an x-fast trie $t$ over
$w$-bit keys and keys $x, y < 2^w$, the predecessor query of $x$ in $t$ returns $y$ if and
only if $y$ is stored in $t$, $y < x$, and every key $z$ stored in $t$ with $z < x$
satisfies $z \le y$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.predecessor_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#predecessor-eq-some-iff).

## When an x-fast trie has no predecessor

For an x-fast trie $t$ over $w$-bit keys
and a key $x < 2^w$, the predecessor query of $x$ in $t$ returns no key if and only if
no key stored in $t$ is smaller than $x$.

Formalized by `Cslib.Algorithms.Lean.XFastTrie.predecessor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#predecessor-eq-none-iff).

## y-fast trie skeleton

A y-fast trie skeleton over $w$-bit keys consists of an x-fast trie
over $w$-bit keys, whose stored keys are the representatives, together with a bucket $B_r$, a
finite set of keys, for every key $r \in \{0, \dots, 2^w - 1\}$.

In the classical structure each bucket is a balanced search tree of $\Theta(w)$ keys; here buckets
are plain finite sets, the bucket ordering invariant and the split and merge maintenance are not
modeled, and no complexity bound is claimed.

Formalized by `Cslib.Algorithms.Lean.YFastTrie`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#yfast-trie).

## Keys of a y-fast trie

Let $t$ be a y-fast trie over $w$-bit keys, let $R$ be the set of
keys stored in the representative x-fast trie of $t$, and for each $r \in R$ let $B(r)$ be the
bucket owned by $r$. The set of keys stored in $t$ is the union of the buckets of its
representatives, $\bigcup_{r \in R} B(r)$.

It is computed from the representatives alone, not by filtering all $2^w$ possible keys.

Formalized by `Cslib.Algorithms.Lean.YFastTrie.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#contents).

## Membership in a y-fast trie via representatives' buckets

For every y-fast trie $t$ over
$w$-bit keys and every $w$-bit key $x$, $x$ is stored in $t$ if and only if $x$ lies in the bucket
owned by some representative of $t$, that is, by some key stored in the representative x-fast
trie of $t$.

Formalized by `Cslib.Algorithms.Lean.YFastTrie.mem_contents_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#mem-contents-iff).

## Valid y-fast trie skeleton

A y-fast trie skeleton $t$ over $w$-bit keys, with bucket $B_r$
owned by each key $r$, is valid when its representative x-fast trie is valid, a key $r$ is stored
in the representative x-fast trie exactly when its bucket $B_r$ is nonempty, and every key $r$
stored in the representative x-fast trie lies in its own bucket $B_r$.

So the representatives are sampled from the stored keys: a representative $0$ whose bucket is
$\{1\}$ is not valid. The classical bucket ordering invariant (the keys of bucket $B_r$ lie in
the interval ending at $r$) is not required, so this is the invariant of the skeleton only.

Formalized by `Cslib.Algorithms.Lean.YFastTrie.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#valid-2).

## Representatives of a valid y-fast trie are stored keys

If a y-fast trie $t$ over
$w$-bit keys is valid, then every key of the representative x-fast trie of $t$ is a stored
key of $t$.

Formalized by `Cslib.Algorithms.Lean.YFastTrie.rep_mem_contents_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#rep-mem-contents-of-valid).

## Keys of a valid y-fast trie are the keys in buckets

If $t$ is a valid y-fast trie over
$w$-bit keys, then a $w$-bit key $x$ is stored in $t$ if and only if $x$ lies in the bucket owned
by some $w$-bit key $r$ (such an owner $r$ is then necessarily a representative).

Formalized by `Cslib.Algorithms.Lean.YFastTrie.mem_contents_iff_exists_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/XFastTrie.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html#mem-contents-iff-exists-of-valid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: X-fast trie](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/x-fast-trie)
