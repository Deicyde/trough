---
declaration: theorem
origin: cited
lean: Erdos1141.erdos_1141.variants.pollack_1_3, Erdos1141.erdos_1141.variants.mertens_third, Erdos1141.erdos_1141
statement: formalized
---

# Erdős Problem 1141

> *References:*
> - [erdosproblems.com/1141](https://www.erdosproblems.com/1141)
> - [A214583](https://oeis.org/A214583)
> - [APSSV26b] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
>   [Short proofs in combinatorics, probability and number theory II](https://arxiv.org/abs/2604.06609).
>   arXiv:2604.06609 (2026).
> - [Or26] Y. Oriike, [Lean formalisation of Erdős problem 1141](https://github.com/yuta0x89/ErdosProblems/blob/a1319f732cdee5140faf47d984e2c451c1184803/Erdos1141.lean) (2026)
> - [Po17] P. Pollack, Bounds for the first several prime character nonresidues. Proc. Amer. Math. Soc.
>   (2017), 2815--2826.
> - [Me1874] F. Mertens, Ein Beitrag zur analytischen Zahlentheorie. J. Reine Angew. Math. (1874),
>   46--62.
> - [Va99] Various, Some of Paul's favorite problems. Booklet produced for the conference "Paul Erdős
>   and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1141.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1141.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1141](https://www.erdosproblems.com/1141).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1141.erdos_1141.variants.pollack_1_3`

Solved: stated here without proof.

> **Theorem 1.3 of [Po17]**: for a quadratic character to a large enough modulus, the primes below
> $m^{1/4+\varepsilon}$ on which the character is $1$ outnumber any fixed power of $\log m$.

```lean
theorem erdos_1141.variants.pollack_1_3 (ε A : ℝ) (hε : 0 < ε) (hA : 0 < A) :
    ∃ m₀ : ℕ, ∀ m : ℕ, m₀ < m → ∀ χ : DirichletCharacter ℂ m, MulChar.IsQuadratic χ →
      Real.log m ^ A ≤ ((residuePrimesUpTo m χ ε).card : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1141.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1141.lean#L68).

## `Erdos1141.erdos_1141.variants.mertens_third`

Solved: stated here without proof.

> **Mertens' third theorem** [Me1874], in the weakened form the linked proof assumes: the product
> over the primes up to $n$ of $1 - 1/p$ is at least $1/(3\log n)$.
>
> The true asymptotic is $e^{-\gamma}/\log n$, and $e^{-\gamma} > 1/3$, so this bound is weaker than
> the theorem and is what the deduction needs.

```lean
theorem erdos_1141.variants.mertens_third (n : ℕ) (hn : 3 ≤ n) :
    1 / (3 * Real.log n) ≤ ∏ p ∈ (Finset.range (n + 1)).filter Nat.Prime, (1 - 1 / (p : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1141.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1141.lean#L81).

## `Erdos1141.erdos_1141`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/main/problems/1141/Erdos1141.lean](https://github.com/Jayyhk/erdos-lean/blob/main/problems/1141/Erdos1141.lean).

> Are there infinitely many $n$ such that $n-k^2$ is prime for all $k$ with $(n,k)=1$ and $k^2 < n$?
>
> In [Va99] it is asked whether $968$ is the largest integer with this property, but this is an
> error, since for example $968-9=7\cdot 137$.
>
> The list of $n$ satisfying the given property is [A214583] in the OEIS. The largest known such $n$
> is $1722$.
>
> The answer is negative: [APSSV26b] proves a stronger finiteness theorem, deducing it from
> Pollack [Po17]. Oriike [Or26] formalised the deduction in Lean.

```lean
theorem erdos_1141 :
    ¬ Infinite { n | Erdos1141Prop n }
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1141.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1141.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1141.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1141.lean)
- [erdosproblems.com/1141](https://www.erdosproblems.com/1141)
