---
declaration: theorem
origin: cited
lean: Erdos413.erdos_413.parts.i, Erdos413.erdos_413.variants.hasPosDensity_barrier_expProd, Erdos413.erdos_413.variants.bigOmega, Erdos413.erdos_413.variants.bigOmega_largest_barrier_lt_100k, Erdos413.erdos_413.parts.ii
statement: formalized
---

# Erdős Problem 413

> *References:*
> - [erdosproblems.com/413](https://www.erdosproblems.com/413)
> - [A5236](https://oeis.org/A5236)
> - [La26] Lau, C. F., *On the Number of Prime Factors of Consecutive Integers*.
>   [arXiv:2604.15042](https://arxiv.org/abs/2604.15042) (2026).
>
> Erdős called a natural number `n` a *barrier* for `ω`, the number of distinct prime divisors,
> if `m + ω(m) ≤ n` for all `m < n`. He believed there should be infinitely many such barriers, and
> even posed a relaxed variant asking whether there is some `ε > 0` for which infinitely many `n`
> satisfy `m + ε · ω(m) ≤ n` for every `m < n`.

*Quoted from [FormalConjectures/ErdosProblems/413.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/413](https://www.erdosproblems.com/413).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos413.erdos_413.parts.i`

Open: stated without proof.

> Are there infinitely many barriers for `ω`?

```lean
theorem erdos_413.parts.i :
    { n | IsBarrier (fun m => ω m) n }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/413.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean#L49).

## `Erdos413.erdos_413.variants.hasPosDensity_barrier_expProd`

Solved: stated here without proof.

> Erdős proved that the barrier set for `expProd` is infinite and even has positive density.
>
> `HasPosDensity` is the right reading rather than positive lower density. In [Er79d] this is
> Theorem 1, "the density of integers satisfying (2) is positive", where `d₀(n) = ∏ αᵢ` is
> `expProd`. The averaging argument there bounds the density below, but Erdős states the existence
> separately on the last page: "With a little more trouble, I can prove that the density of
> integers `n` for which `n` is a barrier for `d₀(n)` exists." He goes further, that if `αᵢ` is the
> density of `n` with `max_{m<n} (m + d₀(m)) = n + i`, then every `αᵢ` exists and they sum to `1`.
>
> [Er79d] Erdős, P., *Some unconventional problems in number theory*.
> Acta Math. Acad. Sci. Hungar. (1979), 71-80.

```lean
theorem erdos_413.variants.hasPosDensity_barrier_expProd :
    { n | IsBarrier (fun m => expProd m) n }.HasPosDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/413.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean#L69).

## `Erdos413.erdos_413.variants.bigOmega`

Open: stated without proof.

> Erdős believed there should be infinitely many barriers for `Ω`, the total prime multiplicity.

```lean
theorem erdos_413.variants.bigOmega :
    { n | IsBarrier (fun m => Ω m) n }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/413.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean#L75).

## `Erdos413.erdos_413.variants.bigOmega_largest_barrier_lt_100k`

Solved: stated here without proof.

> Selfridge computed that the largest `Ω`-barrier below `10^5` is `99840`.

```lean
theorem erdos_413.variants.bigOmega_largest_barrier_lt_100k :
    IsGreatest {n : ℕ | n < 10 ^ 5 ∧ IsBarrier (fun m => Ω m) n} 99840
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/413.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean#L81).

## `Erdos413.erdos_413.parts.ii`

Solved: stated here without proof.

> Does there exist some $\epsilon > 0$ such that there are infinitely many
> $\epsilon$-barriers for $\omega$? Lau [La26, Theorem 1.3] gives a positive answer.

```lean
theorem erdos_413.parts.ii :
    (∃ ε > (0 : ℝ), { n | IsBarrier (fun n => ε * ω n) n }.Infinite)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/413.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/413.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/413.lean)
- [erdosproblems.com/413](https://www.erdosproblems.com/413)
