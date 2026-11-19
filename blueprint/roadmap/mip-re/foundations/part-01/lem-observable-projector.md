---
declaration: lemma
origin: cited
lean: MIPRE.LCS.observableToProjector, MIPRE.LCS.isMeasurementSystem_observableToProjector, MIPRE.LCS.commute_observableToProjector
statement: formalized
proof: formalized
---

# Observables and projective measurements correspond

For an observable $O$ the family $a \mapsto \tfrac12(1 + (-1)^a O)$ is a projective measurement indexed by $\mathbb{F}_2$, and the correspondence preserves commutation: if $O_1$ and $O_2$ commute then so do all of their projectors.

## Depends on

- [Binary observables](def-observable.md)

## Proof

Self-adjointness, idempotence, orthogonality and summation to $1$ are each a two-line computation from $O^* = O$ and $O^2 = 1$; commutation is inherited term by term.

## Lean

Formalized as [`MIPRE.LCS.observableToProjector`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.observableToProjector), [`MIPRE.LCS.isMeasurementSystem_observableToProjector`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.isMeasurementSystem_observableToProjector), [`MIPRE.LCS.commute_observableToProjector`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.commute_observableToProjector).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 389](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L389)
