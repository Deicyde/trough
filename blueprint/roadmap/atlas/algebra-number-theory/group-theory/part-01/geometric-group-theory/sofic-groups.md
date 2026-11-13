---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.Kourovka21Problem86Wanted.soficHammingDist, MathlibExt.GroupTheory.Kourovka21Problem86Wanted.IsSofic, MathlibExt.GroupTheory.Kourovka21Problem86Wanted.conjecture, MathlibExt.GroupTheory.Kourovka21Problem86Wanted.conjecture_refuted
statement: formalized
---

# Sofic groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html).

## Hamming distance for sofic approximations

For a natural number $n$ and permutations
$\sigma$, $\tau$ of $\{0, \dots, n-1\}$, the normalized Hamming distance $d(\sigma, \tau)$ is the
number of points $i < n$ with $\sigma(i) \ne \tau(i)$, divided by $n$, as a real number; for
$n = 0$ it is $0$. It is used in the definition of sofic groups [KOU-21.86].

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem86Wanted.soficHammingDist`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html#sofic-hamming-dist).

## Sofic groups

Let $d$ denote the normalized Hamming distance on permutations. A group
$G$ is sofic if for every finite subset $F \subseteq G$ with $1 \in F$ and every real
$\varepsilon > 0$ there are an integer $n \ge 1$ and a map $\varphi$ from $F$ to the permutations
of $\{0, \dots, n-1\}$ such that $\varphi(1)$ is the identity,
$d(\varphi(gh), \varphi(g)\varphi(h)) < \varepsilon$ for all $g, h \in F$ with $gh \in F$, and
$\varphi(g)$ has no fixed point for every $g \in F$ with $g \ne 1$ [KOU-21.86].

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem86Wanted.IsSofic`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html#is-sofic).

## Soficity problem (Kourovka Notebook Problem 21.86)

The statement that every group $G$ is
sofic [KOU-21.86].

Formalized by `MathlibExt.GroupTheory.Kourovka21Problem86Wanted.conjecture`, a definition declared in [WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html#conjecture).

## Not every group is sofic

The soficity problem (Kourovka Notebook Problem 21.86) has a
negative answer: there exists a group that is not sofic.

OpenAI announced the first example, the unit group of the binary Leavitt algebra. G. Kun and
A. Thom (Theorems A and E) prove that $(\mathbb{Z}/2\mathbb{Z}) \wr_{G/\Gamma} G$ and
$G *_\Gamma G$ are not sofic for explicit residually finite Kazhdan pairs $\Gamma < G$. The
Kourovka Notebook (arXiv:1401.0300v49) marks Problem 21.86 solved.

## Sources

- G. Kun and A. Thom, Nonsofic wreath products of residually finite groups, arXiv:2608.06222 (2026), https://arxiv.org/abs/2608.06222; OpenAI, A counterexample to the soficity conjecture, in Ten advances in mathematics and theoretical computer science, Chapter 3, 2026, https://cdn.openai.com/pdf/ten-proofs-oai.pdf; E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (20 October 2026), Problem 21.86, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.Kourovka21Problem86Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/Kourovka21Problem86Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sofic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/sofic-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/sofic-groups)
