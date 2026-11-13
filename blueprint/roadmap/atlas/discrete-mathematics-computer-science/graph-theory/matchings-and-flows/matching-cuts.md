---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MatchingCutGirthWanted.avgDegree, MathlibExt.Combinatorics.MatchingCutGirthWanted.HasMatchingCut, MathlibExt.Combinatorics.MatchingCutGirthWanted.conjecture, MathlibExt.Combinatorics.MatchingCutGirthWanted.conjecture_refuted
statement: formalized
---

# Matching cuts

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html).

## Average degree of a finite graph

For a simple graph $G$ on a finite vertex set $V$ with
edge set $E$, the average degree of $G$ is the rational number $2|E|/|V|$; it equals $0$ when $V$
is empty.

Formalized by `MathlibExt.Combinatorics.MatchingCutGirthWanted.avgDegree`, a definition declared in [WantedExt/Combinatorics/MatchingCutGirthWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MatchingCutGirthWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html#avg-degree).

## Matching cut

A simple graph $G$ has a matching cut if some matching $M$ of $G$, that is,
a set of pairwise disjoint edges of $G$, is such that deleting the edges of $M$ from $G$ leaves
two vertices $u$ and $v$ that are not joined by any path. The matching may be empty, in which
case this says that $G$ itself has two vertices not joined by any path.

Formalized by `MathlibExt.Combinatorics.MatchingCutGirthWanted.HasMatchingCut`, a definition declared in [WantedExt/Combinatorics/MatchingCutGirthWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MatchingCutGirthWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html#has-matching-cut).

## Matching cut and girth question, affirmative form

For every real number $d$ there is a
natural number $g$ such that every simple graph $G$ on a finite vertex set with at least two
vertices, whose average degree is less than $d$ and whose girth is at least $g$, has a matching
cut. An acyclic graph has infinite girth, so it meets the girth bound for every $g$.

## Sources

- [OPG-37364], Open Problem Garden, "Matching cut and girth".

Formalized by `MathlibExt.Combinatorics.MatchingCutGirthWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/MatchingCutGirthWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MatchingCutGirthWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html#conjecture).

## Negative answer to the matching cut and girth question

It is not the case that for
every real number $d$ there is a natural number $g$ such that every simple graph on a finite
vertex set with at least two vertices, average degree less than $d$ and girth at least $g$ has a
matching cut. That is, there is a real number $d$ such that for every natural number $g$ some
simple graph on a finite vertex set with at least two vertices, average degree less than $d$ and
girth at least $g$ has no matching cut.

Feghali, Lucke, Paulusma and Ries (Lemma 5) construct, for every $g$, a connected 14-regular
bipartite graph of girth at least $g$ with no matching cut; these graphs give $d = 15$.

## Sources

- C. Feghali, F. Lucke, D. Paulusma and B. Ries, Matching Cuts in Graphs of High Girth and H-Free Graphs, ISAAC 2023, arXiv:2212.12317, https://arxiv.org/abs/2212.12317.

Stated but not proved: `MathlibExt.Combinatorics.MatchingCutGirthWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/MatchingCutGirthWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MatchingCutGirthWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matching cuts](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/matching-cuts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/matchings-and-flows/matching-cuts)
