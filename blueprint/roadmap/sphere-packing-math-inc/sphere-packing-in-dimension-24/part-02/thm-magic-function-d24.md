---
declaration: theorem
origin: cited
lean: SpherePacking.Dim24.SpherePackingConstant_le_leech_density
statement: formalized
proof: formalized
---

# magic-function-d24

The function $f$ satisfies the hypotheses of [Theorem LP-d24](../part-01/thm-lp-d24.md), and therefore $\Delta_{24}\le \pi^{12}/12!$. In particular, the Leech lattice packing is optimal.

## Depends on

- [LP-d24](../part-01/thm-lp-d24.md)
- [f-d24](def-f-d24.md)
- [f-basic-d24](lem-f-basic-d24.md)
- [f-integral-d24](lem-f-integral-d24.md)
- [varphi-neg-d24](lem-varphi-neg-d24.md)
- [B-nonneg-d24](lem-b-nonneg-d24.md)
- [B-leadingterms-d24](lem-b-leadingterms-d24.md)
- [LeechPacking-density](../part-01/lem-leechpacking-density.md)

## Proof

Using [Lemma f-integral-d24](lem-f-integral-d24.md), the inequality $f(r)\le 0$ for $r\ge 2$ reduces to showing $A(t)\le 0$, which follows from $\psi_S(it)\le 0$ (by its theta-function expression) and [Lemma varphi-neg-d24](lem-varphi-neg-d24.md). Similarly, $\widehat f(r)\ge 0$ for $r>\sqrt2$ reduces to $B(t)\ge 0$, which is [Lemma B-nonneg-d24](lem-b-nonneg-d24.md). The remaining range $0\lt r\lt \sqrt2$ is handled by subtracting the leading asymptotic terms of $B(t)$ for $t\ge 1$, and [Lemma B-leadingterms-d24](lem-b-leadingterms-d24.md) supplies the required inequality. The linear programming bound [Theorem LP-d24](../part-01/thm-lp-d24.md) then yields $\Delta_{24}\le \pi^{12}/12!$, matching [Lemma LeechPacking-density](../part-01/lem-leechpacking-density.md).

## Lean

Formalized as [`SpherePacking.Dim24.SpherePackingConstant_le_leech_density`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.SpherePackingConstant_le_leech_density).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-proof.tex, line 66](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-proof.tex#L66)
