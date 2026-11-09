---
declaration: theorem
origin: cited
lean: Bugeaud09.problem_10_9, Bugeaud09.problem_10_9.variants.measure_zero, Bugeaud09.problem_10_9.variants.dimH_lt_one
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Mahler's Z-numbers

> See also FormalConjectures/Wikipedia/Mahler32.lean.
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Mah68] Mahler, Kurt. "An unsolved problem on the powers of 3/2."
>     Journal of the Australian Mathematical Society 8.2 (1968): 313-321.
>   - [FLP95] Flatto, Leopold, Jeffrey C. Lagarias, and Andrew D. Pollington.
>     "On the range of fractional parts $\{\xi(p/q)^n\}$."
>     Acta Arithmetica 70.2 (1995): 125-147.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Bugeaud09.problem_10_9`

Open: stated without proof.

> Problem 10.9. There are no real numbers $\xi$ such that $0 \le \{\xi (3/2)^n\} < 1/2$
> for every positive integer $n$, i.e. no Z-number exists. Posed by Mahler [Mah68].

```lean
theorem problem_10_9 : type_of% Mahler32.mahler_conjecture
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean#L44).

## `Bugeaud09.problem_10_9.variants.measure_zero`

Solved: stated here without proof.

> Mahler [Mah68] proved that the set of Z-numbers has Lebesgue measure zero.

```lean
theorem problem_10_9.variants.measure_zero :
    MeasureTheory.volume {ξ : ℝ | IsZNumber ξ} = 0
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean#L64).

## `Bugeaud09.problem_10_9.variants.dimH_lt_one`

Solved: stated here without proof.

> Flatto, Lagarias, and Pollington [FLP95] proved that the set of Z-numbers has
> Hausdorff dimension strictly less than $1$.

```lean
theorem problem_10_9.variants.dimH_lt_one :
    dimH {ξ : ℝ | IsZNumber ξ} < 1
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_9.lean)
