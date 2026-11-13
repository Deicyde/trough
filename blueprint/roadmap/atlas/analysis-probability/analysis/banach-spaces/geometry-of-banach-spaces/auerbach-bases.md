---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.coordCLM, MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.norm_coordCLM_le_one, MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.norm_coordCLM_eq_one, MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.IsAuerbachBasis, MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.exists_auerbach_basis
statement: formalized
proof: formalized
---

# Auerbach bases

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html).

## Coordinate functional of a basis as a continuous linear map

The `i`-th coordinate functional of a basis, as a continuous linear map.
In finite dimensions every linear map is continuous, so this is just the
coordinate functional bundled with its continuity.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.coordCLM`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html#coord-clm).

## Operator norm of a norm-bounded coordinate functional is at most 1

If the `i`-th coordinate functional is bounded by the norm, its operator
norm is at most `1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.norm_coordCLM_le_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html#norm-coord-clm-le-one).

## Coordinate functional of a unit basis vector has operator norm 1

If the `i`-th basis vector has norm `1` and the `i`-th coordinate
functional is bounded by the norm, its operator norm is exactly `1`: it
attains `1` at the `i`-th basis vector.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.norm_coordCLM_eq_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html#norm-coord-clm-eq-one).

## Auerbach basis

An *Auerbach basis* is a basis of unit vectors whose coordinate
functionals all have operator norm `1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.IsAuerbachBasis`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html#is-auerbach-basis).

## Auerbach's theorem

Every finite-dimensional normed space over `𝕜`
has an Auerbach basis, indexed by `Fin (Module.finrank 𝕜 E)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.AuerbachBasis.exists_auerbach_basis`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/AuerbachBasis.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html#exists-auerbach-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Auerbach bases](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/auerbach-bases)
