---
declaration: theorem
origin: cited
lean: PeriodicSpherePacking.density_eq
statement: formalized
proof: formalized
---

# psp-density

For a periodic sphere packing $\mathcal{P} = \mathcal{P}(X)$ with centers $X$ periodic to the lattice $\Lambda$ and separation $r$,

$$
\Delta_{\mathcal{P}} = |X / \Lambda| \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(r / 2)\right)}{\operatorname{Vol}\!\left(\mathbb{R}^d / \Lambda\right)}
$$

## Depends on

- [SpherePacking.density](../sphere-packings/spherepacking-density.md)

## Proof depends on

- [sp-finite-density-bound](lemma-sp-finite-density-bound.md)
- [lattice-points-bound](lemma-lattice-points-bound.md)
- [periodic-points-bounds](lemma-periodic-points-bounds.md)
- [volume-ball-ratio-limit](lemma-volume-ball-ratio-limit.md)

## Proof

Fix any fundamental domain $\mathcal{D}$ (induced by any basis) of the lattice $\Lambda$. Combining [Lemma sp-finite-density-bound](lemma-sp-finite-density-bound.md), [Lemma lattice-points-bound](lemma-lattice-points-bound.md) and [Lemma periodic-points-bounds](lemma-periodic-points-bounds.md), we get the following inequality for the *finite* density:

$$
|X / \Lambda| \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(r / 2)\right)}{\operatorname{Vol}\!\left(\mathbb{R}^d / \Lambda\right)} \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(R - r / 2 - 2L)\right)}{\operatorname{Vol}\!\left(\mathcal{B}_d(R)\right)}
\leq \Delta_{\mathcal{P}}(R)
\leq |X / \Lambda| \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(r / 2)\right)}{\operatorname{Vol}\!\left(\mathbb{R}^d / \Lambda\right)} \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(R + r / 2 + 2L)\right)}{\operatorname{Vol}\!\left(\mathcal{B}_d(R)\right)}
$$

Taking limit on both sides as $R \to \infty$ and apply the Sandwich theorem and [Lemma volume-ball-ratio-limit](lemma-volume-ball-ratio-limit.md), we get

$$
\Delta_{\mathcal{P}} = \limsup_{R \to \infty} \Delta_{\mathcal{P}}(R) = \lim_{R \to \infty} \Delta_{\mathcal{P}}(R) = |X / \Lambda| \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_d(r / 2)\right)}{\operatorname{Vol}\!\left(\mathbb{R}^d / \Lambda\right)}
$$

## Lean

Formalized as [`PeriodicSpherePacking.density_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/PeriodicSpherePacking.density_eq).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/packings-density.tex, line 75](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/packings-density.tex#L75)
