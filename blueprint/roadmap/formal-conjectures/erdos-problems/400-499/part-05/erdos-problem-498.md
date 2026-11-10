---
declaration: theorem
origin: cited
lean: Erdos498.erdos_498
statement: formalized
---

# Erdős Problem 498

> *References:*
> - [erdosproblems.com/498](https://www.erdosproblems.com/498)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er45] Erdős, P., _On a lemma of Littlewood and Offord_. Bull. Amer. Math. Soc. (1945), 898-902.
> - [Kl65] Kleitman, Daniel J., _On a lemma of Littlewood and Offord on the distribution of certain
>   sums_. Math. Z. (1965), 251-259.
> - [Kl70] Kleitman, Daniel J., _On a lemma of Littlewood and Offord on the distributions of linear
>   combinations of vectors_. Advances in Math. (1970), 155-157.

*Quoted from [FormalConjectures/ErdosProblems/498.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/498.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/498](https://www.erdosproblems.com/498).

The file states 1 research or textbook statement: 1 solved.

## `Erdos498.erdos_498`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos498.lean#L2006](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos498.lean#L2006).

> Let $z_1,\ldots,z_n\in\mathbb{C}$ with $1\leq \lvert z_i\rvert$ for $1\leq i\leq n$. Let $D$ be an
> arbitrary disc of radius $1$. Is it true that the number of sums of the shape
>
> $$\sum_{i=1}^n\epsilon_iz_i \textrm{ for }\epsilon_i\in \{-1,1\}$$
>
> which lie in $D$ is at most $\binom{n}{\lfloor n/2\rfloor}$?
>
> A strong form of the Littlewood-Offord problem. Erdős [Er45] proved this is true if
> $z_i\in\mathbb{R}$, and for general $z_i\in\mathbb{C}$ proved a weaker upper bound of
>
> $$\ll \frac{2^n}{\sqrt{n}}.$$
>
> This was solved in the affirmative by Kleitman [Kl65], who also later generalised this to
> arbitrary Hilbert spaces [Kl70].
>
> See also [395].

```lean
theorem erdos_498 :
    ∀ (n : ℕ) (z : Fin n → ℂ), (∀ i, 1 ≤ ‖z i‖) → ∀ c : ℂ,
      {ε : Fin n → ℤ | (∀ i, ε i = -1 ∨ ε i = 1) ∧
        (∑ i, (ε i : ℂ) * z i) ∈ Metric.ball c 1}.ncard ≤ n.choose (n / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/498.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/498.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/498.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/498.lean)
- [erdosproblems.com/498](https://www.erdosproblems.com/498)
