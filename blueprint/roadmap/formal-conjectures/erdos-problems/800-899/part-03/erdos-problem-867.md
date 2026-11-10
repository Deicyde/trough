---
declaration: theorem
origin: cited
lean: Erdos867.erdos_867, Erdos867.erdos_867.variants.lower_bound, Erdos867.erdos_867.variants.adenwalla, Erdos867.erdos_867.variants.freud, Erdos867.erdos_867.variants.coppersmith_phillips_lower_bound, Erdos867.erdos_867.variants.coppersmith_phillips_upper_bound
statement: formalized
---

# Erdős Problem 867

> *References:*
> - [erdosproblems.com/867](https://www.erdosproblems.com/867)
> - [CoPh96] Coppersmith, Don and Phillips, Steven, *On a question of Erdős on subsequence sums*.
>   SIAM J. Discrete Math. (1996), 173-177.
> - [Fr93] Freud, R., *Adding numbers - on a problem of P. Erdős*. James Cook Mathematical
>   Notes (1993), 6199-6202.

*Quoted from [FormalConjectures/ErdosProblems/867.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/867](https://www.erdosproblems.com/867).

The file states 6 research or textbook statements: 6 solved.

## `Erdos867.erdos_867`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos867.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos867.lean).

> Is it true that if $A=\{a_1\lt \cdots \lt a_t\}\subseteq \{1,\ldots,N\}$ has no solutions to
>
> $$a_i+a_{i+1}+\cdots+a_j\in A$$
>
> then
>
> $$\lvert A\rvert \leq \frac{N}{2}+O(1)?$$
>
> In fact this problem is false. Freud [Fr93] constructed a sequence with density $\geq 19/36$.
> The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
> maximal size of such an $A$ satisfies
>
> $$\frac{13}{24}N -O(1)\leq \lvert A\rvert \leq \left(\frac{2}{3}-\frac{1}{512}\right)N+\log N.$$

```lean
theorem erdos_867 :
    ¬ ∃ C : ℝ, ∀ N : ℕ, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (N : ℝ) / 2 + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L57).

## `Erdos867.erdos_867.variants.lower_bound`

Proved here.

> Taking $A=(N/2,N]\cap \mathbb{N}$ shows $\lvert A\rvert \geq N/2-O(1)$ is possible.

```lean
theorem erdos_867.variants.lower_bound :
    ∃ C : ℝ, ∀ N : ℕ, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      ((N : ℝ) / 2 - C ≤ (A.card : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L66).

## `Erdos867.erdos_867.variants.adenwalla`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos867_erdos_867_variants_adenwalla.lean#L262](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos867_erdos_867_variants_adenwalla.lean#L262).

> Adenwalla has observed that
>
> $$\lvert A\rvert \leq (\tfrac{2}{3}+o(1))N.$$

```lean
theorem erdos_867.variants.adenwalla (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (2 / 3 + ε) * (N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L100).

## `Erdos867.erdos_867.variants.freud`

Solved: stated here without proof.

> Freud [Fr93] constructed a sequence with density $\geq 19/36$.

```lean
theorem erdos_867.variants.freud :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      (((19 / 36 : ℝ) - ε) * (N : ℝ) ≤ (A.card : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L109).

## `Erdos867.erdos_867.variants.coppersmith_phillips_lower_bound`

Solved: stated here without proof.

> The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
> maximal size of such an $A$ satisfies
>
> $$\frac{13}{24}N -O(1)\leq \lvert A\rvert.$$

```lean
theorem erdos_867.variants.coppersmith_phillips_lower_bound :
    ∃ C : ℝ, ∀ N : ℕ, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      ((13 / 24 : ℝ) * (N : ℝ) - C ≤ (A.card : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L120).

## `Erdos867.erdos_867.variants.coppersmith_phillips_upper_bound`

Solved: stated here without proof.

> The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
> maximal size of such an $A$ satisfies
>
> $$\lvert A\rvert \leq \left(\frac{2}{3}-\frac{1}{512}\right)N+\log N.$$

```lean
theorem erdos_867.variants.coppersmith_phillips_upper_bound :
    ∀ᶠ N : ℕ in atTop, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (2 / 3 - 1 / 512) * (N : ℝ) + Real.log (N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/867.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/867.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/867.lean)
- [erdosproblems.com/867](https://www.erdosproblems.com/867)
