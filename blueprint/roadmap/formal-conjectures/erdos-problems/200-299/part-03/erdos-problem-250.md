---
declaration: theorem
origin: cited
lean: Erdos250.erdos_250
statement: formalized
---

# Erdős Problem 250

> *Reference:* [erdosproblems.com/250](https://www.erdosproblems.com/250)

*Quoted from [FormalConjectures/ErdosProblems/250.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/250.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/250](https://www.erdosproblems.com/250).

The file states 1 research or textbook statement: 1 solved.

## `Erdos250.erdos_250`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos250.lean#L97](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos250.lean#L97).

> Is
> $$
>   \sum_{n=1}^\infty \frac{\sigma(n)}{2^n}
> $$
> irrational? Here $\sigma(n)$ is the sum of divisors function.
>
> The answer is yes, as shown by Nesterenko [Ne96].
>
> [Ne96] Nesterenko, Yu V., _Modular functions and transcendence questions_,
> Mat. Sb. 187 *9* (1996), 1319--1348.

```lean
theorem erdos_250  : (∀ x, HasSum (fun (n : ℕ) => σ 1 n / (2 : ℝ) ^ n) x → Irrational x)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/250.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/250.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/250.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/250.lean)
- [erdosproblems.com/250](https://www.erdosproblems.com/250)
