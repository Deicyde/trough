---
declaration: theorem
origin: cited
lean: Erdos247.erdos_247, Erdos247.erdos_247.variants.strong_condition
statement: formalized
---

# Erdős Problem 247

> *Reference:* [erdosproblems.com/247](https://www.erdosproblems.com/247)

*Quoted from [FormalConjectures/ErdosProblems/247.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/247.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/247](https://www.erdosproblems.com/247).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos247.erdos_247`

Open: stated without proof.

> Let $n_1 < n_2 < \cdots$ be a sequence of integers such that
>
> $$
>   \limsup \frac{n_k}{k} = \infty.
> $$
>
> Is
>
> $$
>   \sum_{k=1}^{\infty} \frac{1}{2^{n_k}}
> $$
>
> transcendental?

```lean
theorem erdos_247 : ∀ (n : ℕ → ℕ), (StrictMono n) →
    atTop.limsup (fun k => (n k / k.succ : EReal)) = ⊤ →
    Transcendental ℚ (∑' k, (1 : ℝ) / 2 ^ n k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/247.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/247.lean#L44).

## `Erdos247.erdos_247.variants.strong_condition`

Solved: stated here without proof.

> Erdős proved the answer is yes under the stronger condition that
> $\limsup \frac{n_k}{k^t} = \infty$ for all $t\geq 1$.
>
> [ErGr80] Erdős, P. and Graham, R.,
> _Old and new problems and results in combinatorial number theory_.
> Monographies de L'Enseignement Mathematique (1980).

```lean
theorem erdos_247.variants.strong_condition (n : ℕ → ℕ)
    (hn : StrictMono n)
    (h : ∀ t ≥ (1 : ℝ),
      atTop.limsup (fun k => n k / (k.succ : ℝ) ^ t |>.toEReal) = ⊤) :
    Transcendental ℚ (∑' k, (1 : ℝ) / 2 ^ n k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/247.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/247.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/247.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/247.lean)
- [erdosproblems.com/247](https://www.erdosproblems.com/247)
