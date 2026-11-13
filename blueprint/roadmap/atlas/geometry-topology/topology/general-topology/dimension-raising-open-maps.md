---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook136Wanted.kolmogorovInteriorMapRaisesDimension, MathlibExt.Topology.ScottishBook187cWanted.Cube, MathlibExt.Topology.ScottishBook187cWanted.scottishBook187c_refuted
statement: formalized
---

# Dimension-raising open maps

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/dimension-raising-open-maps/index.html).

## Kolmogorov's open map raising dimension

An interior (open) mapping can raise dimension:
there are compact metrizable spaces $X$ and $Y$, where $X$ has small inductive dimension exactly
$1$ and $Y$ has small inductive dimension exactly $2$, and a continuous open surjective map
$f \colon X \to Y$. A space has small inductive dimension exactly $n$ when its small inductive
dimension is at most $n$ but not at most $n - 1$.

## Sources

- S. Eilenberg, Problem 136 of the Scottish Book, asking whether an interior mapping can increase dimension; answered affirmatively by A. Kolmogorov, Annals of Mathematics 38 (1937), pp. 34-38, who gave an example of a continuous interior mapping raising dimension from 1 to 2, as recorded in the typescript Ad 136.

Stated but not proved: `MathlibExt.Topology.ScottishBook136Wanted.kolmogorovInteriorMapRaisesDimension` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook136Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook136Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/dimension-raising-open-maps/index.html#kolmogorov-interior-map-raises-dimension).

## The p-dimensional cube

For $p \in \mathbb{N}$, the cube $I^p = [0,1]^p$ is the set of
points of $\mathbb{R}^p$ all of whose coordinates lie in $[0,1]$, with the subspace topology.

Formalized by `MathlibExt.Topology.ScottishBook187cWanted.Cube`, an abbreviation declared in [WantedExt/Topology/ScottishBook187cWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook187cWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/dimension-raising-open-maps/index.html#cube).

## Open maps can raise the dimension of a cube

There are natural numbers $p < q$ and a
continuous, open, surjective map $f \colon I^p \to I^q$, where $I^p = [0,1]^p$ and
$I^q = [0,1]^q$ are the $p$- and $q$-dimensional cubes.

Keldysh constructed such maps, refuting the claim of Scottish Book Problem 187, part (3), that no
open (interior) continuous map of a $p$-dimensional cube onto a $q$-dimensional cube exists for
$p < q$.

## Sources

- P. Alexandroff, Problem 187 part (3) of the Scottish Book, typescript pp. 82–83; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook187cWanted.scottishBook187c_refuted` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook187cWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook187cWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/dimension-raising-open-maps/index.html#scottish-book187c-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dimension-raising open maps](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/dimension-raising-open-maps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/general-topology/dimension-raising-open-maps)
