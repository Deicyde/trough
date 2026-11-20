---
declaration: theorem
origin: cited
lean: Erdos401.erdos_401
statement: formalized
---

# Erdős Problem 401

> *References:*
> - [erdosproblems.com/401](https://www.erdosproblems.com/401)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).

*Quoted from [FormalConjectures/ErdosProblems/401.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/401.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/401](https://www.erdosproblems.com/401).

The file states 1 research or textbook statement: 1 solved.

## `Erdos401.erdos_401`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos401.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos401.lean).

> Is there some function $f(r)$ such that $f(r)\to \infty$ as $r\to\infty$, such that, for
> infinitely many $n$, there exist $a_1,a_2$ with
>
> $$a_1+a_2> n+f(r)\log n$$
>
> such that $a_1!a_2! \mid n!2^n3^n\cdots p_r^n$?
>
> It is ambiguous in [ErGr80] what the intended quantifiers are on the variables (they write 'is
> it true that we can find $a_1+a_2>n+f(r)\log n$...'). Comparing to previous problems such as
> [728] and [729] it seems most likely that they intended to ask the formulation in the problem
> statement.
>
> The answer is yes: Barreto and Leeham have used ChatGPT to provide a proof of the stated problem
> (in fact essentially the same construction as their solution to [729]).

```lean
theorem erdos_401 :
    ∃ f : ℕ → ℝ, Tendsto f atTop atTop ∧
      ∀ (r : ℕ) (hr : 1 ≤ r),
        {n : ℕ | ∃ a₁ a₂ : ℕ, 0 < a₁ ∧ 0 < a₂ ∧
          (a₁ : ℝ) + a₂ > n + f r * Real.log n ∧
          a₁.factorial * a₂.factorial ∣
            n.factorial * (∏ i ∈ Finset.range r, Nat.nth Nat.Prime i) ^ n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/401.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/401.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/401.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/401.lean)
- [erdosproblems.com/401](https://www.erdosproblems.com/401)
