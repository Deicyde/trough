---
declaration: theorem
origin: cited
lean: Erdos1159.erdos_1159
statement: formalized
---

# Erdős Problem 1159

> *References:*
> - [erdosproblems.com/1159](https://www.erdosproblems.com/1159)
> - [ESS83] Erdős, P. and Silverman, R. and Stein, A., *Intersection properties of families containing
>   sets of nearly the same size*. Ars Combin. (1983), 247--259.
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.

*Quoted from [FormalConjectures/ErdosProblems/1159.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1159.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1159](https://www.erdosproblems.com/1159).

The file states 1 research or textbook statement: 1 open.

## `Erdos1159.erdos_1159`

Open: stated without proof.

> Determine whether there exists a constant $C>1$ such that the following holds.
>
> Let $P$ be a finite [projective plane](https://en.wikipedia.org/wiki/Projective_plane). Must there exist a set of points $S$ such that $1\leq \lvert S\cap \ell\rvert \leq C$ for all lines $\ell$?

```lean
theorem erdos_1159 :
    ∃ C : ℕ, 1 < C ∧
      ∀ (P L : Type) (_ : Membership P L) (_ : Fintype P) (_ : Fintype L),
        ∀ _ : ProjectivePlane P L, ∃ S : Set P, ∀ l : L,
          1 ≤ (S ∩ {p : P | p ∈ l}).ncard ∧ (S ∩ {p : P | p ∈ l}).ncard ≤ C
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1159.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1159.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1159.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1159.lean)
- [erdosproblems.com/1159](https://www.erdosproblems.com/1159)
