---
declaration: theorem
origin: cited
lean: Erdos107.erdos_107, Erdos107.nonempty_cardSet, Erdos107.variants.ersz_bounds, Erdos107.variants.su_bound, Erdos107.variants.hmpt_bound
statement: formalized
---

# Erdős Problem 107

> *References:*
> - [erdosproblems.com/107](https://www.erdosproblems.com/107)
> - [Wikipedia](https://en.wikipedia.org/wiki/Happy_ending_problem)

*Quoted from [FormalConjectures/ErdosProblems/107.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/107](https://www.erdosproblems.com/107).

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 2 test statements, counted here but not shown.

## `Erdos107.erdos_107`

Open: stated without proof.

> Let $f(n)$ be minimal such that any $f(n)$ points in $ℝ^2$, no three on a line,
> contain $n$ points which form the vertices of a convex $n$-gon.
> Prove that $f(n) = 2^{n-2} + 1$.

```lean
theorem erdos_107 : ∀ n ≥ 3, f n = 2^(n - 2) + 1
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/107.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean#L50).

## `Erdos107.nonempty_cardSet`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-107/Solution.lean#L59](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-107/Solution.lean#L59).

> For every $n ≥ 3$, there exists $N$ such that any $N$ points, no three on a line,
> contain a convex $n$-gon.

```lean
theorem nonempty_cardSet : ∀ n ≥ 3, (cardSet n).Nonempty
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/107.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean#L58).

## `Erdos107.variants.ersz_bounds`

Solved: stated here without proof.

> Erdős and Szekeres proved the bounds
>
> $$
>   2^{n-2} + 1 ≤ f(n) ≤ \binom{2n-4}{n-2} + 1
> $$
>
> ([ErSz60] and [ErSz35] respectively).
>
> [ErSz60] Erdős, P. and Szekeres, G., _On some extremum problems in elementary geometry_.
>   Ann. Univ. Sci. Budapest. Eötvös Sect. Math. (1960/61), 53-62.
>
> [ErSz35] Erdős, P. and Szekeres, G., _A combinatorial problem in geometry_.
>   Compos. Math. (1935), 463-470.

```lean
theorem ersz_bounds :
    ∀ n ≥ 3, 2^(n - 2) + 1 ≤ f n ∧ f n ≤ Nat.choose (2 * n - 4) (n - 2) + 1
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/107.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean#L141).

## `Erdos107.variants.su_bound`

Solved: stated here without proof.

> Suk [Su17] proved
>
> $$
>   f(n) ≤ 2^{(1+o(1))n}.
> $$
>
> [Su17] Suk, Andrew, _On the Erdős-Szekeres convex polygon problem_.
>   J. Amer. Math. Soc. (2017), 1047-1053.

```lean
theorem su_bound :
    ∃ r : ℕ → ℝ, r =o[atTop] (fun n => (n : ℝ)) ∧
      ∀ n ≥ 3, (f n : ℝ) ≤ 2^(n + r n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/107.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean#L155).

## `Erdos107.variants.hmpt_bound`

Solved: stated here without proof.

> The current best bound is due to Holmsen, Mojarrad, Pach, and Tardos [HMPT20],
> who prove
>
> $$
>   f(n) ≤ 2^{n+O(\sqrt{n\log n})}.
> $$
>
> [HMPT20] Holmsen, Andreas F. and Mojarrad, Hossein Nassajian and Pach, János and Tardos, Gábor,
>   _Two extensions of the Erdős-Szekeres problem_. J. Eur. Math. Soc. (JEMS) (2020), 3981-3995.

```lean
theorem hmpt_bound :
    ∃ r : ℕ → ℝ, r =O[atTop] (fun n => Real.sqrt (n * Real.log n)) ∧
      ∀ n ≥ 3, (f n : ℝ) ≤ 2^(n + r n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/107.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean#L171).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/107.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/107.lean)
- [erdosproblems.com/107](https://www.erdosproblems.com/107)
