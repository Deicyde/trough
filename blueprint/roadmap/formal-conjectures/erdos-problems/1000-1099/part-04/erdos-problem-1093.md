---
declaration: theorem
origin: cited
lean: Erdos1093.erdos_1093.parts.i, Erdos1093.erdos_1093.parts.ii
statement: formalized
---

# Erdős Problem 1093

> *Reference:* [erdosproblems.com/1093](https://www.erdosproblems.com/1093)

*Quoted from [FormalConjectures/ErdosProblems/1093.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1093.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1093](https://www.erdosproblems.com/1093).

The file states 2 research or textbook statements: 2 open.

## `Erdos1093.erdos_1093.parts.i`

Open: stated without proof.

> Are there infinitely many binomial coefficients with deficiency 1?

```lean
theorem erdos_1093.parts.i :
    {x : ℕ × ℕ | let k := x.1; let n := x.2; 2 * k ≤ n ∧ deficiency n k = 1 ∧
      ∀ p, p.Prime → (p ∣ choose n k) → k < p}.Infinite
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1093.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1093.lean#L46).

## `Erdos1093.erdos_1093.parts.ii`

Open: stated without proof.

> Are there only finitely many binomial coefficients with deficiency > 1?

```lean
theorem erdos_1093.parts.ii :
    {x : ℕ × ℕ | let k := x.1; let n := x.2; 2 * k ≤ n ∧ deficiency n k > 1 ∧
      ∀ p, p.Prime → (p ∣ choose n k) → k < p}.Finite
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1093.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1093.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1093.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1093.lean)
- [erdosproblems.com/1093](https://www.erdosproblems.com/1093)
