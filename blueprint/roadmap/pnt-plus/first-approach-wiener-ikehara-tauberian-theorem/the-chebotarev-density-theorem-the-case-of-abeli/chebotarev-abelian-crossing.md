---
declaration: lemma
origin: cited
---

# Cyclotomic crossing

Choose an integer $m\geq 1$ not dividing the discriminant of $L/K$, large enough that $H := \mathrm{Gal}(L(\mu_m)/L) \cong (\mathbb{Z}/m\mathbb{Z})^\times$ via the cyclotomic character and $\mathrm{Gal}(L(\mu_m)/K) \cong G \times H$. For $\sigma\in G$ and $\tau\in H$ write $S_{\sigma,\tau}$ for the set of primes of $K$ unramified in $L(\mu_m)$ with Frobenius $(\sigma,\tau)\in G\times H$, and $S_\sigma$ for the set of primes of $K$ unramified in $L$ with Frobenius $\sigma$ in $G$. Then

$$
\delta_{\mathrm{inf}}(S_\sigma) \;=\; \sum_{\tau\in H} \delta_{\mathrm{inf}}(S_{\sigma,\tau}).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Every prime counted in $S_\sigma$ lifts to primes in the various $S_{\sigma,\tau}$ according to the Frobenius in the cyclotomic layer; the identity of lower densities is the usual additivity of Dirichlet densities over a finite partition (up to the finitely many ramified primes).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
