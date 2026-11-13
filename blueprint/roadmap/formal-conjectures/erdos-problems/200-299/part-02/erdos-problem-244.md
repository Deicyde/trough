---
declaration: theorem
origin: cited
lean: Erdos244.erdos_244, Erdos244.erdos_244.variants.Romanoff
statement: formalized
---

# Erdős Problem 244

> *Reference:* [erdosproblems.com/244](https://www.erdosproblems.com/244)

*Quoted from [FormalConjectures/ErdosProblems/244.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/244.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/244](https://www.erdosproblems.com/244).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos244.erdos_244`

Open: stated without proof.

> Let $C > 1$. Does the set of integers of the form $p + \lfloor C^k \rfloor$,
> for some prime $p$ and $k\geq 0$, have density $>0$?

```lean
theorem erdos_244 :
    ∀ C > (1 : ℝ), 0 < { p + ⌊C ^ k⌋₊ | (p) (k) (_ : p.Prime) }.lowerDensity
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/244.lean, line 33](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/244.lean#L33).

## `Erdos244.erdos_244.variants.Romanoff`

Solved: stated here without proof.

> Romanoff [Ro34] proved that the answer is yes if $C$ is an integer.
>
> [Ro34] Romanoff, N. P., _Über einige Sätze der additiven Zahlentheorie_.
> Math. Ann. (1934), 668-678.

```lean
theorem erdos_244.variants.Romanoff {C : ℕ} (hC : 1 < C) :
    0 < { p + ⌊C ^ k⌋₊ | (p) (k) (_ : p.Prime) }.lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/244.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/244.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/244.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/244.lean)
- [erdosproblems.com/244](https://www.erdosproblems.com/244)
