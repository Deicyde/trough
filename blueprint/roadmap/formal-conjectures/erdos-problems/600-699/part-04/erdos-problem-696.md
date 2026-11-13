---
declaration: theorem
origin: cited
lean: Erdos696.erdos_696
statement: formalized
---

# Erdős Problem 696

> *References:*
> * [erdosproblems.com/696](https://www.erdosproblems.com/696)
> * [Lean proof](https://github.com/davidturturean/erdos-696/blob/4fa1bf2c6ff6f2e0c7024f814614c7455404fdd3/Erdos696/Main.lean#L35), assuming
>   the Siegel-Walfisz theorem, the Brun-Titchmarsh inequality, and Mertens' theorem as custom axioms.

*Quoted from [FormalConjectures/ErdosProblems/696.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/696.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/696](https://www.erdosproblems.com/696).

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos696.erdos_696`

Solved: stated here without proof.

> Is it true that $H(n)/h(n)\to \infty$ for almost all $n$?
>
> Formalised as: for every threshold $M$, the set of $n$ with $h(n) > 0$ and $H(n)/h(n) > M$
> has natural density $1$. This is false: in fact, $H(n)/h(n) = 2 + o(1)$ for almost all $n$.

```lean
theorem erdos_696 :
    ¬ ∀ M : ℝ,
      {n : ℕ | (h n : ℝ) > 0 ∧ (H n : ℝ) / (h n : ℝ) > M}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/696.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/696.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/696.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/696.lean)
- [erdosproblems.com/696](https://www.erdosproblems.com/696)
