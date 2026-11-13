---
declaration: theorem
origin: cited
lean: SteinerSystems.large_steiner_systems, SteinerSystems.steiner_system_5_6_12, SteinerSystems.steiner_system_5_8_24, SteinerSystems.infinitely_many_steiner_t4, SteinerSystems.infinitely_many_steiner_t5
statement: formalized
---

# Steiner Systems

> A Steiner system $S(t, k, n)$ is a collection of $k$-element subsets (called blocks) of
> an $n$-element set such that every $t$-element subset is contained in exactly one block.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Steiner_system)
> - [Large Steiner Systems](https://epoch.ai/frontiermath/open-problems/large-steiner-systems)
>   by Kunal Marwaha

*Quoted from [FormalConjectures/Wikipedia/SteinerSystem.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `SteinerSystems.large_steiner_systems`

Open: stated without proof.

> Construct an $S(t, k, n)$-Steiner system with $n > k > t > 5$, $t < 10$, and $n < 200$.
>
> No example of a Steiner system with $t > 5$ is known, despite a 2014 existence theorem
> by Keevash showing that such systems must exist for sufficiently large $n$.
>
> *Reference:* [Large Steiner Systems](https://epoch.ai/frontiermath/open-problems/large-steiner-systems)

```lean
theorem large_steiner_systems : Nonempty LargeSteinerSystemWitness
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SteinerSystem.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean#L87).

## `SteinerSystems.steiner_system_5_6_12`

Proved here.

> **Existence of $S(5, 6, 12)$**: The small Witt design.
>
> There exists a unique Steiner system $S(5, 6, 12)$, known as the small Witt design.
> It was constructed by Witt (1938) and is closely related to the Mathieu group $M_{12}$.
> This is one of only two known Steiner systems with $t = 5$.

```lean
theorem steiner_system_5_6_12 : Nonempty S(5, 6, 12)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SteinerSystem.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean#L110).

## `SteinerSystems.steiner_system_5_8_24`

Solved: stated here without proof.

> **Existence of $S(5, 8, 24)$**: The large Witt design.
>
> There exists a unique Steiner system $S(5, 8, 24)$, known as the large Witt design.
> It was constructed by Witt (1938) and is closely related to the Mathieu group $M_{24}$.
> This is one of only two known Steiner systems with $t = 5$.

```lean
theorem steiner_system_5_8_24 : Nonempty S(5, 8, 24)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SteinerSystem.lean, line 253](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean#L253).

## `SteinerSystems.infinitely_many_steiner_t4`

Solved: stated here without proof.

> **There are infinitely many Steiner systems with $t = 4$.**
>
> Keevash (2014) proved that for any fixed $t$ and $k$, a Steiner system $S(t, k, n)$
> exists for all sufficiently large $n$ satisfying the necessary divisibility conditions.
> Since there are infinitely many such admissible $n$, this implies infinitely many
> $S(4, k, n)$ systems exist (for any fixed $k > 4$). The proof is nonconstructive.
>
> Explicit examples include $S(4, 5, 11)$ (the unique system, related to the Mathieu
> group $M_{11}$) and $S(4, 7, 23)$ (related to the Mathieu group $M_{23}$).
>
> Only nontrivial systems with $4 < k < n$ are counted: for every $n$ the single block
> $\{1, \dots, n\}$ is an $S(4, n, n)$, and all $4$-subsets of an $n$-set form an $S(4, 4, n)$.

```lean
theorem infinitely_many_steiner_t4 :
    {s : Σ k n : ℕ, S(4, k, n) | 4 < s.1 ∧ s.1 < s.2.1}.Infinite
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SteinerSystem.lean, line 271](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean#L271).

## `SteinerSystems.infinitely_many_steiner_t5`

Solved: stated here without proof.

> **There are infinitely many Steiner systems with $t = 5$.**
>
> Keevash (2014) proved that for any fixed $t$ and $k$, a Steiner system $S(t, k, n)$
> exists for all sufficiently large $n$ satisfying the necessary divisibility conditions.
> This settles the long-standing open problem of whether infinitely many $S(5, k, n)$
> systems exist. The proof is nonconstructive.
>
> Only two explicit examples are known: $S(5, 6, 12)$ and $S(5, 8, 24)$, both Witt
> designs related to the Mathieu groups $M_{12}$ and $M_{24}$ respectively.
>
> Only nontrivial systems with $5 < k < n$ are counted, for the same reason as in
> `infinitely_many_steiner_t4`.
> No Steiner system with $t \geq 6$ has been explicitly constructed, though Keevash's
> result guarantees their existence nonconstructively as well.

```lean
theorem infinitely_many_steiner_t5 :
    {s : Σ k n : ℕ, S(5, k, n) | 5 < s.1 ∧ s.1 < s.2.1}.Infinite
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SteinerSystem.lean, line 292](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean#L292).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SteinerSystem.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SteinerSystem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Steiner_system)
