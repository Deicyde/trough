---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuousLinearEquiv_prod_of_countableType
statement: formalized
proof: formalized
---

# Strict short exact sequences out of a space of countable type split

over a complete
nontrivially normed field, let `E` be an ultrametric Banach space of countable type, let
`i : M →L[K] E` be an embedding and `q : E →L[K] N` a surjection onto a Banach space with
`range i = ker q`. Then there is a continuous linear equivalence `d : E ≃L[K] M × N` with
`d (i m) = (m, 0)` and `(d x).2 = q x`.

```lean
TauCeti.exists_continuousLinearEquiv_prod_of_countableType.{u_1, u_2, u_3, u_4} {K : Type u_1}
  {E : Type u_2} {N : Type u_3} [NontriviallyNormedField K] [CompleteSpace K] [NormedAddCommGroup E]
  [NormedSpace K E] [IsUltrametricDist E] [CompleteSpace E] [NormedAddCommGroup N] [NormedSpace K N]
  [CompleteSpace N] {M : Type u_4} [AddCommGroup M] [_root_.Module K M] [TopologicalSpace M]
  {v : ℕ → E} (hv : Dense ↑(Submodule.span K (Set.range v))) (i : M →L[K] E) (q : E →L[K] N)
  (hi : Topology.IsEmbedding ⇑i) (hq : Function.Surjective ⇑q) (hiq : (↑i).range = (↑q).ker) :
  ∃ d, (∀ (m : M), d (i m) = (m, 0)) ∧ ∀ (x : E), (d x).2 = q x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Quantitative Open Mapping Theorem](../../../analysis/part-03/normed/part-02/quantitative-open-mapping-theorem.md)
- [Riesz's lemma, translated form](../../../analysis/part-03/normed/part-02/rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuousLinearEquiv_prod_of_countableType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Splitting.html#TauCeti.exists_continuousLinearEquiv_prod_of_countableType).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuousLinearEquiv_prod_of_countableType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Splitting.html#TauCeti.exists_continuousLinearEquiv_prod_of_countableType)
- [Source of `TauCeti.exists_continuousLinearEquiv_prod_of_countableType` in TauCeti/Analysis/Normed/Module/Bases/Splitting.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/Bases/Splitting.lean#L82)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
