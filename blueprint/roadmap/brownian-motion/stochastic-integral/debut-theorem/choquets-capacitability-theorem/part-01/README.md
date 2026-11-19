---
navigation: transparent
---

# supClosure to IsPavingAnalytic.exists_mem_coun…

- [supClosure](def-supclosure.md)
- [infClosure](def-infclosure.md)
- [countableSupClosure](def-countablesupclosure.md)
- [countableInfClosure](def-countableinfclosure.md)
- [InfClosed.mem_countableInfClosure_iff](lem-infclosed-mem-countableinfclosure-iff.md)
- [SupClosed.mem_countableSupClosure_iff](lem-supclosed-mem-countablesupclosure-iff.md)
- [IsCompactSystem](def-iscompactsystem.md)
- [isCompactSystem_isCompact_isClosed](lem-iscompactsystem-iscompact-isclosed.md)
- [isCompactSystem_isCompact](lem-iscompactsystem-iscompact.md)
- [IsCompactSystem.mono](lem-iscompactsystem-mono.md)
- [isCompactSystem_Icc](lem-iscompactsystem-icc.md)
- [IsCompactSystem.sigma](lem-iscompactsystem-sigma.md)
- [IsCompactSystem.prod](lem-iscompactsystem-prod.md)
- [IsCompactSystem.supClosure](lem-iscompactsystem-supclosure.md)
- [IsCompactSystem.infClosure](lem-iscompactsystem-infclosure.md)
- [fst_iInter_of_supClosure_image2_prod_of_antitone](thm-fst-iinter-of-supclosure-image2-prod-of-anti.md)

## Analytic sets

- [Analytic set](def-ispavinganalytic.md)

Some references require $\mathcal{K}$ to be nonempty and $\emptyset \in K$. This gives the same notion: if $K$ is a compact system then so is $K \cup \{\emptyset\}$, and a set that is analytic with an empty $\mathcal{K}$ is empty, hence analytic with $\mathcal{K} = \mathbb{R}$.

Lean note: we can't quantify over universes, so we have to restrict $\mathcal{K}$ to `Type`. We have an auxiliary definition `IsPavingAnalyticFor` that specifies which $\mathcal{K}$ is used.

- [isPavingAnalytic_of_prop](lem-ispavinganalytic-of-prop.md)
- [IsPavingAnalytic.mono](lem-ispavinganalytic-mono.md)
- [IsPavingAnalytic.exists_mem_countableSupClosure_superset](lem-ispavinganalytic-exists-mem-countablesupclos.md)
