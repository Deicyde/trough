---
declaration: proposition
origin: cited
lean: MagicFunction.a.SpecialValues.a_zero
statement: formalized
---

# a0

We have $a(0) = \frac{-8640\, i}{\pi}$.

## Depends on

Its statement uses no other node that has an article here.

## Proof

As $r \to 0$, the factor $\sin(\pi r^2/2)^2$ vanishes to order $r^4$; the only term inside the parentheses of [Proposition a-another-integral](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L444) that blows up at that order is $-\frac{8640}{\pi^3 r^4}$. Hence

$$
a(0) = \lim_{r \to 0} 4i\left(\frac{\pi r^2}{2}\right)^2 \cdot \left(-\frac{8640}{\pi^3 r^4}\right) = \frac{-8640\, i}{\pi}.
$$

## Lean

Stated as [`MagicFunction.a.SpecialValues.a_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.SpecialValues.a_zero); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 466](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L466)
