---
declaration: theorem
origin: cited
lean: Erdos519.erdos_519
statement: formalized
---

# Erdős Problem 519

> *References:*
> - [erdosproblems.com/519](https://www.erdosproblems.com/519)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Bi94] Biró, A., *On a problem of Turán concerning sums of powers of complex numbers*. Acta Math.
>   Hungar. (1994), 209-216.
> - [Bi00] Biró, András, *An improved estimate in a power sum problem of Turán*. Indag. Math. (N.S.)
>   (2000), 343-358.
> - [Bi00b] Biró, A., *An upper estimate in Turán's pure power sum problem*. Indag. Math. (N.S.)
>   (2000), 499--508.
> - [At61b] Atkinson, F. V., *On sums of powers of complex numbers*. Acta Math. Acad.
>   Sci. Hungar. (1961), 185-188.

*Quoted from [FormalConjectures/ErdosProblems/519.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/519.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/519](https://www.erdosproblems.com/519).

The file states 1 research or textbook statement: 1 solved.

## `Erdos519.erdos_519`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos519.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos519.lean).

> Let $z_1,\ldots,z_n\in \mathbb{C}$ with $z_1=1$. Must there exist an absolute constant $c>0$ such
> that
>
> $$
> \max_{1\leq k\leq n}\left\lvert \sum_{i}z_i^k\right\rvert>c?
> $$
>
> Atkinson proved that $c=1/6$ suffices.

```lean
theorem erdos_519 :
    ∃ c : ℝ, 0 < c ∧
      ∀ (n : ℕ) (hn : 0 < n) (z : Fin n → ℂ),
        z ⟨0, hn⟩ = 1 →
          ∃ k : Fin n, c < ‖powerSum z (k.val + 1)‖
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/519.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/519.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/519.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/519.lean)
- [erdosproblems.com/519](https://www.erdosproblems.com/519)
