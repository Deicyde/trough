---
declaration: section
origin: cited
lean: CurveDivisor.divZeros, CurveDivisor.divPoles, CurveDivisor.divZeros_apply, CurveDivisor.divPoles_apply, CurveDivisor.divZeros_nonneg, CurveDivisor.divPoles_nonneg, CurveDivisor.divZeros_sub_divPoles
statement: formalized
proof: formalized
---

# Effective parts of curve divisors

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html).

## Zero part of a divisor

For a divisor $D$ on a set of points $C$, the zero part $D^+$ of
$D$ is the divisor on $C$ whose coefficient at each point $P \in C$ is $\max(D(P), 0)$.

Formalized by `CurveDivisor.divZeros`, a definition declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-zeros).

## Pole part of a divisor

For a divisor $D$ on a set of points $C$, the pole part $D^-$ of
$D$ is the divisor on $C$ whose coefficient at each point $P \in C$ is $\max(-D(P), 0)$.

Formalized by `CurveDivisor.divPoles`, a definition declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-poles).

## Coefficients of the zero part

For every divisor $D$ on a set of points $C$ and every
point $P \in C$, the coefficient at $P$ of the zero part $D^+$ of $D$ is $\max(D(P), 0)$.

Formalized by `CurveDivisor.divZeros_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-zeros-apply).

## Coefficients of the pole part

For every divisor $D$ on a set of points $C$ and every
point $P \in C$, the coefficient at $P$ of the pole part $D^-$ of $D$ is $\max(-D(P), 0)$.

Formalized by `CurveDivisor.divPoles_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-poles-apply).

## The zero part of a divisor is effective

For every divisor $D$ on a set of points $C$,
the zero part $D^+$ of $D$ is effective: $D^+(P) \ge 0$ for every point $P \in C$.

Formalized by `CurveDivisor.divZeros_nonneg`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-zeros-nonneg).

## The pole part of a divisor is effective

For every divisor $D$ on a set of points $C$,
the pole part $D^-$ of $D$ is effective: $D^-(P) \ge 0$ for every point $P \in C$.

Formalized by `CurveDivisor.divPoles_nonneg`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-poles-nonneg).

## A divisor is its zero part minus its pole part

For every set of points $C$ and every
divisor $D$ on $C$, let $D^+$ be its zero part, with coefficient $\max(D(P), 0)$ at each point
$P$, and $D^-$ its pole part, with coefficient $\max(-D(P), 0)$ at each point $P$. Then
$D^+ - D^- = D$.

Formalized by `CurveDivisor.divZeros_sub_divPoles`, a theorem declared in [MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/Curve/EffectiveParts.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html#div-zeros-sub-div-poles).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Effective parts of curve divisors](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/algebraic-curves/divisors-on-curves/effective-parts-of-curve-divisors)
