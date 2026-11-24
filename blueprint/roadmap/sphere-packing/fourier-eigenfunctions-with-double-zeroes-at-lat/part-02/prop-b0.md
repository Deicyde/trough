---
declaration: proposition
origin: cited
lean: MagicFunction.b.SpecialValues.b_zero
statement: formalized
---

# b0

We have $b(0) = 0$.

## Depends on

Its statement uses no other node that has an article here.

## Proof

As $r \to 0$, the factor $\sin(\pi r^2/2)^2$ vanishes to order $r^4$, while the expression in parentheses in [Proposition b-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L785) has only a simple pole in $r^2$ (the term $\frac{144}{\pi r^2}$). Hence the product tends to $0$.

## Lean

Stated as [`MagicFunction.b.SpecialValues.b_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.SpecialValues.b_zero); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 810](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L810)
