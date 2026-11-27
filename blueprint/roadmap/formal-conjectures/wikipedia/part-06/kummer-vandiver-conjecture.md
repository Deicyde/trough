---
declaration: theorem
origin: cited
lean: KummerVandiver.kummer_vandiver
statement: formalized
---

# Kummer–Vandiver conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Kummer%E2%80%93Vandiver_conjecture)

*Quoted from [FormalConjectures/Wikipedia/KummerVandiver.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KummerVandiver.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `KummerVandiver.kummer_vandiver`

Open: stated without proof.

> Kummer–Vandiver conjecture states that for every prime $p$, the class number of the maximal
> real subfield of $\mathbb{Q}(\zeta_p)$ is not divisible by $p$.
> -

```lean
theorem kummer_vandiver (p : ℕ+) (hp : p.Prime) :
    ¬ ↑p ∣ (classNumber (maximalRealSubfield (CyclotomicField p ℚ)))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/KummerVandiver.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KummerVandiver.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/KummerVandiver.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/KummerVandiver.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Kummer%E2%80%93Vandiver_conjecture)
