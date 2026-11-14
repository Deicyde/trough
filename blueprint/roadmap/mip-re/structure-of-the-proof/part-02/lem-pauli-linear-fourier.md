---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.subspaceTrace_eq_zero_iff, MIPRE.Introspection.sum_subspace_sign, MIPRE.Introspection.linear_measurement_fourier, MIPRE.Introspection.linear_measurement_fourier_inverse
statement: formalized
proof: formalized
---

# Pauli operators against a linear-map measurement

Let $\mathbb{F}$ be a finite field of characteristic two, with $\omega=-1$. Let $L : \mathbb{F}^k \to \mathbb{F}^k$ be linear, let $W \in \{X, Z\}$, and for $a$ in the range of $L$ pick $u_a$ with $L(u_a) = a$. Write $\sigma^W_{[L(\cdot) = a]}$ for the projector onto the event that a $W$-basis measurement returns a preimage of $a$. Then for every $v \in \ker(L)^\perp$,

$$
\sigma^W(v) = \sum_{a \in \mathbb{F}^k} \omega^{\operatorname{tr}(u_a \cdot v)}\, \sigma^W_{[L(\cdot) = a]},
$$

and conversely, for every $a$ in the range of $L$,

$$
\sigma^W_{[L(\cdot) = a]} = \mathop{\mathbb{E}}_{v \sim \ker(L)^\perp}\ \omega^{-\operatorname{tr}(v \cdot u_a)}\,
\sigma^W(v).
$$

The choice of $u_a$ off the range of $L$ is immaterial, since there the projector vanishes.

## Depends on

- [Orthogonal and canonical complements](../part-01/def-cl-canonical.md)
- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)

## Proof depends on

- [The two complements](../part-01/lem-cl-canonical.md)

## Proof

Each identity is the Fourier expansion of the other over the group $\ker(L)^\perp$: the character $v \mapsto \omega^{\operatorname{tr}(u_a \cdot v)}$ depends only on $a = L(u_a)$, because two preimages of $a$ differ by an element of $\ker(L)$, which the trace pairing annihilates against $\ker(L)^\perp$.

## Lean

Formalized as [`MIPRE.Introspection.subspaceTrace_eq_zero_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.subspaceTrace_eq_zero_iff), [`MIPRE.Introspection.sum_subspace_sign`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_subspace_sign), [`MIPRE.Introspection.linear_measurement_fourier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_fourier), [`MIPRE.Introspection.linear_measurement_fourier_inverse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_fourier_inverse).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1208](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1208)
