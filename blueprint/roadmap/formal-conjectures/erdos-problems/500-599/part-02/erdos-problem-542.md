---
declaration: theorem
origin: cited
lean: Erdos542.erdos_542.parts.i, Erdos542.erdos_542.variants.sharp, Erdos542.erdos_542.parts.ii, Erdos542.erdos_542.variants.schinzel_szekeres, Erdos542.erdos_542.variants.log_power, Erdos542.erdos_542.variants.chen, Erdos542.erdos_542.variants.one_add_little_o, Erdos542.erdos_542.variants.only_two
statement: formalized
---

# Erdős Problem 542

> *References:*
> - [erdosproblems.com/542](https://www.erdosproblems.com/542)
> - [Er73] Erdős, P., _Problems and results on combinatorial number theory_. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [Er80] Erdős, Paul, _A survey of problems in combinatorial number theory_. Ann. Discrete Math.
>   (1980), 89-115.
> - [Er98] Erdős, Paul, _Some of my new and almost new problems and results in combinatorial number
>   theory_. Number theory (Eger, 1996) (1998), 169-180.
> - [ScSz59] Schinzel, A. and Szekeres, G., _Sur un problème de M. Paul Erdős_. Acta Sci. Math.
>   (Szeged) (1959), 221-229.
> - [Ch96] Chen, Yong-Gao, _On a problem of P. Erdős_. Acta Sci. Math. (Szeged) (1996), 101--114.

*Quoted from [FormalConjectures/ErdosProblems/542.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/542](https://www.erdosproblems.com/542).

The file states 8 research or textbook statements: 2 open and 6 solved.

## `Erdos542.erdos_542.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114).

> Is it true that if $A\subseteq\{1,\ldots,n\}$ is a set such that $[a,b]>n$ for all $a\neq b$,
> where $[a,b]$ is the least common multiple, then
> $$\sum_{a\in A}\frac{1}{a}\leq \frac{31}{30}?$$
>
> The answer is yes, proved by Schinzel and Szekeres [ScSz59]. The bound is best possible as
> $A=\{2,3,5\}$ demonstrates.

```lean
theorem erdos_542.parts.i :
    ∀ (n : ℕ) (A : Finset ℕ), IsLcmFree n A → ∑ a ∈ A, (1 : ℝ) / a ≤ 31 / 30
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L62).

## `Erdos542.erdos_542.variants.sharp`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114).

> The bound $31/30$ is attained by $A=\{2,3,5\}$ (with $n=5$).

```lean
theorem erdos_542.variants.sharp :
    IsLcmFree 5 {2, 3, 5} ∧ ∑ a ∈ ({2, 3, 5} : Finset ℕ), (1 : ℝ) / a = 31 / 30
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L70).

## `Erdos542.erdos_542.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114).

> Is it true that if $A\subseteq\{2,\ldots,n\}$ is a set such that $[a,b]>n$ for all $a\neq b$,
> then there must be $\gg n$ many $m\leq n$ which are not divisible by any $a\in A$?
>
> The answer is no, proved by Schinzel and Szekeres [ScSz59].
>
> The element $1$ is excluded: $A=\{1\}$ satisfies the hypothesis and leaves no such $m$, so
> without this restriction the answer would be negative for a trivial reason.

```lean
theorem erdos_542.parts.ii :
    ¬ ∃ c > 0, ∀ (n : ℕ) (A : Finset ℕ), IsLcmFree n A → 1 ∉ A →
      c * n ≤ ((uncovered n A).card : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L86).

## `Erdos542.erdos_542.variants.schinzel_szekeres`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos542.lean#L2114).

> Schinzel and Szekeres [ScSz59] proved that, for any $\epsilon>0$, there are sets
> $A\subseteq\{2,\ldots,n\}$ as in the problem with $o(n)$ many uncovered $m\leq n$ and for which
> $\sum_{a\in A}\frac{1}{a}>1-\epsilon$.

```lean
theorem erdos_542.variants.schinzel_szekeres :
    ∀ ε > 0, ∀ δ > 0, ∃ (n : ℕ) (A : Finset ℕ), IsLcmFree n A ∧ 1 ∉ A ∧
      ((uncovered n A).card : ℝ) ≤ δ * n ∧ 1 - ε < ∑ a ∈ A, (1 : ℝ) / a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L99).

## `Erdos542.erdos_542.variants.log_power`

Solved: stated here without proof.

> Schinzel and Szekeres [ScSz59] proved that there are examples $A\subseteq\{2,\ldots,n\}$ with at
> most $n/(\log n)^c$ many such $m$, for some real constant $c>0$.

```lean
theorem erdos_542.variants.log_power : ∃ c > (0 : ℝ), ∃ᶠ n : ℕ in atTop, ∃ A : Finset ℕ,
    IsLcmFree n A ∧ 1 ∉ A ∧ ((uncovered n A).card : ℝ) ≤ n / (log n) ^ c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L109).

## `Erdos542.erdos_542.variants.chen`

Solved: stated here without proof.

> Chen [Ch96] has proved that if $n>172509$ then
> $$\sum_{a\in A}\frac{1}{a}< \frac{1}{3}+\frac{1}{4}+\frac{1}{5}+\frac{1}{7}+\frac{1}{11}.$$

```lean
theorem erdos_542.variants.chen (n : ℕ) (hn : 172509 < n) (A : Finset ℕ) (hA : IsLcmFree n A) :
    ∑ a ∈ A, (1 : ℝ) / a < 1 / 3 + 1 / 4 + 1 / 5 + 1 / 7 + 1 / 11
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L118).

## `Erdos542.erdos_542.variants.one_add_little_o`

Open: stated without proof.

> In [Er73] Erdős further speculates that in fact
> $$\sum_{a\in A}\frac{1}{a}\leq 1+o(1),$$
> where the $o(1)$ term $\to 0$ as $n\to \infty$.

```lean
theorem erdos_542.variants.one_add_little_o :
    ∃ o : ℕ → ℝ, Tendsto o atTop (nhds 0) ∧
      ∀ (n : ℕ) (A : Finset ℕ), IsLcmFree n A → ∑ a ∈ A, (1 : ℝ) / a ≤ 1 + o n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L128).

## `Erdos542.erdos_542.variants.only_two`

Open: stated without proof.

> In [Er98] Erdős mentions that he, Schinzel, and Szekeres conjectured that $2,3,5$ and
> $3,4,5,7,11$ are the only two sequences for which the sum is $>1$.

```lean
theorem erdos_542.variants.only_two :
    ∀ (n : ℕ) (A : Finset ℕ), IsLcmFree n A → 1 < ∑ a ∈ A, (1 : ℝ) / a →
      A = {2, 3, 5} ∨ A = {3, 4, 5, 7, 11}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/542.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/542.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/542.lean)
- [erdosproblems.com/542](https://www.erdosproblems.com/542)
