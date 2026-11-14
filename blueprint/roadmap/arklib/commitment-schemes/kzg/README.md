# KZG

ArkLib formalizes the KZG polynomial commitment scheme ([Kate et al. 2010a](https://doi.org/10.1007/978-3-642-17373-8_11)) and its evaluation binding proof from the extended version ([Kate et al. 2010b](https://cacr.uwaterloo.ca/techreports/2010/cacr2010-10.pdf)). Fix a prime $p$, groups $G_1,G_2,G_T$ of order $p$ with generators $g_1\in G_1$ and $g_2\in G_2$, and a $\mathbb{Z}_p$-bilinear pairing $e:G_1\times G_2\to G_T$. Fix a maximal degree $n$. The committed data is a coefficient vector $(a_0,\ldots,a_n)\in\mathbb{Z}_p^{n+1}$, that is, a polynomial $f$ of degree at most $n$; a query is a point $z\in\mathbb{Z}_p$ and its response is $f(z)$.

- [KZG commitment scheme](def-kzg.md)
- [KZG correctness](thm-kzg-correctness.md)
- [$t$-SDH](def-tsdh.md)
- [The assumption needs a restricted class](lem-tsdh-not-univ.md)
- [KZG evaluation binding](thm-kzg-binding.md)
- [KZG function binding](thm-kzg-function-binding.md)
