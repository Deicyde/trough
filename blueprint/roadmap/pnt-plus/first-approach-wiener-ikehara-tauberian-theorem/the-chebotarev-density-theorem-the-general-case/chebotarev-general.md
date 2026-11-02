---
declaration: theorem
origin: cited
---

# Chebotarev density theorem

Let $L/K$ be a finite Galois extension of number fields with Galois group $G$, and let $C\subset G$ be a conjugacy class. The set of prime ideals $\mathfrak{p}$ of $K$ unramified in $L$ whose Frobenius conjugacy class equals $C$ has Dirichlet density $|C|/|G|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Reduction to a cyclic subextension](chebotarev-reduction.md)
- [Abelian Chebotarev](../the-chebotarev-density-theorem-the-case-of-abeli/chebotarev-abelian.md)

## Proof

Combine Lemma [Reduction to a cyclic subextension](chebotarev-reduction.md) with Proposition [Abelian Chebotarev](../the-chebotarev-density-theorem-the-case-of-abeli/chebotarev-abelian.md) applied to the cyclic extension $L/E$: the latter gives $\delta(T_\sigma) = 1/f$, whence $\delta(S) = |C|/|G|$.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
