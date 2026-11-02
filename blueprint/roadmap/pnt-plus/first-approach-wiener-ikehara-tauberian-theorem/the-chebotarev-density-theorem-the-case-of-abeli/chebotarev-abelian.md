---
declaration: proposition
origin: cited
---

# Abelian Chebotarev

Let $L/K$ be finite abelian with Galois group $G$. For every $\sigma\in G$, the Dirichlet density of primes of $K$ with Frobenius $\sigma$ exists and equals $1/|G|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Cyclotomic crossing](chebotarev-abelian-crossing.md)
- [Density after cyclotomic crossing](chebotarev-abelian-density.md)
- [Cyclotomic Chebotarev density](../the-chebotarev-density-theorem-the-case-of-cyclo/chebotarev-cyclotomic-density.md)

## Proof

Let $H_n \subset H$ be the set of elements whose order is divisible by $n$. Summing the densities of Lemma [Density after cyclotomic crossing](chebotarev-abelian-density.md) over $\tau\in H_n$ gives $\delta_{\mathrm{inf}}(S_\sigma) \geq |H_n|/(|G|\,|H|)$. Choosing $m$ so that $|H_n|/|H|$ is arbitrarily close to $1$ (possible since there are primes $m\equiv 1\pmod{n^j}$ by the cyclotomic case already proved, and $|H_n|/|H|$ tends to $1$ as $j\to\infty$), one obtains $\delta_{\mathrm{inf}}(S_\sigma) \geq 1/|G|$. Summing over $\sigma\in G$ forces equality throughout, so each density exists and equals $1/|G|$.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
