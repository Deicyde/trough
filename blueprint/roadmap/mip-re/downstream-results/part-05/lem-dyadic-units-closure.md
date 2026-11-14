---
declaration: lemma
origin: cited
lean: MIPRE.IsMatUnits.mul_cancel, MIPRE.IsMatUnits.map, MIPRE.IsMatUnits.op, MIPRE.IsMatUnits.diagonal, MIPRE.IsMatUnits.prod, MIPRE.HasDyadicUnits.map, MIPRE.HasDyadicUnits.op, MIPRE.HasDyadicUnits.matrix, MIPRE.HasDyadicUnits.prod
statement: formalized
proof: formalized
---

# Transport of dyadic matrix units

Unital matrix units, and hence unital dyadic matrix units (Definition [Unital dyadic matrix units](def-dyadic-units.md)), pass along unital $*$-homomorphisms; to the opposite ring, as $e_{ij} \mapsto e_{ji}^{\mathrm{op}}$; to the ring of $\alpha \times \alpha$ matrices over the ring, as the scalar diagonals $e_{ij}\, {I}_\alpha$; and to the product of two rings, componentwise, for two systems with the same index.

## Depends on

- [Unital dyadic matrix units](def-dyadic-units.md)

## Proof

Each clause is a direct computation. A unital $*$-homomorphism preserves products, adjoints, finite sums and the unit. In the opposite ring $e_{ji}^{\mathrm{op}} e_{ml}^{\mathrm{op}} = (e_{ml} e_{ji})^{\mathrm{op}} = \delta_{jl}\, e_{mi}^{\mathrm{op}}$. Diagonal matrices multiply entrywise, and the adjoint of a diagonal matrix is the diagonal of the adjoints. Products are computed componentwise, which is why the two systems must share an index: indexing dyadic units by $\{0, 1\}^n$ is what makes the product clause need no reindexing. The full proof is `reports/c6b-paper-proofs.md`, Section 3, Lemma 5.

## Lean

Formalized as [`MIPRE.IsMatUnits.mul_cancel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits.mul_cancel), [`MIPRE.IsMatUnits.map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits.map), [`MIPRE.IsMatUnits.op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits.op), [`MIPRE.IsMatUnits.diagonal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits.diagonal), [`MIPRE.IsMatUnits.prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsMatUnits.prod), [`MIPRE.HasDyadicUnits.map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HasDyadicUnits.map), [`MIPRE.HasDyadicUnits.op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HasDyadicUnits.op), [`MIPRE.HasDyadicUnits.matrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HasDyadicUnits.matrix), [`MIPRE.HasDyadicUnits.prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.HasDyadicUnits.prod).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2864](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2864)
