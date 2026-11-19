---
declaration: theorem
origin: cited
lean: E8Packing_density
statement: formalized
proof: formalized
---

# E8Packing-density

We have $\Delta_{\mathcal{P}(E_8)} = \frac{\pi^4}{384}$.

## Depends on

- [psp-density](../density-of-packings/theorem-psp-density.md)
- [E8Packing-covol](e8packing-covol.md)

## Proof

By [Theorem psp-density](../density-of-packings/theorem-psp-density.md), we have $\Delta_{\mathcal{P}(E_8)} = |E_8 / E_8| \cdot \frac{\operatorname{Vol}\!\left(\mathcal{B}_8(\sqrt{2} / 2)\right)}{\mathrm{Covol}(E_8)} = \frac{\pi^4}{384}$, where the last equality follows from [Lemma E8Packing-covol](e8packing-covol.md) and the formula for volume of a ball: $\operatorname{Vol}\!\left(\mathcal{B}_d(R)\right) = R^d \pi^{d / 2} / \Gamma\left(\frac{d}{2} + 1\right)$.

## Lean

Formalized as [`E8Packing_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/E8Packing_density).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/E8-defs.tex, line 110](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/E8-defs.tex#L110)
