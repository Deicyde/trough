---
declaration: lemma
origin: cited
lean: Function.Periodic.intervalIntegral_add_eq, intervalIntegral.integral_comp_sub_right
statement: formalized
proof: formalized
---

# periodic domain shift

Let $f$ be a bounded $2\pi$-periodic function. We have for any $0 \le x\le 2\pi$ that

$$
\int_0^{2\pi} f(y)\, dy= \int_{-x}^{2\pi -x} f(y)\, dy
=\int_{-\pi}^{\pi} f(y-x)\, dy\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have by periodicity and change of variables

$$
\int_{-x}^{0} f(y)\, dy=\int_{-x}^{0} f(y+2\pi)\, dy= \int_{2\pi -x}^{2\pi} f(y)\, dy\, .\qquad\text{(25)}
$$

We then have by breaking up the domain of integration and using (25)

$$
\int_0^{2\pi} f(y)\, dy= \int_0^{2\pi -x} f(y)\, dy+
\int_{2\pi -x}^{2\pi} f(y)\, dy
$$

$$
= \int_0^{2\pi -x} f(y)\, dy+
\int_{ -x}^{0} f(y)\, dy
= \int_{-x}^{2\pi-x} f(y)\, dy\, .
$$

This proves the first identity of the lemma. The second identity follows by substitution of $y$ by $y-x$.

## Lean

Formalized as [`Function.Periodic.intervalIntegral_add_eq`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Function.Periodic.intervalIntegral_add_eq), [`intervalIntegral.integral_comp_sub_right`](https://fpvandoorn.github.io/carleson/docs/find/#doc/intervalIntegral.integral_comp_sub_right).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8630](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8630)
