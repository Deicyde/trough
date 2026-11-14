---
declaration: theorem
origin: cited
lean: LinearProgrammingBound
statement: formalized
proof: formalized
---

# LP-d24

Suppose $f:\mathbb{R}^{24}\to\mathbb{R}$ is a Schwartz function with $f(0)=\widehat f(0)=1$, $\widehat f(y)\ge 0$ for all $y\in\mathbb{R}^{24}$, and $f(x)\le 0$ for $\|x\|\ge 2$. Then every sphere packing in $\mathbb{R}^{24}$ has density at most $\pi^{12}/12!$.

## Depends on

- [Cohn–Elkies (ElkiesCohn)](../../cohn-elkies-linear-programming-bounds/thm-cohn-elkies-general.md)
- [SpherePacking.scale_density](../../sphere-packings/def-spherepacking-scale-density.md)

## Proof

This is the Cohn–Elkies bound [Cohn–Elkies (ElkiesCohn)](../../cohn-elkies-linear-programming-bounds/thm-cohn-elkies-general.md) after scaling to convert the cutoff radius $2$ to the normalized cutoff radius $1$ (and using [Lemma SpherePacking.scale_density](../../sphere-packings/def-spherepacking-scale-density.md) to identify densities under scaling).

## Lean

Formalized as [`LinearProgrammingBound`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/LinearProgrammingBound).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-main.tex, line 37](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-main.tex#L37)
