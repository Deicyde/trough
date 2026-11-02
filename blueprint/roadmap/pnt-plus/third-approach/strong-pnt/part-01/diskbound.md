---
declaration: lemma
origin: cited
lean: DiskBound
statement: formalized
proof: formalized
---

# DiskBound

Let $0 < r < R<1$. If $f:\mathbb{C}\to\mathbb{C}$ is a function analytic on $\overline{\mathbb{D}_1}$ with $f(0)\neq0$ such that $|f(z)|\leq B$ for $|z|\leq R$, then $|B_f(z)|\leq B$ for $|z|\leq R$ also.

## Depends on

- [BlaschkeB](blaschkeb.md)
- [SetOfZeros](setofzeros.md)

## Proof depends on

- [CFunction](cfunction.md)
- [AnalyticOn.norm-le-of-norm-le-on-sphere](analyticon-norm-le-of-norm-le-on-sphere.md)
- [ZeroFactor](zerofactor.md)
- [BlaschkeAnalytic](blaschkeanalytic.md)

## Proof

For $|z|=R$, we know that $z\not\in\mathcal{K}_f(r)$. Thus,

$$
C_f(z)=\frac{f(z)}{\displaystyle\prod_{\rho\in\mathcal{K}_f(r)}(z-\rho)^{m_f(\rho)}}.
$$

Thus, substituting this into Definition [BlaschkeB](blaschkeb.md),

$$
|B_f(z)|=|f(z)|\prod_{\rho\in\mathcal{K}_f(r)}
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|^{m_f(\rho)}.
$$

But note that

$$
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|
=\frac{|R^2-z\overline{\rho}|/R}{|z-\rho|}
=\frac{|z|\cdot|\overline{z-\rho}|/R}{|z-\rho|}=1.
$$

So we have that $|B_f(z)|=|f(z)|\leq B$ when $|z|=R$. Now by the maximum modulus principle, we know that the maximum of $|B_f|$ must occur on the boundary where $|z|=R$. Thus $|B_f(z)|\leq B$ for all $|z|\leq R$.

## Lean

Formalized as [`DiskBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/DiskBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
