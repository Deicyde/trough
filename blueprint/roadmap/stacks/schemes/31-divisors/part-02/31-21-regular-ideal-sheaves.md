---
declaration: section
origin: cited
lean: AlgebraicGeometry.regularSequenceMultiplication, Stacks.AlgebraicGeometry.SeqKoszul.sheafComplex, Stacks.AlgebraicGeometry.QuasiRegular.quasiRegularMap, Stacks.AlgebraicGeometry.SeqKoszul.isH1RegularSequence_of_isKoszulRegularSequence, Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularSequence_of_regularSequence, Stacks.AlgebraicGeometry.RegularIdealSheaf.isIso_quasiRegularMap_of_isH1RegularSequence, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsQuasiRegularIdealSheaf, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularIdealSheaf
statement: formalized
proof: formalized
---

# 31.21 Regular ideal sheaves

Section 31.21 of the Stacks Project, [Tag 067M](https://stacks.math.columbia.edu/tag/067M). 11 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0639, an equation

[Tag 0639](https://stacks.math.columbia.edu/tag/0639) in the Stacks Project.

**`AlgebraicGeometry.regularSequenceMultiplication`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularIdealSheaves.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularIdealSheaves.lean#L330).

> **Stacks Project, Tag 0639.** Multiplication by `f i` on
> `O_X/(f₀, …, f_{i-1})`, for an arbitrary ringed space.

```lean
public noncomputable def regularSequenceMultiplication
    (X : RingedSpace.{u, v}) {n : ℕ}
    (f : Fin n → X.presheaf.obj (op (⊤ : Opens X))) (i : Fin n) :
    RegularSequenceMultiplicationData X f i
```

## Tag 063A, an equation

[Tag 063A](https://stacks.math.columbia.edu/tag/063A) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.AlgebraicGeometry.SeqKoszul.sheafComplex`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/SheafCondition.lean#L192), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/QuasiRegular/SectionKoszulComplex.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiRegular/SectionKoszulComplex.lean#L22) (StacksFrontier): “the notation `K_•(O_X, f_•)` of the section on regular ideal sheaves: the Koszul complex of Modules, Definition 17.24.2 (Tag 062L) for the structure sheaf of a ringed space and a finite family of its global sections.”.

## Tag 063B, an equation

[Tag 063B](https://stacks.math.columbia.edu/tag/063B) in the Stacks Project.

**`Stacks.AlgebraicGeometry.QuasiRegular.quasiRegularMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiRegular/Basic.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiRegular/Basic.lean#L500).

> The canonical morphism of sheaves `(O_X / J)[T₁, ..., Tᵣ] ⟶ ⨁ d, J^d / J^(d+1)` associated to
> global sections `f₁, ..., fᵣ`, sending `Tᵢ` to `fᵢ mod J²`.

```lean
noncomputable def quasiRegularMap (X : RingedSpace.{u}) {r : ℕ}
    (f : Fin r → X.presheaf.obj (op (⊤ : Opens X))) : QuasiRegularMapData X f
```

## Tag 063C, a lemma

[Tag 063C](https://stacks.math.columbia.edu/tag/063C) in the Stacks Project.

**`Stacks.AlgebraicGeometry.SeqKoszul.isH1RegularSequence_of_isKoszulRegularSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/Regular.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/Regular.lean#L77). The attribute's comment: “Koszul-regular implies H₁-regular”. References: EGA IV (19.5.1), “b) => b')”.

> **Stacks Project, Tag 063C.** A Koszul-regular sequence is `H₁`-regular: degree `1` is one of
> the positive degrees in which the Koszul complex of a Koszul-regular sequence is acyclic.

```lean
theorem isH1RegularSequence_of_isKoszulRegularSequence
    (h : IsKoszulRegularSequence X f) : IsH1RegularSequence X f
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularSequence_of_regularSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L205). The attribute's comment: “regular implies Koszul-regular”. References: EGA IV (19.5.1), “a) => b)”.

> A regular sequence of global sections of the structure sheaf is a Koszul-regular sequence: if
> multiplication by `f i` on `O_X/(f₁, …, f_{i-1})` is an injective map of sheaves for every `i`,
> then the Koszul complex `K_•(O_X, f_•)` is acyclic in positive degrees.

```lean
theorem isKoszulRegularSequence_of_regularSequence {r : ℕ}
    (f : Fin r → X.presheaf.obj (op (⊤ : Opens X)))
    (hf : ∀ i : Fin r, Mono (regularSequenceMultiplication X f i).multiplication) :
    SeqKoszul.IsKoszulRegularSequence X f
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isIso_quasiRegularMap_of_isH1RegularSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L217). The attribute's comment: “H₁-regular implies quasi-regular”.

> For an `H₁`-regular sequence of global sections the quasi-regularity morphism of Stacks tag
> 063B is an isomorphism, i.e. the sequence is quasi-regular.

```lean
theorem isIso_quasiRegularMap_of_isH1RegularSequence {r : ℕ}
    (f : Fin r → X.presheaf.obj (op (⊤ : Opens X)))
    (h : SeqKoszul.IsH1RegularSequence X f) : IsIso (quasiRegularMap X f).hom
```

## Tag 063D, a definition

[Tag 063D](https://stacks.math.columbia.edu/tag/063D) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsQuasiRegularIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Basic.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Basic.lean#L132). The attribute's comment: “part (4): quasi-regular ideal sheaf”. References: EGA IV (16.9.1), “quasi-regular”.

> **The local quasi-regularity condition of Stacks tag 063D, part (4).** The ideal sheaf `J` is
> quasi-regular when, near every point of the support of `O_X / J`, it is generated by a sequence
> whose sheaf quasi-regularity map of Stacks tag 063B is an isomorphism.

```lean
def IsQuasiRegularIdealSheaf (X : RingedSpace.{u})
    (J : (structureSheafModule X).Submodule) : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean#L134). The attribute's comment: “part (1): regular ideal sheaf”.

> **Stacks tag 063D, part (1).** The ideal sheaf `J` is regular when, near every point of the
> support of `O_X/J`, it is generated by a regular sequence of sections.

```lean
def IsRegularIdealSheaf (X : RingedSpace.{u}) (J : (structureSheafModule X).Submodule) : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsKoszulRegularIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean#L143). The attribute's comment: “part (2): Koszul-regular ideal sheaf”. References: SGA 6 VII (1.4), “regular ideal J”.

> **Stacks tag 063D, part (2).** The ideal sheaf `J` is Koszul-regular when, near every point of
> the support of `O_X/J`, it is generated by a sequence whose Koszul complex is acyclic in positive
> degrees.

```lean
def IsKoszulRegularIdealSheaf (X : RingedSpace.{u})
    (J : (structureSheafModule X).Submodule) : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsH1RegularIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean#L153). The attribute's comment: “part (3): H₁-regular ideal sheaf”.

> **Stacks tag 063D, part (3).** The ideal sheaf `J` is `H₁`-regular when, near every point of
> the support of `O_X/J`, it is generated by a sequence whose Koszul complex is exact in degree
> `1`.

```lean
def IsH1RegularIdealSheaf (X : RingedSpace.{u})
    (J : (structureSheafModule X).Submodule) : Prop
```

## Tag 063E, a lemma

[Tag 063E](https://stacks.math.columbia.edu/tag/063E) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_of_isRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L238). The attribute's comment: “regular implies Koszul-regular”.

> **A regular ideal sheaf is Koszul-regular.**  One implication of Stacks tag 063E, between
> parts (1) and (2) of Stacks tag 063D.

```lean
theorem isKoszulRegularIdealSheaf_of_isRegularIdealSheaf (h : IsRegularIdealSheaf X J) :
    IsKoszulRegularIdealSheaf X J
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularIdealSheaf_of_isH1RegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L247). The attribute's comment: “H₁-regular implies quasi-regular”.

> **An `H₁`-regular ideal sheaf is quasi-regular.**  One implication of Stacks tag 063E, between
> parts (3) and (4) of Stacks tag 063D.

```lean
theorem isQuasiRegularIdealSheaf_of_isH1RegularIdealSheaf (h : IsH1RegularIdealSheaf X J) :
    IsQuasiRegularIdealSheaf X J
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsKoszulRegularIdealSheaf.isH1RegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Regular.lean#L162). The attribute's comment: “Koszul-regular implies H₁-regular”.

> **Stacks Project, Tag 063E.**  A Koszul-regular ideal sheaf is `H₁`-regular: the local
> witnesses are the same sequences, and degree `1` is a positive degree.

```lean
theorem IsKoszulRegularIdealSheaf.isH1RegularIdealSheaf {X : RingedSpace.{u}}
    {J : (structureSheafModule X).Submodule} (h : IsKoszulRegularIdealSheaf X J) :
    IsH1RegularIdealSheaf X J
```

## Tag 063H, a lemma

[Tag 063H](https://stacks.math.columbia.edu/tag/063H) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_isGeneratedByOn_of_isFiniteType_of_le_sup_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiRegular/StalkGenerators.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiRegular/StalkGenerators.lean#L324). The attribute's comment: “the Nakayama and shrinking step of the proof only: sections of a finite-type `J` whose germs generate `J_x/J_x²` generate `J` near `x`. The characterization itself is `Stacks.AlgebraicGeometry.RegularIdealSheaf.Conormal.isQuasiRegularIdealSheaf_iff`.”.

> **The Nakayama and shrinking step in the proof of Stacks tag 063H.**  Let `J ⊆ O_X` be a
> sheaf of ideals of finite type on a locally ringed space and let `x` be a point of the support
> of `O_X / J`.  Sections `f₁, …, f_r` of `J` over a neighbourhood `U` of `x` whose germs generate
> `J_x` modulo `J_x²` generate `J` on a neighbourhood of `x`.

```lean
theorem exists_isGeneratedByOn_of_isFiniteType_of_le_sup_sq
    (hJ : SheafOfModules.IsFiniteType.{u, u, u} J.toSheafOfModules) {x : X}
    (hne : stalkIdeal J x ≠ ⊤) {U : Opens X} (hxU : x ∈ U) {r : ℕ}
    (f : Fin r → X.presheaf.obj (op U)) (hf : ∀ i, f i ∈ J.obj (op U))
    (hle : stalkIdeal J x
      ≤ Jid (germFamily X.toRingedSpace U f x hxU) ⊔ stalkIdeal J x ^ 2) :
    ∃ (V : Opens X) (_ : x ∈ V) (hVU : V ≤ U),
      IsGeneratedByOn X.toRingedSpace J V
        (fun i => X.presheaf.map (homOfLE hVU).op (f i))
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.Conormal.isQuasiRegularIdealSheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Characterization/IndependentGenerators.lean, line 747](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Characterization/IndependentGenerators.lean#L747). The attribute's comment: “both directions of the characterization: quasi-regular iff of finite type, with finite locally free conormal sheaf and isomorphic symmetric-power-to-graded maps”. References: EGA IV (16.9.4); EGA IV (17.12.1), “more general”.

> **Stacks Project, Tag 063H.** A sheaf of ideals is quasi-regular if and only
> if it is of finite type, has finite locally free conormal sheaf, and has
> isomorphic canonical symmetric-power-to-associated-graded maps in every degree.

```lean
public theorem isQuasiRegularIdealSheaf_iff (X : LocallyRingedSpace.{u})
    (J : (Stacks.RingedSpace.structureSheafModule X.toRingedSpace).Submodule) :
    IsQuasiRegularIdealSheaf X.toRingedSpace J ↔
      (J.toSheafOfModules.IsFiniteType ∧
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree (conormalSheaf X.toRingedSpace J) ∧
        ∀ n : ℕ, IsIso (conormalSymmetricToGradedMap X.toRingedSpace J n))
```

## Tag 067N, a lemma

[Tag 067N](https://stacks.math.columbia.edu/tag/067N) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_quasiRegular_generators_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean#L421). The attribute's comment: “(1)”. References: EGA IV (16.9.5), “(b') => (a)”.

> **Stacks Project, Tag 067N, part (1).** Let `J` be a quasi-regular ideal sheaf on a locally
> ringed space `X`, let `x ∈ X` and let `f₁, …, f_r ∈ J_x` be germs whose classes form a basis of
> the cotangent fibre `J_x / 𝔪_x J_x`.  Then there is an open neighbourhood `U` of `x` on which the
> `f_i` are the germs of sections of `J` which form a quasi-regular sequence generating `J`
> over `U`.

```lean
theorem exists_quasiRegular_generators_of_basis (x : X) {r : ℕ}
    (f : Fin r → Stacks.RingedSpace.stalkIdeal J x)
    (b : Module.Basis (Fin r)
      (X.presheaf.stalk x ⧸ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (Stacks.RingedSpace.idealCotangentFiber J x))
    (hf : ∀ i, b i = Submodule.Quotient.mk (f i))
    (hJ : IsQuasiRegularIdealSheaf X.toRingedSpace J) :
    ∃ (U : Opens X) (hxU : x ∈ U) (fU : Fin r → J.obj (op U)),
      (∀ i, X.presheaf.germ U x hxU (fU i).1 = (f i).1) ∧
      IsIso (quasiRegularMap (X.toRingedSpace.restrict U.isOpenEmbedding)
        (fun i => sectionOnRestriction X.toRingedSpace U (fU i).1)).hom ∧
      IsGeneratedByOn X.toRingedSpace J U (fun i => (fU i).1)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_h1Regular_generators_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean#L449). The attribute's comment: “(2)”.

> **Stacks Project, Tag 067N, part (2).** The `H₁`-regular case: for an `H₁`-regular ideal
> sheaf the sections produced over `U` have a Koszul complex which is germwise exact in degree
> `1`.

```lean
theorem exists_h1Regular_generators_of_basis (x : X) {r : ℕ}
    (f : Fin r → Stacks.RingedSpace.stalkIdeal J x)
    (b : Module.Basis (Fin r)
      (X.presheaf.stalk x ⧸ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (Stacks.RingedSpace.idealCotangentFiber J x))
    (hf : ∀ i, b i = Submodule.Quotient.mk (f i))
    (hJ : IsH1RegularIdealSheaf X.toRingedSpace J) :
    ∃ (U : Opens X) (hxU : x ∈ U) (fU : Fin r → J.obj (op U)),
      (∀ i, X.presheaf.germ U x hxU (fU i).1 = (f i).1) ∧
      IsKoszulSequenceExactOn X.toRingedSpace U (fun i => (fU i).1) (fun j => j = 1) ∧
      IsGeneratedByOn X.toRingedSpace J U (fun i => (fU i).1)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_koszulRegular_generators_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Generators.lean#L475). The attribute's comment: “(3)”.

> **Stacks Project, Tag 067N, part (3).** The Koszul-regular case: for a Koszul-regular ideal
> sheaf the sections produced over `U` have a Koszul complex which is germwise exact in every
> positive degree.

```lean
theorem exists_koszulRegular_generators_of_basis (x : X) {r : ℕ}
    (f : Fin r → Stacks.RingedSpace.stalkIdeal J x)
    (b : Module.Basis (Fin r)
      (X.presheaf.stalk x ⧸ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (Stacks.RingedSpace.idealCotangentFiber J x))
    (hf : ∀ i, b i = Submodule.Quotient.mk (f i))
    (hJ : IsKoszulRegularIdealSheaf X.toRingedSpace J) :
    ∃ (U : Opens X) (hxU : x ∈ U) (fU : Fin r → J.obj (op U)),
      (∀ i, X.presheaf.germ U x hxU (fU i).1 = (f i).1) ∧
      IsKoszulSequenceExactOn X.toRingedSpace U (fun i => (fU i).1) (fun j => 0 < j) ∧
      IsGeneratedByOn X.toRingedSpace J U (fun i => (fU i).1)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_koszulRegular_sections_of_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalPermanence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalPermanence.lean#L168). The attribute's comment: “part (3), with the local witness at x in place of Koszul-regularity of J, and assuming J\_x is not the whole local ring”. References: SGA 6 VII (1.4), “1.4.2”.

> **[Stacks Project, Tag 067N] part (3).** Let `J` be an ideal subsheaf of the structure sheaf
> of a locally ringed space, generated on a neighbourhood of `x` by a sequence that is
> Koszul-regular at every point.  Then any lift of a basis of the cotangent fibre `J_x/𝔪_x J_x` is
> realised on a neighbourhood of `x` by sections that generate `J` and are Koszul-regular at every
> point.
>
> Koszul-regularity of a family on an open is taken germwise, which
> `isKoszulSequenceExactOn_iff_forall_germ_isKoszulRegular` identifies with exactness of its sheaf
> Koszul complex.
>
> Two departures from the source.  The hypothesis is the local witness at `x` that Koszul-regularity
> of `J` supplies there, rather than Koszul-regularity of `J` itself; that is weaker, so a caller
> with the source's hypothesis can supply it.  And `J_x ≠ 𝒪_{X,x}` is assumed, which the source does
> not assume: in the excluded case the cotangent fibre is the residue field, so `r = 1` and `f 0` is
> a unit, and the source's conclusion holds there too.

```lean
theorem exists_koszulRegular_sections_of_basis {X : LocallyRingedSpace.{u}}
    (J : (structureSheafModule X.toRingedSpace).Submodule) (x : X) {r : ℕ}
    (f : Fin r → stalkIdeal J x)
    (b : Module.Basis (Fin r)
      (X.presheaf.stalk x ⧸ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
      (idealCotangentFiber J x))
    (hf : ∀ i, b i = Submodule.Quotient.mk (f i))
    (hsupp : stalkIdeal J x ≠ ⊤)
    (V : Opens X) (hxV : x ∈ V) {s : ℕ} (g : Fin s → X.presheaf.obj (op V))
    (hgen : IsGeneratedByOn X.toRingedSpace J V g)
    (hK : ∀ (y : X) (hy : y ∈ V), Koszul.IsKoszulRegular (germFamily X.toRingedSpace V g y hy)) :
    ∃ (U : Opens X) (hxU : x ∈ U) (fU : Fin r → X.presheaf.obj (op U)),
      (∀ i, X.presheaf.germ U x hxU (fU i) = (f i : X.presheaf.stalk x)) ∧
      IsGeneratedByOn X.toRingedSpace J U fU ∧
      ∀ (y : X) (hy : y ∈ U), Koszul.IsKoszulRegular (germFamily X.toRingedSpace U fU y hy)
```

## Tag 063F, a lemma

[Tag 063F](https://stacks.math.columbia.edu/tag/063F) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isFiniteType_of_isRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L373). The attribute's comment: “finite type for regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A regular ideal sheaf on a scheme is of finite type.

```lean
theorem isFiniteType_of_isRegularIdealSheaf (hJ : IsRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsFiniteType
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasicoherent_of_isRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L381). The attribute's comment: “quasi-coherence for regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A regular ideal sheaf on a scheme is quasi-coherent.

```lean
theorem isQuasicoherent_of_isRegularIdealSheaf (hJ : IsRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isFiniteType_of_isKoszulRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L387). The attribute's comment: “finite type for Koszul-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A Koszul-regular ideal sheaf on a scheme is of finite type.

```lean
theorem isFiniteType_of_isKoszulRegularIdealSheaf
    (hJ : IsKoszulRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsFiniteType
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasicoherent_of_isKoszulRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L396). The attribute's comment: “quasi-coherence for Koszul-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A Koszul-regular ideal sheaf on a scheme is quasi-coherent.

```lean
theorem isQuasicoherent_of_isKoszulRegularIdealSheaf
    (hJ : IsKoszulRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isFiniteType_of_isH1RegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L403). The attribute's comment: “finite type for H₁-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  An `H₁`-regular ideal sheaf on a scheme is of finite type.

```lean
theorem isFiniteType_of_isH1RegularIdealSheaf (hJ : IsH1RegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsFiniteType
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasicoherent_of_isH1RegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L411). The attribute's comment: “quasi-coherence for H₁-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  An `H₁`-regular ideal sheaf on a scheme is quasi-coherent.

```lean
theorem isQuasicoherent_of_isH1RegularIdealSheaf (hJ : IsH1RegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isFiniteType_of_isQuasiRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L417). The attribute's comment: “finite type for quasi-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A quasi-regular ideal sheaf on a scheme is of finite type.

```lean
theorem isFiniteType_of_isQuasiRegularIdealSheaf
    (hJ : IsQuasiRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsFiniteType
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasicoherent_of_isQuasiRegularIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Relative/RegularIdealSheafFiniteType.lean#L426). The attribute's comment: “quasi-coherence for quasi-regular ideal sheaves”.

> **Stacks Project, Tag 063F.**  A quasi-regular ideal sheaf on a scheme is quasi-coherent.

```lean
theorem isQuasicoherent_of_isQuasiRegularIdealSheaf
    (hJ : IsQuasiRegularIdealSheaf X.toRingedSpace J) :
    J.toSheafOfModules.IsQuasicoherent
```

## Tag 063G, a lemma

[Tag 063G](https://stacks.math.columbia.edu/tag/063G) in the Stacks Project.

**`Stacks.AlgebraicGeometry.H1RegularIdealSheaf.isH1RegularIdealSheaf_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/H1RegularIdealSheaf/Affine.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/H1RegularIdealSheaf/Affine.lean#L120). The attribute's comment: “h1\_regular”.

> **Stacks Project, Tag 063G (`h1_regular`).** A sheaf of ideals on a scheme is `H₁`-regular if
> and only if, around each point of the support of its quotient, it is generated on an affine open
> by a sequence which is `H₁`-regular in the ring of sections of that open.

```lean
theorem isH1RegularIdealSheaf_iff_affine (X : Scheme.{u})
    (J : (structureSheafModule X.toRingedSpace).Submodule) :
    IsH1RegularIdealSheaf X.toRingedSpace J ↔
      ∀ x : X, x ∈ idealQuotientSupport X.toRingedSpace J →
        ∃ (U : X.affineOpens) (_hx : x ∈ (U : Set X)) (r : ℕ) (f : Fin r → Γ(X, U.1)),
          IsGeneratedByOn X.toRingedSpace J U.1 f ∧ Koszul.IsH1Regular f
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/KoszulRegularIdealSheaf/Stalkwise.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/KoszulRegularIdealSheaf/Stalkwise.lean#L104). The attribute's comment: “koszul\_regular”.

> **Stacks Project, Tag 063G (`koszul_regular`).** A sheaf of ideals on a scheme is
> Koszul-regular if and only if, around each point of the support of its quotient, it is generated
> on an affine open by a sequence which is Koszul-regular in the ring of sections of that open.

```lean
theorem isKoszulRegularIdealSheaf_iff_affine (X : Scheme.{u})
    (J : (structureSheafModule X.toRingedSpace).Submodule) :
    IsKoszulRegularIdealSheaf X.toRingedSpace J ↔
      ∀ x : X, x ∈ idealQuotientSupport X.toRingedSpace J →
        ∃ (U : X.affineOpens) (_hx : x ∈ (U : Set X)) (r : ℕ) (f : Fin r → Γ(X, U.1)),
          IsGeneratedByOn X.toRingedSpace J U.1 f ∧ Koszul.IsKoszulRegular f
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularIdealSheaf_iff_exists_affine_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/QuasiRegular.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/QuasiRegular.lean#L148). The attribute's comment: “quasi\_regular”.

> A sheaf of ideals on a scheme is quasi-regular
> if and only if, around each point of the support of its quotient, it is generated on an affine
> open by a quasi-regular sequence in the ring of sections of that open.

```lean
theorem isQuasiRegularIdealSheaf_iff_exists_affine_generators (X : Scheme.{u})
    (J : (structureSheafModule X.toRingedSpace).Submodule) :
    IsQuasiRegularIdealSheaf X.toRingedSpace J ↔
      ∀ x : X, x ∈ idealQuotientSupport X.toRingedSpace J →
        ∃ (U : X.affineOpens) (_hx : x ∈ (U : Set X)) (r : ℕ)
          (f : Fin r → X.toRingedSpace.presheaf.obj (op U.1)),
          IsGeneratedByOn X.toRingedSpace J U.1 f ∧
            RingTheory.Sequence.IsQuasiRegular
              (X.toRingedSpace.presheaf.obj (op U.1)) (List.ofFn f)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheafAffine.isRegularIdealSheaf_iff_exists_affine_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheafAffine/Regular.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RegularIdealSheafAffine/Regular.lean#L100). The attribute's comment: “regular”.

> **Stacks Project, Tag 063G (regular).** A sheaf of ideals on a scheme is regular if and only
> if, around each point of the support of its quotient, it is generated on an affine open by a
> regular sequence in the ring of sections of that open.

```lean
theorem isRegularIdealSheaf_iff_exists_affine_generators (X : Scheme.{u})
    (J : (structureSheafModule X.toRingedSpace).Submodule) :
    IsRegularIdealSheaf X.toRingedSpace J ↔
      ∀ x : X, x ∈ idealQuotientSupport X.toRingedSpace J →
        ∃ (U : Opens X) (_hx : x ∈ U) (_hU : IsAffineOpen U) (r : ℕ)
          (f : Fin r → X.presheaf.obj (op U)),
          RingTheory.Sequence.IsRegular (X.presheaf.obj (op U)) (List.ofFn f) ∧
            IsGeneratedByOn X.toRingedSpace J U f
```

## Tag 063I, a lemma

[Tag 063I](https://stacks.math.columbia.edu/tag/063I) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.regular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/NoetherianEquivalence.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/NoetherianEquivalence.lean#L69). References: EGA IV (16.9.10); EGA IV (16.9.11); SGA 6 VII (1.4), “special case”.

> Let `X` be a locally Noetherian scheme, let `J` be a quasi-coherent sheaf of ideals and let `x`
> be a point of the support of `O_X / J`.  The following are equivalent:
>
> 1. `J_x` is generated by a regular sequence in `O_{X, x}`;
> 2. `J_x` is generated by a Koszul-regular sequence in `O_{X, x}`;
> 3. `J_x` is generated by an `H₁`-regular sequence in `O_{X, x}`;
> 4. `J_x` is generated by a quasi-regular sequence in `O_{X, x}`;
> 5. there is an affine neighbourhood `U` of `x` with `J(U)` generated by a regular sequence;
> 6. there is an affine neighbourhood `U` of `x` with `J(U)` generated by a Koszul-regular sequence;
> 7. there is an affine neighbourhood `U` of `x` with `J(U)` generated by an `H₁`-regular sequence;
> 8. there is an affine neighbourhood `U` of `x` with `J(U)` generated by a quasi-regular sequence;
> 9. there is a neighbourhood `U` of `x` on which `J` is a regular ideal sheaf;
> 10. there is a neighbourhood `U` of `x` on which `J` is a Koszul-regular ideal sheaf;
> 11. there is a neighbourhood `U` of `x` on which `J` is an `H₁`-regular ideal sheaf;
> 12. there is a neighbourhood `U` of `x` on which `J` is a quasi-regular ideal sheaf.

```lean
theorem regular_tfae [IsLocallyNoetherian X] (J : X.IdealSheafData) (x : X)
    (hx : x ∈ J.support) :
    List.TFAE
      [∃ (s : ℕ) (g : Fin s → X.presheaf.stalk x),
          stalkIdeal J x hx = Ideal.span (Set.range g) ∧
            IsRegular (X.presheaf.stalk x) (List.ofFn g),
        ∃ (s : ℕ) (g : Fin s → X.presheaf.stalk x),
          stalkIdeal J x hx = Ideal.span (Set.range g) ∧ Koszul.IsKoszulRegular g,
        ∃ (s : ℕ) (g : Fin s → X.presheaf.stalk x),
          stalkIdeal J x hx = Ideal.span (Set.range g) ∧ Koszul.IsH1Regular g,
        ∃ (s : ℕ) (g : Fin s → X.presheaf.stalk x),
          stalkIdeal J x hx = Ideal.span (Set.range g) ∧
            IsQuasiRegular (X.presheaf.stalk x) (List.ofFn g),
        ∃ (U : X.affineOpens) (_ : x ∈ U.1) (s : ℕ) (f : Fin s → Γ(X, U.1)),
          J.ideal U = Ideal.span (Set.range f) ∧ IsRegular Γ(X, U.1) (List.ofFn f),
        ∃ (U : X.affineOpens) (_ : x ∈ U.1) (s : ℕ) (f : Fin s → Γ(X, U.1)),
          J.ideal U = Ideal.span (Set.range f) ∧ Koszul.IsKoszulRegular f,
        ∃ (U : X.affineOpens) (_ : x ∈ U.1) (s : ℕ) (f : Fin s → Γ(X, U.1)),
          J.ideal U = Ideal.span (Set.range f) ∧ Koszul.IsH1Regular f,
        ∃ (U : X.affineOpens) (_ : x ∈ U.1) (s : ℕ) (f : Fin s → Γ(X, U.1)),
          J.ideal U = Ideal.span (Set.range f) ∧ IsQuasiRegular Γ(X, U.1) (List.ofFn f),
        ∃ U : X.Opens, x ∈ U ∧ IsRegularImmersion (J.comap U.ι).subschemeι,
        ∃ U : X.Opens, x ∈ U ∧ IsKoszulRegularImmersion (J.comap U.ι).subschemeι,
        ∃ U : X.Opens, x ∈ U ∧ IsH1RegularImmersion (J.comap U.ι).subschemeι,
        ∃ U : X.Opens, x ∈ U ∧ IsQuasiRegularImmersion (J.comap U.ι).subschemeι]
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.regularIdealSheaf_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean#L195). The attribute's comment: “in particular”.

> **Stacks tag 063I, the closing assertion.** On a locally Noetherian scheme `X` the four notions
> of Stacks tag 063D agree for a quasi-coherent sheaf of ideals: the ideal subsheaf of `O_X` cut
> out by `I : X.IdealSheafData` (the sections dying on the closed subscheme `I.subschemeι`, whose
> sections over an affine open `U` are `I.ideal U`) is regular, if and only if it is
> Koszul-regular, if and only if it is `H₁`-regular, if and only if it is quasi-regular.

```lean
theorem regularIdealSheaf_tfae [IsLocallyNoetherian X] (I : X.IdealSheafData) :
    List.TFAE
      [IsRegularIdealSheaf X.toRingedSpace (definingIdealOfHom I.subschemeι),
        IsKoszulRegularIdealSheaf X.toRingedSpace (definingIdealOfHom I.subschemeι),
        IsH1RegularIdealSheaf X.toRingedSpace (definingIdealOfHom I.subschemeι),
        IsQuasiRegularIdealSheaf X.toRingedSpace (definingIdealOfHom I.subschemeι)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.21, Tag 067M](https://stacks.math.columbia.edu/tag/067M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
