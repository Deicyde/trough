---
declaration: lemma
origin: cited
lean: ordConnected_C
statement: formalized
proof: formalized
---

# C convex

For each $k,n$, the collection ${\mathfrak C}(k,n)$ is convex.

## Depends on

- [P convex](p-convex.md)

## Proof

Let ${\mathfrak p} \le {\mathfrak p}' \le {\mathfrak p}''$ with ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}(k,n)$. Then, in particular, ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak P}(k)$, so, by [P convex](p-convex.md), ${\mathfrak p}' \in {\mathfrak P}(k)$. Next, we show that if ${\mathfrak q} \le {\mathfrak q}' \in {\mathfrak P}(k)$ then $\operatorname{\operatorname{dens}}'_k(\{{\mathfrak q}\}) \ge \operatorname{\operatorname{dens}}_k'(\{{\mathfrak q}'\})$. If ${\mathfrak p} \in {\mathfrak P}(k)$ and $\lambda \ge 2$ with $\lambda {\mathfrak q}' \lesssim \lambda {\mathfrak p}$, then it follows from ${\mathfrak q} \le {\mathfrak q}'$, [(39)](wiggle-order-3.md) of [wiggle order 3](wiggle-order-3.md) and transitivity of $\lesssim$ that $\lambda {\mathfrak q} \lesssim \lambda {\mathfrak p}$. Thus the supremum in the definition [(6)](../README.md) of $\operatorname{\operatorname{dens}}_k'(\{{\mathfrak q}\})$ is over a superset of the set the supremum in the definition of $\operatorname{\operatorname{dens}}_k'(\{{\mathfrak q}'\})$ is taken over, which shows $\operatorname{\operatorname{dens}}'_k(\{{\mathfrak q}\}) \ge \operatorname{\operatorname{dens}}_k'(\{{\mathfrak q}'\})$. From ${\mathfrak p}' \le {\mathfrak p}''$, ${\mathfrak p}'' \in {\mathfrak C}(k,n)$ and [(7)](../README.md) it then follows that

$$
2^{4a}2^{-n} < \operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}''\}) \le \operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}'\})\,.
$$

Similarly, it follows from ${\mathfrak p} \le {\mathfrak p}'$, ${\mathfrak p} \in {\mathfrak C}(k,n)$ and [(7)](../README.md) that

$$
\operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}'\}) \le \operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}\}) \le 2^{4a}2^{-n+1}\,.
$$

Thus ${\mathfrak p}' \in {\mathfrak C}(k,n)$.

## Lean

Formalized as [`ordConnected_C`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_C).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2740](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2740)
