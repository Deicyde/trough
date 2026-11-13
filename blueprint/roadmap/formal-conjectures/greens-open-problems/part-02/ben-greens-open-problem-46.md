---
declaration: theorem
origin: cited
lean: Green46.green_46.improve_lower, Green46.green_46.improve_upper, Green46.green_46.improve_upper_conjectured, Green46.green_46.variants.lower, Green46.green_46.variants.upper
statement: formalized
---

# Ben Green's Open Problem 46

> What is the largest $y$ for which one may cover the interval $[y]$ by residue classes $a_p \pmod{p}$, one for each prime $p \leq x$?
>
> *References:*
> - [Gr24] [Ben Green's Open Problem 46](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.46)
> - [FGK18] Ford, K., Green, B., Konyagin, S., Maynard, J., & Tao, T. (2018). Long gaps between primes.
>   Journal of the American Mathematical Society, 31(1), 65-105.
> - [Iw78] Iwaniec, Henryk. "On the problem of Jacobsthal." Demonstratio Mathematica 11.1 (1978): 225-232.
> - [OAI26a] OpenAI, *A quadratic bound for Jacobsthal's function*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf
> - [Ra38] Rankin, R. A., *The difference between consecutive prime numbers*. J. London Math. Soc.
>   (1938), 242--247.
>
> This is the same problem as Erdős Problem 687.

*Quoted from [FormalConjectures/GreensOpenProblems/46.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Green46.green_46.improve_lower`

Open: stated without proof.

> We conjecture that the best-known lower bound can be improved.

```lean
theorem green_46.improve_lower :
    (bestLower =o[atTop] green_46.improve_lower.answer) ∧ (green_46.improve_lower.answer ≪ maxY)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/46.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean#L66).

## `Green46.green_46.improve_upper`

Solved: stated here; a Lean proof is at [https://github.com/30k30/scholia/blob/b072c89c3edac06521868e32cc15b2bc91bd8533/erdos-687/glue/JacobsthalTo687.lean#L319](https://github.com/30k30/scholia/blob/b072c89c3edac06521868e32cc15b2bc91bd8533/erdos-687/glue/JacobsthalTo687.lean#L319).

> We conjecture that the best-known upper bound can be improved.
>
> Yes. OpenAI [OAI26a] proved $h(k) \ll k^2 / (\log\log 3k)^2$ for Jacobsthal's function $h$
> (Erdős Problem 970). By the Chinese remainder theorem $\mathrm{maxY}(x) < h(\pi(x))$, which gives
> $\mathrm{maxY}(x) \ll (x+1)^2 / (\log\log 3(x+1))^2 = o(x^2)$. Whether $y \ll x^{1+o(1)}$ remains
> open, see `green_46.improve_upper_conjectured`.

```lean
theorem green_46.improve_upper :
    (green_46.improve_upper.answer =o[atTop] bestUpper) ∧ (maxY ≪ green_46.improve_upper.answer)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/46.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean#L83).

## `Green46.green_46.improve_upper_conjectured`

Open: stated without proof.

> It seems very likely that we must have $y \ll x^{1+o(1)}$ [Gr24].

```lean
theorem green_46.improve_upper_conjectured :
    ∃ o : ℕ → ℝ, (o =o[atTop] fun _ : ℕ ↦ (1 : ℝ)) ∧
      maxY ≪ fun x ↦ (x : ℝ) ^ (1 + o x)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/46.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean#L90).

## `Green46.green_46.variants.lower`

Solved: stated here without proof.

> Best known lower bound: $y \gg x \frac{\log x \log \log \log x}{\log \log x}$ [FGK18].

```lean
theorem green_46.variants.lower :
    bestLower ≪ maxY
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/46.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean#L97).

## `Green46.green_46.variants.upper`

Solved: stated here without proof.

> Best known upper bound: $y \ll x^2$ [Iw78].

```lean
theorem green_46.variants.upper :
    maxY ≪ bestUpper
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/46.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/46.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/46.lean)
- [Ben Green's Open Problem 46](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.46)
