---
declaration: lemma
origin: cited
lean: BlaschkeNonzero
statement: formalized
proof: formalized
---

# BlaschkeNonZero

Let $0 < r < R<1$ and $f:\overline{\mathbb{D}_1}\to\mathbb{C}$ be analytic on neighborhoods of points in $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. Then $B_f(z)\neq 0$ for all $z\in\overline{\mathbb{D}_r}$.

## Depends on

- [BlaschkeB](blaschkeb.md)
- [SetOfZeros](setofzeros.md)

## Proof depends on

- [CFunction](cfunction.md)
- [ZeroFactorization](zerofactorization.md)
- [ZeroFactor](zerofactor.md)

## Proof

Suppose that $z\in\mathcal{K}_f(r)$. Then we have that

$$
C_f(z)=\frac{h_z(z)}{\displaystyle\prod_{\rho\in\mathcal{K}_f(r)\setminus\{z\}}
(z-\rho)^{m_f(\rho)}}.
$$

where $h_z(z)\neq 0$ according to Lemma [ZeroFactorization](zerofactorization.md). Thus, substituting this into Definition [BlaschkeB](blaschkeb.md),

$$
|B_f(z)|=|h_z(z)|\cdot\left|R-\frac{|z|^2}{R}\right|^{m_f(z)}
\prod_{\rho\in\mathcal{K}_f(r)\setminus\{z\}}
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|^{m_f(\rho)}.\qquad\text{(2)}
$$

Trivially, $|h_z(z)|\neq 0$. Now note that

$$
\left|R-\frac{|z|^2}{R}\right|=0\implies|z|=R.
$$

However, this is a contradiction because $z\in\overline{\mathbb{D}_r}$ tells us that $|z|\leq r < R$. Similarly, note that

$$
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|=0\implies|z|=\frac{R^2}{|\overline{\rho}|}.
$$

However, this is also a contradiction because $\rho\in\mathcal{K}_f(r)$ tells us that $R < R^2/|\overline{\rho}|=|z|$, but $z\in\overline{\mathbb{D}_r}$ tells us that $|z|\leq r < R$. So, we know that

$$
\left|R-\frac{|z|^2}{R}\right|\neq 0\qquad\text{and}\qquad
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|\neq 0
\quad\text{for all}\quad\rho\in\mathcal{K}_f(r)\setminus\{z\}.
$$

Applying this to Equation (2) we have that $|B_f(z)|\neq 0$. So, $B_f(z)\neq 0$.

Now suppose that $z\not\in\mathcal{K}_f(r)$. Then we have that

$$
C_f(z)=\frac{f(z)}{\displaystyle\prod_{\rho\in\mathcal{K}_f(r)}(z-\rho)^{m_f(\rho)}}.
$$

Thus, substituting this into Definition [BlaschkeB](blaschkeb.md),

$$
|B_f(z)|=|f(z)|\prod_{\rho\in\mathcal{K}_f(r)}
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|^{m_f(\rho)}.\qquad\text{(3)}
$$

We know that $|f(z)|\neq 0$ since $z\not\in\mathcal{K}_f(r)$. Now note that

$$
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|=0\implies|z|=\frac{R^2}{|\overline{\rho}|}.
$$

However, this is a contradiction because $\rho\in\mathcal{K}_f(r)$ tells us that $R < R^2/|\overline{\rho}|=|z|$, but $z\in\overline{\mathbb{D}_r}$ tells us that $|z|\leq r < R$. So, we know that

$$
\left|\frac{R-z\overline{\rho}/R}{z-\rho}\right|\neq 0
\quad\text{for all}\quad\rho\in\mathcal{K}_f(r).
$$

Applying this to Equation (3) we have that $|B_f(z)|\neq 0$. So, $B_f(z)\neq 0$.

We have shown that $B_f(z)\neq 0$ for both $z\in\mathcal{K}_f(r)$ and $z\not\in\mathcal{K}_f(r)$, so the result follows.

## Lean

Formalized as [`BlaschkeNonzero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/BlaschkeNonzero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
