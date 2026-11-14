---
declaration: lemma
origin: cited
lean: grid_existence
statement: formalized
proof: formalized
---

# grid existence

There exists a grid structure $(\mathcal{D}, c,s)$.

## Depends on

- [counting balls](counting-balls.md)
- [boundary measure](boundary-measure.md)

## Proof

*Proof of grid existence.* We first show that $(\tilde{\mathcal{D}},c,s)$ satisfies properties [(7)](../proof-of-metric-space-carleson-overview/README.md), [(8)](../proof-of-metric-space-carleson-overview/README.md), [(10)](../proof-of-metric-space-carleson-overview/README.md) and [(11)](../proof-of-metric-space-carleson-overview/README.md). Property [(10)](../proof-of-metric-space-carleson-overview/README.md) follows from [(12)](basic-grid-structure.md), while [(11)](../proof-of-metric-space-carleson-overview/README.md) follows from [boundary measure](boundary-measure.md).

Let $x\in B(o, D^S)$. We show properties [(7)](../proof-of-metric-space-carleson-overview/README.md) and [(8)](../proof-of-metric-space-carleson-overview/README.md) for $(\tilde{\mathcal{D}},c,s)$ and $x$.

We first show [(7)](../proof-of-metric-space-carleson-overview/README.md) for $(\tilde{\mathcal{D}},c,s)$ by contradiction. Then there is an $I$ violating the conclusion of [(7)](../proof-of-metric-space-carleson-overview/README.md). Pick such $I=I_3(y,l)$ such that $l$ is minimal. By assumption, we have $-S\le k\lt l$; in particular $-S\lt l$. By definition, $I_3(y, l)$ is contained in $I_1(y, l)\cup I_2(y, l)$, which is contained in the union of $I_3(y',l-1)$ with $y'\in Y_{l-1}$. By minimality of $l$, each such $I_3(y',l-1)$ is contained in the union of all $I_3(z,k)$ with $z\in Y_k$. This proves [(7)](../proof-of-metric-space-carleson-overview/README.md).

We now show [(8)](../proof-of-metric-space-carleson-overview/README.md) for $(\tilde{\mathcal{D}},c,s)$. Assume to get a contradiction that there are non-disjoint $I, J\in \tilde{\mathcal{D}}$ with $s(I)\le s(J)$ and $I \not \subset J$. We may assume the existence of such $I$ and $J$ with minimal $s(J)-s(I)$. Let $k=s(I)$. Assume first $s(J)=k$. Let $I=I_3(y_1,k)$ and $J=I_3(y_2,k)$ with $y_1,y_2\in Y_k$. If $y_1=y_2$, then $I=J$, a contradiction to $I\not \subset J$. If $y_1\neq y_2$, then $I\cap J=\emptyset$ by [(10)](basic-grid-structure.md), a contradiction to the non-disjointedness of $I,J$. Assume now $s(J)>k$. Choose $y\in I\cap J$. By property [(7)](../proof-of-metric-space-carleson-overview/README.md), there is $K\in \tilde{\mathcal{D}}$ with $s(K)=s(J)-1$ and $y\in K$. By construction of $J$, and pairwise disjointedness of all $I_3(w,s(J)-1)$ that we have already seen, we have $K\subset J$. By minimality of $s(J)$, we have $I\subset K$. This proves $I\subset J$ and thus [(8)](../proof-of-metric-space-carleson-overview/README.md).

Now note that properties [(8)](../proof-of-metric-space-carleson-overview/README.md), [(10)](../proof-of-metric-space-carleson-overview/README.md) and [(11)](../proof-of-metric-space-carleson-overview/README.md) immediately carry over to $(\mathcal{D},c, s)$ by restriction. [(9)](../proof-of-metric-space-carleson-overview/README.md) is true for $(\mathcal{D}, c, s)$ by definition, and [(7)](../proof-of-metric-space-carleson-overview/README.md) follows from [(7)](../proof-of-metric-space-carleson-overview/README.md) and [(8)](../proof-of-metric-space-carleson-overview/README.md) for $(\tilde{\mathcal{D}}, c, s)$.

## Lean

Formalized as [`grid_existence`](https://fpvandoorn.github.io/carleson/docs/find/#doc/grid_existence).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1239](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1239)
