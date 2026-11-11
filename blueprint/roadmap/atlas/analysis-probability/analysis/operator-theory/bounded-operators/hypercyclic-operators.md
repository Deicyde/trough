---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.Hypercyclicity.IsHypercyclic, MathlibExt.Analysis.FunctionalAnalysis.Hypercyclicity.isHypercyclic_of_criterion
statement: formalized
proof: formalized
---

# Hypercyclic operators

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/hypercyclic-operators/index.html).

## Hypercyclic operator

A bounded operator `T` is *hypercyclic* if some vector has a dense
orbit under iteration of `T`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Hypercyclicity.IsHypercyclic`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/Hypercyclicity.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Hypercyclicity.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/hypercyclic-operators/index.html#is-hypercyclic).

## Hypercyclicity criterion

The *hypercyclicity criterion*: along a sequence `n_k → ∞`, suppose
`T^(n_k) x → 0` on the dense set `X₀`, `S k y → 0` on the dense set `Y₀`,
and `T^(n_k) (S k y) → y` on `Y₀`. Then `T` is hypercyclic.
The Baire proof combines all three eventual estimates and uses cofinality
to meet each rational ball after every prescribed time threshold.
This includes the full-iterate, exact-inverse special case by taking
`n_k = id` and converting the exact identities to constant convergence.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Hypercyclicity.isHypercyclic_of_criterion`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Hypercyclicity.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Hypercyclicity.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/hypercyclic-operators/index.html#is-hypercyclic-of-criterion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypercyclic operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/hypercyclic-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/bounded-operators/hypercyclic-operators)
