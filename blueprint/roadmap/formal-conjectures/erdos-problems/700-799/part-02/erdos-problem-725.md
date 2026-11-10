---
declaration: theorem
origin: cited
lean: Erdos725.erdos_725, Erdos725.erdos_725.variants.erdos_kaplansky, Erdos725.erdos_725.variants.yamamoto
statement: formalized
---

# Erdős Problem 725

> *References:*
> - [erdosproblems.com/725](https://www.erdosproblems.com/725)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica 1 (1981), 25-42. [PDF](https://www.renyi.hu/~p_erdos/1981-16.pdf)
> - [ErKa46] Erdős, P. and Kaplansky, I., *The asymptotic number of Latin rectangles*.
>   Amer. J. Math. 68 (1946), 230-236. [PDF](https://www.renyi.hu/~p_erdos/1946-12.pdf)
> - [Ya51] Yamamoto, K., *On the asymptotic number of Latin rectangles*.
>   Jpn. J. Math. 21 (1951), 113-119.

*Quoted from [FormalConjectures/ErdosProblems/725.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/725.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/725](https://www.erdosproblems.com/725).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos725.erdos_725`

Open: stated without proof.

> Give an asymptotic formula for the number of $k\times n$ Latin rectangles.
>
> The formula $F(k,n)$ must satisfy $L(k,n)\sim F(k,n)$ as $n\to\infty$ for every choice of
> $k=k(n)\leq n$, so it also covers Latin squares ($k=n$).

```lean
theorem erdos_725 (k : ℕ → ℕ) (hk : ∀ n, k n ≤ n) :
    (fun n ↦ (L (k n) n : ℝ)) ~[atTop] fun n ↦ erdos_725.answer (k n) n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/725.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/725.lean#L74).

## `Erdos725.erdos_725.variants.erdos_kaplansky`

Solved: stated here without proof.

> Erdős and Kaplansky [ErKa46] proved the count is
>
> $$\sim e^{-\binom{k}{2}}(n!)^k$$
>
> when $k=o((\log n)^{3/2-\epsilon})$.
>
> Here $\epsilon>0$ is fixed.

```lean
theorem erdos_725.variants.erdos_kaplansky (ε : ℝ) (hε : 0 < ε) (k : ℕ → ℕ)
    (hk : (fun n ↦ (k n : ℝ)) =o[atTop] fun n ↦ Real.log n ^ (3 / 2 - ε)) :
    (fun n ↦ (L (k n) n : ℝ)) ~[atTop]
      fun n ↦ Real.exp (-((k n).choose 2 : ℝ)) * (n.factorial : ℝ) ^ k n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/725.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/725.lean#L86).

## `Erdos725.erdos_725.variants.yamamoto`

Solved: stated here without proof.

> Yamamoto [Ya51] extended this to $k\leq n^{1/3-o(1)}$.
>
> As in [Ya51, p. 113], we assume $k\lt n^{1/3-\delta}$ with $n^{-\delta}\to 0$, where $\delta$
> may be a positive constant or a function of $n$.

```lean
theorem erdos_725.variants.yamamoto (δ : ℕ → ℝ)
    (hδ : Tendsto (fun n : ℕ ↦ (n : ℝ) ^ (-δ n)) atTop (nhds 0)) (k : ℕ → ℕ)
    (hk : ∀ᶠ n in atTop, (k n : ℝ) < (n : ℝ) ^ (1 / 3 - δ n)) :
    (fun n ↦ (L (k n) n : ℝ)) ~[atTop]
      fun n ↦ Real.exp (-((k n).choose 2 : ℝ)) * (n.factorial : ℝ) ^ k n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/725.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/725.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/725.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/725.lean)
- [erdosproblems.com/725](https://www.erdosproblems.com/725)
