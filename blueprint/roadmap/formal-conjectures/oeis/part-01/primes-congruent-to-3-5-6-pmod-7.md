---
declaration: theorem
origin: cited
lean: OeisA3625.conjecture
statement: formalized
---

# Primes congruent to $\{3, 5, 6\} \pmod 7$

> Primes congruent to $3, 5, \text{ or } 6 \pmod 7$.
>
> *References:*
> - [A003625](https://oeis.org/A003625)

*Quoted from [FormalConjectures/OEIS/3625.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3625.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA3625.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a003625-irreducibility/blob/d6c9f90827805142d81eee4e3d9099c8b48cbcc8/lean/OeisA3625FC.lean#L103-L104](https://github.com/KitaKen1/oeis-a003625-irreducibility/blob/d6c9f90827805142d81eee4e3d9099c8b48cbcc8/lean/OeisA3625FC.lean#L103-L104).

> Conjecture: Represents primes $p$ where the polynomial $x^2 + x + 2$ is irreducible over $\text{GF}(p)$.
> - _Federico Provvedi_, Jul 21 2018
>
> Answer: true, the equivalence is classical (complete the square: $4(x^2+x+2) = (2x+1)^2 + 7$,
> then use quadratic reciprocity).

```lean
theorem conjecture (p : ℕ) (hp : p.Prime) :
    A p ↔ Irreducible (X ^ 2 + X + 2 : (ZMod p)[X])
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/3625.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3625.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/3625.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/3625.lean)
- [A003625](https://oeis.org/A003625)
