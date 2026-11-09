---
declaration: theorem
origin: cited
lean: Erdos166.erdos_166, Erdos166.erdos_166.variants.mattheus_verstraete
statement: formalized
---

# Erdős Problem 166

> *References:*
> - [erdosproblems.com/166](https://www.erdosproblems.com/166)
> - [Sp77] Spencer, J., Asymptotic lower bounds for Ramsey functions. Discrete Math. (1977), 69-76.
> - [AKS80] Ajtai, M., Komlós, J. and Szemerédi, E., A note on Ramsey numbers. J. Combin. Theory
>   Ser. A (1980), 354-360.
> - [MaVe23] Mattheus, S. and Verstraëte, J., The asymptotics of $r(4,t)$. Ann. of Math. (2024),
>   941-965.

*Quoted from [FormalConjectures/ErdosProblems/166.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/166.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/166](https://www.erdosproblems.com/166).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos166.erdos_166`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos166.lean#L83](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos166.lean#L83).

> Prove that
>
> $$R(4,k) \gg \frac{k^3}{(\log k)^{O(1)}}.$$
>
> This is true, and was proved by Mattheus and Verstraëte [MaVe23], who showed that
> $R(4,k) \gg \frac{k^3}{(\log k)^4}$.
> This problem is #5 in Ramsey Theory in the graphs problem collection.
>
> The linked formal proof (Codex and GPT-5.6 Sol, via the construction of Bradač used for
> Problem 920) gives `k ^ 3 / (log k) ^ c = O(R(4, k))` for a natural `c > 0`, with the Ramsey
> number defined through `CliqueFree`/`IndepSetFree`; this implies the statement below.

```lean
theorem erdos_166 :
    ∃ (c C : ℝ), 0 < c ∧ 0 < C ∧
      ∀ᶠ (k : ℕ) in atTop,
        (SimpleGraph.classicalRamsey 4 k : ℝ) ≥
          C * (k : ℝ) ^ 3 / (Real.log k) ^ c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/166.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/166.lean#L53).

## `Erdos166.erdos_166.variants.mattheus_verstraete`

Solved: stated here without proof.

> Mattheus and Verstraëte [MaVe23] proved the explicit lower bound
>
> $$R(4,k) \gg \frac{k^3}{(\log k)^4}.$$

```lean
theorem erdos_166.variants.mattheus_verstraete :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ (k : ℕ) in atTop,
      (SimpleGraph.classicalRamsey 4 k : ℝ) ≥ C * (k : ℝ) ^ 3 / (Real.log k) ^ 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/166.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/166.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/166.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/166.lean)
- [erdosproblems.com/166](https://www.erdosproblems.com/166)
