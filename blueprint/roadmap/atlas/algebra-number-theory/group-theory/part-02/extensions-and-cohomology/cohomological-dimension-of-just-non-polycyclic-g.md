---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.baseRelators, MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.twistRelators, MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.KrophollerGroup, MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.rationalCohomologicalDimensionEqFour, MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.rationalCohomologicalDimensionEqFour_holds
statement: formalized
---

# Cohomological dimension of just-non-polycyclic groups

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html).

## Base relators of the Kropholler group

Let $F$ be the free group on $x, y$, viewed inside
the free group on $x, y, t$. The base relators are the elements $[[a, b], [c, d]]$ and $[a, b]^2$
for all $a, b, c, d \in F$.

These elements generate $F''(F')^2$ as a normal subgroup of $F$, so they are relators for
$K = F/F''(F')^2$.

Formalized by `MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.baseRelators`, a definition declared in [WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html#base-relators).

## Twist relators of the Kropholler group

In the free group on $x, y, t$, the twist relators
are the two elements $t x t^{-1} y^{-1}$ and $t y t^{-1} (x y)^{-1}$; they encode the relations
$t x t^{-1} = y$ and $t y t^{-1} = x y$, so conjugation by $t$ acts as the automorphism
$\varphi \colon x \mapsto y,\ y \mapsto x y$.

Formalized by `MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.twistRelators`, a definition declared in [WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html#twist-relators).

## The Kropholler group

The Kropholler group $G$ is the group with generators $x, y, t$ whose
relators are the base relators, namely $[[a, b], [c, d]]$ and $[a, b]^2$ for all $a, b, c, d$ in
the free group $F$ on $x, y$, together with the twist relators $t x t^{-1} y^{-1}$ and
$t y t^{-1} (x y)^{-1}$.

With $K = F/F''(F')^2$ and $\varphi$ the automorphism $x \mapsto y$, $y \mapsto x y$ of $K$, this is
the mapping torus of $\varphi$, that is, the semidirect product $K \rtimes \langle \varphi \rangle$
($\varphi$ has infinite order on $K$).

Formalized by `MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.KrophollerGroup`, an abbreviation declared in [WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html#kropholler-group).

## Rational cohomological dimension 4 of the Kropholler group (Kourovka 12.41)

Let $G$ be
the Kropholler group. This is the proposition that $H^4(G, M) \neq 0$ for some $\mathbb{Q}G$-module
$M$, and $H^n(G, M) = 0$ for every $\mathbb{Q}G$-module $M$ and every integer $n > 4$; that is, the
cohomological dimension of $G$ over $\mathbb{Q}$ is $4$.

This is the answer to Kourovka Notebook Problem 12.41 (P. H. Kropholler).

Formalized by `MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.rationalCohomologicalDimensionEqFour`, a definition declared in [WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html#rational-cohomological-dimension-eq-four).

## The Kropholler group has rational cohomological dimension 4

Let $G$ be the Kropholler group.
Then $H^4(G, M) \neq 0$ for some $\mathbb{Q}G$-module $M$, and $H^n(G, M) = 0$ for every
$\mathbb{Q}G$-module $M$ and every integer $n > 4$. This resolves Kourovka Notebook Problem 12.41
by P. H. Kropholler, which asks whether this cohomological dimension is 3 or 4.

The Kourovka Notebook (21st issue) marks 12.41 solved: $G$ is not constructible, so by Theorem
III.8 of Bridson and Kropholler its cohomological dimension over $\mathbb{Q}$ is its homological
dimension plus 1, and the homological dimension is the Hirsch length 3 (U. Stammbach).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 12.41 (P. H. Kropholler); resolution: M. R. Bridson and P. H. Kropholler, J. Reine Angew. Math. 699 (2015), 217-243; U. Stammbach, J. London Math. Soc. (2) 2 (1970), 567-570, Theorem III.8 of Bridson-Kropholler (non-constructible groups: cd = hd + 1) and Stammbach (hd = Hirsch length = 3); the Kourovka Notebook (21st issue) marks 12.41 solved: it is 4.

Stated but not proved: `MathlibExt.GroupTheory.CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.rationalCohomologicalDimensionEqFour_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CohomologicalDimensionJustNonPolycyclicKourovka12Problem41Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html#rational-cohomological-dimension-eq-four-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cohomological dimension of just-non-polycyclic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/extensions-and-cohomology/cohomological-dimension-of-just-non-polycyclic-g)
