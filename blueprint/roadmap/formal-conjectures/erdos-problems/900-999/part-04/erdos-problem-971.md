---
declaration: theorem
origin: cited
lean: Erdos971.erdos_971, Erdos971.erdos_971.variants.infinite_sequence, Erdos971.erdos_971.variants.many_small
statement: formalized
---

# Erdős Problem 971

> *Reference:* [erdosproblems.com/971](https://www.erdosproblems.com/971)

*Quoted from [FormalConjectures/ErdosProblems/971.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/971.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/971](https://www.erdosproblems.com/971).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos971.erdos_971`

Open: stated without proof.

> Let `p(a, d)` be the least prime congruent to `a (mod d)`.
> Does there exist a constant `c > 0` such that for all large `d`,
> `p(a, d) > (1 + c) * φ(d) * log d` for `≫ φ(d)` many values of `a`?

```lean
theorem erdos_971 :
    ∃ c > (0 : ℝ), ∃ C > (0 : ℝ), ∀ᶠ d in atTop,
      C * (d.totient : ℝ) ≤
        #{a < d | a.Coprime d ∧ (leastCongruentPrime a d : ℝ) > (1 + c) * d.totient * log d}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/971.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/971.lean#L42).

## `Erdos971.erdos_971.variants.infinite_sequence`

Solved: stated here without proof.

> Erdős [Er49c] proved that the statement in `erdos_971` holds for infinitely many values of `d`.
>
> [Er49c] Erdős, P., _On some applications of Brun's method_. Acta Univ. Szeged. Sect. Sci. Math.
> (1949), 57--63.

```lean
theorem erdos_971.variants.infinite_sequence :
    ∃ c > (0 : ℝ), ∃ C > (0 : ℝ),
      {d : ℕ | C * (d.totient : ℝ) ≤
        #{a < d | a.Coprime d ∧ (leastCongruentPrime a d : ℝ) > (1 + c) * d.totient * log d}}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/971.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/971.lean#L55).

## `Erdos971.erdos_971.variants.many_small`

Solved: stated here without proof.

> Erdős [Er49c] proved that for any `ε > 0` we have `p(a, d) < ε * φ(d) * log d` for `≫_ε φ(d)` many
> values of `a` (for all large `d`).
>
> [Er49c] Erdős, P., _On some applications of Brun's method_. Acta Univ. Szeged. Sect. Sci. Math.
> (1949), 57--63.

```lean
theorem erdos_971.variants.many_small :
    ∀ ε > (0 : ℝ), ∃ C > (0 : ℝ), ∀ᶠ d in atTop,
      C * (d.totient : ℝ) ≤
        #{a < d | a.Coprime d ∧ (leastCongruentPrime a d : ℝ) < ε * d.totient * log d}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/971.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/971.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/971.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/971.lean)
- [erdosproblems.com/971](https://www.erdosproblems.com/971)
