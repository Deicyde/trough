---
declaration: theorem
origin: cited
lean: Erdos1028.erdos_1028, Erdos1028.erdos_1028.variants.lower_bound, Erdos1028.erdos_1028.variants.upper_bound, Erdos1028.erdos_1028.variants.erdos_spencer
statement: formalized
---

# Erdős Problem 1028

> *References:*
> - [erdosproblems.com/1028](https://www.erdosproblems.com/1028)
> - [Er63d] Erdős, Pál, *On combinatorial questions connected with a theorem of Ramsey and van der
>   Waerden*. Mat. Lapok (1963), 29-37.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [ErSp71] Erdős, P. and Spencer, J., *Imbalances in $k$-colorations*. Networks (1971/72),
>   379-385.

*Quoted from [FormalConjectures/ErdosProblems/1028.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1028](https://www.erdosproblems.com/1028).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1028.erdos_1028`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1028.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1028.lean).

> Let
> $$H(n)=\min_f \max_{X\subseteq \{1,\ldots,n\}} \left\lvert \sum_{x\lt y\in X} f(x,y)\right\rvert,$$
> where $f$ ranges over all functions $f:\{1,\ldots,n\}^2\to \{-1,1\}$. Estimate $H(n)$.
>
> Erdős [Er63d] proved
> $$\frac{n}{4}\leq H(n) \ll n^{3/2}.$$
> Erdős and Spencer [ErSp71] proved that $H(n)\gg n^{3/2}$.

```lean
theorem erdos_1028 :
    (fun n => (H n : ℝ)) =Θ[atTop]
      fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1028.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean#L61).

## `Erdos1028.erdos_1028.variants.lower_bound`

Solved: stated here without proof.

> Erdős [Er63d] proved
> $$\frac{n}{4}\leq H(n) \ll n^{3/2}.$$

```lean
theorem erdos_1028.variants.lower_bound :
    ∀ᶠ n : ℕ in atTop, (n : ℝ) / 4 ≤ (H n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1028.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean#L70).

## `Erdos1028.erdos_1028.variants.upper_bound`

Solved: stated here without proof.

> Erdős [Er63d] proved
> $$\frac{n}{4}\leq H(n) \ll n^{3/2}.$$

```lean
theorem erdos_1028.variants.upper_bound :
    (fun n => (H n : ℝ)) ≪ (fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1028.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean#L78).

## `Erdos1028.erdos_1028.variants.erdos_spencer`

Solved: stated here without proof.

> Erdős and Spencer [ErSp71] proved that $H(n)\gg n^{3/2}$.

```lean
theorem erdos_1028.variants.erdos_spencer :
    (fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ)) ≪ (fun n => (H n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1028.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1028.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1028.lean)
- [erdosproblems.com/1028](https://www.erdosproblems.com/1028)
