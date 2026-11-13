---
declaration: theorem
origin: cited
lean: Erdos38.erdos_38
statement: formalized
---

# Erdős Problem 38

> *Reference:*
> - [erdosproblems.com/38](https://www.erdosproblems.com/38)
> - [Er56\](Erdős, P., Problems and results in additive number theory.
>   Colloque sur la Théorie des Nombres, Bruxelles, 1955 (1956), 127-137.)

*Quoted from [FormalConjectures/ErdosProblems/38.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/38.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/38](https://www.erdosproblems.com/38).

The file states 1 research or textbook statement: 1 solved.

## `Erdos38.erdos_38`

Solved: stated here; a Lean proof is at [https://www.erdosproblems.com/forum/thread/38#post-6131](https://www.erdosproblems.com/forum/thread/38#post-6131).

> Does there exist $B \subset \mathbb{N}$ which is not an additive basis,
> but is such that for every set $A \subseteq \mathbb{N}$ of Schnirelmann density $\alpha$
> and every $N$ there exists $b \in B$ such that
>
> $$
>   \lvert (A \cup (A+b)) \cap \{1, \ldots, N\} \rvert \geq (\alpha + f(\alpha)) N
> $$
>
> where $f(\alpha) > 0$ for $0 < \alpha < 1$?
>
> Note: here Erdős seems to use a slightly weaker notion of an additive basis (see [Er56] at the top
> of page 135). In particular, for this problem, a set is an additive basis of order $k$ if every
> natural number can be written as a sum of _at most_ $k$ elements of the set, rather than as a sum of
> _precisely_ $k$ elements.
>
> A positive [solution](https://github.com/spicylemonade/erdos-38) was given by GPT 5.5 Pro
> (prompted by gebyjaff, cleanup by Liam Price); in fact a sparse random set $B$ has this property,
> with $f(\alpha)\gg \alpha (1-\alpha)^2$.

```lean
theorem erdos_38 :
    ∃ B : Set ℕ, ¬ B.IsWeakAddBasis ∧ ∃ f : ℝ → ℝ, (∀ α, 0 < α → α < 1 → f α > 0) ∧
      ∀ (A : Set ℕ) (N : ℕ),
        let α := schnirelmannDensity A
        ∃ b ∈ B, (Ioc 0 N ∩ (A ∪ (A + {b}))).ncard ≥ (α + f α) * N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/38.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/38.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/38.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/38.lean)
- [erdosproblems.com/38](https://www.erdosproblems.com/38)
