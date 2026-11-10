---
declaration: theorem
origin: cited
lean: Erdos384.erdos_384, Erdos384.erdos_384.variants.strict
statement: formalized
---

# Erdős Problem 384

> *References:*
> - [erdosproblems.com/384](https://www.erdosproblems.com/384)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ec69] Ecklund, Jr., E. F., *On prime divisors of the binomial coefficient*. Pacific J. Math.
>   (1969), 267-270.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/384.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/384.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/384](https://www.erdosproblems.com/384).

The file states 2 research or textbook statements: 2 solved.

## `Erdos384.erdos_384`

Solved: stated here without proof.

> If $1\lt k\lt n-1$ then $\binom{n}{k}$ is divisible by a prime $p\leq n/2$ (except
> $\binom{7}{3}=\binom{7}{4}=5\cdot 7$).
>
> A conjecture of Erdős and Selfridge [ErGr80]. Proved by Ecklund [Ec69], who made the stronger
> conjecture that whenever $n>k^2$ the binomial coefficient $\binom{n}{k}$ is divisible by a prime
> $p\lt n/k$. Discussed in problem B31 and B33 of Guy's collection [Gu04]. Stronger forms of this
> conjecture are [1094](https://www.erdosproblems.com/1094) and
> [1095](https://www.erdosproblems.com/1095).
>
> Ecklund's theorem is stated for $n \geq 2k$ with the single exception $\binom{7}{3}$; by the
> symmetry $\binom{n}{k} = \binom{n}{n-k}$ this is the form above, where $\binom{7}{4}$ is the
> second exception. The prime bound is $p \leq n/2$ (that is, $2p \leq n$); see
> `erdos_384.variants.strict` for the strict inequality.

```lean
theorem erdos_384 (n k : ℕ) (hk : 1 < k) (hkn : k < n - 1) (h₃ : (n, k) ≠ (7, 3))
    (h₄ : (n, k) ≠ (7, 4)) :
    ∃ p : ℕ, p.Prime ∧ p ∣ n.choose k ∧ 2 * p ≤ n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/384.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/384.lean#L52).

## `Erdos384.erdos_384.variants.strict`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos384.lean#L71](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos384.lean#L71).

> With the strict inequality $p < n/2$ the statement is false: $\binom{4}{2} = 6$ has no prime
> divisor $p < 2$.

```lean
theorem erdos_384.variants.strict :
    ¬ ∀ n k : ℕ, 1 < k → k < n - 1 → (n, k) ≠ (7, 3) → (n, k) ≠ (7, 4) →
      ∃ p : ℕ, p.Prime ∧ p ∣ n.choose k ∧ 2 * p < n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/384.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/384.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/384.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/384.lean)
- [erdosproblems.com/384](https://www.erdosproblems.com/384)
