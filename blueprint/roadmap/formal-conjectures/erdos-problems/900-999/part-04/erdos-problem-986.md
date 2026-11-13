---
declaration: theorem
origin: cited
lean: Erdos986.erdos_986
statement: formalized
---

# Erdős Problem 986

> *References:*
> - [erdosproblems.com/986](https://www.erdosproblems.com/986)
> - [ChGr98] Chung, F. and Graham, R., *Erdős on Graphs: His Legacy of Unsolved Problems*.
>   A K Peters, Ltd. (1998).
> - [Br26] Bradač, D., Off-diagonal Ramsey numbers. arXiv:2605.28793 (2026).
> - [Sp77] Spencer, J., Asymptotic lower bounds for Ramsey functions. Discrete Math. (1977), 69-76.
> - [MaVe23] Mattheus, S. and Verstraëte, J., The asymptotics of $r(4,t)$. Ann. of Math. (2024),
>   941-965.

*Quoted from [FormalConjectures/ErdosProblems/986.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/986.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/986](https://www.erdosproblems.com/986).

The file states 1 research or textbook statement: 1 solved.

## `Erdos986.erdos_986`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos986.lean#L92](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos986.lean#L92).

> For any fixed $s\geq 3$,
>
> $$R(s,k) \gg \frac{k^{s-1}}{(\log k)^c}$$
>
> for some constant $c=c(s)>0$.
>
> According to Chung and Graham [ChGr98] this was first conjectured by Erdős in 1947.
>
> Proved by Bradač [Br26], with $c=2s-4$.
>
> The linked formal proof (Codex and GPT-5.6 Sol) gives `k ^ (s - 1) / (log k) ^ c = O(R(s, k))`
> for a natural `c > 0`, with the Ramsey number defined through `CliqueFree`/`IndepSetFree`; this
> implies the statement below.

```lean
theorem erdos_986 :
    ∀ (s : ℕ) (hs : 3 ≤ s),
      ∃ (c C : ℝ), 0 < c ∧ 0 < C ∧
        ∀ᶠ (k : ℕ) in atTop,
          (SimpleGraph.classicalRamsey s k : ℝ) ≥
            C * (k : ℝ) ^ (s - 1) / (Real.log k) ^ c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/986.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/986.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/986.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/986.lean)
- [erdosproblems.com/986](https://www.erdosproblems.com/986)
