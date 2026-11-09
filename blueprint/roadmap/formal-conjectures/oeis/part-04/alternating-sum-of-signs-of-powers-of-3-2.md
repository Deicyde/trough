---
declaration: theorem
origin: cited
lean: OeisA71532.conjecture1, OeisA71532.conjecture2, OeisA71532.conjecture3, OeisA71532.conjecture3_value
statement: formalized
---

# Alternating sum of signs of powers of $3/2$

> The sequence $a(n) = -\sum_{k=1}^n (-1)^{\lfloor (3/2)^k \rfloor}$.
>
> *References:*
> - [A071532](https://oeis.org/A071532)

*Quoted from [FormalConjectures/OEIS/71532.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA71532.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/SamuelSchlesinger/a071532-counterexample/blob/818c9f6b3f1eed9ebd1b3b9481848dc21f3e3243/Counterexample.lean#L28-L35](https://github.com/SamuelSchlesinger/a071532-counterexample/blob/818c9f6b3f1eed9ebd1b3b9481848dc21f3e3243/Counterexample.lean#L28-L35).

> "Is $a(n)>0$?"
>
> The answer is negative: $a(331523) = -1$. The restriction $n > 2$ excludes the initial
> zero $a(2) = 0$.
>
> The counterexample and formal proof were developed by Codex (GPT-6), prompted by
> Samuel Schlesinger.

```lean
theorem conjecture1 : ¬ ∀ n : ℕ, 2 < n → 0 < a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/71532.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean#L76).

## `OeisA71532.conjecture2`

Open: stated without proof.

> For $n$ large enough, does $a(n) > \sqrt{n}$ always hold?

```lean
theorem conjecture2 :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n → (a n : ℝ) > Real.sqrt (n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/71532.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean#L83).

## `OeisA71532.conjecture3`

Open: stated without proof.

> Conjecture: asymptotically, $a(n) \sim C \log(n)^2$ for some constant $C > 0$.

```lean
theorem conjecture3 :
    ∃ C : ℝ, 0 < C ∧ (fun n : ℕ ↦ (a n : ℝ)) ~[atTop] (fun n : ℕ ↦ C * Real.log (n : ℝ) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/71532.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean#L91).

## `OeisA71532.conjecture3_value`

Open: stated without proof.

> Conjecture: the constant $C$ in $a(n) \sim C \log(n)^2$ is approximately $1.4$.

```lean
theorem conjecture3_value :
    |conjecture3_value.answer - 1.4| < 0.1 ∧
      (fun n : ℕ ↦ (a n : ℝ)) ~[atTop] (fun n : ℕ ↦ conjecture3_value.answer * Real.log (n : ℝ) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/71532.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/71532.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71532.lean)
- [A071532](https://oeis.org/A071532)
