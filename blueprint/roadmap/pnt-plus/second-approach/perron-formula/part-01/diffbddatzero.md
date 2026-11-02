---
declaration: lemma
origin: cited
lean: Perron.diffBddAtZero
statement: formalized
proof: formalized
---

# diffBddAtZero

Let $x>0$. Then for $0 < c < 1 /2$, we have that the function

$$
s ↦ \frac{x^s}{s(s+1)} - \frac1s
$$

is bounded above on the rectangle with corners at $-c-i*c$ and $c+i*c$ (except at $s=0$).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [keyIdentity](keyidentity.md)

## Proof

Applying Lemma [keyIdentity](keyidentity.md), the function $s ↦ x^s/s(s+1) - 1/s = x^s/s - x^0/s - x^s/(1+s)$. The last term is bounded for $s$ away from $-1$. The first two terms are the difference quotient of the function $s ↦ x^s$ at $0$; since it's differentiable, the difference remains bounded as $s\to 0$.

## Lean

Formalized as [`Perron.diffBddAtZero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.diffBddAtZero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
