---
declaration: lemma
origin: cited
lean: Erdos198.baumgartner_strong, Erdos198.baumgartner_headline, Erdos198.erdos_198, Erdos198.erdos_198.variants.concrete
statement: formalized
---

# Erdős Problem 198

> *References:*
> - [erdosproblems.com/198](https://www.erdosproblems.com/198)
> - [Ba75] Baumgartner, James E., Partitioning vector spaces. J. Combinatorial Theory Ser. A (1975),
>   231-233.

*Quoted from [FormalConjectures/ErdosProblems/198.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/198](https://www.erdosproblems.com/198).

The file states 4 research or textbook statements: 4 solved.

## `Erdos198.baumgartner_strong`

Solved: stated here without proof.

> Let $V$ be a vector space over the rationals and let $k$ be a fixed
> positive integer. Then there is a set $X_k \subseteq V$ such that $X_k$ meets
> every infinite arithmetic progression in $V$ but $X_k$ intersects every
> $k$-element arithmetic progression in at most two points.
>
> At the end of [Ba75] the author claims that by "slightly modifying the method of [his proof]", one
> can prove this.

```lean
lemma baumgartner_strong (V : Type*) [AddCommGroup V] [Module ℚ V] (k : ℕ) :
    ∃ X : Set V,
      (∀ Y, Y.IsAPOfLength ⊤ → (X ∩ Y).Nonempty) ∧
      (∀ Y, IsAPOfLength Y k → (X ∩ Y).ncard ≤ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/198.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean#L43).

## `Erdos198.baumgartner_headline`

Proved here.

> The statement for which Baumgartner actually writes a proof.

```lean
lemma baumgartner_headline (V : Type*) [AddCommGroup V] [Module ℚ V] :
    ∃ X : Set V,
      (∀ Y, IsAPOfLength Y ⊤ → (X ∩ Y).Nonempty) ∧
      (∀ Y, IsAPOfLength Y 3 → (X ∩ Y).ncard ≤ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/198.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean#L51).

## `Erdos198.erdos_198`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos198.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos198.lean).

> The answer is no; Erdős and Graham report this was proved by Baumgartner, presumably referring to
> the paper [Ba75], which does not state this exactly, but the following simple construction is
> implicit in [Ba75].
>
> Let $P_1,P_2,\ldots$ be an enumeration of all countably many infinite arithmetic progressions. We
> choose $a_1$ to be the minimal element of $P_1\cap \mathbb{N}$, and in general choose $a_n$ to be an
> element of $P_n\cap \mathbb{N}$ such that $a_n>2a_{n-1}$. By construction $A=\{a_1 < a_2 < \cdots\}$
> contains at least one element from every infinite arithmetic progression, and is a lacunary set, so
> is certainly Sidon.
>
> AlphaProof has found the following explicit construction: $A = \{ (n+1)!+n : n\geq 0\}$. This is a
> Sidon set, and intersects every arithmetic progression, since for any $a,d\in \mathbb{N}$,
> $(a+d+1)!+(a+d)\in A$, and $d$ divides $(a+d+1)!+d$.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_198 : ¬ (∀ A : Set ℕ, IsSidon A → (∃ Y, IsAPOfLength Y ⊤ ∧ Y ⊆ Aᶜ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/198.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean#L77).

## `Erdos198.erdos_198.variants.concrete`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/21f6780f84b406de468389571eb01717b8072f09/FormalConjectures/ErdosProblems/198.lean#L84](https://github.com/mzhorvath1/formal-conjectures/blob/21f6780f84b406de468389571eb01717b8072f09/FormalConjectures/ErdosProblems/198.lean#L84).

> In fact one such sequence is $n! + n$.
>
> This was found and proved by AlphaProof.
>
> It also found $(n + 1)! + n$.

```lean
theorem erdos_198.variants.concrete :  ∃ (A : Set ℕ), A = {n ! + n | n} ∧
    IsSidon A ∧ (∀ Y, IsAPOfLength Y ⊤ → (A ∩ Y).Nonempty)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/198.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/198.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/198.lean)
- [erdosproblems.com/198](https://www.erdosproblems.com/198)
