---
declaration: theorem
origin: cited
lean: Erdos701.erdos_701
statement: formalized
---

# Erdős Problem 701

> *Reference:* [erdosproblems.com/701](https://www.erdosproblems.com/701)

*Quoted from [FormalConjectures/ErdosProblems/701.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/701.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/701](https://www.erdosproblems.com/701).

The file states 1 research or textbook statement: 1 open.

## `Erdos701.erdos_701`

Open: stated without proof.

> Let $\mathcal{F}$ be a family of sets closed under taking subsets (i.e. if
> $B\subseteq A\in\mathcal{F}$ then $B\in \mathcal{F}$). There exists some element $x$ such that
> whenever $\mathcal{F}'\subseteq \mathcal{F}$ is an intersecting subfamily we have
>
> $$\lvert \mathcal{F}'\rvert \leq \lvert \{ A\in \mathcal{F} : x\in A\}\rvert.$$

```lean
theorem erdos_701 : ∀ {X : Type} [Nonempty X] [Fintype X],
    ∀ (F : Set (Set X)), IsLowerSet F →
      ∃ x : X, ∀ᵉ (F' ⊆ F),
        F'.Intersecting →
          (#F' ≤ #{ A : Set X | A ∈ F ∧ x ∈ A })
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/701.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/701.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/701.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/701.lean)
- [erdosproblems.com/701](https://www.erdosproblems.com/701)
