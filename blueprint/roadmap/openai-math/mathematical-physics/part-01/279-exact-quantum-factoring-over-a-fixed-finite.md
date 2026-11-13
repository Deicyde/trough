---
declaration: section
origin: cited
lean: OAI.ExactQuantumFactoring.exact_quantum_factoring
statement: formalized
proof: formalized
---

# 279. Exact quantum factoring over a fixed finite gate set

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a polynomial-time uniform quantum circuit family that outputs the complete prime factorization of every integer with probability one. Both gate count and qubit count are polynomial in the input length, and one fixed finite gate set suffices.

## Exact quantum factoring over a fixed finite gate set

We give a polynomial-time uniform quantum circuit family that outputs the complete prime factorization of every integer *N* ≥ 2 with probability one. A fixed finite set of bounded-arity gates suffices, and both the gate count and the number of qubits have polynomial worst-case bounds in the input length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization constructs a polynomial-time uniform quantum circuit family that outputs the complete prime factorization of every integer $N\ge2$ with probability exactly one. The circuits use one fixed finite set of bounded-arity gates, and both the gate count and number of qubits have polynomial worst-case bounds in the bit length of $N$. The probability-one conclusion is exact, rather than an asymptotic or bounded-error guarantee.

## Lean: Exact quantum factoring over a fixed finite gate set

```lean
theorem exact_quantum_factoring : MainTheorem
```

Stated in [ExactQuantumFactoring.lean, line 149](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ExactQuantumFactoring.lean#L149). Proved in [lean/OAI/Computability/QuantumFactoring/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/QuantumFactoring/Main.lean#L17).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/279.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/279.md)
