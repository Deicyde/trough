---
declaration: section
origin: cited
lean: OAI.QAC.parity_lower_bound, OAI.QAC.parity_lower_bound_polynomial_size
statement: formalized
proof: formalized
---

# 274. Parity is not in QAC$^{0}$

2 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Moore's parity conjecture in the measured-output model: constant-depth quantum circuits with arbitrary one-qubit gates, unbounded-arity Toffoli gates and polynomially many total qubits cannot compute parity with any fixed positive worst-case advantage. Ancillas start in zero, one output qubit is measured, and all other registers may be discarded. Xu–Li's reductions give the same bounded-error obstruction for strict majority.

## Product-projection localization and the QAC0 parity lower bound

We prove that constant-depth quantum circuits with arbitrary one-qubit and unbounded-arity Toffoli gates cannot compute parity with any fixed positive worst-case advantage using polynomially many qubits. Ancillas start in zero, only one output qubit is measured, and all final garbage is unrestricted. This resolves Moore's parity conjecture in the measured-output model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Regular trajectories, pruning and quantum parity

We prove that constant-depth quantum circuits with arbitrary one-qubit gates and unbounded-arity Toffoli gates cannot compute parity with any fixed positive worst-case advantage using polynomially many total qubits. Ancillary qubits are initialized to $|0\rangle$, one output qubit is measured, and all other final registers may be discarded without restriction. This resolves Moore's parity conjecture in the measured-output model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization rules out bounded-error parity computation by constant-depth quantum circuits with polynomially many zero-initialized ancillary qubits. For every fixed depth, polynomial bound on the total number of qubits, and $0<\varepsilon\le1/2$, every sufficiently large input length has an input on which the measured-output parity success probability is less than $1/2+\varepsilon$. A companion specialization gives success strictly below $2/3$. The formalization also includes the product-projection localization estimate supporting this bound.

The formalized result supplies the polynomial-size parity consequence of the paper. For every fixed circuit depth and polynomial bound on the number of qubits, all sufficiently large input lengths have an input on which any such circuit computes measured-output parity with probability strictly below $2/3$. Ancillary qubits start at zero. The formalization also contains the general positive-advantage parity bound and its product-projection localization estimate; regular-trajectory propagation and pruning are not separate formalized statements here.

## Lean: Constant-depth quantum parity lower bound

Stated in [QACParity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QACParity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem QAC.parity_lower_bound : QAC.ParityStatement
```

Proved in [lean/OAI/InformationTheory/QuantumCircuit/Parity.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/QuantumCircuit/Parity.lean#L45).

## Lean: Polynomial-size parity specialization

Stated in [RegularParity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RegularParity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem parity_lower_bound_polynomial_size (d k C : ℕ)
    (_hd : 0 < d) (_hk : 0 < k) (_hC : 0 < C) :
    ∃ n₀ : ℕ, ∀ n ≥ n₀, ∀ N : ℕ, n ≤ N → N ≤ C * (n + 1) ^ k →
      ∀ layers : List (PhysicalLayer N), layers.length ≤ d →
        ∀ out : Fin N, ∃ x : Word n,
          successProbability (physicalCircuitMatrix layers) out x < (2 : ℝ) / 3
```

Proved in [lean/OAI/InformationTheory/QuantumCircuit/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/QuantumCircuit/Main.lean#L12).

## Lean: Polynomial-size quantum parity lower bound

Stated in [RegularParity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RegularParity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem parity_lower_bound_polynomial_size (d k C : ℕ)
    (_hd : 0 < d) (_hk : 0 < k) (_hC : 0 < C) :
    ∃ n₀ : ℕ, ∀ n ≥ n₀, ∀ N : ℕ, n ≤ N → N ≤ C * (n + 1) ^ k →
      ∀ layers : List (PhysicalLayer N), layers.length ≤ d →
        ∀ out : Fin N, ∃ x : Word n,
          successProbability (physicalCircuitMatrix layers) out x < (2 : ℝ) / 3
```

Proved in [lean/OAI/InformationTheory/QuantumCircuit/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/QuantumCircuit/Main.lean#L12).

## Lean: General positive-advantage parity lower bound

Stated in [QACParity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QACParity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem QAC.parity_lower_bound : QAC.ParityStatement
```

Proved in [lean/OAI/InformationTheory/QuantumCircuit/Parity.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/QuantumCircuit/Parity.lean#L45).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/274.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/274.md)
