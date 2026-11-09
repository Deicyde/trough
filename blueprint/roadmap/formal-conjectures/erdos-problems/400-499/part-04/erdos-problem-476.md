---
declaration: theorem
origin: cited
lean: Erdos476.erdos_476
statement: formalized
---

# Erdős Problem 476

> *References:*
> - [erdosproblems.com/476](https://www.erdosproblems.com/476)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [dSHa94] Dias da Silva, J. A. and Hamidoune, Y. O., *Cyclic spaces for Grassmann
>   derivatives and additive theory*. Bull. London Math. Soc. (1994), 140-146.

*Quoted from [FormalConjectures/ErdosProblems/476.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/476.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/476](https://www.erdosproblems.com/476).

The file states 1 research or textbook statement: 1 solved.

## `Erdos476.erdos_476`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos476.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos476.lean).

> Let $A\subseteq \mathbb{F}_p$. Let
> $$
> A\hat{+}A = \{ a+b : a\neq b \in A\}.
> $$
> Is it true that
> $$
> \lvert A\hat{+}A\rvert \geq \min(2\lvert A\rvert-3,p)?
> $$
>
> This is the Erdős-Heilbronn inequality, proved by Dias da Silva and Hamidoune.

```lean
theorem erdos_476 :
    ∀ p : ℕ, Fact p.Prime → ∀ A : Finset (ZMod p),
      A.restrictedSumset.card ≥ min (2 * A.card - 3) p
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/476.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/476.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/476.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/476.lean)
- [erdosproblems.com/476](https://www.erdosproblems.com/476)
