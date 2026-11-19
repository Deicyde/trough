---
declaration: lemma
origin: cited
lean: boundary_exception
statement: formalized
proof: formalized
---

# boundary exception

Let $\mathcal{L}({\mathfrak u})$ be as defined in [(18)](../README.md). We have for each ${\mathfrak u}\in {\mathfrak U}_1(k,n,l)$,

$$
\mu(\bigcup_{I\in \mathcal{L}({\mathfrak u})} I)
\le D^{1-\kappa Z(n+1)}
\mu({\mathcal{I}}(\mathfrak{u})).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\mathfrak u}\in {\mathfrak U}_1(k,n,l)$. Let $I \in \mathcal{L}({\mathfrak u})$. Then we have $s(I) = {\mathrm{s}}({\mathfrak u}) - Z(n+1) - 1$ and $I \subset {\mathcal{I}}({\mathfrak u})$ and $B(c(I), 8D^{s(I)}) \not \subset {\mathcal{I}}({\mathfrak u})$. By [(10)](../../proof-of-metric-space-carleson-overview/README.md), the set $I$ is contained in $B(c(I), 4D^{s(I)})$. By the triangle inequality, the set $I$ is contained in

$$
X({\mathfrak u}):=\{x \in {\mathcal{I}}({\mathfrak u}) \, : \, \rho(x, X \setminus {\mathcal{I}}({\mathfrak u})) \leq 12 D^{{\mathrm{s}}({\mathfrak u}) - Z(n+1)-1}\}\,.
$$

By the small boundary property [(11)](../../proof-of-metric-space-carleson-overview/README.md), noting that

$$
12D^{{\mathrm{s}}({\mathfrak u}) - Z(n+1) - 1} = 12D^{s(I)} > D^{-S}\ ,
$$

we have

$$
\mu(X({\mathfrak u})) \le
2\cdot(12 D^{-Z(n+1)-1})^\kappa
\mu({\mathcal{I}}(\mathfrak{u})).
$$

Using $\kappa<1$ and $D \ge 12$, this proves the lemma.

## Lean

Formalized as [`boundary_exception`](https://fpvandoorn.github.io/carleson/docs/find/#doc/boundary_exception).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2518](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2518)
