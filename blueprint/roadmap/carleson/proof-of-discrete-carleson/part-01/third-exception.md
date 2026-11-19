---
declaration: lemma
origin: cited
lean: third_exception
statement: formalized
proof: formalized
---

# third exception

We have

$$
\mu(G_3)\le 2^{-4} \mu(G)\, .
$$

## Depends on

- [tree count](tree-count.md)
- [boundary exception](boundary-exception.md)
- [top tiles](top-tiles.md)

## Proof

As each ${\mathfrak p}\in {\mathfrak L}_4(k,n,j)$ is contained in $\cup\mathcal{L}({\mathfrak u})$ for some ${\mathfrak u}\in {\mathfrak U}_1(k,n,l)$, we have

$$
\mu(\bigcup_{{\mathfrak p} \in {\mathfrak L}_4 (k,n,j)}{\mathcal{I}}({\mathfrak p}))
\le \sum_{{\mathfrak u}\in {\mathfrak U}_1(k,n,j)}
\mu(\bigcup_{I \in \mathcal{L} ({\mathfrak u})}I).
$$

Using [boundary exception](boundary-exception.md) and then [tree count](tree-count.md), we estimate this further by

$$
\le \sum_{{\mathfrak u}\in {\mathfrak U}_1(k,n,j)}
D^{1-\kappa Z(n+1)}
\mu({\mathcal{I}}(\mathfrak{u}))
$$

$$
\le 2^{100a^2+9a+1-j} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)}
D^{-\kappa Z(n+1)}
\mu({\mathcal{I}}(\mathfrak{m}))\,.
$$

Using [top tiles](top-tiles.md), we estimate this by

$$
\le
2^{100a^2 + 9a + 1-j} D^{-\kappa Z(n+1)}
2^{n+k+3}\mu(G)\, .
$$

Now we estimate $G_3$ defined in [(24)](../README.md) by

$$
\mu(G_3)\le \sum_{k\ge 0}\, \sum_{n \geq k}\,
\sum_{0\le j\le 2n+3}
\mu(\bigcup_{{\mathfrak p} \in {\mathfrak L}_4 (k,n,j)}
{\mathcal{I}}({\mathfrak p}))
$$

$$
\le \sum_{k\ge 0}\, \sum_{n \geq k}\,
\sum_{0\le j\le 2n+3}
2^{100a^2 + 9a + 3 + n + k -j} D^{-\kappa Z(n+1)}\mu(G)
$$

Summing geometric series, using that $D^{\kappa Z}\ge 8$ by [(1)](../../proof-of-metric-space-carleson-overview/README.md), [(2)](../../proof-of-metric-space-carleson-overview/README.md) and [(3)](../../proof-of-metric-space-carleson-overview/README.md), we estimate this by

$$
\le \sum_{k\ge 0}\, \sum_{n \geq k}\,
2^{100a^2 + 9a + 4 + n + k} D^{-\kappa Z(n+1)}\mu(G)
$$

$$
= \sum_{k\ge 0} 2^{100a^2 + 9a + 4 + 2k} D^{-\kappa Z(k+1)} \sum_{n \geq k}\,
2^{n - k} D^{-\kappa Z(n-k)}\mu(G)
$$

$$
\le \sum_{k\ge 0} 2^{100a^2 + 9a + 5 + 2k} D^{-\kappa Z(k+1)}\mu(G)
$$

$$
\le 2^{100a^2 + 9a + 6} D^{-\kappa Z}\mu(G)
$$

Using $D = 2^{100a^2}$ and $a \ge 4$ and $\kappa Z \ge 2$ by [(1)](../../proof-of-metric-space-carleson-overview/README.md) and [(2)](../../proof-of-metric-space-carleson-overview/README.md) proves the lemma.

## Lean

Formalized as [`third_exception`](https://fpvandoorn.github.io/carleson/docs/find/#doc/third_exception).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2553](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2553)
