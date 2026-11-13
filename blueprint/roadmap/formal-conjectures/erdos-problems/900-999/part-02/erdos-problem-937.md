---
declaration: theorem
origin: cited
lean: Erdos937.erdos_937
statement: formalized
---

# Erdős Problem 937

> *Reference:* [erdosproblems.com/937](https://www.erdosproblems.com/937)
>
> *References:*
>  * [BBC24] Bajpai, P., Bennett, M. A. and Chan, T. H., _Arithmetic progressions in squarefull /
>    powerful numbers_, Int. J. Number Theory 20 (2024), 19-45.

*Quoted from [FormalConjectures/ErdosProblems/937.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/937.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/937](https://www.erdosproblems.com/937).

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos937.erdos_937`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos937.lean#L1031](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos937.lean#L1031).

> Are there infinitely many four-term arithmetic progressions of coprime powerful numbers?
> (A number $n$ is *powerful* if $p \mid n \to p^2 \mid n$; `Nat.Powerful`.)
>
> Erdős [Er76d] asked this; the answer is **yes**: Bajpai, Bennett and Chan [BBC24] proved that
> there are infinitely many four-term arithmetic progressions of pairwise coprime powerful numbers.
> (Without coprimality this is easy, and by a theorem of Fermat there are no four *squares* in
> arithmetic progression.)

```lean
theorem erdos_937 :
    {p : ℕ × ℕ | IsCoprimePowerfulAP4 p.1 p.2}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/937.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/937.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/937.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/937.lean)
- [erdosproblems.com/937](https://www.erdosproblems.com/937)
