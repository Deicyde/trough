---
declaration: theorem
origin: cited
lean: Erdos936.erdos_936.variants.two_pow_add_one, Erdos936.erdos_936.variants.two_pow_sub_one, Erdos936.erdos_936.variants.factorial_add_one, Erdos936.erdos_936.variants.factorial_sub_one
statement: formalized
---

# Erdős Problem 936

> *Reference:* [erdosproblems.com/936](https://www.erdosproblems.com/936)

*Quoted from [FormalConjectures/ErdosProblems/936.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/936](https://www.erdosproblems.com/936).

The file states 4 research or textbook statements: 4 open.

## `Erdos936.erdos_936.variants.two_pow_add_one`

Open: stated without proof.

> Is $2^n + 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.two_pow_add_one :
   EventuallyNotPowerful (2 ^ · + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean#L39).

## `Erdos936.erdos_936.variants.two_pow_sub_one`

Open: stated without proof.

> Is $2^n - 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.two_pow_sub_one :
   EventuallyNotPowerful (2 ^ · - 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean#L45).

## `Erdos936.erdos_936.variants.factorial_add_one`

Open: stated without proof.

> Is $n! + 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.factorial_add_one :
   EventuallyNotPowerful (·! + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean#L51).

## `Erdos936.erdos_936.variants.factorial_sub_one`

Open: stated without proof.

> Is $n! - 1$ powerful for finitely many $n$?

```lean
theorem erdos_936.variants.factorial_sub_one :
   EventuallyNotPowerful (·! - 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/936.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/936.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/936.lean)
- [erdosproblems.com/936](https://www.erdosproblems.com/936)
