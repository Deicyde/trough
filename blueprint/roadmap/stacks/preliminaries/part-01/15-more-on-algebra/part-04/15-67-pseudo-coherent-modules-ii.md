---
declaration: section
origin: cited
lean: StacksDraft.PseudoCoherence.colimit_ext_comparison_isIso_of_lt_and_mono, StacksDraft.PseudoCoherence.isPseudoCoherentFrom_iff_colimit_ext_comparison, StacksDraft.PseudoCoherence.canonicalExtTensorComparison_bijective, StacksDraft.PseudoCoherence.baseChange_ext_bijective_of_pseudoCoherent, StacksDraft.PseudoCoherence.pseudoCoherent_iff_derivedTensor_preserves_products, StacksDraft.PseudoCoherence.exists_finitelyPresented_module_mono_homology, StacksDraft.PseudoCoherence.exists_finite_module_detecting_homology_mod_ideal
statement: formalized
proof: formalized
---

# 15.67 Pseudo-coherent modules, II

Section 15.67 of the Stacks Project, [Tag 0G8V](https://stacks.math.columbia.edu/tag/0G8V). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G8W, a lemma

[Tag 0G8W](https://stacks.math.columbia.edu/tag/0G8W) in the Stacks Project.

**`StacksDraft.PseudoCoherence.colimit_ext_comparison_isIso_of_lt_and_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Ext.lean, line 589](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/Ext.lean#L589).

> **Stacks 0G8W.** If `K` is `m`-pseudo-coherent, then the canonical map from the
> filtered colimit of `Extⁿ(K, Mᵢ)` to `Extⁿ(K, colim Mᵢ)` is an isomorphism for
> `n < -m`, and is a monomorphism for `n = -m`.

```lean
theorem colimit_ext_comparison_isIso_of_lt_and_mono
    {R : Type u} [Ring R] {ι : Type v} [Category.{v} ι] [IsFiltered ι]
    (M : ι ⥤ ModuleCat.{v} R) (K : DerivedCategory (ModuleCat.{v} R)) (m : ℤ)
    (hK : IsPseudoCoherentFrom K m) :
    let extFunctor (n : ℤ) :=
      DerivedCategory.singleFunctor (ModuleCat.{v} R) 0 ⋙
        shiftFunctor (DerivedCategory (ModuleCat.{v} R)) n ⋙
        preadditiveCoyoneda.obj (Opposite.op K)
    (∀ n : ℤ, n < -m →
      IsIso (colimit.desc (M ⋙ extFunctor n)
        ((extFunctor n).mapCocone (colimit.cocone M)))) ∧
      Mono (colimit.desc (M ⋙ extFunctor (-m))
        ((extFunctor (-m)).mapCocone (colimit.cocone M)))
```

## Tag 0G8X, a lemma

[Tag 0G8X](https://stacks.math.columbia.edu/tag/0G8X) in the Stacks Project.

**`StacksDraft.PseudoCoherence.isPseudoCoherentFrom_iff_colimit_ext_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Ext.lean, line 1246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/Ext.lean#L1246).

> **Stacks 0G8X.** A cohomologically bounded-above object `K` is `m`-pseudo-coherent if and
> only if, for every filtered diagram of modules, the canonical map from the filtered colimit of
> `Extⁿ(K, -)` to its value on the colimit is an isomorphism for `n < -m` and a monomorphism for
> `n = -m`.

```lean
theorem isPseudoCoherentFrom_iff_colimit_ext_comparison
    {R : Type u} [Ring R] [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R)) (m : ℤ)
    (hK : ∃ n : ℤ, K.IsLE n) :
    IsPseudoCoherentFrom K m ↔
      ∀ (ι : Type v) [Category.{v} ι] [IsFiltered ι]
        (M : ι ⥤ ModuleCat.{v} R),
        let extFunctor (n : ℤ) :=
          DerivedCategory.singleFunctor (ModuleCat.{v} R) 0 ⋙
            shiftFunctor (DerivedCategory (ModuleCat.{v} R)) n ⋙
            preadditiveCoyoneda.obj (Opposite.op K)
        (∀ n : ℤ, n < -m →
          IsIso (colimit.desc (M ⋙ extFunctor n)
            ((extFunctor n).mapCocone (colimit.cocone M)))) ∧
          Mono (colimit.desc (M ⋙ extFunctor (-m))
            ((extFunctor (-m)).mapCocone (colimit.cocone M)))
```

## Tag 087Q, a lemma

[Tag 087Q](https://stacks.math.columbia.edu/tag/087Q) in the Stacks Project.

**`StacksDraft.PseudoCoherence.canonicalExtTensorComparison_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/HomFlat.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/HomFlat.lean#L453). References: EGA 0 (6.2.2); SGA 4 V (8.2.10), “modules over a ring”; SGA 6 I (3.7), “affine case, modules”.

> **Stacks 087Q.** The canonical Hom--tensor map is bijective for a finitely presented
> source and flat tensor factor. The canonical Ext--tensor map is bijective below the
> pseudo-coherence cutoff for a flat tensor factor.

```lean
theorem canonicalExtTensorComparison_bijective [HasDerivedCategory (ModuleCat.{v} R)] :
    ∀ (M : Type v) (N : Type w) (L : Type x)
        [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
        [AddCommGroup L] [Module R L] [Module.Flat R L],
        (Module.FinitePresentation R M →
          Function.Bijective
            (TensorProduct.rTensorHomToHomRTensor (RingHom.id R) M N L)) ∧
        (∀ (d : ℕ), IsModulePseudoCoherentFrom (R := R) M (-(d : ℤ)) →
          ∀ i < d, Function.Bijective
            (canonicalExtTensorComparison R (ModuleCat.of R (ULift.{max u v w x} M))
              (ModuleCat.of R (ULift.{max u v w x} N))
              (ModuleCat.of R (ULift.{max u v w x} L)) i))
```

## Tag 087R, a lemma

[Tag 087R](https://stacks.math.columbia.edu/tag/087R) in the Stacks Project.

**`StacksDraft.PseudoCoherence.baseChange_ext_bijective_of_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/HomFlat.lean, line 637](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/HomFlat.lean#L637).

> **Stacks 087R.** The canonical Ext base-change map is bijective in degree zero for finitely
> presented modules, below the pseudo-coherence cutoff, and in every degree for finite modules
> over a Noetherian ring.
>
> The maps `η` and `t` are characterized on original elements by `m ↦ 1 ⊗ m` and
> `n ⊗ s ↦ s ⊗ n`. The equation `c.comp β = a` and its uniqueness clause specify the canonical
> comparison in every degree. The commuting square using `uliftExtLinearEquiv₀` transports `β`
> in degree zero to `homBaseChangeComparison` on the original modules.

```lean
theorem baseChange_ext_bijective_of_pseudoCoherent
    (R : Type uR) (S : Type uS) (M : Type uM) (N : Type uN)
    [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S]
    [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    [HasDerivedCategory (ModuleCat.{uM} R)] :
    let RM := ModuleCat.of R (ULift.{max uR uS uM uN} M)
    let RN := ModuleCat.of R (ULift.{max uR uS uM uN} N)
    let L := ModuleCat.of R (ULift.{max uR uS uM uN} S)
    let SM := ModuleCat.of S (ULift.{max uR uS uM uN} (S ⊗[R] M))
    let SN := ModuleCat.of S (ULift.{max uR uS uM uN} (S ⊗[R] N))
    let E := (ModuleCat.restrictScalars (algebraMap R S)).obj SN
    ∃ (η : RM ⟶ (ModuleCat.restrictScalars (algebraMap R S)).obj SM)
        (t : ModuleCat.of R (RN ⊗[R] L) ⟶ E),
      (∀ m : M, η (ULift.up m) = ULift.up ((1 : S) ⊗ₜ[R] m)) ∧
      (∀ (n : N) (s : S), t (ULift.up n ⊗ₜ[R] ULift.up s) =
        ULift.up (s ⊗ₜ[R] n)) ∧
      (∀ t' : ModuleCat.of R (RN ⊗[R] L) ⟶ E,
        (∀ (n : N) (s : S), t' (ULift.up n ⊗ₜ[R] ULift.up s) =
          ULift.up (s ⊗ₜ[R] n)) → t' = t) ∧
      ∀ i : ℕ,
        let c : Ext SM SN i →+ Ext RM E i :=
          ((Ext.mk₀ η).precomp E (zero_add i)).comp
            ((ModuleCat.restrictScalars (algebraMap R S)).mapExtAddHom SM SN i)
        let a : (Ext RM RN i) ⊗[R] S →+ Ext RM E i :=
          (((Ext.mk₀ t).postcomp RM (add_zero i)).comp
            (canonicalExtTensorComparison R RM RN L i).toAddMonoidHom).comp
              (TensorProduct.map (LinearMap.id : Ext RM RN i →ₗ[R] Ext RM RN i)
                (ULift.moduleEquiv.symm.toLinearMap : S →ₗ[R] L)).toAddMonoidHom
        ∃ β : (Ext RM RN i) ⊗[R] S →+ Ext SM SN i,
          c.comp β = a ∧
          (∀ γ : (Ext RM RN i) ⊗[R] S →+ Ext SM SN i,
            c.comp γ = a → γ = β) ∧
          (∀ (e : Ext RM RN i) (s r : S),
            β (e ⊗ₜ[R] (r * s)) = r • β (e ⊗ₜ[R] s)) ∧
          (∀ h : i = 0, ∀ x : (Ext RM RN 0) ⊗[R] S,
            uliftExtLinearEquiv₀.{uS, max uS uM, max uS uN, uR} S (S ⊗[R] M) (S ⊗[R] N)
                ((h ▸ β) x) =
              homBaseChangeComparison R S M N
                (TensorProduct.congr (uliftExtLinearEquiv₀.{uR, uM, uN, uS} R M N)
                  (LinearEquiv.refl R S) x)) ∧
          (i = 0 → Module.FinitePresentation R M → Function.Bijective β) ∧
          (∀ d : ℕ, IsModulePseudoCoherentFrom (R := R) M (-(d : ℤ)) →
            i < d → Function.Bijective β) ∧
          (IsNoetherianRing R → Module.Finite R M → Function.Bijective β)
```

## Tag 0CYB, a lemma

[Tag 0CYB](https://stacks.math.columbia.edu/tag/0CYB) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherent_iff_derivedTensor_preserves_products`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Products/Characterization.lean, line 731](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/Products/Characterization.lean#L731).

> **Stacks 0CYB.** Pseudo-coherence of a bounded-above complex is equivalent to derived
> tensor product commuting with arbitrary products; the degreewise variants characterize
> `m`-pseudo-coherence.

```lean
theorem pseudoCoherent_iff_derivedTensor_preserves_products
    (T : DerivedTensorProduct.{u, v, w} R) (P : DerivedProducts.{u, v, w} R)
    (K : DerivedCategory.Minus (ModuleCat.{max v w} (SmallRing.{u, v, w} R))) (m : ℤ) :
    List.TFAE [
      IsPseudoCoherent K.obj,
      ∀ (A : Type (max v w)) (Q : A → ModuleCat.{max v w} (SmallRing.{u, v, w} R)),
        IsIso (tensorProductComparison T P K.obj A Q),
      ∀ (A : Type (max v w)) (Q : ModuleCat.{max v w} (SmallRing.{u, v, w} R)),
        IsIso (tensorPowerComparison T P K.obj A Q),
      ∀ A : Type (max v w), IsIso (tensorRingPowerComparison T P K.obj A)] ∧
    List.TFAE [
      IsPseudoCoherentFrom K.obj m,
      ∀ (A : Type (max v w)) (Q : A → ModuleCat.{max v w} (SmallRing.{u, v, w} R)),
        (∀ i : ℤ, m < i → IsIso ((DerivedCategory.homologyFunctor _ i).map
          (tensorProductComparison T P K.obj A Q))) ∧
        Epi ((DerivedCategory.homologyFunctor _ m).map
          (tensorProductComparison T P K.obj A Q)),
      ∀ (A : Type (max v w)) (Q : ModuleCat.{max v w} (SmallRing.{u, v, w} R)),
        (∀ i : ℤ, m < i → IsIso ((DerivedCategory.homologyFunctor _ i).map
          (tensorPowerComparison T P K.obj A Q))) ∧
        Epi ((DerivedCategory.homologyFunctor _ m).map
          (tensorPowerComparison T P K.obj A Q)),
      ∀ A : Type (max v w),
        (∀ i : ℤ, m < i → IsIso ((DerivedCategory.homologyFunctor _ i).map
          (tensorRingPowerComparison T P K.obj A))) ∧
        Epi ((DerivedCategory.homologyFunctor _ m).map
          (tensorRingPowerComparison T P K.obj A))]
```

## Tag 0G8Y, a lemma

[Tag 0G8Y](https://stacks.math.columbia.edu/tag/0G8Y) in the Stacks Project.

**`StacksDraft.PseudoCoherence.exists_finitelyPresented_module_mono_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Ext.lean, line 1319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/Ext.lean#L1319).

> **Stacks 0G8Y.** For every degree `i`, the degree-`i` cohomology of a pseudo-coherent
> object of `D(R)` embeds in a finitely presented `R`-module, and the embedding is induced by a
> morphism from the object to that module placed in degree `i`.

```lean
theorem exists_finitelyPresented_module_mono_homology {R : Type u} [Ring R]
    (K : DerivedCategory (ModuleCat.{v} R)) (hK : IsPseudoCoherent K) (i : ℤ) :
    ∃ (M : ModuleCat.{v} R), Module.FinitePresentation R M ∧
      ∃ f : K ⟶ (DerivedCategory.singleFunctor (ModuleCat.{v} R) i).obj M,
        Mono ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).map f ≫
          (DerivedCategory.singleFunctorCompHomologyFunctorIso
            (ModuleCat.{v} R) i).hom.app M)
```

## Tag 0A7D, a lemma

[Tag 0A7D](https://stacks.math.columbia.edu/tag/0A7D) in the Stacks Project.

**`StacksDraft.PseudoCoherence.exists_finite_module_detecting_homology_mod_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Noetherian.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/Noetherian.lean#L74).

> **Stacks 0A7D.** If degree-`i` cohomology of a pseudo-coherent complex over a Noetherian
> ring is nonzero modulo an ideal, it is detected by a map to a finite module annihilated by a
> power of that ideal, placed in degree `i`.

```lean
public theorem exists_finite_module_detecting_homology_mod_ideal
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : IsPseudoCoherent K)
    (m : Ideal A) (i : ℤ)
    (hi : Nontrivial
      (((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).obj K) ⧸
        (m • (⊤ : Submodule A
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).obj K))))) :
    ∃ (E : ModuleCat.{v} A), Module.Finite A E ∧
      (∃ n : ℕ, m ^ n • (⊤ : Submodule A E) = ⊥) ∧
      ∃ f : K ⟶ (DerivedCategory.singleFunctor (ModuleCat.{v} A) i).obj E,
        (DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).map f ≫
          (DerivedCategory.singleFunctorCompHomologyFunctorIso
            (ModuleCat.{v} A) i).hom.app E ≠ 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.67, Tag 0G8V](https://stacks.math.columbia.edu/tag/0G8V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
