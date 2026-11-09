# Grothendieck topology

A **Grothendieck topology** on a [category](category.md) specifies, for each
object, which collections of morphisms into it count as coverings of that object. It
abstracts the way the open subsets of a [topological space](../../topology/general-topology/part-01/topological-space.md) cover
larger open sets, keeping only the formal properties that the notion of a sheaf needs. A
category equipped with a Grothendieck topology is called a site, and sheaves on sites are the
setting for étale cohomology, for descent theory and for topos theory.

## Definition

Let $C$ be a category and $X$ an object of $C$. A
[sieve on $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sieves/Basic.html#CategoryTheory.Sieve) is a collection $S$ of morphisms with target $X$
that is closed under precomposition: if $f \colon Y \to X$ lies in $S$, then so does
$f \circ g$ for every morphism $g \colon Z \to Y$. The maximal sieve on $X$ consists of all
morphisms into $X$. For a morphism $h \colon Y \to X$, the
[pullback of $S$ along $h$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sieves/Basic.html#CategoryTheory.Sieve.pullback) is the sieve on $Y$

$$h^*S = \{\, g \colon Z \to Y \;:\; h \circ g \in S \,\}.$$

A [Grothendieck topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology) $J$ on $C$ assigns to each
object $X$ a set $J(X)$ of sieves on $X$, the covering sieves, subject to three axioms:

1. [the maximal sieve on $X$ belongs to $J(X)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.top_mem);
2. if $S \in J(X)$ and $h \colon Y \to X$, then
   [$h^*S \in J(Y)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.pullback_stable);
3. if $S \in J(X)$ and $R$ is a sieve on $X$ such that $h^*R \in J(Y)$ for every $h \colon Y \to X$
   in $S$, then [$R \in J(X)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.transitive).

The first axiom says that the identity of $X$ alone covers $X$, the second that coverings restrict, and the third
that a sieve which covers locally on a covering covers outright.

A presheaf of sets on $C$ is a [functor](functor.md) $P$ from the opposite
category of $C$ to sets. It is a
[sheaf for $J$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/SheafOfTypes.html#CategoryTheory.Presieve.IsSheaf) when, for every covering sieve $S$ on $X$,
each compatible family of elements $x_f \in P(Y)$, one for each $f \colon Y \to X$ in $S$, comes
from exactly one element $t \in P(X)$, in the sense that $P(f)(t) = x_f$ for all $f$. Here compatible
means that $P(g)(x_f) = x_{f \circ g}$ for every $f$ in $S$ and every $g \colon Z \to Y$; because $S$ is a sieve, this is
equivalent to the pairwise condition that $P(g_1)(x_{f_1}) = P(g_2)(x_{f_2})$ whenever
$f_1 \circ g_1 = f_2 \circ g_2$, which is the form Mathlib uses. Sheaves form a [category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sheaf.html#CategoryTheory.Sheaf) of their own.

## Examples

- **Open covers.** The open subsets of a topological space $T$, ordered by inclusion, form a
  category with a morphism $V \to U$ exactly when $V \subseteq U$. In the
  [topology of open covers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Spaces.html#Opens.grothendieckTopology), a sieve on $U$ covers when every
  point of $U$ lies in some open $V$ belonging to the sieve. For presheaves of sets, being a sheaf
  for this topology is
  [the same as the classical gluing condition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sheaves/SheafCondition/UniqueGluing.html#TopCat.Presheaf.isSheaf_iff_isSheafUniqueGluing_types):
  every family of sections over a family of open sets that agree on pairwise intersections glues
  to a unique section over their union.
- **Trivial and discrete topologies.** In the
  [trivial topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.trivial) only the maximal sieves
  cover; it is the least topology, and for it
  [every presheaf is a sheaf](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sheaf.html#CategoryTheory.Presheaf.isSheaf_bot). In the
  [discrete topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.discrete) every sieve covers,
  including the empty one.
- **Dense topology.** In the [dense topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.dense) a
  sieve $S$ on $X$ covers when every morphism $f \colon Y \to X$ can be precomposed with some
  $g \colon Z \to Y$ so that $f \circ g$ lies in $S$.
- **Atomic topology.** If any two morphisms with a common target can be completed to a commuting
  square, which [holds in every category with pullbacks](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.right_ore_of_pullbacks),
  then the nonempty sieves form the [atomic topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.atomic).
- **Canonical topology.** The [canonical topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Canonical.html#CategoryTheory.Sheaf.canonicalTopology) is
  the finest topology for which every representable presheaf is a sheaf (see
  [Yoneda embedding](yoneda-embedding.md)), where finest means having the most covering
  sieves: [each representable presheaf is a sheaf for it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Canonical.html#CategoryTheory.Sheaf.isSheaf_yoneda_obj),
  and [any topology for which every representable presheaf is a sheaf is coarser than it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Canonical.html#CategoryTheory.GrothendieckTopology.Subcanonical.of_isSheaf_yoneda_obj).
  Topologies coarser than the canonical one are called subcanonical.
- **Schemes.** On the category of [schemes](../../geometry/algebraic-geometry/scheme.md), jointly surjective
  families of open immersions generate the [Zariski topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Sites/BigZariski.html#AlgebraicGeometry.Scheme.zariskiTopology),
  and jointly surjective families of étale morphisms generate the
  [étale topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Sites/Etale.html#AlgebraicGeometry.Scheme.etaleTopology), which
  [is finer than the Zariski topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/Sites/Etale.html#AlgebraicGeometry.Scheme.zariskiTopology_le_etaleTopology):
  every Zariski-covering sieve is étale-covering.

## Properties

A sieve containing a covering sieve
[is itself covering](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.superset_covering): if $S \subseteq R$
and $S$ covers, apply the third axiom to $S$ and $R$, using that
[$h$ lies in a sieve exactly when the pullback of that sieve along $h$ is maximal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sieves/Basic.html#CategoryTheory.Sieve.mem_iff_pullback_eq_top).
The intersection of two sieves
[covers exactly when both of them do](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.intersection_covering_iff),
so the covering sieves on each object are closed under enlargement and under finite
intersections.

Topologies on a fixed category are ordered by inclusion:
[$J \le K$ means that every $J$-covering sieve is $K$-covering](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.le_def),
and $K$ is then called finer. The intersection of any family of topologies is again a topology,
so the topologies on $C$ form a complete lattice, with
[the trivial topology as its least element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.trivial_eq_bot)
and [the discrete topology as its greatest](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology.discrete_eq_top).
Refining a topology can only shrink the class of sheaves:
[a sheaf for a finer topology is a sheaf for a coarser one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Sheaf.html#CategoryTheory.Presheaf.IsSheaf.of_le).

Topologies are rarely written down sieve by sieve. In a category with pullbacks, a
[pretopology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Pretopology.html#CategoryTheory.Pretopology) prescribes covering families directly, and a sieve
is [declared covering when it contains a covering family](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Pretopology.html#CategoryTheory.Pretopology.toGrothendieck).
More generally, a [coverage](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Coverage.html#CategoryTheory.Coverage), a choice of covering families
required only to be compatible with pullback, [generates a topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Coverage.html#CategoryTheory.Coverage.toGrothendieck) by closing up under
the axioms.

## Related concepts

On a site whose underlying category is [small](small-category.md), the inclusion
of sheaves of sets into presheaves has a left [adjoint](adjunction.md),
sheafification, which preserves finite limits. A category equivalent to the category of sheaves of sets
on a small site is a Grothendieck topos. The sheaves used in [sheafed spaces](sheafed-space.md) are
sheaves for the topology of open covers.

## In Mathlib

Mathlib follows the saturated convention: a topology is a bundled structure that lists covering
sieves together with the three axioms, rather than covering families, and families enter only
through precoverages, pretopologies and coverages. A
[precoverage](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Precoverage.html#CategoryTheory.Precoverage) is just a choice of covering families on each
object, with no axioms, and it
[generates a topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/PrecoverageToGrothendieck.html#CategoryTheory.Precoverage.toGrothendieck),
[the smallest one in which the sieve generated by each covering family covers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/PrecoverageToGrothendieck.html#CategoryTheory.Precoverage.toGrothendieck_eq_sInf);
the Zariski and étale topologies on schemes are produced this way. No smallness is assumed, so the category of all schemes
carries its topologies directly. The names follow one common convention: the trivial topology,
also called indiscrete, is the least, and the discrete topology is the greatest. Sheaves are
defined for presheaves with values in any category, by asking that each functor of morphisms
from a fixed object into the presheaf be a sheaf of sets.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Category](category.md)
- [Functor](functor.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `CategoryTheory.GrothendieckTopology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Sites/Grothendieck.html#CategoryTheory.GrothendieckTopology)
- [Source of `CategoryTheory.GrothendieckTopology` in Mathlib/CategoryTheory/Sites/Grothendieck.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/CategoryTheory/Sites/Grothendieck.lean#L61)
- [Mathlib overview: General algebra › Category theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L18)
