---
declaration: theorem
origin: cited
lean: Erdos1096.erdos_1096
statement: formalized
---

# Erdős Problem 1096

> *References:*
> - [erdosproblems.com/1096](https://www.erdosproblems.com/1096)
> - [ErKo98] Erdős, P. and Komornik, V., Developments in non-integer bases.
>   Acta Math. Hungar. (1998), 57--83.
> - [Fe16] Feng, D.-J., On the topology of polynomials with bounded integer coefficients.
>   J. Eur. Math. Soc. (2016), 181--193.

*Quoted from [FormalConjectures/ErdosProblems/1096.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1096.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1096](https://www.erdosproblems.com/1096).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1096.erdos_1096`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos1096.lean#L44](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos1096.lean#L44).

> Let $1\lt q<1+\epsilon$ and consider the set of numbers of the shape
> $\sum_{i\in S}q^i$ (for all finite $S$), ordered by size as
> $0=x_1\lt x_2\lt \cdots$.
>
> Is it true that, provided $\epsilon>0$ is sufficiently small, $x_{k+1}-x_k \to 0$?
>
> This was solved affirmatively by Erdős and Komornik [ErKo98], who proved the conclusion
> whenever $1\lt q\lt \sqrt{q_1}$, where $q_1$ is the second Pisot-Vijayaraghavan number.

```lean
theorem erdos_1096 :
    ∃ ε > 0, ∀ q, 1 < q → q < 1 + ε →
    ∀ x : ℕ → ℝ, StrictMono x → Set.range x = { ∑ i ∈ S, q ^ i | S : Finset ℕ } →
    Tendsto (fun k => x (k + 1) - x k) atTop (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1096.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1096.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1096.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1096.lean)
- [erdosproblems.com/1096](https://www.erdosproblems.com/1096)
