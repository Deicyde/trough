---
declaration: theorem
origin: cited
lean: Erdos264.erdos_264.parts.i, Erdos264.erdos_264.parts.ii, Erdos264.erdos_264.variants.example, Erdos264.erdos_264.variants.ko_tao_neg, Erdos264.erdos_264.variants.ko_tao_pos
statement: formalized
---

# Erdős Problem 264

> *Reference:* [erdosproblems.com/264](https://www.erdosproblems.com/264)

*Quoted from [FormalConjectures/ErdosProblems/264.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/264](https://www.erdosproblems.com/264).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos264.erdos_264.parts.i`

Solved: stated here without proof.

> Is $2^n$ an example of an irrationality sequence? Kovač and Tao proved that it is not [KoTa24]
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).

```lean
theorem erdos_264.parts.i : ¬IsIrrationalitySequence (2 ^ ·)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/264.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean#L56).

## `Erdos264.erdos_264.parts.ii`

Open: stated without proof.

> Is $n!$ an example of an irrationality sequence?

```lean
theorem erdos_264.parts.ii : IsIrrationalitySequence Nat.factorial
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/264.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean#L62).

## `Erdos264.erdos_264.variants.example`

Solved: stated here without proof.

> One example is $2^{2^n}$.

```lean
theorem erdos_264.variants.example : IsIrrationalitySequence (fun n ↦ 2 ^ (2 ^ n))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/264.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean#L68).

## `Erdos264.erdos_264.variants.ko_tao_neg`

Solved: stated here without proof.

> Kovač and Tao [KoTa24] generally proved that any strictly increasing sequence of positive integers
> $a_n$ such that $\sum \frac{1}{a_n}$ converges and
> $$
>   \liminf_{n \to \infty} (a_n^2 \sum_{k > n} \frac{1}{a_k^2}) > 0
> $$
> is not an irrationality sequence.
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).

```lean
theorem erdos_264.variants.ko_tao_neg {a : ℕ → ℕ} (h₁ : StrictMono a) (h₂ : 0 ∉ Set.range a)
    (h₃ : Summable ((1 : ℝ) / a ·))
    (h₄ : ∃ C > 0, ∀ᶠ n in atTop, C ≤ a n ^ 2 * ∑' k : Set.Ioi n, (1 : ℝ) / a k ^ 2) :
    ¬IsIrrationalitySequence a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/264.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean#L81).

## `Erdos264.erdos_264.variants.ko_tao_pos`

Solved: stated here without proof.

> On the other hand, Kovač and Tao [KoTa24] do prove that for any function $F$ with
> $\lim_{n \to \infty} \frac{F(n + 1)}{F(n)} = \infty$ there exists such an irrationality sequence with $a_n \sim F(n)$.
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).

```lean
theorem erdos_264.variants.ko_tao_pos {F : ℕ → ℕ}
    (hF : atTop.Tendsto (fun n ↦ (F (n + 1) : ℝ) / F n) atTop) :
    ∃ a : ℕ → ℕ, IsIrrationalitySequence a ∧ (fun n ↦ (a n : ℝ)) ~[atTop] fun n ↦ (F n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/264.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/264.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/264.lean)
- [erdosproblems.com/264](https://www.erdosproblems.com/264)
