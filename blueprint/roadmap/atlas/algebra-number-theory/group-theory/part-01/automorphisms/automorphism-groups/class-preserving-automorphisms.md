---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.classPreservingAutomorphismsInner, MathlibExt.GroupTheory.ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.classPreservingAutomorphismsInner_refuted, MathlibExt.GroupTheory.ScottishBook112Wanted.ScottishBookProblem112Claim, MathlibExt.GroupTheory.ScottishBook112Wanted.scottishBook112_refuted
statement: formalized
---

# Class-preserving automorphisms

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html).

## Claim of Kourovka Problem 16.62

For every group $G$: if every automorphism of $G$ sends
each element $g \in G$ to a conjugate of $g$ (equivalently, maps every conjugacy class of $G$ into
itself), then every automorphism of $G$ is inner, that is, of the form $x \mapsto h x h^{-1}$ for
some $h \in G$.

Formalized by `MathlibExt.GroupTheory.ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.classPreservingAutomorphismsInner`, a definition declared in [WantedExt/GroupTheory/ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html#class-preserving-automorphisms-inner).

## Groups whose automorphisms all preserve conjugacy classes can have outer automorphisms

The
claim of Kourovka Problem 16.62 is false: there is a group $G$ such that every automorphism of $G$
sends each element $g \in G$ to a conjugate of $g$, but some automorphism of $G$ is not inner,
that is, not of the form $x \mapsto h x h^{-1}$ for any $h \in G$.

Heineken constructed finite $p$-groups all of whose automorphisms preserve every conjugacy class,
and Gaschütz' theorem gives these groups outer automorphisms.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.62 (D. MacHale); resolution: H. Heineken, Arch. Math. (Basel) 33 (1979/80), no. 6, 497-503; A. Mann, letter of 20 April 2006, as recorded in the Kourovka Archive, Kourovka Archive, Problem 16.62 (Not necessarily: Heineken's finite p-groups all of whose automorphisms preserve all conjugacy classes have outer automorphisms by Gaschütz' theorem).

Stated but not proved: `MathlibExt.GroupTheory.ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.classPreservingAutomorphismsInner_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClassPreservingAutomorphismsInnerKourovka16Problem62Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html#class-preserving-automorphisms-inner-ref).

## Claim of Scottish Book Problem 112

The claim that for every group $G$, every
automorphism $\alpha$ of $G$ that sends each element to a conjugate of itself (for each
$x \in G$ there is $g \in G$ with $\alpha(x) = g x g^{-1}$) is inner, that is, there is a
single $g \in G$ with $\alpha(x) = g x g^{-1}$ for all $x \in G$.

Formalized by `MathlibExt.GroupTheory.ScottishBook112Wanted.ScottishBookProblem112Claim`, a definition declared in [WantedExt/GroupTheory/ScottishBook112Wanted.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ScottishBook112Wanted.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html#scottish-book-problem112-claim).

## Class-preserving automorphisms need not be inner

The claim of Scottish Book Problem 112
is false: there are a group $G$ and an automorphism $\alpha$ of $G$ that sends every element
to a conjugate of itself (for each $x \in G$ there is $g \in G$ with $\alpha(x) = g x g^{-1}$)
but is not inner (there is no $g \in G$ with $\alpha(x) = g x g^{-1}$ for all $x \in G$).

Burnside's 1913 example is such a group: for an odd prime $p$, a group of order $p^6$,
isomorphic to the group of $3 \times 3$ lower unitriangular matrices over the field
$\mathbb{F}_{p^2}$, whose group of class-preserving outer automorphisms is nontrivial.

## Sources

- W. Burnside's 1913 example, as summarized in M. K. Yadav, "Class preserving automorphisms of finite p-groups: A survey", arXiv:1002.1359, §1 (Burnside constructed a group of order `p ^ 6` with `Out_c (G) ≠ 1`).

Stated but not proved: `MathlibExt.GroupTheory.ScottishBook112Wanted.scottishBook112_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ScottishBook112Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ScottishBook112Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html#scottish-book112-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Class-preserving automorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/class-preserving-automorphisms)
