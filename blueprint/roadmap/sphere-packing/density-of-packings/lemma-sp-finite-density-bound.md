---
declaration: lemma
origin: cited
lean: SpherePacking.finiteDensity_le, SpherePacking.finiteDensity_ge
statement: formalized
proof: formalized
---

# sp-finite-density-bound

For any $R > 0$,

$$
\left|X \cap \mathcal{B}_d\left(R - \frac{r}{2}\right)\right| \cdot \frac{\mathrm{Vol}\left(\mathcal{B}_d\left(\frac{r}{2}\right)\right)}{\mathrm{Vol}(\mathcal{B}_d(R))}
\leq \Delta_{\mathcal{P}}(R)
\leq \left|X \cap \mathcal{B}_d\left(R + \frac{r}{2}\right)\right| \cdot \frac{\mathrm{Vol}\left(\mathcal{B}_d\left(\frac{r}{2}\right)\right)}{\mathrm{Vol}(\mathcal{B}_d(R))}
$$

## Depends on

- [SpherePacking.finiteDensity](../sphere-packings/spherepacking-finitedensity.md)

## Proof

The high level idea is to prove that $\mathcal{P} \cap \mathcal{B}_d(R) = \left(\bigcup_{x \in X} \mathcal{B}_d\left(x, \frac{r}{2}\right)\right) \subseteq \bigcup_{x \in X \cap \mathcal{B}_d\left(R + \frac{r}{2}\right)} \mathcal{B}_d\left(x, \frac{r}{2}\right)$, and a similar inequality for the upper bound. The rest follows by rearranging and using the fact that the balls are pairwise disjoint.

## Lean

Formalized as [`SpherePacking.finiteDensity_le`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.finiteDensity_le), [`SpherePacking.finiteDensity_ge`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.finiteDensity_ge).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/packings-density.tex, line 7](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/packings-density.tex#L7)
