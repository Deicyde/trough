A **Grothendieck topology** on a [category](trough:CategoryTheory.Category) specifies, for each
object, which collections of morphisms into it count as coverings of that object. It
abstracts the way the open subsets of a [topological space](trough:TopologicalSpace) cover
larger open sets, keeping only the formal properties that the notion of a sheaf needs. A
category equipped with a Grothendieck topology is called a site, and sheaves on sites are the
setting for étale cohomology, for descent theory and for topos theory.

## Definition

Let $C$ be a category and $X$ an object of $C$. A
sieve on $X$ is a collection $S$ of morphisms with target $X$
that is closed under precomposition: if $f \colon Y \to X$ lies in $S$, then so does
$f \circ g$ for every morphism $g \colon Z \to Y$. The maximal sieve on $X$ consists of all
morphisms into $X$. For a morphism $h \colon Y \to X$, the
pullback of $S$ along $h$ is the sieve on $Y$

$$h^*S = \{\, g \colon Z \to Y \;:\; h \circ g \in S \,\}.$$

A Grothendieck topology $J$ on $C$ assigns to each
object $X$ a set $J(X)$ of sieves on $X$, the covering sieves, subject to three axioms:

1. the maximal sieve on $X$ belongs to $J(X)$;
2. if $S \in J(X)$ and $h \colon Y \to X$, then
   $h^*S \in J(Y)$;
3. if $S \in J(X)$ and $R$ is a sieve on $X$ such that $h^*R \in J(Y)$ for every $h \colon Y \to X$
   in $S$, then $R \in J(X)$.

The first axiom says that the identity of $X$ alone covers $X$, the second that coverings restrict, and the third
that a sieve which covers locally on a covering covers outright.

A presheaf of sets on $C$ is a [functor](trough:CategoryTheory.Functor) $P$ from the opposite
category of $C$ to sets. It is a
sheaf for $J$ when, for every covering sieve $S$ on $X$,
each compatible family of elements $x_f \in P(Y)$, one for each $f \colon Y \to X$ in $S$, comes
from exactly one element $t \in P(X)$, in the sense that $P(f)(t) = x_f$ for all $f$. Here compatible
means that $P(g)(x_f) = x_{f \circ g}$ for every $f$ in $S$ and every $g \colon Z \to Y$; because $S$ is a sieve, this is
equivalent to the pairwise condition that $P(g_1)(x_{f_1}) = P(g_2)(x_{f_2})$ whenever
$f_1 \circ g_1 = f_2 \circ g_2$, which is the form Mathlib uses. Sheaves form a category of their own.

## Examples

- **Open covers.** The open subsets of a topological space $T$, ordered by inclusion, form a
  category with a morphism $V \to U$ exactly when $V \subseteq U$. In the
  topology of open covers, a sieve on $U$ covers when every
  point of $U$ lies in some open $V$ belonging to the sieve. For presheaves of sets, being a sheaf
  for this topology is
  the same as the classical gluing condition:
  every family of sections over a family of open sets that agree on pairwise intersections glues
  to a unique section over their union.
- **Trivial and discrete topologies.** In the
  trivial topology only the maximal sieves
  cover; it is the least topology, and for it
  every presheaf is a sheaf. In the
  discrete topology every sieve covers,
  including the empty one.
- **Dense topology.** In the dense topology a
  sieve $S$ on $X$ covers when every morphism $f \colon Y \to X$ can be precomposed with some
  $g \colon Z \to Y$ so that $f \circ g$ lies in $S$.
- **Atomic topology.** If any two morphisms with a common target can be completed to a commuting
  square, which holds in every category with pullbacks,
  then the nonempty sieves form the atomic topology.
- **Canonical topology.** The canonical topology is
  the finest topology for which every representable presheaf is a sheaf (see
  [Yoneda embedding](trough:CategoryTheory.yoneda)), where finest means having the most covering
  sieves: each representable presheaf is a sheaf for it,
  and any topology for which every representable presheaf is a sheaf is coarser than it.
  Topologies coarser than the canonical one are called subcanonical.
- **Schemes.** On the category of [schemes](trough:AlgebraicGeometry.Scheme), jointly surjective
  families of open immersions generate the Zariski topology,
  and jointly surjective families of étale morphisms generate the
  étale topology, which
  is finer than the Zariski topology:
  every Zariski-covering sieve is étale-covering.

## Properties

A sieve containing a covering sieve
is itself covering: if $S \subseteq R$
and $S$ covers, apply the third axiom to $S$ and $R$, using that
$h$ lies in a sieve exactly when the pullback of that sieve along $h$ is maximal.
The intersection of two sieves
covers exactly when both of them do,
so the covering sieves on each object are closed under enlargement and under finite
intersections.

Topologies on a fixed category are ordered by inclusion:
$J \le K$ means that every $J$-covering sieve is $K$-covering,
and $K$ is then called finer. The intersection of any family of topologies is again a topology,
so the topologies on $C$ form a complete lattice, with
the trivial topology as its least element
and the discrete topology as its greatest.
Refining a topology can only shrink the class of sheaves:
a sheaf for a finer topology is a sheaf for a coarser one.

Topologies are rarely written down sieve by sieve. In a category with pullbacks, a
pretopology prescribes covering families directly, and a sieve
is declared covering when it contains a covering family.
More generally, a coverage, a choice of covering families
required only to be compatible with pullback, generates a topology by closing up under
the axioms.

## Related concepts

On a site whose underlying category is [small](trough:CategoryTheory.SmallCategory), the inclusion
of sheaves of sets into presheaves has a left [adjoint](trough:CategoryTheory.Adjunction),
sheafification, which preserves finite limits. A category equivalent to the category of sheaves of sets
on a small site is a Grothendieck topos. The sheaves used in [sheafed spaces](trough:AlgebraicGeometry.SheafedSpace) are
sheaves for the topology of open covers.

## In Mathlib

Mathlib follows the saturated convention: a topology is a bundled structure that lists covering
sieves together with the three axioms, rather than covering families, and families enter only
through precoverages, pretopologies and coverages. A
precoverage is just a choice of covering families on each
object, with no axioms, and it
generates a topology,
the smallest one in which the sieve generated by each covering family covers;
the Zariski and étale topologies on schemes are produced this way. No smallness is assumed, so the category of all schemes
carries its topologies directly. The names follow one common convention: the trivial topology,
also called indiscrete, is the least, and the discrete topology is the greatest. Sheaves are
defined for presheaves with values in any category, by asking that each functor of morphisms
from a fixed object into the presheaf be a sheaf of sets.

## Depends on

- [Category](trough:CategoryTheory.Category)
- [Functor](trough:CategoryTheory.Functor)
- [Set](trough:Set)
