---
declaration: lemma
origin: cited
lean: forest_complement
statement: formalized
proof: formalized
---

# forest complement

Let

$$
{\mathfrak P}_2 ={\mathfrak P}\setminus {\mathfrak P}_1\,.
$$

For all $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$ we have

$$
\int_{G \setminus G'} \left|\sum_{{\mathfrak p} \in {\mathfrak P}_2} T_{{\mathfrak p}} f\right| \, \mathrm{d}\mu \le \frac{2^{120a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,.\qquad\text{(26)}
$$

## Depends on

- [antichain operator](../../proof-of-metric-space-carleson-overview/antichain-operator.md)
- [antichain decomposition](../part-02/antichain-decomposition.md)
- [L0 antichain](../part-02/l0-antichain.md)
- [L2 antichain](../part-02/l2-antichain.md)
- [L1 L3 antichain](../part-02/l1-l3-antichain.md)
- [C dens1](../part-02/c-dens1.md)

## Proof

*Proof of forest complement.* If ${\mathfrak p} \not\in {\mathfrak P}_{G \setminus G'}$, then $\mu({\mathcal{I}}({\mathfrak p}) \cap (G \setminus G')) = 0$. By [(20)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md) and [(24)](../../proof-of-metric-space-carleson-overview/README.md), it follows that $\mathbf{1}_{G \setminus G'} T_{{\mathfrak p}}f(x) = 0$ for almost every $x$. We thus have, almost everywhere,

$$
\mathbf{1}_{G\setminus G'} \sum_{{\mathfrak p} \in {\mathfrak P}_2} T_{{\mathfrak p}}f(x) = \mathbf{1}_{G\setminus G'} \sum_{{\mathfrak p} \in {\mathfrak P}_2 \cap {\mathfrak P}_{G \setminus G'}} T_{{\mathfrak p}}f(x)\,.
$$

Let ${\mathfrak L}(k,n)$ denote any of the terms ${\mathfrak L}_i(k,n,j,l) \cap {\mathfrak P}_{G \setminus G'}$ on the right hand side of [(49)](../part-02/antichain-decomposition.md), where the indices $j, l$ may be void. Then ${\mathfrak L}(k,n)$ is an antichain, by Lemmas [L0 antichain](../part-02/l0-antichain.md),[L2 antichain](../part-02/l2-antichain.md), [L1 L3 antichain](../part-02/l1-l3-antichain.md). Further, we have

$$
\operatorname{\operatorname{dens}}_1({\mathfrak L}(k,n)) \le 2^{4a+1 - n}
$$

by [C dens1](../part-02/c-dens1.md), and we have

$$
\operatorname{\operatorname{dens}}_2({\mathfrak L}(k,n)) \le 2^{2a+5} \frac{\mu(F)}{\mu(G)},
$$

since

$$
{\mathfrak L}(k,n) \cap {\mathfrak P}_{F,G} \subset {\mathfrak P}_{G \setminus G'} \cap {\mathfrak P}_{F, G} = \emptyset.
$$

Applying now the triangle inequality according to the decomposition coming from [antichain decomposition](../part-02/antichain-decomposition.md), and then applying [antichain operator](../../proof-of-metric-space-carleson-overview/antichain-operator.md) to each term, we obtain the estimate

$$
\begin{gathered}
\le \sum_{k \ge 0} \sum_{n \ge k} (n + (2n+4) + 2(2n+4) (1+Z(n+1))) \\
\times 2^{117a^3}(q-1)^{-1} (2^{4a+1-n})^{\frac{q-1}{8a^4}} (2^{2a+5} \frac{\mu(F)}{\mu(G)})^{\frac{1}{q} - \frac{1}{2}} \|f\|_2\|\mathbf{1}_{G\setminus G'}\|_2\,.
\end{gathered}
$$

Because $|f| \le \mathbf{1}_F$, we have $\|f\|_2 \le \mu(F)^{1/2}$, and we have $\|\mathbf{1}_{G\setminus G'}\|_2 \le \mu(G)^{1/2}$. Using this and [(3)](../../proof-of-metric-space-carleson-overview/README.md), we bound

$$
\le 2^{118a^3} (q - 1)^{-1} \mu(F)^{\frac{1}{q}} \mu(G)^{\frac{1}{q'}} \sum_{k \ge 0} \sum_{n \ge k} n^2 2^{-n\frac{q-1}{8a^4}}\,.
$$

The last sum equals, by changing the order of summation,

$$
\sum_{n \ge 0} n^2(n+1) 2^{-n\frac{q-1}{8a^4}} \le \frac{2^{2a^3}}{(q-1)^4}\,.
$$

This completes the proof.

## Lean

Formalized as [`forest_complement`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_complement).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2161](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2161)
