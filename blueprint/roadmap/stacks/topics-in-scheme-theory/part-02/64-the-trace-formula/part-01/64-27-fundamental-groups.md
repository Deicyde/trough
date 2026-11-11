---
declaration: section
origin: cited
lean: AlgebraicGeometry.EtaleFundamentalGroup.IsOpenSubgroup, AlgebraicGeometry.exists_finiteEtaleEquivalence, AlgebraicGeometry.EtaleFundamentalGroup.isOpen_coe_of_isOpenSubgroup, AlgebraicGeometry.EtaleFundamentalGroup.nhds_one_hasBasis_isOpenSubgroup, AlgebraicGeometry.isProfiniteTop_etaleFundamentalGroup, AlgebraicGeometry.absoluteGaloisToFundamentalGroup, AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension, AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension_apply
statement: formalized
proof: formalized
---

# 64.27 Fundamental groups

Section 64.27 of the Stacks Project, [Tag 03VD](https://stacks.math.columbia.edu/tag/03VD). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03VE, a definition

[Tag 03VE](https://stacks.math.columbia.edu/tag/03VE) in the Stacks Project.

**`AlgebraicGeometry.EtaleFundamentalGroup.IsOpenSubgroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean#L61).

> **Stacks Project, Tag 03VE.** A subgroup of the étale fundamental group is open if it is
> the stabilizer of a point of the geometric fibre of some finite étale cover.

```lean
public abbrev IsOpenSubgroup {X : Scheme.{u}} [ConnectedSpace X]
    (x : GeometricPoint X) (H : Subgroup (EtaleFundamentalGroup X x)) : Prop
```

## Tag 03VF, a theorem

[Tag 03VF](https://stacks.math.columbia.edu/tag/03VF) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtaleEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/FundamentalGroupTheorem.lean#L85). The attribute's comment: “(3) the functor sending a finite étale Y/X to F\_x(Y) with its natural action is an equivalence onto the finite discrete continuous π₁(X, x)-sets; (1) and (2) are not covered here”.

> **Stacks Project, Tags 0BND (1) and 03VF (3).** Finite étale covers of a connected scheme `X`
> are equivalent to finite sets with a continuous action of `π₁(X, x)`, by an equivalence whose
> underlying finite sets are the geometric fibres at `x` and whose action is evaluation of natural
> automorphisms.

```lean
theorem exists_finiteEtaleEquivalence (X : Scheme.{u}) [ConnectedSpace X]
    (x : GeometricPoint X) :
    ∃ E : FiniteEtaleOver X ≌ ContAction FintypeCat.{u} (EtaleFundamentalGroup X x),
      ∃ α : E.functor ⋙
          forget₂ (ContAction FintypeCat.{u} (EtaleFundamentalGroup X x))
            FintypeCat.{u} ⋙ FintypeCat.incl ≅ finiteEtaleFiberFunctor x,
        ∀ (Y : FiniteEtaleOver X) (σ : EtaleFundamentalGroup X x)
          (y : (E.functor.obj Y).obj.V.obj),
          (α.hom.app Y) (ConcreteCategory.hom ((E.functor.obj Y).obj.ρ σ).asHom y) =
            (σ.asIso.app Y).hom ((α.hom.app Y) y)
```

**`AlgebraicGeometry.EtaleFundamentalGroup.isOpen_coe_of_isOpenSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean#L93). The attribute's comment: “(1) the open subgroups are open subsets; that they are a neighbourhood basis of the identity is `nhds_one_hasBasis_isOpenSubgroup`, and (2) and (3) are not covered here”.

> **Stacks Project, Tag 03VF (1), openness.** An open subgroup of the étale fundamental group
> is an open subset for the canonical topology.

```lean
theorem isOpen_coe_of_isOpenSubgroup {H : Subgroup (EtaleFundamentalGroup X x)}
    (hH : IsOpenSubgroup x H) : IsOpen (H : Set (EtaleFundamentalGroup X x))
```

**`AlgebraicGeometry.EtaleFundamentalGroup.nhds_one_hasBasis_isOpenSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategory/OpenSubgroups.lean#L163). The attribute's comment: “(1) the open subgroups are a neighbourhood basis of the identity; that each of them is an open subset is `isOpen_coe_of_isOpenSubgroup`, and (2) and (3) are not covered here”.

> **Stacks Project, Tag 03VF (1).** For the canonical topology on the étale fundamental group
> of a connected scheme, the open subgroups — the stabilizers of points of geometric fibres — form
> a fundamental system of neighbourhoods of the identity.

```lean
theorem nhds_one_hasBasis_isOpenSubgroup (X : Scheme.{u}) [ConnectedSpace X]
    (x : GeometricPoint X) :
    (nhds (1 : EtaleFundamentalGroup X x)).HasBasis (IsOpenSubgroup x)
      fun H ↦ (H : Set (EtaleFundamentalGroup X x))
```

**`AlgebraicGeometry.isProfiniteTop_etaleFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProfiniteFundamentalGroup.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ProfiniteFundamentalGroup.lean#L53). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 03VF, part (2).** With its canonical topology the étale fundamental
> group of a connected scheme at a geometric point is a profinite group: it is a topological group
> by `AlgebraicGeometry.etaleFundamentalGroupIsTopologicalGroup`, and its underlying space is
> compact, Hausdorff and totally disconnected.

```lean
theorem isProfiniteTop_etaleFundamentalGroup (X : Scheme.{u}) [ConnectedSpace X]
    (x : GeometricPoint X) :
    Stacks.Chapter05.Tag_0BR1.IsProfiniteTop (EtaleFundamentalGroup X x)
```

## Tag 03VG, a proposition

[Tag 03VG](https://stacks.math.columbia.edu/tag/03VG) in the Stacks Project.

**`AlgebraicGeometry.absoluteGaloisToFundamentalGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean#L475). The attribute's comment: “canonical generic-point homomorphism”.

> The residue-field Galois action on the geometric fibre functor at `sbar`.
> Its action is specified below, independently of any isomorphism of groups.

```lean
public noncomputable def absoluteGaloisToFundamentalGroup
    [ConnectedSpace X] :
    Gal(sbar.residueField / X.residueField (sbar.hom default)) →ₜ*
      AlgebraicGeometry.EtaleFundamentalGroup X sbar
```

**`AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean, line 671](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean#L671). The attribute's comment: “fundamental group”.

> The étale fundamental group is the Galois group of the maximal extension
> unramified over the scheme, with canonicality specified below.

```lean
public noncomputable def fundamentalGroupIsoGalMaximalEtaleExtension
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    AlgebraicGeometry.EtaleFundamentalGroup X sbar ≃ₜ*
      Gal(maximalEtaleExtension X sbar / X.residueField (sbar.hom default))
```

**`AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean#L698). The attribute's comment: “compatibility with restriction”.

> The canonical identification sends the generic-point homomorphism to
> restriction of absolute Galois automorphisms to the maximal étale extension.

```lean
public theorem fundamentalGroupIsoGalMaximalEtaleExtension_apply
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    letI : Normal (X.residueField (sbar.hom default))
        (maximalEtaleExtension X sbar) :=
      normal_maximalEtaleExtension X sbar hs hgeneric
    ∀ σ : Gal(sbar.residueField / X.residueField (sbar.hom default)),
      fundamentalGroupIsoGalMaximalEtaleExtension X sbar hs hgeneric
          (absoluteGaloisToFundamentalGroup X sbar σ) =
        (AlgEquiv.restrictNormalHom (maximalEtaleExtension X sbar)) σ
```

**`AlgebraicGeometry.absoluteGaloisToFundamentalGroup_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/FundamentalGroupIso.lean#L733). The attribute's comment: “canonical generic-point action”.

> A generic-field automorphism acts on a finite étale geometric fibre by
> precomposition with the induced automorphism of the geometric point.

```lean
public theorem absoluteGaloisToFundamentalGroup_apply
    [ConnectedSpace X]
    (σ : Gal(sbar.residueField/X.residueField (sbar.hom default)))
    (Y : FiniteEtaleOver X)
    (p : finiteEtaleFiber sbar Y) :
    ((((absoluteGaloisToFundamentalGroup X sbar) σ).asIso.app Y).hom p).1 =
      Spec.map (CommRingCat.ofHom σ.toAlgHom.toRingHom) ≫ p.1
```

**`AlgebraicGeometry.maximalEtaleExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean#L332). The attribute's comment: “maximal extension”.

> The compositum of all finite extensions giving finite étale normalizations.

```lean
public def maximalEtaleExtension :
    IntermediateField (X.residueField (sbar.hom default)) sbar.residueField
```

**`AlgebraicGeometry.normal_maximalEtaleExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean, line 712](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean#L712). The attribute's comment: “Galois extension”.

> The maximal finite-étale extension is normal over the function field.

```lean
public theorem normal_maximalEtaleExtension
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    Normal (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar)
```

**`AlgebraicGeometry.le_maximalEtaleExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/MaximalEtaleExtension.lean#L735). The attribute's comment: “maximality”.

> The extension is largest among extensions with finite étale normalizations of all finite
> subextensions.

```lean
public theorem le_maximalEtaleExtension
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X)
    (M : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField)
    (hM : ∀ L : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField,
      L ≤ M → FiniteDimensional (X.residueField (sbar.hom default)) L →
        FiniteEtaleNormalization X sbar L) :
    M ≤ maximalEtaleExtension X sbar
```

**`AlgebraicGeometry.finiteEtaleNormalization_of_le_maximalEtaleExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/QuotientMap.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/QuotientMap.lean#L234). The attribute's comment: “finite étale normalization”.

> Every finite subextension of the maximal extension gives a finite étale normalization.

```lean
public theorem finiteEtaleNormalization_of_le_maximalEtaleExtension
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X)
    (L : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField)
    [FiniteDimensional (X.residueField (sbar.hom default)) L]
    (hL : L ≤ maximalEtaleExtension X sbar) :
    FiniteEtaleNormalization X sbar L
```

## Tag 03VH, a theorem

[Tag 03VH](https://stacks.math.columbia.edu/tag/03VH) in the Stacks Project.

**`Stacks.EtaleCohomology.IsMixedOfWeightLE.of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusWeights.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusWeights.lean#L225). The attribute's comment: “the weight bound: the eigenvalues on H^i\_c are algebraic numbers of absolute value q ^ (w / 2) with w an integer at most i. The weight datum is the cited theorem of [WeilII]; it is carried here for the two outer terms of the excision sequence of an open-closed decomposition of X and propagated to H^i\_c(X)”.

> Mixedness of weight at most `i` propagates along an exact sequence: in the excision
> sequence `H^i_c(U) → H^i_c(X) → H^i_c(Z)` of an open-closed decomposition `X = U ⊔ Z`, if the
> Frobenius actions on the two outer terms are mixed of weight at most `i`, then so is the
> Frobenius action on `H^i_c(X)`, whose eigenvalues are therefore algebraic numbers of absolute
> value `q ^ (w / 2)` with `w` an integer at most `i`.

```lean
public theorem IsMixedOfWeightLE.of_exact {A B C : Type*} [AddCommGroup A] [Module K A]
    [AddCommGroup B] [Module K B] [AddCommGroup C] [Module K C] [FiniteDimensional K A]
    [FiniteDimensional K B] {fA : Module.End K A} {fB : Module.End K B} {fC : Module.End K C}
    {j : A →ₗ[K] B} {p : B →ₗ[K] C} (hA : IsMixedOfWeightLE q ι i fA)
    (hC : IsMixedOfWeightLE q ι i fC) (hj : ∀ a, j (fA a) = fB (j a))
    (hp : ∀ b, p (fB b) = fC (p b)) (hexact : LinearMap.ker p ≤ LinearMap.range j) :
    IsMixedOfWeightLE q ι i fB
```

**`Stacks.EtaleCohomology.isPureOfWeight_of_duality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusWeights.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusWeights.lean#L241). The attribute's comment: “the final assertion, that w = i when X is smooth and projective of dimension d: proved from mixedness in degree i and in the dual degree 2 * d - i together with the Poincare duality matching of the two spectra”.

> Poincaré duality turns mixedness into purity: if the Frobenius action `f` on `H^i_c` is
> mixed of weight at most `i`, the action `g` on the cohomology of the dual sheaf in degree
> `2 * d - i` is mixed of weight at most `2 * d - i`, and duality matches each eigenvalue `α` of
> `f` with the eigenvalue `q ^ d / α` of `g`, then `f` is pure of weight `i`.

```lean
public theorem isPureOfWeight_of_duality {d : ℤ} {g : Module.End K W}
    (hf : IsMixedOfWeightLE q ι i f) (hg : IsMixedOfWeightLE q ι (2 * d - i) g)
    (hdual : ∀ α : K, f.HasEigenvalue α → g.HasEigenvalue ((q : K) ^ d / α)) (hq : 1 < q) :
    IsPureOfWeight q ι i f
```

**`Stacks.EtaleCohomology.LAdicSheaf.weightBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilIIWeightBound.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilIIWeightBound.lean#L63). The attribute's comment: “the whole tag: the eigenvalues of pi\_X^* on H^i\_c(X\_kbar, F\_rho) are algebraic numbers of absolute value q^(w/2) with w <= i an integer, and w = i for X smooth and proper (the source says projective), for rho satisfying the conclusions of Deligne's conjecture along every embedding of Q\_ell in C”.

> **Weil II** ([Tag 03VH](https://stacks.math.columbia.edu/tag/03VH); Deligne, *La conjecture
> de Weil II*). Let `k` be a finite field with `p ^ q` elements, `k̄` an algebraic closure, `ℓ ≠ p` a
> prime, `X` connected and separated of finite type over `k` with a compactification `j`, and
> `ρ : π₁(X, x̄) → GL_r(ℚ_ℓ)` continuous, satisfying the conclusions of Deligne's conjecture
> (`Stacks.EtaleCohomology.HasDeligneConclusions`) along every embedding `ι : ℚ_ℓ → ℂ`. Then for
> every `i` the eigenvalues of `π_X^*` on `Hⁱ_c(X_k̄, ℱ_ρ ⊗ ℚ_ℓ)` (finite dimensional) are algebraic
> numbers of absolute value `(p ^ q) ^ (w / 2)` along `ι` with `w ∈ ℤ`, `w ≤ i`; and if `X` is smooth
> and proper over `k` (the source asks for projective), then `w = i`.

```lean
theorem LAdicSheaf.weightBound
    {k : Type u} [Field k] [Fintype k] (kbar : Type u) [Field kbar] [Algebra k kbar]
    [IsAlgClosure k kbar] (p q : ℕ) [Fact p.Prime] [CharP k p] (hcard : Fintype.card k = p ^ q)
    (hℓ : ℓ ≠ p) (X : B.Scheme) [IsNoetherian X.1] [ConnectedSpace X.1] (f : X.1 ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] (j : CompactificationOf (Over.mk f))
    (x : GeometricPoint X.1) {r : ℕ} (ρ : EtaleFundamentalGroup X.1 x →* GL (Fin r) ℚ_[ℓ])
    (hρ : Continuous ρ)
    (hD : ∀ ι : ℚ_[ℓ] →+* ℂ, HasDeligneConclusions (geometricFrobeniusFamily f x) p ι ρ) :
    (∀ (i : ℤ) (ι : ℚ_[ℓ] →+* ℂ),
      haveI : FiniteDimensional ℚ_[ℓ] (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X
        ℓ f j kbar (LAdicSheaf.representationSheaf B X x ρ hρ) i) :=
        LAdicSheaf.finiteDimensional_rationalGeometricCompactlySupportedCohomology B ℓ kbar p q
          hcard hℓ X f j _ i
      IsCharpolyMixedOfWeightLE (p ^ q) ι i
        (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f j kbar p q hcard
          (LAdicSheaf.representationSheaf B X x ρ hρ) i).hom) ∧
    (IsProper f → Smooth f → ∀ (i : ℤ) (ι : ℚ_[ℓ] →+* ℂ),
      haveI : FiniteDimensional ℚ_[ℓ] (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X
        ℓ f j kbar (LAdicSheaf.representationSheaf B X x ρ hρ) i) :=
        LAdicSheaf.finiteDimensional_rationalGeometricCompactlySupportedCohomology B ℓ kbar p q
          hcard hℓ X f j _ i
      IsCharpolyPureOfWeight (p ^ q) ι i
        (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f j kbar p q hcard
          (LAdicSheaf.representationSheaf B X x ρ hρ) i).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.27, Tag 03VD](https://stacks.math.columbia.edu/tag/03VD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
