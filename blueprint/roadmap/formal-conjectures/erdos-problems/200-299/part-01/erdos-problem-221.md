---
declaration: theorem
origin: cited
lean: Erdos221.erdos_221
statement: formalized
---

# Erdős Problem 221

> *References:*
> - [erdosproblems.com/221](https://www.erdosproblems.com/221)
> - [Lo54] Lorentz, G. G., *On a problem of additive number theory*. Proc. Amer. Math. Soc. (1954), 838-841.
> - [Ru72] Ruzsa, Jr., I., *On a problem of P. Erdős*. Canad. Math. Bull. (1972), 309-310.

*Quoted from [FormalConjectures/ErdosProblems/221.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/221.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/221](https://www.erdosproblems.com/221).

The file states 1 research or textbook statement: 1 solved.

## `Erdos221.erdos_221`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem221.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem221.lean).

> Is there a set $A\subset\mathbb{N}$ such that, for all large $N$,
>
> $$\lvert A\cap\{1,\ldots,N\}\rvert \ll N/\log N$$
>
> and such that every large integer can be written as $2^k+a$ for some
> $k\geq 0$ and $a\in A$?
>
> Lorentz [Lo54] proved there is such a set with, for all large $N$,
>
> $$\lvert A\cap\{1,\ldots,N\}\rvert \ll \frac{\log\log N}{\log N}N$$
>
> The answer is yes, proved by Ruzsa [Ru72].

```lean
theorem erdos_221 :
    ∃ A : Set ℕ,
      ((fun N => ({a ∈ A | a ≤ N}.ncard : ℝ)) ≪ (fun N => (N : ℝ) / Real.log N)) ∧
      ∀ᶠ N in atTop, ∃ k a, 0 ≤ k ∧ a ∈ A ∧ N = 2 ^ k + a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/221.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/221.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/221.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/221.lean)
- [erdosproblems.com/221](https://www.erdosproblems.com/221)
