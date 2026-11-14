---
declaration: lemma
origin: cited
lean: SpherePacking.Dim24.LeechPacking_density
statement: formalized
proof: formalized
---

# LeechPacking-density

The density of the Leech lattice packing is

$$
\Delta_{\Lambda_{24}} = \operatorname{Vol}\!\left(B_{24}(0,1)\right) = \frac{\pi^{12}}{12!}.
$$

## Depends on

- [LeechPacking](def-leechpacking.md)
- [leech-lattice](def-leech-lattice.md)
- [psp-density](../../density-of-packings/theorem-psp-density.md)

## Proof

By [Theorem psp-density](../../density-of-packings/theorem-psp-density.md), a lattice packing has density $\operatorname{Vol}\!\left(B_d(0,r/2)\right)/\operatorname{Vol}\!\left(\mathbb{R}^d/\Lambda\right)$. Here $d=24$, $r=2$, and $\operatorname{Vol}\!\left(\mathbb{R}^{24}/\Lambda_{24}\right)=1$ by [Definition leech-lattice](def-leech-lattice.md), so the density is $\operatorname{Vol}\!\left(B_{24}(0,1)\right)=\pi^{12}/12!$.

## Lean

Formalized as [`SpherePacking.Dim24.LeechPacking_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.LeechPacking_density).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-main.tex, line 24](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-main.tex#L24)
