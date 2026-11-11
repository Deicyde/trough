---
declaration: section
origin: cited
lean: MathlibExt.Geometry.HopfRinowWanted.Geometry.IsGeodesic, MathlibExt.Geometry.HopfRinowWanted.Geometry.IsGeodesicallyComplete, MathlibExt.Geometry.HopfRinowWanted.Geometry.hopf_rinow
statement: formalized
---

# Hopf–Rinow theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem/index.html).

## Constant-speed geodesic in a metric space

Let $M$ be an extended metric space with
distance $d$. A path $\gamma : \mathbb{R} \to M$ is a constant-speed geodesic if there is a real
number $c \ge 0$ such that every $t_0 \in \mathbb{R}$ has a $\delta > 0$ with
$d(\gamma(s), \gamma(t)) = c\,|t - s|$ for all real $s, t$ with $|s - t_0| < \delta$ and
$|t - t_0| < \delta$.

Formalized by `MathlibExt.Geometry.HopfRinowWanted.Geometry.IsGeodesic`, a definition declared in [WantedExt/Geometry/HopfRinowWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HopfRinowWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem/index.html#is-geodesic).

## Geodesically complete metric space

An extended metric space $M$ with distance $d$ is
geodesically complete if the following holds for all real numbers $a < b$ and every path
$\gamma : \mathbb{R} \to M$. Suppose there is a real $c \ge 0$ such that every
$t_0 \in (a, b)$ has a $\delta > 0$ with $d(\gamma(s), \gamma(t)) = c\,|t - s|$ for all $s, t$
in the interval $(a, b) \cap (t_0 - \delta, t_0 + \delta)$. Then there is a constant-speed
geodesic $\tilde\gamma : \mathbb{R} \to M$ with $\tilde\gamma(t) = \gamma(t)$ for all
$t \in (a, b)$.

Formalized by `MathlibExt.Geometry.HopfRinowWanted.Geometry.IsGeodesicallyComplete`, a definition declared in [WantedExt/Geometry/HopfRinowWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HopfRinowWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem/index.html#is-geodesically-complete).

## Hopf–Rinow theorem

Let $M$ be a connected, locally compact smooth manifold without
boundary, modelled on a finite-dimensional real normed space, with a smooth Riemannian metric
whose Riemannian distance is the (extended) distance of $M$. Then $M$ is geodesically complete
if and only if $M$ is complete for its distance.

## Sources

- H. Hopf and W. Rinow, *Ueber den Begriff der vollständigen differentialgeometrischen Fläche*, Comment. Math. Helv. 3 (1931), 209-225. Listed as §93 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `hopf_rinow` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.HopfRinowWanted.Geometry.hopf_rinow` is written with `theorem_wanted` in [WantedExt/Geometry/HopfRinowWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HopfRinowWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem/index.html#hopf-rinow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hopf–Rinow theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/hopf-rinow-theorem)
