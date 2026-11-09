---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn, TauCeti.BoundedHolomorphicFunctions.isCompactOperator_restrict, TauCeti.isCompact_closure_range_of_isLocallyBoundedOn
statement: formalized
proof: formalized
---

# Montel's theorem as an equivalence

For a family of holomorphic maps of an open set
`Ω ⊆ ℂ` into a proper complex normed space `E`, being locally bounded on `Ω` and being relatively
compact in `C(↥Ω, E)` are the same condition.

```lean
TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn.{u_1, u_2} {ι : Type u_1} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {Ω : Set ℂ} {F : ι → ℂ → E} {f : ι → C(↑Ω, E)}
  [ProperSpace E] (hΩ : IsOpen Ω) (hF : ∀ (i : ι), DifferentiableOn ℂ (F i) Ω)
  (hf : ∀ (i : ι), ⇑(f i) = Ω.domRestrict (F i)) :
  IsCompact (closure (Set.range f)) ↔ TauCeti.IsLocallyBoundedOn F Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Arzelà–Ascoli theorem in `C(X, Y)`](../../../../topology/other-results/the-arzela-ascoli-theorem-in-c-x-y.md)
- [Cauchy estimate](../part-01/cauchy-estimate.md)
- [The equicontinuity half of Montel's theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-equicontinuity-half-of-montels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Montel/Precompact.html#TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn).

## Other forms

**Montel's theorem for bounded holomorphic maps.** Formalized in Tau Ceti as [`TauCeti.BoundedHolomorphicFunctions.isCompactOperator_restrict`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.html#TauCeti.BoundedHolomorphicFunctions.isCompactOperator_restrict).

```lean
TauCeti.BoundedHolomorphicFunctions.isCompactOperator_restrict.{u_1, u_2} {V : Type u_1}
  {E : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup E] [NormedSpace ℂ E]
  {U U' : TopologicalSpace.Opens V} [ProperSpace E] {K : Set V} (hK : IsCompact K) (hU'K : ↑U' ⊆ K)
  (hKU : K ⊆ ↑U) : IsCompactOperator ⇑(TauCeti.BoundedHolomorphicFunctions.restrict ⋯)
```

**Montel's theorem, relative-compactness form.** Formalized in Tau Ceti as [`TauCeti.isCompact_closure_range_of_isLocallyBoundedOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Montel/Precompact.html#TauCeti.isCompact_closure_range_of_isLocallyBoundedOn).

```lean
TauCeti.isCompact_closure_range_of_isLocallyBoundedOn.{u_1, u_2} {ι : Type u_1} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {Ω : Set ℂ} {F : ι → ℂ → E} {f : ι → C(↑Ω, E)}
  [ProperSpace E] (hΩ : IsOpen Ω) (hF : ∀ (i : ι), DifferentiableOn ℂ (F i) Ω)
  (hb : TauCeti.IsLocallyBoundedOn F Ω) (hf : ∀ (i : ι), ⇑(f i) = Ω.domRestrict (F i)) :
  IsCompact (closure (Set.range f))
```

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Montel/Precompact.html#TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn)
- [Source of `TauCeti.isCompact_closure_range_iff_isLocallyBoundedOn` in TauCeti/Analysis/Complex/Conformal/Montel/Precompact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Montel/Precompact.lean#L84)
