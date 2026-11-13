---
declaration: section
origin: cited
lean: MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.period, MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.standardCircle, MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.IsUnknotted, MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.HasQuadrisecant, MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.smooth_knot_has_quadrisecant
statement: formalized
---

# Quadrisecant theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html).

## Period

The period is the real number $2\pi$.

Formalized by `MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.period`, a definition declared in [WantedExt/Topology/QuadrisecantWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/QuadrisecantWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html#period).

## Standard circle

The standard circle is the curve $\mathbb{R} \to \mathbb{R}^3$ given by
$t \mapsto (\cos t, \sin t, 0)$, the unit circle in the $xy$-plane.

Formalized by `MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.standardCircle`, a definition declared in [WantedExt/Topology/QuadrisecantWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/QuadrisecantWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html#standard-circle).

## Unknotted knot

A knot $K$ is unknotted when there is a knot $J$ whose parametrization is
the standard circle $t \mapsto (\cos t, \sin t, 0)$ such that $K$ is ambient-isotopic to $J$ as
an oriented knot.

Formalized by `MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.IsUnknotted`, a definition declared in [WantedExt/Topology/QuadrisecantWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/QuadrisecantWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html#is-unknotted).

## Quadrisecant of a knot

A knot $K$ with parametrization
$\gamma \colon \mathbb{R} \to \mathbb{R}^3$ has a quadrisecant when there are pairwise distinct
reals $t_0, t_1, t_2, t_3 \in [0, 2\pi)$, a point $p \in \mathbb{R}^3$, a nonzero vector
$v \in \mathbb{R}^3$ and reals $a_0, a_1, a_2, a_3$ such that $\gamma(t_i) = p + a_i v$ for each
$i$, that is, the four points $\gamma(t_i)$ lie on one line.

Formalized by `MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.HasQuadrisecant`, a definition declared in [WantedExt/Topology/QuadrisecantWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/QuadrisecantWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html#has-quadrisecant).

## Quadrisecant theorem (Pannwitz–Kuperberg)

Every smooth knot $K$ in $\mathbb{R}^3$ that is
not unknotted has a quadrisecant.

## Sources

- E. Pannwitz (1933); G. Kuperberg, *Quadrisecants of knots and links*, J. Knot Theory Ramif. 3 (1994). Knill, §161. Problem `smooth_knot_has_quadrisecant` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.QuadrisecantWanted.KnotTheory.Quadrisecant.smooth_knot_has_quadrisecant` is written with `theorem_wanted` in [WantedExt/Topology/QuadrisecantWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/QuadrisecantWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html#smooth-knot-has-quadrisecant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadrisecant theorem](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/quadrisecant-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/knot-theory/quadrisecant-theorem)
