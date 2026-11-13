---
declaration: theorem
origin: cited
lean: Erdos648.erdos_648
statement: formalized
---

# Erdős Problem 648

> *References:*
> - [erdosproblems.com/648](https://www.erdosproblems.com/648)
> - [Er95c] Erdős, Paul, *Some problems in number theory*. Octogon Math. Mag. (1995), 3-5.
> - [Ca25b] S. Cambie, *On Erdős problem #648*. arXiv:2503.22691 (2025).

*Quoted from [FormalConjectures/ErdosProblems/648.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/648.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/648](https://www.erdosproblems.com/648).

The file states 1 research or textbook statement: 1 solved.

## `Erdos648.erdos_648`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos648.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos648.lean).

> Let $g(n)$ denote the largest $t$ such that there exist integers $2\leq a_1\lt a_2\lt \cdots \lt a_t \lt n$
> such that
>
> $$P(a_1)>P(a_2)>\cdots >P(a_t)$$
>
> where $P(m)$ is the greatest prime factor of $m$.
> Estimate $g(n)$.
>
> Stijn Cambie has proved [Ca25b]
>
> $$g(n) \asymp \left(\frac{n}{\log n}\right)^{1/2}.$$
>
> Cambie further asks whether there exists a constant $c$ such that
>
> $$g(n) \sim c \left(\frac{n}{\log n}\right)^{1/2}.$$
>
> Cambie's proof shows that such a $c$ must satisfy $2\leq c\leq 2\sqrt{2}$.
>
> The sequence $a_1\lt a_2\lt \cdots\lt a_t$ is packaged as a strictly monotone map `a : Fin t → ℕ`
> with $2\leq a_i\lt n$, the greatest prime factor $P$ is `Nat.maxPrimeFac`, and $g(n)$ is the
> supremum in `ℕ` of the achievable lengths $t$.

```lean
theorem erdos_648 :
    (fun n => (g n : ℝ)) =Θ[atTop] fun n => Real.sqrt ((n : ℝ) / Real.log (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/648.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/648.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/648.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/648.lean)
- [erdosproblems.com/648](https://www.erdosproblems.com/648)
