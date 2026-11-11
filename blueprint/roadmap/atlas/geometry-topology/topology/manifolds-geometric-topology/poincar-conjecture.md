---
declaration: section
origin: cited
lean: MathlibExt.Topology.Poincare3DSmoothWanted.Topology.poincare_3d_smooth, MathlibExt.Topology.Poincare3DTopologicalWanted.Topology.poincare_3d_topological, MathlibExt.Topology.Poincare4DTopologicalWanted.Topology.poincare_4d_topological, MathlibExt.Topology.PoincareHighDimTopologicalWanted.Topology.poincare_high_dim_topological
statement: formalized
---

# Poincaré conjecture

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html).

## Smooth Poincaré conjecture in dimension 3

Let $M$ be a nonempty, compact, simply connected
Hausdorff space with a smooth ($C^\infty$) manifold structure modelled on $\mathbb{R}^3$, without
boundary. Then $M$ is $C^\infty$-diffeomorphic to the unit sphere
$S^3 = \{x \in \mathbb{R}^4 : \|x\| = 1\}$ with its standard smooth structure.

## Sources

- G. Perelman, three arXiv preprints 2002-2003 (math/0211159, math/0303109, math/0307245). In dim 3, Smooth ⇔ PL ⇔ Topological via Moise (1952) / Bing (1959). Problem `poincare_3d_smooth` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.Poincare3DSmoothWanted.Topology.poincare_3d_smooth` is written with `theorem_wanted` in [WantedExt/Topology/Poincare3DSmoothWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/Poincare3DSmoothWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html#poincare-3d-smooth).

## Topological Poincaré conjecture in dimension 3

Let $M$ be a nonempty, compact, simply
connected Hausdorff space with an atlas of charts to $\mathbb{R}^3$, that is, a topological
3-manifold without boundary. Then $M$ is homeomorphic to the unit sphere
$S^3 = \{x \in \mathbb{R}^4 : \|x\| = 1\}$.

## Sources

- G. Perelman, The entropy formula for the Ricci flow and its geometric applications (arXiv:math/0211159, 2002); Ricci flow with surgery on three-manifolds (arXiv:math/0303109, 2003); Finite extinction time for the solutions to the Ricci flow on certain three-manifolds (arXiv:math/0307245, 2003). Originally conjectured by Henri Poincaré in 1904. Problem `poincare_3d_topological` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.Poincare3DTopologicalWanted.Topology.poincare_3d_topological` is written with `theorem_wanted` in [WantedExt/Topology/Poincare3DTopologicalWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/Poincare3DTopologicalWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html#poincare-3d-topological).

## Topological Poincaré conjecture in dimension 4

Let $M$ be a Hausdorff space with an
atlas of charts to $\mathbb{R}^4$ (a topological 4-manifold without boundary, not assumed
second countable). If $M$ is homotopy equivalent to the unit sphere
$S^4 = \{x \in \mathbb{R}^5 : \|x\| = 1\}$, then $M$ is homeomorphic to $S^4$.

## Sources

- M. H. Freedman, The topology of four-dimensional manifolds, J. Differential Geom. 17 (1982), 357-453. Problem `poincare_4d_topological` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.Poincare4DTopologicalWanted.Topology.poincare_4d_topological` is written with `theorem_wanted` in [WantedExt/Topology/Poincare4DTopologicalWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/Poincare4DTopologicalWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html#poincare-4d-topological).

## Topological Poincaré conjecture in dimensions at least 5

Let $n \ge 5$ and let $M$ be a
Hausdorff space with an atlas of charts to $\mathbb{R}^n$ (a topological $n$-manifold without
boundary, not assumed second countable). If $M$ is homotopy equivalent to the unit sphere
$S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}$, then $M$ is homeomorphic to $S^n$.

## Sources

- S. Smale, Generalized Poincaré's conjecture in dimensions greater than four, Ann. of Math. 74 (1961), 391-406. Topological case: M. H. A. Newman, The engulfing theorem for topological manifolds, Ann. of Math. 84 (1966) and E. H. Connell, A topological h-cobordism theorem for n ≥ 5, Illinois J. Math. 11 (1967). Problem `poincare_high_dim_topological` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.PoincareHighDimTopologicalWanted.Topology.poincare_high_dim_topological` is written with `theorem_wanted` in [WantedExt/Topology/PoincareHighDimTopologicalWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/PoincareHighDimTopologicalWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html#poincare-high-dim-topological).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poincaré conjecture](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/manifolds-geometric-topology/poincar-conjecture)
