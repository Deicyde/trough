---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Complex.integral_boundary_unbounded_rect_eq_zero_of_differentiable_on_off_countable_of_integrable_on, Complex.tendsto_integral_boundary_unbounded_rect_one_side_atTop_nhds_sum_other_two_sides
---

# Cauchy–Goursat for unbounded rectangular contours

Let $x_1 \leq x_2$ and $y$ be real numbers, and let $f : \mathbb{C} \to \mathbb{C}$ be continuous on the half-strip $S := \{x_1 \leq \Re z \leq x_2,\ \Im z \geq y\}$ and holomorphic on its interior. Suppose that $f(z) \to 0$ as $\Im z \to \infty$ with $z$ in the vertical strip $\{x_1 \leq \Re z \leq x_2\}$ (that is, uniformly for $x_1 \leq \Re z \leq x_2$), and that $f$ is integrable on the two vertical rays $x_1 + i[y, \infty)$ and $x_2 + i[y, \infty)$. Then

$$
\int_{x_1 + iy}^{x_1 + i\infty} f(z)\, \mathrm{d} z
= \int_{x_1 + iy}^{x_2 + iy} f(z)\, \mathrm{d} z + \int_{x_2 + iy}^{x_2 + i\infty} f(z)\, \mathrm{d} z.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Apply the Cauchy–Goursat theorem for rectangles to the truncated rectangles $\{x_1 \leq \Re z \leq x_2,\ y \leq \Im z \leq T\}$ and let $T \to \infty$: the integral over the upper edge $[x_1 + iT, x_2 + iT]$ tends to $0$ because the decay is uniform on the strip, and the integrals over the truncated vertical sides tend to the integrals over the rays by integrability.

## Lean

Formalized as [`Complex.integral_boundary_unbounded_rect_eq_zero_of_differentiable_on_off_countable_of_integrable_on`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Complex.integral_boundary_unbounded_rect_eq_zero_of_differentiable_on_off_countable_of_integrable_on), [`Complex.tendsto_integral_boundary_unbounded_rect_one_side_atTop_nhds_sum_other_two_sides`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Complex.tendsto_integral_boundary_unbounded_rect_one_side_atTop_nhds_sum_other_two_sides).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 361](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L361)
