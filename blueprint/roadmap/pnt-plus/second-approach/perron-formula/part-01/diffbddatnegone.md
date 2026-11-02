---
declaration: lemma
origin: cited
lean: Perron.diffBddAtNegOne
statement: formalized
proof: formalized
---

# diffBddAtNegOne

Let $x>0$. Then for $0 < c < 1 /2$, we have that the function

$$
s ↦ \frac{x^s}{s(s+1)} - \frac{-x^{-1}}{s+1}
$$

is bounded above on the rectangle with corners at $-1-c-i*c$ and $-1+c+i*c$ (except at $s=-1$).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [keyIdentity](keyidentity.md)

## Proof

Applying Lemma [keyIdentity](keyidentity.md), the function $s ↦ x^s/s(s+1) - x^{-1}/(s+1) = x^s/s - x^s/(s+1) - (-x^{-1})/(s+1)$. The first term is bounded for $s$ away from $0$. The last two terms are the difference quotient of the function $s ↦ x^s$ at $-1$; since it's differentiable, the difference remains bounded as $s\to -1$.

## Lean

Formalized as [`Perron.diffBddAtNegOne`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.diffBddAtNegOne).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
