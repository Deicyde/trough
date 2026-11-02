---
declaration: theorem
origin: cited
lean: ZetaFixedLowerBound
statement: formalized
proof: formalized
---

# ZetaFixedLowerBound

For all $t\in\mathbb{R}$ one has

$$
|\zeta(3/2+it)|\geq\frac{\zeta(3)}{\zeta(3/2)}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From the Euler product expansion of $\zeta$, we have that for $\Re s>1$

$$
\zeta(s)=\prod_p\frac{1}{1-p^{-s}}.
$$

Thus, we have that

$$
\frac{\zeta(2s)}{\zeta(s)}=\prod_p\frac{1-p^{-s}}{1-p^{-2s}}=\prod_p\frac{1}{1+p^{-s}}.
$$

Now note that $|1-p^{-(3/2+it)}|\leq 1+|p^{-(3/2+it)}|=1+p^{-3/2}$. Thus,

$$
|\zeta(3/2+it)|=\prod_p\frac{1}{|1-p^{-(3/2+it)}|}
\geq\prod_p\frac{1}{1+p^{-3/2}}=\frac{\zeta(3)}{\zeta(3/2)}
$$

for all $t\in\mathbb{R}$ as desired.

## Lean

Formalized as [`ZetaFixedLowerBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaFixedLowerBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
