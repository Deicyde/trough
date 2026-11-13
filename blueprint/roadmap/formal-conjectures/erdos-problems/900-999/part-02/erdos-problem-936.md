---
declaration: theorem
origin: cited
lean: Erdos936.erdos_936.variants.two_pow_add_one, Erdos936.erdos_936.variants.two_pow_sub_one, Erdos936.erdos_936.variants.factorial_add_one, Erdos936.erdos_936.variants.factorial_sub_one
statement: formalized
---

# Erdős Problem 936

> *Reference:* [erdosproblems.com/936](https://www.erdosproblems.com/936)

*Quoted from [FormalConjectures/ErdosProblems/936.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/936](https://www.erdosproblems.com/936).

The file states 4 research or textbook statements: 4 open.

## `Erdos936.erdos_936.variants.two_pow_add_one`

Open: stated without proof.

> Is $2^n + 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.two_pow_add_one :
   EventuallyNotPowerful (2 ^ · + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean#L39).

## `Erdos936.erdos_936.variants.two_pow_sub_one`

Open: stated without proof.

> Is $2^n - 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.two_pow_sub_one :
   EventuallyNotPowerful (2 ^ · - 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean#L45).

## `Erdos936.erdos_936.variants.factorial_add_one`

Open: stated without proof.

> Is $n! + 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.factorial_add_one :
   EventuallyNotPowerful (·! + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean#L51).

## `Erdos936.erdos_936.variants.factorial_sub_one`

Open: stated without proof.

> Is $n! - 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.factorial_sub_one :
   EventuallyNotPowerful (·! - 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/936.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/936.lean)
- [erdosproblems.com/936](https://www.erdosproblems.com/936)
