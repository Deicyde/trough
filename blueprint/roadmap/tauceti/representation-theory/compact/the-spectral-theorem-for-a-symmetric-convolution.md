---
declaration: theorem
origin: cited
lean: TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot
statement: formalized
proof: formalized
---

# The spectral theorem for a symmetric convolution operator

its eigenspaces span a dense
subspace of `L²(G)`, in the sense that their supremum has trivial orthogonal complement. Together
with `finiteDimensional_eigenspace_convolutionOperator` this says that `L²(G)` is exhausted, up to
the kernel of the operator, by finite-dimensional translation-invariant subspaces.

```lean
TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot.{u_1, u_2} {𝕜 : Type u_1}
  {G : Type u_2} [RCLike 𝕜] [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [MeasurableSpace G] [BorelSpace G] (k : C(G, 𝕜)) (hk : ∀ (g : G), k g⁻¹ = (starRingEnd 𝕜) (k g)) :
  (⨆ μ, Module.End.eigenspace (↑(TauCeti.convolutionOperator k)) μ)ᗮ = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/Convolution.html#TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot).

## Sources

- [Tau Ceti documentation: `TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/Convolution.html#TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot)
- [Source of `TauCeti.orthogonalComplement_iSup_eigenspaces_convolutionOperator_eq_bot` in TauCeti/RepresentationTheory/Compact/Convolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Compact/Convolution.lean#L758)
