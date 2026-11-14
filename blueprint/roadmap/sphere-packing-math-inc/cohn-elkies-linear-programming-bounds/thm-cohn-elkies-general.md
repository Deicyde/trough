---
declaration: theorem
origin: cited
lean: LinearProgrammingBound
statement: formalized
proof: formalized
---

# Cohn–Elkies (ElkiesCohn)

Let $f:\mathbb{R}^d\to\mathbb{R}$ be a Schwartz function that is not identically zero and satisfies [(1)](thm-cohn-elkies-periodic.md) and [(2)](thm-cohn-elkies-periodic.md). Then the density of any $\Lambda$-periodic sphere packing is bounded above by

$$
\frac{f(0)}{\widehat{f}(0)}\cdot \mathrm{vol}(B_d(0,1/2)).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-periodic.md)
- [periodic-packing-optimal](../sphere-packings/thm-periodic-packing-optimal.md)

## Proof

The result follows immediately from Theorem [periodic-packing-optimal](../sphere-packings/thm-periodic-packing-optimal.md) and [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-periodic.md).

## Lean

Formalized as [`LinearProgrammingBound`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/LinearProgrammingBound).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/cohn-elkies.tex, line 36](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/cohn-elkies.tex#L36)
