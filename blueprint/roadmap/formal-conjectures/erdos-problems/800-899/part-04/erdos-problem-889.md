---
declaration: theorem
origin: cited
lean: Erdos889.erdos_889, Erdos889.erdos_889.variants.v0_gt_1, Erdos889.erdos_889.variants.general, Erdos889.erdos_889.variants.v1_eq_1_finite, Erdos889.erdos_889.variants.V1_eq_1_finite
statement: formalized
---

# Erdős Problem 889

> *Reference:* [erdosproblems.com/889](https://www.erdosproblems.com/889)

*Quoted from [FormalConjectures/ErdosProblems/889.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/889](https://www.erdosproblems.com/889).

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Erdos889.erdos_889`

Open: stated without proof.

> Let $v(n,k)$ count the prime factors of $n+k$ which
> do not divide $n+i$ for $0\leq i < k$. Is it true that
> $v_0(n)=\max_{k\geq 0}v(n,k)\to \infty$ as $n\to \infty$?

```lean
theorem erdos_889 : Tendsto v₀ atTop (𝓝 ⊤)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/889.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean#L52).

## `Erdos889.erdos_889.variants.v0_gt_1`

Solved: stated here without proof.

> $v_0(n) > 1$ for all $n$ except $n$ = 0, 1, 2, 3, 4, 7, 8, 16
>
> [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.

```lean
theorem erdos_889.variants.v0_gt_1 :
    ∀ n : ℕ, n ∉ ({0, 1, 2, 3, 4, 7, 8, 16} : Finset ℕ) → 1 < v₀ n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/889.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean#L61).

## `Erdos889.erdos_889.variants.general`

Open: stated without proof.

> Let $v_l(n) = \max_{k\geq l} v(n,k)$. For every fixed $l$,
> $v_l(n) \to \infty$ as $n \to \infty$
>
> [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.

```lean
theorem erdos_889.variants.general :
    ∀ l, Tendsto (v_l l) atTop (𝓝 ⊤)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/889.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean#L78).

## `Erdos889.erdos_889.variants.v1_eq_1_finite`

Open: stated without proof.

> Does $v_1(n) = 1$ have finite solutions?
>
> [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.

```lean
theorem erdos_889.variants.v1_eq_1_finite :
    {n | v_l 1 n = 1}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/889.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean#L88).

## `Erdos889.erdos_889.variants.V1_eq_1_finite`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-889-capital-v1-finite/blob/44d38dd7f618dbaa0b08fb976c0378b4897021cd/lean/Erdos889V1FiniteFC.lean#L999-L1004](https://github.com/KitaKen1/erdos-889-capital-v1-finite/blob/44d38dd7f618dbaa0b08fb976c0378b4897021cd/lean/Erdos889V1FiniteFC.lean#L999-L1004).

> Does $V_1(n) = 1$ have finite solutions?
>
> This is a modification of `erdos_889.variants.v1_eq_1_finite`,
> which might make it more amenable to attack according to [ErSe67].
>
> Kenta Kitamura (KitaKen1 on GitHub) has given a Lean proof
> ([erdos-889-capital-v1-finite](https://github.com/KitaKen1/erdos-889-capital-v1-finite))
> that there are only finitely many $n$ with $V_1(n) = 1$.
>
> [ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.

```lean
theorem erdos_889.variants.V1_eq_1_finite :
    {n | V_l 1 n = 1}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/889.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/889.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/889.lean)
- [erdosproblems.com/889](https://www.erdosproblems.com/889)
