---
declaration: lemma
origin: cited
lean: SpherePacking.scale_finiteDensity
statement: formalized
proof: formalized
---

# SpherePacking.scale_finiteDensity

Let $\mathcal{P}(X)$ be a sphere packing and $c$ a positive real number. Then, for all $R > 0$,

$$
\Delta_{\mathcal{P}(cX)}(cR) = \Delta_{\mathcal{P}(X)}(R).
$$

## Depends on

- [SpherePacking.finiteDensity](def-spherepacking-finitedensity.md)
- [SpherePacking.scale](def-spherepacking-scale.md)

## Proof

The proof follows by direct computation:

$$
\Delta_{\mathcal{P}(cX)}(cR) = \frac{\operatorname{Vol}\!\left(\mathcal{P}(cX) \cap B_d(0, cR)\right)}{\operatorname{Vol}\!\left(B_d(0, cR)\right)} = \frac{c^d \cdot \operatorname{Vol}\!\left(\mathcal{P}(X) \cap B_d(0, R)\right)}{c^d \cdot \operatorname{Vol}\!\left(B_d(0, R)\right)}
= \Delta_{\mathcal{P}(X)}(R)
$$

where the second equality follows from applying the fact that scaling a (measurable) set by a factor of $c$ scales its volume by a factor of $c^d$ to the fact that $\mathcal{P}(cX) \cap B_d(0, cR) = c \cdot (\mathcal{P}(X) \cap B_d(0, cR))$.

## Lean

Formalized as [`SpherePacking.scale_finiteDensity`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.scale_finiteDensity).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/sphere-packings-scaling.tex, line 9](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/sphere-packings-scaling.tex#L9)
