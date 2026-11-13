---
declaration: theorem
origin: cited
lean: Erdos481.erdos_481
statement: formalized
---

# Erdős Problem 481

> *References:*
> - [erdosproblems.com/481](https://www.erdosproblems.com/481)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980), p.96.
> - [Kl82] Klarner, David A., *A sufficient condition for certain semigroups to be free*.
>   J. Algebra (1982), 140-148.
> - [KoTa22] Kolpakov, Alexander and Talambutsa, Alexey, *On free semigroups of affine maps on the
>   real line*. Proc. Amer. Math. Soc. (2022), 2301-2307.

*Quoted from [FormalConjectures/ErdosProblems/481.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/481.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/481](https://www.erdosproblems.com/481).

The file states 1 research or textbook statement: 1 solved.

## `Erdos481.erdos_481`

Solved: stated here without proof.

> Let $a_1,\ldots,a_r,b_1,\ldots,b_r\in \mathbb{N}$ such that $\sum_{i}\frac{1}{a_i}>1$. For any
> finite sequence of $n$ (not necessarily distinct) integers $A=(x_1,\ldots,x_n)$ let $T(A)$ denote
> the sequence of length $rn$ given by
>
> $$(a_ix_j+b_i)_{1\leq j\leq n, 1\leq i\leq r}.$$
>
> Prove that, if $A_1=(1)$ and $A_{i+1}=T(A_i)$, then there must be some $A_k$ with repeated
> elements.
>
> This is true. This appears to have first been shown by Klarner [Kl82], with a generalisation
> given by Kolpakov and Talambutsa [KoTa22]. Essentially the same proof was found independently by
> Barreto in the comment section.

```lean
theorem erdos_481 {r : ℕ} (a b : Fin r → ℕ) (ha : ∀ i, 0 < a i)
    (hab : 1 < ∑ i, (1 : ℝ) / a i) :
    ∃ k, ¬ ((T a b)^[k] [1]).Nodup
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/481.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/481.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/481.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/481.lean)
- [erdosproblems.com/481](https://www.erdosproblems.com/481)
