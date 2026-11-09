---
declaration: theorem
origin: cited
lean: Erdos261.erdos_261.variants.borwein_loring, Erdos261.erdos_261.variants.borwein_loring_property, Erdos261.erdos_261.parts.i, Erdos261.erdos_261.variants.le_10000, Erdos261.erdos_261.parts.ii, Erdos261.erdos_261.parts.iii, Erdos261.erdos_261.variants.two_representations
statement: formalized
---

# Erdős Problem 261

> *References:*
>  - [erdosproblems.com/261](https://www.erdosproblems.com/261)
>  - [BoLo90] Borwein, Peter and Loring, Terry A., Some questions of Erdős and Graham on numbers
>     of the form $\sum g_n/2^{g_n}$. Math. Comp. (1990), 377--394.
>  - [Er88c] Erdős, P., On the irrationality of certain series: problems and results. New advances
>     in transcendence theory (Durham, 1986) (1988), 102--109.
>  - [TUZ20] Tengely, Szabolcs and Ulas, Maciej and Zygadlo, Jakub, On a Diophantine equation of
>     Erdős and Graham. J. Number Theory (2020), 445--459.
>  - [PALOMAR-2026-10-11-000016](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-11-000016&version=1)

*Quoted from [FormalConjectures/ErdosProblems/261.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/261](https://www.erdosproblems.com/261).

The file states 7 research or textbook statements: 2 open, 3 solved and 2 textbook results.

## `Erdos261.erdos_261.variants.borwein_loring`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L73](https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L73).

> For every positive integer $m$, if $n = 2^{m+1} - m - 2$, then
>
> $$\frac{n}{2^n} = \sum_{n < k \le n + m} \frac{k}{2^k}.$$
>
> This construction is due to Borwein and Loring [BoLo90].

```lean
theorem erdos_261.variants.borwein_loring (m : ℕ) (hm : 0 < m) :
    let n := 2 ^ (m + 1) - m - 2
    n / (2 ^ n : ℚ) = ∑ k ∈ Finset.Ioc n (n + m), k / (2 ^ k : ℚ)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L58).

## `Erdos261.erdos_261.variants.borwein_loring_property`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L78](https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L78).

> The Borwein--Loring construction gives the required property when $m \ge 2$. This lower
> bound ensures that the representation contains at least two terms.

```lean
theorem erdos_261.variants.borwein_loring_property (m : ℕ) (hm : 2 ≤ m) :
    Erdos261Prop (2 ^ (m + 1) - m - 2)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L66).

## `Erdos261.erdos_261.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos261_erdos_261_parts_i.lean#L102](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos261_erdos_261_parts_i.lean#L102).

> Are there infinitely many positive integers $n$ such that there exist some $t \ge 2$ and
> distinct integers $a_1, \ldots, a_t \ge 1$ satisfying
>
> $$\frac{n}{2^n} = \sum_{1 \le k \le t} \frac{a_k}{2^{a_k}}?$$
>
> In [Er88c], Erdős notes that Cusick had a simple proof that infinitely many such $n$ exist.

```lean
theorem erdos_261.parts.i : {n : ℕ | 0 < n ∧ Erdos261Prop n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L77).

## `Erdos261.erdos_261.variants.le_10000`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L85](https://github.com/linrock/math-proofs/blob/b53791ff6294b4b90e3653970367f127a52fd16e/erdos-261/Solution.lean#L85).

> Tengely, Ulas, and Zygadlo [TUZ20] verified that every positive integer $n \le 10000$ has
> the required property.

```lean
theorem erdos_261.variants.le_10000 {n : ℕ} (hn_pos : 0 < n) (hn : n ≤ 10000) :
    Erdos261Prop n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L84).

## `Erdos261.erdos_261.parts.ii`

Open: stated without proof.

> Do all positive integers $n$ have the required property?

```lean
theorem erdos_261.parts.ii : ∀ n > 0, Erdos261Prop n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L90).

## `Erdos261.erdos_261.parts.iii`

Open: stated without proof.

> Is there a rational number $x$ such that
>
> $$x = \sum_{k=1}^{\infty} \frac{a_k}{2^{a_k}}$$
>
> has at least $2^{\aleph_0}$ representations by pairwise distinct positive integers $a_k$?

```lean
theorem erdos_261.parts.iii : ∃ x : ℚ,
    𝔠 ≤ #{a : ℕ → ℕ | Erdos261InfiniteRepresentation x a}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L97).

## `Erdos261.erdos_261.variants.two_representations`

Solved: stated here; a Lean proof is at [https://github.com/g8r-b8/erdos261-lean/blob/976bddf21eafc93ea86a7a1bfd92b847070a6f31/Erdos261.lean#L87](https://github.com/g8r-b8/erdos261-lean/blob/976bddf21eafc93ea86a7a1bfd92b847070a6f31/Erdos261.lean#L87).

> In [Er88c], Erdős asks the weaker question of whether there exists a rational $x$ with at
> least two representations
>
> $$x = \sum_{k=1}^{\infty} \frac{a_k}{2^{a_k}}$$
>
> by pairwise distinct positive integers $a_k$.
>
> The answer is yes: Z. Rafik (erdosproblems.com forum, 27 Apr 2026) observed that
> $4/2^4 = 5/2^5 + 6/2^6$ and $\sum_{m \ge 1} m/2^m = 2$, so $7/4$ is represented both by
> $\mathbb{N}_{>0} \setminus \{4\}$ and by $\mathbb{N}_{>0} \setminus \{5, 6\}$. It is generally believed that
> "two" here is a misprint for $2^{\aleph_0}$ (see `erdos_261.parts.iii`, which remains open).

```lean
theorem erdos_261.variants.two_representations : ∃ x : ℚ,
    2 ≤ #{a : ℕ → ℕ | Erdos261InfiniteRepresentation x a}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/261.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/261.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/261.lean)
- [erdosproblems.com/261](https://www.erdosproblems.com/261)
