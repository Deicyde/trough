---
declaration: theorem
origin: cited
lean: Erdos902.erdos_902, Erdos902.erdos_902.variants.f_one, Erdos902.erdos_902.variants.f_two, Erdos902.erdos_902.variants.erdos_lower, Erdos902.erdos_902.variants.erdos_upper, Erdos902.erdos_902.variants.szekeres_f_three, Erdos902.erdos_902.variants.szekeres_lower
statement: formalized
---

# Erdős Problem 902

> *References:*
> - [erdosproblems.com/902](https://www.erdosproblems.com/902)
> - [Er63c] Erdős, P., *On a problem in graph theory*. Math. Gaz. 47 (1963), 220-223.
>   [PDF](https://www.renyi.hu/~p_erdos/1963-08.pdf)
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59-79.
> - [SzSz65] Szekeres, E. and Szekeres, G., *On a problem of Schütte and Erdős*. Math. Gaz. 49
>   (1965), 290-293.

*Quoted from [FormalConjectures/ErdosProblems/902.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/902](https://www.erdosproblems.com/902).

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 2 test statements, counted here but not shown.

## `Erdos902.erdos_902`

Open: stated without proof.

> Let $f(n)$ be minimal such that there is a tournament (a complete directed graph) on $f(n)$
> vertices such that every set of $n$ vertices is dominated by at least one other vertex.
> Estimate $f(n)$.

```lean
theorem erdos_902 : (fun n ↦ (f n : ℝ)) =Θ[atTop] erdos_902.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L90).

## `Erdos902.erdos_902.variants.f_one`

Proved here.

> It is easy to check that $f(1)=3$ and $f(2)=7$.
>
> This is the statement for $f(1)$.

```lean
theorem erdos_902.variants.f_one : f 1 = 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L99).

## `Erdos902.erdos_902.variants.f_two`

Solved: stated here without proof.

> It is easy to check that $f(1)=3$ and $f(2)=7$.
>
> This is the statement for $f(2)$.

```lean
theorem erdos_902.variants.f_two : f 2 = 7
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L130).

## `Erdos902.erdos_902.variants.erdos_lower`

Solved: stated here without proof.

> Erdős [Er63c] proved
> $$2^{n+1}-1 \leq f(n) \ll n^22^n.$$
>
> This is the lower bound.

```lean
theorem erdos_902.variants.erdos_lower (n : ℕ) : 2 ^ (n + 1) - 1 ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L140).

## `Erdos902.erdos_902.variants.erdos_upper`

Solved: stated here without proof.

> Erdős [Er63c] proved
> $$2^{n+1}-1 \leq f(n) \ll n^22^n.$$
>
> This is the upper bound, in the form proved in [Er63c, (2)]:
> $\limsup_n f(n)2^{-n}n^{-2} \leq \log 2$.

```lean
theorem erdos_902.variants.erdos_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (f n : ℝ) ≤ (Real.log 2 + ε) * n ^ 2 * 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L151).

## `Erdos902.erdos_902.variants.szekeres_f_three`

Solved: stated here without proof.

> Szekeres and Szekeres [SzSz65] proved that $f(3)=19$ and
> $$n2^n \ll f(n).$$
>
> This is the statement for $f(3)$.

```lean
theorem erdos_902.variants.szekeres_f_three : f 3 = 19
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L162).

## `Erdos902.erdos_902.variants.szekeres_lower`

Solved: stated here without proof.

> Szekeres and Szekeres [SzSz65] proved that $f(3)=19$ and
> $$n2^n \ll f(n).$$
>
> This is the lower bound.

```lean
theorem erdos_902.variants.szekeres_lower :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, c * n * 2 ^ n ≤ (f n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/902.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean#L172).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/902.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/902.lean)
- [erdosproblems.com/902](https://www.erdosproblems.com/902)
