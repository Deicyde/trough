---
declaration: theorem
origin: cited
lean: Erdos946.erdos_946, Erdos946.erdos_946.variants.spiro_5040, Erdos946.erdos_946.variants.heathbrown_lower_bound, Erdos946.erdos_946.variants.hildebrand_lower_bound, Erdos946.erdos_946.variants.upper_bound
statement: formalized
---

# Erdős Problem 946

> *References:*
>  - [erdosproblems.com/946](https://www.erdosproblems.com/946)
>  - [ErMi52] Erdős, P. and Mirsky, L., The distribution of values of the divisor function {$d(n)$}.
>    Proc. London Math. Soc. (3) (1952), 257--271.
>  - [Sp81] Spiro, C. A., The frequency with which an integral-valued, prime-independent,
>    multiplicative or additive function of n divides a polynomial function of n.
>  - [He84] Heath-Brown, D. R., The divisor function at consecutive integers.
>    Mathematika 31 (1984), no. 2, 141--149.
>  - [Hi85] Hildebrand, A., The divisor function at consecutive integers. Pacific J. Math.
>    (1987), 307--319
>  - [EPS87] Erdős, P., Pomerance, C., and Sarkőzy, A., On locally repeated values of
>    arithmetic functions. III. Proc. Amer. Math. Soc. (1987), 1--7.

*Quoted from [FormalConjectures/ErdosProblems/946.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/946](https://www.erdosproblems.com/946).

The file states 5 research or textbook statements: 5 solved.

## `Erdos946.erdos_946`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos946.lean#L75](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos946.lean#L75).

> There are infinitely many $n$ such that $τ(n) = τ(n+1)$. Proved in [He84].
> Here τ is the divisor counting function, which is `σ 0` in mathlib.

```lean
theorem erdos_946 : {n : ℕ | σ 0 n = σ 0 (n + 1)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/946.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean#L52).

## `Erdos946.erdos_946.variants.spiro_5040`

Solved: stated here without proof.

> There are infinitely many $n$ such that $τ(n) = τ(n + 5040)$. Proved in [Sp81].

```lean
theorem erdos_946.variants.spiro_5040 : {n : ℕ | σ 0 n = σ 0 (n + 5040)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/946.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean#L59).

## `Erdos946.erdos_946.variants.heathbrown_lower_bound`

Solved: stated here without proof.

> The number of $n \le x$ with $τ(n) = τ(n+1)$ is at least $x / (\log x)^7$ for all sufficiently
> large $x$. Proved in [He84].

```lean
theorem erdos_946.variants.heathbrown_lower_bound :
    (fun x => x / (x.log)^7) =O[atTop] erdos946Count
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/946.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean#L71).

## `Erdos946.erdos_946.variants.hildebrand_lower_bound`

Solved: stated here without proof.

> Improved lower bound in [Hi85]: $Ω(x / (\log \log x)^3)$.

```lean
theorem erdos_946.variants.hildebrand_lower_bound :
    (fun x => x / (x.log.log)^3) =O[atTop] erdos946Count
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/946.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean#L79).

## `Erdos946.erdos_946.variants.upper_bound`

Solved: stated here without proof.

> Upper bound in [EPS87]: $O(x / \sqrt{\log \log x})$.

```lean
theorem erdos_946.variants.upper_bound : erdos946Count =O[atTop] (fun x => x / √x.log.log )
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/946.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/946.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/946.lean)
- [erdosproblems.com/946](https://www.erdosproblems.com/946)
