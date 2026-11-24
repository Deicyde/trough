---
declaration: lemma
origin: cited
lean: SpherePacking.constant_eq_constant_normalized
statement: formalized
proof: formalized
---

# SpherePacking.constant_eq_constant_normalized

$$
\Delta_d = \sup\limits_{\substack{\mathcal{P} \subset \mathbb{R}^d \\ \text{sphere packing} \\ \text{sep.~rad.} = 1}} \Delta_{\mathcal{P}}
$$

## Depends on

- [SpherePackingConstant](spherepackingconstant.md)
- [SpherePacking.density](spherepacking-density.md)

## Proof depends on

- [SpherePacking.scale_density](spherepacking-scale-density.md)

## Proof

That the supremum over packings of unit density is at most the sphere packing constant is obvious. For the reverse inequality, let $\mathcal{P}(X)$ be any sphere packing with separation radius $r$. We know, from Lemma [SpherePacking.scale_density](spherepacking-scale-density.md), that the density of $\mathcal{P}(X)$ is equal to that of the scaled packing $\mathcal{P}\!\left(\frac{X}{r}\right)$. Since the scaled packing has separation radius $1$, its density is naturally at most the supremum over all packings of unit density, meaning that the same is true of $\mathcal{P}(X)$.

## Lean

Formalized as [`SpherePacking.constant_eq_constant_normalized`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.constant_eq_constant_normalized).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/sphere-packings-scaling.tex, line 44](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/sphere-packings-scaling.tex#L44)
