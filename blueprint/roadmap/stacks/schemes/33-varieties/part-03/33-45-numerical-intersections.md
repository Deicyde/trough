---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_eulerPolynomial_twistedSheaf_of_isProper, AlgebraicGeometry.exists_eulerPolynomial_sub_topDimComponents_totalDegree_lt, AlgebraicGeometry.intersectionNumber, AlgebraicGeometry.intersectionNumber_eq_coeff, AlgebraicGeometry.selfIntersectionNumber, AlgebraicGeometry.intersectionNumber_isInteger, AlgebraicGeometry.intersectionNumber_tensor, AlgebraicGeometry.intersectionNumber_update_tensor
statement: formalized
proof: formalized
---

# 33.45 Numerical intersections

Section 33.45 of the Stacks Project, [Tag 0BEL](https://stacks.math.columbia.edu/tag/0BEL). 13 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BEM, a lemma

[Tag 0BEM](https://stacks.math.columbia.edu/tag/0BEM) in the Stacks Project.

**`AlgebraicGeometry.exists_eulerPolynomial_twistedSheaf_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistedSheaf/EulerPolynomialProper.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TwistedSheaf/EulerPolynomialProper.lean#L38).

> Let `k` be a field, let `X` be a scheme proper over `k`, let `𝓛_1, …, 𝓛_r` be invertible
> `𝒪_X`-modules and let `ℱ` be a coherent `𝒪_X`-module.  Then the Euler characteristics of the
> twists `ℱ ⊗ 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_r^{⊗ n_r}` are the values of a polynomial in `ℚ[n_1, …, n_r]`
> which is zero or of total degree at most `dim Supp ℱ`.

```lean
theorem exists_eulerPolynomial_twistedSheaf_of_isProper (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) {r : ℕ} (L : Fin r → X.Modules)
    [∀ i, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L i)] [IsProper f]
    (F : X.Modules) (hF : _root_.SheafOfModules.IsCoherent F) :
    ∃ P : MvPolynomial (Fin r) ℚ,
      (P = 0 ∨ (P.totalDegree : WithBot ℕ∞) ≤
        topologicalKrullDim (_root_.SheafOfModules.supp F)) ∧
      ∀ n : Fin r → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P
        = (@eulerCharacteristic k _ X f _ (twistedSheaf F L n)
            (@twistedSheaf_isCoherent X r F L _ hF n) : ℚ)
```

## Tag 0BEN, a lemma

[Tag 0BEN](https://stacks.math.columbia.edu/tag/0BEN) in the Stacks Project.

**`AlgebraicGeometry.exists_eulerPolynomial_sub_topDimComponents_totalDegree_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersectionLeadingTerm.lean, line 982](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersectionLeadingTerm.lean#L982). The attribute's comment: “the Euler characteristic minus the length-weighted Euler characteristics of the top-dimensional components of the support is a numerical polynomial of lower total degree”.

> **[Stacks, Tag 0BEN].** For `X` proper over a field `k`, a coherent `𝒪_X`-module `ℱ` and
> invertible `𝒪_X`-modules `𝓛_1, …, 𝓛_r`, the difference between
> `χ(X, ℱ ⊗ 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_r^{⊗ n_r})` and the sum over the top-dimensional integral
> components `Z` of `Supp ℱ`, weighted by the length of `ℱ` at the generic point of `Z`, of
> `χ(Z, 𝒪_Z ⊗ 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_r^{⊗ n_r})` is a numerical polynomial in `n_1, …, n_r` of
> total degree strictly less than `dim Supp ℱ`.

```lean
theorem exists_eulerPolynomial_sub_topDimComponents_totalDegree_lt (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] {r : ℕ} (L : Fin r → X.Modules)
    [∀ i, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L i)]
    (F : X.Modules) [F.IsCoherent] :
    ∃ P : MvPolynomial (Fin r) ℚ,
      (P = 0 ∨ ((P.totalDegree : ℕ) : WithBot ℕ∞) <
        topologicalKrullDim (_root_.SheafOfModules.supp F)) ∧
      ∀ n : Fin r → ℤ, MvPolynomial.eval (fun j ↦ (n j : ℚ)) P =
        (eulerCharacteristic k f (twistedSheaf F L n) : ℚ) -
          ∑ᶠ Z : TopDimIntegralSubscheme F,
            (Stacks.Chow.sheafMultiplicity F Z.genericPt : ℚ) *
              (componentTwistEulerCharacteristic k f L Z n : ℚ)
```

## Tag 0BEP, a definition

[Tag 0BEP](https://stacks.math.columbia.edu/tag/0BEP) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L192). References: SGA 6 XIII (2.1); SGA 6 X (4.4), “defn of (L\_1..L\_d;F)”.

> **Stacks 0BEP.** The intersection number `(𝓛_1 ⋯ 𝓛_d · Z)` of `d` invertible
> `𝒪_X`-modules against a closed subscheme `i : Z ⟶ X` of dimension at most `d` of a proper
> scheme `X` over a field `k`: the coefficient of `n_1 ⋯ n_d` in the numerical polynomial
> `χ(Z, 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_d^{⊗ n_d}|_Z)`, computed as the `d`-fold mixed finite difference
>
> `∑_{T ⊆ {1, …, d}} (-1)^{d - |T|} χ(Z, ⨂_{j ∈ T} 𝓛_j|_Z)`
>
> of that function.  This is an honest integer, which is Stacks 0BEQ: only finitely many values of
> the function are used, so neither polynomiality nor a choice of representing polynomial enters.
> The Euler characteristic is written out as the alternating sum of the dimensions of the
> cohomology groups, so that no coherence hypothesis is needed to state the definition;
> `AlgebraicGeometry.intersectionNumber_eq_sum_eulerCharacteristic` is the comparison with
> `AlgebraicGeometry.eulerCharacteristic`.

```lean
public noncomputable def intersectionNumber (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (_hd : topologicalKrullDim Z ≤ d) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)] : ℤ
```

**`AlgebraicGeometry.intersectionNumber_eq_coeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L260). The attribute's comment: “the coefficient of n\_1 ⋯ n\_d”. References: SGA 6 XIII (2.1), “coeff of n\_1⋯n\_s”; SGA 6 X (4.4), “defn of (L\_1..L\_d;F)”.

> **Stacks 0BEP, the coefficient of `n_1 ⋯ n_d`.**  If a rational polynomial `P` in `d`
> variables of total degree at most `d` takes the Euler characteristics
> `χ(Z, 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_d^{⊗ n_d}|_Z)` as its values at the integral tuples, then the
> intersection number `(𝓛_1 ⋯ 𝓛_d · Z)` is the coefficient of `n_1 ⋯ n_d` in `P`.
>
> This is the source's own description of the intersection number.  The existence of such a `P`,
> which is Stacks 0BEM, is not assumed: the statement is unconditional in `P`, and the proof is
> the monomial computation
> `MvPolynomial.sum_neg_one_pow_mul_eval_indicator_eq_coeff_one`.

```lean
public theorem intersectionNumber_eq_coeff (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ d) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)]
    (P : MvPolynomial (Fin d) ℚ)
    (hP : ∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
      ((@eulerCharacteristic k _ Z (i ≫ f) inferInstance
        (twistedSheaf (SheafOfModules.unit Z.ringCatSheaf)
          (fun j => (Scheme.Modules.pullback i).obj (L j)) n)
        (isCoherent_twistedSheafUnitPullback k f i L n) : ℤ) : ℚ))
    (hdeg : P.totalDegree ≤ d) :
    ((intersectionNumber k f i d hd L : ℤ) : ℚ) =
      P.coeff (Finsupp.equivFunOnFinite.symm fun _ => 1)
```

**`AlgebraicGeometry.selfIntersectionNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L311). The attribute's comment: “the self-intersection notation (L^d · Z)”. References: SGA 6 XIII (2.1), “all L\_i equal”.

> **Stacks 0BEP, the self-intersection notation `(𝓛^d · Z)`.**  The intersection number of a
> single invertible `𝒪_X`-module `𝓛` repeated `d` times against a closed subscheme `i : Z ⟶ X` of
> dimension at most `d`.

```lean
public noncomputable def selfIntersectionNumber (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ d) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] : ℤ
```

## Tag 0BEQ, a lemma

[Tag 0BEQ](https://stacks.math.columbia.edu/tag/0BEQ) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_isInteger`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersectionIntegrality.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersectionIntegrality.lean#L164).

> **Stacks 0BEQ.** In the situation of Stacks 0BEP — `k` a field, `X` a scheme proper over `k`,
> `i : Z ⟶ X` a closed subscheme of dimension at most `d`, and `𝓛_1, …, 𝓛_d` invertible
> `𝒪_X`-modules — the intersection number `(𝓛_1 ⋯ 𝓛_d · Z)` is an integer.
>
> The intersection number is the coefficient of the squarefree monomial `n_1 ⋯ n_d` in the
> numerical polynomial `χ(Z, 𝓛_1^{⊗ n_1} ⊗ ⋯ ⊗ 𝓛_d^{⊗ n_d}|_Z)` of Stacks 0BEM, whose
> coefficients are a priori only rational; the assertion is that this one is integral.  The
> polynomial is not assumed: Stacks 0BEM, available unconditionally as
> `AlgebraicGeometry.exists_eulerPolynomial_twistedSheaf_of_isProper`, produces it, and its total
> degree is at most `dim Supp 𝒪_Z ≤ dim Z ≤ d`.  The integer produced is
> `AlgebraicGeometry.intersectionNumber k f i d hd L`, by
> `AlgebraicGeometry.intersectionNumber_eq_coeff`.
>
> The integrality itself is
> `AlgebraicGeometry.exists_int_coeff_one_of_eval_eq_eulerCharacteristic`, which holds for every
> polynomial of total degree at most `d` representing those Euler characteristics.

```lean
public theorem intersectionNumber_isInteger (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ d) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)] :
    ∃ P : MvPolynomial (Fin d) ℚ,
      (∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
        ((@eulerCharacteristic k _ Z (i ≫ f) inferInstance
          (twistedSheaf (SheafOfModules.unit Z.ringCatSheaf)
            (fun j => (Scheme.Modules.pullback i).obj (L j)) n)
          (isCoherent_twistedSheafUnitPullback k f i L n) : ℤ) : ℚ)) ∧
        P.totalDegree ≤ d ∧
        ∃ m : ℤ, P.coeff (Finsupp.equivFunOnFinite.symm fun _ => 1) = (m : ℚ)
```

## Tag 0BER, a lemma

[Tag 0BER](https://stacks.math.columbia.edu/tag/0BER) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Additivity.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Additivity.lean#L499). The attribute's comment: “additivity of the intersection number in each invertible module”.

> **[Stacks, Tag 0BER].**  The intersection number is additive in each slot: if `𝓛_j` is the
> tensor product of `𝓛_j'` and `𝓛_j''`, and the three families of invertible modules agree away
> from `j`, then
>
> `(𝓛_1 ⋯ 𝓛_j ⋯ 𝓛_d · Z) = (𝓛_1 ⋯ 𝓛_j' ⋯ 𝓛_d · Z) + (𝓛_1 ⋯ 𝓛_j'' ⋯ 𝓛_d · Z)`.

```lean
public theorem intersectionNumber_tensor (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ d) (j : Fin d) (L L' L'' : Fin d → X.Modules)
    [∀ q, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L q)]
    [∀ q, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L' q)]
    [∀ q, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L'' q)]
    (hL' : ∀ q, q ≠ j → L' q = L q) (hL'' : ∀ q, q ≠ j → L'' q = L q)
    (hj : L j ≅ (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (X.presheaf) (forget₂ CommRingCat RingCat)
        (X.ringCatSheaf.2)⟩).obj ((L' j))).obj ((L'' j)))) :
    intersectionNumber k f i d hd L =
      intersectionNumber k f i d hd L' + intersectionNumber k f i d hd L''
```

**`AlgebraicGeometry.intersectionNumber_update_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Additivity.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Additivity.lean#L638). The attribute's comment: “additivity in the j-th slot, written with Function.update”.

> **[Stacks, Tag 0BER], the `Function.update` form.**  If `𝓛_j ≅ 𝓜 ⊗ 𝓝` then
>
> `(𝓛_1 ⋯ 𝓛_j ⋯ 𝓛_d · Z) = (𝓛_1 ⋯ 𝓜 ⋯ 𝓛_d · Z) + (𝓛_1 ⋯ 𝓝 ⋯ 𝓛_d · Z)`,
>
> the two families on the right being the given one with its `j`-th member replaced.

```lean
public theorem intersectionNumber_update_tensor (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ d) (j : Fin d) (L : Fin d → X.Modules)
    [∀ q, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L q)] (M N : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 M]
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 N]
    (hj : L j ≅ (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (X.presheaf) (forget₂ CommRingCat RingCat)
        (X.ringCatSheaf.2)⟩).obj (M)).obj (N))) :
    intersectionNumber k f i d hd L =
      intersectionNumber k f i d hd (Function.update L j M) +
        intersectionNumber k f i d hd (Function.update L j N)
```

## Tag 0BES, a lemma

[Tag 0BES](https://stacks.math.columbia.edu/tag/0BES) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_eq_sum_topDimComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Components.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Components.lean#L118). The attribute's comment: “the intersection number is the length-weighted sum of the intersection numbers of the top-dimensional irreducible components”.

> **[Stacks, Tag 0BES].**  Let `k` be a field, let `X` be proper over `k`, let `i : Z ⟶ X` be
> a closed subscheme of dimension `d` and let `𝓛_1, …, 𝓛_d` be invertible `𝒪_X`-modules.  Writing
> `Z_1, …, Z_t` for the irreducible components of `Z` of dimension `d`, with generic points `ξ_i`
> and multiplicities `m_i = length_{𝒪_{X, ξ_i}} 𝒪_{Z, ξ_i}`, the intersection number of `Z` is
> the weighted sum of those of its components:
>
> `(𝓛_1 ⋯ 𝓛_d · Z) = ∑_i m_i (𝓛_1 ⋯ 𝓛_d · Z_i)`.

```lean
public theorem intersectionNumber_eq_sum_topDimComponents (k : Type u) [Field k]
    {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z = (d : WithBot ℕ∞)) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)] :
    intersectionNumber k f i d hd.le L =
      ∑ᶠ W : TopDimIntegralSubscheme
          ((Scheme.Modules.pushforward i).obj (Stacks.Ample.unitModule Z)),
        Stacks.Chow.sheafMultiplicity
            ((Scheme.Modules.pushforward i).obj (Stacks.Ample.unitModule Z)) W.genericPt *
          intersectionNumber k f W.1.subschemeι d
            (topologicalKrullDim_subscheme_le_of_topDimIntegralSubscheme i hd W) L
```

**`AlgebraicGeometry.intersectionNumber_eq_sum_dimComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/ComponentsVanishing.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/ComponentsVanishing.lean#L199).

> **[Stacks, Tag 0BES].**  Let `k` be a field, let `X` be proper over `k`, let `i : Z ⟶ X` be
> a closed subscheme of dimension at most `d` and let `𝓛_1, …, 𝓛_d` be invertible `𝒪_X`-modules.
> Writing `Z_1, …, Z_t` for the irreducible components of `Z` of dimension `d`, with generic
> points `ξ_i` and multiplicities `m_i = length_{𝒪_{X, ξ_i}} 𝒪_{Z, ξ_i}`, the intersection number
> of `Z` is the weighted sum of those of its `d`-dimensional components:
>
> `(𝓛_1 ⋯ 𝓛_d · Z) = ∑_i m_i (𝓛_1 ⋯ 𝓛_d · Z_i)`.
>
> For `dim Z = d` this is
> `AlgebraicGeometry.intersectionNumber_eq_sum_topDimComponents`, the components of dimension `d`
> being then the top-dimensional ones; for `dim Z < d` both sides are zero, the sum being
> empty.

```lean
public theorem intersectionNumber_eq_sum_dimComponents (k : Type u) [Field k]
    {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ (d : WithBot ℕ∞)) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)] :
    intersectionNumber k f i d hd L =
      ∑ᶠ W : DimIntegralSubscheme
          ((Scheme.Modules.pushforward i).obj (Stacks.Ample.unitModule Z)) d,
        Stacks.Chow.sheafMultiplicity
            ((Scheme.Modules.pushforward i).obj (Stacks.Ample.unitModule Z)) W.genericPt *
          intersectionNumber k f W.1.subschemeι d W.topologicalKrullDim_le L
```

## Tag 0BET, a lemma

[Tag 0BET](https://stacks.math.columbia.edu/tag/0BET) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_pullback_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Pullback.lean, line 662](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Pullback.lean#L662). The attribute's comment: “the right-hand side is zero when the scheme-theoretic image has dimension less than d”.

> **[Stacks, Tag 0BET], the case of a scheme-theoretic image of smaller dimension.** Let `k`
> be a field, let `f : Y ⟶ X` be a morphism of schemes proper over `k`, let `i : Z ⟶ Y` be an
> integral closed subscheme of dimension at most `d` and let `𝓛_1, …, 𝓛_d` be invertible
> `𝒪_X`-modules.  If the scheme-theoretic image `f(Z)` has dimension less than `d`, then
>
> `(f^*𝓛_1 ⋯ f^*𝓛_d · Z) = 0`.

```lean
public theorem intersectionNumber_pullback_eq_zero (k : Type u) [Field k] {Y X Z : Scheme.{u}}
    (pY : Y ⟶ Spec (.of k)) (pX : X ⟶ Spec (.of k)) [IsProper pY] [IsProper pX]
    (f : Y ⟶ X) (hf : f ≫ pX = pY) (i : Z ⟶ Y) [IsClosedImmersion i] [IsIntegral Z]
    (d : ℕ) (hd : topologicalKrullDim Z ≤ (d : WithBot ℕ∞)) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)]
    (hIm : topologicalKrullDim (i ≫ f).image < (d : WithBot ℕ∞)) :
    intersectionNumber k pY i d hd (fun j => (Scheme.Modules.pullback f).obj (L j)) = 0
```

**`AlgebraicGeometry.intersectionNumber_pullback_eq_degreeOver_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Pullback.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Pullback.lean#L698). The attribute's comment: “the degree formula when the scheme-theoretic image has the same dimension”.

> **[Stacks, Tag 0BET], the equal-dimensional case.** Let `k` be a field, let `f : Y ⟶ X` be a
> morphism of schemes proper over `k`, let `i : Z ⟶ Y` be an integral closed subscheme of
> dimension `d` and let `𝓛_1, …, 𝓛_d` be invertible `𝒪_X`-modules.  If the scheme-theoretic image
> `f(Z)` again has dimension `d`, then
>
> `(f^*𝓛_1 ⋯ f^*𝓛_d · Z) = deg(f|_Z : Z → f(Z)) (𝓛_1 ⋯ 𝓛_d · f(Z))`,
>
> the degree being the one of [Stacks, Morphisms, Definition 02NY].

```lean
public theorem intersectionNumber_pullback_eq_degreeOver_mul (k : Type u) [Field k]
    {Y X Z : Scheme.{u}} (pY : Y ⟶ Spec (.of k)) (pX : X ⟶ Spec (.of k))
    [IsProper pY] [IsProper pX] (f : Y ⟶ X) (hf : f ≫ pX = pY) (i : Z ⟶ Y)
    [IsClosedImmersion i] [IsIntegral Z] (d : ℕ)
    (hZ : topologicalKrullDim Z = (d : WithBot ℕ∞)) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)]
    (hIm : topologicalKrullDim (i ≫ f).image = (d : WithBot ℕ∞)) :
    haveI : IsProper (i ≫ f) := isProper_comp_of_structureMap k pY pX f hf i
    haveI : IsIntegral (i ≫ f).image := Stacks.Chow.isIntegral_image (i ≫ f)
    haveI : IsProper (i ≫ f).toImage := Stacks.Chow.isProper_toImage (i ≫ f)
    intersectionNumber k pY i d hZ.le (fun j => (Scheme.Modules.pullback f).obj (L j)) =
      degreeOver (i ≫ f).toImage *
        intersectionNumber k pX (i ≫ f).imageι d hIm.le L
```

## Tag 0BEU, a lemma

[Tag 0BEU](https://stacks.math.columbia.edu/tag/0BEU) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_eq_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/DivisorIntersectionProper.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/DivisorIntersectionProper.lean#L92). The attribute's comment: “taking the divisor's dimension bound as an argument”.

> **[Stacks, Tag 0BEU].**  Let `k` be a field, let `X` be a scheme proper over `k`, let
> `i : Z ⟶ X` be a closed subscheme of dimension at most `d + 1` and let `𝓛_1, …, 𝓛_{d+1}` be
> invertible `𝒪_X`-modules.  Let `D ⊆ Z` be an effective Cartier divisor of dimension at most `d`
> with `𝓛_1|_Z ≅ 𝒪_Z(D)`.  Then
>
> `(𝓛_1 ⋯ 𝓛_{d+1} · Z) = (𝓛_2 ⋯ 𝓛_{d+1} · D)`,
>
> the intersection number of the divisor being taken along the composite closed immersion
> `D ⟶ Z ⟶ X`.
>
> This is
> `AlgebraicGeometry.intersectionNumber_eq_intersectionNumber_of_isEffectiveCartierDivisor` with
> its hypothesis `hfin` discharged by
> `AlgebraicGeometry.forall_finiteDimensional_cohomologyOverField_of_isProper`, which is
> [Stacks, Tag 02O6].
>
> The bound `hdD` on the dimension of the divisor is still an argument here; it is *not* part of
> Tag 0BEU's data, being a consequence of `hd`, and it is discharged in
> `AlgebraicGeometry.intersectionNumber_eq_of_isEffectiveCartierDivisor'`, which therefore carries
> the tag with no bound to supply. This form keeps its own registration.

```lean
public theorem intersectionNumber_eq_of_isEffectiveCartierDivisor
    (k : Type u) [Field k] {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hd : topologicalKrullDim Z ≤ (d + 1 : ℕ)) (L : Fin (d + 1) → X.Modules)
    [∀ t, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L t)]
    (Dv : Z.IdealSheafData) [hDv : IsEffectiveCartierDivisor Dv]
    (hdD : topologicalKrullDim Dv.subscheme ≤ d)
    (hL : (Scheme.Modules.pullback i).obj (L 0) ≅ (invertibleSheaf Dv : Z.Modules)) :
    intersectionNumber k f i (d + 1) hd L =
      intersectionNumber k f (Dv.subschemeι ≫ i) d hdD fun t : Fin d => L t.succ
```

**`AlgebraicGeometry.intersectionNumber_eq_of_isEffectiveCartierDivisor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/DivisorIntersectionProper.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/DivisorIntersectionProper.lean#L142). The attribute's comment: “the intersection number of a closed subscheme against invertible modules equals that of an effective Cartier divisor cutting out the first module's restriction”.

> **[Stacks, Tag 0BEU].**  Let `k` be a field, let `X` be a scheme proper over `k`, let
> `i : Z ⟶ X` be a closed subscheme of dimension at most `d + 1` and let `𝓛_1, …, 𝓛_{d+1}` be
> invertible `𝒪_X`-modules.  Let `D ⊆ Z` be an effective Cartier divisor with
> `𝓛_1|_Z ≅ 𝒪_Z(D)`.  Then
>
> `(𝓛_1 ⋯ 𝓛_{d+1} · Z) = (𝓛_2 ⋯ 𝓛_{d+1} · D)`,
>
> the intersection number of the divisor being taken along the composite closed immersion
> `D ⟶ Z ⟶ X`.
>
> This is the tag with nothing assumed.  Beyond `hd`, `hL` and the effective Cartier divisor
> instance — which are the tag's own data — it has no hypothesis: the dimension bound
> `dim D ≤ d` that the right-hand intersection number needs is supplied by
> `AlgebraicGeometry.topologicalKrullDim_subscheme_le_of_isEffectiveCartierDivisor_of_isProper`,
> since an effective Cartier divisor is nowhere dense and so loses a dimension.

```lean
public theorem intersectionNumber_eq_of_isEffectiveCartierDivisor'
    (k : Type u) [Field k] {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hd : topologicalKrullDim Z ≤ (d + 1 : ℕ)) (L : Fin (d + 1) → X.Modules)
    [∀ t, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L t)]
    (Dv : Z.IdealSheafData) [hDv : IsEffectiveCartierDivisor Dv]
    (hL : (Scheme.Modules.pullback i).obj (L 0) ≅ (invertibleSheaf Dv : Z.Modules)) :
    intersectionNumber k f i (d + 1) hd L =
      intersectionNumber k f (Dv.subschemeι ≫ i) d
        (topologicalKrullDim_subscheme_le_of_isEffectiveCartierDivisor_of_isProper k f i d hd Dv)
        fun t : Fin d => L t.succ
```

## Tag 0BEV, a lemma

[Tag 0BEV](https://stacks.math.columbia.edu/tag/0BEV) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean#L275).

> **[Stacks, Tag 0BEV].** Let `k` be a field, let `X` be a scheme proper over `k`, let
> `i : Z ⟶ X` be a closed subscheme of dimension `d` and let `𝓛_1, …, 𝓛_d` be ample invertible
> `𝒪_X`-modules.  Then the intersection number `(𝓛_1 ⋯ 𝓛_d · Z)` is positive.

```lean
public theorem intersectionNumber_pos (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hdim : topologicalKrullDim Z = (d : WithBot ℕ∞)) (L : Fin d → X.Modules)
    [∀ j, SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 (L j)]
    (hL : ∀ j, Scheme.Modules.IsAmple X (L j)) :
    0 < intersectionNumber k f i d hdim.le L
```

**`AlgebraicGeometry.selfIntersectionNumber_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean#L286). The attribute's comment: “the self-intersection number of a single ample module”.

> **[Stacks, Tag 0BEV] for the self-intersection number** `(𝓛^d · Z)` of a single ample
> invertible module.

```lean
public theorem selfIntersectionNumber_pos (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hdim : topologicalKrullDim Z = (d : WithBot ℕ∞)) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) :
    0 < selfIntersectionNumber k f i d hdim.le L
```

**`AlgebraicGeometry.degreeWithRespectTo_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/Positivity.lean#L297). The attribute's comment: “the degree deg\_L(Z) of Tag 0BEW is positive”.

> **[Stacks, Tag 0BEV] for the degree** `deg_𝓛(Z)` of [Stacks, Tag 0BEW]: the degree of a
> closed subscheme with respect to an ample invertible module is positive.

```lean
public theorem degreeWithRespectTo_pos (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i] (d : ℕ)
    (hdim : topologicalKrullDim Z = (d : WithBot ℕ∞)) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) :
    0 < degreeWithRespectTo k f i d hdim L hL
```

## Tag 0BEW, a definition

[Tag 0BEW](https://stacks.math.columbia.edu/tag/0BEW) in the Stacks Project.

**`AlgebraicGeometry.degreeWithRespectTo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L338).

> **Stacks 0BEW.** The degree `deg_𝓛(Z)` of a closed subscheme `i : Z ⟶ X` of a proper scheme
> `X` over a field `k` with respect to an ample invertible `𝒪_X`-module `𝓛`: the intersection
> number `(𝓛^d · Z)` for `d` the dimension of `Z`.
>
> The dimension is passed as a natural number `d` together with the hypothesis
> `topologicalKrullDim Z = d`, which is what makes `d` the source's `dim(Z)`; `d` is therefore
> determined by the data and the degree does not depend on which `d` is supplied.  An empty `Z` has
> dimension `⊥` and an infinite-dimensional `Z` has dimension `⊤`, neither of which is
> `(d : WithBot ℕ∞)` for a natural number `d`, so no value is assigned to them — see the
> implementation notes.  Ampleness is not used in the body: the source requires it so that
> `deg_𝓛` deserves the name of a degree, and it is carried for that reason.

```lean
public noncomputable def degreeWithRespectTo (k : Type u) [Field k] {X Z : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (d : ℕ) (hd : topologicalKrullDim Z = d) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (_hample : Scheme.Modules.IsAmple X L) : ℤ
```

## Tag 0BEX, a lemma

[Tag 0BEX](https://stacks.math.columbia.edu/tag/0BEX) in the Stacks Project.

**`AlgebraicGeometry.selfIntersectionNumber_pullback_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/FiniteDominant.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/FiniteDominant.lean#L227). The attribute's comment: “for an arbitrary invertible module, with no ampleness”.

> **[Stacks, Tag 0BEX].** Let `k` be a field, let `f : Y ⟶ X` be a finite dominant morphism of
> proper varieties over `k` of dimension `d` and let `𝓛` be an invertible `𝒪_X`-module.  Then
>
> `(f^*𝓛^d · Y) = deg(f) (𝓛^d · X)`,
>
> the degree `deg(f) = [R(Y) : R(X)]` being `AlgebraicGeometry.degreeOver` of
> [Stacks, Morphisms, Definition 02NY].  For `𝓛` ample both sides are the degrees
> `deg_{f^*𝓛}(Y)` and `deg_𝓛(X)` of [Stacks, Tag 0BEW], which is the source's statement; see
> `AlgebraicGeometry.degreeWithRespectTo_pullback_of_isFinite`.
>
> Ampleness is not assumed: it is not used by the source's proof and neither side needs it to be
> formed.

```lean
public theorem selfIntersectionNumber_pullback_of_isFinite (k : Type u) [Field k]
    {Y X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsVariety k p] [IsProper p] (f : Y ⟶ X)
    [IsFinite f] [IsDominant f] [IsVariety k (f ≫ p)] (d : ℕ)
    (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    selfIntersectionNumber k (f ≫ p) (𝟙 Y) d
          (((topologicalKrullDim_eq_of_isFinite_of_isDominant f).trans hd).le)
          ((Scheme.Modules.pullback f).obj L) =
      (degreeOver f : ℤ) * selfIntersectionNumber k p (𝟙 X) d hd.le L
```

**`AlgebraicGeometry.degreeWithRespectTo_pullback_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/FiniteDominant.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/FiniteDominant.lean#L298).

> **[Stacks, Tag 0BEX].** Let `k` be a field, let `f : Y ⟶ X` be a finite dominant morphism of
> proper varieties over `k` and let `𝓛` be an ample invertible `𝒪_X`-module.  Then
>
> `deg_{f^*𝓛}(Y) = deg(f) deg_𝓛(X)`,
>
> the degrees being those of [Stacks, Tag 0BEW] and `deg(f) = [R(Y) : R(X)]` that of
> [Stacks, Morphisms, Definition 02NY].
>
> The dimension of `X` is passed as a natural number `d` together with
> `topologicalKrullDim X = d`, as `AlgebraicGeometry.degreeWithRespectTo` asks; the dimension of
> `Y` is then `d` too and is not a hypothesis.  Neither is the ampleness of `f^*𝓛` that the
> left-hand side needs: it is `AlgebraicGeometry.isAmple_pullback_of_isFinite`.
>
> The content is `AlgebraicGeometry.selfIntersectionNumber_pullback_of_isFinite`, which does not
> mention ampleness; `AlgebraicGeometry.degreeWithRespectTo` is by definition the
> self-intersection number, so this is that statement read at the source's notation.

```lean
public theorem degreeWithRespectTo_pullback_of_isFinite (k : Type u) [Field k]
    {Y X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsVariety k p] [IsProper p] (f : Y ⟶ X)
    [IsFinite f] [IsDominant f] [IsVariety k (f ≫ p)] (d : ℕ)
    (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Scheme.Modules.IsAmple X L) :
    degreeWithRespectTo k (f ≫ p) (𝟙 Y) d
          ((topologicalKrullDim_eq_of_isFinite_of_isDominant f).trans hd)
          ((Scheme.Modules.pullback f).obj L) (isAmple_pullback_of_isFinite f L hL) =
      (degreeOver f : ℤ) * degreeWithRespectTo k p (𝟙 X) d hd L hL
```

## Tag 0BEY, a lemma

[Tag 0BEY](https://stacks.math.columbia.edu/tag/0BEY) in the Stacks Project.

**`AlgebraicGeometry.intersectionNumber_one_eq_invertibleCurveDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L369).

> **Stacks 0BEY.** For a closed subscheme `Z ⊂ X` of dimension at most one of a proper scheme
> `X` over a field `k` and an invertible `𝒪_X`-module `𝓛`, the intersection number `(𝓛 · Z)` is
> the degree `deg(𝓛|_Z)` of Stacks 0AYR.
>
> The source's proof is that `n ↦ χ(Z, 𝓛|_Z^{⊗ n})` has degree one, so its leading coefficient is
> the difference of consecutive values.  With the finite difference as the definition that
> difference *is* the intersection number: the sum over `Finset (Fin 1)` has the two terms
> `-χ(Z, 𝒪_Z)` and `χ(Z, 𝓛|_Z)`, the first twist being the trivial one
> (`AlgebraicGeometry.twistedSheafZeroIso`) and the second `𝓛|_Z` itself
> (`Stacks.SheafOfModules.Invertible.tensorPowerOneIso` and the left unitor), and
> `AlgebraicGeometry.invertibleCurveDegree` is by definition their difference.  Neither
> polynomiality nor a degree computation is needed, so the statement keeps the source's `≤ 1`;
> it is in fact true for every `Z`.

```lean
public theorem intersectionNumber_one_eq_invertibleCurveDegree (k : Type u) [Field k]
    {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (hdim : topologicalKrullDim Z ≤ 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    intersectionNumber k f i 1 hdim (fun _ => L) =
      invertibleCurveDegree k (i ≫ f) hdim ((Scheme.Modules.pullback i).obj L)
```

**`AlgebraicGeometry.degreeWithRespectTo_eq_invertibleCurveDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersection.lean#L425). The attribute's comment: “the ample case”.

> **Stacks 0BEY, the ample case.** For a closed subscheme `Z ⊂ X` of dimension one of a proper
> scheme `X` over a field `k` and an ample invertible `𝒪_X`-module `𝓛`, the degree `deg_𝓛(Z)` of
> Stacks 0BEW is the degree `deg(𝓛|_Z)` of Stacks 0AYR.
>
> The source states this for `Z` of dimension at most one, but at dimension zero the two numbers
> differ: `deg_𝓛(Z)` is then `(𝓛^0 · Z) = χ(Z, 𝒪_Z)`
> (`AlgebraicGeometry.intersectionNumber_zero`) while `deg(𝓛|_Z)` is `χ(Z, 𝓛|_Z) - χ(Z, 𝒪_Z)`,
> and for a nonempty zero-dimensional `Z` the first is the positive integer `dim_k Γ(Z, 𝒪_Z)` and
> the second is `0`.  The hypothesis is therefore `topologicalKrullDim Z = 1`, which is where
> `deg_𝓛(Z)` is the intersection number `(𝓛 · Z)`; the conclusion is then
> `AlgebraicGeometry.intersectionNumber_one_eq_invertibleCurveDegree`, which does keep the
> source's `≤ 1`.

```lean
public theorem degreeWithRespectTo_eq_invertibleCurveDegree (k : Type u) [Field k]
    {X Z : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (i : Z ⟶ X) [IsClosedImmersion i]
    (hd : topologicalKrullDim Z = 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hample : Scheme.Modules.IsAmple X L) :
    degreeWithRespectTo k f i 1 hd L hample =
      invertibleCurveDegree k (i ≫ f) hd.le ((Scheme.Modules.pullback i).obj L)
```

## Tag 0BJ8, a proposition

[Tag 0BJ8](https://stacks.math.columbia.edu/tag/0BJ8) in the Stacks Project.

**`AlgebraicGeometry.degreeWithRespectTo_div_factorial_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean#L276). The attribute's comment: “the leading coefficient deg\_L(X)/d! is a positive constant”.

> **[Stacks, Tag 0BJ8], the leading coefficient.**  For `X` proper over `k` of dimension `d`
> and `𝓛` ample, the constant `deg_𝓛(X)/d!` is positive.  The degree `deg_𝓛(X)` is positive by
> [Stacks, Tag 0BEV] and `d!` is positive.

```lean
public theorem degreeWithRespectTo_div_factorial_pos :
    0 < (degreeWithRespectTo k f (𝟙 X) d hdim L hL : ℚ) / (d.factorial : ℚ)
```

**`AlgebraicGeometry.exists_degree_lt_eventually_finrank_globalSections_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean#L382). The attribute's comment: “the asymptotic formula for dim\_k Γ(X, L^n)”.

> **[Stacks, Tag 0BJ8], the asymptotic formula.**  For `X` proper over `k` of dimension `d` and
> `𝓛` ample, for all sufficiently large `n`
>
> `dim_k Γ(X, 𝓛^{⊗ n}) = deg_𝓛(X)/d! ⬝ n^d + P(n)`
>
> with `P` a rational polynomial of degree strictly less than `d`.

```lean
public theorem exists_degree_lt_eventually_finrank_globalSections_eq :
    ∃ P : Polynomial ℚ, P.degree < (d : WithBot ℕ) ∧
      ∀ᶠ n : ℕ in atTop,
        (Module.finrank k (globalSectionsOverField k f
            (tensorPower X.presheaf X.ringCatSheaf.2 L (n : ℤ))) : ℚ) =
          (degreeWithRespectTo k f (𝟙 X) d hdim L hL : ℚ) / (d.factorial : ℚ) * (n : ℚ) ^ d +
            P.eval (n : ℚ)
```

**`AlgebraicGeometry.asymptotic_riemann_roch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/NumericalIntersections/AsymptoticRiemannRoch.lean#L466).

> **[Stacks, Tag 0BJ8] (Asymptotic Riemann–Roch).**  Let `k` be a field, let `X` be a scheme
> proper over `k` of dimension `d` and let `𝓛` be an ample invertible `𝒪_X`-module.  Then
>
> `dim_k Γ(X, 𝓛^{⊗ n}) = deg_𝓛(X)/d! ⬝ n^d + lower order terms`
>
> for all sufficiently large `n`, and the leading constant `deg_𝓛(X)/d!` is positive.

```lean
public theorem asymptotic_riemann_roch :
    0 < (degreeWithRespectTo k f (𝟙 X) d hdim L hL : ℚ) / (d.factorial : ℚ) ∧
      ∃ P : Polynomial ℚ, P.degree < (d : WithBot ℕ) ∧
        ∀ᶠ n : ℕ in atTop,
          (Module.finrank k (globalSectionsOverField k f
              (tensorPower X.presheaf X.ringCatSheaf.2 L (n : ℤ))) : ℚ) =
            (degreeWithRespectTo k f (𝟙 X) d hdim L hL : ℚ) / (d.factorial : ℚ) * (n : ℚ) ^ d +
              P.eval (n : ℚ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.45, Tag 0BEL](https://stacks.math.columbia.edu/tag/0BEL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
