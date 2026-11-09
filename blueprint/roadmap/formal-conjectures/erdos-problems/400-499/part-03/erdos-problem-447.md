---
declaration: theorem
origin: cited
lean: Erdos447.erdos_447.parts.i, Erdos447.erdos_447.parts.ii
statement: formalized
---

# Erdős Problem 447

> *References:*
> - [erdosproblems.com/447](https://www.erdosproblems.com/447)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Kl71] Kleitman, Daniel, *Collections of subsets containing no two sets and their union*.
>   Proceedings of the LA Meeting AMS (1971), 153-155.

*Quoted from [FormalConjectures/ErdosProblems/447.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/447.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/447](https://www.erdosproblems.com/447).

The file states 2 research or textbook statements: 2 solved.

## `Erdos447.erdos_447.parts.i`

Solved: stated here without proof.

> How large can a union-free collection $\mathcal{F}$ of subsets of $[n]$ be? By union-free we mean
> there are no solutions to $A\cup B=C$ with distinct $A,B,C\in \mathcal{F}$. Must
> $\lvert \mathcal{F}\rvert =o(2^n)$?
>
> In [Er65b] Erdős reported that the estimate $\lvert \mathcal{F}\rvert=o(2^n)$ was proved in
> unpublished work by Sárközy and Szemerédi.

```lean
theorem erdos_447.parts.i :
    (fun n : ℕ => (maxUnionFree n : ℝ)) =o[atTop] (fun n : ℕ => (2 : ℝ) ^ n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/447.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/447.lean#L50).

## `Erdos447.erdos_447.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos447.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos447.lean).

> How large can a union-free collection $\mathcal{F}$ of subsets of $[n]$ be? By union-free we mean
> there are no solutions to $A\cup B=C$ with distinct $A,B,C\in \mathcal{F}$. Perhaps even
> $$\lvert \mathcal{F}\rvert <(1+o(1))\binom{n}{\lfloor n/2\rfloor}?$$
>
> Solved by Kleitman [Kl71], who proved
> $$\lvert \mathcal{F}\rvert <(1+o(1))\binom{n}{\lfloor n/2\rfloor}.$$

```lean
theorem erdos_447.parts.ii :
    ∃ c : ℕ → ℝ, (c =o[atTop] (1 : ℕ → ℝ)) ∧ ∀ᶠ n : ℕ in atTop,
      (maxUnionFree n : ℝ) < (1 + c n) * (n.choose (n / 2) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/447.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/447.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/447.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/447.lean)
- [erdosproblems.com/447](https://www.erdosproblems.com/447)
