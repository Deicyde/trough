---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.quantumValue_eq_entangledValue
statement: formalized
proof: formalized
---

# Mixed states and POVMs do not change the quantum value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] Let $\mathrm{val}^*_{\mathrm{POVM}}(\mathfrak{G})$ be the supremum of the winning probabilities $\sum_{x,y,a,b} \mu(x,y)\, D(x,y,a,b)\, \operatorname{tr}\bigl( (A^x_a \otimes B^y_b)\, \rho \bigr)$ over all finite sets $S_\textsc{A}$, $S_\textsc{B}$, density matrices $\rho$ on $\mathbb{C}^{S_\textsc{A}} \otimes \mathbb{C}^{S_\textsc{B}}$ and POVMs $\{A^x_a\}$ on $\mathbb{C}^{S_\textsc{A}}$, $\{B^y_b\}$ on $\mathbb{C}^{S_\textsc{B}}$. Then $\mathrm{val}^*_{\mathrm{POVM}}(\mathfrak{G}) = \mathrm{val}^*(\mathfrak{G})$.

## Depends on

- [Tensor-product strategy](../foundations/part-01/def-tensor-strategy.md)
- [Quantum value](../foundations/part-01/def-q-value.md)

## Proof depends on

- [Naimark dilation of a question-indexed family](../foundations/part-02/lem-naimark-dilation.md)

## Proof

A tensor-product strategy (Definition [Tensor-product strategy](../foundations/part-01/def-tensor-strategy.md)) is a strategy of the second kind, with $S_\textsc{A} = \{1, \ldots, d_\textsc{A}\}$, $S_\textsc{B} = \{1, \ldots, d_\textsc{B}\}$, $\rho = |\psi\rangle\langle\psi|$ and projective measurements, which gives $\mathrm{val}^* \leq \mathrm{val}^*_{\mathrm{POVM}}$.

Conversely, given a strategy of the second kind, purify $\rho$ on a reference system placed on Bob's side, where Bob's effects act as $B^y_b \otimes {I}$, so that the bipartite structure survives; then dilate the two POVM *families* to projective measurements on one extra register each, and reindex the two finite sets by initial segments of $\mathbb{N}$. Neither step changes an outcome probability, so the result is a tensor-product strategy of the same value.

The dilation is the only delicate point, and the reason is that the shared state may not depend on the questions while the dilating isometry does. Writing $A^x_a = (K^x_a)^\dagger K^x_a$, the isometry $V_x : v \mapsto \sum_a (K^x_a v) \otimes |a\rangle$ satisfies $V_x^\dagger ({I} \otimes |a\rangle\langlea|) V_x = A^x_a$; extending each $V_x$ to a unitary $U_x$ of $\mathbb{C}^{S_\textsc{A}} \otimes \mathbb{C}^{{\mathcal{A}}}$ and setting $P^x_a := U_x^\dagger ({I} \otimes |a\rangle\langlea|) U_x$ gives projective measurements all of which are compressed back to the POVMs by the *same*, question-independent isometry $v \mapsto v \otimes |a_0\rangle$, so that the single state $|\psi\rangle \otimes |a_0\rangle \otimes |b_0\rangle$ works for every question. In Lean the extension is Mathlib's completion of an orthonormal family to an orthonormal basis, and only the factorization $A^x_a = (K^x_a)^\dagger K^x_a$ is used, not a matrix square root, which Mathlib does not have. The nonemptiness of ${\mathcal{A}}$ and ${\mathcal{B}}$ needed to choose $a_0$ and $b_0$ is derived, not assumed: $\mu$ is a probability distribution, so some question is asked, and a POVM on a space carrying a state has a nonempty outcome set.

## Lean

Formalized as [`MIPRE.Repetition.quantumValue_eq_entangledValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.quantumValue_eq_entangledValue).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 197](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L197)
