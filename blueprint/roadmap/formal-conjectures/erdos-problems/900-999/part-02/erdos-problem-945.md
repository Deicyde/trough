---
declaration: theorem
origin: cited
lean: Erdos945.erdos_945, Erdos945.erdos_945.variants.constant, Erdos945.erdos_945.variants.equivalence, Erdos945.erdos_945.variants.lower_bound, Erdos945.erdos_945.variants.upper_bound
statement: formalized
---

# Erdős Problem 945

> *References:*
>  - [erdosproblems.com/945](https://www.erdosproblems.com/945)
>  - [ErMi52] Erdős, P. and Mirsky, L., The distribution of values of the divisor function {$d(n)$}. Proc. London Math. Soc. (3) (1952), 257--271.

*Quoted from [FormalConjectures/ErdosProblems/945.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/945](https://www.erdosproblems.com/945).

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result.

## `Erdos945.erdos_945`

Open: stated without proof.

> Is it true that $F(x) \leq (\log x)^{O(1)}$?

```lean
theorem erdos_945 : Erdos945Prop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/945.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean#L51).

## `Erdos945.erdos_945.variants.constant`

Open: stated without proof.

> Is there a constant $C > 0$ such that, for all large $x$, every interval $[x, x+(\log x)C]$
> contains two integers with the same number of divisors?

```lean
theorem erdos_945.variants.constant : Erdos945Constant
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/945.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean#L66).

## `Erdos945.erdos_945.variants.equivalence`

Textbook result, stated without proof.

> The two ways of phrasing the conjecture are equivalent.

```lean
theorem erdos_945.variants.equivalence : Erdos945Prop ↔ Erdos945Constant
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/945.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean#L74).

## `Erdos945.erdos_945.variants.lower_bound`

Solved: stated here without proof.

> Erdős and Mirsky [ErMi52] proved that $\frac{(\log x)^{1/2}}{\log\log x}\ll F(x)$.

```lean
theorem erdos_945.variants.lower_bound :
    (fun (x : ℕ) => (log x).sqrt /(log x).log) =O[atTop] fun (n : ℕ) => (F n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/945.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean#L81).

## `Erdos945.erdos_945.variants.upper_bound`

Solved: stated here without proof.

> Erdős and Mirsky [ErMi52] proved that $\log F(x) \ll \frac{(\log x)^{1/2}}$.

```lean
theorem erdos_945.variants.upper_bound :
    (fun (n : ℕ) => (F n : ℝ).log) =O[atTop] fun (x : ℕ) => (log x).sqrt /(log x).log
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/945.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/945.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/945.lean)
- [erdosproblems.com/945](https://www.erdosproblems.com/945)
