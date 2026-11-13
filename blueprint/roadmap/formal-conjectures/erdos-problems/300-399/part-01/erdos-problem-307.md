---
declaration: theorem
origin: cited
lean: Erdos307.erdos_307, Erdos307.erdos_307.variants.coprime, Erdos307.erdos_307.variants.coprime_one_notMem, Erdos307.erdos_307.barrier, Erdos307.erdos_307.barrier_sixty
statement: formalized
---

# Erdős Problem 307

> *Reference:* [erdosproblems.com/307](https://www.erdosproblems.com/307)

*Quoted from [FormalConjectures/ErdosProblems/307.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/307](https://www.erdosproblems.com/307).

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result.

## `Erdos307.erdos_307`

Open: stated without proof.

> Are there two finite set of primes $P$ and $Q$ such that
>
> $$
> 1 = \left( \sum_{p \in P} \frac{1}{p} \right) \left( \sum_{q \in Q} \frac{1}{q} \right)
> $$
>
> ?
>
> Asked by Barbeau [Ba76].
>
> [Ba76] Barbeau, E. J., _Computer challenge corner: Problem 477: A brute force program._

```lean
theorem erdos_307 : ∃ P Q : Finset ℕ, (∀ p ∈ P, p.Prime) ∧ (∀ q ∈ Q, q.Prime) ∧
    1 = (∑ p ∈ P, (p : ℚ)⁻¹) * (∑ q ∈ Q, (q : ℚ)⁻¹)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/307.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean#L45).

## `Erdos307.erdos_307.variants.coprime`

Textbook result, proved here.

> Instead of asking for sets of primes, ask only that all elements in the sets be relatively coprime.
>
> Cambie has found several examples when this weakened version is true. For example,
>
> $$
> 1=\left(1+\frac{1}{5}\right)\left(\frac{1}{2}+\frac{1}{3}\right)
> $$
>
> and
>
> $$
> 1=\left(1+\frac{1}{41}\right)\left(\frac{1}{2}+\frac{1}{3}+\frac{1}{7}\right).
> $$

```lean
theorem erdos_307.variants.coprime : ∃ P Q : Finset ℕ, 0 ∉ P ∩ Q ∧ 1 < #P ∧ 1 < #Q ∧
    Set.Pairwise P Nat.Coprime ∧ Set.Pairwise Q Nat.Coprime ∧
    1 = (∑ p ∈ P, (p : ℚ)⁻¹) * (∑ q ∈ Q, (q : ℚ)⁻¹)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/307.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean#L62).

## `Erdos307.erdos_307.variants.coprime_one_notMem`

Open: stated without proof.

> There are no examples known of the weakened coprime version if we insist that $1\not\in P\cup Q$.

```lean
theorem erdos_307.variants.coprime_one_notMem : ∃ P Q : Finset ℕ, 0 ∉ P ∩ Q ∧ 1 ∉ P ∪ Q ∧
    1 < #P ∧ 1 < #Q ∧ Set.Pairwise P Nat.Coprime ∧ Set.Pairwise Q Nat.Coprime ∧
    1 = (∑ p ∈ P, (p : ℚ)⁻¹) * (∑ q ∈ Q, (q : ℚ)⁻¹)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/307.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean#L73).

## `Erdos307.erdos_307.barrier`

Solved: stated here; a Lean proof is at [https://github.com/ElVec1o/erdos307/blob/76d242b024102f32d8411c714be4ad140a8b7c4b/lean/Erdos307/Closed.lean#L121](https://github.com/ElVec1o/erdos307/blob/76d242b024102f32d8411c714be4ad140a8b7c4b/lean/Erdos307/Closed.lean#L121).

> A machine-checked **barrier** for Erdős 307 (Bonfioli, 2026): any solution with `Q` nonempty uses at
> least 59 primes in total, and `(∏_{p ∈ P} p)² ≥ 4·10¹¹²` — i.e. `∏_{p ∈ P} p ≥ 2·10⁵⁶` (and, by
> symmetry, the same for `∏ Q`); so no solution lies below a prime-product of `2.09·10⁵⁶`. The full
> `sorry`-free proof is in the linked repository (`Closed.lean`): the left conjunct is `card_ge_59`,
> the right is `erdos307_barrier_closed`. Both depend on `propext, Classical.choice, Quot.sound` and
> nothing further: the evaluation of the first 59 primes is kernel-checked by `decide`, so no
> `native_decide` enters this statement.

```lean
theorem erdos_307.barrier {P Q : Finset ℕ}
    (hP : ∀ p ∈ P, p.Prime) (hQ : ∀ q ∈ Q, q.Prime) (hQne : Q.Nonempty)
    (heq : 1 = (∑ p ∈ P, (p : ℚ)⁻¹) * (∑ q ∈ Q, (q : ℚ)⁻¹)) :
    59 ≤ #(P ∪ Q) ∧ (4 * 10 ^ 112 : ℚ) ≤ (∏ p ∈ P, (p : ℚ)) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/307.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean#L90).

## `Erdos307.erdos_307.barrier_sixty`

Solved: stated here; a Lean proof is at [https://github.com/ElVec1o/erdos307/blob/080164a8db2eeb20f65c362894ec93f12448609a/lean/Erdos307/Sixty.lean#L367](https://github.com/ElVec1o/erdos307/blob/080164a8db2eeb20f65c362894ec93f12448609a/lean/Erdos307/Sixty.lean#L367).

> A stronger machine-checked **barrier** (Bonfioli, 2026), closing the 59-prime level: any solution of
> Erdős 307 in fact uses at least `60` primes in total. The full `sorry`-free proof is `erdos307_sixty`
> in the linked repository (`Sixty.lean` at tag `v1.1.1`); its only non-logical input is a `native_decide`
> depth-first search establishing that no admissible 59-prime support survives the Pythagorean
> `plus`-value square test, with axioms `propext, Classical.choice, Quot.sound` together with that
> `native_decide`.

```lean
theorem erdos_307.barrier_sixty {P Q : Finset ℕ}
    (hP : ∀ p ∈ P, p.Prime) (hQ : ∀ q ∈ Q, q.Prime)
    (heq : 1 = (∑ p ∈ P, (p : ℚ)⁻¹) * (∑ q ∈ Q, (q : ℚ)⁻¹)) :
    60 ≤ #(P ∪ Q)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/307.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/307.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/307.lean)
- [erdosproblems.com/307](https://www.erdosproblems.com/307)
