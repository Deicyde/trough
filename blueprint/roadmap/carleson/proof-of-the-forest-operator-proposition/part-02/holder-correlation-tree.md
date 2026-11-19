---
declaration: lemma
origin: cited
lean: TileStructure.Forest.holder_correlation_tree
statement: formalized
proof: formalized
---

# Holder correlation tree

We have for all $J \in \mathcal{J}'$ that

$$
\|h_J\|_{C^{\tau}(B(c(J), 16D^{s(J)}))} \le 2^{485a^3} \prod_{j = 1,2} (\inf_{B(c(J), \frac{1}{8}D^{s(J)})} |T_{{\mathfrak T}({\mathfrak u}_j)}^* g_j| + \inf_J M_{\mathcal{B}, 1} |g_j|)\,.\qquad\text{(42)}
$$

## Depends on

- [global tree control 2](global-tree-control-2.md)

## Proof

*Proof of Holder correlation tree.* Let $P$ be the product on the right hand side of (42), and $h_J$ be as defined in [(41)](README.md). By [(37)](lipschitz-partition-unity.md) and [adjoint tile support](../part-01/adjoint-tile-support.md), the function $h_J$ is supported in $B'(J) \cap {\mathcal{I}}({\mathfrak u}_1)$. By [(37)](lipschitz-partition-unity.md), [global tree control 1](global-tree-control-1.md) and [global tree control 2](global-tree-control-2.md), we have for all $y \in B'(J)$:

$$
|h_J(y)| \le 2^{257a^3+4a+3} P\,.
$$

We have by the triangle inequality

$$
\begin{aligned}
&|h_J(y) - h_J(y')|\\
&\le |\chi_J(y) - \chi_J(y')| |T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1(y)| |T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2(y)|\qquad\text{(43)}\\
& + |\chi_J(y')| |e({\mathcal{Q}}({\mathfrak u}_1)(y)) T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1(y) - e({\mathcal{Q}}({\mathfrak u}_1)(y')) T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1(y')| |T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2(y)|\qquad\text{(44)}\\
& + |\chi_J(y')| |T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1(y')| |e({\mathcal{Q}}({\mathfrak u}_2)(y)) T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2(y) - e({\mathcal{Q}}({\mathfrak u}_2)(y')) T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2(y')|\,.\qquad\text{(45)}\end{aligned}
$$

As $h_J$ is supported in ${\mathcal{I}}({\mathfrak u}_1)$, we can assume without loss of generality that $y' \in {\mathcal{I}}({\mathfrak u}_1)$. If $y \notin {\mathcal{I}}({\mathfrak u}_1)$, then (43) vanishes. If $y \in {\mathcal{I}}({\mathfrak u}_1)$ then we have by [(38)](lipschitz-partition-unity.md), [global tree control 1](global-tree-control-1.md) and [global tree control 2](global-tree-control-2.md)

$$
\eqref{eq-h-Lip-1} \le 2^{484a^3+4a+3} \frac{\rho(y,y')}{D^{s(J)}} P\,,
$$

where $P$ denotes the product on the right hand side of (42).

By [(37)](lipschitz-partition-unity.md), [global tree control 1](global-tree-control-1.md) and [global tree control 2](global-tree-control-2.md), we have

$$
\eqref{eq-h-Lip-2} \le 2^{257a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} P\,.
$$

By [(37)](lipschitz-partition-unity.md), and twice [global tree control 1](global-tree-control-1.md), we have

$$
\eqref{eq-h-Lip-3} \le 2^{256a^3+8a+5} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} P\,.
$$

Using that $\rho(y,y') \le 32D^{s(J)}$ and $a \ge 4$, the lemma follows.

## Lean

Formalized as [`TileStructure.Forest.holder_correlation_tree`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.holder_correlation_tree).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5547](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5547)
