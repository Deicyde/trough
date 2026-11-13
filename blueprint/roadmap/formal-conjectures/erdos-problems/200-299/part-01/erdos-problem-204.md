---
declaration: theorem
origin: cited
lean: Erdos204.erdos_204
statement: formalized
---

# Erdős Problem 204

> *References:*
> - [erdosproblems.com/204](https://www.erdosproblems.com/204)
> - [Ad25] S. Adenwalla, A Question of Erdős and Graham on Covering Systems. arXiv:2501.15170 (2025).

*Quoted from [FormalConjectures/ErdosProblems/204.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/204.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/204](https://www.erdosproblems.com/204).

The file states 1 research or textbook statement: 1 solved.

## `Erdos204.erdos_204`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem204.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem204.lean).

> Are there $n$ such that there is a covering system with moduli the divisors of $n$ which is 'as
> disjoint as possible'?
>
> That is, for all $d\mid n$ with $d>1$ there is an associated $a_d$ such that every integer is
> congruent to some $a_d\pmod{d}$, and if there is some integer $x$ with
>
> $$x\equiv a_d\pmod{d}\textrm{ and }x\equiv a_{d'}\pmod{d'}$$
>
> then $(d,d')=1$.
>
> The density of such $n$ is zero. Erdős and Graham believed that no such $n$ exist.
>
> Adenwalla [Ad25] has proved there are no such $n$.
>
> This was formalized by van Doorn in Lean using Aristotle.

```lean
theorem erdos_204 : ¬ ∃ (n : ℕ) (a : ℕ → ℤ),
    let D := {d : ℕ | d ∣ n ∧ d > 1}
    (∀ x : ℤ, ∃ d ∈ D, x ≡ a d [ZMOD d]) ∧
    (∀ d ∈ D, ∀ d' ∈ D, d ≠ d' → (∃ x : ℤ, x ≡ a d [ZMOD d] ∧ x ≡ a d' [ZMOD d']) →
      Nat.gcd d d' = 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/204.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/204.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/204.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/204.lean)
- [erdosproblems.com/204](https://www.erdosproblems.com/204)
