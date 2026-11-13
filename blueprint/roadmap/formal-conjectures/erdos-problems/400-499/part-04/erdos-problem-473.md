---
declaration: theorem
origin: cited
lean: Erdos473.erdos_473, Erdos473.erdos_473.variants.finite
statement: formalized
---

# Erdős Problem 473

> *References:*
> - [erdosproblems.com/473](https://www.erdosproblems.com/473)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*, Monographies de L'Enseignement Mathématique (1980).

*Quoted from [FormalConjectures/ErdosProblems/473.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/473.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/473](https://www.erdosproblems.com/473).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos473.erdos_473`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos473.lean#L236](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos473.lean#L236).

> Is there a permutation $a_1, a_2, \ldots$ of the positive integers such that $a_k + a_{k+1}$ is
> always prime?
>
> A question of Segal [ErGr80, p.94]. The answer is yes, as shown by Odlyzko. The linked formal
> proof (Codex and GPT-5.6 Sol) builds the permutation as a spanning one-way ray of the graph on the
> positive integers in which two numbers are adjacent when their sum is prime.

```lean
theorem erdos_473 :
    ∃ a : ℕ ≃ ℕ+, ∀ n : ℕ, ((a n : ℕ) + (a (n + 1) : ℕ)).Prime
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/473.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/473.lean#L45).

## `Erdos473.erdos_473.variants.finite`

Open: stated without proof.

> Segal also asked whether for every $n \ge 2$ there is a permutation $a_1, \ldots, a_n$ of
> $\{1, \ldots, n\}$ such that $a_k + a_{k+1}$ is prime for all $1 \le k < n$. This is conjectured to
> be true, and has been verified for infinitely many $n$.

```lean
theorem erdos_473.variants.finite :
    ∀ n : ℕ, 2 ≤ n → ∃ a : Fin n ≃ Fin n, ∀ k : Fin n, ∀ h : k.val + 1 < n,
      ((a k).val + 1 + ((a ⟨k.val + 1, h⟩).val + 1)).Prime
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/473.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/473.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/473.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/473.lean)
- [erdosproblems.com/473](https://www.erdosproblems.com/473)
