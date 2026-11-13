---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.orderFourAutomorphismBoundedSeries, MathlibExt.GroupTheory.OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.orderFourAutomorphismBoundedSeries_holds
statement: formalized
---

# Automorphisms of order four with few fixed points

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/automorphisms-of-order-four-with-few-fixed-point/index.html).

## Kourovka Problem 11.126 (automorphisms of order four with few fixed points)

The
statement that there are a natural number $h$ and a function $f : \mathbb{N} \to \mathbb{N}$ such
that, for every natural number $m$, every finite soluble group $G$ and every automorphism
$\varphi$ of $G$ of order $4$ with at most $m$ fixed points, there are normal subgroups $M \le N$
of $G$ with $|G : N| \le f(m)$, $[[N, N], N] \le M$ (so $N/M$ is nilpotent of class at most $2$)
and $\gamma_{h+1}(M) = 1$ (so $M$ is nilpotent of class at most $h$), where $\gamma_1(M) = M$ and
$\gamma_{i+1}(M) = [\gamma_i(M), M]$.

Formalized by `MathlibExt.GroupTheory.OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.orderFourAutomorphismBoundedSeries`, a definition declared in [WantedExt/GroupTheory/OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/automorphisms-of-order-four-with-few-fixed-point/index.html#order-four-automorphism-bounded-series).

## Bounded normal series for soluble groups with an automorphism of order four

There are a
natural number $h$ and a function $f : \mathbb{N} \to \mathbb{N}$ such that, for every natural
number $m$, every finite soluble group $G$ and every automorphism $\varphi$ of $G$ of order $4$
with at most $m$ fixed points, there are normal subgroups $M \le N$ of $G$ with
$|G : N| \le f(m)$, $[[N, N], N] \le M$ (so $N/M$ is nilpotent of class at most $2$) and
$\gamma_{h+1}(M) = 1$ (so $M$ is nilpotent of class at most $h$), where $\gamma_1(M) = M$ and
$\gamma_{i+1}(M) = [\gamma_i(M), M]$. That is, the answer to Kourovka Problem 11.126 is positive.

The Kourovka Archive records the answer "Yes, there do", given by Makarenko and Khukhro.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.126 (P. V. Shumyatskiĭ); resolution: N. Yu. Makarenko and E. I. Khukhro, Algebra and Logic 45 (2006), 326-343, Kourovka Archive, Problem 11.126: "Yes, there do", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.orderFourAutomorphismBoundedSeries_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OrderFourAutomorphismNilpotentSeriesKourovka11Problem126Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/automorphisms-of-order-four-with-few-fixed-point/index.html#order-four-automorphism-bounded-series-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automorphisms of order four with few fixed points](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/automorphisms-of-order-four-with-few-fixed-point/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/automorphisms-of-order-four-with-few-fixed-point)
