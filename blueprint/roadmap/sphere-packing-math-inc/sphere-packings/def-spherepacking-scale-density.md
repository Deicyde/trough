---
declaration: lemma
origin: cited
lean: SpherePacking.scale_density
statement: formalized
proof: formalized
---

# SpherePacking.scale_density

Let $\mathcal{P}(X)$ be a sphere packing and $c$ a positive real number. Then, the density of the scaled packing $\mathcal{P}(cX)$ is equal to the density of the original packing $\mathcal{P}(X)$.

## Depends on

- [SpherePacking.scale](def-spherepacking-scale.md)

## Proof depends on

- [SpherePacking.scale_finiteDensity](thm-spherepacking-scale-finitedensity.md)

## Proof

One can show, using relatively unsophisticated real analysis, that

$$
\limsup_{R \to \infty} \Delta_{\mathcal{P}(cX)}(R) = \limsup_{cR \to \infty} \Delta_{\mathcal{P}(cX)}(cR)
$$

Lemma [SpherePacking.scale_finiteDensity](thm-spherepacking-scale-finitedensity.md) tells us that $\Delta_{\mathcal{P}(cX)}(cR) = \Delta_{\mathcal{P}(X)}(R)$ for every $R > 0$. Therefore,

$$
\limsup_{cR \to \infty} \Delta_{\mathcal{P}(cX)}(cR) = \limsup_{cR \to \infty} \Delta_{\mathcal{P}(X)}(R) = \limsup_{R \to \infty} \Delta_{\mathcal{P}(X)}(R)
$$

where the second equality is the result of a similar change of variables to the one done above.

## Lean

Formalized as [`SpherePacking.scale_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.scale_density).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/sphere-packings-scaling.tex, line 25](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/sphere-packings-scaling.tex#L25)
