---
declaration: section
origin: cited
---

# 283. Polynomial-time unitary synthesis from a Boolean oracle

1 manuscript, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Solves the constant-error Aaronson–Kuperberg unitary synthesis problem: a uniform polynomial-size quantum oracle circuit approximates every *n*-qubit unitary channel within diamond-norm error 1/2, after a suitable Boolean oracle is chosen. Gates, qubits, oracle calls and query length are polynomially bounded. The target-dependent oracle may have an unrestricted truth table; its efficient classical construction is not asserted.

## Polynomial-Time Unitary Synthesis from a Boolean Oracle

We give a positive answer to the constant-error formulation of the Aaronson–Kuperberg unitary synthesis problem. For every *n*, a quantum oracle circuit generated in polynomial time from *n* alone can approximate the channel of every *n*-qubit unitary to full diamond-norm error at most 1/2, after a suitable Boolean oracle is chosen. Using the fixed gates $H,T,T^\dagger,\mathrm{CNOT}$, the circuit has polynomially many qubits, elementary gates, and oracle calls, and its oracle queries have polynomial length. The oracle may depend on the target unitary; the theorem does not give an efficient classical procedure for constructing it.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/paper.pdf).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
