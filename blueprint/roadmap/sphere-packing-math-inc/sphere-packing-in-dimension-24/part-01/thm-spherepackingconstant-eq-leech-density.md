---
declaration: theorem
origin: cited
lean: SpherePacking.Dim24.SpherePackingConstant_eq_leech_density
statement: formalized
proof: formalized
---

# SpherePackingConstant_eq_leech_density

The optimal sphere packing density in $\mathbb{R}^{24}$ equals the Leech lattice density:

$$
\Delta_{24} = \Delta_{\Lambda_{24}} = \frac{\pi^{12}}{12!}.
$$

## Depends on

- [magic-function-d24](../part-02/thm-magic-function-d24.md)
- [LeechPacking-density](lem-leechpacking-density.md)

## Proof

By [Theorem magic-function-d24](../part-02/thm-magic-function-d24.md), we have $\Delta_{24}\le \pi^{12}/12!$. By [Lemma LeechPacking-density](lem-leechpacking-density.md), $\Delta_{\Lambda_{24}}=\pi^{12}/12!$. Since $\Lambda_{24}$ is a sphere packing in $\mathbb{R}^{24}$, we have $\Delta_{\Lambda_{24}}\le \Delta_{24}$. Therefore, all three quantities are equal.

## Lean

Formalized as [`SpherePacking.Dim24.SpherePackingConstant_eq_leech_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.SpherePackingConstant_eq_leech_density).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-main.tex, line 45](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-main.tex#L45)
