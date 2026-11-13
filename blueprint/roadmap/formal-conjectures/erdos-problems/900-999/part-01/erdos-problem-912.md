---
declaration: theorem
origin: cited
lean: Erdos912.erdos_912.variants.selfridge, Erdos912.erdos_912, Erdos912.erdos_912.variants.tao
statement: formalized
---

# Erdős Problem 912

> *References:*
>  - [erdosproblems.com/912](https://www.erdosproblems.com/912)
>  - [Er82c] Erdős, P., Miscellaneous problems in number theory. Congr. Numer. (1982), 25-45.

*Quoted from [FormalConjectures/ErdosProblems/912.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/912.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/912](https://www.erdosproblems.com/912).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos912.erdos_912.variants.selfridge`

Solved: stated here without proof.

> Erdős and Selfridge prove in [Er82c] that $h(n) \asymp \left(\frac{n}{\log n}\right)^{1/2}$.

```lean
theorem erdos_912.variants.selfridge :
    (fun n => (h n : ℝ)) =Θ[atTop] (fun n => (n / Real.log n) ^ (1 / 2 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/912.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/912.lean#L41).

## `Erdos912.erdos_912`

Open: stated without proof.

> Prove that there exists some $c>0$ such that
>
> $$h(n) \sim c \left(\frac{n}{\log n}\right)^{1/2}$$
>
> as $n\to \infty$.

```lean
theorem erdos_912 : ∃ c > 0,
    (fun n => (h n : ℝ)) ~[atTop] (fun n => c * (n / Real.log n) ^ (1 / 2 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/912.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/912.lean#L50).

## `Erdos912.erdos_912.variants.tao`

Open: stated without proof.

> A heuristic of Tao using the Cramér model for the primes suggests this is true with
> $c=\sqrt{2\pi}$.

```lean
theorem erdos_912.variants.tao :
    (fun n => (h n : ℝ)) ~[atTop] (fun n => √(2 * Real.pi) * (n / Real.log n) ^ (1 / 2 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/912.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/912.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/912.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/912.lean)
- [erdosproblems.com/912](https://www.erdosproblems.com/912)
