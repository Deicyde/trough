---
declaration: theorem
origin: cited
lean: Erdos520.erdos_520
statement: formalized
---

# Erdős Problem 520

> *References:*
> - [erdosproblems.com/520](https://www.erdosproblems.com/520)
> - [Hø26] Høystad, S. W. R., *A self-contained Lean 4 proof that Erdős Problem #520 has a
>   negative answer* (2026), https://github.com/saasom/Erdos520/blob/v1.1.0/paper/erdos520_note.pdf
> - [Ha13] Harper, A. J., *Bounds on the suprema of Gaussian processes, and omega results for the
>   sum of a random multiplicative function*. Ann. Appl. Probab. 23 (2013), 584–616.

*Quoted from [FormalConjectures/ErdosProblems/520.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/520.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/520](https://www.erdosproblems.com/520).

The file states 1 research or textbook statement: 1 solved.

## `Erdos520.erdos_520`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos520.lean#L24](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos520.lean#L24).

> Let $f$ be a Rademacher multiplicative function.
> Does there exist some constant $c > 0$ such that, almost surely,
> $$
>   \limsup_{N \to \infty} \frac{\sum_{m \leq N} f(m)}{\sqrt{N \log \log N}} = c?
> $$
>
> The answer is no: Høystad [Hø26] (with GPT-5.6 Pro and Claude) proved, following the
> Halász–Lau–Tenenbaum–Wu–Caich martingale approach with Harper's low-moment estimates [Ha13],
> that almost surely $\sum_{m \le N} f(m) \ll \sqrt{N} (\log \log N)^{1/4 + \eta}$ for every
> $\eta > 0$, so the $\limsup$ is $0$ almost surely. The linked formal
> proof works with the concrete model `ℕ → Bool` with the product of fair coins, whose
> squarefree-supported Rademacher function is `IsRademacherMultiplicative`; this refutes the
> statement below.

```lean
theorem erdos_520 :
    ¬ ∃ c > 0, ∀ (Ω : Type) [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
      (f : ℕ → Ω → ℝ), IsRademacherMultiplicative f →
      ∀ᵐ ω, limsup (fun N ↦ ∑ m ≤ N, f m ω / sqrt (N * log (log N))) atTop = c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/520.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/520.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/520.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/520.lean)
- [erdosproblems.com/520](https://www.erdosproblems.com/520)
