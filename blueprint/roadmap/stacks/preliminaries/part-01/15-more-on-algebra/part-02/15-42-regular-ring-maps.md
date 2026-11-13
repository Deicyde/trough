---
declaration: section
origin: cited
lean: IsRegularRingHom, isRegularRingHom_tfae_localizations, isRegularRingHom_baseChange, isRegularRingHom_comp, isRegularRingHom_of_filteredColimit_smooth, isRegularRingHom_iff_isSeparableExtension, isRegularRingHom_of_comp_of_flat_of_surjectiveOnSpec
statement: formalized
proof: formalized
---

# 15.42 Regular ring maps

Section 15.42 of the Stacks Project, [Tag 07BY](https://stacks.math.columbia.edu/tag/07BY). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07BZ, a definition

[Tag 07BZ](https://stacks.math.columbia.edu/tag/07BZ) in the Stacks Project.

**`IsRegularRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L92).

> A ring homomorphism is *regular* if it is flat and, over every prime of its source, its
> residue-field fibre is Noetherian and geometrically regular over that residue field.

```lean
public def IsRegularRingHom {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) : Prop
```

## Tag 07C0, a lemma

[Tag 07C0](https://stacks.math.columbia.edu/tag/07C0) in the Stacks Project.

**`isRegularRingHom_tfae_localizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L469).

> A ring homomorphism with Noetherian target is regular if and only if all its induced maps on
> local rings at corresponding prime ideals are regular, and if and only if this holds for
> maximal ideals of the target and their contractions.

```lean
public theorem isRegularRingHom_tfae_localizations
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) [IsNoetherianRing S] :
    List.TFAE [
      IsRegularRingHom f,
      ∀ (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] (h : p = q.comap f),
        IsRegularRingHom (Localization.localRingHom p q f h),
      ∀ (m : Ideal R) [m.IsPrime] (m' : Ideal S) [m'.IsMaximal]
        (h : m = m'.comap f),
        IsRegularRingHom (Localization.localRingHom m m' f h)]
```

## Tag 07C1, a lemma

[Tag 07C1](https://stacks.math.columbia.edu/tag/07C1) in the Stacks Project.

**`isRegularRingHom_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L554).

> A finite-type base change of a regular ring homomorphism is regular.

```lean
public theorem isRegularRingHom_baseChange
    {R : Type u} {Λ : Type v} {R' : Type w}
    [CommRing R] [CommRing Λ] [CommRing R'] [Algebra R Λ] [Algebra R R']
    [Algebra.FiniteType R R']
    (h : IsRegularRingHom (algebraMap R Λ)) :
    IsRegularRingHom
      (Algebra.TensorProduct.includeRight (R := R) (A := Λ) (B := R')).toRingHom
```

## Tag 07QI, a lemma

[Tag 07QI](https://stacks.math.columbia.edu/tag/07QI) in the Stacks Project.

**`isRegularRingHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 704](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L704).

> The composite of two regular ring homomorphisms is regular if all its fibres are
> Noetherian.

```lean
public theorem isRegularRingHom_comp
    {A : Type u} {B : Type v} {C : Type w} [CommRing A] [CommRing B] [CommRing C]
    (f : A →+* B) (g : B →+* C)
    (hf : IsRegularRingHom f) (hg : IsRegularRingHom g)
    (hNoetherian : ∀ (p : Ideal A) [p.IsPrime],
      let : Algebra A C := (g.comp f).toAlgebra
      IsNoetherianRing (p.Fiber C)) :
    IsRegularRingHom (g.comp f)
```

## Tag 07EP, a lemma

[Tag 07EP](https://stacks.math.columbia.edu/tag/07EP) in the Stacks Project.

**`isRegularRingHom_of_filteredColimit_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 1181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L1181).

> The colimit of a small nonempty directed system of smooth `R`-algebras, computed on
> underlying sets, whose residue-field fibres are Noetherian is regular over `R`.

```lean
public theorem isRegularRingHom_of_filteredColimit_smooth
    {R : Type u} [CommRing R]
    {J : Type w} [Preorder J] [IsDirectedOrder J] [Nonempty J] [Small.{max u v} J]
    (F : J ⥤ CommAlgCat.{v} R) (c : Cocone F) (hc : IsColimit c)
    [PreservesColimit (F ⋙ forget₂ (CommAlgCat.{v} R) CommRingCat.{v})
      (forget CommRingCat.{v})]
    (hsm : ∀ j, Algebra.Smooth R (F.obj j))
    (hnoeth : ∀ (p : Ideal R) [p.IsPrime], IsNoetherianRing (p.Fiber c.pt)) :
    IsRegularRingHom (algebraMap R c.pt)
```

## Tag 07EQ, a lemma

[Tag 07EQ](https://stacks.math.columbia.edu/tag/07EQ) in the Stacks Project.

**`isRegularRingHom_iff_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 1292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L1292).

> A field extension is a regular ring map if and only if it is separable.

```lean
public theorem isRegularRingHom_iff_isSeparableExtension (k : Type u) (K : Type v)
    [Field k] [Field K] [Algebra k K] :
    IsRegularRingHom (algebraMap k K) ↔ Algebra.IsSeparableExtension k K
```

## Tag 07NT, a lemma

[Tag 07NT](https://stacks.math.columbia.edu/tag/07NT) in the Stacks Project.

**`isRegularRingHom_of_comp_of_flat_of_surjectiveOnSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/RegularRingHom.lean, line 1314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/RegularRingHom.lean#L1314).

> If a composite ring homomorphism is regular and the second homomorphism is flat and
> surjective on prime spectra, then the first homomorphism is regular.

```lean
public theorem isRegularRingHom_of_comp_of_flat_of_surjectiveOnSpec
    {A : Type u} {B : Type v} {C : Type w}
    [CommRing A] [CommRing B] [CommRing C]
    (f : A →+* B) (g : B →+* C)
    (hgf : IsRegularRingHom (g.comp f))
    (hgflat : g.Flat)
    (hgsurj : Function.Surjective (PrimeSpectrum.comap g)) :
    IsRegularRingHom f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.42, Tag 07BY](https://stacks.math.columbia.edu/tag/07BY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
