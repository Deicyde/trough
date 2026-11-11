---
declaration: section
origin: cited
lean: Manifold.normalizedHausdorffMeasure, Manifold.riemannianVolume, Manifold.riemannianVolume_real
statement: formalized
proof: formalized
---

# Riemannian volume

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-volume/index.html).

## Normalized Hausdorff measure

Let $n$ be a natural number and let $X$ be an extended
metric space with its Borel $\sigma$-algebra. The normalized $n$-dimensional Hausdorff measure of
$X$ is the measure $\frac{\omega_n}{2^n} \mathcal{H}^n$, where $\omega_n$ is the Lebesgue volume of
the open unit ball of the Euclidean space $\mathbb{R}^n$ and $\mathcal{H}^n$ is the unnormalized
$n$-dimensional Hausdorff measure, in which a set of diameter $r$ has content $r^n$.

With this normalization it agrees with Lebesgue measure on $\mathbb{R}^n$ (classically, by the
isodiametric inequality); the case $n = 1$ is checked by the computation of the Riemannian volume
of the real line.

Formalized by `Manifold.normalizedHausdorffMeasure`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Volume.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Volume.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-volume/index.html#normalized-hausdorff-measure).

## Riemannian volume

Let $E$ be a finite-dimensional real normed space, let $I$ be a model
with corners on $E$, and let $M$ be a $C^\infty$ manifold modeled on $I$, so that $M$ has dimension
$n = \dim_{\mathbb{R}} E$. Suppose that $M$ carries a $C^\infty$ Riemannian metric and an extended
metric equal to the Riemannian distance (the infimum of the lengths of $C^1$ paths), and is given
its Borel $\sigma$-algebra. The Riemannian volume of $M$ is the normalized $n$-dimensional
Hausdorff measure of $M$.

The manifold and Riemannian hypotheses are not used in the formula; they tie the dimension to the
model of $M$ and restrict the definition to the setting in which, classically, this measure is the
Riemannian volume, given in charts by the density $\sqrt{\det(g_{ij})}$ against Lebesgue measure.

Formalized by `Manifold.riemannianVolume`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Volume.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Volume.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-volume/index.html#riemannian-volume).

## The Riemannian volume of the real line is Lebesgue measure

The Riemannian volume of the
real line $\mathbb{R}$, with its standard Riemannian metric (the usual inner product on each tangent
space) and with its usual distance, which is the Riemannian distance, is Lebesgue measure.

This is a normalization check of the Riemannian volume in dimension one.

Formalized by `Manifold.riemannianVolume_real`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Volume.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/Volume.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-volume/index.html#riemannian-volume-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemannian volume](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-volume/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/riemannian-volume)
