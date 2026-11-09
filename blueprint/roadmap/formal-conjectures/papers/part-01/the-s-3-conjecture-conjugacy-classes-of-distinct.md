---
declaration: theorem
origin: cited
lean: ConjugacyClassSizes.conjClassSizes_iff_sym_three, ConjugacyClassSizes.conjClassSizes_iff_sym_three_solvable
statement: formalized
---

# The $S_3$-conjecture (conjugacy classes of distinct sizes)

> *References:*
> * W. Zhou, I. Gorshkov, *On $\{2,3,5\}$-groups with conjugacy classes of distinct sizes*,
>   [arXiv:2606.22244](https://arxiv.org/abs/2606.22244) (2026).
> * F. M. Markel, *Groups with many conjugate elements*, J. Algebra **26** (1973), 69–74.
>   (Origin of the $S_3$-conjecture.)
> * R. Knörr, W. Lempken, B. Thielcke, *The $S_3$-conjecture for solvable groups*,
>   Israel J. Math. **91** (1995), 61–76.
> * J. Zhang, *Finite groups with many conjugate elements*, J. Algebra **170** (1994), 608–624.
> * Z. Arad, M. Muzychuk, A. Oliver, *On groups with conjugacy classes of distinct sizes*,
>   J. Algebra **280** (2004), 537–576.
> * [Conjugacy class](https://en.wikipedia.org/wiki/Conjugacy_class)
>
> A finite group in which distinct conjugacy classes have distinct cardinalities is called an
> *anti-homogeneous* group (or *ah-group*). The symmetric group $S_3$ is an ah-group: its three
> conjugacy classes have sizes $1$, $2$, and $3$. Markel's **$S_3$-conjecture** (1973) asserts that,
> up to isomorphism, $S_3$ is the only nontrivial finite ah-group. The conjecture has been proved
> for all solvable groups (independently by Zhang and by Knörr–Lempken–Thielcke), but the general
> non-solvable case remains open.

*Quoted from [FormalConjectures/Paper/ConjugacyClassSizes.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ConjugacyClassSizes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements and 1 API statement, counted here but not shown.

## `ConjugacyClassSizes.conjClassSizes_iff_sym_three`

Open: stated without proof.

> **Markel's $S_3$-conjecture** (1973): any nontrivial finite ah-group is isomorphic to $S_3$.
>
> The conjecture is open in general; it is known to be true for solvable groups.

```lean
theorem conjClassSizes_iff_sym_three
    (G : Type) [Group G] [Fintype G] [Nontrivial G]
    (h : HasDistinctConjClassSizes (G := G)) :
    Nonempty (G ≃* Equiv.Perm (Fin 3))
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Paper/ConjugacyClassSizes.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ConjugacyClassSizes.lean#L135).

## `ConjugacyClassSizes.conjClassSizes_iff_sym_three_solvable`

Solved: stated here without proof.

> The $S_3$-conjecture holds for solvable groups: every nontrivial *solvable* finite ah-group is
> isomorphic to $S_3$. This was proved independently by Zhang (1994) and by
> Knörr–Lempken–Thielcke (1995).

```lean
theorem conjClassSizes_iff_sym_three_solvable
    (G : Type) [Group G] [Fintype G] [Group.IsSolvable G] [Nontrivial G]
    (h : HasDistinctConjClassSizes (G := G)) :
    Nonempty (G ≃* Equiv.Perm (Fin 3))
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Paper/ConjugacyClassSizes.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ConjugacyClassSizes.lean#L147).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ConjugacyClassSizes.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ConjugacyClassSizes.lean)
- [arXiv:2606.22244](https://arxiv.org/abs/2606.22244)
