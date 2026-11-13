---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TwoAutomorphismSquareInnerKourovka14Problem1Wanted.twoAutomorphismCentralizingSylowSquareInner, MathlibExt.GroupTheory.TwoAutomorphismSquareInnerKourovka14Problem1Wanted.twoAutomorphismCentralizingSylowSquareInner_holds
statement: formalized
---

# Squares of 2-automorphisms

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/squares-of-2-automorphisms/index.html).

## Kourovka Problem 14.1

The statement that for every finite group $G$ with no nontrivial
normal subgroup of odd order and every automorphism $\varphi$ of $G$ whose order is a power of
$2$, if $\varphi$ fixes every element of some Sylow $2$-subgroup of $G$, then $\varphi^2$ is
conjugation by some element of $G$, that is, $\varphi^2$ is an inner automorphism.

Formalized by `MathlibExt.GroupTheory.TwoAutomorphismSquareInnerKourovka14Problem1Wanted.twoAutomorphismCentralizingSylowSquareInner`, a definition declared in [WantedExt/GroupTheory/TwoAutomorphismSquareInnerKourovka14Problem1Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoAutomorphismSquareInnerKourovka14Problem1Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/squares-of-2-automorphisms/index.html#two-automorphism-centralizing-sylow-squa).

## Glauberman's theorem on squares of $2$-automorphisms (Kourovka Problem 14.1)

Let $G$ be a
finite group with no nontrivial normal subgroup of odd order, and let $\varphi$ be an automorphism
of $G$ whose order is a power of $2$. If $\varphi$ fixes every element of some Sylow $2$-subgroup
of $G$, then $\varphi^2$ is an inner automorphism of $G$, that is, $\varphi^2$ is conjugation by
some $g \in G$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.1 (R. Zh. Aleev); resolution: G. Glauberman, Math. Z. 107 (1968), 1-20, Kourovka Archive, Problem 14.1 (answer: Yes, it is true).

Stated but not proved: `MathlibExt.GroupTheory.TwoAutomorphismSquareInnerKourovka14Problem1Wanted.twoAutomorphismCentralizingSylowSquareInner_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwoAutomorphismSquareInnerKourovka14Problem1Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoAutomorphismSquareInnerKourovka14Problem1Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/squares-of-2-automorphisms/index.html#two-automorphism-centralizing-sylow-squa-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares of 2-automorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/squares-of-2-automorphisms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/squares-of-2-automorphisms)
