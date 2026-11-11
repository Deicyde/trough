---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.pRegularOrbitsImplyRegularOrbit, MathlibExt.GroupTheory.PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.pRegularOrbitsImplyRegularOrbit_refuted
statement: formalized
---

# Regular orbits of linear groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/regular-orbits-of-linear-groups/index.html).

## Zhang's question on regular orbits from $p$-regular orbits

The statement that for every
finite field $F$, every nonzero finite-dimensional vector space $V$ over $F$ and every finite group
$G$ acting faithfully on $V$ by $F$-linear maps, if the only $G$-invariant subspaces of $V$ are $0$
and $V$, and for every prime $p$ some vector of $V$ has a stabilizer in $G$ of order prime to $p$
(a $p$-regular orbit), then some vector of $V$ has trivial stabilizer in $G$ (a regular orbit).

This is Kourovka Notebook Problem 12.25 (Jiping Zhang).

Formalized by `MathlibExt.GroupTheory.PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.pRegularOrbitsImplyRegularOrbit`, a definition declared in [WantedExt/GroupTheory/PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/regular-orbits-of-linear-groups/index.html#p-regular-orbits-imply-regular-orbit).

## $p$-regular orbits for every prime do not force a regular orbit

There exist a finite field $F$,
a nonzero finite-dimensional vector space $V$ over $F$ and a finite group $G$ acting faithfully on
$V$ by $F$-linear maps such that the only $G$-invariant subspaces of $V$ are $0$ and $V$ and, for
every prime $p$, some vector of $V$ has a stabilizer in $G$ of order prime to $p$, but no vector of
$V$ has trivial stabilizer in $G$.

Resolved false: the Kourovka Archive answers 12.25 "No, not always" (V. I. Zenkov). Write
$\mathbb{Z}_n$ for the cyclic group of order $n$, $A_4$ for the alternating group of degree $4$ and
$\mathbb{F}_2$ for the field with two elements. Let $H = A_4 \wr \mathbb{Z}_5$ be the wreath
product, let $V = O_2(H)$ be the largest normal $2$-subgroup of $H$, so $V \cong \mathbb{F}_2^{10}$,
and let $G \cong \mathbb{Z}_3 \wr \mathbb{Z}_5$ be a complement to $V$ in $H$. The faithful
irreducible action of $G$ on $V$ by conjugation has orbits with stabilizers of order $5$ and of
order $3$, hence $p$-regular orbits for every prime $p$, but no regular orbit, since
$|G| = 1215 > 1024 = |V|$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.25 (Jiping Zhang); resolution: V. I. Zenkov, letter of 11 February 1994, as recorded in the Kourovka Archive, Problem 12.25, Archive answer: No, not always; H = A_4 ≀ Z_5, V = O_2(H), G a complement to V acting by conjugation, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.pRegularOrbitsImplyRegularOrbit_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PRegularOrbitsRegularOrbitKourovka12Problem25Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/regular-orbits-of-linear-groups/index.html#p-regular-orbits-imply-regular-orbit-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular orbits of linear groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/regular-orbits-of-linear-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/regular-orbits-of-linear-groups)
