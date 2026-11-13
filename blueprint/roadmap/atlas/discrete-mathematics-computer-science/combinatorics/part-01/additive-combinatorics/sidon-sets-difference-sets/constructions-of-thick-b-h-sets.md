---
declaration: section
origin: cited
lean: MetaMathlibExt.boseSet, MetaMathlibExt.mem_boseSet, MetaMathlibExt.singerSet, MetaMathlibExt.mem_singerSet, MetaMathlibExt.ZModAffinelyEquivalent, MetaMathlibExt.zModAffinelyEquivalent_refl, MetaMathlibExt.bhMaxCard, MetaMathlibExt.bhMinLength
statement: formalized
---

# Constructions of thick B_h-sets

27 results, 11 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html).

## Generalized Bose set

Let $F$ be a finite field with $q$ elements, $K$ a field extension
of $F$, $h$ and $b$ natural numbers and $\theta \in K$. The generalized Bose set
$\mathrm{Bose}_h(q, b)$ is the set of residues $a \in \mathbb{Z}/(q^h - 1)\mathbb{Z}$ such that
$\theta^a = \theta^b + v$ for some $v \in F$, where $\theta^a$ is computed with the least
nonnegative representative of $a$ (for $h = 0$ the modulus is $0$, $a$ ranges over $\mathbb{Z}$
and $\theta^a$ means $\theta^{|a|}$).

In the paper $K$ has degree $h$ over $F$ and $\theta$ generates $K^\times$; the definition does
not need these assumptions.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Definition 1.

Formalized by `MetaMathlibExt.boseSet`, a definition declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bose-set).

## Membership in a Bose set

Let $F$ be a finite field with $q$ elements, let $K$ be a field
extension of $F$, let $\theta \in K$, and let $h$ and $b$ be natural numbers. A residue
$a \in \mathbb{Z}/(q^h - 1)\mathbb{Z}$ lies in the Bose set $\mathrm{Bose}_h(q, b)$ built from
$F$, $K$ and $\theta$ if and only if $\theta^a = \theta^b + v$ for some $v \in F$, where
$\theta^a$ means $\theta$ raised to the least nonnegative representative of $a$ (or to $|a|$
when $h = 0$, since then $\mathbb{Z}/(q^h - 1)\mathbb{Z} = \mathbb{Z}$).

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Definition 1.

Formalized by `MetaMathlibExt.mem_boseSet`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#mem-bose-set).

## Generalized Singer set

Let $F$ be a finite field with $q$ elements, let $K$ be a field
extension of $F$, let $\theta \in K$, let $h$ and $b$ be natural numbers, and put
$M = (q^{h+1} - 1)/(q - 1)$. The generalized Singer set $\mathrm{Singer}_h(q, b)$ is the set of
residues $a \in \mathbb{Z}/M\mathbb{Z}$ such that $\theta^a = u\theta^b + v$ for some
$u, v \in F$, where $\theta^a$ means $\theta$ raised to the least nonnegative representative
of $a$.

The construction is intended for $[K : F] = h + 1$ and $\theta$ a generator of $K^\times$; the
definition itself does not assume either.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Definition 2.

Formalized by `MetaMathlibExt.singerSet`, a definition declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#singer-set).

## Membership in a Singer set

Let $F$ be a finite field with $q$ elements, let $K$ be a
field extension of $F$, let $\theta \in K$, let $h$ and $b$ be natural numbers, and put
$M = (q^{h+1} - 1)/(q - 1)$. A residue $a \in \mathbb{Z}/M\mathbb{Z}$ lies in the Singer set
$\mathrm{Singer}_h(q, b)$ built from $F$, $K$ and $\theta$ if and only if
$\theta^a = u\theta^b + v$ for some $u, v \in F$, where $\theta^a$ means $\theta$ raised to the
least nonnegative representative of $a$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Definition 2.

Formalized by `MetaMathlibExt.mem_singerSet`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#mem-singer-set).

## Affine equivalence of sets of residues

For a natural number $M$, sets
$A_1, A_2 \subseteq \mathbb{Z}/M\mathbb{Z}$ are affinely equivalent, written $A_1 \sim A_2$, if
there are a unit $d$ of $\mathbb{Z}/M\mathbb{Z}$ and an element $s \in \mathbb{Z}/M\mathbb{Z}$
such that $A_2 = \{d a + s : a \in A_1\}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the definition before Theorem 4.

Formalized by `MetaMathlibExt.ZModAffinelyEquivalent`, a definition declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#zmod-affinely-equivalent).

## Affine equivalence is reflexive

For every natural number $M$, every subset $A$ of
$\mathbb{Z}/M\mathbb{Z}$ is affinely equivalent to itself (take $d = 1$ and $s = 0$).

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the definition before Theorem 4.

Formalized by `MetaMathlibExt.zModAffinelyEquivalent_refl`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#z-mod-affinely-equivalent-refl).

## Maximum size of a $B_h$-set in $\{1, \dots, n\}$

For natural numbers $h$ and $n$, $R_h(n)$
is the largest number of elements of a $B_h$-set of natural numbers contained in
$\{1, \dots, n\}$. If no $B_h$-set is contained in $\{1, \dots, n\}$ (for example when $n = 0$),
then $R_h(n) = 0$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the paragraph before Theorem 5.

Formalized by `MetaMathlibExt.bhMaxCard`, a definition declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card).

## Shortest interval containing a $B_h$-set of given size

For natural numbers $h$ and $k$,
$R_h^{-1}(k)$ is the smallest natural number $n$ such that some $B_h$-set of natural numbers with
exactly $k$ elements is contained in $\{1, \dots, n\}$; it is $0$ when no such $n$ exists, for
example when $k = 0$, since a $B_h$-set is nonempty.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the paragraph before Theorem 5.

Formalized by `MetaMathlibExt.bhMinLength`, a definition declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length).

## $R_h(n)$ is at most $n$

For all natural numbers $h$ and $n$, let $R_h(n)$ be the largest
size of a $B_h$-set contained in $\{1, \dots, n\}$, or $0$ if there is no such set (for example
when $h = 0$ or $n = 0$). Then $R_h(n) \le n$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the definition of `R_h(n)` before Theorem 5.

Formalized by `MetaMathlibExt.bhMaxCard_le`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-le).

## $R_h(1) = 1$

For every natural number $h \ge 1$, the largest size $R_h(1)$ of a $B_h$-set
contained in $\{1\}$ equals $1$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the definition of `R_h(n)` before Theorem 5.

Formalized by `MetaMathlibExt.bhMaxCard_one`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-one).

## The shortest interval holding a one-element $B_h$-set

For every natural number
$h \ge 1$, the smallest natural number $n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with
exactly one element is $1$; that is, $R_h^{-1}(1) = 1$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, the paragraph before Theorem 7 ("Clearly, `R_h⁻¹(1) = 1`").

Formalized by `MetaMathlibExt.bhMinLength_one`, a theorem declared in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length-one).

## Bose's construction of $B_h$-sets

Let $h \ge 2$, let $F$ be a finite field with $q$
elements, let $K$ be a field extension of $F$ of degree $h$, let $\theta$ be a generator of the
multiplicative group $K^\times$, and let $b$ be a natural number such that $\theta^b$ has degree
$h$ over $F$. Then the generalized Bose set $\mathrm{Bose}_h(q, b)$, a subset of
$\mathbb{Z}/(q^h - 1)\mathbb{Z}$, is a $B_h$-set with exactly $q$ elements.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 3 (first sentence) (`jis-2024-24.1.2-thm-3`).

Stated but not proved: `MetaMathlibExt.isBhSet_boseSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#is-bh-set-bose-set).

## Singer's construction of $B_h$-sets

Let $h \ge 2$, let $F$ be a finite field with $q$
elements, let $K$ be a field extension of $F$ of degree $h + 1$, let $\theta$ be a generator of
the multiplicative group $K^\times$, and let $b$ be a natural number such that $\theta^b$ has
degree $h + 1$ over $F$. Then the generalized Singer set $\mathrm{Singer}_h(q, b)$, a subset of
$\mathbb{Z}/M\mathbb{Z}$ with $M = (q^{h+1} - 1)/(q - 1)$, is a $B_h$-set with exactly $q + 1$
elements.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 3 (second sentence) (`jis-2024-24.1.2-thm-3`).

Stated but not proved: `MetaMathlibExt.isBhSet_singerSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#is-bh-set-singer-set).

## Affine equivalences between Bose sets

Let $F$ be a finite field with $q$ elements and
characteristic $p$, let $h \ge 2$, let $K$ be a field extension of $F$ of degree $h$, and let
$\theta \in K$ have order $|K| - 1$, that is, generate $K^\times$. Let $b$ and $e$ be natural
numbers such that the minimal polynomials of $\theta^b$ and $\theta^e$ over $F$ both have
degree $h$. Suppose that (i) $b \equiv e \pmod{(q^h - 1)/(q - 1)}$, or
(ii) $\theta^b - \theta^e \in F$, or (iii) $b \equiv p^i e \pmod{q^h - 1}$ for some natural
number $i$. Then the Bose sets $\mathrm{Bose}_h(q, b)$ and $\mathrm{Bose}_h(q, e)$ built from
$F$, $K$ and $\theta$ are affinely equivalent.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 4 (items (i)–(iii)) (`jis-2024-24.1.2-thm-4`).

Stated but not proved: `MetaMathlibExt.zModAffinelyEquivalent_boseSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#z-mod-affinely-equivalent-bose-set).

## Affine equivalences between Singer sets

Let $F$ be a finite field with $q$ elements and
characteristic $p$, let $h \ge 2$, let $K$ be a field extension of $F$ of degree $h + 1$, and
let $\theta \in K$ have order $|K| - 1$, that is, generate $K^\times$. Put
$M = (q^{h+1} - 1)/(q - 1)$. Let $b$ and $e$ be natural numbers such that the minimal
polynomials of $\theta^b$ and $\theta^e$ over $F$ both have degree $h + 1$. Suppose that
(iv) $b \equiv e \pmod{M}$, or (v) $b \equiv p^i e \pmod{q^{h+1} - 1}$ for some natural number
$i$, or (vi) $\theta^b - \theta^e \in F$, or (vii) $r\theta^b + t\theta^{e+b} + w\theta^e \in F$
for some $r, t, w \in F$ with $r$ and $t$ not both $0$. Then the Singer sets
$\mathrm{Singer}_h(q, b)$ and $\mathrm{Singer}_h(q, e)$ built from $F$, $K$ and $\theta$ are
affinely equivalent.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 4 (items (iv)–(vii)) (`jis-2024-24.1.2-thm-4`).

Stated but not proved: `MetaMathlibExt.zModAffinelyEquivalent_singerSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#z-mod-affinely-equivalent-singer-set).

## Unconditional bounds for $R_h(n)$ and $R_h^{-1}(k)$

Let $h \ge 2$. Write $R_h(n)$ for the
largest size of a $B_h$-set contained in $\{1, \dots, n\}$, with $R_h(0) = 0$, and $R_h^{-1}(k)$
for the least $n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$ elements, with
$R_h^{-1}(0) = 0$ (a $B_h$-set is nonempty). Then every natural number $n$ satisfies
$R_h(n) \ge n^{1/h} - 2^{44} n^{154/(155h)}$, and every natural number $k$ satisfies
$R_h^{-1}(k) \le k^h + 3^{155h} k^{h - 1/155}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 5(a) (`jis-2024-24.1.2-thm-5`).

Stated but not proved: `MetaMathlibExt.bhMaxCard_bhMinLength_bounds_unconditional` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-bh-min-length-bounds-uncondi).

## Bounds for $R_h(n)$ and $R_h^{-1}(k)$ beyond $e^{e^{34}}$

Let $h \ge 2$. Write $R_h(n)$ for
the largest size of a $B_h$-set contained in $\{1, \dots, n\}$ and $R_h^{-1}(k)$ for the least
$n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$ elements. Then every natural number
$n \ge e^{e^{34}}$ satisfies $R_h(n) \ge n^{1/h} - 7 n^{2/(3h)}$, and every natural number
$k \ge e^{e^{34}}$ satisfies $R_h^{-1}(k) \le k^h + (3k)^{h - 1/3}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 5(b) (`jis-2024-24.1.2-thm-5`).

Stated but not proved: `MetaMathlibExt.bhMaxCard_bhMinLength_bounds_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-bh-min-length-bounds-large).

## Eventual bounds for $R_h(n)$ and $R_h^{-1}(k)$

Let $h \ge 2$. Write $R_h(n)$ for the
largest size of a $B_h$-set contained in $\{1, \dots, n\}$ and $R_h^{-1}(k)$ for the least $n$
such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$ elements. Then
$R_h(n) \ge n^{1/h} - n^{21/(40h)}$ for all sufficiently large natural numbers $n$, and
$R_h^{-1}(k) \le k^h + 2^h k^{h - 19/40}$ for all sufficiently large natural numbers $k$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 5(c) (`jis-2024-24.1.2-thm-5`).

Stated but not proved: `MetaMathlibExt.bhMaxCard_bhMinLength_bounds_eventually` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-bh-min-length-bounds-eventua).

## Riemann Hypothesis bounds for $R_h(n)$ and $R_h^{-1}(k)$

Assume the Riemann Hypothesis
and let $h \ge 2$. Write $R_h(n)$ for the largest size of a $B_h$-set contained in
$\{1, \dots, n\}$, with $R_h(0) = 0$ (a $B_h$-set is nonempty), and $R_h^{-1}(k)$ for the least
$n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$ elements, and let $\log$ be the
natural logarithm, with the convention $\log 0 = 0$. Then every natural number $k \ge 1$
satisfies $R_h^{-1}(k) < k^h + \log(20k)\, k^{h - 1/2} + 2 k^{h - 1} (\log(20k))^{2h}$, and
every natural number $n$ satisfies $R_h(n) \ge n^{1/h} - (7 + (\log n)/h)\, n^{1/(2h)}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 5(d) (`jis-2024-24.1.2-thm-5`).

Stated but not proved: `MetaMathlibExt.bhMaxCard_bhMinLength_bounds_of_RH` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-max-card-bh-min-length-bounds-of-rh).

## Cully-Hugill's theorem for 155th powers

For every natural number $n \ge 1$ there is a
prime $p$ with $n^{155} < p < (n + 1)^{155}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 6 (Cully-Hugill) (`jis-2024-24.1.2-thm-6`).

Stated but not proved: `MetaMathlibExt.exists_prime_between_pow_155` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#exists-prime-between-pow-155).

## Unconditional bounds for $R_h^{-1}(k)$, $k \ge 4$, and $R_h(n)$, $n \ge h + 3$

Let
$h \ge 2$. Write $R_h(n)$ for the largest size of a $B_h$-set contained in $\{1, \dots, n\}$ and
$R_h^{-1}(k)$ for the least $n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$
elements. Then every natural number $k \ge 4$ satisfies
$R_h^{-1}(k) < k^h + 3^{155h} k^{h - 1/155}$, and every natural number $n \ge h + 3$ satisfies
$R_h(n) \ge n^{1/h} - 2^{44} n^{154/(155h)}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 7 (`jis-2024-24.1.2-thm-7`).

Stated but not proved: `MetaMathlibExt.bhMinLength_lt_and_bhMaxCard_ge_explicit` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length-lt-and-bh-max-card-ge-expl).

## Cully-Hugill's theorem for cubes

For every natural number $n > \exp(\exp(32.537))$ there
is a prime $p$ with $n^3 < p < (n + 1)^3$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 8 (Cully-Hugill) (`jis-2024-24.1.2-thm-8`).

Stated but not proved: `MetaMathlibExt.exists_prime_between_cubes_of_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#exists-prime-between-cubes-of-large).

## Strict bounds for thick $B_h$-sets beyond $e^{e^{34}}$

Let $h \ge 2$. For natural
numbers $n$ and $k$, let $R_h(n)$ be the largest size of a $B_h$-set of natural numbers contained
in $\{1, \dots, n\}$, and let $R_h^{-1}(k)$ be the smallest $n$ such that $\{1, \dots, n\}$
contains a $B_h$-set with exactly $k$ elements. Then every natural number $k > e^{e^{34}}$
satisfies $R_h^{-1}(k) < k^h + (3k)^{h - 1/3}$, and every natural number $n > e^{e^{34}}$
satisfies $R_h(n) > n^{1/h} - 7 n^{2/(3h)}$.

The printed theorem leaves $n$ unquantified; the hypothesis on $n$ is taken from Theorem 5(b).

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 9 (`jis-2024-24.1.2-thm-9`).

Stated but not proved: `MetaMathlibExt.bhMinLength_lt_and_bhMaxCard_gt_large` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length-lt-and-bh-max-card-gt-larg).

## Baker–Harman–Pintz theorem

There is a real number $x_0$ such that for every real
$x \ge x_0$ there is a prime $p$ with $x - x^{21/40} \le p \le x$ and a prime $p'$ with
$x \le p' \le x + x^{21/40}$.

This is the form quoted in the paper, which prints the first interval as $[x - x^{21/40}, n]$
with $n$ undefined; the right endpoint is read as $x$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 10 (Baker, Harman and Pintz) (`jis-2024-24.1.2-thm-10`).

Stated but not proved: `MetaMathlibExt.eventually_exists_prime_short_intervals` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#eventually-exists-prime-short-intervals).

## Eventual strict upper bound for $R_h^{-1}(k)$ and lower bound for $R_h(n)$

Let $h \ge 2$.
Write $R_h(n)$ for the largest size of a $B_h$-set contained in $\{1, \dots, n\}$ and
$R_h^{-1}(k)$ for the least $n$ such that $\{1, \dots, n\}$ contains a $B_h$-set with $k$
elements. Then $R_h^{-1}(k) < k^h + 2^h k^{h - 19/40}$ for all sufficiently large natural
numbers $k$, and $R_h(n) \ge n^{1/h} - n^{21/(40h)}$ for all sufficiently large natural
numbers $n$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 11 (`jis-2024-24.1.2-thm-11`).

Stated but not proved: `MetaMathlibExt.bhMinLength_lt_and_bhMaxCard_ge_eventually` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length-lt-and-bh-max-card-ge-even).

## Dudek–Grenié–Molteni theorem

Assume the Riemann Hypothesis. Then for every natural
number $n \ge 2$ there is a prime $p$ with
$n^2 < p < \bigl(n + (1 + 1/\log n)^2 \log n\bigr)^2$, where $\log$ is the natural logarithm.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 12 (`jis-2024-24.1.2-thm-12`).

Stated but not proved: `MetaMathlibExt.exists_prime_between_sq_of_RH` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#exists-prime-between-sq-of-rh).

## Riemann Hypothesis bounds for $R_h^{-1}(k)$, $k \ge 4$, and $R_h(n)$, $n \ge h + 3$

Assume
the Riemann Hypothesis and let $h \ge 2$. Write $R_h(n)$ for the largest size of a $B_h$-set
contained in $\{1, \dots, n\}$ and $R_h^{-1}(k)$ for the least $n$ such that $\{1, \dots, n\}$
contains a $B_h$-set with $k$ elements, and let $\log$ be the natural logarithm. Then every
natural number $k \ge 4$ satisfies
$R_h^{-1}(k) < k^h + \log(20k)\, k^{h - 1/2} + 2 k^{h - 1} (\log(20k))^{2h}$, and every natural
number $n \ge h + 3$ satisfies $R_h(n) \ge n^{1/h} - (7 + (\log n)/h)\, n^{1/(2h)}$.

## Sources

- Kevin O'Bryant, *Constructing Thick `B_h`-Sets*, Journal of Integer Sequences 27 (2024), Article 24.1.2, Theorem 13 (`jis-2024-24.1.2-thm-13`).

Stated but not proved: `MetaMathlibExt.bhMinLength_lt_and_bhMaxCard_ge_of_RH` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ThickBhSetsWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html#bh-min-length-lt-and-bh-max-card-ge-of-r).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Constructions of thick B_h-sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/constructions-of-thick-b-h-sets)
