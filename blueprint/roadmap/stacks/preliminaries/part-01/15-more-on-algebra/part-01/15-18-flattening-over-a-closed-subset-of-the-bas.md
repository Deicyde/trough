---
declaration: section
origin: cited
lean: Module.FlatAlongZeroLocus, Module.FlatAlongZeroLocus.baseChange, Module.FlatAlongZeroLocus.of_baseChange, Module.exists_flatAlongZeroLocus_baseChange_of_colimit
statement: formalized
proof: formalized
---

# 15.18 Flattening over a closed subset of the base

Section 15.18 of the Stacks Project, [Tag 05LK](https://stacks.math.columbia.edu/tag/05LK). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 052W, an equation

[Tag 052W](https://stacks.math.columbia.edu/tag/052W) in the Stacks Project.

**`Module.FlatAlongZeroLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean#L45).

> An `S`-module `M` is flat over `R` along the inverse image of the zero
> locus of an ideal `I` of `R` if the localization `M_q` is flat over `R` for every prime ideal `q`
> of `S` containing the extension of `I`.

```lean
def Module.FlatAlongZeroLocus
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (I : Ideal R) (M : Type w) [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M] : Prop
```

## Tag 052X, a lemma

[Tag 052X](https://stacks.math.columbia.edu/tag/052X) in the Stacks Project.

**`Module.FlatAlongZeroLocus.baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean#L57).

> Let `T` be a pushout of maps of commutative rings `R → S` and `R → R'`.
> If an `S`-module `M` is flat over `R` along the inverse image of the zero locus of `I`, and the
> extension of `I` to `R'` is contained in `I'`, then `T ⊗[S] M` is flat over `R'` along the
> inverse image of the zero locus of `I'`.

```lean
lemma Module.FlatAlongZeroLocus.baseChange
    (R : Type u) (S : Type v) (R' : Type w) (T : Type x)
    [CommRing R] [CommRing S] [CommRing R'] [CommRing T]
    [Algebra R S] [Algebra R R'] [Algebra R T] [Algebra S T] [Algebra R' T]
    [IsScalarTower R S T] [IsScalarTower R R' T] [Algebra.IsPushout R R' S T]
    (I : Ideal R) (I' : Ideal R')
    (M : Type*) [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    (hI : I.map (algebraMap R R') ≤ I')
    (hM : Module.FlatAlongZeroLocus R S I M) :
    Module.FlatAlongZeroLocus R' T I' (TensorProduct S T M)
```

## Tag 05LL, a lemma

[Tag 05LL](https://stacks.math.columbia.edu/tag/05LL) in the Stacks Project.

**`Module.FlatAlongZeroLocus.of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ClosedSubset/FlatAlongZeroLocus.lean#L345).

> Flatness along the inverse image of a closed subset descends after a
> base change which is surjective onto that closed subset and whose local rings there are flat
> over the original base.

```lean
theorem Module.FlatAlongZeroLocus.of_baseChange
    (R : Type u) (S : Type v) (R' : Type w) (M : Type x)
    [CommRing R] [CommRing S] [CommRing R'] [Algebra R S] [Algebra R R']
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    (I : Ideal R) (I' : Ideal R')
    (_hmap : I.map (algebraMap R R') ≤ I')
    (hsurj : ∀ (p : Ideal R), p.IsPrime → I ≤ p →
      ∃ (p' : Ideal R'), p'.IsPrime ∧ I' ≤ p' ∧
        p'.comap (algebraMap R R') = p)
    (hflat : ∀ (p' : Ideal R') [p'.IsPrime], I' ≤ p' →
      Module.Flat R (Localization.AtPrime p')) :
    letI := Algebra.TensorProduct.rightAlgebra (R := R) (A := S) (B := R')
    Module.FlatAlongZeroLocus R' (S ⊗[R] R') I'
      ((S ⊗[R] R') ⊗[S] M) →
      Module.FlatAlongZeroLocus R S I M
```

## Tag 05LM, a lemma

[Tag 05LM](https://stacks.math.columbia.edu/tag/05LM) in the Stacks Project.

**`Module.exists_flatAlongZeroLocus_baseChange_of_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ClosedSubset/ColimitDescent.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ClosedSubset/ColimitDescent.lean#L615).

> Flatness of a finitely presented module along the closed subset defined
> by a compatible family of ideals in a directed system descends from the colimit to one stage.

```lean
theorem Module.exists_flatAlongZeroLocus_baseChange_of_colimit
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S]
    (M : Type w) [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FinitePresentation S M]
    (Λ : Type u) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
    (A : Λ ⥤ CommAlgCat.{u} R) (I : ∀ i, Ideal (A.obj i))
    (hI : ∀ {i j : Λ} (hij : i ≤ j),
      Ideal.map (A.map (homOfLE hij)).hom.toRingHom (I i) ≤ I j)
    (hflat :
      let R' := (colimit A : CommAlgCat.{u} R)
      let S' := S ⊗[R] R'
      letI : Algebra R' S' := Algebra.TensorProduct.rightAlgebra
      Module.FlatAlongZeroLocus
        R' S'
        (⨆ i, Ideal.map (colimit.ι A i).hom.toRingHom (I i))
        (S' ⊗[S] M)) :
    ∃ i : Λ,
      let Sᵢ := S ⊗[R] (A.obj i)
      letI : Algebra (A.obj i) Sᵢ := Algebra.TensorProduct.rightAlgebra
      Module.FlatAlongZeroLocus
        (A.obj i) Sᵢ (I i) (Sᵢ ⊗[S] M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.18, Tag 05LK](https://stacks.math.columbia.edu/tag/05LK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
