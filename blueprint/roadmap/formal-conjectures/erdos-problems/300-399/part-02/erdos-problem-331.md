---
declaration: theorem
origin: cited
lean: Erdos331.erdos_331, Erdos331.erdos_331.variants.ruzsa
statement: formalized
---

# Erdős Problem 331

> *References:*
> - [erdosproblems.com/331](https://www.erdosproblems.com/331)
> - [ErFr84] Erdős, P. and Freud, R., On disjoint sets of differences. J. Number Theory (1984),
>   99--109.

*Quoted from [FormalConjectures/ErdosProblems/331.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/331.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/331](https://www.erdosproblems.com/331).

The file states 2 research or textbook statements: 2 solved.

## `Erdos331.erdos_331`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/d30552f64c55686d40b928a0a3b8e2396357a4ee/ErdosProblem331.lean](https://github.com/Woett/Lean-files/blob/d30552f64c55686d40b928a0a3b8e2396357a4ee/ErdosProblem331.lean).

> Let $A,B\subseteq \mathbb{N}$ such that for all large $N
>
> $$$\lvert A\cap \{1,\ldots,N\}\rvert \gg
> N^{1/2}$$
>
> and
>
> $$\lvert B\cap \{1,\ldots,N\}\rvert \gg N^{1/2}.$$
>
> Is it true that there are infinitely many solutions to $a_1-a_2=b_1-b_2\neq 0$ with $a_1,a_2\in A$
> and $b_1,b_2\in B$?
>
> Ruzsa has observed that there is a simple counterexample: take $A$ to be the set of numbers whose
> binary representation has only non-zero digits in even places, and $B$ similarly but with non-zero
> digits only in odd places. It is easy to see $A$ and $B$ both grow like $\gg N^{1/2}$ and yet for
> any $n\geq 1$ there is exactly one solution to $n=a+b$ with $a\in A$ and $b\in B$.
>
> This was formalized in Lean by van Doorn using Aristotle.

```lean
theorem erdos_331 :
    ¬ ∀ A B : Set ℕ,
    (fun (n : ℕ) ↦ (n : ℝ) ^ (1 / 2 : ℝ)) =O[atTop] (fun (n : ℕ) ↦ (count (· ∈ A) n : ℝ)) →
    (fun (n : ℕ) ↦ (n : ℝ) ^ (1 / 2 : ℝ)) =O[atTop] (fun (n : ℕ) ↦ (count (· ∈ B) n : ℝ)) →
    { s : ℕ × ℕ × ℕ × ℕ | let ⟨a₁, a₂, b₁, b₂⟩ := s
      a₁ ∈ A ∧ a₂ ∈ A ∧ b₁ ∈ B ∧ b₂ ∈ B ∧
      a₁ ≠ a₂ ∧ a₁ + b₂ = a₂ + b₁ }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/331.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/331.lean#L52).

## `Erdos331.erdos_331.variants.ruzsa`

Solved: stated here without proof.

> Ruzsa suggests that a non-trivial variant of this problem arises if one imposes the stronger
> condition that $|A \cap \{1,\dots,N\}| \sim c_A N^{1/2}$ for some constant $c_A>0$, and similarly
> for $B$.
>
> The answer is yes. Write $A(N) = |A \cap \{1,\dots,N\}|$ and $B(N) = |B \cap \{1,\dots,N\}|$.
> Erdős and Freud [ErFr84, Theorem 4] proved that if $a_1 - a_2 = b_1 - b_2$ has only trivial
> solutions and $\liminf_N \min(A(N), B(N)) / N^{1/2} > 0$, then neither $A(N) / N^{1/2}$ nor
> $B(N) / N^{1/2}$ tends to a limit. If there were only finitely many non-trivial solutions, removing
> the finitely many elements of $A$ that occur in them would give sets with the same asymptotics and
> no non-trivial solution.

```lean
theorem erdos_331.variants.ruzsa :
    ∀ A B : Set ℕ,
    (∃ c_A > 0, (fun (n : ℕ) ↦ (count (· ∈ A) n : ℝ)) ~[atTop] (fun (n : ℕ) ↦ c_A * (n : ℝ) ^ (1 / 2 : ℝ))) →
    (∃ c_B > 0, (fun (n : ℕ) ↦ (count (· ∈ B) n : ℝ)) ~[atTop] (fun (n : ℕ) ↦ c_B * (n : ℝ) ^ (1 / 2 : ℝ))) →
    { s : ℕ × ℕ × ℕ × ℕ | let ⟨a₁, a₂, b₁, b₂⟩ := s
      a₁ ∈ A ∧ a₂ ∈ A ∧ b₁ ∈ B ∧ b₂ ∈ B ∧
      a₁ ≠ a₂ ∧ a₁ + b₂ = a₂ + b₁ }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/331.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/331.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/331.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/331.lean)
- [erdosproblems.com/331](https://www.erdosproblems.com/331)
