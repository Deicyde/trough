---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.twirlX_wZ, MIPRE.Introspection.twirlZ_wX
statement: formalized
proof: formalized
---

# Exact Pauli twirling

Over a finite field of characteristic two, for a subspace $K\leq\mathbb{F}^k$, twirl by the uniform distribution on $\tau^W(K)$, where $W\in\{X,Z\}$ and $W'$ is the other basis. The twirl fixes $\tau^{W'}(u)$ if $u\in K^\perp$ and is zero otherwise. Here the annihilator uses the field-valued dot product. The source proves the general-characteristic statement; this formalization supplies its characteristic-two specialization used by the pipeline.

## Depends on

- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)

## Proof

Conjugation by the opposite Pauli family multiplies an operator by the sign of the trace pairing. Average these signs on $K$. The character is trivial exactly on $K^\perp$, by Lemma [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md); all other character sums vanish.

## Lean

Formalized as [`MIPRE.Introspection.twirlX_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.twirlX_wZ), [`MIPRE.Introspection.twirlZ_wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.twirlZ_wX).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1327](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1327)
