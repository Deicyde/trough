---
declaration: theorem
origin: cited
lean: Erdos328.erdos_328
statement: formalized
---

# Erdős Problem 328

> *References:*
> - [erdosproblems.com/328](https://www.erdosproblems.com/328)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*.
>   Ann. Discrete Math. (1980), 89-115.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Er80e] Erdős, P., *Some applications of Ramsey's theorem to additive number theory*.
>   European J. Combin. (1980), 43-46.
> - [NeRo85] J. Nešetřil and V. Rödl, *Two proofs in combinatorial number theory*.
>   Proc. Amer. Math. Soc. (1985), 185-188.

*Quoted from [FormalConjectures/ErdosProblems/328.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/328.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/328](https://www.erdosproblems.com/328).

The file states 1 research or textbook statement: 1 solved.

## `Erdos328.erdos_328`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/328/Erdos328.lean](https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/328/Erdos328.lean).

> Suppose $A\subseteq\mathbb{N}$ and $C>0$ is such that $1_A\ast 1_A(n)\leq C$ for all
> $n\in\mathbb{N}$. Can $A$ be partitioned into $t$ many subsets $A_1,\ldots,A_t$ (where
> $t=t(C)$ depends only on $C$) such that $1_{A_i}\ast 1_{A_i}(n)\lt C$ for all $1\leq i\leq t$
> and $n\in \mathbb{N}$?
>
> The answer is no. Asked by Erdős and Newman. Nešetřil and Rödl [NeRo85] have shown the
> answer is no for all $C$ (even if $t$ is also allowed to depend on $A$).
>
> Erdős [Er80e] had previously shown the answer is no for $C=3,4$ and infinitely many other
> values of $C$.
>
> See also [774].
>
> The linked proof writes the representation function as
> `Set.ncard {p : ℕ × ℕ | p.1 ∈ A ∧ p.2 ∈ A ∧ p.1 + p.2 = n}`, which counts the same ordered
> pairs as `sumRep`, and states the partition condition as a named definition with the same two
> conjuncts used below. Its `∃ t` additionally carries `1 ≤ t`, which costs nothing: `t = 0`
> forces `A = ∅`, and `A = {1}` has all representation counts at most `C` for `C ≥ 1`.

```lean
theorem erdos_328 :
    ¬ ∀ C : ℕ, 0 < C →
      ∃ t : ℕ, ∀ A : Set ℕ, (∀ n, sumRep A n ≤ C) →
        ∃ P : Fin t → Set ℕ, (⋃ i, P i) = A ∧
          Set.univ.PairwiseDisjoint P ∧
          ∀ i, ∀ n, sumRep (P i) n < C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/328.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/328.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/328.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/328.lean)
- [erdosproblems.com/328](https://www.erdosproblems.com/328)
