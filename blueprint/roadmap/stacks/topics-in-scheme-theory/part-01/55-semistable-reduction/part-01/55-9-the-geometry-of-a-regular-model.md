---
declaration: section
origin: cited
lean: Stacks.Models.isEffectiveCartierDivisor_specialFiber, Stacks.Models.RegularModelSituation.isEffectiveCartierDivisor_specialFiberComponent, Stacks.Models.RegularModelSituation.specialFiberIdeal_eq_prod, Stacks.Models.invertibleSheafIsoUnit_specialFiber, Stacks.Models.RegularModelSituation.isGorenstein_model, Stacks.Models.RegularModelSituation.relativeDimension_model, Stacks.Models.RegularModelSituation.isGorenstein_specialFiberComponent, Stacks.Models.RegularModelSituation.isGorenstein_model_and_specialFiberComponents
statement: formalized
proof: formalized
---

# 55.9 The geometry of a regular model

Section 55.9 of the Stacks Project, [Tag 0C5Y](https://stacks.math.columbia.edu/tag/0C5Y). 12 tags here are carried by 45 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C5Z, a lemma

[Tag 0C5Z](https://stacks.math.columbia.edu/tag/0C5Z) in the Stacks Project.

**`Stacks.Models.isEffectiveCartierDivisor_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberCartier.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberCartier.lean#L56). The attribute's comment: “special\_fibre\_cartier”.

> **Stacks Project, Tag 0C5Z.** The scheme-theoretic special fibre of a scheme flat over a
> discrete valuation ring is an effective Cartier divisor: on every affine chart it is the zero
> scheme of the image of a uniformizer, which flatness keeps a nonzerodivisor.

```lean
public theorem isEffectiveCartierDivisor_specialFiber
    {R k : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    [Field k] [Algebra R k]
    (residueEquiv : IsLocalRing.ResidueField R ≃ₐ[R] k)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [Flat f] :
    IsEffectiveCartierDivisor
      (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap R k)))).ker
```

**`Stacks.Models.RegularModelSituation.isEffectiveCartierDivisor_specialFiberComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberComponentCartier.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberComponentCartier.lean#L259). The attribute's comment: “component\_cartier”.

> **Stacks Project, Tag 0C5Z (component clause).** Each irreducible component of the special
> fibre of a regular model, taken with its reduced induced structure as a closed subscheme of the
> model, is an effective Cartier divisor on the model.
>
> It is an integral closed subscheme of codimension one, and every local ring of the regular
> scheme `X` is factorial, so Tag 0AGA applies.

```lean
public theorem isEffectiveCartierDivisor_specialFiberComponent :
    IsEffectiveCartierDivisor (S.specialFiberComponentIdeal Z)
```

**`Stacks.Models.RegularModelSituation.specialFiberIdeal_eq_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberComponentCartier.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberComponentCartier.lean#L421). The attribute's comment: “part (3): X\_k = ∑ mᵢ Cᵢ with mᵢ the multiplicity of Cᵢ in X\_k”.

> **Stacks Project, Tag 0C5Z, part (3).** The special fibre of a regular model is the sum
> `X_k = ∑ mᵢ Cᵢ` of its irreducible components `Cᵢ`, as effective Cartier divisors, with `mᵢ`
> the multiplicity of `Cᵢ` in `X_k`. Divisor sums are written multiplicatively.
>
> The components are integral effective Cartier divisors covering the special fibre, so
> [Stacks, Tag 0BCP] writes `X_k` as some nonnegative combination `∑ aᵢ Cᵢ`; reading off the order
> at the generic point of each `Cᵢ`, which is a discrete valuation ring, gives `aᵢ = mᵢ`.

```lean
public theorem specialFiberIdeal_eq_prod :
    S.specialFiberIdeal =
      ∏ Z, S.specialFiberComponentIdeal Z ^ S.specialFiberMultiplicity Z
```

**`Stacks.Models.invertibleSheafIsoUnit_specialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberPrincipal.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberPrincipal.lean#L268). The attribute's comment: “part (4): the special fibre has trivial invertible sheaf”. References: SGA 6 X (7.8), “O\_X(X\_s) ≅ O\_X”.

> **The invertible sheaf of the special fibre is trivial**, `𝒪_X(X_k) ≅ 𝒪_X`, for any scheme
> flat over a discrete valuation ring: the special fibre is the zero scheme of the regular global
> section determined by a uniformizer, and the divisor of a regular section of an invertible
> module reproduces that module.

```lean
public noncomputable def invertibleSheafIsoUnit_specialFiber
    (residueEquiv : IsLocalRing.ResidueField R ≃ₐ[R] k)
    (f : X ⟶ Spec (.of R)) [Flat f] {π : R} (hπ : Irreducible π) :
    invertibleSheaf' (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap R k)))).ker ≅
      SheafOfModules.unit X.ringCatSheaf
```

## Tag 0C60, a lemma

[Tag 0C60](https://stacks.math.columbia.edu/tag/0C60) in the Stacks Project.

**`Stacks.Models.RegularModelSituation.isGorenstein_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean#L101). The attribute's comment: “part (1): Gorenstein morphism”.

> The structure morphism of a regular model of a smooth curve over a discrete valuation ring is
> a Gorenstein morphism.
>
> Local Noetherianity of the fibres is not an extra assumption — it follows from local
> Noetherianity of the total space — so it is packaged existentially, as the Gorenstein-morphism
> predicate of Tag 0C04 takes a proof of it as an argument.

```lean
public theorem isGorenstein_model :
    ∃ hf : ∀ y : Spec (.of S.R), IsLocallyNoetherian (S.X_to_R.fiber y),
      S.X_to_R.IsGorenstein hf
```

**`Stacks.Models.RegularModelSituation.relativeDimension_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean#L168). The attribute's comment: “part (1): relative dimension one”.

> Every nonempty fibre of the structure morphism of a regular model of a smooth curve is
> equidimensional of dimension one.
>
> The generic fibre is the curve `C`, so it is irreducible of dimension one; the total space is
> integral by Tag 0BCM, and Tag 0B2J transports both conclusions to the special fibre.

```lean
public theorem relativeDimension_model : RelativeDimension S.X_to_R 1
```

**`Stacks.Models.RegularModelSituation.isGorenstein_specialFiberComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean#L220). The attribute's comment: “part (2)”.

> Each irreducible component `Cᵢ` of the special fibre of a regular model, taken with its
> reduced induced structure as a closed subscheme of the model, is a Gorenstein scheme.
>
> The component is an effective Cartier divisor on `X` by the component clause of Tag 0C5Z, and
> `X` is regular, hence Gorenstein, so the scheme-theoretic form of Tag 0BJJ applies.

```lean
public theorem isGorenstein_specialFiberComponent (Z : irreducibleComponents S.specialFiber) :
    AlgebraicGeometry.IsGorenstein (S.specialFiberComponentIdeal Z).subscheme
```

**`Stacks.Models.RegularModelSituation.isGorenstein_model_and_specialFiberComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GorensteinGeometry.lean#L229).

> For a regular model `X` of a smooth curve `C` over `K`: the structure morphism
> `X ⟶ Spec(R)` is a Gorenstein morphism of relative dimension one, and each irreducible component
> of the special fibre `X_k` is Gorenstein.

```lean
public theorem isGorenstein_model_and_specialFiberComponents :
    (∃ hf : ∀ y : Spec (.of S.R), IsLocallyNoetherian (S.X_to_R.fiber y),
        S.X_to_R.IsGorenstein hf) ∧
      RelativeDimension S.X_to_R 1 ∧
      ∀ Z : irreducibleComponents S.specialFiber,
        AlgebraicGeometry.IsGorenstein (S.specialFiberComponentIdeal Z).subscheme
```

## Tag 0C61, a situation

[Tag 0C61](https://stacks.math.columbia.edu/tag/0C61) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/RegularProperModel.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/RegularProperModel.lean#L57).

> **Stacks Project, Tag 0C61.** The standing situation of the geometry of a regular model: a
> discrete valuation ring with a chosen uniformizer, a smooth projective curve over its fraction
> field whose only global functions are the constants, and a regular proper model of that
> curve.

```lean
public structure RegularProperModelSituation extends RegularModelSituation.{u}
```

## Tag 0C62, a lemma

[Tag 0C62](https://stacks.math.columbia.edu/tag/0C62) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.connectedSpace_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberConnected.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberConnected.lean#L389). The attribute's comment: “the special fibre X\_k of a regular proper model is connected”. References: SGA 2 XIII (2.2), “special case”; SGA 6 X (7.12), “special case”.

> **[Stacks, Tag 0C62].**  In Situation [Stacks, Tag 0C61] the special fibre `X_k` of the
> regular proper model is connected.
>
> This is the second conclusion of [Stacks, Tag 0AY8] — geometric connectedness of the fibres,
> `RegularProperModelSituation.geometricallyConnected_X_to_R` — read at the closed point of
> `Spec(R)`:  the special fibre is the base change of the model along `Spec(k) ⟶ Spec(R)`, whose
> source is a one-point scheme, and a scheme geometrically connected over a one-point base is
> connected.

```lean
public theorem connectedSpace_specialFiber : ConnectedSpace S.specialFiber
```

## Tag 0C63, a lemma

[Tag 0C63](https://stacks.math.columbia.edu/tag/0C63) in the Stacks Project.

**`Stacks.Models.multiplicityHom_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L135). The attribute's comment: “the first map, which sends 1 to (m\_1, ..., m\_n)”.

> The first map of the sequence sends `1` to the vector `(m₁, …, mₙ)` of multiplicities.

```lean
theorem multiplicityHom_one {ι : Type*} (m : ι → ℕ) :
    multiplicityHom m 1 = fun i => (m i : ℤ)
```

**`Stacks.Models.componentPicardHom_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L157). The attribute's comment: “the second map, which sends the ith basis vector to O\_X(C\_i)”.

> The second map of the sequence sends the `i`th basis vector of `ℤ^{⊕n}` to the class of
> `𝒪_X(Cᵢ)`.

```lean
theorem componentPicardHom_single [DecidableEq ι] (i : ι) :
    componentPicardHom S C (Pi.single i 1) = picardClass (C i)
```

**`Stacks.Models.genericFiberPicardRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L165). The attribute's comment: “the third map, restriction of Picard classes to the generic fibre”.

> **The third map `Pic(X) ⟶ Pic(C)` of the Picard sequence of a regular model**: restriction
> of Picard classes along the inclusion of the generic fibre.

```lean
def genericFiberPicardRestriction : ofScheme S.X →+ ofScheme S.C
```

**`Stacks.Models.componentPicardHom_multiplicityHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L218). The attribute's comment: “the composite Z -> Z^n -> Pic(X) vanishes”.

> The composite of the first two maps of the sequence vanishes.

```lean
theorem componentPicardHom_multiplicityHom (a : ℤ) :
    componentPicardHom S C (multiplicityHom m a) = 0
```

**`Stacks.Models.injective_multiplicityHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L230). The attribute's comment: “exactness at Z, i.e. injectivity of the first map”.

> The first map of the sequence is injective, which is exactness at `ℤ`.

```lean
theorem injective_multiplicityHom : Function.Injective (multiplicityHom (ι := ι) m)
```

**`Stacks.Models.picardSequence_specialFiberComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequence.lean#L258). The attribute's comment: “the two named maps and the clauses proved here, for the components of X\_k”.

> Take the family `C₁, …, Cₙ` to be the irreducible components of `X_k` with their reduced
> induced structure, and let `mᵢ` be multiplicities with `X_k = Σ mᵢ Cᵢ`. Then the first map of
> the sequence sends `1` to `(m₁, …, mₙ)`, the second sends the `i`th basis vector to
> `[𝒪_X(Cᵢ)]`, the composite of the two vanishes, and the first map is injective.

```lean
theorem picardSequence_specialFiberComponents
    (hdec : S.specialFiberIdeal =
      ∏ Z, RegularModelSituation.specialFiberComponentIdeal S.toRegularModelSituation Z ^ m Z) :
    multiplicityHom m 1 = (fun Z => (m Z : ℤ)) ∧
      (∀ Z, componentPicardHom S
          (RegularModelSituation.specialFiberComponentIdeal S.toRegularModelSituation)
          (Pi.single Z 1) =
        picardClass
          (RegularModelSituation.specialFiberComponentIdeal S.toRegularModelSituation Z)) ∧
      (∀ a, componentPicardHom S
        (RegularModelSituation.specialFiberComponentIdeal S.toRegularModelSituation)
        (multiplicityHom m a) = 0) ∧
      Function.Injective (multiplicityHom m)
```

**`Stacks.Models.picardSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequenceExact.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardSequenceExact.lean#L697). References: EGA IV (21.6.11), “special case”; SGA 6 X (7.8), “partial, special case”.

> **Stacks Project, Tag 0C63.** In Situation 0C61 there is an exact sequence
>
> `0 ⟶ ℤ ⟶ ℤ^{⊕n} ⟶ Pic(X) ⟶ Pic(C) ⟶ 0`
>
> where the first map sends `1` to the vector `(m₁, …, mₙ)` of multiplicities of the irreducible
> components `C₁, …, Cₙ` of the special fibre, and the second map sends the `i`th basis vector to
> the class of `𝒪_X(Cᵢ)`.
>
> The three maps are the group homomorphisms `Stacks.Models.multiplicityHom`,
> `Stacks.Models.componentPicardHom` and `Stacks.Models.genericFiberPicardRestriction`, the last
> being pullback of Picard classes along the inclusion of the generic fibre; the components are the
> irreducible components of `X_k` with their reduced induced structure, which are effective Cartier
> divisors by [Stacks, Tag 0C5Z]; and `ℤ^{⊕n}` is the group of integer families on them, the
> components being finitely many. The decomposition `X_k = Σ mᵢ Cᵢ` with which the situation opens
> is part of the conclusion, and the seven conjuncts are, in order: that decomposition, the value
> of the first map on `1`, the values of the second map on the basis vectors, exactness at `ℤ`
> (injectivity of the first map), exactness at `ℤ^{⊕n}`, exactness at `Pic(X)`, and exactness at
> `Pic(C)` (surjectivity of the third map).

```lean
theorem picardSequence_exact (S : RegularProperModelSituation.{u}) :
    ∃ m : irreducibleComponents S.specialFiber → ℕ,
      S.specialFiberIdeal =
          ∏ Z, S.toRegularModelSituation.specialFiberComponentIdeal Z ^ m Z ∧
        multiplicityHom m 1 = (fun Z => (m Z : ℤ)) ∧
        (∀ Z, componentPicardHom S S.toRegularModelSituation.specialFiberComponentIdeal
            (Pi.single Z 1) =
          Stacks.Divisors.picardClass
            (S.toRegularModelSituation.specialFiberComponentIdeal Z)) ∧
        Function.Injective (multiplicityHom m) ∧
        Function.Exact (multiplicityHom m)
            (componentPicardHom S S.toRegularModelSituation.specialFiberComponentIdeal) ∧
        Function.Exact
            (componentPicardHom S S.toRegularModelSituation.specialFiberComponentIdeal)
            (genericFiberPicardRestriction S) ∧
        Function.Surjective (genericFiberPicardRestriction S)
```

## Tag 0C64, a lemma

[Tag 0C64](https://stacks.math.columbia.edu/tag/0C64) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.specialFiberDegreePairing_bilinear_and_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean#L659). The attribute's comment: “the pairing ⟨a, L⟩ = ∑ a\_Z deg(L|\_\{C\_Z}), its bilinearity, and the symmetry ⟨a, O\_X(∑ b\_Y C\_Y)⟩ = ⟨b, O\_X(∑ a\_Z C\_Z)⟩ at integer coefficients”.

> **Stacks Project, Tag 0C64.** In the situation of [Stacks, Tag 0C61], let `C_Z` run over the
> irreducible components of the special fibre of the regular proper model `X ⟶ Spec(R)`, each with
> its reduced induced structure as a closed subscheme of `X`. For an invertible `𝒪_X`-module `ℒ`
> and an integer family `a` the degree pairing is
>
> `⟨a, ℒ⟩ = ∑_Z a_Z · deg(ℒ|_{C_Z})`;
>
> it is bilinear, and for integer families `a` and `b`
>
> `⟨a, 𝒪_X(∑_Y b_Y C_Y)⟩ = ⟨b, 𝒪_X(∑_Z a_Z C_Z)⟩`.
>
> The four clauses are, in order: the defining formula for the pairing, additivity in the
> coefficient family, additivity in the invertible module — the Picard group being written
> multiplicatively, so that addition of its elements is the tensor product — and the symmetry.
> The third is the invertible case of [Stacks, Tag 0AYX] on each component, and the fourth is
> proved as the source proves it: expand both sides by the first three clauses and appeal to the
> symmetry of the intersection matrix
> `deg(𝒪_X(C_Y)|_{C_Z}) = deg(𝒪_X(C_Z)|_{C_Y})`, which is
> `Stacks.Models.RegularProperModelSituation.componentDegree_specialFiberComponent_comm`.

```lean
theorem specialFiberDegreePairing_bilinear_and_comm
    (s : Finset (irreducibleComponents S.specialFiber)) :
    (∀ (a : irreducibleComponents S.specialFiber → ℤ) (L : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L),
        S.specialFiberDegreePairing s a L hL =
          ∑ Z ∈ s, a Z * S.specialFiberComponentDegree Z L hL) ∧
      (∀ (a a' : irreducibleComponents S.specialFiber → ℤ) (L : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L),
        S.specialFiberDegreePairing s (a + a') L hL =
          S.specialFiberDegreePairing s a L hL + S.specialFiberDegreePairing s a' L hL) ∧
      (∀ (a : irreducibleComponents S.specialFiber → ℤ) (L M : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L)
        (hM : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property M)
        (hLM : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property
            ((((Stacks.SheafOfModules.Tensor.sheafTensor
              ⟨(S.X.toRingedSpace).presheaf, (S.X.toRingedSpace).IsSheaf⟩).obj (L)).obj (M)))),
        S.specialFiberDegreePairing s a ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨(S.X.toRingedSpace).presheaf, (S.X.toRingedSpace).IsSheaf⟩).obj (L)).obj (M))) hLM =
          S.specialFiberDegreePairing s a L hL + S.specialFiberDegreePairing s a M hM) ∧
      (∀ a b : irreducibleComponents S.specialFiber → ℤ,
        S.specialFiberDegreePairing s a (S.specialFiberVerticalDivisorSheaf s b)
            (S.isInvertible_specialFiberVerticalDivisorSheaf s b) =
          S.specialFiberDegreePairing s b (S.specialFiberVerticalDivisorSheaf s a)
            (S.isInvertible_specialFiberVerticalDivisorSheaf s a))
```

**`Stacks.Models.degreePairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean#L164). The attribute's comment: “the pairing ⟨a, L⟩ = ∑ aᵢ deg(L|\_\{Cᵢ}); the whole tag, its bilinearity and its symmetry together, is Stacks.Models.RegularProperModelSituation.specialFiberDegreePairing\_bilinear\_and\_comm of StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean”.

> **Stacks Project, Tag 0C64.** The degree pairing `⟨a, ℒ⟩ = ∑ᵢ aᵢ · deg(ℒ|_{Cᵢ})` of an
> integer coefficient family `a` against an invertible `𝒪_X`-module, over a finite family of
> components `Cᵢ` of the special fibre that are proper curves over the residue field.

```lean
def degreePairing (a : ι → ℤ) (L : S.X.Modules)
    (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
      (structureSheafRing S.X.toRingedSpace).property L) : ℤ
```

## Tag 0C65, an equation

[Tag 0C65](https://stacks.math.columbia.edu/tag/0C65) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.specialFiberIntersectionProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean#L583). The attribute's comment: “the second displayed equality, the symmetry ⟨a, O\_X(∑ b\_Y C\_Y)⟩ = ⟨b, O\_X(∑ a\_Z C\_Z)⟩, at the irreducible components of the special fibre and on nonnegative coefficient families; at integer coefficients it is the fourth clause of Stacks.Models.RegularProperModelSituation.specialFiberDegreePairing\_bilinear\_and\_comm”.

> **Stacks Project, Tag 0C65, second equality**, on nonnegative coefficient families: the
> intersection product of the components of the special fibre is symmetric,
> `(∑_Z a_Z C_Z · ∑_Y b_Y C_Y) = (∑_Y b_Y C_Y · ∑_Z a_Z C_Z)`.
>
> This is `Stacks.Models.intersectionProduct_comm_of_expansion_of_matrix_symm` with both of its
> hypotheses discharged: `hexpand` by
> `Stacks.Models.RegularProperModelSituation.specialFiberDivisorDegree_eq_sum` and `hsymm` by
> `Stacks.Models.RegularProperModelSituation.specialFiberIntersectionMatrix_comm`.

```lean
theorem specialFiberIntersectionProduct_comm
    (a b : irreducibleComponents S.specialFiber → ℕ) :
    S.specialFiberIntersectionProduct (fun Z => (a Z : ℤ)) b =
      S.specialFiberIntersectionProduct (fun Z => (b Z : ℤ)) a
```

**`Stacks.Models.RegularProperModelSituation.specialFiberDegreePairing_bilinear_and_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean#L659). The attribute's comment: “the second displayed equality ⟨a, O\_X(∑ b\_Y C\_Y)⟩ = ⟨b, O\_X(∑ a\_Z C\_Z)⟩ at INTEGER coefficient families a, b, which is the fourth clause. Here O\_X(∑ b\_Y C\_Y) is Stacks.Models.RegularProperModelSituation.specialFiberVerticalDivisorSheaf, the difference twist of Stacks 01WX part (4) at the positive and negative parts of b; its degree on C\_Z is ∑\_Y b\_Y (C\_Z · C\_Y) by Stacks.Models.RegularProperModelSituation.specialFiberComponentDegree\_specialFiberVerticalDivisorSheaf\_eq\_sum, and on a nonnegative family the pairing against it is the intersection product Stacks.Models.intersectionProduct of the first displayed equality, by Stacks.Models.RegularProperModelSituation.specialFiberDegreePairing\_specialFiberVerticalDivisorSheaf\_natCast”.

> **Stacks Project, Tag 0C64.** In the situation of [Stacks, Tag 0C61], let `C_Z` run over the
> irreducible components of the special fibre of the regular proper model `X ⟶ Spec(R)`, each with
> its reduced induced structure as a closed subscheme of `X`. For an invertible `𝒪_X`-module `ℒ`
> and an integer family `a` the degree pairing is
>
> `⟨a, ℒ⟩ = ∑_Z a_Z · deg(ℒ|_{C_Z})`;
>
> it is bilinear, and for integer families `a` and `b`
>
> `⟨a, 𝒪_X(∑_Y b_Y C_Y)⟩ = ⟨b, 𝒪_X(∑_Z a_Z C_Z)⟩`.
>
> The four clauses are, in order: the defining formula for the pairing, additivity in the
> coefficient family, additivity in the invertible module — the Picard group being written
> multiplicatively, so that addition of its elements is the tensor product — and the symmetry.
> The third is the invertible case of [Stacks, Tag 0AYX] on each component, and the fourth is
> proved as the source proves it: expand both sides by the first three clauses and appeal to the
> symmetry of the intersection matrix
> `deg(𝒪_X(C_Y)|_{C_Z}) = deg(𝒪_X(C_Z)|_{C_Y})`, which is
> `Stacks.Models.RegularProperModelSituation.componentDegree_specialFiberComponent_comm`.

```lean
theorem specialFiberDegreePairing_bilinear_and_comm
    (s : Finset (irreducibleComponents S.specialFiber)) :
    (∀ (a : irreducibleComponents S.specialFiber → ℤ) (L : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L),
        S.specialFiberDegreePairing s a L hL =
          ∑ Z ∈ s, a Z * S.specialFiberComponentDegree Z L hL) ∧
      (∀ (a a' : irreducibleComponents S.specialFiber → ℤ) (L : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L),
        S.specialFiberDegreePairing s (a + a') L hL =
          S.specialFiberDegreePairing s a L hL + S.specialFiberDegreePairing s a' L hL) ∧
      (∀ (a : irreducibleComponents S.specialFiber → ℤ) (L M : S.X.Modules)
        (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L)
        (hM : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property M)
        (hLM : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property
            ((((Stacks.SheafOfModules.Tensor.sheafTensor
              ⟨(S.X.toRingedSpace).presheaf, (S.X.toRingedSpace).IsSheaf⟩).obj (L)).obj (M)))),
        S.specialFiberDegreePairing s a ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨(S.X.toRingedSpace).presheaf, (S.X.toRingedSpace).IsSheaf⟩).obj (L)).obj (M))) hLM =
          S.specialFiberDegreePairing s a L hL + S.specialFiberDegreePairing s a M hM) ∧
      (∀ a b : irreducibleComponents S.specialFiber → ℤ,
        S.specialFiberDegreePairing s a (S.specialFiberVerticalDivisorSheaf s b)
            (S.isInvertible_specialFiberVerticalDivisorSheaf s b) =
          S.specialFiberDegreePairing s b (S.specialFiberVerticalDivisorSheaf s a)
            (S.isInvertible_specialFiberVerticalDivisorSheaf s a))
```

**`Stacks.Models.intersectionProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean#L230). The attribute's comment: “the product, defined as ⟨a, O\_X(∑ bⱼCⱼ)⟩; its symmetry on the components of the special fibre is Stacks.Models.RegularProperModelSituation.specialFiberIntersectionProduct\_comm of StacksFrontier/AlgebraicGeometry/Curves/Models/DegreePairingSymmetry.lean”.

> **Stacks Project, Tag 0C65, the definition of the intersection product.** For an integer
> family `a` and a nonnegative family `b` on components `Cᵢ` that are effective Cartier divisors,
> `(∑ᵢ aᵢCᵢ · ∑ⱼ bⱼCⱼ)` is the degree pairing of `a` against `𝒪_X(∑ⱼ bⱼCⱼ)`.

```lean
def intersectionProduct (a : ι → ℤ) (b : ι → ℕ)
    (hC : ∀ i ∈ s, Stacks.Divisors.IsEffectiveCartierDivisor (C i)) : ℤ
```

**`Stacks.Models.intersectionProduct_eq_degreePairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionPairing.lean#L239). The attribute's comment: “the first displayed equality, which is the definition”.

> **Stacks Project, Tag 0C65, first equality.** The intersection product
> `(∑ᵢ aᵢCᵢ · ∑ⱼ bⱼCⱼ)` is the degree pairing `⟨a, 𝒪_X(∑ⱼ bⱼCⱼ)⟩`.

```lean
theorem intersectionProduct_eq_degreePairing (a : ι → ℤ) (b : ι → ℕ)
    (hC : ∀ i ∈ s, Stacks.Divisors.IsEffectiveCartierDivisor (C i)) :
    intersectionProduct S s C g hg hdim a b hC =
      degreePairing S s C g hg hdim a (Stacks.Divisors.invertibleSheaf' (∏ j ∈ s, C j ^ b j))
        (@Stacks.Divisors.isTensorInvertible_invertibleSheaf _ (∏ j ∈ s, C j ^ b j)
          (Stacks.Divisors.isEffectiveCartierDivisor_prod s C b hC))
```

## Tag 0C66, a lemma

[Tag 0C66](https://stacks.math.columbia.edu/tag/0C66) in the Stacks Project.

**`Stacks.Models.intersectionProduct_specialFiber_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionForm.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/IntersectionForm.lean#L338). The attribute's comment: “part (2), in the orientation (∑ aᵢCᵢ · ∑ mᵢCᵢ) = 0 of the symmetric form”.

> **The special fibre is orthogonal to every integral combination of the components**,
> `(Σ aᵢCᵢ · Σ mᵢCᵢ) = 0`, because the sheaf `𝒪_X(Σ mᵢCᵢ) = 𝒪_X(X_k)` is trivial and the structure
> sheaf has degree zero on each component.
>
> This is part (2) of [Stacks, Tag 0C66] at an abstract family of components and in the orientation
> that the triviality of `𝒪_X(X_k)` gives directly. The clause as the source states it,
> `(Σ mᵢCᵢ · Cⱼ) = 0` at the irreducible components of the special fibre, is
> `Stacks.Models.RegularProperModelSituation.specialFiberIntersectionProduct_multiplicity_eq_zero`
> of `StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean`, and follows
> from this statement by the symmetry of the form, [Stacks, Tag 0C64]. Both are registered.

```lean
theorem intersectionProduct_specialFiber_eq_zero (a : ι → ℤ) (m : ι → ℕ)
    (hC : ∀ j ∈ s, Stacks.Divisors.IsEffectiveCartierDivisor (C j))
    (hdec : S.specialFiberIdeal = ∏ j ∈ s, C j ^ m j) :
    intersectionProduct S s C g hg hdim a m hC = 0
```

**`Stacks.Models.RegularProperModelSituation.specialFiberIntersectionMatrix_nonneg_and_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean#L113). The attribute's comment: “part (1): (C\_Z · C\_Y) ≥ 0 for Z ≠ Y, with equality if and only if C\_Z ∩ C\_Y = ∅”.

> **Stacks Project, Tag 0C66, part (1).** For two distinct irreducible components `C_Z ≠ C_Y` of
> the special fibre of a regular proper model, `(C_Z · C_Y) ≥ 0`, and `(C_Z · C_Y) = 0` if and only
> if `C_Z ∩ C_Y = ∅`.
>
> The entry `(C_Z · C_Y)` is the degree of `𝒪_X(C_Y)` on `C_Z`. Since `C_Z ≠ C_Y` are distinct
> irreducible components, `C_Z ⊄ C_Y`, so the canonical section of `𝒪_X(C_Y)` restricts to a
> *nonzero* global section of `𝒪_X(C_Y)|_{C_Z}` on the integral proper curve `C_Z`, whose zero
> scheme is the scheme-theoretic intersection `C_Z ∩ C_Y`. Part (1) of [Stacks, Tag 0B40] then
> gives `(C_Z · C_Y) ≥ 0`, and part (2) of that tag gives `(C_Z · C_Y) > 0` exactly when the zero
> scheme is nonempty, that is exactly when `C_Z` meets `C_Y`.

```lean
theorem specialFiberIntersectionMatrix_nonneg_and_eq_zero_iff
    {Z Y : irreducibleComponents S.specialFiber} (h : Z ≠ Y) :
    0 ≤ S.specialFiberIntersectionMatrix Z Y ∧
      (S.specialFiberIntersectionMatrix Z Y = 0 ↔ (Z.1 : Set S.specialFiber) ∩ Y.1 = ∅)
```

**`Stacks.Models.RegularProperModelSituation.specialFiberIntersectionProduct_multiplicity_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean#L160). The attribute's comment: “part (2): (∑\_Z m\_Z C\_Z · C\_Y) = 0, the special fibre is orthogonal to each component”. References: SGA 7 X (1.8), “partial”.

> **Stacks Project, Tag 0C66, part (2).** The special fibre `X_k = ∑_Z m_Z C_Z` of a regular
> proper model is orthogonal to each of its irreducible components, `(∑_Z m_Z C_Z · C_Y) = 0`.
>
> This is the orientation in which the source states the clause. By the symmetry of the form,
> [Stacks, Tag 0C64], it equals `(C_Y · ∑_Z m_Z C_Z)`, which is the degree on `C_Y` of
> `𝒪_X(∑_Z m_Z C_Z) = 𝒪_X(X_k)`; and that invertible module is trivial, the special fibre being cut
> out by a uniformizer of the discrete valuation ring, so the degree vanishes.

```lean
theorem specialFiberIntersectionProduct_multiplicity_eq_zero
    (Y : irreducibleComponents S.specialFiber) :
    S.specialFiberIntersectionProduct (fun Z => (S.specialFiberMultiplicity Z : ℤ))
      (Pi.single Y 1) = 0
```

**`Stacks.Models.RegularProperModelSituation.not_forall_specialFiberIntersectionMatrix_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean#L187). The attribute's comment: “part (3): no nonempty proper set I of components has (C\_Z · C\_Y) = 0 for all Z in I and all Y not in I”.

> **Stacks Project, Tag 0C66, part (3).** There is no nonempty proper set `I` of irreducible
> components of the special fibre with `(C_Z · C_Y) = 0` for all `Z ∈ I` and all `Y ∉ I`.
>
> By part (1) such an `I` would make every component in `I` disjoint from every component not in
> `I`, so the special fibre would be the union of the two disjoint nonempty closed sets
> `⋃_{Z ∈ I} C_Z` and `⋃_{Y ∉ I} C_Y` — the components cover the special fibre, and there are
> finitely many of them, so both unions are closed. That contradicts the connectedness of the
> special fibre, [Stacks, Tag 0C62].

```lean
theorem not_forall_specialFiberIntersectionMatrix_eq_zero
    (I : Set (irreducibleComponents S.specialFiber)) (hne : I.Nonempty) (hI : I ≠ Set.univ) :
    ¬ ∀ Z ∈ I, ∀ Y ∉ I, S.specialFiberIntersectionMatrix Z Y = 0
```

**`Stacks.Models.RegularProperModelSituation.specialFiberIntersectionForm_nonpos_and_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SpecialFiberIntersectionForm.lean#L273). The attribute's comment: “part (4): (∑\_Z a\_Z C\_Z · ∑\_Z a\_Z C\_Z) ≤ 0 for rational a, with equality if and only if a\_Z = q m\_Z for a single rational q”. References: SGA 7 X (1.15), “partial”; SGA 7 X (1.8), “special case”.

> **Stacks Project, Tag 0C66, part (4).** For every family `a` of *rational* coefficients on the
> irreducible components of the special fibre of a regular proper model,
>
> `(∑_Z a_Z C_Z · ∑_Z a_Z C_Z) ≤ 0`,
>
> and equality holds if and only if there is a single `q ∈ ℚ` with `a_Z = q m_Z` for every `Z`.
>
> This is the source's own deduction from the other three parts through the linear algebra of
> [Stacks, Tag 0C5X]: the intersection matrix is symmetric by [Stacks, Tag 0C64], has nonnegative
> off-diagonal entries by part (1), kills the strictly positive multiplicity vector `m` by part (2)
> — each multiplicity is positive by [Stacks, Tag 0C5Z] — and is irreducible by part (3). A
> symmetric matrix with those three properties is negative semidefinite with nullspace exactly the
> line spanned by `m`.
>
> The form is written as the double sum `∑_Z ∑_Y a_Z a_Y (C_Z · C_Y)`, which is the bilinear
> extension to rational coefficients of the form of [Stacks, Tag 0C65]; the two agree wherever both
> are defined, by
> `Stacks.Models.RegularProperModelSituation.specialFiberIntersectionProduct_eq_sum_sum`.

```lean
theorem specialFiberIntersectionForm_nonpos_and_eq_zero_iff
    (a : irreducibleComponents S.specialFiber → ℚ) :
    ∑ Z, ∑ Y, a Z * a Y * (S.specialFiberIntersectionMatrix Z Y : ℚ) ≤ 0 ∧
      (∑ Z, ∑ Y, a Z * a Y * (S.specialFiberIntersectionMatrix Z Y : ℚ) = 0 ↔
        ∃ q : ℚ, ∀ Z, a Z = q * (S.specialFiberMultiplicity Z : ℚ))
```

## Tag 0C67, a lemma

[Tag 0C67](https://stacks.math.columbia.edu/tag/0C67) in the Stacks Project.

**`Stacks.Models.isEffectiveCartierDivisor_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean#L129). The attribute's comment: “D is an effective Cartier divisor, given a decomposition of X\_k”.

> **The reduced fibre of a decomposition into effective Cartier divisors is an effective
> Cartier divisor**, being a sum of nonnegative multiples of effective Cartier divisors.

```lean
theorem isEffectiveCartierDivisor_reducedSpecialFibre
    (hC : ∀ i ∈ s, IsEffectiveCartierDivisor (C i)) :
    IsEffectiveCartierDivisor (reducedSpecialFibre s C m)
```

**`Stacks.Models.zsmul_picardClass_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean#L163). The attribute's comment: “O\_X(D) has order dividing d in Pic(X), given a decomposition of X\_k”.

> **Stacks Project, Tag 0C67.** The invertible sheaf `𝒪_X(D)` of the reduced special fibre
> `D = Σ (mᵢ/d) Cᵢ` of a regular proper model has order dividing `d` in `Pic(X)`:
> `𝒪_X(D)^{⊗d} = 𝒪_X(dD) = 𝒪_X(X_k) = 𝒪_X`.

```lean
theorem zsmul_picardClass_reducedSpecialFibre
    (hdec : S.specialFiberIdeal = ∏ i ∈ s, C i ^ m i) :
    ((s.gcd m : ℕ) : ℤ) • picardClass (reducedSpecialFibre s C m) = 0
```

**`Stacks.Models.isInvertible_immersionConormalSheaf_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean#L175). The attribute's comment: “the conormal sheaf of D is an invertible O\_D-module”.

> **Stacks Project, Tag 0C67.** The conormal module `𝒞_{D/X}` of the reduced special fibre
> `D = Σ (mᵢ/d) Cᵢ` is an invertible `𝒪_D`-module: it is the restriction `ℐ_D|_D` of the ideal
> sheaf of an effective Cartier divisor.

```lean
theorem isInvertible_immersionConormalSheaf_reducedSpecialFibre :
    IsInvertible (reducedSpecialFibre s C m).subscheme.presheaf
      (structureIsSheaf (reducedSpecialFibre s C m).subscheme.toRingedSpace)
      (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre s C m).subschemeι)
```

**`Stacks.Models.zsmul_picardClass_immersionConormalSheaf_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean#L185). The attribute's comment: “the conormal class has order dividing d in Pic(D)”.

> **Stacks Project, Tag 0C67.** The conormal module `𝒞_{D/X}` of the reduced special fibre
> `D = Σ (mᵢ/d) Cᵢ` has order dividing `d` in `Pic(D)`: it is the pullback to `D` of
> `𝒪_X(-D) = -[𝒪_X(D)]`, and pullback is a homomorphism of Picard groups.

```lean
theorem zsmul_picardClass_immersionConormalSheaf_reducedSpecialFibre
    (hdec : S.specialFiberIdeal = ∏ i ∈ s, C i ^ m i) :
    ((s.gcd m : ℕ) : ℤ) • picardClass (reducedSpecialFibre s C m).subscheme.presheaf
        (structureIsSheaf (reducedSpecialFibre s C m).subscheme.toRingedSpace)
        (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre s C m).subschemeι)
        (isInvertible_immersionConormalSheaf (reducedSpecialFibre s C m)) = 0
```

**`Stacks.Models.reducedSpecialFibre_order_dvd_gcd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibre.lean#L204). The attribute's comment: “all four conclusions, given a decomposition of X\_k rather than a canonical one”.

> **Stacks Project, Tag 0C67.** All four conclusions at once: the reduced special fibre
> `D = Σ (mᵢ/d) Cᵢ` of a regular proper model is an effective Cartier divisor, `𝒪_X(D)` has order
> dividing `d = gcd(mᵢ)` in `Pic(X)`, and `𝒞_{D/X}` is an invertible `𝒪_D`-module of order
> dividing `d` in `Pic(D)`.

```lean
theorem reducedSpecialFibre_order_dvd_gcd
    (hC : ∀ i ∈ s, IsEffectiveCartierDivisor (C i))
    (hdec : S.specialFiberIdeal = ∏ i ∈ s, C i ^ m i) :
    IsEffectiveCartierDivisor (reducedSpecialFibre s C m) ∧
      ((s.gcd m : ℕ) : ℤ) • picardClass (reducedSpecialFibre s C m) = 0 ∧
      IsInvertible (reducedSpecialFibre s C m).subscheme.presheaf
        (structureIsSheaf (reducedSpecialFibre s C m).subscheme.toRingedSpace)
        (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre s C m).subschemeι) ∧
      ((s.gcd m : ℕ) : ℤ) • picardClass (reducedSpecialFibre s C m).subscheme.presheaf
        (structureIsSheaf (reducedSpecialFibre s C m).subscheme.toRingedSpace)
        (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre s C m).subschemeι)
        (isInvertible_immersionConormalSheaf (reducedSpecialFibre s C m)) = 0
```

**`Stacks.Models.isEffectiveCartierDivisor_reducedSpecialFibre_specialFiberComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean#L90). The attribute's comment: “D is an effective Cartier divisor, at the canonical decomposition of X\_k into its irreducible components”.

> **Stacks Project, Tag 0C67, at the canonical decomposition.** The reduced special fibre
> `D = Σ (mᵢ/d) Cᵢ` of the decomposition of `X_k` into its irreducible components is an effective
> Cartier divisor on the model: the components are effective Cartier divisors by part (2) of
> [Stacks, Tag 0C5Z], and a nonnegative combination of effective Cartier divisors is one.

```lean
theorem isEffectiveCartierDivisor_reducedSpecialFibre_specialFiberComponents :
    IsEffectiveCartierDivisor (reducedSpecialFibre Finset.univ
      S.specialFiberComponentIdeal S.specialFiberMultiplicity)
```

**`Stacks.Models.reducedSpecialFibre_order_dvd_gcd_specialFiberComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean#L110). The attribute's comment: “all four conclusions at the canonical decomposition of X\_k into its irreducible components, whose two inputs are parts (2) and (3) of 0C5Z: C\_i the components with their reduced induced structure, m\_i the multiplicity of C\_i in X\_k, d = gcd(m\_i) and D = sum (m\_i/d)C\_i”.

> **Stacks Project, Tag 0C67, at the canonical decomposition into irreducible components.**
> Let `C₁, …, Cₙ` be the irreducible components of the special fibre `X_k` of a regular proper
> model, with their reduced induced structure, let `mᵢ` be the multiplicity of `Cᵢ` in `X_k`, put
> `d = gcd(m₁, …, mₙ)` and let `D = Σ (mᵢ/d) Cᵢ`. Then `D` is an effective Cartier divisor,
> `𝒪_X(D)` has order dividing `d` in `Pic(X)`, and the conormal module `𝒞_{D/X}` is an invertible
> `𝒪_D`-module of order dividing `d` in `Pic(D)`.
>
> This is `Stacks.Models.reducedSpecialFibre_order_dvd_gcd` with both of its hypotheses supplied
> from [Stacks, Tag 0C5Z]: effectivity of the components is part (2) and `X_k = Σ mᵢ Cᵢ` is
> part (3).

```lean
theorem reducedSpecialFibre_order_dvd_gcd_specialFiberComponents :
    IsEffectiveCartierDivisor (reducedSpecialFibre Finset.univ
        S.specialFiberComponentIdeal S.specialFiberMultiplicity) ∧
      ((Finset.univ.gcd S.specialFiberMultiplicity : ℕ) : ℤ) •
          picardClass (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
            S.specialFiberMultiplicity) = 0 ∧
      IsInvertible (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
          S.specialFiberMultiplicity).subscheme.presheaf
        (structureIsSheaf (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
          S.specialFiberMultiplicity).subscheme.toRingedSpace)
        (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre Finset.univ
          S.specialFiberComponentIdeal S.specialFiberMultiplicity).subschemeι) ∧
      ((Finset.univ.gcd S.specialFiberMultiplicity : ℕ) : ℤ) •
          picardClass (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
              S.specialFiberMultiplicity).subscheme.presheaf
            (structureIsSheaf (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
              S.specialFiberMultiplicity).subscheme.toRingedSpace)
            (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre Finset.univ
              S.specialFiberComponentIdeal S.specialFiberMultiplicity).subschemeι)
            (isInvertible_immersionConormalSheaf (reducedSpecialFibre Finset.univ
              S.specialFiberComponentIdeal S.specialFiberMultiplicity)) = 0
```

**`Stacks.Models.addOrderOf_picardClass_reducedSpecialFibre_specialFiberComponents_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean#L141). The attribute's comment: “O\_X(D) has order dividing d in Pic(X), at the canonical decomposition of X\_k into its irreducible components”.

> **Stacks Project, Tag 0C67, at the canonical decomposition**, as a statement about additive
> orders: the class of `𝒪_X(D)` in `Pic(X)` has order dividing `d = gcd(mᵢ)`, for `D` the reduced
> special fibre of the decomposition of `X_k` into its irreducible components.

```lean
theorem addOrderOf_picardClass_reducedSpecialFibre_specialFiberComponents_dvd :
    addOrderOf (picardClass (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
      S.specialFiberMultiplicity)) ∣ Finset.univ.gcd S.specialFiberMultiplicity
```

**`Stacks.Models.addOrderOf_picardClass_immersionConormalSheaf_specialFiberComponents_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedSpecialFibreComponents.lean#L153). The attribute's comment: “the conormal class of D has order dividing d in Pic(D), at the canonical decomposition of X\_k into its irreducible components”.

> **Stacks Project, Tag 0C67, at the canonical decomposition**, as a statement about additive
> orders: the class of the conormal module `𝒞_{D/X}` in `Pic(D)` has order dividing
> `d = gcd(mᵢ)`, for `D` the reduced special fibre of the decomposition of `X_k` into its
> irreducible components.

```lean
theorem addOrderOf_picardClass_immersionConormalSheaf_specialFiberComponents_dvd :
    addOrderOf (picardClass (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
        S.specialFiberMultiplicity).subscheme.presheaf
      (structureIsSheaf (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
        S.specialFiberMultiplicity).subscheme.toRingedSpace)
      (Stacks.Thickenings.immersionConormalSheaf (reducedSpecialFibre Finset.univ
        S.specialFiberComponentIdeal S.specialFiberMultiplicity).subschemeι)
      (isInvertible_immersionConormalSheaf (reducedSpecialFibre Finset.univ
        S.specialFiberComponentIdeal S.specialFiberMultiplicity))) ∣
      Finset.univ.gcd S.specialFiberMultiplicity
```

## Tag 0C68, a lemma

[Tag 0C68](https://stacks.math.columbia.edu/tag/0C68) in the Stacks Project.

**`Stacks.Models.exists_chain_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedFibreFiltration.lean, line 1204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedFibreFiltration.lean#L1204). The attribute's comment: “the whole lemma: the increasing chain of effective Cartier divisors from the reduced special fibre (X\_k)\_red to the divisor D = sum (mᵢ/d)Cᵢ, d = gcd(mᵢ), each step adding a single component, with H⁰(Z\_j, O\_\{Z\_j}) a field finite over the residue field at every stage. Stated at a decomposition X\_k = sum mᵢCᵢ of the special fibre into integral proper curves over the residue field, which is the opening phrase of Situation 0C61”.

> **Stacks Project, Tag 0C68** [Artin–Winters, Lemma 2.6].  In Situation
> [Stacks, Tag 0C61], write the special fibre as a sum of effective Cartier divisors
> `X_k = Σ mᵢCᵢ`, put `d = gcd(mᵢ)` and let `D = Σ (mᵢ/d)Cᵢ`.  Then there is a sequence of
> effective Cartier divisors `(X_k)_red = Z₀ ⊆ Z₁ ⊆ … ⊆ Z_M = D` in which each step
> `Z_{j+1} = Z_j + C_{i_j}` adds a single component, and such that `H⁰(Z_j, 𝒪_{Z_j})` is a field,
> finite over the residue field `k` for the algebra structure induced by the base ring, for every
> `j = 0, …, M`.
>
> Every input of the source's induction is proved here.  Connectedness of the reduced special
> fibre is [Stacks, Tag 0C62],
> `Stacks.Models.RegularProperModelSituation.connectedSpace_subscheme_radical_specialFiberIdeal`;
> finiteness of the global functions of a proper scheme over `k` is clause (1) of
> [Stacks, Tag 0BUG],
> `Stacks.AlgebraicGeometry.ProperSectionsGeom.moduleFinite_globalSections_of_isProper`; finite
> dimensionality of coherent cohomology over a field is [Stacks, Tag 02O6],
> `AlgebraicGeometry.forall_finiteDimensional_cohomologyOverField_unit`; and the geometric step is
> `Stacks.Models.exists_componentDegree_negativeTwist_neg`, which runs the four properties of
> [Stacks, Tag 0C66] at the given decomposition.  [Stacks, Tag 0C4T] and part (1) of
> [Stacks, Tag 0B40] enter through
> `Stacks.Models.injective_inclusion_appTop_of_forall_eq_zero`.  See the implementation notes of
> this file.

```lean
theorem exists_chain_reducedSpecialFibre
    (hC : ∀ i ∈ s, IsEffectiveCartierDivisor (C i))
    (hm : ∀ i ∈ s, 0 < m i)
    (hdec : S.specialFiberIdeal = ∏ i ∈ s, C i ^ m i)
    (hred : S.specialFiberIdeal.radical = ∏ i ∈ s, C i)
    (g : ∀ i, (C i).subscheme ⟶ Spec (.of S.k)) (_hgproper : ∀ i, IsProper (g i))
    (hdim : ∀ i, topologicalKrullDim (C i).subscheme ≤ 1)
    (hint : ∀ i, AlgebraicGeometry.IsIntegral (C i).subscheme) :
    ∃ (M : ℕ) (Z : ℕ → S.X.IdealSheafData),
      Z 0 = S.specialFiberIdeal.radical ∧ Z M = reducedSpecialFibre s C m ∧
      (∀ j < M, ∃ i ∈ s, Z (j + 1) = Z j * C i ∧ Z (j + 1) ≤ Z j) ∧
      ∀ j ≤ M, IsEffectiveCartierDivisor (Z j) ∧ IsField Γ((Z j).subscheme, ⊤) ∧
        ∃ φ : S.k →+* Γ((Z j).subscheme, ⊤),
          φ.comp (algebraMap S.R S.k) = fibreSubschemeBaseMap S (Z j) ∧ φ.Finite
```

## Tag 0C69, a lemma

[Tag 0C69](https://stacks.math.columbia.edu/tag/0C69) in the Stacks Project.

**`Stacks.Models.one_sub_genus_eq_gcd_mul_finrank_mul_one_sub_genus_reducedSpecialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaDecomposition.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaDecomposition.lean#L559). The attribute's comment: “the formula 1 - g\_C = d [kappa:k\](1 - g\_D) at a decomposition X\_k = sum m\_i C\_i of the special fibre into integral proper curves over the residue field whose product is the reduced special fibre, of which the irreducible components of Situation 0C61 are the case: d = gcd(m\_i), D = sum (m\_i/d)C\_i, kappa = H^0(D, O\_D), and g\_D the genus of D over kappa. That kappa is a field finite over the residue field is part of the conclusion”.

> **The formula of [Stacks, Tag 0C69]** [Artin-Winters, Lemma 2.6].  In Situation
> [Stacks, Tag 0C61], written at a decomposition `X_k = Σ mᵢCᵢ` of the special fibre into integral
> proper curves over the residue field, with `d = gcd(mᵢ)`, `D = Σ (mᵢ/d)Cᵢ` the reduced special
> fibre and `κ = H⁰(D, 𝒪_D)`:
>
> `1 - g_C = d · [κ : k] · (1 - g_D)`,
>
> where `g_C` is the genus of `C` over `K` and `g_D` the genus of `D` over `κ`.  That `κ` is a
> field, finite over `k`, is part of the conclusion rather than a hypothesis: it is the top stage
> of the chain of [Stacks, Tag 0C68].
>
> The binder list is exactly that of `Stacks.Models.exists_chain_reducedSpecialFibre`, whose
> conclusion at its top stage is what makes `κ` a field finite over `k`.  The source's proof is
> the composite of four identities, each of them a theorem here:
> `1 - g_C = χ(C, 𝒪_C)` is `Stacks.Models.one_sub_genus_curve_eq_eulerCharacteristic`;
> `χ(C, 𝒪_C) = χ(X_k, 𝒪_{X_k})` is
> `RegularProperModelSituation.eulerCharacteristic_unit_eq_eulerCharacteristic_unit_specialFibre`;
> `χ(X_k, 𝒪_{X_k}) = d·χ(D, 𝒪_D)` is `Stacks.Models.fibreEuler_specialFiberIdeal_eq`; and
> `χ(D, 𝒪_D) = [κ : k](1 - g_D)` is `Stacks.Models.fibreEuler_reducedSpecialFibre_eq`.

```lean
theorem one_sub_genus_eq_gcd_mul_finrank_mul_one_sub_genus_reducedSpecialFibre
    (hC : ∀ i ∈ s, IsEffectiveCartierDivisor (C i))
    (hm : ∀ i ∈ s, 0 < m i)
    (hdec : S.specialFiberIdeal = ∏ i ∈ s, C i ^ m i)
    (hred : S.specialFiberIdeal.radical = ∏ i ∈ s, C i)
    (g : ∀ i, (C i).subscheme ⟶ Spec (.of S.k)) (hgproper : ∀ i, IsProper (g i))
    (hdimC : ∀ i, topologicalKrullDim (C i).subscheme ≤ 1)
    (hint : ∀ i, AlgebraicGeometry.IsIntegral (C i).subscheme) :
    ∃ hκ : IsField Γ((reducedSpecialFibre s C m).subscheme, ⊤),
      letI : Algebra S.k Γ((reducedSpecialFibre s C m).subscheme, ⊤) :=
        ((Scheme.ΓSpecIso (.of S.k)).inv ≫ (S.fibreSubschemeToSpec
          (reducedSpecialFibre s C m)
          (specialFiberIdeal_le_reducedSpecialFibre S s C m hdec)).appTop).hom.toAlgebra
      letI : Field Γ((reducedSpecialFibre s C m).subscheme, ⊤) := hκ.toField
      Module.Finite S.k Γ((reducedSpecialFibre s C m).subscheme, ⊤) ∧
        (1 : ℤ) - (AlgebraicGeometry.genus S.C_to_K : ℤ) =
          ((s.gcd m : ℕ) : ℤ) *
            (Module.finrank S.k Γ((reducedSpecialFibre s C m).subscheme, ⊤) : ℤ) *
            (1 - (AlgebraicGeometry.genus
              (reducedSpecialFibre s C m).subscheme.toSpecΓ : ℤ))
```

**`Stacks.Models.one_sub_genus_eq_gcd_mul_finrank_mul_one_sub_genus_specialFiberComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaDecomposition.lean, line 613](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaDecomposition.lean#L613). The attribute's comment: “the formula 1 - g\_C = d [kappa:k\](1 - g\_D) at the irreducible components of the special fibre, which is the setting of Situation 0C61: d = gcd(m\_i) for m\_i the multiplicity of C\_i in X\_k, D = sum (m\_i/d)C\_i the reduced special fibre, kappa = H^0(D, O\_D), and g\_D the genus of D over kappa. That kappa is a field finite over the residue field is part of the conclusion”.

> **Stacks Project, Tag 0C69** [Artin-Winters, Lemma 2.6], at the irreducible components of
> the special fibre, which is the setting of Situation [Stacks, Tag 0C61].  With `C₁, …, Cₙ` the
> irreducible components of `X_k`, `mᵢ` their multiplicities, `d = gcd(mᵢ)`, `D = Σ (mᵢ/d)Cᵢ` and
> `κ = H⁰(D, 𝒪_D)`:
>
> `1 - g_C = d · [κ : k] · (1 - g_D)`.
>
> Every binder of the general statement is discharged at the canonical family: the components are
> integral effective Cartier divisors, proper of dimension at most one over the residue field with
> positive multiplicities, `X_k = Σ mᵢCᵢ` is part (3) of [Stacks, Tag 0C5Z], and the reduction
> `(X_k)_red = Σ Cᵢ` is
> `Stacks.Models.RegularModelSituation.radical_specialFiberIdeal_eq_prod`.

```lean
theorem one_sub_genus_eq_gcd_mul_finrank_mul_one_sub_genus_specialFiberComponents :
    ∃ hκ : IsField Γ((reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
        S.specialFiberMultiplicity).subscheme, ⊤),
      letI : Algebra S.k Γ((reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
          S.specialFiberMultiplicity).subscheme, ⊤) :=
        ((Scheme.ΓSpecIso (.of S.k)).inv ≫ (S.fibreSubschemeToSpec
          (reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
            S.specialFiberMultiplicity)
          (specialFiberIdeal_le_reducedSpecialFibre S Finset.univ
            S.specialFiberComponentIdeal S.specialFiberMultiplicity
            S.specialFiberIdeal_eq_prod)).appTop).hom.toAlgebra
      letI : Field Γ((reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
        S.specialFiberMultiplicity).subscheme, ⊤) := hκ.toField
      Module.Finite S.k Γ((reducedSpecialFibre Finset.univ S.specialFiberComponentIdeal
        S.specialFiberMultiplicity).subscheme, ⊤) ∧
        (1 : ℤ) - (AlgebraicGeometry.genus S.C_to_K : ℤ) =
          ((Finset.univ.gcd S.specialFiberMultiplicity : ℕ) : ℤ) *
            (Module.finrank S.k Γ((reducedSpecialFibre Finset.univ
              S.specialFiberComponentIdeal S.specialFiberMultiplicity).subscheme, ⊤) : ℤ) *
            (1 - (AlgebraicGeometry.genus (reducedSpecialFibre Finset.univ
              S.specialFiberComponentIdeal S.specialFiberMultiplicity).subscheme.toSpecΓ : ℤ))
```

## Tag 0C6A, a lemma

[Tag 0C6A](https://stacks.math.columbia.edu/tag/0C6A) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.specialFiberMultiplicity_eq_one_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean, line 1058](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean#L1058). The attribute's comment: “m\_1 = m\_2 = 1, every component of the special fibre has multiplicity one”.

> **Stacks Project, Tag 0C6A: `m₁ = m₂ = 1`.** Every irreducible component of the special
> fibre occurs in `X_k` with multiplicity one.

```lean
theorem specialFiberMultiplicity_eq_one_of_isExceptionalCurveOfFirstKind
    {i j : irreducibleComponents S.specialFiber} (hij : i ≠ j)
    {κi κj : Type u} [Field κi] [Field κj]
    {ei : projectiveLineProj κi ≅ (S.specialFiberComponentIdeal i).subscheme}
    {ej : projectiveLineProj κj ≅ (S.specialFiberComponentIdeal j).subscheme}
    (hi : (S.specialFiberComponentIdeal i).IsExceptionalCurveOfFirstKind κi ei)
    (hj : (S.specialFiberComponentIdeal j).IsExceptionalCurveOfFirstKind κj ej)
    (hmeet : Nonempty
      (S.specialFiberComponentIdeal i ⊔ S.specialFiberComponentIdeal j).subscheme) :
    ∀ Z : irreducibleComponents S.specialFiber, S.specialFiberMultiplicity Z = 1
```

**`Stacks.Models.RegularProperModelSituation.genus_eq_zero_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean#L1081). The attribute's comment: “C has genus 0, the generic fibre of the model has genus zero”.

> **Stacks Project, Tag 0C6A: the generic curve has genus zero.**

```lean
theorem genus_eq_zero_of_isExceptionalCurveOfFirstKind
    {i j : irreducibleComponents S.specialFiber} (hij : i ≠ j)
    {κi κj : Type u} [Field κi] [Field κj]
    {ei : projectiveLineProj κi ≅ (S.specialFiberComponentIdeal i).subscheme}
    {ej : projectiveLineProj κj ≅ (S.specialFiberComponentIdeal j).subscheme}
    (hi : (S.specialFiberComponentIdeal i).IsExceptionalCurveOfFirstKind κi ei)
    (hj : (S.specialFiberComponentIdeal j).IsExceptionalCurveOfFirstKind κj ej)
    (hmeet : Nonempty
      (S.specialFiberComponentIdeal i ⊔ S.specialFiberComponentIdeal j).subscheme) :
    genus S.C_to_K = 0
```

**`Stacks.Models.RegularProperModelSituation.exists_section_fibreSubschemeToSpec_sup_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean, line 1099](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean#L1099). The attribute's comment: “C\_1 and C\_2 meet in a k-rational point”.

> **Stacks Project, Tag 0C6A: the two components meet in a `k`-rational point.** The
> scheme-theoretic intersection `C_i ∩ C_j`, as a closed subscheme of the model, carries a
> structure morphism over the residue field compatible with the model morphism, and that morphism
> is an isomorphism — so the intersection is a single rational point of `k`.

```lean
theorem exists_section_fibreSubschemeToSpec_sup_of_isExceptionalCurveOfFirstKind
    {i j : irreducibleComponents S.specialFiber} (hij : i ≠ j)
    {κi κj : Type u} [Field κi] [Field κj]
    {ei : projectiveLineProj κi ≅ (S.specialFiberComponentIdeal i).subscheme}
    {ej : projectiveLineProj κj ≅ (S.specialFiberComponentIdeal j).subscheme}
    (hi : (S.specialFiberComponentIdeal i).IsExceptionalCurveOfFirstKind κi ei)
    (hj : (S.specialFiberComponentIdeal j).IsExceptionalCurveOfFirstKind κj ej)
    (hmeet : Nonempty
      (S.specialFiberComponentIdeal i ⊔ S.specialFiberComponentIdeal j).subscheme) :
    ∃ f : (S.specialFiberComponentIdeal i ⊔
        S.specialFiberComponentIdeal j).subscheme ⟶ Spec (.of S.k),
      (f ≫ Spec.map (CommRingCat.ofHom (algebraMap S.R S.k)) =
        (S.specialFiberComponentIdeal i ⊔
          S.specialFiberComponentIdeal j).subschemeι ≫ S.X_to_R) ∧
      ∃ e : Spec (.of S.k) ≅ (S.specialFiberComponentIdeal i ⊔
        S.specialFiberComponentIdeal j).subscheme, e.hom ≫ f = 𝟙 (Spec (.of S.k))
```

**`Stacks.Models.RegularProperModelSituation.exists_iso_projectiveLineProj_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean, line 1138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean#L1138). The attribute's comment: “C\_1 and C\_2 are isomorphic to the projective line over the residue field”.

> **Stacks Project, Tag 0C6A: `C₁ ≅ 𝐏¹_k` and `C₂ ≅ 𝐏¹_k`.** Each irreducible component of
> the special fibre is the projective line over the residue field, compatibly with the structure
> morphism of the model: the component carries a morphism to `Spec k` lying over `Spec R`, and an
> isomorphism with `𝐏¹_k` carrying that morphism to the structure morphism of `𝐏¹_k`.
>
> The projective line is the graded model `Proj k[T₀, T₁]`.

```lean
theorem exists_iso_projectiveLineProj_of_isExceptionalCurveOfFirstKind
    {i j : irreducibleComponents S.specialFiber} (hij : i ≠ j)
    {κi κj : Type u} [Field κi] [Field κj]
    {ei : projectiveLineProj κi ≅ (S.specialFiberComponentIdeal i).subscheme}
    {ej : projectiveLineProj κj ≅ (S.specialFiberComponentIdeal j).subscheme}
    (hi : (S.specialFiberComponentIdeal i).IsExceptionalCurveOfFirstKind κi ei)
    (hj : (S.specialFiberComponentIdeal j).IsExceptionalCurveOfFirstKind κj ej)
    (hmeet : Nonempty
      (S.specialFiberComponentIdeal i ⊔ S.specialFiberComponentIdeal j).subscheme) :
    ∀ Z : irreducibleComponents S.specialFiber,
      ∃ f : (S.specialFiberComponentIdeal Z).subscheme ⟶ Spec (.of S.k),
        (f ≫ Spec.map (CommRingCat.ofHom (algebraMap S.R S.k)) =
          (S.specialFiberComponentIdeal Z).subschemeι ≫ S.X_to_R) ∧
        ∃ e : projectiveLineProj S.k ≅ (S.specialFiberComponentIdeal Z).subscheme,
          e.hom ≫ f = projToSpecCoeff S.k 1
```

**`Stacks.Models.RegularProperModelSituation.nonempty_fin_two_equiv_irreducibleComponents_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean, line 1176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ExceptionalComponentsMeet.lean#L1176). The attribute's comment: “n = 2, the special fibre has exactly two irreducible components”.

> **Stacks Project, Tag 0C6A: `n = 2`.** In Situation [Stacks, Tag 0C61], if two distinct
> irreducible components `C_i` and `C_j` of the special fibre are exceptional curves of the first
> kind and meet, then the special fibre has exactly two irreducible components.
>
> The components are indexed by `irreducibleComponents S.specialFiber` itself, so the assertion
> `n = 2` is an equivalence of that index type with `Fin 2`; no ordering of the components is
> chosen.

```lean
theorem nonempty_fin_two_equiv_irreducibleComponents_of_isExceptionalCurveOfFirstKind
    {i j : irreducibleComponents S.specialFiber} (hij : i ≠ j)
    {κi κj : Type u} [Field κi] [Field κj]
    {ei : projectiveLineProj κi ≅ (S.specialFiberComponentIdeal i).subscheme}
    {ej : projectiveLineProj κj ≅ (S.specialFiberComponentIdeal j).subscheme}
    (hi : (S.specialFiberComponentIdeal i).IsExceptionalCurveOfFirstKind κi ei)
    (hj : (S.specialFiberComponentIdeal j).IsExceptionalCurveOfFirstKind κj ej)
    (hmeet : Nonempty
      (S.specialFiberComponentIdeal i ⊔ S.specialFiberComponentIdeal j).subscheme) :
    Nonempty (Fin 2 ≃ irreducibleComponents S.specialFiber)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.9, Tag 0C5Y](https://stacks.math.columbia.edu/tag/0C5Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
