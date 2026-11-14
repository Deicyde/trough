---
declaration: theorem
origin: cited
lean: SpherePacking.SpherePackingConstant_le_E8Packing_density
statement: formalized
proof: formalized
---

# CE_Main

All *periodic* packing $\mathcal{P} \subseteq \mathbb{R}^8$ has density satisfying $\Delta_{\mathcal{P}} \leq \Delta_{E_8} = \frac{\pi^4}{384}$, the density of the $E_8$ sphere packing (see [Definition E8Packing](../the-e-8-lattice/e8packing.md)).

## Depends on

- [E8-Lattice](../the-e-8-lattice/e8-lattice.md)
- [SpherePackingConstant](def-spherepackingconstant.md)
- [SpherePacking.density](def-spherepacking-density.md)
- [E8Packing-density](../the-e-8-lattice/e8packing-density.md)
- [g](../cohn-elkies-linear-programming-bounds/thm-g.md)
- [Cohn–Elkies (ElkiesCohn)](../cohn-elkies-linear-programming-bounds/thm-cohn-elkies-general.md)

## Proof

Directly follows from [Cohn–Elkies (ElkiesCohn)](../cohn-elkies-linear-programming-bounds/thm-cohn-elkies-general.md) applied to the function $f(x)=g(x/\sqrt{2})$ of [Theorem g](../cohn-elkies-linear-programming-bounds/thm-g.md).

## Lean

Formalized as [`SpherePacking.SpherePackingConstant_le_E8Packing_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.SpherePackingConstant_le_E8Packing_density).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/main-result.tex, line 5](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/main-result.tex#L5)
