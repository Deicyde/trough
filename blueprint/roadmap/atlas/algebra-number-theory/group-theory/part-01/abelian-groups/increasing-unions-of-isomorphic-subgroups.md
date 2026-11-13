---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ScottishBook62Wanted.ScottishBookProblem62Claim, MathlibExt.GroupTheory.ScottishBook62Wanted.mazurUlam62_refuted
statement: formalized
---

# Increasing unions of isomorphic subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/increasing-unions-of-isomorphic-subgroups/index.html).

## Claim of Scottish Book Problem 62

The claim that for every abelian group $G$ and
every sequence of subgroups $H_0 \le H_1 \le H_2 \le \cdots$ of $G$ whose union is $G$ and
each of which is isomorphic to $H_1$, the group $G$ is itself isomorphic to $H_1$.

The problem is posed for groups; the claim here is restricted to abelian groups, which loses
nothing for its refutation since Baer's counterexample is abelian.

Formalized by `MathlibExt.GroupTheory.ScottishBook62Wanted.ScottishBookProblem62Claim`, a definition declared in [WantedExt/GroupTheory/ScottishBook62Wanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ScottishBook62Wanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/increasing-unions-of-isomorphic-subgroups/index.html#scottish-book-problem62-claim).

## Refutation of Scottish Book Problem 62

The claim of Scottish Book Problem 62 is false:
there are an abelian group $G$ and subgroups $H_0 \le H_1 \le H_2 \le \cdots$ of $G$ whose
union is $G$, each isomorphic to $H_1$, such that $G$ is not isomorphic to $H_1$.

R. Baer's counterexample is $G = \mathbb{Q}$ with $H_n = \frac{1}{n!}\mathbb{Z}$: each $H_n$
is isomorphic to $\mathbb{Z}$ and their union is $\mathbb{Q}$, but $\mathbb{Q}$ is not
isomorphic to $\mathbb{Z}$.

## Sources

- S. Mazur and S. Ulam, Problem 62 of the Scottish Book; the typescript Ad 62 records R. Baer's remark giving the counterexample, with `G` the group of rational numbers and `G 1` the integers: the rationals are the union of an increasing chain of subgroups each isomorphic to the integers (for example the subgroups `(1 / n !) ℤ`), but the rationals are not isomorphic to the integers.

Stated but not proved: `MathlibExt.GroupTheory.ScottishBook62Wanted.mazurUlam62_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ScottishBook62Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ScottishBook62Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/increasing-unions-of-isomorphic-subgroups/index.html#mazur-ulam62-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Increasing unions of isomorphic subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/increasing-unions-of-isomorphic-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/abelian-groups/increasing-unions-of-isomorphic-subgroups)
