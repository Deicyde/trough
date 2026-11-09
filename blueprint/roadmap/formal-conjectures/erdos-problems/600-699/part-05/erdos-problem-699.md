---
declaration: theorem
origin: cited
lean: Erdos699.sylvester_schur, Erdos699.erdos_699, Erdos699.erdos_szekeres_strengthening
statement: formalized
---

# Erdős Problem 699

> *Reference:* [erdosproblems.com/699](https://www.erdosproblems.com/699)

*Quoted from [FormalConjectures/ErdosProblems/699.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/699.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/699](https://www.erdosproblems.com/699).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos699.sylvester_schur`

Solved: stated here; a Lean proof is at [https://github.com/AllenGrahamHart/FormalConjectures-Bench/blob/482dacc4d9335240f26218cdc62032da3100392b/formalizations/erdos699/Erdos699Formalization.lean#L7679](https://github.com/AllenGrahamHart/FormalConjectures-Bench/blob/482dacc4d9335240f26218cdc62032da3100392b/formalizations/erdos699/Erdos699Formalization.lean#L7679).

> Sylvester and Schur: for $1 \le i \le n/2$ there is a prime $p > i$ dividing `n.choose i`.

```lean
theorem sylvester_schur (n i : ℕ) (hi : 1 ≤ i) (hi_half : i ≤ n / 2) :
    ∃ p : ℕ, p.Prime ∧ i < p ∧ p ∣ Nat.choose n i
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/699.lean, line 33](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/699.lean#L33).

## `Erdos699.erdos_699`

Open: stated without proof.

> **Erdős Problem 699.** Is it true that for every $1 \le i < j \le n / 2$ there exists a prime
> $p \ge i$ with $p \mid \gcd\big(\binom{n}{i}, \binom{n}{j}\big)$?

```lean
theorem erdos_699 :
    ∀ n i j : ℕ,
      1 ≤ i →
      i < j →
      j ≤ n / 2 →
      ∃ p : ℕ, p.Prime ∧ i ≤ p ∧ p ∣ Nat.gcd (Nat.choose n i) (Nat.choose n j)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/699.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/699.lean#L42).

## `Erdos699.erdos_szekeres_strengthening`

Open: stated without proof.

> Erdős and Szekeres conjectured that, apart from a finite exceptional set of triples `(n, i, j)`,
> one can always take `p > i` in the prime divisor statement.

```lean
theorem erdos_szekeres_strengthening :
    ∃ E : Finset (ℕ × ℕ × ℕ), ∀ n i j : ℕ,
      1 ≤ i →
      i < j →
      j ≤ n / 2 →
      (n, i, j) ∉ E →
      ∃ p : ℕ, p.Prime ∧ i < p ∧ p ∣ Nat.gcd (Nat.choose n i) (Nat.choose n j)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/699.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/699.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/699.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/699.lean)
- [erdosproblems.com/699](https://www.erdosproblems.com/699)
