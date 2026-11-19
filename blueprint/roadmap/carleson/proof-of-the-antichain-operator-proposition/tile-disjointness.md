---
declaration: lemma
origin: cited
lean: tile_disjointness
statement: formalized
proof: formalized
---

# tile disjointness

Let ${\mathfrak p},{\mathfrak p}'\in \mathfrak{A}$. If there exists an $x\in X$ with $x\in E({\mathfrak p})\cap E({\mathfrak p}')$, then ${\mathfrak p}= {\mathfrak p}'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\mathfrak p},{\mathfrak p}'$ and $x$ be given. Assume without loss of generality that ${\mathrm{s}}({\mathfrak p})\le {\mathrm{s}}({\mathfrak p}')$. As we have $x\in E({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p})$ and $x\in E({\mathfrak p}')\subset {\mathcal{I}}({\mathfrak p}')$ by Definition [(19)](../proof-of-metric-space-carleson-overview/discrete-carleson.md), we conclude for $i=1,2$ that ${Q}(x)\in{\Omega}({\mathfrak p})$ and ${Q}(x)\in{\Omega}({\mathfrak p}')$. By [(14)](../proof-of-metric-space-carleson-overview/README.md) we have ${\Omega}({\mathfrak p}')\subset {\Omega}({\mathfrak p})$. By Definition [(22)](../proof-of-metric-space-carleson-overview/README.md), we conclude ${\mathfrak p}\le {\mathfrak p}'$. As $\mathfrak{A}$ is an antichain, we conclude ${\mathfrak p}={\mathfrak p}'$. This proves the lemma.

## Lean

Formalized as [`tile_disjointness`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tile_disjointness).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3430](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3430)
