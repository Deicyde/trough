---
declaration: theorem
origin: cited
lean: TauCeti.IntegralOrder.det_smul_mem_span
statement: formalized
proof: formalized
---

# Cramer's bound for subalgebras of integral elements

Let `e` be an `F`-basis of `E` lying in
an `R`-subalgebra `Γ` all of whose elements are integral over the integrally closed domain `R`, and
let `r = det (Tr_F (e i * e j))` be the Gram determinant of the regular trace form. Then `r • x`
lies in the `R`-span of `e` for every `x ∈ Γ`.

```lean
TauCeti.IntegralOrder.det_smul_mem_span.{u_1, u_2, u_3, u_4} {R : Type u_1} {F : Type u_2}
  {E : Type u_3} [CommRing R] [Field F] [Ring E] [Algebra R F] [IsFractionRing R F] [Algebra F E]
  [Algebra R E] [IsScalarTower R F E] [FiniteDimensional F E] [IsIntegrallyClosed R] {ι : Type u_4}
  [Fintype ι] [DecidableEq ι] (e : Module.Basis ι F E) {Γ : Subalgebra R E}
  (he : ∀ (i : ι), e i ∈ Γ) (hint : ∀ x ∈ Γ, IsIntegral R x) {x : E} (hx : x ∈ Γ) :
  ((LinearMap.BilinForm.toMatrix e) (Algebra.regularTraceForm F E)).det • x ∈
    Submodule.span R (Set.range ⇑e)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralOrder.det_smul_mem_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Overorder.html#TauCeti.IntegralOrder.det_smul_mem_span).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralOrder.det_smul_mem_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/IntegralOrder/Overorder.html#TauCeti.IntegralOrder.det_smul_mem_span)
- [Source of `TauCeti.IntegralOrder.det_smul_mem_span` in TauCeti/RingTheory/IntegralOrder/Overorder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/IntegralOrder/Overorder.lean#L50)
