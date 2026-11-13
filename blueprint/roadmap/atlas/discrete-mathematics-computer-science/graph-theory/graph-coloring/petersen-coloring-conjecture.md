---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.PetersenColoringConjectureWanted.PVertex, MathlibExt.GraphTheory.PetersenColoringConjectureWanted.petersenEdgeSet, MathlibExt.GraphTheory.PetersenColoringConjectureWanted.petersenGraph, MathlibExt.GraphTheory.PetersenColoringConjectureWanted.IsPetersenColoring, MathlibExt.GraphTheory.PetersenColoringConjectureWanted.conjecture, MathlibExt.GraphTheory.PetersenColoringConjectureWanted.conjecture_refuted
statement: formalized
---

# Petersen coloring conjecture

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html).

## Vertices of the Petersen graph

The vertex set of the Petersen graph is
$\mathbb{Z}/5\mathbb{Z} \times \{\mathrm{false}, \mathrm{true}\}$; the vertices
$(i, \mathrm{false})$ with $i \in \mathbb{Z}/5\mathbb{Z}$ form the outer 5-cycle and the vertices
$(i, \mathrm{true})$ form the inner 5-star.

Formalized by `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.PVertex`, an abbreviation declared in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#pvertex).

## Edges of the Petersen graph

The edge set of the Petersen graph on
$\mathbb{Z}/5\mathbb{Z} \times \{\mathrm{false}, \mathrm{true}\}$ consists of the unordered
pairs $\{(i, \mathrm{false}), (i + 1, \mathrm{false})\}$ (the outer 5-cycle),
$\{(i, \mathrm{false}), (i, \mathrm{true})\}$ (the spokes) and
$\{(i, \mathrm{true}), (i + 2, \mathrm{true})\}$ (the inner 5-star), for
$i \in \mathbb{Z}/5\mathbb{Z}$.

Formalized by `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.petersenEdgeSet`, a definition declared in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#petersen-edge-set).

## Petersen graph

The Petersen graph is the simple graph on
$\mathbb{Z}/5\mathbb{Z} \times \{\mathrm{false}, \mathrm{true}\}$ whose edges are the outer
5-cycle edges $\{(i, \mathrm{false}), (i + 1, \mathrm{false})\}$, the spokes
$\{(i, \mathrm{false}), (i, \mathrm{true})\}$ and the inner 5-star edges
$\{(i, \mathrm{true}), (i + 2, \mathrm{true})\}$ for $i \in \mathbb{Z}/5\mathbb{Z}$.

Formalized by `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.petersenGraph`, a definition declared in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#petersen-graph).

## Petersen coloring

Let $G$ be a simple graph on a vertex type $V$ and let $P$ be the
Petersen graph. A map $f$ from unordered pairs of vertices of $G$ to unordered pairs of vertices
of $P$ is a Petersen coloring of $G$ when $f$ sends every edge of $G$ to an edge of $P$ and, for
every vertex $v$ of $G$, there is a vertex $w$ of $P$ such that $f$ maps the set of edges of $G$
incident to $v$ bijectively onto the set of edges of $P$ incident to $w$.

Formalized by `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.IsPetersenColoring`, a definition declared in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#is-petersen-coloring).

## Petersen coloring conjecture

For every finite vertex type $V$ and every simple graph $G$
on $V$, if every vertex of $G$ has exactly three neighbors and $G$ is bridgeless, then $G$ admits
a Petersen coloring.

Formalized by `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.conjecture`, a definition declared in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#conjecture).

## The Petersen coloring conjecture is false

There are a finite vertex type $V$ and a
simple graph $G$ on $V$ in which every vertex has exactly three neighbors and no edge is a bridge,
such that $G$ has no Petersen coloring: no map $f$ from unordered pairs of vertices of $G$ to
unordered pairs of vertices of the Petersen graph $P$ sends every edge of $G$ to an edge of $P$
and, for every vertex $v$ of $G$, maps the edges of $G$ at $v$ bijectively onto the edges of $P$
at some vertex $w$ of $P$.

Putman (arXiv:2608.10012, Aug 2026) gave 112-vertex counterexamples with SAT/DRAT certificates,
and Goedgebeur, Jooken, Macajova, Mattiolo, Mazzuoccolo and Ulyanov (arXiv:2608.10028,
Theorem 6) prove two simple bridgeless cubic 52-vertex graphs have no Petersen colouring.

## Sources

- Jan Goedgebeur, Jorik Jooken, Edita Macajova, Davide Mattiolo, Giuseppe Mazzuoccolo and Nikolay Ulyanov, Disproving the Petersen Coloring Conjecture: Theoretical Analysis and an Infinite Family of Counterexamples, arXiv preprint (2026), arXiv:2608.10028, https://arxiv.org/abs/2608.10028; Bryce Putman, A 112-Vertex Counterexample to the Petersen Coloring Conjecture, arXiv preprint (2026), arXiv:2608.10012, https://arxiv.org/abs/2608.10012.

Stated but not proved: `MathlibExt.GraphTheory.PetersenColoringConjectureWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/PetersenColoringConjectureWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Petersen coloring conjecture](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/petersen-coloring-conjecture)
