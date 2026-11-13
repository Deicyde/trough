---
declaration: theorem
origin: cited
lean: Erdos417.erdos_417.parts.i, Erdos417.erdos_417.parts.ii
statement: formalized
---

# Erdős Problem 417

> *References:*
> - [erdosproblems.com/417](https://www.erdosproblems.com/417)
> - [Er98] Erdős, Paul, Some of my new and almost new problems and results in combinatorial number
>   theory. Number theory (Eger, 1996) (1998), 169-180.

*Quoted from [FormalConjectures/ErdosProblems/417.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/417.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/417](https://www.erdosproblems.com/417).

The file states 2 research or textbook statements: 2 open.

## `Erdos417.erdos_417.parts.i`

Open: stated without proof.

> Let
>
> $$V'(x)=\#\{\phi(m) : 1\leq m\leq x\}$$
>
> and
>
> $$V(x)=\#\{\phi(m) \leq x : 1\leq m\}.$$
>
> Does $\lim V(x)/V'(x)$ exist?

```lean
theorem erdos_417.parts.i :
    ∃ L : ENNReal, Tendsto (fun x ↦
      ({ k | k ∈ range totient ∧ (k : ℝ) ≤ x }.ncard : ENNReal) /
      ((totient '' { m | 1 ≤ m ∧ (m : ℝ) ≤ x }).ncard : ENNReal))
      atTop (𝓝 L)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/417.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/417.lean#L41).

## `Erdos417.erdos_417.parts.ii`

Open: stated without proof.

> Is it $>1$?

```lean
theorem erdos_417.parts.ii :
    ∃ L > (1 : ENNReal), Tendsto (fun x ↦
      ({ k | k ∈ range totient ∧ (k : ℝ) ≤ x }.ncard : ENNReal) /
      ((totient '' { m | 1 ≤ m ∧ (m : ℝ) ≤ x }).ncard : ENNReal))
      atTop (𝓝 L)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/417.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/417.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/417.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/417.lean)
- [erdosproblems.com/417](https://www.erdosproblems.com/417)
