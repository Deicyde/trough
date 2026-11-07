The **Galois correspondence**, also called the fundamental theorem of Galois theory,
says that for a finite Galois extension of [fields](trough:Field) $E/F$ the intermediate
fields of the extension are in one-to-one, inclusion-reversing correspondence with the
[subgroups](trough:Subgroup) of its Galois group. It turns questions about fields, which
can be infinite and hard to enumerate, into questions about a finite group, and it is the
basis of the classical applications of Galois theory, such as the
[insolvability of the general quintic by radicals](trough:AbelRuffini.exists_not_solvable_by_rad).

## Statement

Let $E/F$ be a field extension. Its Galois group $\mathrm{Gal}(E/F)$ is the group of
field automorphisms of $E$ that fix every element of $F$. The extension is Galois if it is
normal and separable: every element of $E$ is algebraic over $F$, and its
minimal polynomial over $F$ splits into linear factors in $E$ and has no repeated roots. For an extension of
finite degree, being Galois is equivalent to each of: the elements of
$E$ fixed by all of $\mathrm{Gal}(E/F)$ are exactly those of $F$; the group has exactly
$[E:F]$ elements, where the degree $[E:F]$ is the dimension of $E$ as a vector space over $F$; $E$ is the [splitting field](trough:Polynomial.SplittingField) of a
[separable polynomial](trough:Polynomial.Separable) over $F$.

To a subgroup $H$ of $\mathrm{Gal}(E/F)$ attach its
fixed field
$E^H = \{x \in E : \sigma(x) = x \text{ for all } \sigma \in H\}$, and to an intermediate
field $F \subseteq K \subseteq E$ attach the
subgroup of automorphisms fixing $K$ pointwise,
which is isomorphic to $\mathrm{Gal}(E/K)$
and is denoted that way. For any extension, $K \subseteq E^H$ holds
exactly when $H \subseteq \mathrm{Gal}(E/K)$,
so both maps reverse inclusions.

**Theorem.** If $E/F$ is a finite Galois extension, then $K \mapsto \mathrm{Gal}(E/K)$ and
$H \mapsto E^H$ are mutually inverse,
inclusion-reversing bijections between the
intermediate fields of $E/F$ and the subgroups of $\mathrm{Gal}(E/F)$. Moreover, if $K$
corresponds to $H$, then

$$|H| = [E:K], \qquad [K:F] = [\mathrm{Gal}(E/F) : H].$$

Both formulas are in Mathlib (the first,
the second); the right-hand
side of the second is the [index](trough:Subgroup.index) of $H$. Finally, $K$ is Galois over
$F$ if and only if $H$ is a normal subgroup of
$\mathrm{Gal}(E/F)$, and in that case
restriction to $K$ induces an isomorphism from the
[quotient group](trough:QuotientGroup.Quotient.group) $\mathrm{Gal}(E/F)/H$ onto $\mathrm{Gal}(K/F)$.

## Examples

- **A biquadratic field.** Let $E = \mathbb{Q}(\sqrt2, \sqrt3)$, the splitting field of
  $(x^2-2)(x^2-3)$ over $\mathbb{Q}$, of degree $4$. Its Galois group has four elements:
  the identity, $\sigma$ sending $\sqrt2$ to $-\sqrt2$ and fixing $\sqrt3$, $\tau$ sending
  $\sqrt3$ to $-\sqrt3$ and fixing $\sqrt2$, and $\sigma\tau$. It has five subgroups, and the correspondence pairs them with five
  fields: the trivial group with $E$, $\{1, \sigma\}$ with $\mathbb{Q}(\sqrt3)$,
  $\{1, \tau\}$ with $\mathbb{Q}(\sqrt2)$, $\{1, \sigma\tau\}$ with $\mathbb{Q}(\sqrt6)$,
  and the whole group with $\mathbb{Q}$. The group is abelian, so every intermediate field is
  Galois over $\mathbb{Q}$.
- **A cubic.** Let $E = \mathbb{Q}(\sqrt[3]{2}, \omega)$ with $\omega$ a primitive cube root
  of unity, the splitting field of $x^3 - 2$. It has degree $6$, and its Galois group permutes
  the three roots $\sqrt[3]{2}, \omega\sqrt[3]{2}, \omega^2\sqrt[3]{2}$ as the full symmetric
  group $S_3$. The three subgroups of order $2$ correspond to the cubic fields
  $\mathbb{Q}(\omega^i\sqrt[3]{2})$, none of them Galois over $\mathbb{Q}$, matching the fact
  that these subgroups are not normal. The normal subgroup of order $3$ corresponds to the
  quadratic field $\mathbb{Q}(\omega) = \mathbb{Q}(\sqrt{-3})$, which is Galois.

## Properties

- **Extreme cases.** The whole field $E$ corresponds to the
  trivial subgroup and $F$ to the
  whole group; for a finite Galois extension the
  fixed field of the whole group is $F$.
- **Lattice operations.** Since the bijection reverses order, it exchanges joins and meets:
  the subgroup fixing the compositum $KL$ is
  the intersection of the subgroups fixing $K$ and $L$.
- **Conjugation.** For $\sigma$ in the Galois group, the subgroup fixing $\sigma(K)$ is
  the conjugate $\sigma\,\mathrm{Gal}(E/K)\,\sigma^{-1}$,
  so conjugate subgroups correspond to conjugate fields, as in the cubic example.

## Proof

The two halves use different hypotheses. Let $H$ be a subgroup of $\mathrm{Gal}(E/F)$ with
$E/F$ finite. Every element of $H$ fixes $E^H$, so $H \subseteq \mathrm{Gal}(E/E^H)$. A finite
extension has at most as many automorphisms as its degree; applied to
$E/E^H$, which is finite because $E/F$ is, this bounds $|\mathrm{Gal}(E/E^H)|$ by $[E:E^H]$.
Artin's theorem gives $[E:E^H] = |H|$,
so $\mathrm{Gal}(E/E^H)$ has at most $|H|$ elements and
equals $H$. This half needs no Galois
hypothesis.

Conversely, let $K$ be an intermediate field. Clearly $K \subseteq E^{\mathrm{Gal}(E/K)}$.
Since $E$ is Galois over $F$, it is
also Galois over $K$, so
$|\mathrm{Gal}(E/K)| = [E:K]$ (the count for Galois extensions).
By Artin's theorem $E$ has the same degree $[E:K]$ over the larger field
$E^{\mathrm{Gal}(E/K)}$, and the tower law forces the two fields to be equal:
$K$ is the fixed field of $\mathrm{Gal}(E/K)$.
The two maps are therefore inverse, and they reverse inclusions.

## Generalizations

For a Galois extension of infinite degree, every intermediate field is still
the fixed field of its subgroup, but in general
not every subgroup arises this way. The Galois group carries a natural profinite topology, the
Krull topology, and intermediate fields correspond
bijectively to the closed subgroups.

For an arbitrary extension the two maps still form a Galois connection between ordered sets,
as the inclusion criterion in the statement shows; for an extension of finite degree, the
Galois condition is what makes them inverse bijections. Among the uses of the correspondence is
[the theorem that a polynomial solvable by radicals has a solvable Galois group](trough:isSolvable_gal_minpoly).

## In Mathlib

Mathlib packages the correspondence as an order isomorphism between the lattice of
intermediate fields and the order dual of the lattice of subgroups of the Galois group,
which records in one object that the two maps are inverse and reverse inclusions. The
subgroup attached to an intermediate field $K$ is a subgroup of $\mathrm{Gal}(E/F)$, not the
group $\mathrm{Gal}(E/K)$ itself; a separate isomorphism identifies the two. A Galois extension
is defined as a normal and separable one, with no finiteness condition, and separability
includes algebraicity, so finite degree is a separate hypothesis wherever the theorem needs
it. Several statements hold more generally than the textbook version: the degree formula
$[K:F] = [\mathrm{Gal}(E/F):H]$ and the equivalence between normal subgroups and Galois
subextensions are proved for Galois extensions of any degree, with the convention that the
degree of an infinite extension and the index of an infinite-index subgroup are both $0$.

## Depends on

- [Algebraic extension](trough:Algebra.IsAlgebraic)
- [Minimal polynomial](trough:minpoly)
- [Finite-dimensionality](trough:FiniteDimensional)
- [Index of a subgroup](trough:Subgroup.index)
- [Normal subgroup](trough:Subgroup.Normal)
- [Quotient group](trough:QuotientGroup.Quotient.group)
