---
declaration: section
origin: cited
lean: Algebra.isGeometricallyIrreducible_adjoin_linearCombination, Algebra.exists_algebraicIndependent_linearCombinations, Algebra.algebraicIndependent_linearCombination_of_codimTwo, Stacks.Bertini.FamilyDivisors.Hypotheses.exists_ringKrullDim_quotient_add_two_eq_reducedChart, Algebra.isGeometricallyIrreducible_universalDivisorChart_of_linearSubst, Algebra.algebraicIndependent_universalDivisorChartMap_X_of_linearSubst, Stacks.Bertini.FamilyDivisors.Hypotheses.exists_mem_minimalPrimes_height_eq_two, Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_isUnit_and_height_eq_two
statement: formalized
proof: formalized
---

# 37.32 Bertini theorems

Section 37.32 of the Stacks Project, [Tag 0G4C](https://stacks.math.columbia.edu/tag/0G4C). 4 tags here are carried by 43 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G4D, a lemma

[Tag 0G4D](https://stacks.math.columbia.edu/tag/0G4D) in the Stacks Project.

**`Algebra.isGeometricallyIrreducible_adjoin_linearCombination`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Bertini.lean, line 821](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Bertini.lean#L821).

> Let `K/k` be a finitely generated geometrically irreducible extension and let `Ω` be generated
> over `K` by algebraically independent elements `x₁, …, xₙ`. If `x₁, …, xₙ`, `∑ gᵢxᵢ` and
> `∑ cᵢgᵢ` are algebraically independent over `k`, then `Ω` is geometrically irreducible over the
> subfield generated over `k` by the `xᵢ` and `∑ gᵢxᵢ`.

```lean
theorem isGeometricallyIrreducible_adjoin_linearCombination
    (k K Ω : Type u) [Field k] [Field K] [Field Ω]
    [Algebra k K] [Algebra K Ω] [Algebra k Ω] [IsScalarTower k K Ω]
    (n : ℕ) (_hn : 0 < n) (x : Fin n → Ω) (g : Fin n → K)
    (hgen : IntermediateField.adjoin K (Set.range x) = ⊤)
    (hx : AlgebraicIndependent K x)
    (hK : Algebra.IsGeometricallyIrreducible k K)
    (hfg : (⊤ : IntermediateField k K).FG)
    (c : Fin n → k)
    (hind : AlgebraicIndependent k
      (Sum.elim x (Bool.rec
        (∑ i, algebraMap K Ω (g i) * x i)
        (∑ i, algebraMap K Ω ((algebraMap k K (c i)) * g i))))) :
    let ξ : Ω := ∑ i, algebraMap K Ω (g i) * x i
    let F : IntermediateField k Ω :=
      IntermediateField.adjoin k (Set.range x ∪ {ξ})
    letI : Algebra F Ω := F.toSubalgebra.toAlgebra
    Algebra.IsGeometricallyIrreducible F Ω
```

## Tag 0G4E, a lemma

[Tag 0G4E](https://stacks.math.columbia.edu/tag/0G4E) in the Stacks Project.

**`Algebra.exists_algebraicIndependent_linearCombinations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniAlgebraicIndependence.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniAlgebraicIndependence.lean#L333).

> Let `A` be a domain of finite type over a field `k`, let
> `n ≥ 2` and let `g : Fin n → A`. If the common zero locus of `g 0` and `g 1` has an irreducible
> component of dimension `dim A - 2`, then there are `c : Fin n → k` for which the variables
> `x₁, …, xₙ`, the linear combination `∑ gᵢxᵢ` and the constant `∑ cᵢgᵢ` are algebraically
> independent over `k`.

```lean
public theorem exists_algebraicIndependent_linearCombinations
    (k : Type u) (A : Type v) [Field k] [CommRing A] [IsDomain A] [Algebra k A]
    [Algebra.FiniteType k A] {n : ℕ} (hn : 2 ≤ n) (g : Fin n → A)
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {g ⟨0, by omega⟩, g ⟨1, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    ∃ c : Fin n → k,
      AlgebraicIndependent k
        (Sum.elim (MvPolynomial.X : Fin n → MvPolynomial (Fin n) A)
          (fun j : Fin 2 =>
            if j = 0 then
              ∑ i : Fin n, MvPolynomial.C (g i) * MvPolynomial.X i
            else
              MvPolynomial.C (∑ i : Fin n, algebraMap k A (c i) * g i)))
```

**`Algebra.algebraicIndependent_linearCombination_of_codimTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniLinearCombinationCodimTwo.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniLinearCombinationCodimTwo.lean#L90). The attribute's comment: “the variables and their linear combination, read in the ambient field”.

> **The variables and their linear combination are algebraically independent over the base
> field.** Let `A` be a domain of finite type over `k`, `n ≥ 2` and `g : Fin n → A` such that
> `V(g₁, g₂)` has an irreducible component of codimension two in `Spec A`. Then the `n + 1` elements
> `x₁, …, xₙ` and `ξ = ∑ gᵢxᵢ` of `Ω` are algebraically independent over `k`.

```lean
theorem algebraicIndependent_linearCombination_of_codimTwo
    [IsDomain A] [Algebra.FiniteType k A] [IsFractionRing A K]
    {n : ℕ} (hn : 2 ≤ n) (x : Fin n → Ω) (hx : AlgebraicIndependent K x) (g : Fin n → A)
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {g ⟨0, by omega⟩, g ⟨1, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    AlgebraicIndependent k
      (Sum.elim x fun _ : Unit => ∑ i, algebraMap K Ω (algebraMap A K (g i)) * x i)
```

## Tag 0G4F, a lemma

[Tag 0G4F](https://stacks.math.columbia.edu/tag/0G4F) in the Stacks Project.

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_ringKrullDim_quotient_add_two_eq_reducedChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartAlgebra.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartAlgebra.lean#L126). The attribute's comment: “hypothesis (3) as the codimension datum of the chart statements”.

> On a trivializing affine chart meeting `Z`, the reduced chart ring `A` is a domain of finite
> type over `k`, and some minimal prime `p` over the ideal generated by the images of the functions
> of `v₂` and `v₃` satisfies `dim (A ⧸ p) + 2 = dim A`.

```lean
theorem exists_ringKrullDim_quotient_add_two_eq_reducedChart (c : D.Chart)
    (hZ : ((c.U : Set D.X) ∩ (h.Z : Set D.X)).Nonempty) :
    letI := reducedChartAlgebra c.U
    ∃ p : Ideal (reducedChartRing c.U),
      p ∈ (Ideal.span {Ideal.Quotient.mk _ (chartFunction c.triv h.v₂),
        Ideal.Quotient.mk _ (chartFunction c.triv h.v₃)}).minimalPrimes ∧
        ringKrullDim (reducedChartRing c.U ⧸ p) + 2 = ringKrullDim (reducedChartRing c.U)
```

**`Algebra.isGeometricallyIrreducible_universalDivisorChart_of_linearSubst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartChangeOfBasis.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartChangeOfBasis.lean#L326). The attribute's comment: “the generic fibre over a chart, for distinguished vectors of an arbitrary basis”.

> The function field of the universal divisor over a chart is geometrically irreducible over
> the field generated by the parameters. This is
> `Algebra.isGeometricallyIrreducible_universalDivisorChart` with the parameters indexed by an
> arbitrary finite set `σ` and its hypotheses imposed not on `f` itself but on the image `g` of `f`
> under an invertible `k`-linear transformation `b` of the parameters.

```lean
theorem isGeometricallyIrreducible_universalDivisorChart_of_linearSubst (hn : 2 ≤ n)
    (g : Fin (n + 1) → A) (hg : ∀ i, g i = ∑ j, algebraMap k A (b i j) * f j)
    {w : A} (hw : w * g 0 = 1)
    (hcompat : ∀ a : A, algebraMap K Ω (algebraMap A K a) =
      universalDivisorChartMap A Ω f (C a))
    (hK : Algebra.IsGeometricallyIrreducible k K)
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {g ⟨1, by omega⟩, g ⟨2, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    letI F : IntermediateField k Ω :=
      IntermediateField.adjoin k
        (Set.range fun j : σ => universalDivisorChartMap A Ω f (X j))
    letI : Algebra F Ω := F.toSubalgebra.toAlgebra
    Algebra.IsGeometricallyIrreducible F Ω
```

**`Algebra.algebraicIndependent_universalDivisorChartMap_X_of_linearSubst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartChangeOfBasis.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartChangeOfBasis.lean#L360). The attribute's comment: “the dominance over the parameter space, for an arbitrary basis”.

> The parameters of a chart are algebraically independent over the base field. This is
> `Algebra.algebraicIndependent_universalDivisorChartMap_X` with the parameters indexed by an
> arbitrary finite set and its hypotheses imposed on the image of `f` under an invertible
> `k`-linear transformation of the parameters.

```lean
theorem algebraicIndependent_universalDivisorChartMap_X_of_linearSubst (hn : 2 ≤ n)
    (g : Fin (n + 1) → A) (hg : ∀ i, g i = ∑ j, algebraMap k A (b i j) * f j)
    {w : A} (hw : w * g 0 = 1)
    (hcompat : ∀ a : A, algebraMap K Ω (algebraMap A K a) =
      universalDivisorChartMap A Ω f (C a))
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {g ⟨1, by omega⟩, g ⟨2, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    AlgebraicIndependent k fun j : σ => universalDivisorChartMap A Ω f (X j)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_mem_minimalPrimes_height_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean#L64). The attribute's comment: “hypothesis (3) read on a chart meeting Z, as an exact height”.

> On a trivializing affine chart `U` that meets `Z`, the prime of `Γ(U, ⊤)` cutting out `Z ∩ U`
> is a minimal prime over the ideal generated by the functions `g₂, g₃` of `v₂, v₃`, and its height
> is exactly two.

```lean
theorem exists_mem_minimalPrimes_height_eq_two (c : D.Chart)
    (hZ : ((c.U : Set D.X) ∩ (h.Z : Set D.X)).Nonempty) :
    ∃ p : Ideal Γ(c.U.toScheme, ⊤),
      p ∈ (Ideal.span {chartFunction c.triv h.v₂, chartFunction c.triv h.v₃}).minimalPrimes ∧
        p.height = 2
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_isUnit_and_height_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean#L81). The attribute's comment: “hypothesis (3) on a single chart: an invertible first function and an exact height”.

> There is a trivializing affine chart on which the function of `v₁` is a unit and on which
> some minimal prime over the ideal generated by the functions of `v₂` and `v₃` has height exactly
> two.

```lean
theorem exists_chart_isUnit_and_height_eq_two :
    ∃ c : D.Chart, IsUnit (chartFunction c.triv h.v₁) ∧
      ∃ p : Ideal Γ(c.U.toScheme, ⊤),
        p ∈ (Ideal.span {chartFunction c.triv h.v₂, chartFunction c.triv h.v₃}).minimalPrimes ∧
          p.height = 2
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.v₁_notMem_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean#L111). The attribute's comment: “v₁ is independent from v₂ and v₃”.

> The vector `v₁` is not in the span of `v₂` and `v₃`.

```lean
theorem v₁_notMem_span : h.v₁ ∉ Submodule.span D.k {h.v₂, h.v₃}
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.linearIndependent_v₂_v₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean#L129). The attribute's comment: “v₂ and v₃ are independent”.

> The vectors `v₂` and `v₃` are linearly independent.

```lean
theorem linearIndependent_v₂_v₃ : LinearIndependent D.k ![h.v₂, h.v₃]
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.linearIndependent_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartCodimension.lean#L151). The attribute's comment: “the three distinguished vectors are linearly independent”.

> The three distinguished vectors `v₁, v₂, v₃` of hypothesis (3) are linearly independent.

```lean
theorem linearIndependent_distinguished : LinearIndependent D.k ![h.v₁, h.v₂, h.v₃]
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_chartRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean#L75). The attribute's comment: “hypothesis (2) read on a trivializing affine chart”.

> The chart ring `Γ(U, ⊤)` of a trivializing affine chart is geometrically irreducible
> over `k`.

```lean
theorem isGeometricallyIrreducible_chartRing (c : D.Chart) :
    letI := chartAlgebra c.U
    Algebra.IsGeometricallyIrreducible D.k Γ(c.U.toScheme, ⊤)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_reducedChartRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean#L95). The attribute's comment: “hypothesis (2) read on the reduced ring of a trivializing affine chart”.

> The reduced chart ring `Γ(U, ⊤) ⧸ √0` of a trivializing affine chart is geometrically
> irreducible over `k`.

```lean
theorem isGeometricallyIrreducible_reducedChartRing (c : D.Chart) :
    letI := reducedChartAlgebra c.U
    Algebra.IsGeometricallyIrreducible D.k (reducedChartRing c.U)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_reducedChartFractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFractionField.lean#L107). The attribute's comment: “hypothesis (2) as geometric irreducibility of the chart's fraction field”.

> The fraction field of the reduced chart ring of a trivializing affine chart is geometrically
> irreducible over `k`.

```lean
theorem isGeometricallyIrreducible_reducedChartFractionRing (c : D.Chart) :
    letI := reducedChartAlgebra c.U
    Algebra.IsGeometricallyIrreducible D.k (reducedChartFractionRing c.U)
```

**`Algebra.isGeometricallyIrreducible_universalDivisorChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFunctionField.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFunctionField.lean#L432). The attribute's comment: “the generic fibre over a trivializing affine chart, in field-theoretic form”.

> **The function field of the universal divisor over a trivializing chart is geometrically
> irreducible over the field generated by the parameters.**
>
> Let `A` be a domain of finite type over a field `k` with fraction field `K` geometrically
> irreducible over `k`, let `n ≥ 2` and let `f₀, …, fₙ ∈ A` with `f₀` invertible. If the common
> zero locus of `f₁` and `f₂` has an irreducible component of codimension two in `Spec A`, then a
> fraction field `Ω` of the chart ring `A[x₀, …, xₙ]/(x₀f₀ + ⋯ + xₙfₙ)` of the universal divisor
> is geometrically irreducible over the subfield generated over `k` by the images of the
> coordinates `x₀, …, xₙ`. The hypothesis `hcompat` says that the two maps `A → K → Ω` and
> `A → A[x₀, …, xₙ] → Ω` agree.

```lean
theorem isGeometricallyIrreducible_universalDivisorChart
    (k A K Ω : Type u) [Field k] [CommRing A] [IsDomain A] [Algebra k A]
    [Algebra.FiniteType k A] [Field K] [Algebra A K] [IsFractionRing A K] [Algebra k K]
    [IsScalarTower k A K] [Field Ω] [Algebra K Ω] [Algebra k Ω] [IsScalarTower k K Ω]
    {n : ℕ} (hn : 2 ≤ n) (f : Fin (n + 1) → A) {u : A} (hu : u * f 0 = 1)
    [Algebra (MvPolynomial (Fin (n + 1)) A ⧸ Ideal.span {universalLinearForm f}) Ω]
    [IsFractionRing (MvPolynomial (Fin (n + 1)) A ⧸ Ideal.span {universalLinearForm f}) Ω]
    (hcompat : ∀ a : A, algebraMap K Ω (algebraMap A K a) =
      universalDivisorChartMap A Ω f (C a))
    (hK : Algebra.IsGeometricallyIrreducible k K)
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {f ⟨1, by omega⟩, f ⟨2, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    letI F : IntermediateField k Ω :=
      IntermediateField.adjoin k
        (Set.range fun j : Fin (n + 1) => universalDivisorChartMap A Ω f (X j))
    letI : Algebra F Ω := F.toSubalgebra.toAlgebra
    Algebra.IsGeometricallyIrreducible F Ω
```

**`Algebra.algebraicIndependent_universalDivisorChartMap_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFunctionField.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartFunctionField.lean#L463). The attribute's comment: “the dominance over the parameter space, read on a trivializing affine chart”.

> **The parameters of the chart are algebraically independent over the base field.** In the
> situation of `Algebra.isGeometricallyIrreducible_universalDivisorChart` the `n + 1` images of the
> coordinates `x₀, …, xₙ` in a fraction field `Ω` of the chart ring
> `A[x₀, …, xₙ]/(x₀f₀ + ⋯ + xₙfₙ)` are algebraically independent over `k`; equivalently, the
> polynomial ring `k[x₀, …, xₙ]` injects into `Ω`.

```lean
theorem algebraicIndependent_universalDivisorChartMap_X
    (k A K Ω : Type u) [Field k] [CommRing A] [IsDomain A] [Algebra k A]
    [Algebra.FiniteType k A] [Field K] [Algebra A K] [IsFractionRing A K] [Algebra k K]
    [IsScalarTower k A K] [Field Ω] [Algebra K Ω] [Algebra k Ω] [IsScalarTower k K Ω]
    {n : ℕ} (hn : 2 ≤ n) (f : Fin (n + 1) → A) {u : A} (hu : u * f 0 = 1)
    [Algebra (MvPolynomial (Fin (n + 1)) A ⧸ Ideal.span {universalLinearForm f}) Ω]
    [IsFractionRing (MvPolynomial (Fin (n + 1)) A ⧸ Ideal.span {universalLinearForm f}) Ω]
    (hcompat : ∀ a : A, algebraMap K Ω (algebraMap A K a) =
      universalDivisorChartMap A Ω f (C a))
    (hcodim : ∃ p : Ideal A,
      p ∈ (Ideal.span {f ⟨1, by omega⟩, f ⟨2, by omega⟩}).minimalPrimes ∧
        ringKrullDim (A ⧸ p) + 2 = ringKrullDim A) :
    AlgebraicIndependent k fun j : Fin (n + 1) => universalDivisorChartMap A Ω f (X j)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_reducedChartDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean#L88). The attribute's comment: “the generic fibre over a chart, from the tag's own hypotheses”.

> Let `Ω` be a fraction field of the chart ring of the universal divisor over the reduced chart
> ring of a trivializing affine chart, compatibly with the fraction field `K` of the chart's own
> domain. If an invertible `k`-linear substitution of the parameters carries the chart equations to
> a tuple `g` whose zeroth entry is a unit and whose first two entries carry the codimension datum,
> then `Ω` is geometrically irreducible over the subfield generated over `k` by the images of the
> parameters.

```lean
theorem isGeometricallyIrreducible_reducedChartDivisor (c : D.Chart) {m : ℕ}
    (b : Matrix (Fin (m + 3)) D.basisIndex D.k) (b' : Matrix D.basisIndex (Fin (m + 3)) D.k)
    (hbb' : b * b' = 1) (hb'b : b' * b = 1) (Ω : Type u) [Field Ω] [Algebra D.k Ω] :
    letI := reducedChartAlgebra c.U
    ∀ [Algebra (reducedChartFractionRing c.U) Ω]
      [IsScalarTower D.k (reducedChartFractionRing c.U) Ω]
      [Algebra (reducedChartDivisorRing c) Ω] [IsFractionRing (reducedChartDivisorRing c) Ω]
      (g : Fin (m + 3) → reducedChartRing c.U) (w : reducedChartRing c.U),
      (∀ i, g i = ∑ j : D.basisIndex,
          algebraMap D.k (reducedChartRing c.U) (b i j) * reducedChartEquation c j) →
      w * g ⟨0, by omega⟩ = 1 →
      (∃ q : Ideal (reducedChartRing c.U),
        q ∈ (Ideal.span {g ⟨1, by omega⟩, g ⟨2, by omega⟩}).minimalPrimes ∧
          ringKrullDim (reducedChartRing c.U ⧸ q) + 2 = ringKrullDim (reducedChartRing c.U)) →
      (∀ a : reducedChartRing c.U,
        algebraMap (reducedChartFractionRing c.U) Ω
            (algebraMap (reducedChartRing c.U) (reducedChartFractionRing c.U) a) =
          Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
            (MvPolynomial.C a)) →
      letI F : IntermediateField D.k Ω :=
        IntermediateField.adjoin D.k
          (Set.range fun j : D.basisIndex =>
            Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
              (MvPolynomial.X j))
      letI : Algebra F Ω := F.toSubalgebra.toAlgebra
      Algebra.IsGeometricallyIrreducible F Ω
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.algebraicIndependent_reducedChartDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean#L128). The attribute's comment: “the dominance over the parameter space, from the tag's own hypotheses”.

> In the situation of
> `Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_reducedChartDivisor` the
> images of the parameters of the family in `Ω` are algebraically independent over `k`.

```lean
theorem algebraicIndependent_reducedChartDivisor (c : D.Chart) {m : ℕ}
    (b : Matrix (Fin (m + 3)) D.basisIndex D.k) (b' : Matrix D.basisIndex (Fin (m + 3)) D.k)
    (hbb' : b * b' = 1) (hb'b : b' * b = 1) (Ω : Type u) [Field Ω] [Algebra D.k Ω] :
    letI := reducedChartAlgebra c.U
    ∀ [Algebra (reducedChartFractionRing c.U) Ω]
      [IsScalarTower D.k (reducedChartFractionRing c.U) Ω]
      [Algebra (reducedChartDivisorRing c) Ω] [IsFractionRing (reducedChartDivisorRing c) Ω]
      (g : Fin (m + 3) → reducedChartRing c.U) (w : reducedChartRing c.U),
      (∀ i, g i = ∑ j : D.basisIndex,
          algebraMap D.k (reducedChartRing c.U) (b i j) * reducedChartEquation c j) →
      w * g ⟨0, by omega⟩ = 1 →
      (∃ q : Ideal (reducedChartRing c.U),
        q ∈ (Ideal.span {g ⟨1, by omega⟩, g ⟨2, by omega⟩}).minimalPrimes ∧
          ringKrullDim (reducedChartRing c.U ⧸ q) + 2 = ringKrullDim (reducedChartRing c.U)) →
      (∀ a : reducedChartRing c.U,
        algebraMap (reducedChartFractionRing c.U) Ω
            (algebraMap (reducedChartRing c.U) (reducedChartFractionRing c.U) a) =
          Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
            (MvPolynomial.C a)) →
      AlgebraicIndependent D.k fun j : D.basisIndex =>
        Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
          (MvPolynomial.X j)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_generic_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartGenericFibre.lean#L182). The attribute's comment: “the generic fibre and the dominance on a chart, from the tag's own hypotheses”.

> There is a trivializing affine chart whose chart ring of the universal divisor is a domain
> and on which, for every fraction field `Ω` of that ring compatible with the chart's own fraction
> field, the function field of the universal divisor is geometrically irreducible over the subfield
> generated by the parameters and the parameters are algebraically independent over `k`.

```lean
theorem exists_chart_generic_fibre :
    ∃ c : D.Chart,
      IsDomain (reducedChartDivisorRing c) ∧
      letI := reducedChartAlgebra c.U
      ∀ (Ω : Type u) [Field Ω] [Algebra D.k Ω] [Algebra (reducedChartFractionRing c.U) Ω]
        [IsScalarTower D.k (reducedChartFractionRing c.U) Ω]
        [Algebra (reducedChartDivisorRing c) Ω] [IsFractionRing (reducedChartDivisorRing c) Ω],
      (∀ a : reducedChartRing c.U,
        algebraMap (reducedChartFractionRing c.U) Ω
            (algebraMap (reducedChartRing c.U) (reducedChartFractionRing c.U) a) =
          Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
            (MvPolynomial.C a)) →
      (AlgebraicIndependent D.k fun j : D.basisIndex =>
        Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
          (MvPolynomial.X j)) ∧
      letI F : IntermediateField D.k Ω :=
        IntermediateField.adjoin D.k
          (Set.range fun j : D.basisIndex =>
            Algebra.universalDivisorChartMap (reducedChartRing c.U) Ω (reducedChartEquation c)
              (MvPolynomial.X j))
      letI : Algebra F Ω := F.toSubalgebra.toAlgebra
      Algebra.IsGeometricallyIrreducible F Ω
```

**`Stacks.Bertini.FamilyDivisors.exists_surjective_ker_le_nilradical_reducedChartDivisorRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartReduction.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartReduction.lean#L141). The attribute's comment: “the reduced chart ring of the universal divisor as the reduction of its chart ring”.

> **The reduced chart ring of the universal divisor is the reduction of its chart ring**: there
> is a surjection from the chart ring onto the reduced chart ring with kernel inside the
> nilradical.

```lean
theorem exists_surjective_ker_le_nilradical_reducedChartDivisorRing (c : D.Chart) :
    ∃ Φ : chartDivisorRing c →+* reducedChartDivisorRing c,
      Function.Surjective Φ ∧ RingHom.ker Φ ≤ nilradical (chartDivisorRing c)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_substitution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartSubstitution.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartSubstitution.lean#L115). The attribute's comment: “hypothesis (3) as the substitution datum of the chart statements”.

> There is a trivializing affine chart, an invertible pair of `k`-matrices between the parameter
> index set of the family and `{0, …, m + 2}`, and a tuple `g` of elements of the reduced chart ring
> which is the image of the chart equations under that substitution, whose zeroth entry is invertible
> and whose first and second entries carry the codimension datum.

```lean
theorem exists_chart_substitution :
    ∃ (c : D.Chart) (m : ℕ) (b : Matrix (Fin (m + 3)) D.basisIndex D.k)
      (b' : Matrix D.basisIndex (Fin (m + 3)) D.k),
      b * b' = 1 ∧ b' * b = 1 ∧
      letI := reducedChartAlgebra c.U
      ∃ (g : Fin (m + 3) → reducedChartRing c.U) (w : reducedChartRing c.U),
        (∀ i, g i = ∑ j : D.basisIndex,
            algebraMap D.k (reducedChartRing c.U) (b i j) * reducedChartEquation c j) ∧
          w * g ⟨0, by omega⟩ = 1 ∧
          ∃ q : Ideal (reducedChartRing c.U),
            q ∈ (Ideal.span {g ⟨1, by omega⟩, g ⟨2, by omega⟩}).minimalPrimes ∧
              ringKrullDim (reducedChartRing c.U ⧸ q) + 2 =
                ringKrullDim (reducedChartRing c.U)
```

**`Stacks.Bertini.FamilyDivisors.isIrreducible_supportSet_universalDivisor_of_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartSupport.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniChartSupport.lean#L314). The attribute's comment: “the passage from the trivializing charts to the universal divisor”.

> **The universal divisor is irreducible, for a cover closed under refining intersections.**
> Same as `Stacks.Bertini.FamilyDivisors.isIrreducible_supportSet_universalDivisor`, but with the
> two topological hypotheses replaced by the requirement that the intersection of any two members
> of the cover contain a member: the parts of `H_univ` over the charts are then automatically
> nonempty, because each is irreducible, and the part over a member inside `Uᵢ ∩ Uⱼ` witnesses
> that the parts over `Uᵢ` and over `Uⱼ` meet.
>
> This is the shape in which the union argument of [Stacks, Tag 0G4F] is run: the cover is the
> family of all affine opens of `X` trivializing `L` on which the hypotheses hold, which is closed
> under passing to a smaller affine open.

```lean
theorem isIrreducible_supportSet_universalDivisor_of_directed {ι : Sort*} [Nonempty ι]
    (W : ι → D.X.Opens) (hW : ⨆ i, W i = ⊤) (hdir : ∀ i j, ∃ k, W k ≤ W i ⊓ W j)
    [∀ i, IsAffine (W i).toScheme] [∀ i, IsNoetherianRing Γ((W i).toScheme, ⊤)]
    (hnil : ∀ i, (nilradical Γ((W i).toScheme, ⊤)).IsPrime)
    (eW : ∀ i, D.restrictedModule (W i) ≅ SheafOfModules.unit (W i).toScheme.ringCatSheaf)
    (hf : ∀ i, ∃ j, ¬ IsNilpotent (D.chartEquation (eW i) j))
    (hcodim : ∀ i, ∀ p ∈ (Ideal.span (Set.range (D.chartEquation (eW i)))).minimalPrimes,
      2 ≤ p.height) :
    IsIrreducible D.universalDivisor.supportSet
```

**`Stacks.Bertini.FamilyDivisors.commonZeroSet`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniCommonZeroSet.lean#L102). The attribute's comment: “the common zero locus of the linear system”.

> **The common zero locus `Z = ⋂_{v ∈ V} H_v`** of the linear system. This is the closed set
> on which hypothesis (4) of [Stacks, Tag 0G4F] imposes a codimension bound.

```lean
def commonZeroSet : Set D.X
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_basis_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniDistinguishedBasis.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniDistinguishedBasis.lean#L52). The attribute's comment: “the three distinguished vectors as the first members of a basis”.

> The linear system has a basis indexed by `Fin (m + 3)`, for some `m`, whose members at
> `0, 1, 2` are the three distinguished vectors `v₁, v₂, v₃` of hypothesis (3).

```lean
theorem exists_basis_distinguished :
    ∃ (m : ℕ) (W : Module.Basis (Fin (m + 3)) D.k D.V),
      W ⟨0, by omega⟩ = h.v₁ ∧ W ⟨1, by omega⟩ = h.v₂ ∧ W ⟨2, by omega⟩ = h.v₃
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean#L131). The attribute's comment: “the hypotheses”.

> **The hypotheses of the Bertini irreducibility theorem** on the standing situation of the
> Bertini theorems: `X` of finite type and geometrically irreducible over `k`, an irreducible
> component `Z` of `H_{v₂} ∩ H_{v₃}` of codimension exactly two not contained in `H_{v₁}`, and a
> codimension-two condition on the common zero locus of the linear system.

```lean
structure Hypotheses (D : FamilyDivisors.{u, v})
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.two_le_height_chartEquation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean#L183). The attribute's comment: “hypothesis (4) read on a trivializing affine chart”.

> **Hypothesis (4), read on a chart.** Every minimal prime over the ideal `(f₁, …, f_r)`
> generated by the functions representing the sections `ψ(vᵢ)` on a trivializing affine chart has
> height at least two.

```lean
theorem two_le_height_chartEquation (c : D.Chart)
    {q : Ideal Γ(c.U.toScheme, ⊤)}
    (hq : q ∈ (Ideal.span (Set.range (D.chartEquation c.triv))).minimalPrimes) :
    2 ≤ q.height
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_not_isNilpotent_chartEquation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean#L193). The attribute's comment: “hypothesis (3) read on a trivializing affine chart”.

> **Hypothesis (3), read on a chart.** On every trivializing affine chart some basis vector is
> represented by a function that is not nilpotent.

```lean
theorem exists_not_isNilpotent_chartEquation (c : D.Chart) :
    ∃ j, ¬ IsNilpotent (D.chartEquation c.triv j)
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isIrreducible_supportSet_universalDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean#L221). The attribute's comment: “the irreducibility of the universal divisor, from the tag's own hypotheses”.

> **`H_univ` is irreducible under the hypotheses of the Bertini irreducibility theorem.**

```lean
theorem isIrreducible_supportSet_universalDivisor :
    IsIrreducible D.universalDivisor.supportSet
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.irreducibleSpace_universalDivisorScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniHypotheses.lean#L233). The attribute's comment: “the universal divisor as an irreducible scheme, from the tag's own hypotheses”.

> **`H_univ` is an irreducible scheme under the hypotheses of the Bertini irreducibility
> theorem.**

```lean
theorem irreducibleSpace_universalDivisorScheme :
    IrreducibleSpace D.universalDivisor.subscheme
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_isUnit_chartFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniInvertibleChart.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniInvertibleChart.lean#L81). The attribute's comment: “hypothesis (3) as an invertible section on a chart meeting Z”.

> There is a trivializing affine chart meeting `Z` on which the function of `v₁` is
> invertible.

```lean
theorem exists_chart_isUnit_chartFunction :
    ∃ c : D.Chart, ((c.U : Set D.X) ∩ (h.Z : Set D.X)).Nonempty ∧
      IsUnit (chartFunction c.triv h.v₁)
```

**`Stacks.Bertini.FamilyDivisors.isFractionRing_parameterBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniParameterFunctionField.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniParameterFunctionField.lean#L105). The attribute's comment: “the residue field at the generic point of the parameter space”.

> The function field `κ(η)` of the parameter space `𝔸^r_k` is a fraction field of the
> polynomial ring in the parameters.

```lean
theorem isFractionRing_parameterBase :
    letI := D.parameterBaseFunctionFieldAlgebra
    IsFractionRing (MvPolynomial D.basisIndex D.k) D.parameterBase.functionField
```

**`Stacks.Bertini.FamilyDivisors.adjoin_range_coord_parameterBase_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniParameterFunctionField.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniParameterFunctionField.lean#L123). The attribute's comment: “the generic point of the parameter space generates the residue field”.

> The residue field `κ(η)` at the generic point of `𝔸^r_k` is generated over `k` as a field by
> the images of the coordinates.

```lean
theorem adjoin_range_coord_parameterBase_eq_top :
    letI := D.parameterBaseFunctionFieldAlgebra
    letI := D.parameterBaseFunctionFieldBaseAlgebra
    IntermediateField.adjoin D.k
      (Set.range fun i : D.basisIndex =>
        algebraMap (MvPolynomial D.basisIndex D.k) D.parameterBase.functionField
          (MvPolynomial.X i)) = ⊤
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.exists_chart_isFractionRing_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorFunctionField.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorFunctionField.lean#L116). The attribute's comment: “the residue field of the universal divisor at its generic point”.

> Under the hypotheses of the family, `H_univ` is irreducible and there is a chart `c`, whose
> part of `H_univ` contains the generic point, such that the residue field of `H_univ` at its
> generic point is a fraction field of the chart ring of the universal divisor over `c`, with
> structure map sending the reduction of a section `a` over the chart to the value of `a` at the
> generic point.

```lean
theorem exists_chart_isFractionRing_residueField :
    haveI := h.irreducibleSpace_universalDivisorScheme
    ∃ (c : D.Chart) (hξ : genericPoint D.universalDivisorScheme ∈ D.chartDivisorOpen c.U),
      ∃ _ : Algebra (reducedChartDivisorRing c)
          (D.universalDivisorScheme.residueField (genericPoint D.universalDivisorScheme)),
        IsFractionRing (reducedChartDivisorRing c)
            (D.universalDivisorScheme.residueField
              (genericPoint D.universalDivisorScheme)) ∧
          ∀ a : Γ(D.universalDivisorScheme, D.chartDivisorOpen c.U),
            algebraMap (reducedChartDivisorRing c)
                (D.universalDivisorScheme.residueField (genericPoint D.universalDivisorScheme))
                (reducedChartDivisorReduction c (D.chartSubschemeΓEquiv c.U c.triv a)) =
              D.universalDivisorScheme.evaluation (D.chartDivisorOpen c.U)
                (genericPoint D.universalDivisorScheme) hξ a
```

**`Stacks.Bertini.FamilyDivisors.isFractionRing_parameterSpecResidueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean#L120). The attribute's comment: “the residue field at the generic point of the parameter space, on `Spec Γ`”.

> The residue field of `Spec Γ(𝔸^r_k, ⊤)` at its generic point is a fraction field of the
> polynomial ring in the parameters: `κ(η) = k(xⱼ)`.

```lean
theorem isFractionRing_parameterSpecResidueField :
    letI := D.parameterSpecResidueFieldAlgebra
    IsFractionRing (MvPolynomial D.basisIndex D.k) D.parameterSpecResidueField
```

**`Stacks.Bertini.FamilyDivisors.adjoin_range_parameterSpecResidueField_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean#L140). The attribute's comment: “the coordinates generate the residue field at the generic point of `𝔸^r_k`”.

> `κ(η)` is generated over `k` by the images of the coordinates.

```lean
theorem adjoin_range_parameterSpecResidueField_eq_top :
    letI := D.parameterSpecResidueFieldAlgebra
    letI := D.parameterSpecResidueFieldBaseAlgebra
    IntermediateField.adjoin D.k
      (Set.range fun j : D.basisIndex =>
        algebraMap (MvPolynomial D.basisIndex D.k) D.parameterSpecResidueField
          (MvPolynomial.X j)) = ⊤
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isGeometricallyIrreducible_residueField_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean#L231). The attribute's comment: “the generic fibre, read on the residue field of the universal divisor”.

> The residue field of `H_univ` at its generic point is geometrically irreducible over `κ(η)`.

```lean
theorem isGeometricallyIrreducible_residueField_genericPoint :
    haveI := h.irreducibleSpace_universalDivisorScheme
    letI := residueFieldAlgebraOfEq (D.universalFamily ≫ D.parameterBase.isoSpec.hom)
      (comp_isoSpec_genericPoint_eq D.universalFamily h.base_genericPoint_universalFamily)
    Algebra.IsGeometricallyIrreducible D.parameterSpecResidueField
      (D.universalDivisorScheme.residueField (genericPoint D.universalDivisorScheme))
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.geometricallyIrreducible_fiber_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean#L315). The attribute's comment: “the generic fibre of the universal family”. References: SGA 7 XVIII (6.1.6.1), “Case s = 1 of 6.1.6.1”.

> The generic fibre of the universal family is geometrically irreducible.

```lean
theorem geometricallyIrreducible_fiber_genericPoint :
    haveI := h.irreducibleSpace_universalDivisorScheme
    GeometricallyIrreducible
      (D.universalFamily.fiberToSpecResidueField (genericPoint D.parameterBase))
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.forGeneral_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorGenericFibre.lean#L335). References: SGA 7 XVIII (6.1.6.1), “special case”.

> Let `X` be a scheme of finite type over a field `k`, geometrically irreducible over `k`, let
> `L` be an invertible module on `X` and let `V ⊂ Γ(X, L)` be a finite dimensional linear system.
> Assume there are `v₁, v₂, v₃ ∈ V` and an irreducible component `Z` of `H_{v₂} ∩ H_{v₃}` with
> `Z ⊄ H_{v₁}` and `codim(Z, X) = 2`, and assume every irreducible closed subset of the common zero
> locus of `V` has codimension at least two in `X`. Then for general `v ∈ V ⊗_k k'` the divisor `H_v`
> is geometrically irreducible over `k'`: there is one nonempty open `U ⊂ 𝔸^r_k`, defined over `k`,
> such that `H_v` is geometrically irreducible over `k'` for every field extension `k'/k` and every
> `k'`-point of `U`.

```lean
theorem forGeneral_geometricallyIrreducible :
    D.ForGeneral (fun K _ _ w =>
      ∀ a : Fin (Module.finrank D.k D.V) → K,
        w = ∑ i, TensorProduct.tmul D.k (D.basis i) (a i) →
          GeometricallyIrreducible
            ((D.specializedDivisor K a).subschemeι ≫ D.baseChangeToSpec K))
```

**`Algebra.isIrreducible_zeroLocus_universalLinearForm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorIrreducible.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorIrreducible.lean#L747). The attribute's comment: “irreducibility of the universal divisor over an affine chart”.

> **The universal divisor over an affine chart is irreducible.** Let `A` be a Noetherian domain
> and `f₁, …, f_r ∈ A` with `f₁ ≠ 0`. If every irreducible component of `V(f₁, …, f_r)` has
> codimension at least two in `Spec A`, then the zero locus of `x₁f₁ + ⋯ + x_rf_r` in
> `Spec A[x₁, …, x_r]` is irreducible.
>
> This is the irreducibility of `H_U` in the proof of [Stacks, Tag 0G4F]; see the module docstring
> for what the source deduces from it and what is not formalized here.

```lean
theorem isIrreducible_zeroLocus_universalLinearForm (hf : f 0 ≠ 0)
    (hcodim : ∀ p ∈ (Ideal.span (Set.range f)).minimalPrimes, 2 ≤ p.height) :
    IsIrreducible (PrimeSpectrum.zeroLocus {universalLinearForm f} :
      Set (PrimeSpectrum (MvPolynomial (Fin (n + 1)) A)))
```

**`Algebra.isIrreducible_zeroLocus_linearForm_of_isPrime_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorIrreducible.lean, line 855](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalDivisorIrreducible.lean#L855). The attribute's comment: “the reduction step and the irreducibility of the universal divisor over a chart”.

> **The universal divisor over an affine chart is irreducible, without a reducedness
> hypothesis.** Let `A` be a Noetherian ring whose nilradical is prime — equivalently, with `Spec A`
> irreducible — let `σ` be a finite index set and let `f : σ → A` be a family with `f i₀` not
> nilpotent for some index `i₀`. If every irreducible component of the common zero locus `V(f)` has
> codimension at least two in `Spec A`, then the zero locus of `∑ᵢ fᵢxᵢ` in `Spec A[xᵢ : i ∈ σ]` is
> irreducible.
>
> This is the reduction step at the beginning of the proof of [Stacks, Tag 0G4F], carried out on a
> chart: the source replaces `X` by its reduction, which changes neither the topology of `X` nor
> that of the universal divisor. Here `A` is replaced by `A / √0`, which is a Noetherian domain,
> and `Algebra.isIrreducible_zeroLocus_linearForm` is applied there; the comparison map
> `Spec (A/√0)[xᵢ] → Spec A[xᵢ]` is surjective because its kernel consists of nilpotents, so the
> two zero loci are homeomorphic, and heights and minimal primes are unchanged by
> `Ideal.le_height_of_mem_minimalPrimes_map_quotientMk`.

```lean
theorem isIrreducible_zeroLocus_linearForm_of_isPrime_nilradical
    (hnil : (nilradical A).IsPrime) {σ : Type v} [Fintype σ] (f : σ → A) {i₀ : σ}
    (hf : ¬ IsNilpotent (f i₀))
    (hcodim : ∀ p ∈ (Ideal.span (Set.range f)).minimalPrimes, 2 ≤ p.height) :
    IsIrreducible (PrimeSpectrum.zeroLocus {∑ i, C (f i) * X i} :
      Set (PrimeSpectrum (MvPolynomial σ A)))
```

**`Stacks.Bertini.FamilyDivisors.Hypotheses.isDominant_universalFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalFamilyDominance.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniUniversalFamilyDominance.lean#L153). The attribute's comment: “the dominance of the universal family over the parameter space”.

> Under the hypotheses of the family, the universal family `H_univ → 𝔸^r_k` is dominant.

```lean
theorem isDominant_universalFamily : IsDominant D.universalFamily
```

## Tag 0G4G, a remark

[Tag 0G4G](https://stacks.math.columbia.edu/tag/0G4G) in the Stacks Project.

**`Stacks.Bertini.FamilyDivisors.exists_smooth_irreducibleSpace_specializedDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmoothIrreducibleMember.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmoothIrreducibleMember.lean#L425). The attribute's comment: “for an arbitrary finite dimensional linear system with phi_(L, psi) a closed immersion: the hyperplane section is H_v over k itself”.

> **[Stacks, Tag 0G4G] for an arbitrary linear system.** Let `k` be an algebraically closed
> field and let `X ⊂ 𝐏^n_k` be smooth and irreducible of dimension `≥ 2`. Then there is a
> hyperplane `H ⊂ 𝐏^n_k` such that `X ∩ H` is smooth and irreducible. The tag as the source states
> it, for a closed subscheme of `ℙⁿ_k`, is
> `Stacks.Bertini.ProjectiveSubscheme.exists_hyperplane_smooth_irreducibleSpace`.
>
> The remark works in the standing situation of [Stacks, Tag 0G47] with
> `V = k T_0 ⊕ … ⊕ k T_n`, `L = 𝒪_X(1)` and `ψ` the restriction of the coordinates to `X`; the
> hyperplane attached to `v ∈ V` is `H_v` and `X ∩ H_v` is the divisor `Z(ψ(v))`, which over `k`
> itself is `Stacks.Bertini.FamilyDivisors.specializedDivisor` at the coordinate tuple of `v`.
> The inclusion `X ⊂ 𝐏^n_k` is read as the remark reads it when it invokes
> [Stacks, Tag 0FD6]: `ψ` generates `L` (hypothesis (2) there) and the morphism
> `φ_{L,ψ} : X → 𝐏(V)` it determines is an immersion (hypothesis (3) there, at every basis,
> equivalently at one by `Stacks.Bertini.FamilyDivisors.isImmersive_congr_basis'`), together with
> properness of `X` over `k`, which says that the immersion is a closed one. This is a
> generalization: `V` may be any finite dimensional linear system, `ψ` need not be injective.
> Nothing else about the embedding is assumed: ampleness of `L`, which Enriques–Severi–Zariski
> needs, is derived by `Stacks.Bertini.FamilyDivisors.isAmple_of_isImmersive`. "Of dimension
> `≥ 2`" is `2 ≤ dim X`, the Krull dimension of the underlying space.
>
> The conclusion asserts in addition `ψ(v) ≠ 0`, that is `X ⊄ H_v`: the hyperplane is honest and
> `X ∩ H_v` is a genuine hyperplane section, not the whole of `X`.
>
> The proof is the remark's: smoothness of the general member is [Stacks, Tag 0FD6],
> connectedness is Enriques–Severi–Zariski in the form [Stacks, Tag 0FD9], and a connected scheme
> smooth over a field is irreducible.

```lean
theorem exists_smooth_irreducibleSpace_specializedDivisor [IsAlgClosed D.k] [Smooth D.toBase]
    [IsProper D.toBase] [IrreducibleSpace D.X] (hgen : D.Generates)
    (himm : ∀ (m : ℕ) (b : Module.Basis (Fin (m + 1)) D.k D.V),
      D.IsImmersive b (D.generatesBy_basis hgen b))
    (hdim : (2 : WithBot ℕ∞) ≤ topologicalKrullDim D.X) :
    ∃ c : Fin (Module.finrank D.k D.V) → D.k,
      D.sectionOf (∑ i, c i • D.basis i) ≠ 0 ∧
        Smooth ((D.specializedDivisor D.k c).subschemeι ≫ D.baseChangeToSpec D.k) ∧
          IrreducibleSpace (D.specializedDivisor D.k c).subscheme
```

**`Stacks.Bertini.ProjectiveSubscheme.exists_hyperplane_smooth_irreducibleSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmoothIrreducibleMember.lean, line 617](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/BertiniSmoothIrreducibleMember.lean#L617).

> **[Stacks, Tag 0G4G].** Let `k` be an algebraically closed field and let `X ⊂ 𝐏^n_k` be
> smooth and irreducible of dimension `≥ 2`. Then there is a hyperplane `H ⊂ 𝐏^n_k` such that
> `X ∩ H` is smooth and irreducible.
>
> `X ⊂ 𝐏^n_k` is a closed immersion `i : X → ℙⁿ_k`, and `X` is smooth over `k` through it. A
> hyperplane is `H = Z(∑ⱼ cⱼ Tⱼ)` for a nonzero `c ∈ kⁿ⁺¹`, the zero scheme of a nonzero linear
> form in the homogeneous coordinates `T_0, …, T_n` of `𝒪(1)`
> (`Stacks.AlgebraicGeometry.ProjectiveSpaceSectionMultiplication.hyperplane`), and `X ∩ H` is its
> scheme-theoretic inverse image `H.comap i`. "Of dimension `≥ 2`" is `2 ≤ dim X`.
>
> The proof is the remark's: smoothness of the general hyperplane section is [Stacks, Tag 0FD6],
> connectedness is Enriques–Severi–Zariski in the form [Stacks, Tag 0FD9], and a connected scheme
> smooth over a field is irreducible
> (`Stacks.Bertini.FamilyDivisors.exists_smooth_irreducibleSpace_divisor`, applied to the standing
> situation `Stacks.Bertini.ProjectiveSubscheme.family` of the remark).

```lean
theorem exists_hyperplane_smooth_irreducibleSpace [IsAlgClosed k] [IsClosedImmersion i]
    [Smooth (i ≫ pullback.fst (terminal.from (Spec (.of k)))
      (terminal.from (projectiveSpaceAtUniverse.{u} n)))]
    [IrreducibleSpace X] (hdim : (2 : WithBot ℕ∞) ≤ topologicalKrullDim X) :
    ∃ c : Fin (n + 1) → k, c ≠ 0 ∧
      let H := Stacks.AlgebraicGeometry.ProjectiveSpaceSectionMultiplication.hyperplane n
        (Spec (.of k))
        (Stacks.Divisors.sectionsOfTop (projectiveSpaceTwistingSheaf n (Spec (.of k)))
          (∑ j, (pullback.fst (terminal.from (Spec (.of k)))
              (terminal.from (projectiveSpaceAtUniverse.{u} n))).appTop
                ((Scheme.ΓSpecIso (.of k)).inv (c j)) •
            pullbackGlobalSections (projectiveSpaceOver.toIntegralAtUniverse n (Spec (.of k)))
              (twistingSheafAtUniverse.{u} n)
              (Stacks.TwistPullbackPinned.coordGlobalSection.{u} n j)))
      Smooth ((H.comap i).subschemeι ≫ i ≫ pullback.fst (terminal.from (Spec (.of k)))
          (terminal.from (projectiveSpaceAtUniverse.{u} n))) ∧
        IrreducibleSpace (H.comap i).subscheme
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.32, Tag 0G4C](https://stacks.math.columbia.edu/tag/0G4C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
