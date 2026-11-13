---
declaration: section
origin: cited
lean: WeierstrassCurve.Affine.IsSupersingular, WeierstrassCurve.Affine.IsSupersingular.of_pow_torsion, WeierstrassCurve.Affine.IsSupersingular.pow_torsion
statement: formalized
proof: formalized
---

# Supersingular elliptic curves

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves/index.html).

## Supersingular elliptic curves

Let $p$ be a prime and let $E$ be an elliptic curve over an
algebraic closure $\overline{\mathbb{F}}_p$ of $\mathbb{Z}/p\mathbb{Z}$. Then $E$ is called
supersingular when every point $P \in E(\overline{\mathbb{F}}_p)$ with $pP = 0$ is $P = 0$.

## Sources

- arXiv:2308.11539v1, `main.tex`, lines 164–170, which gives the equivalent condition that for every positive integer $r$, every point $P$ with $p^r P = 0$ is $P = 0$; this definition is its case $r = 1$.

Formalized by `WeierstrassCurve.Affine.IsSupersingular`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves/index.html#is-supersingular).

## Supersingularity from trivial prime-power torsion

Let $p$ be a prime and let $E$ be an
elliptic curve over an algebraic closure $\overline{\mathbb{F}}_p$ of $\mathbb{Z}/p\mathbb{Z}$. If
for every integer $r \ge 1$ the only point $P \in E(\overline{\mathbb{F}}_p)$ with $p^r P = 0$ is
$P = 0$, then $E$ is supersingular.

Formalized by `WeierstrassCurve.Affine.IsSupersingular.of_pow_torsion`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves/index.html#of-pow-torsion).

## Supersingular curves have trivial prime-power torsion

Let $p$ be a prime and let $E$ be a
supersingular elliptic curve over an algebraic closure $\overline{\mathbb{F}}_p$ of
$\mathbb{Z}/p\mathbb{Z}$. Then for every integer $r \ge 1$, every point
$P \in E(\overline{\mathbb{F}}_p)$ with $p^r P = 0$ is $P = 0$.

Formalized by `WeierstrassCurve.Affine.IsSupersingular.pow_torsion`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/Supersingular.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves/index.html#pow-torsion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Supersingular elliptic curves](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/supersingular-elliptic-curves)
