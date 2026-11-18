---
declaration: theorem
origin: cited
lean: BorelCaratheodoryDeriv
statement: formalized
proof: formalized
---

# BorelCaratheodoryDeriv

Let $R,\,M>0$. Let $f$ be analytic on $|z|\leq R$ such that $f(0)=0$ and suppose $\Re f(z)\leq M$ for all $|z|\leq R$. Then for any $0 < r < R$,

$$
|f'(z)|\leq\frac{16MR^2}{(R-r)^3}
$$

for all $|z|\leq r$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [DerivativeBound](derivativebound.md)

## Proof

Using Lemma [DerivativeBound](derivativebound.md) with $r'=(R+r)/2$, and noting that $r < R$, we have that

$$
|f'(z)|\leq\frac{4M(R+r)^2}{(R-r)^3}\leq\frac{16MR^2}{(R-r)^3}.
$$

## Lean

Formalized as [`BorelCaratheodoryDeriv`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/BorelCaratheodoryDeriv).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
