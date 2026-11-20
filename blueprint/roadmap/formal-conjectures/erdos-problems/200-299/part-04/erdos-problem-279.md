---
declaration: theorem
origin: cited
lean: Erdos279.erdos_279
statement: formalized
---

# Erdős Problem 279

> *Reference:* [erdosproblems.com/279](https://www.erdosproblems.com/279)

*Quoted from [FormalConjectures/ErdosProblems/279.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/279.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/279](https://www.erdosproblems.com/279).

The file states 1 research or textbook statement: 1 open.

## `Erdos279.erdos_279`

Open: stated without proof.

> Let $k\geq 3$. Is there a choice of congruence classes $a_p\pmod{p}$ for every prime $p$
> such that all sufficiently large integers can be written as $a_p+tp$ for some prime $p$
> and integer $t\geq k$?

```lean
theorem erdos_279 :  ∀ k : Nat, k ≥ 3 →
    ∃ a : Nat → Nat, ∃ N : Nat, (∀ p : Nat, p.Prime → a p < p) ∧
    ∀ n ≥ N, ∃ p : Nat, ∃ t ≥ k, p.Prime ∧ n = a p + t * p
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/279.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/279.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/279.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/279.lean)
- [erdosproblems.com/279](https://www.erdosproblems.com/279)
