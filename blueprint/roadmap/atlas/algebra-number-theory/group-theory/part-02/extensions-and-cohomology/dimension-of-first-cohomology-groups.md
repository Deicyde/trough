---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.IsAbsolutelyIrreducible, MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.firstCohomologyDimAtMostTwo, MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.firstCohomologyDimAtMostTwo_refuted
statement: formalized
---

# Dimension of first cohomology groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups/index.html).

## Absolutely irreducible representations

A representation $\rho$ of a group $G$ on a vector
space $V$ over a field $k$ is absolutely irreducible when $V \neq 0$, the only $G$-invariant
subspaces of $V$ are $0$ and $V$, and every $k$-linear endomorphism of $V$ commuting with
$\rho(g)$ for all $g \in G$ is a scalar multiple of the identity.

For a finite-dimensional irreducible module this is equivalent to irreducibility over an algebraic
closure of $k$.

Formalized by `MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.IsAbsolutelyIrreducible`, a definition declared in [WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups/index.html#is-absolutely-irreducible).

## Mazurov's question on first cohomology (Kourovka 16.55)

The proposition that for every
field $k$, every finite group $G$ and every faithful absolutely irreducible representation $\rho$
of $G$ on a finite-dimensional $k$-vector space $V$, the first cohomology group $H^1(G, V)$ has
dimension at most $2$ over $k$.

Formalized by `MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.firstCohomologyDimAtMostTwo`, a definition declared in [WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups/index.html#first-cohomology-dim-at-most-two).

## Mazurov's question on first cohomology (Kourovka 16.55) has a negative answer

There exist a
field $k$, a finite group $G$ and a faithful absolutely irreducible representation of $G$ on a
finite-dimensional $k$-vector space $V$ such that the first cohomology group $H^1(G, V)$ has
dimension greater than $2$ over $k$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.55 (V. D. Mazurov); resolution: L. L. Scott, J. Algebra 260 (2003), 416-425; J. N. Bray and R. A. Wilson, J. Group Theory 11 (2008), 669-673, Kourovka Archive, Problem 16.55 (No, it is not).

Stated but not proved: `MathlibExt.GroupTheory.FirstCohomologyDimensionKourovka16Problem55Wanted.firstCohomologyDimAtMostTwo_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FirstCohomologyDimensionKourovka16Problem55Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups/index.html#first-cohomology-dim-at-most-two-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dimension of first cohomology groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/extensions-and-cohomology/dimension-of-first-cohomology-groups)
