---
declaration: theorem
origin: cited
lean: Erdos921.erdos_921
statement: formalized
---

# Erdős Problem 921

> *References:*
> - [erdosproblems.com/921](https://www.erdosproblems.com/921)
> - [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Ga63] Gallai, T., Kritische Graphen. I. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1963), 165-192.
> - [KST84] Kierstead, H. A., Szemerédi, E. and Trotter, W. T., On coloring graphs with locally
>   small chromatic number. Combinatorica (1984), 183-185.

*Quoted from [FormalConjectures/ErdosProblems/921.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/921.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/921](https://www.erdosproblems.com/921).

The file states 1 research or textbook statement: 1 solved.

## `Erdos921.erdos_921`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos921.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos921.lean#L39).

> Let $k\geq 4$ and let $f_k(n)$ be the largest $m$ such that there is a graph on $n$ vertices
> with chromatic number $k$ in which every odd cycle has length $> m$.
> Then
> $$f_k(n) \asymp n^{\frac{1}{k-2}}.$$
>
> A question of Erdős and Gallai.
>
> Proved for all $k\geq 4$ by Kierstead, Szemerédi, and Trotter [KST84].
>
> The linked formal proof (Codex and GPT-5.6 Sol) states this as `f k n = Θ(n ^ (1 / (k - 2)))`,
> where `f k n` is the largest `m` such that some graph on `n` vertices with chromatic number `k`
> has no odd cycle of length at most `m`; the two eventual statements below are the two halves
> of this estimate.

```lean
theorem erdos_921 :
    ∀ (k : ℕ), 4 ≤ k →
      ∃ (c₁ c₂ : ℝ), 0 < c₁ ∧ 0 < c₂ ∧
        (∀ᶠ (n : ℕ) in atTop,
          (∃ (G : SimpleGraph (Fin n)),
            G.chromaticNumber = (k : ℕ∞) ∧
            ∀ l ∈ G.oddCycleLengths, c₁ * (n : ℝ) ^ (1 / ((k : ℝ) - 2)) < (l : ℝ))) ∧
        (∀ᶠ (n : ℕ) in atTop,
          ∀ (G : SimpleGraph (Fin n)),
            G.chromaticNumber = (k : ℕ∞) →
            ∃ l ∈ G.oddCycleLengths, (l : ℝ) ≤ c₂ * (n : ℝ) ^ (1 / ((k : ℝ) - 2)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/921.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/921.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/921.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/921.lean)
- [erdosproblems.com/921](https://www.erdosproblems.com/921)
