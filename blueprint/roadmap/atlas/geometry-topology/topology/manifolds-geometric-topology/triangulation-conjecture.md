---
declaration: section
origin: cited
lean: MathlibExt.Topology.ManolescuTriangulationWanted.Topology.ClosedTopManifold, MathlibExt.Topology.ManolescuTriangulationWanted.Topology.Triangulable, MathlibExt.Topology.ManolescuTriangulationWanted.Topology.manolescu_triangulation_disproof
statement: formalized
---

# Triangulation conjecture

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture/index.html).

## Closed topological manifold

For a natural number $n$, a closed topological $n$-manifold
is a nonempty, compact, connected, Hausdorff, second-countable topological space $M$ together
with an atlas of charts, homeomorphisms from open subsets of $M$ onto open subsets of
$\mathbb{R}^n$, whose domains cover $M$. Since the charts land in $\mathbb{R}^n$ itself rather
than in a half-space, $M$ has no boundary.

Formalized by `MathlibExt.Topology.ManolescuTriangulationWanted.Topology.ClosedTopManifold`, a structure declared in [WantedExt/Topology/ManolescuTriangulationWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ManolescuTriangulationWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture/index.html#closed-top-manifold).

## Triangulable closed manifold

A closed topological $n$-manifold $M$ is triangulable if,
for some natural number $N$, there is a simplicial complex $K$ in $\mathbb{R}^N$ with finitely
many faces such that $M$ is homeomorphic to the geometric realization of $K$, the union of its
faces with the subspace topology from $\mathbb{R}^N$.

For a compact manifold this is the usual notion of triangulability. Requiring finitely many faces
is essential: otherwise any copy of $M$ embedded in $\mathbb{R}^N$ would be the realization of the
complex whose faces are its points.

Formalized by `MathlibExt.Topology.ManolescuTriangulationWanted.Topology.Triangulable`, a definition declared in [WantedExt/Topology/ManolescuTriangulationWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ManolescuTriangulationWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture/index.html#triangulable).

## Manolescu's disproof of the triangulation conjecture

For every natural number $n \ge 5$
there is a closed connected topological $n$-manifold that is not triangulable.

## Sources

- C. Manolescu, *Pin(2)-equivariant Seiberg–Witten Floer homology and the triangulation conjecture*, J. Amer. Math. Soc. 29 (2016), via the Galewski–Stern and Matumoto reduction. Earlier, the triangulation conjecture was known false in dimension 4 (Casson). Problem `manolescu_triangulation_disproof` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.ManolescuTriangulationWanted.Topology.manolescu_triangulation_disproof` is written with `theorem_wanted` in [WantedExt/Topology/ManolescuTriangulationWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ManolescuTriangulationWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture/index.html#manolescu-triangulation-disproof).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triangulation conjecture](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/manifolds-geometric-topology/triangulation-conjecture)
