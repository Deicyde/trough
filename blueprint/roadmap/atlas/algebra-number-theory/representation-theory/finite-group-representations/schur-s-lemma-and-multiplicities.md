---
declaration: section
origin: cited
lean: CharacterTheory.finrank_intertwiningMap_eq_one_or_zero, CharacterTheory.multiplicity_eq_finrank_intertwiningMap
statement: formalized
proof: formalized
---

# Schur's lemma and multiplicities

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/schur-s-lemma-and-multiplicities/index.html).

## Schur's lemma, dimension form

Let $G$ be a finite group, $k$ an algebraically closed
field, and $\rho$, $\sigma$ irreducible representations of $G$ on finite-dimensional $k$-vector
spaces. Then the space $\operatorname{Hom}_G(\rho, \sigma)$ of intertwining maps from $\rho$ to
$\sigma$ has dimension $1$ over $k$ if $\sigma$ and $\rho$ are equivalent, and dimension $0$
otherwise.

Formalized by `CharacterTheory.finrank_intertwiningMap_eq_one_or_zero`, a theorem declared in [MathlibExt/RepresentationTheory/RepresentationMultiplicity.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/RepresentationMultiplicity.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/schur-s-lemma-and-multiplicities/index.html#finrank-intertwining-map-eq-one-or-zero).

## Multiplicity equals the dimension of the intertwining space

Let $G$ be a finite group,
$k$ an algebraically closed field, and $(\rho_i)_{i \in I}$ a family, indexed by a finite set $I$,
of irreducible representations of $G$ on finite-dimensional $k$-vector spaces that are pairwise
non-equivalent: $\rho_i$ and $\rho_j$ are not equivalent whenever $i \ne j$. Let $\sigma$ be a
representation of $G$ on a finite-dimensional $k$-vector space, and let $(d_i)_{i \in I}$ be
natural numbers such that $\sigma$ is equivalent to the direct sum of $d_i$ copies of $\rho_i$ over
all $i \in I$. Then for every $i \in I$, $d_i$ equals the dimension over $k$ of the space
$\operatorname{Hom}_G(\rho_i, \sigma)$ of intertwining maps from $\rho_i$ to $\sigma$.

Formalized by `CharacterTheory.multiplicity_eq_finrank_intertwiningMap`, a theorem declared in [MathlibExt/RepresentationTheory/RepresentationMultiplicity.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/RepresentationMultiplicity.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/schur-s-lemma-and-multiplicities/index.html#multiplicity-eq-finrank-intertwining-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur's lemma and multiplicities](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/schur-s-lemma-and-multiplicities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/finite-group-representations/schur-s-lemma-and-multiplicities)
