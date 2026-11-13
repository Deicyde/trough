---
declaration: theorem
origin: cited
lean: GottschalkSurjunctivity.gottschalk_surjunctivity_conjecture, GottschalkSurjunctivity.counter_gottschalk_surjunctivity, GottschalkSurjunctivity.isSurjunctive_of_finite
statement: formalized
---

# Gottschalk's surjunctivity conjecture

> A group $G$ is *surjunctive* if every injective, continuous, $G$-equivariant map
> $A^G \to A^G$ (for any finite alphabet $A$) is surjective.
>
> Here equivariance is with respect to the left shift action of $G$ on $A^G$,
> defined by $(g \cdot x)(h) = x(g^{-1} h)$, and continuity is with respect to
> the product topology on $A^G$ (where $A$ carries the discrete topology).
>
> Gottschalk's conjecture (1973) states that every group is surjunctive. It is false: an
> internal OpenAI model gave counterexamples in September 2026 [OAI26a], [OAI26b].
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Surjunctive_group)
> - Gottschalk, W. H. (1973), "Some general dynamical notions"
> - [OAI26a] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in
>   Characteristic Two*. OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf
> - [OAI26b] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd
>   Characteristic*. OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf

*Quoted from [FormalConjectures/Wikipedia/SurjunctiveGroup.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SurjunctiveGroup.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 solved and 1 textbook result. It also has 3 API statements, counted here but not shown.

## `GottschalkSurjunctivity.gottschalk_surjunctivity_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/OddKaplansky/Main.lean#L81](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/OddKaplansky/Main.lean#L81).

> **Gottschalk's surjunctivity conjecture** (1973): every group is surjunctive.
> That is, for every group `G` and every finite alphabet `A`, every injective cellular
> automaton on `A^G` is surjective.
>
> This is false. It was disproved by an internal OpenAI model in September 2026 [OAI26a],
> [OAI26b]; see `counter_gottschalk_surjunctivity` for the counterexample and for what the
> linked Lean proof covers.

```lean
theorem gottschalk_surjunctivity_conjecture :
    ¬ ∀ (G : Type) [Group G], IsSurjunctive G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/SurjunctiveGroup.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SurjunctiveGroup.lean#L98).

## `GottschalkSurjunctivity.counter_gottschalk_surjunctivity`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/OddKaplansky/Main.lean#L81](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Algebra/OddKaplansky/Main.lean#L81).

> **Gottschalk's surjunctivity conjecture** is false: there is a group that is not
> surjunctive.
>
> There are a finite field $K$, a group $G$ and $a, b \in K[G]$ with $ab = 1$ and
> $ba \neq 1$. The linear cellular automaton $x \mapsto (g \mapsto \sum_u b_u x(gu))$ on
> $K^G$ is then injective but not surjective. In [OAI26a], $K$ has characteristic two and $G$
> is finitely presented. In [OAI26b], $K$ has odd characteristic and $G$ is finitely
> generated.
>
> This was proved by an internal OpenAI model in September 2026. The linked Lean proof is for
> [OAI26b]. It shows that the map above is injective and not surjective. That the map is
> continuous and shift-equivariant, as `IsSurjunctive` requires, is not part of the linked
> proof.

```lean
theorem counter_gottschalk_surjunctivity :
    ∃ (G : Type) (_ : Group G), ¬ IsSurjunctive G
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/SurjunctiveGroup.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SurjunctiveGroup.lean#L118).

## `GottschalkSurjunctivity.isSurjunctive_of_finite`

Textbook result, proved here.

> Every finite group is surjunctive. This is a classical result: an injective
> endomorphism of a finite set is surjective.

```lean
theorem isSurjunctive_of_finite (G : Type) [Group G] [Finite G] :
    IsSurjunctive G
```

Category `textbook`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Wikipedia/SurjunctiveGroup.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SurjunctiveGroup.lean#L125).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SurjunctiveGroup.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SurjunctiveGroup.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Surjunctive_group)
