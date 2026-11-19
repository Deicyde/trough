---
declaration: lemma
origin: cited
lean: MeasureTheory.eLpNorm_pow_eq_distribution
statement: formalized
proof: formalized
---

# layer cake representation

Let $1\le p< \infty$. Then for any measurable function $u:X\to [0,\infty)$ on the measure space $X$ relative to the measure $\mu$ we have

$$
\|u\|_p^p=p\int_0^\infty \lambda^{p-1}\mu(\{x: u(x)\ge \lambda\})\, d\lambda\, .\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The left-hand side of (1) is by definition

$$
\int_X u(x)^p \, d\mu(x)\, .
$$

Writing $u(x)$ as an elementary integral in $\lambda$ and then using Fubini, we write for the last display

$$
=\int_X \int _0^{u(x)}
p \lambda^{p-1} d\lambda\, d\mu(x)
$$

$$
=p\int _0^{\infty}
\lambda^{p-1} \mu(\{x: u(x)\ge \lambda\}) d\lambda\, .
$$

This proves the lemma.

## Lean

Formalized as [`MeasureTheory.eLpNorm_pow_eq_distribution`](https://fpvandoorn.github.io/carleson/docs/find/#doc/MeasureTheory.eLpNorm_pow_eq_distribution).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6683](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6683)
