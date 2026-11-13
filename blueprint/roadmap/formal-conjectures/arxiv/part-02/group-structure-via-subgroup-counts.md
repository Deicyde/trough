---
declaration: theorem
origin: cited
lean: Arxiv.«2604.08040».solvable_of_cyc_lt, Arxiv.«2604.08040».nilpotent_of_cyc_lt, Arxiv.«2604.08040».solvable_of_cyc_lt_two_pow_succ
statement: formalized
---

# Group structure via subgroup counts

> *Reference:* [arXiv:2604.08040v1](https://arxiv.org/abs/2604.08040v1)
> **Group Structure via Subgroup Counts**
> by *Angsuman Das, Hiranya Kishore Dey, Khyati Sharma* (2026)
>
> For a finite group $G$, let $\mathrm{cyc}(G)$ denote the number of cyclic subgroups of $G$,
> and let $t = \pi(G)$ denote the number of distinct prime divisors of $|G|$.
>
> The paper establishes several structural results of the form
> "if $\mathrm{cyc}(G)$ or $\mathrm{sub}(G)$ is small relative to $2^t$, then $G$
> has a strong structural property":
>
> * $\mathrm{cyc}(G) < 5 \cdot 2^{t-2} \implies G$ is nilpotent (Theorem 3.1)
> * $\mathrm{cyc}(G) < 2^{t+1} \implies G$ is supersolvable (Theorem 4.2)
> * $\mathrm{sub}(G) < 59 \cdot 2^{t-3} \implies G$ is solvable (Theorem 5.3)
>
> **Conjecture 5.5** proposes the analogue for solvability via cyclic subgroup count:
> if $\mathrm{cyc}(G) < 2^{t+2}$, then $G$ is solvable.
>
> * **In-Paper Location:** Conjecture 5.5, Section 5 "Solvability of a group from $\mathrm{sub}(G)$"
>   ([PDF page 15](https://arxiv.org/pdf/2604.08040v1#page=15))
> * **OpenConjecture ID:** 1512

*Quoted from [FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 5 test statements, counted here but not shown.

## `Arxiv.«2604.08040».solvable_of_cyc_lt`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/das-dey-sharma-conjecture-5-5/blob/7a2600dd6471536cf246ad8d78d756e130d2fe9e/lean/Conjecture55FC.lean#L15-L18](https://github.com/KitaKen1/das-dey-sharma-conjecture-5-5/blob/7a2600dd6471536cf246ad8d78d756e130d2fe9e/lean/Conjecture55FC.lean#L15-L18).

> **Conjecture 5.5** (Das, Dey, Sharma 2026):
> If a finite group `G` satisfies $\mathrm{cyc}(G) < 2^{t+2}$, where $t = \pi(G)$ is the
> number of distinct prime divisors of $|G|$, then `G` is solvable.
>
> This is Theorem 7.1 of the second version of the paper,
> [arXiv:2604.08040v2](https://arxiv.org/abs/2604.08040v2) (Das, Dey, Galindo, Sharma),
> proved there using the classification of finite simple groups.
>
> The Lean proof here by Kenta Kitamura instead uses only the Feit–Thompson theorem and the Gorenstein–Walter classification of groups with dihedral Sylow 2-subgroups, together with counting arguments on Sylow 2-subgroups and families of cyclic subgroups.

```lean
theorem solvable_of_cyc_lt :
    ∀ (G : Type) [Group G] [Fintype G],
      cyc G < 2 ^ (numPrimeFactors G + 2) → Group.IsSolvable G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean#L81).

## `Arxiv.«2604.08040».nilpotent_of_cyc_lt`

Solved: stated here without proof.

> **Theorem 3.1.** Below $5 \cdot 2^{t-2}$ cyclic subgroups, the group is nilpotent.

```lean
theorem nilpotent_of_cyc_lt (h : cyc G < 5 * 2 ^ (numPrimeFactors G - 2)) :
    Group.IsNilpotent G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean#L90).

## `Arxiv.«2604.08040».solvable_of_cyc_lt_two_pow_succ`

Solved: stated here without proof.

> **Theorem 4.2.** Below $2^{t+1}$ cyclic subgroups, the group is supersolvable.
>
> Stated here as solvability, which supersolvability implies, since Mathlib does not
> currently have a standalone `IsSupersolvable` class.

```lean
theorem solvable_of_cyc_lt_two_pow_succ (h : cyc G < 2 ^ (numPrimeFactors G + 1)) :
    Group.IsSolvable G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2604.08040/Conjecture5_5.lean)
- [arXiv:2604.08040v1](https://arxiv.org/abs/2604.08040v1)
