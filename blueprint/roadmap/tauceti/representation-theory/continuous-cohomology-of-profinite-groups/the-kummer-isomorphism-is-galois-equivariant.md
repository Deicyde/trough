---
declaration: theorem
origin: cited
lean: TauCeti.smul_fixingSubgroupKummerEquiv, TauCeti.explicitMap1_kummerIso, RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv, TauCeti.nsmul_smul_fixingSubgroupKummerEquivOfTrivial
statement: formalized
proof: formalized
---

# The Kummer isomorphism is Galois equivariant

Let the subgroup `N` of `G_K` fixing `σ(L)`
be normal, so that `G_K` acts on `H¹(N, μₙ)` by conjugation. If `g ∈ G_K` and the
`K`-endomorphism `τ` of `L` satisfy `σ ∘ τ = g ∘ σ`, then conjugation by `g` corresponds under the
Kummer isomorphism to the map of power classes `Lˣ ⧸ (Lˣ)ⁿ → Lˣ ⧸ (Lˣ)ⁿ` induced by `τ`.

```lean
TauCeti.smul_fixingSubgroupKummerEquiv.{u_1, u_2} {K : Type u_1} [Field K] {n : ℕ} {L : Type u_2}
  [Field L] [Algebra K L] (σ : L →ₐ[K] SeparableClosure K) [σ.fieldRange.fixingSubgroup.Normal]
  (hn : IsUnit ↑n) (g : TauCeti.AbsoluteGaloisGroup K) (τ : L →ₐ[K] L)
  (hτ : ∀ (x : L), σ (τ x) = g (σ x)) (x : Additive (TauCeti.powerClassQuotient Lˣ n)) :
  g • (TauCeti.fixingSubgroupKummerEquiv σ hn) x =
    (TauCeti.fixingSubgroupKummerEquiv σ hn)
      ((MonoidHom.toAdditive (TauCeti.powerClassMap n (Units.map ↑τ))) x)
```

## Depends on

- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.smul_fixingSubgroupKummerEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.html#TauCeti.smul_fixingSubgroupKummerEquiv).

## Other forms

**The Kummer isomorphism is natural for pullback along an arbitrary field extension.** Formalized in Tau Ceti as [`TauCeti.explicitMap1_kummerIso`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/Kummer.html#TauCeti.explicitMap1_kummerIso).

```lean
TauCeti.explicitMap1_kummerIso.{u_2, u_3} {K : Type u_2} [Field K] {L : Type u_3} [Field L]
  [Algebra K L] (n : ℕ) (τ : SeparableClosure K →ₐ[K] SeparableClosure L) (hn : IsUnit ↑n)
  (x : TauCeti.powerClassQuotient Kˣ n) :
  (TauCeti.ContCohomology.explicitMap1 (TauCeti.AbsoluteGaloisGroup K) (TauCeti.KummerCoeff K n)
        (TauCeti.AbsoluteGaloisGroup L) (TauCeti.KummerCoeff L n) (TauCeti.absoluteGaloisGroupMap τ)
        (TauCeti.kummerCoeffBaseChange n τ) ⋯ ⋯)
      (Multiplicative.toAdd ((TauCeti.kummerIso K n hn) x)) =
    Multiplicative.toAdd
      ((TauCeti.kummerIso L n ⋯) ((TauCeti.powerClassMap n (Units.map ↑(algebraMap K L))) x))
```

**The Kummer isomorphism on square classes is natural in field isomorphisms.** Formalized in Tau Ceti as [`RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/MuTwo/FieldCongr.html#RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv).

```lean
RingEquiv.trivialF2Map1Equiv_kummerSquareClassEquiv.{u, v} {K : Type u} {L : Type v} [Field K]
  [Field L] [Invertible 2] [Invertible 2] (e : K ≃+* L) (x : TauCeti.SquareClassGroup K) :
  (TauCeti.trivialF2Map1Equiv e.absoluteGaloisGroupCongr) ((TauCeti.kummerSquareClassEquiv K) x) =
    (TauCeti.kummerSquareClassEquiv L) ((↑e).squareClassMap x)
```

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

- [Tau Ceti documentation: `TauCeti.smul_fixingSubgroupKummerEquiv`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.html#TauCeti.smul_fixingSubgroupKummerEquiv)
- [Source of `TauCeti.smul_fixingSubgroupKummerEquiv` in TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisCohomology/EquivariantKummer.lean#L249)
