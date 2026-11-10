---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.size, Cardinal.stacksBound, AlgebraicGeometry.exists_size_cutoff, AlgebraicGeometry.Scheme.size_lt_of_le_stacksBound, AlgebraicGeometry.Scheme.size_lt_of_le_stacksBound_iSup, AlgebraicGeometry.Scheme.size_of_isAffine, AlgebraicGeometry.Scheme.size_le_of_iSup_eq_top, AlgebraicGeometry.Scheme.size_pullback_le
statement: formalized
proof: formalized
---

# 3.9 Constructing categories of schemes

Section 3.9 of the Stacks Project, [Tag 000H](https://stacks.math.columbia.edu/tag/000H). 11 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 000I, a lemma

[Tag 000I](https://stacks.math.columbia.edu/tag/000I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Basic.lean#L63).

> **The size of a scheme** (Stacks tag 000I, Definition 3.9.2).
>
> The *size* of a scheme `S` is the maximum of `ℵ₀`, the cardinality of the set of
> affine opens of `S`, and the supremum over affine opens `U ⊆ S` of the
> cardinality of the ring of sections `Γ(S, U)`.
>
> Every Section 3.9 size bound is stated in terms of this one cardinal, so the bounds
> compose.

```lean
noncomputable def Scheme.size (S : Scheme.{u}) : Cardinal.{u}
```

## Tag 046U, an equation

[Tag 046U](https://stacks.math.columbia.edu/tag/046U) in the Stacks Project.

**`Cardinal.stacksBound`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/Cardinal/SizeBound.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/SetTheory/Cardinal/SizeBound.lean#L42).

> **Stacks 046U.** The bound function `Bound(κ) = max {κ ^ ℵ₀, κ⁺}` on cardinals.
> Here `Order.succ κ` is the cardinal successor `κ⁺`.

```lean
noncomputable def Cardinal.stacksBound (κ : Cardinal) : Cardinal
```

## Tag 000J, a lemma

[Tag 000J](https://stacks.math.columbia.edu/tag/000J) in the Stacks Project.

**`AlgebraicGeometry.exists_size_cutoff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L82).

> For every set `S₀` of schemes there is an uncountable strong limit cardinal `κ` of uncountable
> cofinality such that every member of `S₀` has size below `κ`, that is, the collection
> `Sch_κ = {S | size S < κ}` contains `S₀`.

```lean
theorem exists_size_cutoff (S₀ : Set Scheme.{u}) [Small.{u} S₀] :
    ∃ κ : Cardinal.{u}, ℵ₀ < κ ∧ Cardinal.IsStrongPrelimit κ ∧ ℵ₀ < κ.ord.cof ∧
      ∀ S ∈ S₀, S.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_le_stacksBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L95). The attribute's comment: “(2)”.

> If `S` is an object of `Sch_κ` and `T` is a scheme of size at most `Bound(size S)`, then `T` is
> an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_le_stacksBound {κ : Cardinal.{u}} (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) {S T : Scheme.{u}} (hS : S.size < κ)
    (hT : T.size ≤ Cardinal.stacksBound S.size) : T.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_le_stacksBound_iSup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L103). The attribute's comment: “(3), (4)”.

> Let `F` be an at most countable family of objects of `Sch_κ`. Then every scheme of size at most
> `Bound(⨆ i, size (F i))` is an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_le_stacksBound_iSup {κ : Cardinal.{u}} (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) (hcof : ℵ₀ < κ.ord.cof) {ι : Type u}
    (hι : #ι ≤ ℵ₀) (F : ι → Scheme.{u}) (hF : ∀ i, (F i).size < κ) {X : Scheme.{u}}
    (hX : X.size ≤ Cardinal.stacksBound (⨆ i, (F i).size)) : X.size < κ
```

## Tag 000P, a lemma

[Tag 000P](https://stacks.math.columbia.edu/tag/000P) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Affine.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Affine.lean#L164).

> **Stacks 000P.** Let `S` be an affine scheme and `R = Γ(S, 𝒪_S)`. Then
> `size S = max ℵ₀ #R`.

```lean
theorem Scheme.size_of_isAffine (S : Scheme.{u}) [IsAffine S] :
    S.size = max ℵ₀ #Γ(S, ⊤)
```

## Tag 000Q, a lemma

[Tag 000Q](https://stacks.math.columbia.edu/tag/000Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_le_of_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/OpenCover.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/OpenCover.lean#L250).

> If `S : I → X.Opens` is an open cover of `X` indexed by a nonempty type `I`, then
> `size X ≤ max #I (⨆ i, size (S i))`.

```lean
theorem Scheme.size_le_of_iSup_eq_top {X : Scheme.{u}} {I : Type u} [Nonempty I]
    (S : I → X.Opens) (hcov : ⨆ i, S i = ⊤) :
    Scheme.size X ≤ max #I (⨆ i, Scheme.size (S i : Scheme))
```

## Tag 04T6, a lemma

[Tag 04T6](https://stacks.math.columbia.edu/tag/04T6) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_pullback_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Pullback.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Pullback.lean#L365).

> **Stacks 04T6.** The size of a fibre product of schemes is bounded by the maximum of the
> sizes of the two factors.

```lean
theorem Scheme.size_pullback_le {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) :
    Scheme.size (pullback f g) ≤ max (Scheme.size X) (Scheme.size Y)
```

## Tag 04T7, a lemma

[Tag 04T7](https://stacks.math.columbia.edu/tag/04T7) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_le_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/FiniteType.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/FiniteType.lean#L238).

> If `f : X ⟶ S` is locally of finite type and `X` is quasi-compact, then
> `Scheme.size X ≤ Scheme.size S`.

```lean
theorem Scheme.size_le_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [CompactSpace X] :
    Scheme.size X ≤ Scheme.size S
```

## Tag 04VA, a lemma

[Tag 04VA](https://stacks.math.columbia.edu/tag/04VA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_le_of_mono_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Monomorphism.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Monomorphism.lean#L345).

> If `f : X ⟶ Y` is a quasi-compact monomorphism of schemes, then `size X ≤ size Y`.

```lean
theorem Scheme.size_le_of_mono_quasiCompact
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Mono f] [QuasiCompact f] :
    X.size ≤ Y.size
```

**`AlgebraicGeometry.Scheme.size_le_of_mono_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Monomorphism.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Monomorphism.lean#L356).

> If `f : X ⟶ Y` is a monomorphism of schemes which is locally of finite presentation, then
> `size X ≤ size Y`.

```lean
theorem Scheme.size_le_of_mono_locallyOfFinitePresentation
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Mono f] [LocallyOfFinitePresentation f] :
    X.size ≤ Y.size
```

## Tag 000R, a lemma

[Tag 000R](https://stacks.math.columbia.edu/tag/000R) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_pullback_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L123). The attribute's comment: “(1)”.

> The fibre product of two objects of `Sch_κ` over any base, which need not lie in `Sch_κ`, is
> again an object of `Sch_κ`.

```lean
theorem Scheme.size_pullback_lt {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    (hX : X.size < κ) (hY : Y.size < κ) : (pullback f g).size < κ
```

**`AlgebraicGeometry.Scheme.size_sigmaObj_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L132). The attribute's comment: “(2)”.

> If `κ` is uncountable of uncountable cofinality, the coproduct of an at most countable family
> of objects of `Sch_κ` is again an object of `Sch_κ`.

```lean
theorem Scheme.size_sigmaObj_lt (hκ : ℵ₀ < κ) (hcof : ℵ₀ < κ.ord.cof) {ι : Type u}
    (hι : #ι ≤ ℵ₀) (Y : ι → Scheme.{u}) (hY : ∀ i, (Y i).size < κ) : (∐ Y).size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_mono_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L150). The attribute's comment: “(8)”.

> The source of a quasi-compact monomorphism into an object of `Sch_κ` is an object of
> `Sch_κ`.

```lean
theorem Scheme.size_lt_of_mono_quasiCompact {X Y : Scheme.{u}} (f : X ⟶ Y) [Mono f]
    [QuasiCompact f] (hY : Y.size < κ) : X.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_mono_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L157). The attribute's comment: “(8)”.

> The source of a monomorphism locally of finite presentation into an object of `Sch_κ` is an
> object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_mono_locallyOfFinitePresentation {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Mono f] [LocallyOfFinitePresentation f] (hY : Y.size < κ) : X.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L163). The attribute's comment: “(3)”.

> The source of an open immersion into an object of `Sch_κ` is an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_isOpenImmersion {U S : Scheme.{u}} (f : U ⟶ S)
    [IsOpenImmersion f] (hS : S.size < κ) : U.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L169). The attribute's comment: “(4)”.

> The source of a closed immersion into an object of `Sch_κ` is an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_isClosedImmersion {T S : Scheme.{u}} (f : T ⟶ S)
    [IsClosedImmersion f] (hS : S.size < κ) : T.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L179). The attribute's comment: “(6)”.

> Let `S` be a scheme with an open covering `S = ⋃ i, U i` and let `T` be an object of `Sch_κ`
> such that the index type and every member of the covering are bounded by `size(T) ^ ℵ₀`. Then `S`
> is an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_openCover (hκ : ℵ₀ < κ) (hsl : Cardinal.IsStrongPrelimit κ)
    {S : Scheme.{u}} {I : Type u} [Nonempty I] (U : I → S.Opens) (hcov : ⨆ i, U i = ⊤)
    {T : Scheme.{u}} (hT : T.size < κ) (hI : #I ≤ T.size ^ ℵ₀)
    (hU : ∀ i, (↑(U i) : Scheme.{u}).size ≤ T.size ^ ℵ₀) : S.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_locallyOfFiniteType_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L204). The attribute's comment: “(5)”.

> The source of a finite type morphism (locally of finite type and quasi-compact) into an object
> of `Sch_κ` is an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_locallyOfFiniteType_of_quasiCompact {T S : Scheme.{u}} (f : T ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (hS : S.size < κ) : T.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_locallyOfFiniteType_of_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L214). The attribute's comment: “(7)”.

> Let `f : T ⟶ S` be locally of finite type with `S` an object of `Sch_κ`, and suppose `T` has an
> affine open covering indexed by a type of cardinality at most `size(S) ^ ℵ₀`. Then `T` is an object
> of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_locallyOfFiniteType_of_affineCover (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) {T S : Scheme.{u}} (f : T ⟶ S)
    [LocallyOfFiniteType f] {I : Type u} [Nonempty I] (V : I → T.affineOpens)
    (hcov : ⨆ i, (V i).1 = ⊤) (hI : #I ≤ S.size ^ ℵ₀) (hS : S.size < κ) : T.size < κ
```

**`AlgebraicGeometry.Scheme.size_lt_of_isAffine_of_mk_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L228). The attribute's comment: “(9)”.

> An affine scheme `S` whose ring of global sections has cardinality at most
> `Bound(size T) = size(T) ^ ℵ₀` for some object `T` of `Sch_κ` is itself an object of `Sch_κ`.

```lean
theorem Scheme.size_lt_of_isAffine_of_mk_le (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) {S T : Scheme.{u}} [IsAffine S] (hT : T.size < κ)
    (h : Cardinal.mk Γ(S, ⊤) ≤ T.size ^ ℵ₀) : S.size < κ
```

**`AlgebraicGeometry.Scheme.size_Spec_lt_of_mk_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L241). The attribute's comment: “(9)”.

> If `#R ≤ Bound(size T) = size(T) ^ ℵ₀` for some object `T` of `Sch_κ`, then `Spec R` is an
> object of `Sch_κ`.

```lean
theorem Scheme.size_Spec_lt_of_mk_le (hκ : ℵ₀ < κ) (hsl : Cardinal.IsStrongPrelimit κ)
    (R : CommRingCat.{u}) {T : Scheme.{u}} (hT : T.size < κ)
    (h : Cardinal.mk R ≤ T.size ^ ℵ₀) : (Spec R).size < κ
```

**`AlgebraicGeometry.Scheme.size_Spec_lt_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L264). The attribute's comment: “(9)(b)”.

> For an object `Spec R` of `Sch_κ` and a finite type `R`-algebra `A`, the scheme `Spec A` is an
> object of `Sch_κ`.

```lean
theorem Scheme.size_Spec_lt_of_finiteType (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) (R A : Type u) [CommRing R] [CommRing A]
    [Algebra R A] [Algebra.FiniteType R A] (hR : (Spec (CommRingCat.of R)).size < κ) :
    (Spec (CommRingCat.of A)).size < κ
```

**`AlgebraicGeometry.Scheme.size_Spec_lt_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L273). The attribute's comment: “(9)(c)”.

> For an object `Spec R` of `Sch_κ` and a localization `A` of `R` at a submonoid, the scheme
> `Spec A` is an object of `Sch_κ`.

```lean
theorem Scheme.size_Spec_lt_of_isLocalization (hκ : ℵ₀ < κ)
    (hsl : Cardinal.IsStrongPrelimit κ) {R : Type u} [CommRing R] (M : Submonoid R)
    (A : Type u) [CommRing A] [Algebra R A] [IsLocalization M A]
    (hR : (Spec (CommRingCat.of R)).size < κ) : (Spec (CommRingCat.of A)).size < κ
```

**`AlgebraicGeometry.Scheme.size_Spec_lt_of_subring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Cutoff.lean#L282). The attribute's comment: “(9)(e)”.

> For an object `Spec R` of `Sch_κ` and a subring `R' ⊆ R`, the scheme `Spec R'` is an object of
> `Sch_κ`.

```lean
theorem Scheme.size_Spec_lt_of_subring (hκ : ℵ₀ < κ) (hsl : Cardinal.IsStrongPrelimit κ)
    {R : Type u} [CommRing R] (R' : Subring R)
    (hR : (Spec (CommRingCat.of R)).size < κ) : (Spec (CommRingCat.of R')).size < κ
```

**`AlgebraicGeometry.Scheme.size_sigmaObj_lt_of_lt_cof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductCutoff.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductCutoff.lean#L65). The attribute's comment: “(2), index type below the cofinality”.

> **Stacks 000R (2)** at an arbitrary index type. The coproduct of a family of objects of
> `Sch_κ` indexed by a type smaller than the cofinality of `κ` is again an object of `Sch_κ`.
>
> The hypothesis on the index type is what bounds the supremum of the sizes; the index type's own
> cardinality is then below `κ` because the cofinality of an ordinal is at most the ordinal.

```lean
theorem Scheme.size_sigmaObj_lt_of_lt_cof (hκ : ℵ₀ < κ) {ι : Type u} (hι : #ι < κ.ord.cof)
    (Y : ι → Scheme.{u}) (hY : ∀ i, (Y i).size < κ) : (∐ Y).size < κ
```

**`AlgebraicGeometry.Scheme.size_sigmaObj_lt_of_forall_size_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductCutoff.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductCutoff.lean#L81). The attribute's comment: “(2), uniformly bounded family at an index type below the cutoff”.

> **Stacks 000R (2) for a family of uniformly bounded size.** The coproduct of a family of
> objects of `Sch_κ` indexed by a type of cardinality below `κ` is again an object of `Sch_κ` as
> soon as the sizes of its members admit *one* bound below `κ`.
>
> The cofinality hypothesis of `AlgebraicGeometry.Scheme.size_sigmaObj_lt_of_lt_cof` is there only
> to bound the supremum `⨆ i, size (Y i)`, and a uniform bound does that directly. This is the
> form needed by a family indexed by the points of a scheme of the site — a set of size below `κ`
> whose cardinality need not be below `cof κ` — whose members are cut out of affine opens of one
> fixed scheme, so that their sizes are bounded in terms of that one scheme's.

```lean
theorem Scheme.size_sigmaObj_lt_of_forall_size_le (hκ : ℵ₀ < κ) {ι : Type u} (hι : #ι < κ)
    (Y : ι → Scheme.{u}) (c : Cardinal.{u}) (hc : c < κ) (hY : ∀ i, (Y i).size ≤ c) :
    (∐ Y).size < κ
```

**`AlgebraicGeometry.BigFppfSite.contains_spec_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean#L59). The attribute's comment: “(9), for a tensor product”.

> The spectrum of a tensor product of two contained spectra is contained.

```lean
theorem contains_spec_tensorProduct (B : BigFppfSite.{u}) {R A C : Type u}
    [CommRing R] [CommRing A] [CommRing C] [Algebra R A] [Algebra R C]
    (hA : B.Contains (Spec (.of A))) (hC : B.Contains (Spec (.of C))) :
    B.Contains (Spec (.of (A ⊗[R] C)))
```

**`AlgebraicGeometry.BigFppfSite.contains_spec_algebraicClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean#L69). The attribute's comment: “(9), for an algebraic closure”.

> The spectrum of an algebraic closure of a contained field is contained.

```lean
theorem contains_spec_algebraicClosure (B : BigFppfSite.{u}) {K : Type u} [Field K]
    (hK : B.Contains (Spec (.of K))) :
    B.Contains (Spec (.of (AlgebraicClosure K)))
```

**`AlgebraicGeometry.BigFppfSite.contains_spec_residueField_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean#L78). The attribute's comment: “(9), for the residue field of a prime”.

> The spectrum of the residue field of a prime of a contained spectrum is contained.

```lean
theorem contains_spec_residueField_atPrime (B : BigFppfSite.{u}) {A : Type u} [CommRing A]
    (hA : B.Contains (Spec (.of A))) (p : Ideal A) [p.IsPrime] :
    B.Contains (Spec (.of (IsLocalRing.ResidueField (Localization.AtPrime p))))
```

**`AlgebraicGeometry.BigFppfSite.contains_spec_algebraicClosure_residueField_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrimeResidueFieldSite.lean#L93). The attribute's comment: “(9), for the algebraic closure of the residue field of a prime of a tensor product”.

> For algebras `A` and `C` over `R` whose spectra are objects of the site and a prime `𝔰` of
> `A ⊗_R C`, the spectrum of an algebraic closure of the residue field of `𝔰` is an object of the
> site.

```lean
theorem contains_spec_algebraicClosure_residueField_tensorProduct (B : BigFppfSite.{u})
    {R A C : Type u} [CommRing R] [CommRing A] [CommRing C] [Algebra R A] [Algebra R C]
    (hA : B.Contains (Spec (.of A))) (hC : B.Contains (Spec (.of C)))
    (s : Ideal (A ⊗[R] C)) [s.IsPrime] :
    B.Contains (Spec (.of (AlgebraicClosure
      (IsLocalRing.ResidueField (Localization.AtPrime s)))))
```

## Tag 0AHK, a lemma

[Tag 0AHK](https://stacks.math.columbia.edu/tag/0AHK) in the Stacks Project.

**`AlgebraicGeometry.Scheme.size_le_of_fpqc_factorsThrough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Coverings.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Coverings.lean#L287).

> **Stacks 0AHK.** Let `f : X ⟶ Y` be a morphism of schemes. If there is an fpqc
> covering `{g j : Y' j ⟶ Y}` of `Y` such that every `g j` factors through `f`, then
> `Y.size ≤ X.size`.

```lean
theorem Scheme.size_le_of_fpqc_factorsThrough {X Y : Scheme} (f : X ⟶ Y)
    {J : Type*} (Y' : J → Scheme) (g : ∀ j, Y' j ⟶ Y)
    (hcov : IsFpqcCovering Y' g)
    (hfac : ∀ j, ∃ h : Y' j ⟶ X, h ≫ f = g j) :
    Scheme.size Y ≤ Scheme.size X
```

## Tag 0AHL, a lemma

[Tag 0AHL](https://stacks.math.columbia.edu/tag/0AHL) in the Stacks Project.

**`exists_fppf_refinement_schemeSize_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Size/Coverings.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Size/Coverings.lean#L409).

> **Stacks 0AHL.** Every fppf covering `𝒞` of a scheme `X` is refined by an fppf covering
> `𝒲` of `X` indexed in the universe of `X` whose total space is small: the coproduct of the
> members of `𝒲` satisfies `Scheme.size (∐ 𝒲.X) ≤ Scheme.size X`.

```lean
theorem exists_fppf_refinement_schemeSize_le (X : Scheme.{u}) (𝒞 : FppfCovering.{v} X) :
    ∃ 𝒲 : FppfCovering.{u} X,
      𝒲.IsRefinement 𝒞 ∧ Scheme.size (∐ 𝒲.X) ≤ Scheme.size X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.9, Tag 000H](https://stacks.math.columbia.edu/tag/000H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
