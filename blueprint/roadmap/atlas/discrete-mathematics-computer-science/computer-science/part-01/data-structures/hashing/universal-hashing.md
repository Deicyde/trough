---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.UniversalHashing.collisionCount, Cslib.Algorithms.Lean.UniversalHashing.IsUniversal, Cslib.Algorithms.Lean.UniversalHashing.IsUniversalOn, Cslib.Algorithms.Lean.UniversalHashing.collisionCount_le_card, Cslib.Algorithms.Lean.UniversalHashing.collisionCount_self, Cslib.Algorithms.Lean.UniversalHashing.not_isUniversal_empty, Cslib.Algorithms.Lean.UniversalHashing.not_isUniversalOn_empty, Cslib.Algorithms.Lean.UniversalHashing.isUniversal_bound_empty
statement: formalized
proof: formalized
---

# Universal hashing

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html).

## General

## Collision count

For a finite family $H$ of functions from a set $\alpha$ to
$\{0, 1, \dots, m - 1\}$ and keys $x, y \in \alpha$, the collision count of $x$ and $y$ in $H$
is the number of functions $h \in H$ with $h(x) = h(y)$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.collisionCount`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#collision-count).

## Universal hash family

A finite family $H$ of functions from a set $\alpha$ to
$\{0, 1, \dots, m - 1\}$ is universal if $m > 0$, $H$ is nonempty, and for all distinct keys
$x \ne y$ in $\alpha$ the number of functions $h \in H$ with $h(x) = h(y)$, multiplied by $m$,
is at most $|H|$; that is, $x$ and $y$ collide under at most a $1/m$ fraction of the members
of $H$.

Nonemptiness makes sense of choosing a member of $H$ uniformly at random, the reading behind
the bound.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.IsUniversal`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#is-universal).

## Indexed universal hash family

Let $s$ be a finite set of indices from a type $\iota$,
and let $h$ assign to each index $i \in \iota$ a function $h_i$ from a set $\alpha$ to
$\{0, 1, \dots, m - 1\}$. The family $h$ is universal on $s$ if $m > 0$, $s$ is nonempty,
and for all distinct keys $x \ne y$ in $\alpha$ the number of indices $i \in s$ with
$h_i(x) = h_i(y)$, multiplied by $m$, is at most $|s|$.

Each index is counted separately, even when two indices give the same function; this is the
form in which the classical counting arguments, including the one for the mod-prime family,
are carried out. Nonemptiness is required because there is no uniform random choice from an
empty family.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.IsUniversalOn`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#is-universal-on).

## Collision count is at most the family size

For every finite family $H$ of functions
from a set $\alpha$ to $\{0, 1, \dots, m - 1\}$ and all keys $x, y \in \alpha$, the number of
functions $h \in H$ with $h(x) = h(y)$ is at most $|H|$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.collisionCount_le_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#collision-count-le-card).

## A key collides with itself under the whole family

For every finite family $H$ of
functions from a set $\alpha$ to $\{0, 1, \dots, m - 1\}$ and every key $x \in \alpha$, the
collision count of $x$ with itself in $H$ equals $|H|$: $x$ collides with itself under every
function in $H$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.collisionCount_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#collision-count-self).

## The empty hash family is not universal

For every type of keys $\alpha$ and every natural
number $m$, the empty family of functions $\alpha \to \{0, \dots, m - 1\}$ is not universal:
universality includes nonemptiness, since its meaning is a bound on the collision probability for
a uniformly chosen member.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.not_isUniversal_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#not-is-universal-empty).

## The empty indexed family is not universal

For every index type $\iota$, every type of
keys $\alpha$, every natural number $m$ and every family $(h_i)_{i \in \iota}$ of functions
$h_i \colon \alpha \to \{0, \dots, m - 1\}$, the family is not universal over the empty index
set: indexed universality includes nonemptiness of the index set, since there is no uniform
random choice from an empty family.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.not_isUniversalOn_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#not-is-universal-on-empty).

## The empty family satisfies the collision bound

For every natural number $m$ and all
distinct keys $x \ne y$ in a set $\alpha$, the collision count of $x$ and $y$ in the empty
family of functions from $\alpha$ to $\{0, 1, \dots, m - 1\}$, multiplied by $m$, is at most
the size of the empty family, which is $0$.

This is the collision bound of universality without its other conditions; universality also
requires the family to be nonempty and $m > 0$, so the empty family is not universal.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.isUniversal_bound_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#is-universal-bound-empty).

## Mod-prime hash function

For natural numbers $p$ and $m$ with $m > 0$ and elements $a, b$
of $\mathbb{Z}/p\mathbb{Z}$, the mod-prime hash function
$h_{a,b} \colon \mathbb{Z}/p\mathbb{Z} \to \{0, \dots, m - 1\}$ is
$h_{a,b}(x) = \operatorname{val}(ax + b) \bmod m$, where $ax + b$ is computed in
$\mathbb{Z}/p\mathbb{Z}$ and $\operatorname{val}(z)$ is the canonical natural-number
representative of $z$ (the residue in $\{0, \dots, p - 1\}$ when $p > 0$, and $|z|$ when
$p = 0$). This is the function $h_{a,b}(x) = ((ax + b) \bmod p) \bmod m$ of CLRS
Section 11.3.3.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeHash`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-hash).

## Mod-prime index set

For a natural number $p$, the index set of the mod-prime family is
the set of pairs $(a, b)$ with $a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \neq 0$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.ModPrimeIndex`, an abbreviation declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-index).

## Indexed mod-prime family

For natural numbers $p$ and $m$ with $m > 0$, the indexed
mod-prime family assigns to each index $(a, b)$, with $a, b \in \mathbb{Z}/p\mathbb{Z}$ and
$a \neq 0$, the mod-prime hash function
$h_{a,b} \colon \mathbb{Z}/p\mathbb{Z} \to \{0, \dots, m - 1\}$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeHashes`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-hashes).

## Mod-prime family of distinct functions

For $p > 0$ and $m > 0$, the mod-prime family
is the finite set of all functions $h_{a,b}$ from $\mathbb{Z}/p\mathbb{Z}$ to
$\{0, 1, \dots, m - 1\}$ with $a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \ne 0$, where
$h_{a,b}$ is the mod-prime hash function with index $(a, b)$.

Universality is proved for the indexed family of mod-prime hash functions, matching the
$p(p - 1)$ count of indices in CLRS; this set of distinct functions can be smaller, since
distinct index pairs may give the same function after the final reduction modulo $m$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeFamily`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-family).

## Value of the mod-prime hash

For natural numbers $p$ and $m$ with $m > 0$ and elements
$a, b, x$ of $\mathbb{Z}/p\mathbb{Z}$, the mod-prime hash value
$h_{a,b}(x) \in \{0, \dots, m - 1\}$, read as a natural number, equals
$\operatorname{val}(ax + b) \bmod m$. Here $ax + b$ is computed in $\mathbb{Z}/p\mathbb{Z}$, and
$\operatorname{val}(z)$ is the canonical natural-number representative of $z$: the residue in
$\{0, \dots, p - 1\}$ when $p > 0$, and $|z|$ when $p = 0$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeHash_val`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-hash-val).

## Collisions of a mod-prime hash function

Let $p$ be a natural number, $m > 0$ and
$a, b \in \mathbb{Z}/p\mathbb{Z}$, and write $\operatorname{val}(z)$ for the canonical
natural-number representative of $z \in \mathbb{Z}/p\mathbb{Z}$ (for $p = 0$, where
$\mathbb{Z}/0\mathbb{Z} = \mathbb{Z}$, its absolute value), so that the mod-prime hash
function is $h_{a,b}(x) = \operatorname{val}(ax + b) \bmod m$. For all keys
$x, y \in \mathbb{Z}/p\mathbb{Z}$, we have $h_{a,b}(x) = h_{a,b}(y)$ exactly when
$\operatorname{val}(ax + b) \bmod m = \operatorname{val}(ay + b) \bmod m$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeHash_eq_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-hash-eq-iff).

## The pair map of the mod-prime family

Let $p$ be a natural number and fix two keys
$x, y \in \mathbb{Z}/p\mathbb{Z}$. The pair map at $x$ and $y$ sends an index $(a, b)$ of the
mod-prime family, that is, $a, b \in \mathbb{Z}/p\mathbb{Z}$ with $a \ne 0$, to the pair
$(ax + b, ay + b) \in (\mathbb{Z}/p\mathbb{Z})^2$ of inner hash values at $x$ and $y$.

This is the map of the CLRS counting argument for the mod-prime family.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairMap`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-map).

## Evaluating the pair map

Let $p$ be a natural number, let $x, y \in \mathbb{Z}/p\mathbb{Z}$,
and let $(a, b)$ be an index of the mod-prime family, so that $a, b \in \mathbb{Z}/p\mathbb{Z}$
and $a \ne 0$. Then the pair map at $x$ and $y$ sends $(a, b)$ to $(ax + b, ay + b)$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairMap_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-map-apply).

## The two values of the pair map differ

Let $p$ be a prime and let $x \ne y$ be keys in the
field $\mathbb{Z}/p\mathbb{Z}$. For every index $(a, b)$ of the mod-prime family, that is,
$a, b \in \mathbb{Z}/p\mathbb{Z}$ with $a \ne 0$, we have $ax + b \ne ay + b$.

Indeed, the difference $(ax + b) - (ay + b) = a(x - y)$ is a product of two nonzero factors.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairMap_fst_ne_snd`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-map-fst-ne-snd).

## Pair bijection of the CLRS counting argument

Let $p$ be a prime and let $x \neq y$ be
elements of the field $\mathbb{Z}/p\mathbb{Z}$. The pair bijection for $x, y$ is the bijection
from the indices $(a, b)$, with $a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \neq 0$, to the ordered
pairs $(r, s)$ of elements of $\mathbb{Z}/p\mathbb{Z}$ with $r \neq s$ that sends $(a, b)$ to
the pair map value $(ax + b, ay + b)$. Its inverse solves the linear system $ax + b = r$,
$ay + b = s$: it sends $(r, s)$ to $(a, b)$ with $a = (r - s)/(x - y)$ and $b = r - ax$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairEquiv`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-equiv).

## The pair bijection is given by the pair map

Let $p$ be a prime and let $x \neq y$ be
elements of $\mathbb{Z}/p\mathbb{Z}$. For every index $(a, b)$ with
$a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \neq 0$, the image of $(a, b)$ under the pair bijection
for $x, y$, viewed as an element of $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/p\mathbb{Z}$, is the
value of the pair map at $(a, b)$, namely $(ax + b, ay + b)$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairEquiv_apply_fst`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-equiv-apply-fst).

## The pair map is injective

Let $p$ be a prime and let $x \ne y$ be keys in
$\mathbb{Z}/p\mathbb{Z}$. Then the pair map at $x$ and $y$, which sends an index $(a, b)$ of the
mod-prime family (so $a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \ne 0$) to $(ax + b, ay + b)$,
is injective.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.pairMap_injective`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#pair-map-injective).

## Collision bound for the mod-prime hash functions

Let $p$ be a prime and $m > 0$, and
for $a, b \in \mathbb{Z}/p\mathbb{Z}$ with $a \ne 0$ let
$h_{a,b}(x) = ((ax + b) \bmod p) \bmod m$ be the mod-prime hash function. For distinct keys
$x \ne y$ in $\mathbb{Z}/p\mathbb{Z}$, the number of index pairs $(a, b)$ with $a \ne 0$ and
$h_{a,b}(x) = h_{a,b}(y)$, multiplied by $m$, is at most $p(p - 1)$, the total number of
index pairs.

This is the counting step of CLRS Theorem 11.5. The bijection
$(a, b) \mapsto (ax + b, ay + b)$ identifies the colliding index pairs with the pairs $(r, s)$
of distinct residues modulo $p$ whose representatives in $\{0, \dots, p - 1\}$ are congruent
modulo $m$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrime_collision_mul_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-collision-mul-le).

## Number of mod-prime indices

For every positive natural number $p$, the set of pairs
$(a, b)$ of elements of $\mathbb{Z}/p\mathbb{Z}$ with $a \neq 0$ has exactly $p(p - 1)$
elements.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrimeIndex_card`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-index-card).

## Universality of the mod-prime family

Let $p$ be a prime and $m$ a positive natural number.
The indexed mod-prime family, whose member at the index $(a, b)$, with
$a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \neq 0$, is the mod-prime hash function $h_{a,b}$, is
universal over the set of all such indices: this set is nonempty, and for all distinct keys
$x \neq y$ in $\mathbb{Z}/p\mathbb{Z}$, the number of indices $(a, b)$ with
$h_{a,b}(x) = h_{a,b}(y)$, multiplied by $m$, is at most the number of indices. This is CLRS
Theorem 11.5.

A uniformly random index therefore collides on any two distinct keys with probability at most
$1/m$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.modPrime_isUniversalOn`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mod-prime-is-universal-on).

## Members of the mod-prime family

Let $p > 0$ and $m > 0$. A function $h$ from
$\mathbb{Z}/p\mathbb{Z}$ to $\{0, 1, \dots, m - 1\}$ belongs to the mod-prime family of
distinct functions exactly when $h = h_{a,b}$ for some index $(a, b)$ with
$a, b \in \mathbb{Z}/p\mathbb{Z}$ and $a \ne 0$, where $h_{a,b}$ is the mod-prime hash
function with index $(a, b)$.

Formalized by `Cslib.Algorithms.Lean.UniversalHashing.mem_modPrimeFamily`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/UniversalHashing.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html#mem-mod-prime-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Universal hashing](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/universal-hashing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/hashing/universal-hashing)
