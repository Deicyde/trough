---
declaration: theorem
origin: cited
lean: Arxiv.id2303_01089.conjecture_1_3, Arxiv.id2303_01089.conjecture_1_4
statement: formalized
---

# Furstenberg's \`times p, times q\` conjectures

> *Reference:* [arxiv/2303.01089](https://arxiv.org/abs/2303.01089)
> **Around Furstenberg's times $p$, times $q$ conjecture: times $p$-invariant measures
> with some large Fourier coefficients**
> by *Catalin Badea, Sophie Grivaux*

*Quoted from [FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Arxiv.id2303_01089.conjecture_1_3`

Open: stated without proof.

> **Conjecture 1.3** (the $\times p, \times q$ conjecture): the only atomless Borel probability
> measure on $\mathbb{T}$ which is both $T_p$- and $T_q$-invariant is the Lebesgue measure.

```lean
theorem conjecture_1_3 {p q : ℕ} (hp : 2 <= p) (hq : 2 <= q) (hpq : MultiplicativelyIndependent p q)
    {μ : Measure 𝕋} [IsProbabilityMeasure μ] [MeasureTheory.IsAtomLess μ]
    (hmup : MeasurePreserving (Tn p) μ μ)
    (hmuq : MeasurePreserving (Tn q) μ μ) :
    μ = volume
```

Category `research open`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean#L75).

## `Arxiv.id2303_01089.conjecture_1_4`

Solved: stated here without proof.

> **Conjecture 1.4**: if $\mu$ is an atomless $T_p$-invariant Borel probability measure on
> $\mathbb{T}$, then $T_{q^n}\mu$ converges weak-star to Lebesgue measure.
> This paper disproves the conjecture.

```lean
theorem conjecture_1_4 :
    ¬ ∀ p q : ℕ, 2 <= p → 2 <= q → MultiplicativelyIndependent p q →
      ∀ μ : ProbabilityMeasure 𝕋,
        MeasureTheory.IsAtomLess μ.1 → MeasurePreserving (Tn p) μ μ →
        Tendsto (fun n : ℕ => μ.map (Tn_continuous (q ^ n)).aemeasurable) atTop
          (𝓝 UnitAddCircle.ProbabilityMeasure)
```

Category `research solved`; AMS [37 Dynamical systems and ergodic theory](../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean)
- [arxiv/2303.01089](https://arxiv.org/abs/2303.01089)
