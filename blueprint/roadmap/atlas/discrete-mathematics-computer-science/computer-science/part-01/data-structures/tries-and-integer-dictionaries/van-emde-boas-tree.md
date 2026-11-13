---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.VanEmdeBoas, Cslib.Algorithms.Lean.VanEmdeBoas.empty, Cslib.Algorithms.Lean.VanEmdeBoas.member, Cslib.Algorithms.Lean.VanEmdeBoas.insert, Cslib.Algorithms.Lean.VanEmdeBoas.Valid, Cslib.Algorithms.Lean.VanEmdeBoas.contents, Cslib.Algorithms.Lean.VanEmdeBoas.member_empty, Cslib.Algorithms.Lean.VanEmdeBoas.member_insert_self
statement: formalized
proof: formalized
---

# Van Emde Boas tree

44 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html).

## Van Emde Boas

## Two-level van Emde Boas tree

For a natural number $m$, a two-level van Emde Boas tree over
the universe $\{0, \dots, m^2 - 1\}$ consists of a summary bit vector of length $m$ and, for each
$i < m$, a cluster bit vector of length $m$; bit $j$ of cluster $i$ records whether the element
$im + j$ is stored. Unlike the fully recursive van Emde Boas tree over universes of size
$2^{2^k}$, the summary and the clusters here are plain bit vectors, not van Emde Boas trees.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#van-emde-boas).

## Empty van Emde Boas tree

For a natural number $m$, the empty van Emde Boas tree over
the universe $\{0, 1, \dots, m^2 - 1\}$ is the tree in which all $m$ summary bits and all
$m^2$ cluster bits ($m$ clusters of $m$ bits each) are unset.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#empty).

## Membership in a van Emde Boas tree

An element $x$ of the universe
$\{0, 1, \dots, m^2 - 1\}$ is a member of a two-level van Emde Boas tree $t$ when bit
$x \bmod m$ of cluster $\lfloor x / m \rfloor$ of $t$ is set. The summary bits are not consulted.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member).

## Insertion into a van Emde Boas tree

Let $m$ be a natural number, let $t$ be a van Emde
Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$ and let $x$ be an element of the
universe. Inserting $x$ into $t$ gives the tree obtained from $t$ by setting bit $x \bmod m$ of
cluster $\lfloor x / m \rfloor$ and summary bit $\lfloor x / m \rfloor$, leaving every other bit
unchanged.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#insert).

## Summary invariant of a van Emde Boas tree

A two-level van Emde Boas tree $t$ with $m$
clusters is valid when, for every cluster index $i < m$, summary bit $i$ of $t$ is set exactly when
cluster $i$ of $t$ is nonempty, that is, when some bit $j < m$ of cluster $i$ is set.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#valid).

## Set of stored elements of a van Emde Boas tree

Let $m$ be a natural number. For a van
Emde Boas tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$, the set of stored elements of
$t$ is the finite set of those elements of the universe that are members of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 596](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L596). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#contents).

## The empty van Emde Boas tree has no members

For every $m$ and every $x$ in the universe
$\{0, 1, \dots, m^2 - 1\}$, $x$ is not a member of the empty two-level van Emde Boas tree over that
universe.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member-empty).

## An inserted element is a member of a van Emde Boas tree

For every two-level van Emde Boas
tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and every $x$ in that universe, $x$ is a
member of the tree obtained by inserting $x$ into $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member_insert_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member-insert-self).

## Insertion into a van Emde Boas tree leaves other elements unchanged

For every two-level
van Emde Boas tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and all $x \ne y$ in that
universe, $y$ is a member of the tree obtained by inserting $x$ into $t$ if and only if $y$ is a
member of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member_insert_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member-insert-of-ne).

## Membership after insertion into a van Emde Boas tree

For every two-level van Emde Boas
tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and all $x, y$ in that universe, $y$ is a
member of the tree obtained by inserting $x$ into $t$ if and only if $y = x$ or $y$ is a member
of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member-insert).

## Insertion into a van Emde Boas tree keeps existing members

For every two-level van Emde
Boas tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and all $x, y$ in that universe, if $y$
is a member of $t$, then $y$ is a member of the tree obtained by inserting $x$ into $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.member_insert_of_member`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#member-insert-of-member).

## The empty van Emde Boas tree is valid

For every natural number $m$, the empty two-level
van Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$ satisfies the summary invariant: each
summary bit is set exactly when its cluster is nonempty.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#valid-empty).

## Insertion preserves validity of van Emde Boas trees

For every natural number $m$, every
element $x$ of the universe $\{0, \dots, m^2 - 1\}$ and every two-level van Emde Boas tree $t$ over
that universe that satisfies the summary invariant (each summary bit is set exactly when its
cluster is nonempty), the tree obtained from $t$ by inserting $x$ also satisfies the summary
invariant.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#valid-insert).

## The contents of a van Emde Boas tree are its members

For every two-level van Emde Boas
tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and every $x$ in that universe, $x$ belongs
to the finite set of stored elements of $t$ if and only if $x$ is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.mem_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#mem-contents).

## Contents of the empty van Emde Boas tree

For every natural number $m$, the set of
stored elements of the empty van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$
is empty.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.contents_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#contents-empty).

## Contents after insertion into a van Emde Boas tree

Let $m$ be a natural number, let
$t$ be a van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$ and let $x$ be an
element of the universe. The set of stored elements of the tree obtained by inserting $x$ into
$t$ is the set of stored elements of $t$ together with $x$. No validity assumption on $t$ is
needed.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.contents_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#contents-insert).

## Minimum query of a van Emde Boas tree

Let $t$ be a two-level van Emde Boas tree over the
universe $\{0, \dots, m^2 - 1\}$. If some summary bit of $t$ is set, let $h$ be the least cluster
index whose summary bit is set; if cluster $h$ has a set position, let $\ell$ be the least one.
The minimum query on $t$ then returns the element $h \cdot m + \ell$. If no summary bit is set,
or cluster $h$ has no set position, it returns no element.

In a valid tree this is the least stored element.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min).

## The van Emde Boas minimum is stored

Let $t$ be a two-level van Emde Boas tree over the
universe $\{0, \dots, m^2 - 1\}$. If the minimum query on $t$ returns $x$, then $x$ is stored in
$t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-mem).

## The van Emde Boas minimum is a lower bound

Let $t$ be a valid two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$. If the minimum query on $t$ returns $x$, then
$x \le y$ for every $y$ stored in $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_least`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 733](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L733). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-least).

## Empty minimum query in a van Emde Boas tree

Let $t$ be a valid two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$. The minimum query on $t$ returns no element if and
only if no element of the universe is stored in $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-eq-none-iff).

## Characterization of the van Emde Boas minimum

Let $t$ be a valid two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$, and let $x$ be in the universe. The minimum query
on $t$ returns $x$ if and only if $x$ is stored in $t$ and $x \le y$ for every $y$ stored in $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_eq_some_iff_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-eq-some-iff-of-valid).

## The empty van Emde Boas tree has no minimum

For every $m$, the minimum query of the empty
two-level van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$ returns no element.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 810](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L810). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-empty).

## Minimum of a one-element van Emde Boas tree

For every $x$ in the universe
$\{0, \dots, m^2 - 1\}$, the minimum query on the two-level van Emde Boas tree obtained by
inserting $x$ into the empty tree returns $x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.min?_insert_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 814](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L814). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#min-insert-empty).

## Maximum query of a van Emde Boas tree

For a two-level van Emde Boas tree $t$ over the
universe $\{0, 1, \dots, m^2 - 1\}$, the maximum query first finds the greatest index $i < m$ whose
summary bit is set, and then the greatest index $j < m$ whose bit is set in cluster $i$; it returns
the element $i m + j$. It returns no element if no summary bit is set, or if no bit of cluster $i$
is set. When the summary bits record exactly the nonempty clusters, this is the greatest stored
element.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max).

## The maximum query of a van Emde Boas tree returns a member

For every two-level van Emde
Boas tree $t$ over the universe $\{0, 1, \dots, m^2 - 1\}$ and every $x$ in that universe, if the
maximum query of $t$ returns $x$, then $x$ is a member of $t$. No validity hypothesis on $t$ is
needed.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 858](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L858). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-mem).

## The van Emde Boas maximum query bounds every member

Let $m$ be a natural number and let
$t$ be a valid van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$. If the maximum
query on $t$ returns $x$, then $y \le x$ for every member $y$ of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_greatest`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 865](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L865). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-greatest).

## When the van Emde Boas maximum query returns nothing

Let $m$ be a natural number and let
$t$ be a valid van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$. The maximum query
on $t$ returns no element if and only if no element of the universe is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-eq-none-iff).

## Correctness of the van Emde Boas maximum query

Let $m$ be a natural number, let $t$ be a
valid van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$ and let $x$ be an element of
the universe. The maximum query on $t$ returns $x$ if and only if $x$ is a member of $t$ and
$y \le x$ for every member $y$ of $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_eq_some_iff_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 917](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L917). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-eq-some-iff-of-valid).

## Maximum query on the empty van Emde Boas tree

For every natural number $m$, the
maximum query on the empty van Emde Boas tree over the universe $\{0, 1, \dots, m^2 - 1\}$
returns no element.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 942](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L942). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-empty).

## Maximum query on a one-element van Emde Boas tree

Let $m$ be a natural number and let
$x$ be an element of the universe $\{0, 1, \dots, m^2 - 1\}$. The maximum query on the tree
obtained by inserting $x$ into the empty van Emde Boas tree over this universe returns $x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.max?_insert_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 946](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#max-insert-empty).

## Successor query in a two-level van Emde Boas tree

Let $T$ be a two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$ and let $x = hm + \ell$ with $0 \le h, \ell < m$, so
that $x$ sits at position $\ell$ of cluster $h$. If cluster $h$ has a set position after $\ell$, the
successor of $x$ in $T$ is $hm + \ell'$ for the least such position $\ell'$. Otherwise, let $h'$ be
the least cluster index with $h < h'$ whose summary bit is set; the successor is $h'm + \ell''$ for
the least position $\ell''$ set in cluster $h'$. If there is no such $h'$, or cluster $h'$ has no
set position, $x$ has no successor.

In a valid tree, the successor of $x$ is the least member of $T$ greater than $x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1014](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1014). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor).

## The van Emde Boas successor is stored

Let $T$ be a two-level van Emde Boas tree over the
universe $\{0, \dots, m^2 - 1\}$, not necessarily valid, and let $x$ and $y$ be elements of the
universe. If the successor of $x$ in $T$ is $y$, then $y$ is a member of $T$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1067](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1067). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-mem).

## The van Emde Boas successor is strictly larger than its argument

Let $T$ be a two-level
van Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$, not necessarily valid, and let $x$
and $y$ be elements of the universe. If the successor of $x$ in $T$ is $y$, then $x < y$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1079](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1079). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-gt).

## No member lies strictly between an element and its van Emde Boas successor

Let $T$ be a
valid two-level van Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$ and let $x$, $y$, $z$
be elements of the universe. If the successor of $x$ in $T$ is $y$ and $z$ is a member of $T$ with
$x < z$, then $y \le z$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_least`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1094](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1094). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-least).

## A van Emde Boas successor is missing exactly when nothing larger is stored

Let $T$ be a
valid two-level van Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$ and let $x$ be an
element of the universe. Then $x$ has no successor in $T$ if and only if every member $z$ of $T$
satisfies $z \le x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-eq-none-iff).

## The van Emde Boas successor is the least larger member

Let $T$ be a valid two-level van
Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$ and let $x$ and $y$ be elements of the
universe. Then the successor of $x$ in $T$ is $y$ if and only if $y$ is a member of $T$, $x < y$,
and $y \le z$ for every member $z$ of $T$ with $x < z$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_eq_some_iff_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-eq-some-iff-of-valid).

## The empty van Emde Boas tree has no successors

For every $m$ and every element $x$ of the
universe $\{0, \dots, m^2 - 1\}$, $x$ has no successor in the empty two-level van Emde Boas tree
over that universe.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.successor_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#successor-empty).

## Predecessor query in a two-level van Emde Boas tree

Let $T$ be a two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$ and let $x = hm + \ell$ with $0 \le h, \ell < m$, so
that $x$ sits at position $\ell$ of cluster $h$. If cluster $h$ has a set position before $\ell$,
the predecessor of $x$ in $T$ is $hm + \ell'$ for the greatest such position $\ell'$. Otherwise,
let $h'$ be the greatest cluster index with $h' < h$ whose summary bit is set; the predecessor is
$h'm + \ell''$ for the greatest position $\ell''$ set in cluster $h'$. If there is no such $h'$, or
cluster $h'$ has no set position, $x$ has no predecessor.

In a valid tree, the predecessor of $x$ is the greatest member of $T$ less than $x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor).

## The van Emde Boas predecessor is stored

Let $T$ be a two-level van Emde Boas tree over the
universe $\{0, \dots, m^2 - 1\}$, not necessarily valid, and let $x$ and $y$ be elements of the
universe. If the predecessor of $x$ in $T$ is $y$, then $y$ is a member of $T$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-mem).

## The van Emde Boas predecessor is strictly smaller than its argument

Let $T$ be a two-level
van Emde Boas tree over the universe $\{0, \dots, m^2 - 1\}$, not necessarily valid, and let $x$
and $y$ be elements of the universe. If the predecessor of $x$ in $T$ is $y$, then $y < x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-lt).

## Maximality of the van Emde Boas predecessor

Let $t$ be a valid two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$, and let $x$, $y$ and $z$ be in the universe. If the
predecessor query for $x$ in $t$ returns $y$, and $z$ is stored in $t$ with $z < x$, then
$z \le y$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_greatest`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-greatest).

## Empty predecessor query in a van Emde Boas tree

Let $t$ be a valid two-level van Emde Boas
tree over the universe $\{0, \dots, m^2 - 1\}$, and let $x$ be in the universe. The predecessor
query for $x$ in $t$ returns no element if and only if $x \le z$ for every $z$ stored in $t$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-eq-none-iff).

## Characterization of the van Emde Boas predecessor

Let $t$ be a valid two-level van Emde
Boas tree over the universe $\{0, \dots, m^2 - 1\}$, and let $x$ and $y$ be in the universe. The
predecessor query for $x$ in $t$ returns $y$ if and only if $y$ is stored in $t$, $y < x$, and
$z \le y$ for every $z$ stored in $t$ with $z < x$.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_eq_some_iff_of_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-eq-some-iff-of-valid).

## Predecessor queries in the empty van Emde Boas tree

For every $x$ in the universe
$\{0, \dots, m^2 - 1\}$, the predecessor query for $x$ in the empty two-level van Emde Boas tree
returns no element.

Formalized by `Cslib.Algorithms.Lean.VanEmdeBoas.predecessor_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean, line 1466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/VanEmdeBoas.lean#L1466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html#predecessor-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van Emde Boas tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/tries-and-integer-dictionaries/van-emde-boas-tree)
