---
declaration: theorem
origin: cited
lean: Erdos1023.erdos_1023, Erdos1023.erdos_1023.variants.erdos_kleitman, Erdos1023.erdos_1023.variants.hunter
statement: formalized
---

# Erdős Problem 1023

> *References:*
> - [erdosproblems.com/1023](https://www.erdosproblems.com/1023)
> - [Er71, p.105] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.

*Quoted from [FormalConjectures/ErdosProblems/1023.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1023.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1023](https://www.erdosproblems.com/1023).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1023.erdos_1023`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1023.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1023.lean).

> Let $F(n)$ be the maximal size of a family of subsets of $\{1,\ldots,n\}$ such that no set in
> this family is the union of other members of the family. Is it true that there is a constant
> $c>0$ such that
> $$F(n)\sim c \frac{2^n}{n^{1/2}}?$$
>
> Hunter observes in the comments that this follows from the solution to [447], which implies
> $F(n)\sim \binom{n}{n/2}$.

```lean
theorem erdos_1023 :
    ∃ c : ℝ, 0 < c ∧
      ((fun n : ℕ => (F n : ℝ)) ~[atTop]
        (fun n : ℕ => c * 2 ^ n / (n : ℝ) ^ (1 / 2 : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1023.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1023.lean#L55).

## `Erdos1023.erdos_1023.variants.erdos_kleitman`

Solved: stated here without proof.

> Erdős and Kleitman proved in unpublished work that
> $$F(n)\asymp \frac{2^n}{n^{1/2}}.$$
> ([Er71] has an exponent of $3/2$, but this is presumably a typo.)

```lean
theorem erdos_1023.variants.erdos_kleitman :
    (fun n : ℕ => (F n : ℝ)) =Θ[atTop] (fun n : ℕ => (2 : ℝ) ^ n / (n : ℝ) ^ (1 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1023.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1023.lean#L67).

## `Erdos1023.erdos_1023.variants.hunter`

Solved: stated here without proof.

> Hunter observes in the comments that this follows from the solution to [447], which implies
> $F(n)\sim \binom{n}{n/2}$.

```lean
theorem erdos_1023.variants.hunter :
    (fun n : ℕ => (F n : ℝ)) ~[atTop] (fun n : ℕ => (n.choose (n / 2) : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1023.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1023.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1023.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1023.lean)
- [erdosproblems.com/1023](https://www.erdosproblems.com/1023)
