---
declaration: lemma
origin: cited
---

# Density after cyclotomic crossing

In the notation of Lemma [Cyclotomic crossing](chebotarev-abelian-crossing.md), if the order of $\tau\in H$ is divisible by $|G|$, then $\langle(\sigma,\tau)\rangle \cap (G\times\{1\}) = \{1\}$, so $L(\mu_m)$ is obtained by adjoining $\mu_m$ to the fixed field $F := L(\mu_m)^{\langle(\sigma,\tau)\rangle}$. Applying Proposition [Cyclotomic Chebotarev density](../the-chebotarev-density-theorem-the-case-of-cyclo/chebotarev-cyclotomic-density.md) to the cyclotomic extension $F(\mu_m)/F$ and transporting densities as in the reduction step of Theorem 7.2.2 yields $\delta(S_{\sigma,\tau}) = 1/(|G|\,|H|)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Cyclotomic Chebotarev density](../the-chebotarev-density-theorem-the-case-of-cyclo/chebotarev-cyclotomic-density.md)
- [Cyclotomic crossing](chebotarev-abelian-crossing.md)

## Proof

See Sharifi, Theorem 7.2.2, Step 2 (display after “Now suppose that $|G|$ divides the order of $\tau$”).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
