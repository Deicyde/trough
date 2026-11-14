---
declaration: lemma
origin: cited
lean: TileStructure.Forest.adjoint_tree_estimate, TileStructure.Forest.indicator_adjoint_tree_estimate
statement: formalized
proof: formalized
---

# adjoint tree estimate

For all bounded $g$ supported on $G$ we have that

$$
\left\| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g\right\|_2 \le 2^{181a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2\,,
$$

$$
\left\| \mathbf{1}_F \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g\right\|_2 \le 2^{282a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2\,.
$$

## Depends on

- [densities tree bound](densities-tree-bound.md)

## Proof

By [densities tree bound](densities-tree-bound.md), we have for all bounded $f$ and $g$ with $|g| \le \mathbf{1}_G$ that

$$
\left| \int_X \overline{\sum_{{\mathfrak p}\in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g} f \,\mathrm{d}\mu \right| = \left| \int_X \overline{g} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f \,\mathrm{d}\mu \right|
$$

$$
\le 2^{181a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2 \|f\|_2\,.\qquad\text{(26)}
$$

Let $f = \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g$. Since $|g| \le \mathbf{1}_G$, $f$ is bounded and has bounded support. In particular $\|f\|_2 < \infty$. Dividing (26) by $\|f\|_2$ completes the proof.

The proof of the second part is similar with $f = \mathbf{1}_F \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g$.

## Lean

Formalized as [`TileStructure.Forest.adjoint_tree_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.adjoint_tree_estimate), [`TileStructure.Forest.indicator_adjoint_tree_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.indicator_adjoint_tree_estimate).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5246](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5246)
