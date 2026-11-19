---
declaration: lemma
origin: cited
lean: dens1_le_dens'
statement: formalized
proof: formalized
---

# dens compare

We have for every $k\ge 0$ and ${\mathfrak P}'\subset {\mathfrak P}(k)$

$$
\operatorname{\operatorname{dens}}_1({\mathfrak P}')\le \operatorname{\operatorname{dens}}_k'({\mathfrak P}')\, .
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

It suffices to show that for all ${\mathfrak p}'\in {\mathfrak P}'$ and $\lambda\ge 2$ and ${\mathfrak p}\in {\mathfrak P}({\mathfrak P}')$ with $\lambda {\mathfrak p}' \lesssim \lambda {\mathfrak p}$ we have

$$
\frac{\mu({E}_2(\lambda, {\mathfrak p}))}{\mu({\mathcal{I}}({\mathfrak p}))}
\le \sup_{{\mathfrak p}'' \in {\mathfrak P}(k): \lambda {\mathfrak p}' \lesssim \lambda {\mathfrak p}''}
\frac{\mu({E}_2(\lambda, {\mathfrak p}''))}{\mu({\mathcal{I}}({\mathfrak p}''))}.
$$

Let such ${\mathfrak p}'$, $\lambda$, ${\mathfrak p}$ be given. It suffices to show that ${\mathfrak p}\in {\mathfrak P}(k)$, that is, it satisfies [(1)](../README.md) and [(2)](../README.md).

We show [(1)](../README.md). As ${\mathfrak p}\in {\mathfrak P}({\mathfrak P}')$, there exists ${\mathfrak p}''\in {\mathfrak P}'$ with ${\mathcal{I}}({\mathfrak p}')\subset {\mathcal{I}}({\mathfrak p}'')$. By assumption on ${\mathfrak P}'$, we have ${\mathfrak p}''\in {\mathfrak P}(k)$ and there exists $J\in \mathcal{D}$ with ${\mathcal{I}}({\mathfrak p}'')\subset J$ and

$$
\mu(G\cap J)>2^{-k-1} \mu(J).
$$

Then also ${\mathcal{I}}({\mathfrak p}')\subset J$, which proves [(1)](../README.md) for ${\mathfrak p}$.

We show [(2)](../README.md). Assume to get a contradiction that there exists $J\in \mathcal{D}$ with ${\mathcal{I}}({\mathfrak p})\subset J$ and

$$
\mu(G\cap J)>2^{-k} \mu(J).\qquad\text{(43)}
$$

As $\lambda{\mathfrak p}'\lesssim \lambda{\mathfrak p}$, we have ${\mathcal{I}}({\mathfrak p}')\subset {\mathcal{I}}({\mathfrak p})$, and therefore ${\mathcal{I}}({\mathfrak p}')\subset J$. This contradicts ${\mathfrak p}'\in {\mathfrak P}'\subset {\mathfrak P}(k)$. This proves [(2)](../README.md) for ${\mathfrak p}$.

## Lean

Formalized as [`dens1_le_dens'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dens1_le_dens').

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2847](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2847)
