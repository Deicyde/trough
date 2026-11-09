---
declaration: theorem
origin: cited
lean: Erdos539.erdos_539, Erdos539.erdos_539.variants.sq, Erdos539.erdos_539.variants.sq_isBigO, Erdos539.erdos_539.variants.isBigO_sq, Erdos539.erdos_539.variants.sq_cube_root, Erdos539.erdos_539.variants.isBigO_sq_cube_root, Erdos539.erdos_539.variants.sq_cube_root_isBigO, Erdos539.erdos_539.variants.limit
statement: formalized
---

# Erdős Problem 539

> In this problem, a function $h : \mathbb{N} \to\mathbb{N}$ is defined maximally by a specified
> counting property.
>
> The problem asks to estimate $h(n)$. This has been interpreted here as asking for $\Theta(h(n))$.
> The principal version includes the unknown function `erdos_539.answer`. On the other hand, the best
> known upper bound is $n^{2/3}$ and the best known lower bound is $\sqrt{n}$ so we
> also provide these candidates as variants. Moreover, it suffices to show $O(h(n))$ and
> $O(\sqrt{n})$ respectively for each, so further variants are provided for those.
>
> In the source paper [Er73], Erdős also remarks that it should not be too difficult
> to determine $\lim_{n\to\infty}\log(h(n))/\log(n)$. This does not appear on the website, and
> it is not clear whether this remains open, but we include it here either way.
>
> *References:*
> - [erdosproblems.com/539](https://www.erdosproblems.com/539)
> - [GR99] Granville, A., & Roesler, F. (1999). _The Set of Differences of a Given Set_. The American Mathematical Monthly, 106(4), 338–344.
> - [Er73] Erdős, P., _Problems and results on combinatorial number theory_. A survey of combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.
> - [Sc+26] Schmitt, J., Gehrunger, T., Dekoninck, J., Bérczi, G., Kreitner, U., Price, L., & Holmes, D. (2026). _ProofCouncil: An LLM Agent for Solving Open Mathematical Problems_. [arXiv:2607.09474](https://arxiv.org/abs/2607.09474), Appendix A, Theorem A.1.

*Quoted from [FormalConjectures/ErdosProblems/539.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/539](https://www.erdosproblems.com/539).

The file states 8 research or textbook statements: 1 open and 7 solved.

## `Erdos539.erdos_539`

Open: stated without proof.

> Let $h(n)$ be maximal such that, for any set $A\subseteq \mathbb{N}$ of size $n$, the
> set$$\left\{ \frac{a}{(a,b)}: a,b\in A\right\}$$has size at least $h(n)$. Estimate $h(n)$.

```lean
theorem erdos_539 :
    (fun n ↦ (cofactorThreshold n : ℝ)) =Θ[atTop] erdos_539.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L66).

## `Erdos539.erdos_539.variants.sq`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-539-sqrt-disproof/blob/f4b14f9ef32c111162d3fd587e1c65b27a1524d5/lean/Erdos539SqrtFC.lean#L41-L44](https://github.com/KitaKen1/erdos-539-sqrt-disproof/blob/f4b14f9ef32c111162d3fd587e1c65b27a1524d5/lean/Erdos539SqrtFC.lean#L41-L44).

> Let $h(n)$ be maximal such that, for any set $A\subseteq \mathbb{N}$ of size $n$, the
> set$$\left\{ \frac{a}{(a,b)}: a,b\in A\right\}$$has size at least $h(n)$.
> Is $h(n) = \Theta(\sqrt{n})$?

```lean
theorem erdos_539.variants.sq :
    ¬ ((fun n ↦ (cofactorThreshold n : ℝ)) =Θ[atTop] fun n ↦ √n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L77).

## `Erdos539.erdos_539.variants.sq_isBigO`

Solved: stated here without proof.

> Erdős and Szemerédi proved that$$n^{1/2} \ll h(n)$$.

```lean
theorem erdos_539.variants.sq_isBigO :
    (fun n : ℕ ↦ √n) =O[atTop] fun n ↦ (cofactorThreshold n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L83).

## `Erdos539.erdos_539.variants.isBigO_sq`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-539-sqrt-disproof/blob/f4b14f9ef32c111162d3fd587e1c65b27a1524d5/lean/Erdos539SqrtFC.lean#L36-L39](https://github.com/KitaKen1/erdos-539-sqrt-disproof/blob/f4b14f9ef32c111162d3fd587e1c65b27a1524d5/lean/Erdos539SqrtFC.lean#L36-L39).

> Is $h(n) = O(\sqrt{n})$?

```lean
theorem erdos_539.variants.isBigO_sq :
    ¬ ((fun n ↦ (cofactorThreshold n : ℝ)) =O[atTop] fun n ↦ √n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L92).

## `Erdos539.erdos_539.variants.sq_cube_root`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296](https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296).

> Let $h(n)$ be maximal such that, for any set $A\subseteq \mathbb{N}$ of size $n$, the
> set$$\left\{ \frac{a}{(a,b)}: a,b\in A\right\}$$has size at least $h(n)$.
> Is $h(n) = \Theta(n^{2/3})$?
> The answer is negative; see [Sc+26, Theorem A.1] and the linked Lean proof.

```lean
theorem erdos_539.variants.sq_cube_root :
    ¬ ((fun n ↦ (cofactorThreshold n : ℝ)) =Θ[atTop]
      fun n ↦ (n : ℝ) ^ ((2 : ℝ) / 3))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L104).

## `Erdos539.erdos_539.variants.isBigO_sq_cube_root`

Solved: stated here without proof.

> Granville and Roesler [GR99] showed that $$h(n)\ll n^{2/3}$$.

```lean
theorem erdos_539.variants.isBigO_sq_cube_root :
    (fun n ↦ (cofactorThreshold n : ℝ)) =O[atTop] fun n ↦ (n : ℝ) ^ ((2 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L111).

## `Erdos539.erdos_539.variants.sq_cube_root_isBigO`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296](https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296).

> This lower bound is false; see [Sc+26, Theorem A.1] and the linked Lean proof.

```lean
theorem erdos_539.variants.sq_cube_root_isBigO :
    ¬ ((fun n : ℕ ↦ (n : ℝ) ^ ((2 : ℝ) / 3)) =O[atTop]
      fun n ↦ (cofactorThreshold n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L120).

## `Erdos539.erdos_539.variants.limit`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296](https://github.com/KitaKen1/erdos-539-formal-conjectures/blob/79897cf9241390eb168572f4a481e29e0e64b5f7/lean/Erdos539/FC.lean#L282-L296).

> From [Er73]: The determination of
> $$
>   \lim_{n\to\infty}\frac{\log(h(n))}{\log(n)}
> $$
> will perhaps be not too difficult.
> The limit is $1/2$; see [Sc+26, Theorem A.1] and the linked Lean proof.

```lean
theorem erdos_539.variants.limit :
    atTop.Tendsto
      (fun n ↦ Real.log (cofactorThreshold n) / Real.log n)
      erdos_539.variants.limit.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/539.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean#L138).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/539.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/539.lean)
- [erdosproblems.com/539](https://www.erdosproblems.com/539)
