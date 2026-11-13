---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.BrooksWanted.brooks, MathlibExt.Combinatorics.SimpleGraph.ErdosGirthChromaticWanted.erdos_high_girth_chromatic, MetaMathlibExt.five_color_theorem, MetaMathlibExt.mycielski_theorem
statement: formalized
---

# Graph coloring: its own results

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/index.html).

Vertex, edge, list and fractional colorings of graphs and the chromatic number, from Brooks' and Vizing's theorems to perfect graphs and the four color theorem.

## Brooks' theorem

Let $G$ be a finite connected simple graph and let $\Delta$ be its maximum
degree: every vertex of $G$ has degree at most $\Delta$ and some vertex has degree exactly $\Delta$.
If $G$ is not complete and is not isomorphic to a cycle graph on an odd number of vertices, then $G$
has a proper vertex coloring with $\Delta$ colors.

## Sources

- R. L. Brooks, On colouring the nodes of a network, Proc. Camb. Philos. Soc. 37 (1941), DOI 10.1017/S030500410002168X.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.BrooksWanted.brooks`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Brooks.lean, line 1217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Brooks.lean#L1217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/index.html#brooks).

## Erdős's theorem on graphs of high girth and high chromatic number

For all natural numbers
$k$ and $g$ with $g \ge 3$, there is a finite simple graph $G$ that has a cycle, whose girth
(the length of a shortest cycle) is at least $g$, and whose chromatic number is at least $k$.

In particular, there are finite graphs of arbitrarily high girth and chromatic number.

## Sources

- P. Erdős, Graph theory and probability, Canad. J. Math. 11 (1959), 34–38, DOI 10.4153/CJM-1959-003-9.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.ErdosGirthChromaticWanted.erdos_high_girth_chromatic`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ErdosGirthChromatic.lean, line 870](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/ErdosGirthChromatic.lean#L870). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/index.html#erdos-high-girth-chromatic).

## Five color theorem

Every straight-line planar simple graph $G$ on a finite vertex set
has a proper vertex coloring with five colors.

## Sources

- https://en.wikipedia.org/wiki/Five_color_theorem.

Stated but not proved: `MetaMathlibExt.five_color_theorem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Graph/FiveColorTheoremWanted.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Graph/FiveColorTheoremWanted.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-02/index.html#five-color-theorem).

## Mycielski's theorem

Write $\chi(G)$ for the chromatic number of a simple graph $G$. For
every simple graph $G$ on a finite vertex set there is a simple graph $H$ on a finite vertex set
with strictly more vertices than $G$ that contains a subgraph isomorphic to $G$, such that $H$ is
triangle-free whenever $G$ is, and such that $\chi(H) = \chi(G) + 1$ whenever $\chi(G)$ is
finite. Moreover, for every natural number $k$ there is a triangle-free simple graph $H$ on a
finite vertex set with $\chi(H) \ge k$.

The explicit Mycielski construction is abstracted here to the existence of such a graph $H$.

## Sources

- J. Mycielski, "Sur le coloriage des graphes" (1955), https://doi.org/10.4064/cm-3-2-161-162 (statement ID `mycielski-theorem-s1`).

Formalized by `MetaMathlibExt.mycielski_theorem`, a theorem declared in [MathlibExt/Combinatorics/Graph/MycielskiTheorem.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Graph/MycielskiTheorem.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-02/index.html#mycielski-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph coloring](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring)
