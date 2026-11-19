---
declaration: lemma
origin: cited
lean: iUnion_L0', pairwiseDisjoint_L0', antichain_L0'
statement: formalized
proof: formalized
---

# L0 antichain

We have that

$$
{\mathfrak L}_0(k,n) = \dot{\bigcup_{0 \le l < n}} {\mathfrak L}_0(k,n,l)\,,
$$

where each ${\mathfrak L}_0(k,n,l)$ is an antichain.

## Depends on

- [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

It suffices to show that ${\mathfrak L}_0(k,n)$ contains no chain of length $n + 1$. Suppose that we had such a chain ${\mathfrak p}_0 \le {\mathfrak p}_1 \le \dotsb \le {\mathfrak p}_{n}$ with ${\mathfrak p}_i \ne {\mathfrak p}_{i+1}$ for $i =0, \dotsc, n-1$. By [(7)](../README.md), we have that $\operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}_n\}) > 2^{-n}$. Thus, by [(6)](../README.md), there exists ${\mathfrak p}' \in {\mathfrak P}(k)$ and $\lambda \ge 2$ with $\lambda {\mathfrak p}_n \le \lambda {\mathfrak p}'$ and

$$
\frac{\mu(E_2(\lambda, {\mathfrak p}'))}{\mu({\mathcal{I}}({\mathfrak p}'))} > \lambda^{a} 2^{4a} 2^{-n}\,.\qquad\text{(50)}
$$

Let $\mathfrak{O}$ be the set of all ${\mathfrak p}'' \in {\mathfrak P}(k)$ such that we have ${\mathcal{I}}({\mathfrak p}'') = {\mathcal{I}}({\mathfrak p}')$ and $B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), \lambda) \cap \Omega({\mathfrak p}'') \neq \emptyset$. We now show that

$$
|\mathfrak{O}| \le 2^{4a}\lambda^a\,.\qquad\text{(51)}
$$

The balls $B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}''), 0.2)$, ${\mathfrak p}'' \in \mathfrak{O}$ are disjoint by [(15)](../../proof-of-metric-space-carleson-overview/README.md), and by the triangle inequality contained in $B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), \lambda+1.2)$. By assumption [(11)](../../introduction/README.md) on $\Theta$, this ball can be covered with

$$
2^{a\lceil \log_2(\lambda+1.2) + \log_2(5)\rceil} \le 2^{a(\log_2(\lambda) + 4)} = 2^{4a}\lambda^a
$$

many $d_{{\mathfrak p}'}$-balls of radius $0.2$. Here we have used that for $\lambda \ge 2$

$$
\lceil \log_2(\lambda + 1.2)  + \log_2(5) \rceil \le 1+ \log_2(1.6  \lambda) + \log_2(5) = 4 + \log_2(\lambda)\,.
$$

By the triangle inequality, each such ball contains at most one ${\mathcal{Q}}({\mathfrak p}'')$, and each ${\mathcal{Q}}({\mathfrak p}'')$ is contained in one of the balls. Thus we get (51).

By [(24)](../../proof-of-metric-space-carleson-overview/README.md) and [(25)](../../proof-of-metric-space-carleson-overview/README.md) we have $E_2(\lambda, {\mathfrak p}') \subset \bigcup_{{\mathfrak p}'' \in \mathfrak{O}} E_1({\mathfrak p}'')$, thus

$$
2^{4a}\lambda^a 2^{-n} < \sum_{{\mathfrak p}'' \in \mathfrak{O}} \frac{\mu(E_1({\mathfrak p}''))}{\mu({\mathcal{I}}({\mathfrak p}''))}\,.
$$

Hence there exists a tile ${\mathfrak p}'' \in \mathfrak{O}$ with

$$
\mu(E_1({\mathfrak p}'')) \ge 2^{-n} \mu({\mathcal{I}}({\mathfrak p}'))\,.
$$

By the definition [(5)](../README.md) of $\mathfrak{M}(k,n)$, there exists a tile $\mathfrak{m} \in \mathfrak{M}(k,n)$ with ${\mathfrak p}' \leq \mathfrak{m}$. From (50), the inclusion $E_2(\lambda, {\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}')$ and $a\ge 1$ we obtain

$$
2^n \geq 2^{4a} \lambda^{a} \geq \lambda\,.
$$

From the triangle inequality, [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and $a \ge 1$, we now obtain for all ${\vartheta} \in B_{\mathfrak{m}}({\mathcal{Q}}(\mathfrak{m}), 1)$ that

$$
\begin{aligned}
&\quad d_{{\mathfrak p}_0}({\mathcal{Q}}({\mathfrak p}_0), {\vartheta})\\
&\leq d_{{\mathfrak p}_0}({\mathcal{Q}}({\mathfrak p}_0), {\mathcal{Q}}({\mathfrak p}_{n})) + d_{{\mathfrak p}_0}({\mathcal{Q}}({\mathfrak p}_{n}), {\mathcal{Q}}({\mathfrak p}')) + d_{{\mathfrak p}_0}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak p}''))\\
&\quad+ d_{{\mathfrak p}_0}({\mathcal{Q}}({\mathfrak p}''), {\mathcal{Q}}(\mathfrak{m})) +
d_{{\mathfrak p}_0}({\mathcal{Q}}(\mathfrak{m}), {\vartheta})\\
&\leq 1 + 2^{-95an} (d_{{\mathfrak p}_{n}}({\mathcal{Q}}({\mathfrak p}_n), {\mathcal{Q}}({\mathfrak p}')) + d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak p}''))\\
&\quad+ d_{{\mathfrak p}''}({\mathcal{Q}}({\mathfrak p}''), {\mathcal{Q}}(\mathfrak{m})) +
d_{\mathfrak{m}}({\mathcal{Q}}(\mathfrak{m}), {\vartheta}))\\
&\leq 1 + 2^{-95an}(\lambda + (\lambda + 1) + 1 + 1) \leq 100\,.
\end{aligned}
$$

Thus, by [(22)](../../proof-of-metric-space-carleson-overview/README.md), $100{\mathfrak p}_0 \lesssim \mathfrak{m}$, a contradiction to ${\mathfrak p}_0 \notin {\mathfrak C}(k,n)$.

## Lean

Formalized as [`iUnion_L0'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/iUnion_L0'), [`pairwiseDisjoint_L0'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/pairwiseDisjoint_L0'), [`antichain_L0'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_L0').

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3275](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3275)
