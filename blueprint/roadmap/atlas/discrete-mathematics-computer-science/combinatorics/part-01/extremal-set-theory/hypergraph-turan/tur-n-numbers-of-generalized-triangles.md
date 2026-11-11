---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.ContainsGeneralizedTriangle, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleTuranNumber, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.IsSteinerSystem, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.blowUp, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.maxBlowUpSize, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleFiveTuranNumber, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleSixTuranNumber, MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleFiveTuranNumber_holds
statement: formalized
---

# Turán numbers of generalized triangles

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html).

## Generalized triangle $\mathcal{T}_r$

Let $r, n \in \mathbb{N}$ and let $G$ be a family of
subsets of $\{0, \dots, n-1\}$, typically an $r$-uniform hypergraph. Then $G$ contains a
generalized triangle $\mathcal{T}_r$ (the book $B_{r,2}$) when there are edges
$D_1, D_2, D_3 \in G$, not necessarily distinct, with $|D_1 \cap D_2| + 1 = r$,
$D_1 \triangle D_2 \subseteq D_3$ and $D_3 \cap D_1 \cap D_2 = \emptyset$.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.ContainsGeneralizedTriangle`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#contains-generalized-triangle).

## Turán number of the generalized triangle

For $r, n \in \mathbb{N}$, the Turán number
$\mathrm{ex}(n, \mathcal{T}_r)$ is the largest number of edges of an $r$-uniform hypergraph on the
vertex set $\{0, \dots, n-1\}$ that contains no generalized triangle $\mathcal{T}_r$.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleTuranNumber`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#generalized-triangle-turan-number).

## Steiner system $S(t, r, m)$

Let $t, r, m \in \mathbb{N}$ and let $D$ be a family of
subsets of $\{0, \dots, m-1\}$. Then $D$ is a Steiner system $S(t, r, m)$ when every block of $D$
has exactly $r$ elements and every $t$-element subset of $\{0, \dots, m-1\}$ is contained in
exactly one block of $D$.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.IsSteinerSystem`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#is-steiner-system).

## Blow-up of a hypergraph along a map

Let $D$ be a family of subsets of
$\{0, \dots, m-1\}$, let $r \in \mathbb{N}$ and let $\varphi : \{0, \dots, n-1\} \to
\{0, \dots, m-1\}$. The $r$-uniform blow-up of $D$ along $\varphi$ is the family of $r$-element
subsets $e \subseteq \{0, \dots, n-1\}$ such that $\varphi$ is injective on $e$ and the image
$\varphi(e)$ is a block of $D$.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.blowUp`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#blow-up).

## Largest blow-up of a hypergraph

Let $D$ be a family of subsets of $\{0, \dots, m-1\}$
and let $r, n \in \mathbb{N}$. The largest blow-up size of $D$ is the maximum, over all maps
$\varphi : \{0, \dots, n-1\} \to \{0, \dots, m-1\}$, of the number of edges of the $r$-uniform
blow-up of $D$ along $\varphi$; it is $0$ when there is no such map.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.maxBlowUpSize`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#max-blow-up-size).

## Turán number of $\mathcal{T}_5$ via blow-ups of $S(4, 5, 11)$

There exist a Steiner system
$D$ of type $S(4, 5, 11)$ on $\{0, \dots, 10\}$ and an $n_0 \in \mathbb{N}$ such that for every
$n \ge n_0$, the Turán number $\mathrm{ex}(n, \mathcal{T}_5)$ of the generalized triangle
$\mathcal{T}_5$ (the book $B_{5,2}$) equals the largest number of edges of a $5$-uniform blow-up
of $D$ along a map $\{0, \dots, n-1\} \to \{0, \dots, 10\}$.

## Sources

- AimPL Problem 2.1 (Hypergraph Turán problem), case `k = 5`.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleFiveTuranNumber`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#generalized-triangle-five-turan-number).

## Turán number of $\mathcal{T}_6$ via blow-ups of $S(5, 6, 12)$

There exist a Steiner system
$D$ of type $S(5, 6, 12)$ on $\{0, \dots, 11\}$ and an $n_0 \in \mathbb{N}$ such that for every
$n \ge n_0$, the Turán number $\mathrm{ex}(n, \mathcal{T}_6)$ of the generalized triangle
$\mathcal{T}_6$ (the book $B_{6,2}$) equals the largest number of edges of a $6$-uniform blow-up
of $D$ along a map $\{0, \dots, n-1\} \to \{0, \dots, 11\}$.

## Sources

- AimPL Problem 2.1 (Hypergraph Turán problem), case `k = 6`.

Formalized by `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleSixTuranNumber`, a definition declared in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#generalized-triangle-six-turan-number).

## Norin–Yepremyan theorem for $\mathcal{T}_5$

There exist a Steiner system $D$ of type
$S(4, 5, 11)$ on $\{0, \dots, 10\}$ and an $n_0 \in \mathbb{N}$ such that for every $n \ge n_0$,
the Turán number $\mathrm{ex}(n, \mathcal{T}_5)$ of the generalized triangle $\mathcal{T}_5$ (the
book $B_{5,2}$) equals the largest number of edges of a $5$-uniform blow-up of $D$ along a map
$\{0, \dots, n-1\} \to \{0, \dots, 10\}$.

Norin and Yepremyan proved more: for all large $n$, every extremal $\mathcal{T}_5$-free
$5$-uniform hypergraph on $n$ vertices is a blow-up of $S(4, 5, 11)$ (the Frankl–Füredi
construction).

## Sources

- AimPL: Hypergraph Turán problem, Problem 2.1 (Frankl-Füredi), http://aimpl.org/hypergraphturan/2/; resolution: S. Norin and L. Yepremyan, Turán number of generalized triangles, J. Combin. Theory Ser. A 146 (2017), 312-343, arXiv:1501.01913, Theorem 1.1: there is n0 such that for all n ≥ n0, ex(n, 𝒯_r) = ex(n, Σ_r) for r = 5, 6, and the extremal graphs are blow-ups of the unique (11, 5, 4) and (12, 6, 5) Steiner systems; the blow-ups are the Frankl-Füredi lower-bound constructions named in the AimPL problem, https://doi.org/10.1016/j.jcta.2016.09.003.

Stated but not proved: `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleFiveTuranNumber_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#generalized-triangle-five-turan-number-h).

## Norin–Yepremyan theorem for $\mathcal{T}_6$

There exist a Steiner system $D$ of type
$S(5, 6, 12)$ on $\{0, \dots, 11\}$ and an $n_0 \in \mathbb{N}$ such that for every $n \ge n_0$,
the Turán number $\mathrm{ex}(n, \mathcal{T}_6)$ of the generalized triangle $\mathcal{T}_6$ (the
book $B_{6,2}$) equals the largest number of edges of a $6$-uniform blow-up of $D$ along a map
$\{0, \dots, n-1\} \to \{0, \dots, 11\}$.

Norin and Yepremyan proved more: for all large $n$, every extremal $\mathcal{T}_6$-free
$6$-uniform hypergraph on $n$ vertices is a blow-up of $S(5, 6, 12)$ (the Frankl–Füredi
construction).

## Sources

- AimPL: Hypergraph Turán problem, Problem 2.1 (Frankl-Füredi), http://aimpl.org/hypergraphturan/2/; resolution: S. Norin and L. Yepremyan, Turán number of generalized triangles, J. Combin. Theory Ser. A 146 (2017), 312-343, arXiv:1501.01913, Theorem 1.1: there is n0 such that for all n ≥ n0, ex(n, 𝒯_r) = ex(n, Σ_r) for r = 5, 6, and the extremal graphs are blow-ups of the unique (11, 5, 4) and (12, 6, 5) Steiner systems; the blow-ups are the Frankl-Füredi lower-bound constructions named in the AimPL problem, https://doi.org/10.1016/j.jcta.2016.09.003.

Stated but not proved: `MathlibExt.Combinatorics.GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.generalizedTriangleSixTuranNumber_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GeneralizedTriangleTuranNumberAIMCombinatoricsProblem151Wanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html#generalized-triangle-six-turan-number-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán numbers of generalized triangles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/tur-n-numbers-of-generalized-triangles)
