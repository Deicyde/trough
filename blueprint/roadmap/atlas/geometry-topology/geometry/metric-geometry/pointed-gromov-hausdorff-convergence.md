---
declaration: section
origin: cited
lean: GromovHausdorff.PointedGHConverges, GromovHausdorff.pointedGHConverges_iff_dis_lt, GromovHausdorff.pointedGHConverges_const, GromovHausdorff.pointedGHConverges_iff_exists_measurable
statement: formalized
proof: formalized
---

# Pointed Gromov–Hausdorff convergence

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html).

## Pointed Gromov–Hausdorff convergence

Let $X_0, X_1, \dots$ and $Y$ be pseudometric
spaces with base points $p_n \in X_n$ and $q \in Y$. The sequence $(X_n, p_n)$ converges to
$(Y, q)$ in the pointed Gromov–Hausdorff sense if for all $R > 0$ and $\varepsilon > 0$ there is
$N$ such that for every $n \ge N$ there is a map $f$ from the open ball $B(p_n, R)$ to $Y$ with
$f(p_n) = q$, with $|d(f(x), f(y)) - d(x, y)| \le \varepsilon$ for all $x, y \in B(p_n, R)$, and
such that every point of the open ball $B(q, R - \varepsilon)$ is at distance less than
$\varepsilon$ from some point of the image of $f$.

No measurability or continuity is required of $f$, and the spaces need not be complete or
separable, so this extends the metric part of the pointed measured Gromov–Hausdorff convergence
of Gigli–Mondino–Savaré, who use Borel maps on complete separable spaces. Open balls are an
implementation choice for their unspecified balls $B_R$.

Formalized by `GromovHausdorff.PointedGHConverges`, a definition declared in [MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html#pointed-ghconverges).

## Pointed Gromov–Hausdorff convergence with strict distortion

Let $X_0, X_1, \dots$ and
$Y$ be pseudometric spaces with base points $p_n \in X_n$ and $q \in Y$. Then $(X_n, p_n)$
converges to $(Y, q)$ in the pointed Gromov–Hausdorff sense if and only if for all $R > 0$ and
$\varepsilon > 0$ there is $N$ such that for every $n \ge N$ there are a map $f$ from the open
ball $B(p_n, R)$ to $Y$ and a real number $\delta < \varepsilon$ with $f(p_n) = q$, with
$|d(f(x), f(y)) - d(x, y)| \le \delta$ for all $x, y \in B(p_n, R)$, and such that every point
of the open ball $B(q, R - \varepsilon)$ is at distance less than $\varepsilon$ from some point
of the image of $f$.

That is, the distortion of $f$ may be required to be strictly less than $\varepsilon$, as in
arXiv:2602.04826, Def. 2.12.

Formalized by `GromovHausdorff.pointedGHConverges_iff_dis_lt`, a theorem declared in [MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html#pointed-ghconverges-iff-dis-lt).

## Constant sequences converge in the pointed Gromov–Hausdorff sense

For every
pseudometric space $Y$ and every point $q \in Y$, the constant sequence $(X_n, p_n) = (Y, q)$
converges to $(Y, q)$ in the pointed Gromov–Hausdorff sense.

Formalized by `GromovHausdorff.pointedGHConverges_const`, a theorem declared in [MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/PointedGromovHausdorff.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html#pointed-ghconverges-const).

## Pointed Gromov–Hausdorff convergence with measurable maps

Let $X_0, X_1, \dots$ be
separable pseudometric spaces, each with its Borel $\sigma$-algebra, with base points
$p_n \in X_n$, and let $Y$ be a pseudometric space with any $\sigma$-algebra and a base point
$q \in Y$. Then $(X_n, p_n)$ converges to $(Y, q)$ in the pointed Gromov–Hausdorff sense if and
only if for all $R > 0$ and $\varepsilon > 0$ there is $N$ such that for every $n \ge N$ there is
a map $f$ from the open ball $B(p_n, R)$ to $Y$, measurable for the subspace $\sigma$-algebra on
the ball, with $f(p_n) = q$, with $|d(f(x), f(y)) - d(x, y)| \le \varepsilon$ for all
$x, y \in B(p_n, R)$, and such that every point of the open ball $B(q, R - \varepsilon)$ is at
distance less than $\varepsilon$ from some point of the image of $f$.

So for separable spaces the approximating maps can be taken Borel, as Gigli–Mondino–Savaré
require.

Formalized by `GromovHausdorff.pointedGHConverges_iff_exists_measurable`, a theorem declared in [MathlibExt/Topology/MetricSpace/PointedGromovHausdorffBorel.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/PointedGromovHausdorffBorel.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html#pointed-ghconverges-iff-exists-measurabl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pointed Gromov–Hausdorff convergence](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/metric-geometry/pointed-gromov-hausdorff-convergence)
