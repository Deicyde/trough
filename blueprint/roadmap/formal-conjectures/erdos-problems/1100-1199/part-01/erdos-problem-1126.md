---
declaration: theorem
origin: cited
lean: Erdos1126.erdos_1126
statement: formalized
---

# Erdős Problem 1126

> *References:*
> - [erdosproblems.com/1126](https://www.erdosproblems.com/1126)
> - [Er60c] Erdős, P., *Problem 310*. Colloq. Math., 311.
> - [dB66] de Bruijn, N. G., *On almost additive functions*. Colloq. Math. (1966), 59-63.
> - [Ju65] Jurkat, Wolfgang B., *On Cauchy's functional equation*. Proc. Amer. Math. Soc. (1965), 683-686.

*Quoted from [FormalConjectures/ErdosProblems/1126.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1126.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1126](https://www.erdosproblems.com/1126).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1126.erdos_1126`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1126.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1126.lean).

> If
>
> $$f(x+y)=f(x)+f(y)$$
>
> for almost all $x,y\in \mathbb{R}$ then there exists a function $g$ such that
>
> $$g(x+y)=g(x)+g(y)$$
>
> for all $x,y\in\mathbb{R}$ such that $f(x)=g(x)$ for almost all $x$.
>
> Proved independently by de Bruijn [dB66] and Jurkat [Ju65].

```lean
theorem erdos_1126 : ∀
    (f : ℝ → ℝ)
    (h :
      ∀ᵐ (p : ℝ × ℝ) ∂(volume.prod volume),
        f (p.1 + p.2) = f p.1 + f p.2),
    ∃ h : ℝ → ℝ,
      (∀ x y, h (x + y) = h x + h y) ∧ (∀ᵐ x ∂volume, f x = h x)
```

Category `research solved`; AMS [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1126.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1126.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1126.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1126.lean)
- [erdosproblems.com/1126](https://www.erdosproblems.com/1126)
