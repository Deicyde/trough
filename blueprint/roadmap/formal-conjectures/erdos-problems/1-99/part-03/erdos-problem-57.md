---
declaration: theorem
origin: cited
lean: Erdos57.erdos_57
statement: formalized
---

# Erdős Problem 57

> *References:*
> - [erdosproblems.com/57](https://www.erdosproblems.com/57)
> - [ErHa66] Erdős, P. and Hajnal, A., *On chromatic number of graphs and set-systems*.
>   Acta Math. Acad. Sci. Hungar. (1966), 61-99.
> - [LiMo20] Liu, Hong and Montgomery, Richard, *A solution to Erdős and Hajnal's odd cycle problem*.
>   arXiv:2010.15802 (2020).

*Quoted from [FormalConjectures/ErdosProblems/57.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/57.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/57](https://www.erdosproblems.com/57).

The file states 1 research or textbook statement: 1 solved.

## `Erdos57.erdos_57`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos57.lean#L11124](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos57.lean#L11124).

> If $G$ is a graph with infinite chromatic number and $a_1 < a_2 < \cdots$ are lengths of the odd
> cycles of $G$ then $\sum \frac{1}{a_i} = \infty$.
>
> Conjectured by Erdős and Hajnal [ErHa66], and solved by Liu and Montgomery [LiMo20].
>
> The linked formal proof (Codex and GPT-5.6 Sol) states the conclusion as
> `¬ Summable (oddCycleReciprocal G)`, where `oddCycleReciprocal G n` is `n⁻¹` if `n` is an odd
> cycle length of `G` and `0` otherwise; this is the indicator form of the sum below.

```lean
theorem erdos_57 :
    ∀ {V : Type*} (G : SimpleGraph V), G.chromaticNumber = ⊤ →
      ¬ Summable (fun (a : G.oddCycleLengths) ↦ 1 / (a : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/57.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/57.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/57.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/57.lean)
- [erdosproblems.com/57](https://www.erdosproblems.com/57)
