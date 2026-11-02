# The Chebotarev density theorem: the case of cyclotomic extensions

Throughout this section, $K$ is a number field, $m \geq 1$ is a fixed integer, $L = K(\mu_m)$, and $G = \mathrm{Gal}(L/K)$. (In particular $G$ is abelian, and for $K=\mathbb{Q}$ one recovers $G \cong (\mathbb{Z}/m\mathbb{Z})^\times$.) Write $\zeta_K$ and $\zeta_L$ for the Dedekind zeta functions of $K$ and $L$, and for an abelian character $\chi : G \to \mathbb{C}^\times$ write $L(\chi,s)$ for the associated Artin $L$-function (equivalently, the Hecke $L$-function of the ideal character attached to $\chi$; cf. Notation 7.1.17 and Proposition 7.1.18 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>).

The goal of this section is to prove the Chebotarev density theorem in the cyclotomic case (Proposition [Cyclotomic Chebotarev density](chebotarev-cyclotomic-density.md) below), following the classical argument via Artin $L$-functions as in Sharifi, Propositions 7.1.16–7.1.19 and Proposition 7.2.1. The abelian and general cases are then reduced to this one in the subsequent sections.

- [Artin $L$-function as Euler product](artin-l-euler.md)
- [Dedekind-factor](dedekind-factor.md)
- [Simple pole](dedekind-pole.md)
- [Continuation of nontrivial Artin $L$-functions](artin-l-continuation.md)
- [Dedekind-nonvanishing](dedekind-nonvanishing.md)
- [Orthogonality for Frobenius classes](chebotarev-orthogonality.md)
- [Cyclotomic Chebotarev density](chebotarev-cyclotomic-density.md)
- [PNT for one character](dedekind-pnt.md)

*Remark on prime powers.* Expanding $-\frac{L'}{L}(\chi,s)$ as a Dirichlet series selects coefficients supported on prime powers $\mathfrak{p}^j$ with weight $\chi(\varphi_{\mathfrak{p}})^j\log N\mathfrak{p}$. Thus an *exact* identity expressing $-\sum_\chi \chi(\sigma)^{-1}\frac{L'}{L}(\chi,s)$ as a sum over primes with Frobenius $\sigma$ should use the condition $\varphi_{\mathfrak{p}}^j=\sigma$ rather than $\varphi_{\mathfrak{p}}=\sigma$. For the density statement in Proposition [Cyclotomic Chebotarev density](chebotarev-cyclotomic-density.md) this distinction is immaterial: the $j=1$ terms agree with the Frobenius condition, while the $j\geq 2$ terms converge absolutely for $\Re(s)>1/2$ and do not affect the residue at $s=1$.

*The proof of [PNT for one character](dedekind-pnt.md) is shown with its statement.*
