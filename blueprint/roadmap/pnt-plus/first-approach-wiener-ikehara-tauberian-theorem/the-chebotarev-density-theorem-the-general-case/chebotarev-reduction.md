---
declaration: lemma
origin: cited
---

# Reduction to a cyclic subextension

Fix $\sigma\in C$ and let $E$ be the fixed field of $\langle\sigma\rangle$, so $L/E$ is cyclic of degree $f = |\langle\sigma\rangle|$. Write $S$ for the set of primes of $K$ unramified in $L$ whose Frobenius class equals $C$, and $T_\sigma$ for the set of primes $\mathfrak{P}$ of $E$ unramified in $L$ (and lying over $K$) with Frobenius equal to $\sigma$. Then

$$
\delta(S) \;=\; \frac{f\,|C|}{|G|}\,\delta(T_\sigma),
$$

whenever either density exists. In particular, the Chebotarev statement for $L/K$ and $C$ follows from the abelian statement for the cyclic extension $L/E$ and the element $\sigma$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $\mathfrak{P}\in T_\sigma$, then $\varphi_{\mathfrak{P}}=\sigma$ fixes $E$, so $\mathfrak{P}$ has residue degree one over $K$. There are exactly $|G|/f$ primes of $L$ over $\mathfrak{P}\cap K$, and their Frobenii are equidistributed among the $|C|$ elements of the conjugacy class $C$; exactly $|G|/(f\,|C|)$ of them have Frobenius $\sigma$. Comparing the Dirichlet series $\sum N\mathfrak{p}^{-s}$ over $S$ with $\sum N\mathfrak{P}^{-s}$ over $T_\sigma$ (and using $\sum_{\mathfrak{p}} N\mathfrak{p}^{-s} \sim \sum_{\mathfrak{P}} N\mathfrak{P}^{-s}$) yields the displayed identity. See Sharifi, Theorem 7.2.2, Step 1.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
