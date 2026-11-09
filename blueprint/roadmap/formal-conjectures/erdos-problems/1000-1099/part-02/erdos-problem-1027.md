---
declaration: theorem
origin: cited
lean: Erdos1027.erdos_1027
statement: formalized
---

# Erdős Problem 1027

> *References:*
> - [erdosproblems.com/1027](https://www.erdosproblems.com/1027)
> - [Er64e] Erdős, P., *On a combinatorial problem. II*. Acta Math. Acad. Sci. Hungar. (1964),
>   445-447.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.

*Quoted from [FormalConjectures/ErdosProblems/1027.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1027.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1027](https://www.erdosproblems.com/1027).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1027.erdos_1027`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1027.lean#L209](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1027.lean#L209).

> Let $c>0$, and let $n$ be sufficiently large depending on $c$. Suppose that $\mathcal{F}$ is a
> family of at most $c2^n$ many finite sets of size $n$. Let $X=\cup_{A\in \mathcal{F}}A$.
>
> Must there exist $\gg_c 2^{\lvert X\rvert}$ many sets $B\subset X$ which intersect every set in
> $\mathcal{F}$, yet contain none of them?
>
> The existence of a single such $B$ is equivalent to $\mathcal{F}$ being $2$-chromatic (or having
> property B), see [901](https://www.erdosproblems.com/901).
>
> This is true, and a proof was given in the comment section by Koishi Chan.

```lean
theorem erdos_1027 : ∀ c : ℝ, 0 < c → ∃ δ : ℝ, 0 < δ ∧
    ∀ᶠ n : ℕ in atTop, ∀ (α : Type) [DecidableEq α] (F : Finset (Finset α)),
      (∀ A ∈ F, A.card = n) → (F.card : ℝ) ≤ c * 2 ^ n →
        δ * 2 ^ (groundSet F).card ≤ (goodSets F).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1027.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1027.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1027.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1027.lean)
- [erdosproblems.com/1027](https://www.erdosproblems.com/1027)
