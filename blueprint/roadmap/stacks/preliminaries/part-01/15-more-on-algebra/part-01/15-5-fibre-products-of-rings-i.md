---
declaration: section
origin: cited
lean: Algebra.FiniteType.pullback, RingFibreProduct.finiteType_of_pullback_pi, RingFibreProduct.isPullback_localization_away, ModuleGlueing.extensionOfScalarsToPullback, MilnorPatching.exists_rightAdjoint_extensionOfScalarsToPullback
statement: formalized
proof: formalized
---

# 15.5 Fibre products of rings, I

Section 15.5 of the Stacks Project, [Tag 08KG](https://stacks.math.columbia.edu/tag/08KG). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00IT, a lemma

[Tag 00IT](https://stacks.math.columbia.edu/tag/00IT) in the Stacks Project.

**`Algebra.FiniteType.pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FibreProduct.lean#L219).

> **Stacks Tag 00IT.** Let `R` be a Noetherian ring and let `f : A →ₐ[R] B`
> and `g : C →ₐ[R] B` be `R`-algebra maps. If `A` and `C` are of finite type over
> `R`, `f` is surjective, and `g` is a finite morphism (that is, `B` is finitely
> generated as a `C`-module), then the fibre product `A ×_B C` is of finite type
> over `R`.

```lean
theorem Algebra.FiniteType.pullback [IsNoetherianRing R] [Algebra.FiniteType R A]
    [Algebra.FiniteType R C] (f : A →ₐ[R] B) (g : C →ₐ[R] B) (hf : Function.Surjective f)
    (hBC : g.Finite) : Algebra.FiniteType R (f.pullback g)
```

## Tag 08NI, a lemma

[Tag 08NI](https://stacks.math.columbia.edu/tag/08NI) in the Stacks Project.

**`RingFibreProduct.finiteType_of_pullback_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FibreProduct.lean#L259).

> Stacks Tag 08NI: in a cartesian square formed from finite products of surjective maps of
> finite type algebras over a Noetherian ring, the lower right corner is of finite type.

```lean
public theorem finiteType_of_pullback_pi
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {I : Type*} [Finite I]
    {A B : I → Type*}
    [∀ i, CommRing (A i)] [∀ i, CommRing (B i)]
    [∀ i, Algebra R (A i)] [∀ i, Algebra R (B i)]
    {Q : Type*} [CommRing Q] [Algebra R Q]
    {P : Type*} [CommRing P] [Algebra R P]
    (φ : ∀ i, A i →ₐ[R] B i) (ψ : ∀ i, Q →ₐ[R] B i)
    (toA : P →ₐ[R] ∀ i, A i) (toQ : P →ₐ[R] Q)
    (e : P ≃ₐ[R]
      AlgHom.pullback
        (AlgHom.pi (fun i ↦ (φ i).comp (Pi.evalAlgHom R A i)))
        (AlgHom.pi ψ))
    (_he : ∀ p, (e p : (∀ i, A i) × Q) = (toA p, toQ p))
    (hφ : ∀ i, Function.Surjective (φ i))
    (hψ : ∀ i, Function.Surjective (ψ i))
    (hA : ∀ i, Algebra.FiniteType R (A i))
    (_hB : ∀ i, Algebra.FiniteType R (B i))
    (hQ : Algebra.FiniteType R Q) :
    Algebra.FiniteType R P
```

## Tag 01Z8, a lemma

[Tag 01Z8](https://stacks.math.columbia.edu/tag/01Z8) in the Stacks Project.

**`RingFibreProduct.isPullback_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FibreProduct/Localization.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FibreProduct/Localization.lean#L143).

> Let `B' = B ×_R R'` be a fibre product of commutative rings along `s : B → R` and
> `t : R' → R`, and let `h ∈ B'` map to `g ∈ B` and `f ∈ R'`, with `s g = t f`. Then the square
> of localizations `B'_h → B_g`, `B'_h → R'_f`, `B_g → R_{s g}`, `R'_f → R_{s g}` is again a
> pullback, that is, `B'_h ≅ B_g ×_{R_{s g}} R'_f`.

```lean
theorem isPullback_localization_away
    {R R' B B' : Type u}
    [CommRing R] [CommRing R'] [CommRing B] [CommRing B']
    (s : B →+* R) (t : R' →+* R)
    (πB : B' →+* B) (πR' : B' →+* R')
    (hPB : IsPullback (CommRingCat.ofHom πB) (CommRingCat.ofHom πR')
      (CommRingCat.ofHom s) (CommRingCat.ofHom t))
    (h : B') (g : B) (f : R')
    (hB : πB h = g) (hR' : πR' h = f) (hcompat : s g = t f) :
    IsPullback
      (CommRingCat.ofHom
        (Localization.awayLift ((algebraMap B (Localization.Away g)).comp πB) h (by
          rw [RingHom.comp_apply, hB]
          exact IsLocalization.Away.algebraMap_isUnit g)))
      (CommRingCat.ofHom
        (Localization.awayLift ((algebraMap R' (Localization.Away f)).comp πR') h (by
          rw [RingHom.comp_apply, hR']
          exact IsLocalization.Away.algebraMap_isUnit f)))
      (CommRingCat.ofHom (Localization.awayMap s g))
      (CommRingCat.ofHom
        (Localization.awayLift ((algebraMap R (Localization.Away (s g))).comp t) f (by
          rw [RingHom.comp_apply, ← hcompat]
          exact IsLocalization.Away.algebraMap_isUnit (s g))))
```

## Tag 0D2E, an equation

[Tag 0D2E](https://stacks.math.columbia.edu/tag/0D2E) in the Stacks Project.

**`ModuleGlueing.extensionOfScalarsToPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/CategoricalPullback.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/CategoricalPullback.lean#L96).

> A commutative square of commutative rings induces the
> extension-of-scalars functor
> `Mod B' ⟶ Mod B ×_(Mod A) Mod A'`. Its value at `L'` consists of the two scalar
> extensions of `L'` and their canonical identification after extending scalars to `A`.

```lean
noncomputable def extensionOfScalarsToPullback.{u, uB', uB, uA', uA}
    {B' : Type uB'} {B : Type uB} {A' : Type uA'} {A : Type uA}
    [CommRing B'] [CommRing B] [CommRing A'] [CommRing A]
    (toB : B' →+* B) (toA' : B' →+* A') (BtoA : B →+* A) (A'toA : A' →+* A)
    (comm : BtoA.comp toB = A'toA.comp toA') :
    ModuleCat.{max u uB uA' uA} B' ⥤
      CategoricalPullback (ModuleCat.extendScalars.{uB, uA, max u uB uA' uA} BtoA)
        (ModuleCat.extendScalars.{uA', uA, max u uB uA' uA} A'toA)
```

## Tag 0D2F, a lemma

[Tag 0D2F](https://stacks.math.columbia.edu/tag/0D2F) in the Stacks Project.

**`MilnorPatching.exists_rightAdjoint_extensionOfScalarsToPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/ModuleCategory.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/ModuleCategory.lean#L614).

> **Stacks Project, Tag 0D2F.** The extension-of-scalars functor associated to a commutative
> square of rings has a right adjoint.  Its value on `(N, M', φ)` is naturally the `B'`-module
> `N ×_φ M'` of compatible pairs.

```lean
public theorem exists_rightAdjoint_extensionOfScalarsToPullback
    {B' : Type uB'} {B : Type uB} {R' : Type uR'} {R : Type uR}
    [CommRing B'] [CommRing B] [CommRing R'] [CommRing R]
    (toB : B' →+* B) (toR' : B' →+* R') (BtoR : B →+* R) (R'toR : R' →+* R)
    (comm : BtoR.comp toB = R'toR.comp toR') :
    ∃ (F : CategoricalPullback (ModuleCat.extendScalars.{uB, uR, max u uB uR' uR} BtoR)
        (ModuleCat.extendScalars.{uR', uR, max u uB uR' uR} R'toR) ⥤ ModuleCat.{max u uB uR' uR} B')
      (e : ∀ X, F.obj X ≃ₗ[B']
        compatiblePairsModule.{u} toB toR' BtoR R'toR comm X)
      (adj : extensionOfScalarsToPullback.{u} toB toR' BtoR R'toR comm ⊣ F),
      (∀ {X Y} (f : X ⟶ Y) (p : F.obj X),
        (e Y (F.map f p)).1.1 = f.fst (e X p).1.1 ∧
          (e Y (F.map f p)).1.2 = f.snd (e X p).1.2) ∧
      ∀ (L : ModuleCat.{max u uB uR' uR} B') (X) (h : L ⟶ F.obj X) (l : L),
        (e X (h l)).1.1 =
            ((adj.homEquiv L X).symm h).fst ((1 : B) ⊗ₜ[B',toB] l) ∧
          (e X (h l)).1.2 =
            ((adj.homEquiv L X).symm h).snd ((1 : R') ⊗ₜ[B',toR'] l)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.5, Tag 08KG](https://stacks.math.columbia.edu/tag/08KG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
