---
declaration: section
origin: cited
lean: CurveDivisor, CurveDivisor.coeff
statement: formalized
proof: formalized
---

# Divisors on a curve

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/divisors-on-a-curve/index.html).

## Divisors on a curve

For a set $C$ (the points of a curve), a divisor on $C$ is a finitely
supported function $D \colon C \to \mathbb{Z}$. Its support is the finite set of points
$P \in C$ with $D(P) \neq 0$.

Formalized by `CurveDivisor`, an abbreviation declared in [MathlibExt/AlgebraicGeometry/Curve/Divisor.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/Divisor.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/divisors-on-a-curve/index.html#curve-divisor).

## Coefficient of a divisor at a point

For a divisor $D$ on a set of points $C$ and a
point $P \in C$, the coefficient of $D$ at $P$ is the integer $D(P)$.

Formalized by `CurveDivisor.coeff`, a definition declared in [MathlibExt/AlgebraicGeometry/Curve/Divisor.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/Divisor.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/divisors-on-a-curve/index.html#coeff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisors on a curve](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/divisors-on-a-curve/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/divisors-on-a-curve)
