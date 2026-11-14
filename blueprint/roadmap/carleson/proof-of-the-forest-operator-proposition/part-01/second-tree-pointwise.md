---
declaration: lemma
origin: cited
lean: TileStructure.Forest.second_tree_pointwise
statement: formalized
proof: formalized
---

# second tree pointwise

For all ${\mathfrak u} \in {\mathfrak U}$, all $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have

$$
\Bigg| \sum_{s \in \sigma({\mathfrak u}, x)} \int K_s(x,y) P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))} f(y) \, \mathrm{d}\mu(y) \Bigg| \le T_{\mathcal{N}}^{{\mathcal{Q}}({\mathfrak u})} P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))} f(x')\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $s_1 = \underline{\sigma}({\mathfrak u}, x)$. By definition, there exists a tile ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ with ${\mathrm{s}}({\mathfrak p}) = s_1$ and $x \in E({\mathfrak p})$. Then $x \in {\mathcal{I}}({\mathfrak p}) \cap L$. By [(8)](../../proof-of-metric-space-carleson-overview/README.md) and the definition of $\mathcal{L}({\mathfrak T}({\mathfrak u}))$, it follows that $L \subset {\mathcal{I}}({\mathfrak p})$, in particular $x' \in {\mathcal{I}}({\mathfrak p})$, so $x \in I_{s_1}(x')$. Next, let $s_2 = \overline{\sigma}({\mathfrak u}, x)$ and let ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u})$ with ${\mathrm{s}}({\mathfrak p}') = s_2$ and $x \in E({\mathfrak p}')$. Since ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u})$, we have $4{\mathfrak p}' \lesssim {\mathfrak u}$. Since ${Q}(x) \in {\Omega}({\mathfrak p}')$, it follows that

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \le 5\,.
$$

Applying the doubling property [(8)](../../introduction/README.md) five times, we obtain

$$
d_{B(c({\mathfrak p}), 8D^{s_2})}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \le 5 \cdot 2^{5a}\,.
$$

By the triangle inequality, we have $B(x, D^{s_2}) \subset B(c({\mathfrak p}), 8 D^{s_2})$, so by [(9)](../../introduction/README.md)

$$
d_{B(x, D^{s_2})}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \le 5 \cdot 2^{5a}\,.
$$

Finally, by applying [(10)](../../introduction/README.md) $100a$ times, we obtain

$$
d_{B(x, D^{s_2-1})}({\mathcal{Q}}({\mathfrak u}), {Q}(x)) \le 5 \cdot 2^{-95a} < 1\,.
$$

Consequently, $D^{s_2 - 1} < R_Q({\mathcal{Q}}({\mathfrak u}), x)$. The lemma now follows from the definition of $T_{\mathcal{N}}$.

## Lean

Formalized as [`TileStructure.Forest.second_tree_pointwise`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.second_tree_pointwise).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4606](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4606)
