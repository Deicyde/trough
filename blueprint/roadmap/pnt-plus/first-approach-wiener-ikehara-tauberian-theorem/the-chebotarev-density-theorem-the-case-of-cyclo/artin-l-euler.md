---
declaration: lemma
origin: cited
---

# Artin $L$-function as Euler product

Let $\chi : G \to \mathbb{C}^\times$ be an abelian character. For $\Re(s) > 1$ one has

$$
L(\chi,s) \;=\; \prod_{\mathfrak{p}} \bigl(1 - \chi(\mathfrak{p})\, N\mathfrak{p}^{-s}\bigr)^{-1}
\;=\; \sum_{\mathfrak{a} \subseteq \mathcal{O}_K} \chi(\mathfrak{a})\, N\mathfrak{a}^{-s},
$$

where the product runs over nonzero prime ideals of $\mathcal{O}_K$, with the convention $\chi(\mathfrak{p}) = 0$ if $\mathfrak{p}$ ramifies in the fixed field of $\ker\chi$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is the specialisation of the Artin Euler product (Definition 7.1.15 of Sharifi) to abelian characters; see Proposition 7.1.18 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>. Absolute convergence for $\Re(s)>1$ follows from comparison with $\zeta_K(s)$.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
