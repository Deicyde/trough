---
declaration: lemma
origin: cited
lean: MIPRE.PauliSites, MIPRE.PauliSites.proj, MIPRE.PauliSites.xpow, MIPRE.PauliSites.unit, MIPRE.PauliSites.isMatUnits_unit, MIPRE.PauliSites.commute_unit, MIPRE.PauliSites.units, MIPRE.PauliSites.units_mul, MIPRE.PauliSites.star_units, MIPRE.PauliSites.sum_units_diag, MIPRE.PauliSites.isMatUnits_units, MIPRE.PauliSites.hasDyadicUnits
statement: formalized
proof: formalized
---

# Pauli sites give dyadic matrix units

Let $R$ be a $*$-algebra over $\mathbb{C}$ with self-adjoint elements $x_k, z_k$ for $k \in \mathbb{N}$, such that $x_k^2 = z_k^2 = 1$ and $z_k x_k = -x_k z_k$, and elements at distinct sites commute. Put $p_k = \frac12 (1 + z_k)$ and $u^{(k)}_{ab} = x_k^a\, p_k\, x_k^b$ for $a, b \in \{0, 1\}$. Then each $u^{(k)}$ is a system of unital $2 \times 2$ matrix units, and the products $e_{ij} = \prod_{k < n} u^{(k)}_{i_k j_k}$, for $i, j \in \{0, 1\}^n$, are unital $2^n \times 2^n$ matrix units. So $R$ has unital dyadic matrix units (Definition [Unital dyadic matrix units](def-dyadic-units.md)).

## Depends on

- [Unital dyadic matrix units](def-dyadic-units.md)

## Proof

$p_k$ is a projection, $x_k p_k x_k = 1 - p_k$ by anticommutation, and so $p_k x_k p_k = x_k (1 - p_k) p_k = 0$. Hence $u^{(k)}_{ab} u^{(k)}_{cd} = x_k^a\, p_k x_k^{b + c} p_k\, x_k^d$ is $u^{(k)}_{ad}$ if $b = c$ and $0$ otherwise, $(u^{(k)}_{ab})^* = u^{(k)}_{ba}$, and $u^{(k)}_{00} + u^{(k)}_{11} = p_k + (1 - p_k) = 1$. Units at distinct sites commute, so the relations of the product system follow site by site, by induction on $n$. The construction is that of `reports/c6b-paper-proofs.md`, Section 3.8.

## Lean

Formalized as [`MIPRE.PauliSites`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites), [`MIPRE.PauliSites.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.proj), [`MIPRE.PauliSites.xpow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.xpow), [`MIPRE.PauliSites.unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.unit), [`MIPRE.PauliSites.isMatUnits_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.isMatUnits_unit), [`MIPRE.PauliSites.commute_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.commute_unit), [`MIPRE.PauliSites.units`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.units), [`MIPRE.PauliSites.units_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.units_mul), [`MIPRE.PauliSites.star_units`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.star_units), [`MIPRE.PauliSites.sum_units_diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.sum_units_diag), [`MIPRE.PauliSites.isMatUnits_units`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.isMatUnits_units), [`MIPRE.PauliSites.hasDyadicUnits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.PauliSites.hasDyadicUnits).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2888](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2888)
