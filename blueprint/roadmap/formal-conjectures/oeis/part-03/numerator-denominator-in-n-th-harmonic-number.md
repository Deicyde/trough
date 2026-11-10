---
declaration: theorem
origin: cited
lean: OeisA64169.conjecture
statement: formalized
---

# Numerator - denominator in $n$-th harmonic number

> $a(n) = \text{numerator}(H_n) - \text{denominator}(H_n)$, where
> $H_n = 1 + 1/2 + \dots + 1/n$.
>
> *References:*
> - [A064169](https://oeis.org/A064169)

*Quoted from [FormalConjectures/OEIS/64169.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/64169.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA64169.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_64169_conjecture_0/Submission/Spec.lean#L514](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_64169_conjecture_0/Submission/Spec.lean#L514).

> "Conjecture: for $n > 2$, $n$ divides $a(n-2)$ if and only if $n$ is a prime.
> Checked up to 20000. - _Amiram Eldar_ and _Thomas Ordowski_, Jul 27 2019
>
> This is false for the composite number $16843^2$.

```lean
theorem conjecture : ¬ ∀ (n : ℕ), 2 < n → ((n : ℤ) ∣ a (n - 2) ↔ n.Prime)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/64169.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/64169.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/64169.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/64169.lean)
- [A064169](https://oeis.org/A064169)
