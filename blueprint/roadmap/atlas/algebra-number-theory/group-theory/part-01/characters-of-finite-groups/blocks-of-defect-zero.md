---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.IsPSoluble, MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.HasDefectZeroBlock, MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.defectZeroBlockIffPRegularCentralizer, MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.defectZeroBlockIffPRegularCentralizer_refuted, MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.defectZeroCharacters, MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.commutatorSolutionCount, MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.nondivisibleCommutatorClasses, MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.defectZeroBlocksEqNondivisibleClasses
statement: formalized
---

# Blocks of defect zero

11 results, 8 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html).

## $p$-soluble groups

Let $p$ be a natural number. A group $G$ is $p$-soluble when it has a
subnormal series $1 = H_0 \le H_1 \le \dots \le H_n = G$, each $H_i$ normal in $H_{i+1}$, whose
factors $H_{i+1}/H_i$ are $p$-groups or have order prime to $p$. Here an infinite factor is taken
to have order $0$.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.IsPSoluble`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#is-psoluble).

## Groups with a $p$-block of defect zero

Let $p$ be a natural number. A group $G$ has a
$p$-block of defect zero when some irreducible finite-dimensional complex representation of $G$ has
degree divisible by $p^{v_p(|G|)}$, where $v_p(|G|)$ is the exponent of $p$ in the prime
factorization of the order $|G|$ of $G$ (this exponent is $0$ when $p$ is not prime or $G$ is
infinite). For a prime $p$ and a finite group $G$, the number $p^{v_p(|G|)}$ is $|G|_p$, the largest
power of $p$ dividing $|G|$.

By Brauer's theory the $p$-blocks of defect zero are exactly the singletons $\{\chi\}$ with $\chi$
irreducible and $|G|_p \mid \chi(1)$.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.HasDefectZeroBlock`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#has-defect-zero-block).

## Kourovka Problem 12.26

This is the proposition (Shi Shengming) that for every prime $p$ and
every finite $p$-soluble group $G$, the group $G$ has a $p$-block of defect zero if and only if some
normal subgroup $N$ of $G$ of order prime to $p$ contains an element $x$ whose centralizer $C_G(x)$
in $G$ has order prime to $p$.

Equivalently, some $x \in O_{p'}(G)$ has a centralizer of order prime to $p$, since $O_{p'}(G)$ is
the largest normal subgroup of $G$ of order prime to $p$.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.defectZeroBlockIffPRegularCentralizer`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#defect-zero-block-iff-pregular-centraliz).

## Refutation of Kourovka Problem 12.26

The proposition of Kourovka Problem 12.26 is false:
it is not the case that for every prime $p$ and every finite $p$-soluble group $G$, the group $G$
has a $p$-block of defect zero if and only if some normal subgroup $N$ of $G$ of order prime to $p$
contains an element $x$ whose centralizer $C_G(x)$ in $G$ has order prime to $p$.

V. I. Zenkov's counterexample: the group $G = 3^2.\mathrm{GL}_2(3)$ of order $432$ is soluble and
has a $2$-block of defect zero (an irreducible character of degree $16$), but the centralizer of
every element of $O_{2'}(G) = 3^2$, the largest normal subgroup of $G$ of odd order, has even order.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.26 (Shi Shengming; Jiping Zhang); resolution: V. I. Zenkov, Trudy Inst. Mat. i Mekh. UrO RAN 3 (1995), 36-40 (Russian), Kourovka Archive, Problem 12.26: No; G = 3^2.GL_2(3), p = 2.

Stated but not proved: `MathlibExt.GroupTheory.DefectZeroBlockCentralizerKourovka12Problem26Wanted.defectZeroBlockIffPRegularCentralizer_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlockCentralizerKourovka12Problem26Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#defect-zero-block-iff-pregular-centraliz-2).

## Characters of $p$-defect zero

For a natural number $p$ and a group $G$, the set of
characters $\chi \colon G \to \mathbb{C}$ of irreducible finite-dimensional complex representations
of $G$ whose degree is divisible by $p^a$, where $a$ is the exponent of $p$ in the prime
factorization of the order $|G|$ (and $a = 0$ when $G$ is infinite or $p$ is not prime).

For a prime $p$ and a finite group $G$, each $p$-block of defect zero contains exactly one
irreducible character, and every such character forms a block of defect zero (Brauer), so these
characters count the $p$-blocks of defect zero.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.defectZeroCharacters`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#defect-zero-characters).

## Number of solutions of a commutator equation

For an element $g$ of a group $G$, the
number of pairs $(x, y) \in G \times G$ with $[x, y] = x y x^{-1} y^{-1} = g$, taken to be $0$ when
there are infinitely many such pairs.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.commutatorSolutionCount`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#commutator-solution-count).

## Conjugacy classes with commutator count not divisible by $p$

For a natural number $p$ and
a group $G$, the set of conjugacy classes of $G$ containing an element $g$ such that the number of
pairs $(x, y) \in G \times G$ with $[x, y] = x y x^{-1} y^{-1} = g$ (taken to be $0$ when there are
infinitely many) is not divisible by $p$.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.nondivisibleCommutatorClasses`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#nondivisible-commutator-classes).

## Kourovka Problem 12.80(a): blocks of defect zero and commutator equations

For every prime
$p$ and every finite group $G$ whose order is divisible by $p$, the number of irreducible complex
characters of $G$ of $p$-defect zero equals the number of conjugacy classes of $G$ containing an
element $g$ for which the number of pairs $(x, y) \in G \times G$ with
$[x, y] = x y x^{-1} y^{-1} = g$ is not divisible by $p$.

Each $p$-block of defect zero contains exactly one irreducible character, and every irreducible
character of $p$-defect zero forms such a block (Brauer), so this is K. W. Roggenkamp's question
whether the number of $p$-blocks of defect zero equals that number of classes.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.defectZeroBlocksEqNondivisibleClasses`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#defect-zero-blocks-eq-nondivisible-class).

## Kourovka Problem 12.80(b): the case of simple groups

For every prime $p$ and every
finite simple group $G$ whose order is divisible by $p$, the number of irreducible complex
characters of $G$ of $p$-defect zero equals the number of conjugacy classes of $G$ containing an
element $g$ for which the number of pairs $(x, y) \in G \times G$ with
$[x, y] = x y x^{-1} y^{-1} = g$ is not divisible by $p$.

Formalized by `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.simpleDefectZeroBlocksEqNondivisibleClasses`, a definition declared in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#simple-defect-zero-blocks-eq-nondivisibl).

## Kourovka Problem 12.80(a) has a negative answer

It is not true that for every prime $p$ and
every finite group $G$ whose order is divisible by $p$, the number of irreducible complex characters
of $G$ of $p$-defect zero equals the number of conjugacy classes of $G$ containing an element $g$
for which the number of pairs $(x, y) \in G \times G$ with $[x, y] = x y x^{-1} y^{-1} = g$ is not
divisible by $p$.

L. Barker's counterexample: for $p = 2$ and $G = \mathbb{Z}_3 \times S_3$ there are three
irreducible characters of degree $2$, all of $2$-defect zero (so three $2$-blocks of defect zero),
but only one class, that of $(1, (123))$, with an odd number of solutions of $[x, y] = g$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.80 (K. W. Roggenkamp; S. P. Strunkov); resolution: L. Barker, letter of 27 May 1996 (part a); B. Sambale, letter of 5 May 2021 (part b); as recorded in the Kourovka Archive, Problem 12.80, (a) p = 2, G = ℤ_3 × S_3; (b) p = 2, G = A_5: one 2-block of defect zero, three classes ((123), (12345), (13524)) with an odd number of solutions of [x, y] = g, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.defectZeroBlocksEqNondivisibleClasses_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#defect-zero-blocks-eq-nondivisible-class-2).

## Kourovka Problem 12.80(b) has a negative answer

It is not true that for every prime $p$ and
every finite simple group $G$ whose order is divisible by $p$, the number of irreducible complex
characters of $G$ of $p$-defect zero equals the number of conjugacy classes of $G$ containing an
element $g$ for which the number of pairs $(x, y) \in G \times G$ with
$[x, y] = x y x^{-1} y^{-1} = g$ is not divisible by $p$.

B. Sambale's counterexample: in $A_5$ with $p = 2$ there is one irreducible character of $2$-defect
zero (the character of degree $4$, so one $2$-block of defect zero) but three classes, those of
$(123)$, $(12345)$ and $(13524)$, with an odd number of solutions of $[x, y] = g$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.80 (K. W. Roggenkamp; S. P. Strunkov); resolution: L. Barker, letter of 27 May 1996 (part a); B. Sambale, letter of 5 May 2021 (part b); as recorded in the Kourovka Archive, Problem 12.80, (a) p = 2, G = ℤ_3 × S_3; (b) p = 2, G = A_5: one 2-block of defect zero, three classes ((123), (12345), (13524)) with an odd number of solutions of [x, y] = g, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.simpleDefectZeroBlocksEqNondivisibleClasses_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DefectZeroBlocksCommutatorCountKourovka12Problem80Wanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html#simple-defect-zero-blocks-eq-nondivisibl-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Blocks of defect zero](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/blocks-of-defect-zero)
