---
declaration: theorem
origin: cited
lean: BabaiSeressConjectures.babai_seress_conjecture_alternating, BabaiSeressConjectures.babai_seress_conjecture
statement: formalized
---

# Babai–Seress Conjectures on the Diameter of Finite Groups

> *References:*
> - [Wikipedia, *Diameter (group theory)*](https://en.wikipedia.org/wiki/Diameter_(group_theory))
> - [H. A. Helfgott and Á. Seress, *On the diameter of permutation groups*](https://arxiv.org/abs/1109.3550)
> - [L. Babai and Á. Seress, *On the diameter of permutation groups*,
>   European Journal of Combinatorics 13 (1992), 231–243](https://doi.org/10.1016/S0195-6698(05)80029-0)
>
> This file contains two conjectures from the Babai–Seress paper:
>
> - **Conjecture 1.5**: $\operatorname{diam}(A_n) < n^C$ for some absolute constant $C$,
>   where $A_n$ is the alternating group on $n$ elements.
>
> - **Conjecture 1.7**: $\operatorname{diam}(G) < (\log |G|)^C$ for some absolute constant $C$,
>   where $G$ ranges over all non-abelian finite simple groups.
>
> Conjecture 1.7 generalises Conjecture 1.5, since for $G = A_n$ we have
> $\log |A_n| \approx n \log n$, so a polylogarithmic bound in $|G|$ implies a polynomial
> bound in $n$.

*Quoted from [FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 3 test statements, counted here but not shown.

## `BabaiSeressConjectures.babai_seress_conjecture_alternating`

Open: stated without proof.

> **Babai–Seress Conjecture (Conjecture 1.5)**: There exists an absolute constant $C$ such
> that the diameter of the alternating group $A_n$ satisfies
> $$\operatorname{diam}(A_n) \leq n^C.$$
>
> *Reference:* [L. Babai and Á. Seress, *On the diameter of permutation groups*,
> European Journal of Combinatorics 13 (1992), Conjecture 1.5](https://doi.org/10.1016/S0195-6698(05)80029-0)

```lean
theorem babai_seress_conjecture_alternating :
    ∃ C : ℕ, ∀ n : ℕ,
    (groupDiam (alternatingGroup (Fin n)) : ℝ) ≤ (n : ℝ) ^ C
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean#L156).

## `BabaiSeressConjectures.babai_seress_conjecture`

Open: stated without proof.

> **Babai–Seress Conjecture (Conjecture 1.7)**: There exists an absolute constant $C$ such
> that every finite simple non-abelian group $G$ satisfies
> $$\operatorname{diam}(G) \leq (\log |G|)^C.$$
>
> *Reference:* [L. Babai and Á. Seress, *On the diameter of permutation groups*,
> European Journal of Combinatorics 13 (1992), Conjecture 1.7](https://doi.org/10.1016/S0195-6698(05)80029-0)

```lean
theorem babai_seress_conjecture :
    ∃ C : ℕ,
    ∀ (G : Type) [Group G] [Fintype G] [IsSimpleGroup G],
    (∃ a b : G, a * b ≠ b * a) →
    (groupDiam G : ℝ) ≤ (Real.log (Fintype.card G : ℝ)) ^ C
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean#L168).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiameterSimpleFiniteGroups.lean)
- [Wikipedia, *Diameter (group theory)*](https://en.wikipedia.org/wiki/Diameter_%28group_theory%29)
