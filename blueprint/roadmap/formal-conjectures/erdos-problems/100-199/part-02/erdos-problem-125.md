---
declaration: theorem
origin: cited
lean: Erdos125.erdos_125, Erdos125.erdos_125.variants.positive_lower_density, Erdos125.erdos_125.variants.positive_upper_density, Erdos125.erdos_125.variants.zero_density, Erdos125.erdos_125.variants.zero_lower_positive_upper_density, Erdos125.erdos_125.variants.positive_unequal_density
statement: formalized
---

# Erdős Problem 125

> *Reference:* [erdosproblems.com/125](https://www.erdosproblems.com/125)
>
> There are four possibilities for the density of $A+B$:
> 1. $A+B$ has zero upper and lower density (and hence also zero density).
> 2. $A+B$ has zero lower density, but positive upper density (and hence no density).
> 3. $A+B$ has positive upper and lower density that are equal (and hence positive density).
> 4. $A+B$ has positive upper and lower density that are unequal (and hence no density).

*Quoted from [FormalConjectures/ErdosProblems/125.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/125](https://www.erdosproblems.com/125).

The file states 6 research or textbook statements: 3 open and 3 solved.

## `Erdos125.erdos_125`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/300bf771bdbef43d7b9aa2521e633a50fd54dd28/FormalConjectures/ErdosProblems/125.lean](https://github.com/google-deepmind/formal-conjectures/blob/300bf771bdbef43d7b9aa2521e633a50fd54dd28/FormalConjectures/ErdosProblems/125.lean).

> Case 3:
> Does $A + B$ have positive upper and lower density that are equal?
> This is the literal interpretation of "positive density" which was falsified.

```lean
theorem erdos_125 :
    ¬ (A + B).HasPosDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L67).

## `Erdos125.erdos_125.variants.positive_lower_density`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/c27415379b5dbe34105d1fdd707994540c4c6fc7/FormalConjectures/ErdosProblems/125.lean#L468](https://github.com/mo271/formal-conjectures/blob/c27415379b5dbe34105d1fdd707994540c4c6fc7/FormalConjectures/ErdosProblems/125.lean#L468).

> Literature question:
> Does $A + B$ have positive lower density?
>
> This has been falsified.

```lean
theorem erdos_125.variants.positive_lower_density :
    ¬ 0 < (A + B).lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L80).

## `Erdos125.erdos_125.variants.positive_upper_density`

Open: stated without proof.

> Literature question:
> Does $A + B$ have positive upper density?

```lean
theorem erdos_125.variants.positive_upper_density :
    0 < (A + B).upperDensity
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L90).

## `Erdos125.erdos_125.variants.zero_density`

Open: stated without proof.

> Case 1:
> Does $A + B$ have zero upper and lower density?

```lean
theorem erdos_125.variants.zero_density :
    (A + B).upperDensity = 0 ∧ (A + B).lowerDensity = 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L99).

## `Erdos125.erdos_125.variants.zero_lower_positive_upper_density`

Open: stated without proof.

> Case 2:
> Does $A + B$ have zero lower density, but positive upper density?

```lean
theorem erdos_125.variants.zero_lower_positive_upper_density :
    (A + B).lowerDensity = 0 ∧ 0 < (A + B).upperDensity
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L108).

## `Erdos125.erdos_125.variants.positive_unequal_density`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/0bc740d2351c53713e66d9340e83f7d2c1ddecab/FormalConjectures/ErdosProblems/125.lean#L860](https://github.com/mo271/formal-conjectures/blob/0bc740d2351c53713e66d9340e83f7d2c1ddecab/FormalConjectures/ErdosProblems/125.lean#L860).

> Case 4:
> Does $A + B$ have positive upper and lower density that are unequal?
>
> This follows from the disproof `erdos_125.variants.positive_lower_density` above.

```lean
theorem erdos_125.variants.positive_unequal_density :
    ¬ (0 < (A + B).lowerDensity ∧ (A + B).lowerDensity < (A + B).upperDensity)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/125.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/125.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/125.lean)
- [erdosproblems.com/125](https://www.erdosproblems.com/125)
