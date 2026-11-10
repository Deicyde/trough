---
declaration: theorem
origin: cited
lean: Erdos115.erdos_115
statement: formalized
---

# Erdős Problem 115

> *References:*
> - [erdosproblems.com/115](https://www.erdosproblems.com/115)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [ErLe94] Erëmenko, A. and Lempert, L., *An extremal problem for polynomials*. Proc. Amer. Math.
>   Soc. (1994), 191-193.
> - [Po59a] Pommerenke, Ch., *On the derivative of a polynomial*. Michigan Math. J. (1959), 373-375.

*Quoted from [FormalConjectures/ErdosProblems/115.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/115.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/115](https://www.erdosproblems.com/115).

The file states 1 research or textbook statement: 1 solved.

## `Erdos115.erdos_115`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos115.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos115.lean).

> If $p(z)$ is a polynomial of degree $n$ such that $\{z : \lvert p(z)\rvert\leq 1\}$ is connected
> then is it true that
>
> $$\max_{\substack{z\in\mathbb{C}\\ \lvert p(z)\rvert\leq 1}} \lvert p'(z)\rvert
> \leq (\tfrac{1}{2}+o(1))n^2?$$
>
> Eremenko and Lempert [ErLe94] have shown this is true, and in fact Chebyshev polynomials are the
> extreme examples.

```lean
theorem erdos_115 :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ p : Polynomial ℂ, p.Monic → p.natDegree = n →
      IsConnected {z : ℂ | ‖p.eval z‖ ≤ 1} → ∀ z : ℂ, ‖p.eval z‖ ≤ 1 →
        ‖p.derivative.eval z‖ ≤ (1 / 2 + ε) * (n : ℝ) ^ 2
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/115.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/115.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/115.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/115.lean)
- [erdosproblems.com/115](https://www.erdosproblems.com/115)
