---
declaration: theorem
origin: cited
lean: Erdos292.erdos_292, Erdos292.erdos_292.variants.martin, Erdos292.erdos_292.variants.mul, Erdos292.erdos_292.variants.prime_pow, Erdos292.erdos_292.variants.two_mul
statement: formalized
---

# Erdős Problem 292

> *References:*
> - [erdosproblems.com/292](https://www.erdosproblems.com/292)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ma00] Martin, Greg, *Denser Egyptian fractions*. Acta Arith. (2000), 231-260.

*Quoted from [FormalConjectures/ErdosProblems/292.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/292](https://www.erdosproblems.com/292).

The file states 5 research or textbook statements: 5 solved.

## `Erdos292.erdos_292`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos292.lean#L116](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos292.lean#L116).

> Let $A$ be the set of $n\in \mathbb{N}$ such that there exist $1\leq m_1\lt \cdots \lt m_k=n$ with
> $\sum\tfrac{1}{m_i}=1$. Explore $A$. In particular, does $A$ have density $1$?
>
> Straus observed that $A$ is closed under multiplication. Furthermore, it is easy to see that $A$
> does not contain any prime power.
>
> The answer is yes, as proved by Martin [Ma00], who in fact proved that if
> $B=\mathbb{N}\backslash A$ then, for all large $x$,
>
> $$\frac{\lvert B\cap [1,x]\rvert}{x}\asymp \frac{\log\log x}{\log x},$$
>
> and also gave an essentially complete description of $B$ as those integers which are small
> multiples of prime powers.
>
> van Doorn has observed that if $n\in A$ (with $n>1$) then $2n\in A$ also, since if
> $\sum \frac{1}{m_i}=1$ then $\frac{1}{2}+\sum\frac{1}{2m_i}=1$ also.

```lean
theorem erdos_292 : A.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/292.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean#L60).

## `Erdos292.erdos_292.variants.martin`

Solved: stated here without proof.

> Martin [Ma00] proved that if $B=\mathbb{N}\backslash A$ then
> $\frac{\lvert B\cap [1,x]\rvert}{x}\asymp \frac{\log\log x}{\log x}$.

```lean
theorem erdos_292.variants.martin :
    (fun x : ℕ ↦ ((Aᶜ ∩ Set.Icc 1 x).ncard : ℝ) / x) =Θ[atTop]
      fun x ↦ Real.log (Real.log x) / Real.log x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/292.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean#L66).

## `Erdos292.erdos_292.variants.mul`

Solved: stated here without proof.

> Straus observed that $A$ is closed under multiplication.

```lean
theorem erdos_292.variants.mul : ∀ m ∈ A, ∀ n ∈ A, m * n ∈ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/292.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean#L73).

## `Erdos292.erdos_292.variants.prime_pow`

Solved: stated here without proof.

> $A$ does not contain any prime power.

```lean
theorem erdos_292.variants.prime_pow : ∀ n ∈ A, ¬ IsPrimePow n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/292.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean#L78).

## `Erdos292.erdos_292.variants.two_mul`

Solved: stated here without proof.

> van Doorn observed that if $n\in A$ (with $n>1$) then $2n\in A$ also.

```lean
theorem erdos_292.variants.two_mul : ∀ n ∈ A, 1 < n → 2 * n ∈ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/292.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/292.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/292.lean)
- [erdosproblems.com/292](https://www.erdosproblems.com/292)
