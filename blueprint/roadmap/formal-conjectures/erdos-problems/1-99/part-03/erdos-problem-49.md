---
declaration: theorem
origin: cited
lean: Erdos49.erdos_49, Erdos49.erdos_49.variants.little_o, Erdos49.erdos_49.variants.tao, Erdos49.erdos_49.variants.primes_maximal
statement: formalized
---

# Erdős Problem 49

> *References:*
> - [erdosproblems.com/49](https://www.erdosproblems.com/49)
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er95c] Erdős, Paul, *Some problems in number theory*. Octogon Math. Mag. (1995), 3-5.
> - [Ta24d] Tao, Terence, *Monotone nondecreasing sequences of the Euler totient function*.
>   Matematica (2024), 793-820.

*Quoted from [FormalConjectures/ErdosProblems/49.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/49](https://www.erdosproblems.com/49).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos49.erdos_49`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L120](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L120).

> Let $A=\{a_1\lt \cdots\lt a_t\}\subseteq \{1,\ldots,N\}$ be such that $\phi(a_1)\lt \cdots\lt \phi(a_t)$.
> The primes are such an example. Are they the largest possible? Can one show that
> $\lvert A\rvert<(1+o(1))\pi(N)$ or even $\lvert A\rvert=o(N)$?
>
> Erdős remarks that the last conjecture is probably easy, and that similar questions can be asked
> about $\sigma(n)$.
>
> Solved by Tao [Ta24d], who proved that
>
> $$ \lvert A\rvert \leq \left(1+O\left(\frac{(\log\log x)^5}{\log x}\right)\right)\pi(x).$$
>
> In [Er95c] Erdős further asks about the situation when $\phi(a_1)\leq \cdots \leq \phi(a_t)$.
>
> See also [415](https://www.erdosproblems.com/415).

```lean
theorem erdos_49 : ∀ ε : ℝ, 0 < ε →
    ∀ᶠ N : ℕ in atTop, (f N : ℝ) ≤ (1 + ε) * Nat.primeCounting N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/49.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean#L68).

## `Erdos49.erdos_49.variants.little_o`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L340](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L340).

> The weaker statement $\lvert A\rvert=o(N)$.

```lean
theorem erdos_49.variants.little_o :
    (fun N : ℕ ↦ (f N : ℝ)) =o[atTop] fun N ↦ (N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/49.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean#L76).

## `Erdos49.erdos_49.variants.tao`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L120](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos49.lean#L120).

> Tao [Ta24d] proved that
> $\lvert A\rvert \leq \left(1+O\left(\frac{(\log\log N)^5}{\log N}\right)\right)\pi(N)$, even for
> sets on which $\phi$ is merely non-decreasing.

```lean
theorem erdos_49.variants.tao : ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 10 ≤ N →
    (g N : ℝ) ≤ (1 + C * (Real.log (Real.log N) ^ 5 / Real.log N)) *
      Nat.primeCounting N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/49.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean#L88).

## `Erdos49.erdos_49.variants.primes_maximal`

Open: stated without proof.

> Are the primes the largest possible example, i.e. is $f(N) = \pi(N)$ for all $N \geq 2$?

```lean
theorem erdos_49.variants.primes_maximal :
    ∀ N : ℕ, 2 ≤ N → f N = Nat.primeCounting N
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/49.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/49.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/49.lean)
- [erdosproblems.com/49](https://www.erdosproblems.com/49)
