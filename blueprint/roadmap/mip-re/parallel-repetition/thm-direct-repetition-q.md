---
declaration: theorem
origin: cited
lean: MIPRE.Repetition.quantumValue_repeat_le
statement: formalized
proof: formalized
---

# Direct parallel repetition for entangled strategies

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] There is a universal constant $c > 0$ such that for every game $\mathfrak{G}$ with nonempty answer alphabets and $\mathrm{val}^*(\mathfrak{G}) < 1$, and every integer $n \geq 1$, writing $\varepsilon = 1 - \mathrm{val}^*(\mathfrak{G})$,

$$
\mathrm{val}^*\bigl( \mathfrak{G}^{n} \bigr) \;\leq\;
\exp\Bigl( - \frac{c\, \varepsilon^{13}\, n}{\varepsilon + \log\bigl(\left\vert {{\mathcal{A}}} \right\vert\,\left\vert {{\mathcal{B}}} \right\vert\bigr)} \Bigr)\;.
$$

## Depends on

- [Direct repetition](def-direct-repetition.md)
- [Quantum value](../foundations/part-01/def-q-value.md)
- [Mixed states and POVMs do not change the quantum value](lem-povm-value-eq.md)

## Proof

This is the main theorem of Chapter 6 of (OpenAI26), whose Lean proof is vendored at `MIPRE/Background/Repetition/TenProofs/`. Its entangled value is defined with a density matrix on the product of two finite sets and POVMs; Lemma [Mixed states and POVMs do not change the quantum value](lem-povm-value-eq.md) identifies it with $\mathrm{val}^*$ (Definition [Quantum value](../foundations/part-01/def-q-value.md)), after which the two direct repetitions are literally the same construction.

## Lean

Formalized as [`MIPRE.Repetition.quantumValue_repeat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.quantumValue_repeat_le).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 172](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L172)
