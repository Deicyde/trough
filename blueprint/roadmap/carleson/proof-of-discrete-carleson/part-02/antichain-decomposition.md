---
declaration: lemma
origin: cited
lean: antichain_decomposition
statement: formalized
proof: formalized
---

# antichain decomposition

We have that

$$
\begin{aligned}
&\quad {\mathfrak P}_2 \cap {\mathfrak P}_{G \setminus G'}\qquad\text{(49)}\\
&= \bigcup_{k \ge 0} \bigcup_{n \ge k} {\mathfrak L}_0(k,n) \cap {\mathfrak P}_{G \setminus G'} \\
&\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} {\mathfrak L}_2(k,n,j) \cap {\mathfrak P}_{G \setminus G'}\\
&\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} {\mathfrak L}_1(k,n,j,l) \cap {\mathfrak P}_{G \setminus G'}\\
&\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} {\mathfrak L}_3(k,n,j,l)\cap {\mathfrak P}_{G \setminus G'}\,.
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\mathfrak p} \in {\mathfrak P}_2 \cap {\mathfrak P}_{G \setminus G'}$. Clearly, for every cube $J = {\mathcal{I}}({\mathfrak p})$ with ${\mathfrak p} \in {\mathfrak P}_{G \setminus G'}$ there exists some $k \ge 0$ such that [(1)](../README.md) holds, and for no cube $J \in \mathcal{D}$ and no $k < 0$ does [(2)](../README.md) hold. Thus ${\mathfrak p} \in {\mathfrak P}(k)$ for some $k \ge 0$.

Next, since $E_2(\lambda, {\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}')\cap G$ for every $\lambda \ge 2$ and every tile ${\mathfrak p}' \in {\mathfrak P}(k)$ with $\lambda{\mathfrak p} \lesssim \lambda {\mathfrak p}'$, it follows from [(2)](../README.md) that $\mu(E_2(\lambda, {\mathfrak p}')) \le 2^{-k} \mu({\mathcal{I}}({\mathfrak p}'))$ for every such ${\mathfrak p}'$, so $\operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}\}) \le 2^{-k}$. Combining this with $a \ge 0$, it follows from [(7)](../README.md) that there exists $n\ge k$ with ${\mathfrak p} \in {\mathfrak C}(k,n)$.

Since ${\mathfrak p} \in {\mathfrak P}_{G \setminus G'}$, we have in particular ${\mathcal{I}}({\mathfrak p}) \not \subset A(2n + 6, k, n)$, so there exist at most $1 + (4n + 12)2^n < 2^{2n+4}$ tiles $\mathfrak{m} \in \mathfrak{M}(k,n)$ with ${\mathfrak p} \le \mathfrak{m}$. It follows that ${\mathfrak p} \in {\mathfrak L}_0(k,n)$ or ${\mathfrak p} \in {\mathfrak C}_1(k,n,j)$ for some $1 \le j \le 2n + 3$. In the former case we are done, in the latter case the equality to be shown follows from the definitions of the collections ${\mathfrak C}_i$ and ${\mathfrak L}_i$.

## Lean

Formalized as [`antichain_decomposition`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_decomposition).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3251](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3251)
