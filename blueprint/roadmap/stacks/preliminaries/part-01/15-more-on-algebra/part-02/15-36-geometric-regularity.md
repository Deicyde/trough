---
declaration: section
origin: cited
lean: geometricallyRegular_tfae, flat_localization_and_regular_quotient_of_basis_kaehlerDifferential
statement: formalized
proof: formalized
---

# 15.36 Geometric regularity

Section 15.36 of the Stacks Project, [Tag 07E4](https://stacks.math.columbia.edu/tag/07E4). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07E5, a proposition

[Tag 07E5](https://stacks.math.columbia.edu/tag/07E5) in the Stacks Project.

**`geometricallyRegular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/PurelyInseparableCriterion.lean, line 886](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/PurelyInseparableCriterion.lean#L886). References: EGA 0 (22.5.8), “b) ⇔ b'), char p”.

> Let `A` be a Noetherian local algebra over a field `k` of positive characteristic `p`.
> The following are equivalent:
>
> 1. `A` is geometrically regular over `k`;
> 2. `A ⊗[k] k'` is regular for every finite intermediate field `k'` of `k¹ᵖ`;
> 3. `A` is regular and the canonical map from `H¹(L_(K/k))` to `𝔪/𝔪²` is injective;
> 4. `A` is regular and the canonical map from `Ω[k/ZMod p] ⊗[k] K` to
>    `Ω[A/ZMod p] ⊗[A] K` is injective,
>
> where `K` is the residue field of `A`.

```lean
public theorem geometricallyRegular_tfae
    (p : ℕ) [Fact p.Prime] (k : Type u) (A : Type v)
    [Field k] [CharP k p] [CommRing A] [Algebra k A]
    [IsNoetherianRing A] [IsLocalRing A] :
    letI : Algebra (ZMod p) k := ZMod.algebra k p
    letI : Algebra (ZMod p) A :=
      ((algebraMap k A).comp (algebraMap (ZMod p) k)).toAlgebra
    letI : IsScalarTower (ZMod p) k A := IsScalarTower.of_algebraMap_eq' rfl
    letI : Algebra k (PerfectClosure k p) := (PerfectClosure.of k p).toAlgebra
    List.TFAE [
      Algebra.IsGeometricallyRegular k A,
      (∀ (k' : IntermediateField k (PerfectClosure k p)),
        FiniteDimensional k k' →
        (∀ x : k', (x : PerfectClosure k p) ^ p ∈
          Set.range (algebraMap k (PerfectClosure k p))) →
        IsRegularRing (A ⊗[k] k')),
      IsRegularLocalRing A ∧
        Function.Injective
          (Algebra.H1Cotangent.map k A (IsLocalRing.ResidueField A)
            (IsLocalRing.ResidueField A)),
      IsRegularLocalRing A ∧
        Function.Injective
          ((KaehlerDifferential.mapBaseChange (ZMod p) k A).baseChange
            (IsLocalRing.ResidueField A))]
```

## Tag 07E6, a lemma

[Tag 07E6](https://stacks.math.columbia.edu/tag/07E6) in the Stacks Project.

**`flat_localization_and_regular_quotient_of_basis_kaehlerDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/PurelyInseparableCriterion.lean, line 1206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyRegular/PurelyInseparableCriterion.lean#L1206).

> Let `A` be a Noetherian local algebra over a field `k` of positive characteristic, and assume
> that `A` is geometrically regular over `k`. Let `F` be a finitely generated intermediate field of
> the residue field of `A`. If `yᵢ ∈ F` have differentials forming a basis of `Ω[F⁄k]`, and a
> map `k[X₁, …, Xₘ] → A` lifts the `yᵢ`, then `A` is flat over its localization at the inverse
> image of the maximal ideal, and the quotient of `A` by the extended prime is regular local.

```lean
public theorem flat_localization_and_regular_quotient_of_basis_kaehlerDifferential
    (p : ℕ) [Fact p.Prime] (k : Type u) (A : Type v)
    [Field k] [CharP k p] [CommRing A] [Algebra k A] [IsNoetherianRing A] [IsLocalRing A]
    [Algebra.IsGeometricallyRegular k A] (m : ℕ)
    (F : IntermediateField k (ResidueField A)) [Algebra.EssFiniteType k F]
    (y : Fin m → F) (b : Module.Basis (Fin m) F Ω[F⁄k])
    (hb : ∀ i, b i = KaehlerDifferential.D k F (y i))
    (φ : MvPolynomial (Fin m) k →ₐ[k] A)
    (hφ : ∀ i, residue A (φ (MvPolynomial.X i)) = algebraMap F (ResidueField A) (y i)) :
    letI : Algebra (MvPolynomial (Fin m) k) A := φ.toRingHom.toAlgebra
    ∀ (A₀ : Type w) [CommRing A₀] [Algebra (MvPolynomial (Fin m) k) A₀]
      [IsLocalization.AtPrime A₀ ((maximalIdeal A).comap φ)] [Algebra A₀ A]
      [IsScalarTower (MvPolynomial (Fin m) k) A₀ A],
      Module.Flat A₀ A ∧
        IsRegularLocalRing (A ⧸ Ideal.map φ ((maximalIdeal A).comap φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.36, Tag 07E4](https://stacks.math.columbia.edu/tag/07E4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
