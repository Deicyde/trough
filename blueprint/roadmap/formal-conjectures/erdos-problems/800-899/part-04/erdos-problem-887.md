---
declaration: theorem
origin: cited
lean: Erdos887.erdos_887.parts.i, Erdos887.erdos_887.parts.ii, Erdos887.erdos_887.variants.rosenfeld_infinite, Erdos887.erdos_887.variants.rosenfeld_4
statement: formalized
---

# Erdős Problem 887

> *References:*
> * [erdosproblems.com/887](https://www.erdosproblems.com/887)
> * [ErRo97] Erdős, Paul and Rosenfeld, Moshe, The factor-difference set of integers. Acta Arith. (1997), 353--359.

*Quoted from [FormalConjectures/ErdosProblems/887.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/887](https://www.erdosproblems.com/887).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos887.erdos_887.parts.i`

Open: stated without proof.

> Is there an absolute constant $K$ such that, for every $C > 0$, if $n$ is sufficiently large then
> $n$ has at most $K$ divisors in $(n^{\frac{1}{2}}, n^{\frac{1}{2}} + C n^{\frac{1}{4}})$.

```lean
theorem erdos_887.parts.i : ∀ C > (0 : ℝ), ∀ᶠ n in atTop,
    #{ d ∈ Ioo ⌊√n⌋₊ ⌈√n + C * n^((1 : ℝ) / 4)⌉₊ | d ∣ n } ≤ erdos_887.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/887.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean#L40).

## `Erdos887.erdos_887.parts.ii`

Open: stated without proof.

> Is there an absolute constant $K$ such that, for every $C > 0$, if $n$ is sufficiently large then
> $n$ has at most $K$ divisors in $(n^{\frac{1}{2}}, n^{\frac{1}{2}} + C n^{\frac{1}{4}})$.

```lean
theorem erdos_887.parts.ii : ∃ K, ∀ C > (0 : ℝ), ∀ᶠ n in atTop,
    #{ d ∈ Ioo ⌊√n⌋₊ ⌈√n + C * n^((1 : ℝ) / 4)⌉₊ | d ∣ n } ≤ K
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/887.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean#L49).

## `Erdos887.erdos_887.variants.rosenfeld_infinite`

Solved: stated here without proof.

> A question of Erdős and Rosenfeld, who proved that there are infinitely many $n$ with (at least)
> $4$ divisors in $(n^{\frac{1}{2}}, n^{\frac{1}{2}} + cn^{\frac{1}{4}})$.

```lean
theorem erdos_887.variants.rosenfeld_infinite : ∃ C > (0 : ℝ),
    Infinite {n : ℕ | 4 ≤ #{ d ∈ Ioo ⌊√n⌋₊ ⌈√n + C * n^((1 : ℝ) / 4)⌉₊ | d ∣ n }}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/887.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean#L58).

## `Erdos887.erdos_887.variants.rosenfeld_4`

Solved: stated here; a Lean proof is at [https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos887.lean#L538](https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos887.lean#L538).

> Erdős and Rosenfeld ask whether $4$ is the best possible $K$ for the infinitude of $n$
> with (at least) $K$ divisors in $(n^{\frac{1}{2}}, n^{\frac{1}{2}} + C n^{\frac{1}{4}})$, for some
> constant $C > 0$. The constant cannot be taken to be $1$. Distinct divisors $d > \sqrt{n}$ give
> distinct integers $d + n/d$, and a divisor in the interval has
> $2\sqrt{n} < d + n/d < 2\sqrt{n} + C^2$, so for $C = 1$ there is at most one such divisor.
>
> The answer is no. In a [forum post](https://www.erdosproblems.com/forum/thread/887#post-7374)
> (July 2026), m-czech showed that for $C = 31$ infinitely many $n$ have $5$ divisors in the
> interval. The construction is $n = (x^2 - 1)(x^2 - 4)(x^2 - 16)(x^2 - 49)$ with
> $z^2 = 56 x^2 + 65$.

```lean
theorem erdos_887.variants.rosenfeld_4 :
    ¬ IsGreatest {K | ∃ C > (0 : ℝ),
      Infinite {n : ℕ | K ≤ #{ d ∈ Ioo ⌊√n⌋₊ ⌈√n + C * n^((1 : ℝ) / 4)⌉₊ | d ∣ n }}} 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/887.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/887.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/887.lean)
- [erdosproblems.com/887](https://www.erdosproblems.com/887)
