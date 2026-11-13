---
declaration: theorem
origin: cited
lean: Erdos891.erdos_891, Erdos891.erdos_891.variants.schinzel, Erdos891.erdos_891.variants.case_k_2, Erdos891.erdos_891.variants.weisenberg
statement: formalized
---

# Erdős Problem 891

> *References:*
> - [erdosproblems.com/891](https://www.erdosproblems.com/891)
> - [Po18] Pólya, Georg, Zur arithmetischen {U}ntersuchung der {P}olynome. Math. Z. (1918), 143--148.
> - [Wikipedia] https://en.wikipedia.org/wiki/Dickson%27s_conjecture

*Quoted from [FormalConjectures/ErdosProblems/891.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/891](https://www.erdosproblems.com/891).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos891.erdos_891`

Open: stated without proof.

> Let $2=p_1 < p_2 < \cdots$ be the primes and $k\geq 2$. Is it true that, for all sufficiently large
> $n$, there must exist an integer in $[n,n+p_1\cdots p_k)$ with $>k$ many prime factors?

```lean
theorem erdos_891 :
    ∀ k ≥ 2, ∀ᶠ n in atTop,
    ∃ m ∈ Ico n (n + ∏ i ∈ range k, i.nth Nat.Prime), k < ω m
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/891.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean#L42).

## `Erdos891.erdos_891.variants.schinzel`

Solved: stated here without proof.

> Schinzel deduced from Pólya's theorem [Po18] (that the sequence of $k$-smooth integers has unbounded
> gaps) that this is true with $p_1\cdots p_k$ replaced by $p_1\cdots p_{k-1}p_{k+1}$.

```lean
theorem erdos_891.variants.schinzel :
    ∀ k ≥ 2, ∀ᶠ n in atTop,
      ∃ m ∈ Ico n (n + (∏ i ∈ range (k - 1), i.nth Nat.Prime) * k.nth Nat.Prime),
      k < ω m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/891.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean#L52).

## `Erdos891.erdos_891.variants.case_k_2`

Open: stated without proof.

> This is unknown even for $k=2$ - that is, is it true that in every interval of $6$
> (sufficiently large) consecutive integers there must exist one with at least $3$ prime factors?

```lean
theorem erdos_891.variants.case_k_2 :
    ∀ᶠ n in atTop,
      ∃ m ∈ Ico n (n + 6), 3 ≤ ω m
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/891.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean#L63).

## `Erdos891.erdos_891.variants.weisenberg`

Solved: stated here without proof.

> Weisenberg has observed that Dickson's conjecture implies the answer is no if we replace
> $p_1\cdots p_k$ with $p_1\cdots p_k-1$. Indeed, let $L_k$ be the lowest common multiple of all
> integers at most $p_1\cdots p_k$. By Dickson's conjecture [Wikipedia], there are infinitely many
> $n'$ such that $\frac{L_k}{m}n'+1$ is prime for all $1\leq m < p_1\cdots p_k$. It follows that,
> if $n=L_kn'+1$, then all integers in $[n,n+p_1\cdots p_k-1)$ have at most $k$ prime factors.
>
> The statement is conditional on Dickson's conjecture, formalised as
> `Dickson.dickson_conjecture`.

```lean
theorem erdos_891.variants.weisenberg (k : ℕ) (hk : k ≥ 2)
    (hdickson : type_of% Dickson.dickson_conjecture) :
    ∃ᶠ n in atTop,
      ∀ m ∈ Ico n (n + (∏ i ∈ range k, i.nth Nat.Prime) - 1),
      ω m ≤ k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/891.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/891.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/891.lean)
- [erdosproblems.com/891](https://www.erdosproblems.com/891)
