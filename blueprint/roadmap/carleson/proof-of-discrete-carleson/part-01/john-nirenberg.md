---
declaration: lemma
origin: cited
lean: john_nirenberg
statement: formalized
proof: formalized
---

# John Nirenberg

For all integers $k,n,\lambda\ge 0$, we have

$$
\mu(A(\lambda,k,n)) \le 2^{k+1-\lambda}\mu(G)\,.\qquad\text{(29)}
$$

## Depends on

- [dense cover](dense-cover.md)
- [pairwise disjoint](pairwise-disjoint.md)
- [dyadic union](dyadic-union.md)

## Proof

Fix $k,n$ as in the lemma and suppress notation to write $A(\lambda)$ for $A(\lambda,k,n)$. We prove the lemma by induction on $\lambda$. For $\lambda=0$, we use that $A(\lambda)$ by definition of $\mathfrak{M}(k,n)$ is contained in the union of elements in $\mathcal{C}(G,k)$. [dense cover](dense-cover.md) then completes the base of the induction.

Now assume that the statement of John Nirenberg is proven for some integer $\lambda\ge 0$. The set $A(\lambda+1)$ is contained in the set $A(\lambda)$. Let $\mathcal{M}$ be the set of dyadic cubes which are a subset of $A(\lambda)$. By [dyadic union](dyadic-union.md), the union of $\mathcal{M}$ is $A(\lambda)$. Let $\mathcal{M}^*$ be the set of maximal dyadic cubes in $\mathcal{M}$.

Let $x\in A(\lambda+1)$ and $L\in \mathcal{M}^*$ such that $x\in L$. Then by the dyadic property [(8)](../../proof-of-metric-space-carleson-overview/README.md)

$$
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n)} \mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(x) =
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):{\mathcal{I}}({\mathfrak p}) \subset L} \mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(x) +
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):L \subsetneq {\mathcal{I}}({\mathfrak p})} \mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(x)\,.\qquad\text{(30)}
$$

We now show

$$
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):{\mathcal{I}}({\mathfrak p}) \subset L} \mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(x)\ge 2^{n+1}\,.\qquad\text{(31)}
$$

The left-hand side of (30) is strictly greater than $(\lambda+1)2^{n+1}$. If $L$ is the top cube the second sum $Q_2$ on the right-hand side of (30) is zero and (31) follows immediately. Otherwise consider the inclusion-minimal cube $\hat{L}$ with $L\subsetneq\hat{L}$; all tiles ${\mathfrak p}$ over which $Q_2$ is summed over satisfy $\hat{L}\subset{\mathfrak p}$, so $Q_2$ is constant for all $x\in\hat{L}$. By maximality of $L$, $Q_2$ is at most $\lambda 2^{n+1}$ somewhere on $\hat{L}$, thus on all of $\hat{L}$ and consequently also at $x$. Rearranging the inequality yields (31).

By [pairwise disjoint](pairwise-disjoint.md), we have

$$
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):{\mathcal{I}}({\mathfrak p}) \subset L} \mu({E_1}({\mathfrak p})) \leq \mu(L)\, .
$$

Multiplying by $2^n$ and applying [(4)](../README.md), we obtain

$$
\sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):{\mathcal{I}}({\mathfrak p}) \subset L} \mu({\mathcal{I}}({\mathfrak p})) \leq 2^n \mu(L)\, .\qquad\text{(32)}
$$

We then have with (31) and (32)

$$
2^{n+1}\mu(A(\lambda+1)\cap L) =
\int_{A(\lambda+1)\cap L} 2^{n+1} d\mu
$$

$$
\le
\int \sum_{{\mathfrak p} \in {\mathfrak{M}}(k,n):{\mathcal{I}}({\mathfrak p}) \subset L} \mathbf{1}_{{\mathcal{I}}({\mathfrak p})} d\mu
\le 2^n \mu(L)\, .
$$

Hence

$$
2\mu(A(\lambda+1))=2\sum_{L\in \mathcal{M}^*}
\mu(A(\lambda+1)\cap L)\le
\sum_{L\in \mathcal{M}^*}\mu( L)= \mu(A(\lambda))\, .
$$

Using the induction hypothesis, this proves (29) for $\lambda+1$ and completes the proof of the lemma.

## Lean

Formalized as [`john_nirenberg`](https://fpvandoorn.github.io/carleson/docs/find/#doc/john_nirenberg).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2315](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2315)
