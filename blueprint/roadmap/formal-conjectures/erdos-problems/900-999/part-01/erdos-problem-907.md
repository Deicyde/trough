---
declaration: theorem
origin: cited
lean: Erdos907.erdos_907
statement: formalized
---

# Erdős Problem 907

> *References:*
> - [erdosproblems.com/907](https://www.erdosproblems.com/907)
> - [dB51] de Bruijn, N. G., *Functions whose differences belong to a given class*. Nieuw Arch.
>   Wiskunde (2) (1951), 194-218.

*Quoted from [FormalConjectures/ErdosProblems/907.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/907.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/907](https://www.erdosproblems.com/907).

The file states 1 research or textbook statement: 1 solved.

## `Erdos907.erdos_907`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos907.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos907.lean).

> Let $f:\mathbb{R}\to \mathbb{R}$ be such that $f(x+h)-f(x)$ is continuous for every $h>0$. Is it
> true that
>
> $$f=g+h$$
>
> for some continuous $g$ and additive $h$ (i.e. $h(x+y)=h(x)+h(y)$)?
>
> A conjecture of Erdős from the early 1950s. Answered in the affirmative by de Bruijn [dB51].

```lean
theorem erdos_907 :
    ∀ f : ℝ → ℝ, (∀ h : ℝ, 0 < h → Continuous fun x => f (x + h) - f x) →
      ∃ g a : ℝ → ℝ, Continuous g ∧ (∀ x y, a (x + y) = a x + a y) ∧ f = g + a
```

Category `research solved`; AMS [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md), [39 Difference and functional equations](../../../by-subject/part-02/39-difference-and-functional-equations/README.md). Declared in [FormalConjectures/ErdosProblems/907.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/907.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/907.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/907.lean)
- [erdosproblems.com/907](https://www.erdosproblems.com/907)
