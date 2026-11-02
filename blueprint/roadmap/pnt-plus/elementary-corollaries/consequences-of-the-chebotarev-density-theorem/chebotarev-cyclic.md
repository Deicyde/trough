---
declaration: lemma
origin: cited
---

# Cyclotomic Chebotarev

Let $m\geq 1$ and $G = \mathrm{Gal}(\mathbb{Q}(\mu_m)/\mathbb{Q}) \cong (\mathbb{Z}/m\mathbb{Z})^\times$. For any $a$ coprime to $m$,

$$
\sum_{\substack{N\mathfrak{p}\leq x\\ N\mathfrak{p}\equiv a\pmod{m}}} \log N\mathfrak{p}
\;=\;
\frac{1}{|G|} \sum_{N\mathfrak{p}\leq x} \log N\mathfrak{p}
\;+\; o\Bigl(\sum_{N\mathfrak{p}\leq x} \log N\mathfrak{p}\Bigr).
$$

In particular the primes in the progression $a\pmod{m}$ have natural density $1/\varphi(m)$ (Dirichlet's theorem).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Cyclotomic Chebotarev density](../../first-approach-wiener-ikehara-tauberian-theorem/the-chebotarev-density-theorem-the-case-of-cyclo/chebotarev-cyclotomic-density.md)
- [PNT for one character](../../first-approach-wiener-ikehara-tauberian-theorem/the-chebotarev-density-theorem-the-case-of-cyclo/dedekind-pnt.md)
- [WeakPNT-AP](../../first-approach-wiener-ikehara-tauberian-theorem/the-prime-number-theorem-in-arithmetic-progressi/weakpnt-ap.md)

## Proof

Specialise Proposition [Cyclotomic Chebotarev density](../../first-approach-wiener-ikehara-tauberian-theorem/the-chebotarev-density-theorem-the-case-of-cyclo/chebotarev-cyclotomic-density.md) to $K=\mathbb{Q}$ and $L=\mathbb{Q}(\mu_m)$: the Frobenius condition $\varphi_p=\sigma_a$ with $\sigma_a(\zeta_m)=\zeta_m^a$ is exactly $p\equiv a\pmod{m}$. The asymptotic form with $\log N\mathfrak{p}$ follows by Fourier expansion of the indicator of the progression against characters of $G$, using Lemma [PNT for one character](../../first-approach-wiener-ikehara-tauberian-theorem/the-chebotarev-density-theorem-the-case-of-cyclo/dedekind-pnt.md) to kill the nontrivial character sums and the prime-number theorem in AP (Lemma [WeakPNT-AP](../../first-approach-wiener-ikehara-tauberian-theorem/the-prime-number-theorem-in-arithmetic-progressi/weakpnt-ap.md)) for the main term. Cf. also Corollary 7.2.3 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
