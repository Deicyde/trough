---
declaration: theorem
origin: cited
lean: Erdos233.erdos_233, Erdos233.erdos_233.variants.upper_bound, Erdos233.erdos_233.variants.lower_bound
statement: formalized
---

# Erdős Problem 233

> *References:*
>   - [erdosproblems.com/233](https://www.erdosproblems.com/233)
>   - [A74741](https://oeis.org/A74741)
>   - [Wikipedia](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture)

*Quoted from [FormalConjectures/ErdosProblems/233.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/233.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/233](https://www.erdosproblems.com/233).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos233.erdos_233`

Open: stated without proof.

> A conjecture by Heath-Brown:
> The sum of squares of the first $N$ gaps between consecutive primes behaves like $N * (log N)^2$.

```lean
theorem erdos_233 :
    (fun N => ((∑ n ∈ Finset.range N, (primeGap n) ^ 2) : ℝ)) =O[atTop] fun N => N * (log N)^2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/233.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/233.lean#L40).

## `Erdos233.erdos_233.variants.upper_bound`

Solved: stated here without proof.

> Cramér proved an upper bound of $O(N(\log N)^4)$ conditional on the Riemann hypothesis.

```lean
theorem erdos_233.variants.upper_bound (h : RiemannHypothesis) :
    (fun N => ((∑ n ∈ Finset.range N, (primeGap n) ^ 2) : ℝ)) =O[atTop] fun N => N * (log N)^4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/233.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/233.lean#L48).

## `Erdos233.erdos_233.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/032848c62fdf4c422bb0ee6663dc8d009d456c2c/FormalConjectures/ErdosProblems/233.lean#L57](https://github.com/mzhorvath1/formal-conjectures/blob/032848c62fdf4c422bb0ee6663dc8d009d456c2c/FormalConjectures/ErdosProblems/233.lean#L57).

> The prime number theorem immediately implies a lower bound of $\gg N(\log N)^2$ for the sum of
> squares of gaps between consecutive primes.
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem erdos_233.variants.lower_bound :
    (fun (N : ℕ) => N * (log N)^2) =O[atTop]
    (fun N => ((∑ n ∈ Finset.range N, (primeGap n) ^ 2) : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/233.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/233.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/233.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/233.lean)
- [erdosproblems.com/233](https://www.erdosproblems.com/233)
