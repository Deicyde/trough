---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.IsEverywhereUnramified, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.maximalUnramifiedProPF, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.MaxUnramifiedProPGaloisGroup, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.generatorRank, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.trivialZModpRep, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.relationRank, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.H2Finite, MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.shafarevich_relation_rank_bound
statement: formalized
---

# Class field towers

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html).

## Everywhere unramified extension

Let $M/F$ be an extension of number fields, with rings
of integers $\mathcal{O}_F$ and $\mathcal{O}_M$. Then $M/F$ is everywhere unramified when every
prime ideal $\mathfrak{P}$ of $\mathcal{O}_M$ lying over a nonzero prime ideal $\mathfrak{p}$
of $\mathcal{O}_F$ has ramification index $1$ over $\mathcal{O}_F$, and every infinite place of
$M$ lying over a real place of $F$ is real.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.IsEverywhereUnramified`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#is-everywhere-unramified).

## Maximal unramified pro-$p$ extension

Let $F$ be a number field, $\overline{F}$ an
algebraic closure of $F$, and $p$ a prime. The maximal unramified pro-$p$ extension
$F^{\mathrm{un},p}$ of $F$ is the compositum in $\overline{F}$ of all intermediate fields
$F \subseteq M \subseteq \overline{F}$ such that $M/F$ is finite, Galois and everywhere
unramified, and its Galois group $\mathrm{Gal}(M/F)$ is a $p$-group (each such $M$ is a
number field).

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.maximalUnramifiedProPF`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#maximal-unramified-pro-pf).

## Galois group of the maximal unramified pro-$p$ extension

For a number field $F$ and a
prime $p$, this is the group $\mathrm{Gal}(F^{\mathrm{un},p}/F)$ of field automorphisms of the
maximal unramified pro-$p$ extension $F^{\mathrm{un},p}$ of $F$ that fix $F$, under
composition and with the Krull topology.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.MaxUnramifiedProPGaloisGroup`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#max-unramified-pro-pgalois-group).

## Generator rank of a topological group

For a topological group $G$, the generator
rank $d(G)$ is the least natural number $k$ such that some finite subset $S \subseteq G$ with
$k$ elements generates a dense subgroup of $G$. If no finite subset of $G$ generates a dense
subgroup, then $d(G) = 0$ by convention.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.generatorRank`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#generator-rank).

## Trivial representation on $\mathbb{Z}/p\mathbb{Z}$

For a natural number $p$ and a
topological group $G$, this is $\mathbb{Z}/p\mathbb{Z}$ with the discrete topology, regarded as a
continuous representation of $G$ over $\mathbb{Z}/p\mathbb{Z}$ on which every element of $G$
acts as the identity.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.trivialZModpRep`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#trivial-zmodp-rep).

## Relation rank of a topological group

For a prime $p$ and a topological group $G$, the
relation rank $r(G)$ is the dimension over $\mathbb{F}_p$ of the continuous cohomology group
$H^2(G, \mathbb{F}_p)$ of degree $2$, with coefficients in the trivial representation of $G$ on
$\mathbb{F}_p$. If this space is infinite-dimensional, then $r(G) = 0$ by convention.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.relationRank`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#relation-rank).

## Finite-dimensional second cohomology mod $p$

For a prime $p$ and a topological group
$G$, this is the statement that the continuous cohomology group $H^2(G, \mathbb{F}_p)$ of degree
$2$, with coefficients in the trivial representation of $G$ on $\mathbb{F}_p$, is
finite-dimensional over $\mathbb{F}_p$.

Formalized by `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.H2Finite`, a definition declared in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#h2-finite).

## Shafarevich's relation-rank bound

Let $F$ be a number field, let $p$ be an odd prime,
and let $G = \mathrm{Gal}(F^{\mathrm{un},p}/F)$ be the Galois group of the maximal unramified
pro-$p$ extension of $F$. Write $d(G)$ for the generator rank and $r(G)$ for the relation rank
of $G$, $r_1$ and $r_2$ for the numbers of real and complex places of $F$, and $\delta$ for $1$
if $F$ contains a primitive $p$-th root of unity and $0$ otherwise. Then the continuous
cohomology group $H^2(G, \mathbb{F}_p)$ with trivial coefficients is finite-dimensional over
$\mathbb{F}_p$, and

$$r(G) \le d(G) + (r_1 + r_2 - 1) + \delta.$$

## Sources

- D. C. Mayer, *New number fields with known p-class tower*, Tatra Mt. Math. Publ. 64 (2015), 21–57 (Theorem 5.1, S=∅; arXiv:1510.00565); H. Koch, *Galois Theory of p-Extensions*, Springer 2002 (Theorems 11.5 and 11.8); I. R. Shafarevich, *Extensions with prescribed ramification points* (1963). Lean hypothesis: https://github.com/logical-intelligence/erdos-unit-distance (Hyp_ShafarevichRelationRankBound). Problem `shafarevich_relation_rank_bound` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ShafarevichRelationRankWanted.NumberTheory.shafarevich_relation_rank_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShafarevichRelationRankWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html#shafarevich-relation-rank-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Class field towers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/class-field-towers)
