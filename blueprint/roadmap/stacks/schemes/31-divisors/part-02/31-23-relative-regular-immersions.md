---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.isQuasiRegularImmersion_baseChange_of_flat, Stacks.AlgebraicGeometry.isH1RegularImmersion_baseChange_of_flat, AlgebraicGeometry.IsRelativeH1RegularImmersion, Stacks.AlgebraicGeometry.IsRelativeQuasiRegularImmersion, AlgebraicGeometry.isFlatAt_of_isRelativeQuasiRegularImmersion, Stacks.AlgebraicGeometry.isRegularImmersion_baseChange_of_isRelativeQuasiRegularImmersion, Stacks.AlgebraicGeometry.isRegularImmersion_of_isRelativeQuasiRegularImmersion, AlgebraicGeometry.isRegular_atPrime_baseChange_of_isQuasiRegular
statement: formalized
proof: formalized
---

# 31.23 Relative regular immersions

Section 31.23 of the Stacks Project, [Tag 063P](https://stacks.math.columbia.edu/tag/063P). 12 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 063R, a lemma

[Tag 063R](https://stacks.math.columbia.edu/tag/063R) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isQuasiRegularImmersion_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/BaseChange.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/BaseChange.lean#L369). The attribute's comment: “quasi\_base\_change”.

> **Stacks Project, Tag 063R, the quasi-regular half.**  A quasi-regular immersion whose source
> is flat over the base remains quasi-regular after any base change of the base scheme.
>
> The `H₁`-regular half of the tag is
> `Stacks.AlgebraicGeometry.isH1RegularImmersion_baseChange_of_flat`, in
> `StacksFrontier.AlgebraicGeometry.RegularImmersion.H1BaseChange`.

```lean
theorem isQuasiRegularImmersion_baseChange_of_flat {S X Z S' : Scheme.{u}} (f : X ⟶ S)
    (i : Z ⟶ X) [IsImmersion i] [Flat (i ≫ f)] (hi : IsQuasiRegularImmersion i) (g : S' ⟶ S) :
    IsQuasiRegularImmersion (pullback.fst (pullback.snd g f) i)
```

**`Stacks.AlgebraicGeometry.isH1RegularImmersion_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/H1BaseChange.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/H1BaseChange.lean#L185). The attribute's comment: “h1\_base\_change”.

> **Stacks Project, Tag 063R, the `H₁`-regular half.**  An `H₁`-regular immersion whose source
> is flat over the base remains `H₁`-regular after any base change of the base scheme.

```lean
theorem isH1RegularImmersion_baseChange_of_flat {S X Z S' : Scheme.{u}} (f : X ⟶ S)
    (i : Z ⟶ X) [IsImmersion i] [Flat (i ≫ f)] (hi : IsH1RegularImmersion i) (g : S' ⟶ S) :
    IsH1RegularImmersion (pullback.fst (pullback.snd g f) i)
```

## Tag 063S, a definition

[Tag 063S](https://stacks.math.columbia.edu/tag/063S) in the Stacks Project.

**`AlgebraicGeometry.IsRelativeH1RegularImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeDefs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeDefs.lean#L49). The attribute's comment: “part (2): relative H₁-regular immersion”.

> **Part (2) of Stacks tag 063S.**  An immersion into a scheme over a base is a *relative
> `H₁`-regular immersion* when the immersed scheme is flat over the base and the immersion is
> `H₁`-regular.

```lean
abbrev IsRelativeH1RegularImmersion {Z X S : Scheme.{u}}
    (f : X ⟶ S) (i : Z ⟶ X) [IsImmersion i] : Prop
```

**`Stacks.AlgebraicGeometry.IsRelativeQuasiRegularImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/Basic.lean#L84). The attribute's comment: “part (1): relative quasi-regular immersion”.

> **Part (1) of Stacks tag 063S.** An immersion into a scheme over a base is a *relative
> quasi-regular immersion* when the immersed scheme is flat over the base and the immersion is
> quasi-regular.

```lean
abbrev IsRelativeQuasiRegularImmersion {Z X S : Scheme.{u}} (f : X ⟶ S) (i : Z ⟶ X)
    [IsImmersion i] : Prop
```

## Tag 063T, a lemma

[Tag 063T](https://stacks.math.columbia.edu/tag/063T) in the Stacks Project.

**`AlgebraicGeometry.isFlatAt_of_isRelativeQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeFlatness.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeFlatness.lean#L375).

> Let `f : X ⟶ S` be a morphism of schemes and `i : Z ⟶ X` a relative quasi-regular immersion
> over `S`.  Then `f` is flat at every point of the image of `i` whose local ring on `X` is
> Noetherian.

```lean
theorem isFlatAt_of_isRelativeQuasiRegularImmersion
    {X S Z : Scheme.{u}} (f : X ⟶ S) (i : Z ⟶ X) [IsImmersion i]
    (hi : IsRelativeQuasiRegularImmersion f i)
    (x : X) (hx : x ∈ Set.range i.base)
    (hNoetherian : IsNoetherianRing (X.presheaf.stalk x)) :
    IsFlatAt f.toLRSHom.toShHom x
```

## Tag 063U, a lemma

[Tag 063U](https://stacks.math.columbia.edu/tag/063U) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_baseChange_of_isRelativeQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/BaseChange.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/BaseChange.lean#L385). The attribute's comment: “regularity after arbitrary base change”. References: EGA IV (19.2.4), “c') => b')”.

> **Stacks Project, Tag 063U, regularity after an arbitrary base change.**  A relative
> quasi-regular immersion into a scheme flat and locally of finite presentation over the base
> remains a regular immersion after any change of the base.
>
> The base change is again a relative quasi-regular immersion over `S'`:  its quasi-regularity is
> the quasi-regular half of Stacks tag 063R and the flatness of its source over `S'` is
> `flat_comp_of_isPullback`.  Flatness and local finite presentation of `S' ×_S X ⟶ S'` are base
> changes of those of `X ⟶ S`.  So the already-proved
> `isRegularImmersion_of_isRelativeQuasiRegularImmersion` applies over `S'`.

```lean
theorem isRegularImmersion_baseChange_of_isRelativeQuasiRegularImmersion {S X Z S' : Scheme.{u}}
    (f : X ⟶ S) (i : Z ⟶ X) [IsImmersion i] [Flat f] [LocallyOfFinitePresentation f]
    (hi : IsRelativeQuasiRegularImmersion f i) (g : S' ⟶ S) :
    IsRegularImmersion (pullback.fst (pullback.snd g f) i)
```

**`Stacks.AlgebraicGeometry.isRegularImmersion_of_isRelativeQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/Relative.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/Relative.lean#L216). The attribute's comment: “regularity of the immersion”. References: EGA IV (19.2.4), “c') => c)”.

> A relative quasi-regular immersion into a scheme flat and locally of finite presentation over
> the base is a regular immersion.

```lean
theorem isRegularImmersion_of_isRelativeQuasiRegularImmersion {S X Z : Scheme.{u}} (f : X ⟶ S)
    (i : Z ⟶ X) [IsImmersion i] [Flat f] [LocallyOfFinitePresentation f]
    (hi : IsRelativeQuasiRegularImmersion f i) : IsRegularImmersion i
```

## Tag 0FUD, a remark

[Tag 0FUD](https://stacks.math.columbia.edu/tag/0FUD) in the Stacks Project.

**`AlgebraicGeometry.isRegular_atPrime_baseChange_of_isQuasiRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/QuasiRegularBaseChange.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/QuasiRegularBaseChange.lean#L91). The attribute's comment: “regularity at primes after base change”.

> Let `A → B` be flat and of finite presentation and let `f₁, …, f_r ∈ B` be a quasi-regular
> sequence whose quotient is flat over `A`.  For any `A`-algebra `A'` and any prime `q` of
> `B' = B ⊗_A A'` containing the base-changed sequence, that sequence is regular in the local ring
> `B'_q`.

```lean
theorem isRegular_atPrime_baseChange_of_isQuasiRegular
    {A B A' : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [CommRing A'] [Algebra A A'] [Module.Flat A B]
    [Algebra.FinitePresentation A B] {r : ℕ} (f : Fin r → B)
    (hflat : Module.Flat A (B ⧸ Ideal.span (Set.range f)))
    (hf : IsQuasiRegular B (List.ofFn f))
    (q : Ideal (B ⊗[A] A')) [q.IsPrime]
    (hq : Ideal.span (Set.range (KoszulH1.fp (A := A) (A' := A') f)) ≤ q) :
    IsRegular (Localization.AtPrime q)
      ((List.ofFn (KoszulH1.fp (A := A) (A' := A') f)).map
        (algebraMap (B ⊗[A] A') (Localization.AtPrime q)))
```

Declarations registered for the tag:

- [`Koszul.quasiRegular_and_h1Regular_baseChange_of_quotient_flat`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/FlatQuotient.lean#L640), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/QuasiRegularBaseChange.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/QuasiRegularBaseChange.lean#L38) (StacksFrontier): “quasi-regularity and constant length after base change”.

## Tag 063V, a lemma

[Tag 063V](https://stacks.math.columbia.edu/tag/063V) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_open_flat_of_isRelativeH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhood.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhood.lean#L505). The attribute's comment: “part (1): flat open neighbourhood of a relative H₁-regular immersion”.

> Let `f : X ⟶ S` be locally of finite presentation and let `i : Z ⟶ X` be a relative
> `H₁`-regular immersion over `S`.  Then there is an open subscheme of `X` containing the image of
> `Z` on which `f` is flat.

```lean
theorem exists_open_flat_of_isRelativeH1RegularImmersion
    {S X Z : Scheme.{u}} (f : X ⟶ S) (i : Z ⟶ X) [IsImmersion i]
    [LocallyOfFinitePresentation f]
    (hi : AlgebraicGeometry.IsRelativeH1RegularImmersion f i) :
    ∃ U : X.Opens, Set.range i.base ⊆ (U : Set X) ∧ Flat (U.ι ≫ f)
```

**`Stacks.AlgebraicGeometry.isRegularImmersion_of_isRelativeH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhoodRegularity.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhoodRegularity.lean#L115). The attribute's comment: “part (2): the immersion is regular”.

> **Stacks Project, Tag 063V, part (2): the immersion is regular.**  A relative `H₁`-regular
> immersion into a scheme locally of finite presentation over the base is a regular immersion.

```lean
theorem isRegularImmersion_of_isRelativeH1RegularImmersion {S X Z : Scheme.{u}} (f : X ⟶ S)
    (i : Z ⟶ X) [IsImmersion i] [LocallyOfFinitePresentation f]
    (hi : AlgebraicGeometry.IsRelativeH1RegularImmersion f i) : IsRegularImmersion i
```

**`Stacks.AlgebraicGeometry.isRegularImmersion_baseChange_of_isRelativeH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhoodRegularity.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhoodRegularity.lean#L126). The attribute's comment: “part (2): the immersion stays regular after any base change”.

> **Stacks Project, Tag 063V, part (2): regularity after an arbitrary base change.**  A
> relative `H₁`-regular immersion into a scheme locally of finite presentation over the base
> remains a regular immersion after any change of the base scheme.

```lean
theorem isRegularImmersion_baseChange_of_isRelativeH1RegularImmersion {S X Z S' : Scheme.{u}}
    (f : X ⟶ S) (i : Z ⟶ X) [IsImmersion i] [LocallyOfFinitePresentation f]
    (hi : AlgebraicGeometry.IsRelativeH1RegularImmersion f i) (g : S' ⟶ S) :
    IsRegularImmersion (pullback.fst (pullback.snd g f) i)
```

## Tag 063W, a lemma

[Tag 063W](https://stacks.math.columbia.edu/tag/063W) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_mem_isRelativeQuasiRegularImmersion_le_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/Containing.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/Containing.lean#L638). The attribute's comment: “item (1): containing”.

> **Stacks tag 063W, item (1).**  Let `f : X ⟶ S` be flat and locally of finite presentation,
> let `T` be a closed subscheme of `X` and let `x` be a point of `T` whose fibre over `f x` is a
> quasi-regular immersion near `x`.  Then there is an open `U ∋ x` and a relative quasi-regular
> immersion `Z ⊆ U` over `S` with `T ∩ U ⊆ Z` and `Z_s = T_s ∩ U_s`.

```lean
theorem exists_mem_isRelativeQuasiRegularImmersion_le_comap (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (T : X.IdealSheafData) (x : X) (hx : x ∈ T.support)
    (hfib : ∃ V : (f.fiber (f x)).Opens, f.asFiber x ∈ V ∧ IsQuasiRegularImmersion
      (((T.comap (f.fiberι (f x))).comap V.ι).subschemeι)) :
    ∃ (U : X.Opens) (_ : x ∈ U) (Z : U.toScheme.IdealSheafData),
      IsRelativeQuasiRegularImmersion (U.ι ≫ f) Z.subschemeι ∧ Z ≤ T.comap U.ι ∧
        Z.comap ((f.fiberι (f x)).resLE U (f.fiberι (f x) ⁻¹ᵁ U) le_rfl)
          = (T.comap (f.fiberι (f x))).comap (f.fiberι (f x) ⁻¹ᵁ U).ι
```

**`Stacks.AlgebraicGeometry.exists_mem_isRelativeQuasiRegularImmersion_of_dim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/EqualityEquationCount.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/EqualityEquationCount.lean#L159). The attribute's comment: “item (3): equation count”.

> **Stacks tag 063W, item (3).**  Let `f : X ⟶ S` be flat and locally of finite presentation,
> let `T` be a closed subscheme of `X` and let `x` be a point of `T` such that the fibre of `T`
> over `f x` is a quasi-regular immersion on a neighbourhood of `x`.  Assume that `T` is cut out on
> an affine open neighbourhood of `x` by `n` equations, and that `n` is the drop in local dimension
> from the fibre `X_s` to the fibre `T_s` at `x`.  Then there is an open `U ∋ x` on which `T`
> itself is a relative quasi-regular immersion over `S`, and a regular immersion.

```lean
theorem exists_mem_isRelativeQuasiRegularImmersion_of_dim_eq (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (T : X.IdealSheafData) (x : X) (hx : x ∈ T.support)
    (hfib : ∃ V : (f.fiber (f x)).Opens, f.asFiber x ∈ V ∧ IsQuasiRegularImmersion
      (((T.comap (f.fiberι (f x))).comap V.ι).subschemeι))
    {n : ℕ} {U₀ : X.Opens} (hU₀ : IsAffineOpen U₀) (hxU₀ : x ∈ U₀) (g : Fin n → Γ(X, U₀))
    (hg : T.ideal ⟨U₀, hU₀⟩ = Ideal.span (Set.range g))
    (hdim : topologicalKrullDimAt (T.comap (f.fiberι (f x))).subscheme
          ⟨f.asFiber x, asFiber_mem_support_comap f T x hx⟩ + (n : WithBot ℕ∞)
        = topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)) :
    ∃ U : X.Opens, x ∈ U ∧
      IsRelativeQuasiRegularImmersion (U.ι ≫ f) (T.comap U.ι).subschemeι ∧
        IsRegularImmersion (T.comap U.ι).subschemeι
```

**`Stacks.AlgebraicGeometry.exists_mem_isRelativeQuasiRegularImmersion_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/EqualityFlat.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/EqualityFlat.lean#L71). The attribute's comment: “equality\_flat”. References: EGA IV (19.2.4), “b) => c)”.

> **Stacks tag 063W, item (2).**  Let `f : X ⟶ S` be flat and locally of finite presentation,
> let `T` be a closed subscheme of `X` whose closed immersion into `X` is locally of finite
> presentation, and let `x` be a point of `T` such that the fibre of `T` over `f x` is a
> quasi-regular immersion on a neighbourhood of `x` and `T` is flat over `S` at `x`.  Then there
> is an open `U ∋ x` on which `T` itself is a relative quasi-regular immersion over `S`, and a
> regular immersion.

```lean
theorem exists_mem_isRelativeQuasiRegularImmersion_of_flatAt {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] (T : X.IdealSheafData)
    [LocallyOfFinitePresentation T.subschemeι] (x : X) (hx : x ∈ T.support)
    (hfib : ∃ V : (f.fiber (f x)).Opens, f.asFiber x ∈ V ∧
      IsQuasiRegularImmersion (((T.comap (f.fiberι (f x))).comap V.ι).subschemeι))
    (hflat : ((T.subschemeι ≫ f).stalkMap (⟨x, hx⟩ : T.subscheme)).hom.Flat) :
    ∃ U : X.Opens, x ∈ U ∧
      IsRelativeQuasiRegularImmersion (U.ι ≫ f) (T.comap U.ι).subschemeι ∧
        IsRegularImmersion (T.comap U.ι).subschemeι
```

**`Stacks.AlgebraicGeometry.isRelativeQuasiRegularImmersion_subschemeι_of_forall_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/Fibrewise.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/Fibrewise.lean#L82). The attribute's comment: “fibrewise criterion”.

> **The fibrewise criterion of Stacks tag 063W.**  Let `f : X ⟶ S` be flat and locally of finite
> presentation and let `T` be a closed subscheme of `X` which is flat and locally of finite
> presentation over `S`.  If every fibre of `T` is a quasi-regular closed subscheme of the
> corresponding fibre of `X`, then `T` is a relative quasi-regular immersion over `S`.

```lean
theorem isRelativeQuasiRegularImmersion_subschemeι_of_forall_fiber (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (T : X.IdealSheafData) [Flat (T.subschemeι ≫ f)]
    [LocallyOfFinitePresentation (T.subschemeι ≫ f)]
    (hfib : ∀ s : S, IsQuasiRegularImmersion (T.comap (f.fiberι s)).subschemeι) :
    IsRelativeQuasiRegularImmersion f T.subschemeι
```

## Tag 067R, a lemma

[Tag 067R](https://stacks.math.columbia.edu/tag/067R) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/SmoothSection.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/SmoothSection.lean#L65). References: EGA IV (17.12.3), “necessity”; SGA 6 VII (1.10), “section case”; SGA 6 VII (4.2), “more general”; SGA 6 VIII (1.3), “more general”; SGA 6 VIII (2.4), “special case”.

> **Stacks Project, Tag 067R.**  A section `σ` of a smooth morphism `f : X ⟶ S` of schemes is a
> regular immersion.

```lean
theorem isRegularImmersion_of_smooth_section (f : X ⟶ S) [Smooth f] (σ : S ⟶ X)
    (hσ : σ ≫ f = 𝟙 S) :
    letI : IsImmersion σ := isImmersion_of_comp_eq_id σ f hσ
    IsRegularImmersion σ
```

## Tag 067S, a lemma

[Tag 067S](https://stacks.math.columbia.edu/tag/067S) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isRegularImmersion_of_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean#L81). The attribute's comment: “regular”.

> **Stacks 067S** for regular immersions. If the composite of an immersion with a smooth
> morphism is regular, the immersion is regular.

```lean
theorem isRegularImmersion_of_comp_of_smooth
    (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i] [IsImmersion (i ≫ f)] [Smooth f]
    (hj : IsRegularImmersion (i ≫ f)) : IsRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_of_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean#L103). The attribute's comment: “koszul\_regular”.

> **Stacks 067S** for Koszul-regular immersions. If the composite of an immersion with a smooth
> morphism is Koszul-regular, the immersion is Koszul-regular.

```lean
theorem isKoszulRegularImmersion_of_comp_of_smooth
    (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i] [IsImmersion (i ≫ f)] [Smooth f]
    (hj : IsKoszulRegularImmersion (i ≫ f)) : IsKoszulRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_of_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean#L130). The attribute's comment: “h1\_regular”.

> **Stacks 067S** for `H₁`-regular immersions. If the composite of an immersion with a smooth
> morphism is `H₁`-regular, the immersion is `H₁`-regular.

```lean
theorem isH1RegularImmersion_of_comp_of_smooth
    (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i] [IsImmersion (i ≫ f)] [Smooth f]
    (hj : IsH1RegularImmersion (i ≫ f)) : IsH1RegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_of_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothPermanence.lean#L147). The attribute's comment: “quasi\_regular”.

> **Stacks 067S** for quasi-regular immersions. If the composite of an immersion with a smooth
> morphism is quasi-regular, the immersion is quasi-regular.

```lean
theorem isQuasiRegularImmersion_of_comp_of_smooth
    (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i] [IsImmersion (i ≫ f)] [Smooth f]
    (hj : IsQuasiRegularImmersion (i ≫ f)) : IsQuasiRegularImmersion i
```

## Tag 067T, a lemma

[Tag 067T](https://stacks.math.columbia.edu/tag/067T) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_of_syntomic_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/SyntomicIntoSmooth.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/SyntomicIntoSmooth.lean#L82). References: SGA 6 VII (1.10), “more general”.

> **Stacks Project, Tag 067T.**  Let `i : Y ⟶ X` be an immersion and `f : X ⟶ S` a smooth
> morphism such that the structure morphism `i ≫ f` of `Y` over `S` is syntomic.  Then `i` is a
> regular immersion.

```lean
theorem isRegularImmersion_of_syntomic_of_smooth [IsImmersion i] [Smooth f]
    (h : Syntomic (i ≫ f)) : IsRegularImmersion i
```

## Tag 067U, a lemma

[Tag 067U](https://stacks.math.columbia.edu/tag/067U) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_of_smooth_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/SyntomicIntoSmooth.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeRegularImmersion/SyntomicIntoSmooth.lean#L135). References: SGA 6 VII (1.10); SGA 1 II (4.16), “X smooth ⇒ i regular”; SGA 6 VIII (1.1), “more general”; SGA 6 VIII (1.3), “more general”; SGA 6 VIII (1.8), “partial, special case”; SGA 6 VIII (2.4), “special case”.

> **Stacks Project, Tag 067U.**  An immersion `i : Y ⟶ X` between two schemes smooth over `S`
> is a regular immersion.  This is the case of Stacks tag 067T in which the structure morphism of
> `Y` is smooth, a smooth morphism being syntomic (Stacks tag 01VD).

```lean
theorem isRegularImmersion_of_smooth_of_smooth [IsImmersion i] [Smooth f] [Smooth (i ≫ f)] :
    IsRegularImmersion i
```

## Tag 0693, a lemma

[Tag 0693](https://stacks.math.columbia.edu/tag/0693) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetPermanence.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetPermanence.lean#L481). The attribute's comment: “koszul\_regular”.

> **Stacks tag 0693 for Koszul-regular immersions.** In a commutative triangle `Y ⟶ X ⟶ S` with
> `X ⟶ S` smooth and both `Y ⟶ X` and `Y ⟶ S` immersions, the composite `Y ⟶ S` of a Koszul-regular
> immersion `Y ⟶ X` is a Koszul-regular immersion.
>
> Koszul-regularity is local on the source, and near a point of `Y` the immersion into `X` is pushed
> into a relative affine space `𝔸ⁿ_V` over an affine open `V ⊆ S`.  Shrinking `V` to an affine open
> `T` over which `Y` is closed, the lifted coordinates of that chart define a section `σ` of
> `𝔸ⁿ_V ⟶ V` over `T` through which the chart factors, and Stacks tag 068Z for the retracted
> immersion `σ` descends Koszul-regularity to `Y ⟶ T`.

```lean
theorem isKoszulRegularImmersion_comp_of_smooth (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i]
    [IsImmersion (i ≫ f)] [Smooth f] (hi : IsKoszulRegularImmersion i) :
    IsKoszulRegularImmersion (i ≫ f)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetPermanence.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetPermanence.lean#L549). The attribute's comment: “h1\_regular”.

> **Stacks tag 0693 for `H₁`-regular immersions.** In a commutative triangle `Y ⟶ X ⟶ S` with
> `X ⟶ S` smooth and both `Y ⟶ X` and `Y ⟶ S` immersions, the composite `Y ⟶ S` of an `H₁`-regular
> immersion `Y ⟶ X` is an `H₁`-regular immersion.
>
> `H₁`-regularity is local on the source, and near a point of `Y` the immersion into `X` is pushed
> into a relative affine space `𝔸ⁿ_V` over an affine open `V ⊆ S`.  Shrinking `V` to an affine open
> `T` over which `Y` is closed, the lifted coordinates of that chart define a section `σ` of
> `𝔸ⁿ_V ⟶ V` over `T` through which the chart factors, and Stacks tag 068Z for the retracted
> immersion `σ` descends `H₁`-regularity to `Y ⟶ T`.

```lean
theorem isH1RegularImmersion_comp_of_smooth (i : Y ⟶ X) (f : X ⟶ S) [IsImmersion i]
    [IsImmersion (i ≫ f)] [Smooth f] (hi : IsH1RegularImmersion i) :
    IsH1RegularImmersion (i ≫ f)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_comp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetQuasiRegular.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SmoothTargetQuasiRegular.lean#L260). The attribute's comment: “quasi\_regular”.

> **Smooth postcomposition.** In a commutative triangle `Y ⟶ X ⟶ S` with `X ⟶ S` smooth and
> both `Y ⟶ X` and `Y ⟶ S` immersions, the composite `Y ⟶ S` of a quasi-regular immersion `Y ⟶ X`
> is a quasi-regular immersion.

```lean
theorem isQuasiRegularImmersion_comp_of_smooth {Y X S : Scheme.{u}} (i : Y ⟶ X) (f : X ⟶ S)
    [IsImmersion i] [IsImmersion (i ≫ f)] [Smooth f] (hi : IsQuasiRegularImmersion i) :
    IsQuasiRegularImmersion (i ≫ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.23, Tag 063P](https://stacks.math.columbia.edu/tag/063P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
