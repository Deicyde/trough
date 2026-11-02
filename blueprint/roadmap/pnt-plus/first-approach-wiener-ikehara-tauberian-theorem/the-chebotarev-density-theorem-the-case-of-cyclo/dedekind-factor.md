---
declaration: lemma
origin: cited
---

# Dedekind-factor

For $\Re(s) > 1$ one has

$$
\zeta_L(s) \;=\; \prod_{\chi : G \to \mathbb{C}^\times} L(\chi,s),
$$

where the product runs over all (necessarily one-dimensional) irreducible characters of $G$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Artin $L$-function as Euler product](artin-l-euler.md)

## Proof

In general, for a Galois extension $L/K$ and characters $\chi$ of irreducible representations of $\mathrm{Gal}(L/K)$, Proposition 7.1.16 of <https://www.math.ucla.edu/~sharifi/algnum.pdf> gives $\zeta_L(s) = \prod_\chi L(\chi,s)^{\chi(1)}$ for $\Re(s)>1$. In the present abelian (cyclotomic) setting every irreducible character is one-dimensional, so $\chi(1)=1$ and the exponents disappear. Alternatively, comparing Euler factors at an unramified prime $\mathfrak{p}$: the primes of $L$ above $\mathfrak{p}$ contribute the factor $(1 - N\mathfrak{p}^{-fs})^{-g}$ to $\zeta_L$, while the Artin factors multiply to the same quantity by the usual identity $\prod_\chi (1 - \chi(\varphi_{\mathfrak{p}}) X) = 1 - X^f$ (with $X = N\mathfrak{p}^{-s}$ and $f$ the residue degree).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
