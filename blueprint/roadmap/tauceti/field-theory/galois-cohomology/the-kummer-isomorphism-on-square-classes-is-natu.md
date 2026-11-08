---
declaration: theorem
origin: cited
lean: RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv, TauCeti.nsmul_smul_fixingSubgroupKummerEquivOfTrivial
statement: formalized
proof: formalized
---

# The Kummer isomorphism on square classes is natural in field isomorphisms

transport of
`H¹(-, 𝔽₂)` along `G_L ≃ G_K` corresponds to pushforward of square classes along `e`.

```lean
RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv.{u, v} {K : Type u} {L : Type v} [Field K]
  [Field L] [Invertible 2] [Invertible 2] (e : K ≃+* L) (x : TauCeti.SquareClassGroup K) :
  (TauCeti.trivialF2Map1Equiv e.absoluteGaloisGroupCongr) ((TauCeti.kummerSquareClassEquiv K) x) =
    (TauCeti.kummerSquareClassEquiv L) ((↑e).squareClassMap x)
```

## Depends on

- [The Kummer isomorphism](../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)

## Lean

Formalized in Tau Ceti as [`RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/MuTwo/FieldCongr.html#RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv).

## Other forms

**The Kummer isomorphism with trivial coefficients is equivariant up to the cyclotomic twist.** Formalized in Tau Ceti as [`TauCeti.nsmul_smul_fixingSubgroupKummerEquivOfTrivial`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.html#TauCeti.nsmul_smul_fixingSubgroupKummerEquivOfTrivial).

```lean
TauCeti.nsmul_smul_fixingSubgroupKummerEquivOfTrivial.{u_1, u_2, u_3} {K : Type u_1} [Field K]
  {n : ℕ} {L : Type u_2} [Field L] [Algebra K L] (σ : L →ₐ[K] SeparableClosure K) {M : Type u_3}
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M]
  [DistribMulAction (TauCeti.AbsoluteGaloisGroup K) M]
  [ContinuousSMul (TauCeti.AbsoluteGaloisGroup K) M] [σ.fieldRange.fixingSubgroup.Normal]
  (hn : IsUnit ↑n) (e : TauCeti.KummerCoeff K n ≃+ M)
  (htriv : ∀ (g : TauCeti.AbsoluteGaloisGroup K) (m : M), g • m = m)
  (hN : ∀ h ∈ σ.fieldRange.fixingSubgroup, ∀ (ξ : TauCeti.KummerCoeff K n), h • ξ = ξ)
  (g : TauCeti.AbsoluteGaloisGroup K) (τ : L →ₐ[K] L) (hτ : ∀ (x : L), σ (τ x) = g (σ x)) (k : ℕ)
  (hk : ∀ (ξ : TauCeti.KummerCoeff K n), g • ξ = k • ξ)
  (x : Additive (TauCeti.powerClassQuotient Lˣ n)) :
  k • g • (TauCeti.fixingSubgroupKummerEquivOfTrivial σ hn e htriv hN) x =
    (TauCeti.fixingSubgroupKummerEquivOfTrivial σ hn e htriv hN)
      ((MonoidHom.toAdditive (TauCeti.powerClassMap n (Units.map ↑τ))) x)
```

## Sources

- [Tau Ceti documentation: `RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/MuTwo/FieldCongr.html#RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv)
- [Source of `RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv` in TauCeti/FieldTheory/GaloisCohomology/MuTwo/FieldCongr.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/MuTwo/FieldCongr.lean#L142)
