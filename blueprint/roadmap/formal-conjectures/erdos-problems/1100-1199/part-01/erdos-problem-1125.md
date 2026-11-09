---
declaration: theorem
origin: cited
lean: Erdos1125.erdos_1125
statement: formalized
---

# Erdős Problem 1125

> *References:*
> - [erdosproblems.com/1125](https://www.erdosproblems.com/1125)
> - [Er81b] Erdős, P., *My Scottish Book 'Problems'*. The Scottish Book (1981), 27-35.
> - [Ke69] Kemperman, J. H. B., *On the regularity of generalized convex functions*. Trans. Amer. Math. Soc. (1969), 69-93.
> - [La84] Laczkovich, M., *On Kemperman's inequality $2f(x)\leq f(x+h)+f(x+2h)$*. Colloq. Math. (1984), 109-115.

*Quoted from [FormalConjectures/ErdosProblems/1125.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1125.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1125](https://www.erdosproblems.com/1125).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1125.erdos_1125`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1125.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1125.lean).

> Let $f:\mathbb{R}\to \mathbb{R}$ be such that
> $$2f(x) \leq f(x+h)+f(x+2h)$$
> for every $x\in \mathbb{R}$ and $h>0$. Must $f$ be monotonic?
>
> A problem of Kemperman [Ke69], who proved it is true if $f$ is measurable. Erdős [Er81b] wrote 'if it were my problem I would offer \$500 for it'. This was solved by Laczkovich [La84].

```lean
theorem erdos_1125 : ∀ (f : ℝ → ℝ)
    (hf : ∀ x : ℝ, ∀ h : ℝ, h > 0 → 2 * f x ≤ f (x + h) + f (x + 2 * h)),
    Monotone f
```

Category `research solved`; AMS [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/ErdosProblems/1125.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1125.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1125.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1125.lean)
- [erdosproblems.com/1125](https://www.erdosproblems.com/1125)
