---
declaration: theorem
origin: cited
lean: Erdos69.erdos_69, Erdos69.erdos_69.variants.specialisation_of_erdos_257
statement: formalized
---

# Erdős Problem 69

> *Reference:* [erdosproblems.com/69](https://www.erdosproblems.com/69)

*Quoted from [FormalConjectures/ErdosProblems/69.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/69.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/69](https://www.erdosproblems.com/69).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos69.erdos_69`

Textbook result, stated without proof.

> Is
>
> $$
> \sum_{n\geq 2}\frac{\omega(n)}{2^n}
> $$
>
> irrational? (Here $\omega(n)$ counts the number of distinct prime divisors of $n$.)

```lean
theorem erdos_69 : Irrational <| ∑' n, ω (n + 2) / 2 ^ (n + 2)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/69.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/69.lean#L40).

## `Erdos69.erdos_69.variants.specialisation_of_erdos_257`

Proved here.

> Tao observed that `erdos_69` is a special case of `erdos_257`, since
>
> $$
> \sum_{n\geq 2}\frac{\omega(n)}{2^n} = \sum_p \frac{1}{2^p - 1}.
> $$

```lean
theorem erdos_69.variants.specialisation_of_erdos_257 :
    let A := { n : ℕ | n.Prime }
    ∑' n, ω (n + 2) / (2 ^ (n + 2) : ℝ) = ∑' p : A, 1 / (2 ^ p.1 - 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/69.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/69.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/69.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/69.lean)
- [erdosproblems.com/69](https://www.erdosproblems.com/69)
