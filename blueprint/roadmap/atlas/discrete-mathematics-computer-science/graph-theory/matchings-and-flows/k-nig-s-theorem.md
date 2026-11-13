---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.KonigMatchingCoverWanted.konig_matching_cover_general, MathlibExt.Combinatorics.SimpleGraph.KonigMatchingCoverWanted.konig_matching_cover
statement: formalized
proof: formalized
---

# Kőnig's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/k-nig-s-theorem/index.html).

## Kőnig's theorem on a finite vertex type

Let $G$ be a bipartite simple graph on a finite
vertex type $V$. Then there are a matching $M$ in $G$ and a vertex cover $C \subseteq V$ of $G$ such
that the number of edges of $M$ equals the number of vertices in $C$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.KonigMatchingCoverWanted.konig_matching_cover_general`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/KonigMatchingCover.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/KonigMatchingCover.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/k-nig-s-theorem/index.html#konig-matching-cover-general).

## Kőnig's theorem for finite bipartite graphs

Every bipartite simple graph $G$ on a finite vertex
type $V$ has a matching $M$ and a vertex cover $C \subseteq V$ such that the number of edges of $M$
equals the number of vertices in $C$.

## Sources

- D. Kőnig (1931); J. Egerváry (1931) weighted form. It follows from `konig_matching_cover_general`; the instances `[DecidableEq V]` and `[DecidableRel G.Adj]` are unused and keep the source's shape.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.KonigMatchingCoverWanted.konig_matching_cover`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/KonigMatchingCover.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/KonigMatchingCover.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/k-nig-s-theorem/index.html#konig-matching-cover).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kőnig's theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/k-nig-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/matchings-and-flows/k-nig-s-theorem)
