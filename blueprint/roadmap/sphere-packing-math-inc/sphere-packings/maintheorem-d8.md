---
declaration: corollary
origin: cited
lean: SpherePacking.Dim8.MainTheorem
statement: formalized
proof: formalized
---

# MainTheorem-d8

$\Delta_8 = \Delta_{E_8}$.

## Depends on

- [upper-bound-E8](corollary-upper-bound-e8.md)

## Proof

By definition, $\Delta_{E_8} \leq \Delta_8$, while [Corollary upper-bound-E8](corollary-upper-bound-e8.md) shows $\Delta_8 = \sup_{\mathrm{packing} \, \mathcal{P}} \leq \Delta_{E_8}$, and the result follows.

## Lean

Formalized as [`SpherePacking.Dim8.MainTheorem`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim8.MainTheorem).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/main-result.tex, line 19](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/main-result.tex#L19)
