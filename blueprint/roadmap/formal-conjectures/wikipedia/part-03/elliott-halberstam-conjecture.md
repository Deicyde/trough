---
declaration: theorem
origin: cited
lean: ElliottHalberstamConjecture.elliott_halberstam, ElliottHalberstamConjecture.elliott_halberstam.variants.bombieri_vinogradov, ElliottHalberstamConjecture.elliott_halberstam.variants.friedlander_granville
statement: formalized
---

# Elliott–Halberstam conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Elliott%E2%80%93Halberstam_conjecture)
> - [EH68] Elliott, Peter D. T. A. and Halberstam, Heini, *A conjecture in prime number
>   theory*, Symposia Mathematica, Vol. IV (INDAM, Rome, 1968/69), 59–72.
> - [FG89] Friedlander, John and Granville, Andrew, *Limitations to the equi-distribution of
>   primes I*, Ann. of Math. (2) 129 (1989), no. 2, 363–382.

*Quoted from [FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `ElliottHalberstamConjecture.elliott_halberstam`

Open: stated without proof.

> The Elliott–Halberstam conjecture: for every $\theta < 1$ and $A > 0$ there exists a
> constant $C > 0$ such that
>
> $$\sum_{1 \le q \le x^{\theta}} E(x; q) \le \frac{C x}{\log^A x}$$
>
> for all $x > 2$.

```lean
theorem elliott_halberstam (θ : ℝ) (hθ : θ < 1) (A : ℝ) (hA : 0 < A) :
    ∃ C > (0 : ℝ), ∀ x : ℕ, 2 < x →
      ∑ q ∈ Finset.Icc 1 ⌊(x : ℝ) ^ θ⌋₊, E x q ≤ C * x / Real.log x ^ A
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean#L57).

## `ElliottHalberstamConjecture.elliott_halberstam.variants.bombieri_vinogradov`

Solved: stated here without proof.

> The Bombieri–Vinogradov theorem: the Elliott–Halberstam conjecture holds for every
> $\theta < 1/2$. This result may be regarded as an averaged form of the generalized
> Riemann hypothesis.

```lean
theorem elliott_halberstam.variants.bombieri_vinogradov (θ : ℝ) (hθ : θ < 1 / 2) (A : ℝ)
    (hA : 0 < A) :
    ∃ C > (0 : ℝ), ∀ x : ℕ, 2 < x →
      ∑ q ∈ Finset.Icc 1 ⌊(x : ℝ) ^ θ⌋₊, E x q ≤ C * x / Real.log x ^ A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean#L68).

## `ElliottHalberstamConjecture.elliott_halberstam.variants.friedlander_granville`

Solved: stated here without proof.

> The Elliott–Halberstam conjecture fails at the endpoint $\theta = 1$, as shown by
> Friedlander and Granville [FG89].

```lean
theorem elliott_halberstam.variants.friedlander_granville :
    ¬ ∀ A : ℝ, 0 < A → ∃ C > (0 : ℝ), ∀ x : ℕ, 2 < x →
      ∑ q ∈ Finset.Icc 1 x, E x q ≤ C * x / Real.log x ^ A
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ElliottHalberstamConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Elliott%E2%80%93Halberstam_conjecture)
