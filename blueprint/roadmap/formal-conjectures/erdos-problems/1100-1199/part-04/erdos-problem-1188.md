---
declaration: theorem
origin: cited
lean: Erdos1188.erdos_1188
statement: formalized
---

# Erdős Problem 1188

> *Reference:* [erdosproblems.com/1188](https://www.erdosproblems.com/1188)

*Quoted from [FormalConjectures/ErdosProblems/1188.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1188.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1188](https://www.erdosproblems.com/1188).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1188.erdos_1188`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-1188/Research/SparseAsymptotic.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-1188/Research/SparseAsymptotic.lean).

> Call a set of distinct integers $1\lt n_1\lt \cdots\lt n_k$ with associated congruence
> classes $a_i\pmod{n_i}$ a distinct covering system if every integer satisfies at
> least one of these congruences. A minimal distinct covering system is one such
> that no proper subset forms a covering system. Let $F(x)$ count the number of
> minimal distinct covering systems with all moduli in $[1,x]$. Estimate $F(x)$.
>
> The estimate is `log(log F(x)) / log x → 1`.

```lean
theorem erdos_1188 :
    Tendsto (fun x : ℕ => Real.log (Real.log (coveringCount x : ℝ)) / Real.log (x : ℝ))
      atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1188.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1188.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1188.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1188.lean)
- [erdosproblems.com/1188](https://www.erdosproblems.com/1188)
