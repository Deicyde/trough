---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.HasNormalSeriesInfiniteCyclicFactors, MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.polyInfiniteCyclicHasOuterAutomorphism, MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.polyInfiniteCyclicHasOuterAutomorphism_refuted
statement: formalized
---

# Outer automorphisms of poly-infinite-cyclic groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou/index.html).

## Normal series with infinite cyclic factors

A group $G$ has a normal series with infinite
cyclic factors when there are a natural number $n$ and subgroups
$1 = H_0 \le H_1 \le \cdots \le H_n = G$, each normal in $G$, such that every factor
$H_{i+1}/H_i$ is infinite cyclic.

Formalized by `MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.HasNormalSeriesInfiniteCyclicFactors`, a definition declared in [WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou/index.html#has-normal-series-infinite-cyclic-factor).

## Outer automorphisms of groups with an infinite cyclic normal series (Kourovka 13.23)

The
conjecture that every nontrivial group with a normal series with infinite cyclic factors has an
automorphism that is not inner.

This is Kourovka Problem 13.23 (F. de Giovanni).

Formalized by `MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.polyInfiniteCyclicHasOuterAutomorphism`, a definition declared in [WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou/index.html#poly-infinite-cyclic-has-outer-automorph).

## Only inner automorphisms despite an infinite cyclic normal series (Kourovka 13.23 refuted)

There is a nontrivial group $G$ with a normal series with infinite cyclic factors such that every
automorphism of $G$ is inner. So the conjecture of Kourovka Problem 13.23 is false.

Brescia, Ingrosso and Trombetti construct a torsion-free group $G$ of Hirsch length $14$ with a
series $1 = G_0 \trianglelefteq \cdots \trianglelefteq G_{14} = G$ of normal subgroups of $G$
with infinite cyclic factors and $\mathrm{Out}(G) = 1$; the Kourovka Notebook (21st issue)
marks 13.23 solved, "No, not always".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 13.23 (F. de Giovanni); resolution: M. Brescia, E. Ingrosso and M. Trombetti, A torsion-free supersoluble group with trivial outer automorphism group, preprint (2026), arXiv:2607.11775, abstract: a torsion-free group of Hirsch length 14 with a series 1 = G_0 ◁ ⋯ ◁ G_14 = G of normal subgroups of G with infinite cyclic factors and Out(G) = 1; the Kourovka Notebook (21st issue) marks 13.23 solved, https://arxiv.org/abs/2607.11775.

Stated but not proved: `MathlibExt.GroupTheory.PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.polyInfiniteCyclicHasOuterAutomorphism_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PolyInfiniteCyclicOuterAutomorphismKourovka13Problem23Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou/index.html#poly-infinite-cyclic-has-outer-automorph-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Outer automorphisms of poly-infinite-cyclic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/outer-automorphisms-of-poly-infinite-cyclic-grou)
