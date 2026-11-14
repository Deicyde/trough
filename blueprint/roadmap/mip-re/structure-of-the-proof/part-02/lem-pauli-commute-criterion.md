---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.linear_measurements_commute
statement: formalized
proof: formalized
---

# A commutation criterion for $X$ and $Z$ measurements

Over a finite field of characteristic two, let $L, R : \mathbb{F}^k \to \mathbb{F}^k$ be linear with $\ker(R)^\perp \subseteq \ker(L)$. Then the measurements $\{\sigma^Z_{[L(\cdot) = b]}\}_b$ and $\{\sigma^X_{[R(\cdot) = d]}\}_d$ commute.

## Depends on

- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)

## Proof

Expand both families by Lemma [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md). The $Z$-side expansion runs over $v \in \ker(L)^\perp$ and the $X$-side over $w \in \ker(R)^\perp$, and $\sigma^Z(v)$ and $\sigma^X(w)$ commute exactly when $\operatorname{tr}(v \cdot w) = 0$. The hypothesis gives $w \in \ker(L)$ for every such $w$, and $v \in \ker(L)^\perp$, so the pairing vanishes term by term.

## Lean

Formalized as [`MIPRE.Introspection.linear_measurements_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurements_commute).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1244](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1244)
