---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.HasMaxCondition, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.HasMinCondition, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.IsMinimax, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.SameFiniteImages, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.IsResiduallyFinite, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.minimaxDeterminedByFiniteImages, MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.minimaxDeterminedByFiniteImages_holds
statement: formalized
---

# Finite images of minimax groups

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html).

## Maximal condition on subgroups

A group $G$ satisfies the maximal condition on subgroups
when every subgroup of $G$ is finitely generated.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.HasMaxCondition`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#has-max-condition).

## Minimal condition on subgroups

A group $G$ satisfies the minimal condition on subgroups
when the order on subgroups of $G$ by inclusion is well-founded: every nonempty set of subgroups
of $G$ has a minimal element, equivalently there is no infinite strictly descending chain of
subgroups of $G$.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.HasMinCondition`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#has-min-condition).

## Minimax groups

A group $G$ is a minimax group when it has a finite subnormal series
$1 = H_0 \le H_1 \le \dots \le H_n = G$, with each $H_i$ normal in $H_{i+1}$, such that every
factor $H_{i+1}/H_i$ satisfies the maximal condition on subgroups or the minimal condition on
subgroups.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.IsMinimax`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#is-minimax).

## Groups with the same finite images

Two groups $G$ and $H$ have the same finite images
when, for every finite group $Q$, there is a surjective homomorphism $G \to Q$ exactly when there
is a surjective homomorphism $H \to Q$.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.SameFiniteImages`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#same-finite-images).

## Residually finite groups

A group $G$ is residually finite when for every element
$g \ne 1$ of $G$ there is a normal subgroup $N$ of finite index in $G$ with $g \notin N$.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.IsResiduallyFinite`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#is-residually-finite).

## Minimax groups and finite images (Kourovka 12.90)

The statement that for all groups $G$
and $H$, if $G$ is a finitely generated soluble minimax group and $H$ is a finitely generated
residually finite group with the same finite images as $G$ (a finite group is a homomorphic image
of $G$ exactly when it is a homomorphic image of $H$), then $H$ is a minimax group.

Formalized by `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.minimaxDeterminedByFiniteImages`, a definition declared in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#minimax-determined-by-finite-images).

## Finite images determine minimaxity (Mann–Segal)

Let $G$ be a finitely generated
soluble minimax group and let $H$ be a finitely generated residually finite group with the same
finite images as $G$: a finite group is a homomorphic image of $G$ exactly when it is a
homomorphic image of $H$. Then $H$ is a minimax group.

This answers Kourovka Problem 12.90 (J. S. Wilson) affirmatively: the Kourovka Archive answers
"Yes, it must" (A. Mann and D. Segal, 1990; see also A. V. Tushev, 1994).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.90 (J. S. Wilson); resolution: A. Mann and D. Segal, Proc. London Math. Soc. (3) 61 (1990), 529-545; A. V. Tushev, Math. Notes 56 (1994), no. 5, 1190-1192, Kourovka Archive, Problem 12.90: Yes, it must.

Stated but not proved: `MathlibExt.GroupTheory.MinimaxFiniteImagesKourovka12Problem90Wanted.minimaxDeterminedByFiniteImages_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MinimaxFiniteImagesKourovka12Problem90Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html#minimax-determined-by-finite-images-hold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite images of minimax groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/finite-images-of-minimax-groups)
