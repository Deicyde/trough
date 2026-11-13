---
declaration: section
origin: cited
lean: Manifold.metricInCoordinates, Manifold.metricInCoordinates_apply, Manifold.metricInCoordinates_conformalScale, Manifold.contDiffOn_metricInCoordinates, Manifold.metricCkTopology, Manifold.RiemannianMetricWithCk, Manifold.RiemannianMetricWithCk.ofMetric, Manifold.tendsto_metricCkTopology_iff
statement: formalized
proof: formalized
---

# Spaces of Riemannian metrics

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html).

## Coordinate expression of a Riemannian metric

Let $g$ be a smooth Riemannian metric on
the tangent bundle of a smooth manifold $M$ modeled through a model with corners $I : H \to E$,
and let $e$ be an open partial homeomorphism from $M$ to $H$. Write $\psi$ for the inverse of the
extended chart $I \circ e$, $T$ for the target of $I \circ e$, and $D\psi(x)$ for the derivative
of $\psi$ at $x$ within $T$. The coordinate expression of $g$ in $e$ is the field of continuous
bilinear forms on $E$ that assigns to each $x \in E$ the pullback form
$(v, w) \mapsto g_{\psi(x)}(D\psi(x)\,v, D\psi(x)\,w)$.

Formalized by `Manifold.metricInCoordinates`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#metric-in-coordinates).

## Pointwise formula for a metric in coordinates

Let $g$ be a smooth Riemannian metric
on the tangent bundle of a smooth manifold $M$ modeled through a model with corners
$I : H \to E$, and let $e$ be an open partial homeomorphism from $M$ to $H$. Write $g^e$ for the
coordinate expression of $g$ in $e$, $\psi$ for the inverse of the extended chart $I \circ e$,
$T$ for the target of $I \circ e$, and $D\psi(x)$ for the derivative of $\psi$ at $x$ within
$T$. Then for all $x, v, w \in E$ we have
$g^e(x)(v, w) = g_{\psi(x)}(D\psi(x)\,v, D\psi(x)\,w)$.

Formalized by `Manifold.metricInCoordinates_apply`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#metric-in-coordinates-apply).

## Conformal scaling of a metric in coordinates

Let $g$ be a smooth Riemannian metric on
the tangent bundle of a smooth manifold $M$ modeled through a model with corners $I : H \to E$,
let $u : M \to \mathbb{R}$ be a smooth function with $u(p) > 0$ for every $p \in M$, and let $e$
be an open partial homeomorphism from $M$ to $H$. Write $g^e$ for the coordinate expression of
$g$ in $e$ and $\psi$ for the inverse of the extended chart $I \circ e$. Then for every $x \in E$
the coordinate expression of the conformally scaled metric $u g$ satisfies
$(u g)^e(x) = u(\psi(x))\, g^e(x)$.

Formalized by `Manifold.metricInCoordinates_conformalScale`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#metric-in-coordinates-conformal-scale).

## Smoothness of a metric in coordinates

Let $E$ be a finite-dimensional real normed
space, let $M$ be a smooth manifold modeled through a model with corners $I : H \to E$, and let
$g$ be a smooth Riemannian metric on the tangent bundle of $M$. For every chart $e$ in the maximal
smooth atlas of $M$, the coordinate expression of $g$ in $e$, viewed as a map from $E$ to the
continuous bilinear forms on $E$, is $C^\infty$ on the target of the extended chart $I \circ e$.

Formalized by `Manifold.contDiffOn_metricInCoordinates`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricInCoordinates.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#cont-diff-on-metric-in-coordinates).

## The $C^k$ topology on smooth Riemannian metrics

Let $M$ be a smooth manifold modelled
on a real normed space $E$ through a model with corners $I$, and let $k \in \mathbb{N} \cup
\{\infty\}$. For a chart $\varphi$ of the maximal smooth atlas of $M$, write $T_\varphi \subseteq E$
for the target of the extended chart $I \circ \varphi$. The (weak, compact-open) $C^k$ topology on
the space of smooth Riemannian metrics on $M$ is the coarsest topology for which, for every
chart $\varphi$ of the maximal atlas and every natural number $i \le k$, the map sending a
metric $g$ to the $i$-th iterated derivative within $T_\varphi$ of the coordinate expression of
$g$ in $\varphi$ is continuous, where these derivatives carry the topology of uniform
convergence on compact subsets of $T_\varphi$.

For $k = \infty$ this is the $C^\infty$ topology. Every element of the space is a smooth metric,
whatever $k$ is; $k$ only indexes the topology.

## Sources

- Burns-Matveev v2 §8.4 finite-atlas `ε`-balls, v3 §8.3 weak `C^k` topology after Hirsch Ch. II. `k = ⊤` is the `C^∞` topology (smooth, not analytic). The space carries smooth metrics for every `k`, and no chart is chosen. Equality with the finite-atlas `ε`-ball topology on a closed manifold follows by the standard argument (relatively compact chart domains and chain rule).

Formalized by `Manifold.metricCkTopology`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#metric-ck-topology).

## The space $\mathcal{G}^k(M)$ of smooth metrics with the $C^k$ topology

For a smooth
manifold $M$ and $k \in \mathbb{N} \cup \{\infty\}$, $\mathcal{G}^k(M)$ is the space of all
smooth Riemannian metrics on $M$, equipped with the $C^k$ topology. It is not the space of
$C^k$ metrics: every element is smooth, and $k$ only indexes the topology.

Formalized by `Manifold.RiemannianMetricWithCk`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#riemannian-metric-with-ck).

## Smooth metrics as elements of $\mathcal{G}^k(M)$

For a smooth manifold $M$ and
$k \in \mathbb{N} \cup \{\infty\}$, the identity map is a bijection from the space of smooth
Riemannian metrics on $M$ to $\mathcal{G}^k(M)$, the same space of metrics equipped with the
$C^k$ topology.

Formalized by `Manifold.RiemannianMetricWithCk.ofMetric`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#of-metric).

## Convergence in the $C^k$ topology on smooth metrics

Let $M$ be a smooth manifold
modelled on a real normed space $E$ through a model with corners $I$, let
$k \in \mathbb{N} \cup \{\infty\}$, let $l$ be a filter on a type $\alpha$, and let $g_a$
($a \in \alpha$) and $g_0$ be smooth Riemannian metrics on $M$. For a chart $\varphi$ of the
maximal smooth atlas of $M$, write $T_\varphi \subseteq E$ for the target of the extended chart
$I \circ \varphi$. Then $g_a$ tends to $g_0$ along $l$ in the $C^k$ topology if and only if, for
every chart $\varphi$ of the maximal atlas, every natural number $i \le k$ and every compact set
$K \subseteq T_\varphi$, the $i$-th iterated derivatives within $T_\varphi$ of the coordinate
expressions of $g_a$ in $\varphi$ converge uniformly on $K$ along $l$ to the $i$-th iterated
derivative within $T_\varphi$ of the coordinate expression of $g_0$ in $\varphi$.

## Sources

- Burns-Matveev v3 §8.3.

Formalized by `Manifold.tendsto_metricCkTopology_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#tendsto-metric-ck-topology-iff).

## Convergence in $\mathcal{G}^k(M)$

Let $M$ be a smooth manifold modelled on a real
normed space $E$ through a model with corners $I$, let $k \in \mathbb{N} \cup \{\infty\}$, let
$l$ be a filter on a type $\alpha$, and let $g_a$ ($a \in \alpha$) and $g_0$ be smooth
Riemannian metrics on $M$. For a chart $\varphi$ of the maximal smooth atlas of $M$, write
$T_\varphi \subseteq E$ for the target of the extended chart $I \circ \varphi$. Then $g_a$,
regarded as elements of the space $\mathcal{G}^k(M)$ of smooth metrics with the $C^k$
topology, tend to $g_0$ along $l$ if and only if, for every chart $\varphi$ of the maximal
atlas, every natural number $i \le k$ and every compact set $K \subseteq T_\varphi$, the $i$-th
iterated derivatives within $T_\varphi$ of the coordinate expressions of $g_a$ in $\varphi$
converge uniformly on $K$ along $l$ to the $i$-th iterated derivative within $T_\varphi$ of the
coordinate expression of $g_0$ in $\varphi$.

Formalized by `Manifold.RiemannianMetricWithCk.tendsto_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#tendsto-iff).

## The $C^k$ topologies on smooth metrics get finer as $k$ grows

Let $M$ be a smooth
manifold and let $k \le k'$ be elements of $\mathbb{N} \cup \{\infty\}$. On the space of
smooth Riemannian metrics on $M$, the $C^{k'}$ topology is finer than the $C^k$ topology.

Formalized by `Manifold.metricCkTopology_anti`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#metric-ck-topology-anti).

## Constant rescalings converge in every $C^k$ topology

Let $M$ be a smooth manifold
modelled on a finite-dimensional real normed space, let $g$ be a smooth Riemannian metric on
$M$, and let $k \in \mathbb{N} \cup \{\infty\}$. Let $l$ be a filter on a type $\alpha$ and let
$c_a > 0$ ($a \in \alpha$) be positive reals with $c_a \to 1$ along $l$. Then the rescaled
metrics $c_a g$ tend to $g$ along $l$ in the $C^k$ topology.

In every chart the coordinate expression of $c_a g$ is $c_a$ times that of $g$, hence so is
each iterated derivative within the chart target, while those derivatives of $g$ are bounded on
each compact subset of the target.

Formalized by `Manifold.tendsto_conformalScale_const_metricCkTopology`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/MetricCkTopology.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html#tendsto-conformal-scale-const-metric-ck).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spaces of Riemannian metrics](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/spaces-of-riemannian-metrics)
