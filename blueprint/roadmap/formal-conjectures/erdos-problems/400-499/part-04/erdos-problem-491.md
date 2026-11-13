---
declaration: theorem
origin: cited
lean: Erdos491.erdos_491
statement: formalized
---

# Erdős Problem 491

> *References:*
> - [erdosproblems.com/491](https://www.erdosproblems.com/491)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59--79.
> - [Wi70] E. Wirsing, A characterization of $\log n$ as an additive arithmetic function.
>   Symposia Math. (1970), 45-57.

*Quoted from [FormalConjectures/ErdosProblems/491.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/491.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/491](https://www.erdosproblems.com/491).

The file states 1 research or textbook statement: 1 solved.

## `Erdos491.erdos_491`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos491.lean#L34](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos491.lean#L34).

> Let $f : \mathbb{N} \to \mathbb{R}$ be an additive function (so that $f(ab) = f(a) + f(b)$
> whenever $(a, b) = 1$). If $|f(n+1) - f(n)| < c$ for some constant $c$ and all $n$, then must
> there exist some $c'$ such that $f(n) = c' \log n + O(1)$?
>
> A question of Erdős [Er61, p.237; Er82e, p.65], who had proved that $f(n) = c' \log n$ under the
> stronger hypotheses $f(n+1) - f(n) = o(1)$ or $f(n+1) \ge f(n)$. The answer is yes, proved by
> Wirsing [Wi70]. See also `erdos_897.variants.log_growth`.

```lean
theorem erdos_491 :
    ∀ (f : ℕ → ℝ), (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
      (∃ C : ℝ, ∀ n : ℕ, |f (n + 1) - f n| < C) →
      ∃ c : ℝ, (fun n : ℕ ↦ f n - c * Real.log n) =O[atTop] (fun _ : ℕ ↦ (1 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/491.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/491.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/491.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/491.lean)
- [erdosproblems.com/491](https://www.erdosproblems.com/491)
