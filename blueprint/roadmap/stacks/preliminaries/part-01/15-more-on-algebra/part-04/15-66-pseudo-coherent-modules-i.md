---
declaration: section
origin: cited
lean: StacksDraft.PseudoCoherence.HasFiniteFreeResolutionUpTo, StacksDraft.PseudoCoherence.IsPseudoCoherentFrom, StacksDraft.PseudoCoherence.IsPseudoCoherent, StacksDraft.PseudoCoherence.IsModulePseudoCoherentFrom, StacksDraft.PseudoCoherence.IsModulePseudoCoherent, PseudoCoherence.isPseudoCoherent_of_distinguished_one, PseudoCoherence.isPseudoCoherent_of_distinguished_two, PseudoCoherence.isPseudoCoherent_of_distinguished_three
statement: formalized
proof: formalized
---

# 15.66 Pseudo-coherent modules, I

Section 15.66 of the Stacks Project, [Tag 064N](https://stacks.math.columbia.edu/tag/064N). 19 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 064P, an equation

[Tag 064P](https://stacks.math.columbia.edu/tag/064P) in the Stacks Project.

**`StacksDraft.PseudoCoherence.HasFiniteFreeResolutionUpTo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Module.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Module.lean#L76).

> A module has a finite free resolution through degree `n` if there is an exact sequence
> `R^{a_n} → ⋯ → R^{a_0} → M → 0`. Exactness is required at `M` and at every finite free term
> except the leftmost one.

```lean
def HasFiniteFreeResolutionUpTo
    (R : Type u) [Ring R] (M : Type v) [AddCommGroup M] [Module R M] (n : ℕ) : Prop
```

## Tag 064Q, a definition

[Tag 064Q](https://stacks.math.columbia.edu/tag/064Q) in the Stacks Project.

**`StacksDraft.PseudoCoherence.IsPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/PseudoCoherent.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/PseudoCoherent.lean#L123). The attribute's comment: “(1)”. References: SGA 6 II (2.3.2).

> An object `K` of `D(R)` is *`m`-pseudo-coherent* when there is a bounded complex `E` of
> finite free `R`-modules and a morphism `α : Q(E) ⟶ K` in `D(R)`, where `Q` sends a complex to its
> image in the derived category, such that `Hⁱ(α)` is an isomorphism for every `i > m` and `Hᵐ(α)`
> is surjective.

```lean
def IsPseudoCoherentFrom (K : DerivedCategory (ModuleCat.{v} R)) (m : ℤ) : Prop
```

**`StacksDraft.PseudoCoherence.IsPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/PseudoCoherent.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/PseudoCoherent.lean#L132). The attribute's comment: “(2)”.

> An object `K` of `D(R)` is *pseudo-coherent* when it is represented by a bounded-above
> complex of finite free `R`-modules.

```lean
def IsPseudoCoherent (K : DerivedCategory (ModuleCat.{v} R)) : Prop
```

**`StacksDraft.PseudoCoherence.IsModulePseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/PseudoCoherent.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/PseudoCoherent.lean#L139). The attribute's comment: “(3)”.

> An `R`-module `M` is *`m`-pseudo-coherent* when the object of `D(R)` concentrated in
> degree `0` with value `M` is `m`-pseudo-coherent.

```lean
def IsModulePseudoCoherentFrom (M : Type v) [AddCommGroup M] [Module R M] (m : ℤ) : Prop
```

**`StacksDraft.PseudoCoherence.IsModulePseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/PseudoCoherent.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/PseudoCoherent.lean#L146). The attribute's comment: “(4)”.

> An `R`-module `M` is *pseudo-coherent* when the object of `D(R)` concentrated in degree `0`
> with value `M` is pseudo-coherent.

```lean
def IsModulePseudoCoherent (M : Type v) [AddCommGroup M] [Module R M] : Prop
```

## Tag 064R, a lemma

[Tag 064R](https://stacks.math.columbia.edu/tag/064R) in the Stacks Project.

**`PseudoCoherence.isPseudoCoherent_of_distinguished_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Triangle.lean, line 848](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Triangle.lean#L848). The attribute's comment: “(1)”. References: SGA 6 I (2.6), “special case”; SGA 6 III (1.4), “special case”.

> **Statement (1).** If `K` is `(m+1)`-pseudo-coherent and `L` is
> `m`-pseudo-coherent, and `(K, L, M, f, g, h)` is a distinguished triangle, then
> `M` is `m`-pseudo-coherent.
>
> Assembled from the three sub-lemmas above. The degree bookkeeping: with
> `α : Q P ⟶ K` iso on `H^i` (`i > m+1`)/epi on `H^{m+1}` and `β : Q E ⟶ L` iso on
> `H^i` (`i > m`)/epi on `H^m`, the cone `C` carries `μ = φ.hom₃ : Q C ⟶ M`. For
> `i > m`: `H^i(α)` is epi (iso if `i > m+1`, epi if `i = m+1`), `H^i(β)` iso,
> `H^{i+1}(α)` iso (since `i+1 > m+1`), `H^{i+1}(β)` mono (iso since `i+1 > m`), so
> Sub-lemma B gives `H^i(μ)` iso. For `i = m`: `H^m(β)` epi, `H^{m+1}(α)` epi,
> `H^{m+1}(β)` mono (iso since `m+1 > m`), so Sub-lemma C gives `H^m(μ)` epi. Hence
> `(C, μ)` witnesses that `M` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherent_of_distinguished_one
    (m : ℤ) (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distinguishedTriangles)
    (hK : IsPseudoCoherentFrom T.obj₁ (m + 1))
    (hL : IsPseudoCoherentFrom T.obj₂ m) :
    IsPseudoCoherentFrom T.obj₃ m
```

**`PseudoCoherence.isPseudoCoherent_of_distinguished_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Triangle.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Triangle.lean#L905). The attribute's comment: “(2)”. References: SGA 6 I (2.5), “b), modules over a ring”; SGA 6 I (2.6), “special case”; SGA 6 III (1.4), “special case”.

> **Statement (2).** If `K` and `M` are both `m`-pseudo-coherent, and
> `(K, L, M, f, g, h)` is a distinguished triangle, then `L` is
> `m`-pseudo-coherent.
>
> Reduction to (1): apply (1) to the (distinguished) inverse-rotated triangle
> `(M⟦-1⟧, K, L)`, using that `M⟦-1⟧` is `(m+1)`-pseudo-coherent (shift of the
> `m`-pseudo-coherent `M`) and `K` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherent_of_distinguished_two
    (m : ℤ) (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distinguishedTriangles)
    (hK : IsPseudoCoherentFrom T.obj₁ m)
    (hM : IsPseudoCoherentFrom T.obj₃ m) :
    IsPseudoCoherentFrom T.obj₂ m
```

**`PseudoCoherence.isPseudoCoherent_of_distinguished_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Triangle.lean, line 930](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Triangle.lean#L930). The attribute's comment: “(3)”. References: SGA 6 I (2.6), “special case”; SGA 6 III (1.4), “special case”.

> **Statement (3).** If `L` is `(m+1)`-pseudo-coherent and `M` is
> `m`-pseudo-coherent, and `(K, L, M, f, g, h)` is a distinguished triangle, then
> `K` is `(m+1)`-pseudo-coherent.
>
> Reduction to (1): apply (1) to the (distinguished) rotated triangle
> `(L, M, K⟦1⟧)`, concluding `K⟦1⟧` is `m`-pseudo-coherent; shifting back by `-1`
> and transporting along the isomorphism `(K⟦1⟧)⟦-1⟧ ≅ K` yields that `K` is
> `(m+1)`-pseudo-coherent.

```lean
theorem isPseudoCoherent_of_distinguished_three
    (m : ℤ) (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distinguishedTriangles)
    (hL : IsPseudoCoherentFrom T.obj₂ (m + 1))
    (hM : IsPseudoCoherentFrom T.obj₃ m) :
    IsPseudoCoherentFrom T.obj₁ (m + 1)
```

## Tag 064S, a lemma

[Tag 064S](https://stacks.math.columbia.edu/tag/064S) in the Stacks Project.

**`PseudoCoherence.finite_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Homology.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Homology.lean#L364). The attribute's comment: “(1)”.

> Statement 1 (Stacks 064S). If `K^•` is `m`-pseudo-coherent and `H^i(K^•) = 0`
> for all `i > m`, then `H^m(K^•)` is a finite type `R`-module.

```lean
theorem finite_homology_of_isPseudoCoherentFrom {R : Type u} [Ring R]
    [HasDerivedCategory (ModuleCat.{v} R)] (K : DerivedCategory (ModuleCat.{v} R))
    (m : ℤ) (hK : IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat R) i).obj K)) :
    Module.Finite R ((DerivedCategory.homologyFunctor (ModuleCat R) m).obj K)
```

**`PseudoCoherence.finitePresentation_homology_succ_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Homology.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Homology.lean#L399). The attribute's comment: “(2)”.

> Statement 2 (Stacks 064S). If `K^•` is `m`-pseudo-coherent and `H^i(K^•) = 0`
> for all `i > m + 1`, then `H^{m+1}(K^•)` is a finitely presented `R`-module.

```lean
theorem finitePresentation_homology_succ_of_isPseudoCoherentFrom {R : Type u} [Ring R]
    [HasDerivedCategory (ModuleCat.{v} R)] (K : DerivedCategory (ModuleCat.{v} R))
    (m : ℤ) (hK : IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m + 1 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat R) i).obj K)) :
    Module.FinitePresentation R
      ((DerivedCategory.homologyFunctor (ModuleCat R) (m + 1)).obj K)
```

## Tag 064T, a lemma

[Tag 064T](https://stacks.math.columbia.edu/tag/064T) in the Stacks Project.

**`StacksDraft.PseudoCoherence.modulePseudoCoherent_iff_finiteness_and_resolutions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Module.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Module.lean#L471). References: SGA 6 I (2.9), “special case”.

> Finite generation, finite presentation, finite free resolutions of a fixed length, and
> infinite finite free resolutions characterize the corresponding forms of pseudo-coherence for a
> module, represented in a universe containing both `R` and `M`.

```lean
theorem modulePseudoCoherent_iff_finiteness_and_resolutions
    [HasDerivedCategory (ModuleCat.{max v u} R)] (M : Type v) [AddCommGroup M] [Module R M] :
    (IsModulePseudoCoherentFrom (R := R) (ULift.{u} M) 0 ↔ Module.Finite R M) ∧
    (IsModulePseudoCoherentFrom (R := R) (ULift.{u} M) (-1) ↔ Module.FinitePresentation R M) ∧
    (∀ d : ℕ, IsModulePseudoCoherentFrom (R := R) (ULift.{u} M) (-(d : ℤ)) ↔
      HasFiniteFreeResolutionOfLength (R := R) (ULift.{u} M) d) ∧
    (IsModulePseudoCoherent (R := R) (ULift.{u} M) ↔
      Nonempty (FiniteFreeModuleResolution R (ULift.{u} M)))
```

## Tag 064U, a lemma

[Tag 064U](https://stacks.math.columbia.edu/tag/064U) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherent_iff_pseudoCoherentFrom_all_iff_finiteProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Basic.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Basic.lean#L1041).

> **Stacks 064U.** Pseudo-coherence is equivalent both to `m`-pseudo-coherence for every
> integer `m` and to admitting a bounded-above finite projective representative. If cohomology
> vanishes above `b`, a finite free representative can be chosen to vanish above `b`.

```lean
theorem pseudoCoherent_iff_pseudoCoherentFrom_all_iff_finiteProjective
    {R : Type u} [Ring R] [HasDerivedCategory (ModuleCat.{max u v} R)]
    (K : DerivedCategory (ModuleCat.{max u v} R)) (b : ℤ) :
    let allDegrees := ∀ m : ℤ, IsPseudoCoherentFrom K m
    let finiteProjectiveRepresentative :=
      ∃ P : CochainComplex (ModuleCat.{max u v} R) ℤ,
        (∃ n : ℤ, P.IsStrictlyLE n) ∧
          (∀ i : ℤ, Module.Finite R (P.X i) ∧ Module.Projective R (P.X i)) ∧
          Nonempty (DerivedCategory.Q.obj P ≅ K)
    (IsPseudoCoherent K ↔ allDegrees) ∧
      (IsPseudoCoherent K ↔ finiteProjectiveRepresentative) ∧
      (IsPseudoCoherent K →
        (∀ i : ℤ, b < i →
          IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K)) →
        ∃ (F : CochainComplex (ModuleCat.{max u v} R) ℤ)
          (α : DerivedCategory.Q.obj F ⟶ K),
            (∀ i : ℤ, Module.Finite R (F.X i) ∧ Module.Free R (F.X i)) ∧
              F.IsStrictlyLE b ∧ IsIso α)
```

## Tag 064V, a lemma

[Tag 064V](https://stacks.math.columbia.edu/tag/064V) in the Stacks Project.

**`StacksDraft.PseudoCoherence.isPseudoCoherent_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Basic.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Basic.lean#L1151). References: SGA 6 I (2.5), “b), pseudo-coherent case”; SGA 6 I (2.6), “partial”.

> **Stacks 064V.** In a distinguished triangle in `D(R)`, if two of the three objects are
> pseudo-coherent, then so is the third.

```lean
theorem isPseudoCoherent_of_distinguished
    {R : Type u} [Ring R] [HasDerivedCategory (ModuleCat.{v} R)]
    (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distinguishedTriangles) :
    (IsPseudoCoherent T.obj₁ → IsPseudoCoherent T.obj₂ → IsPseudoCoherent T.obj₃) ∧
    (IsPseudoCoherent T.obj₁ → IsPseudoCoherent T.obj₃ → IsPseudoCoherent T.obj₂) ∧
    (IsPseudoCoherent T.obj₂ → IsPseudoCoherent T.obj₃ → IsPseudoCoherent T.obj₁)
```

## Tag 064W, a lemma

[Tag 064W](https://stacks.math.columbia.edu/tag/064W) in the Stacks Project.

**`StacksDraft.PseudoCoherence.isPseudoCoherentFrom_of_vanishing_and_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Module.lean, line 745](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Module.lean#L745). References: SGA 6 I (2.11), “b), H^i=0 for i>m+1”.

> Vanishing above degree `m`, with the appropriate finiteness assumptions on the cohomology
> in degrees `m` and `m + 1`, implies `m`-pseudo-coherence.

```lean
theorem isPseudoCoherentFrom_of_vanishing_and_finite_homology
    {R : Type u} [Ring R] [HasDerivedCategory (ModuleCat.{v} R)] [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R)) (m : ℤ) :
    ((∀ i : ℤ, m ≤ i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
      IsPseudoCoherentFrom K m) ∧
    ((∀ i : ℤ, m < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
      Module.Finite R ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) m).obj K) →
      IsPseudoCoherentFrom K m) ∧
    ((∀ i : ℤ, m + 1 < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
      Module.FinitePresentation R
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (m + 1)).obj K) →
      Module.Finite R ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) m).obj K) →
      IsPseudoCoherentFrom K m)
```

## Tag 064X, a lemma

[Tag 064X](https://stacks.math.columbia.edu/tag/064X) in the Stacks Project.

**`PseudoCoherence.isPseudoCoherentFrom_and_pseudoCoherent_of_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Characterization.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Characterization.lean#L103). References: SGA 6 I (2.12), “necessity”.

> **Stacks 064X.** Each summand of an `m`-pseudo-coherent binary biproduct is
> `m`-pseudo-coherent, and each summand of a pseudo-coherent binary biproduct is
> pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_and_pseudoCoherent_of_biproduct
    {R : Type u} [Ring R] (K L : DerivedCategory (ModuleCat.{v} R)) (m : ℤ) :
    (IsPseudoCoherentFrom (K ⊞ L) m →
      IsPseudoCoherentFrom K m ∧ IsPseudoCoherentFrom L m) ∧
    (IsPseudoCoherent (K ⊞ L) → IsPseudoCoherent K ∧ IsPseudoCoherent L)
```

## Tag 064Y, a lemma

[Tag 064Y](https://stacks.math.columbia.edu/tag/064Y) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherentFrom_and_pseudoCoherent_of_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Module.lean, line 617](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Module.lean#L617). References: SGA 5 VIII (5.1), “'if' direction”; SGA 6 I (2.11), “Part a), special case”.

> A bounded-above complex with suitably pseudo-coherent terms is pseudo-coherent in the
> corresponding degrees. In particular, pseudo-coherence of every term implies pseudo-coherence
> of the complex.

```lean
theorem pseudoCoherentFrom_and_pseudoCoherent_of_boundedAbove
    (K : CochainComplex (ModuleCat.{v} R) ℤ) (hK : ∃ b : ℤ, K.IsStrictlyLE b) :
    (∀ m : ℤ, (∀ i : ℤ, IsModulePseudoCoherentFrom (R := R) (K.X i) (m - i)) →
      IsPseudoCoherentFrom (DerivedCategory.Q.obj K) m) ∧
    ((∀ i : ℤ, IsModulePseudoCoherent (R := R) (K.X i)) →
      IsPseudoCoherent (DerivedCategory.Q.obj K))
```

## Tag 066B, a lemma

[Tag 066B](https://stacks.math.columbia.edu/tag/066B) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherentFrom_and_pseudoCoherent_of_boundedAbove_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Module.lean, line 884](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Module.lean#L884).

> A cohomologically bounded-above derived object whose cohomology modules are
> pseudo-coherent in the corresponding degrees is pseudo-coherent.

```lean
theorem pseudoCoherentFrom_and_pseudoCoherent_of_boundedAbove_cohomology
    (K : DerivedCategory (ModuleCat.{v} R))
    (hK : ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    (∀ m : ℤ,
      (∀ i : ℤ, IsModulePseudoCoherentFrom (R := R)
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K) (m - i)) →
      IsPseudoCoherentFrom K m) ∧
    ((∀ i : ℤ, IsModulePseudoCoherent (R := R)
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
      IsPseudoCoherent K)
```

## Tag 064Z, a lemma

[Tag 064Z](https://stacks.math.columbia.edu/tag/064Z) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherentFrom_and_pseudoCoherent_iff_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/ChangeOfRings.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/ChangeOfRings.lean#L452). References: SGA 6 III (1.12), “affine case, X = Y”.

> **Stacks 064Z.** If `B` is pseudo-coherent as an `A`-module, restriction of scalars along
> `A → B` preserves and reflects both `m`-pseudo-coherence and pseudo-coherence of complexes.

```lean
theorem pseudoCoherentFrom_and_pseudoCoherent_iff_restrictScalars
    {A : Type u} {B : Type v} [Ring A] [Ring B] (f : A →+* B)
    (hB : IsModulePseudoCoherent (R := A)
      ((ModuleCat.restrictScalars f).obj (ModuleCat.of B B)))
    (K : CochainComplex (ModuleCat.{max u v w} B) ℤ) (m : ℤ) :
    let Kₐ := ((ModuleCat.restrictScalars.{max u v w} f).mapHomologicalComplex
      (ComplexShape.up ℤ)).obj K
    (IsPseudoCoherentFrom (DerivedCategory.Q.obj K) m ↔
      IsPseudoCoherentFrom (DerivedCategory.Q.obj Kₐ) m) ∧
    (IsPseudoCoherent (DerivedCategory.Q.obj K) ↔
      IsPseudoCoherent (DerivedCategory.Q.obj Kₐ))
```

## Tag 0650, a lemma

[Tag 0650](https://stacks.math.columbia.edu/tag/0650) in the Stacks Project.

**`StacksDraft.PseudoCoherence.derivedExtensionScalars_preserves_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/BaseChange.lean, line 671](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/BaseChange.lean#L671). References: SGA 6 I (2.13), “special case”.

> Derived extension of scalars along a homomorphism `f : R →+* A` of commutative rings
> preserves `m`-pseudo-coherent objects of the derived category for every integer `m`, and it
> preserves pseudo-coherent objects. The source ring, the target ring and the module carrier live
> in three independent universes.

```lean
public theorem derivedExtensionScalars_preserves_pseudoCoherent
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A)
    (K : DerivedCategory (ModuleCat.{v} R)) :
    (∀ m : ℤ, IsPseudoCoherentFrom K m →
      IsPseudoCoherentFrom ((derivedExtensionScalars f).obj K) m) ∧
      (IsPseudoCoherent K → IsPseudoCoherent ((derivedExtensionScalars f).obj K))
```

## Tag 066C, a lemma

[Tag 066C](https://stacks.math.columbia.edu/tag/066C) in the Stacks Project.

**`StacksDraft.PseudoCoherence.extensionScalars_preserves_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/ChangeOfRings.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/ChangeOfRings.lean#L83).

> **Stacks 066C.** Extension of scalars along a flat ring homomorphism preserves
> `m`-pseudo-coherent modules for every integer `m` and preserves pseudo-coherent modules.

```lean
theorem extensionScalars_preserves_pseudoCoherent
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] (f : A →+* B) (hf : f.Flat)
    (M : ModuleCat.{w} A) :
    (∀ m : ℤ, IsModulePseudoCoherentFrom (R := A) M m →
      IsModulePseudoCoherentFrom (R := B) ((ModuleCat.extendScalars f).obj M) m) ∧
      (IsModulePseudoCoherent (R := A) M →
        IsModulePseudoCoherent (R := B) ((ModuleCat.extendScalars f).obj M))
```

## Tag 066D, a lemma

[Tag 066D](https://stacks.math.columbia.edu/tag/066D) in the Stacks Project.

**`StacksDraft.PseudoCoherence.isPseudoCoherentFrom_and_isPseudoCoherent_of_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Local.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Local.lean#L582).

> **Stacks 066D.** Both `m`-pseudo-coherence and pseudo-coherence descend from a finite
> principal open cover.

```lean
theorem isPseudoCoherentFrom_and_isPseudoCoherent_of_localization
    {R : Type u} [CommRing R] {ι : Type*} [Finite ι]
    (f : ι → R) (hf : Ideal.span (Set.range f) = ⊤)
    (K : DerivedCategory (ModuleCat.{max v u} R)) (m : ℤ) :
    ((∀ i, IsPseudoCoherentFrom ((localizationAwayFunctorAux.{u, v} (f i)).obj K) m) →
      IsPseudoCoherentFrom K m) ∧
    ((∀ i, IsPseudoCoherent ((localizationAwayFunctorAux.{u, v} (f i)).obj K)) →
      IsPseudoCoherent K)
```

## Tag 068R, a lemma

[Tag 068R](https://stacks.math.columbia.edu/tag/068R) in the Stacks Project.

**`StacksDraft.PseudoCoherence.isPseudoCoherentFrom_and_isPseudoCoherent_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Local.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Local.lean#L550).

> **Stacks 068R.** Both `m`-pseudo-coherence and pseudo-coherence descend along a faithfully
> flat extension of commutative rings.

```lean
theorem isPseudoCoherentFrom_and_isPseudoCoherent_of_faithfullyFlat_baseChange
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : f.FaithfullyFlat)
    (K : CochainComplex (ModuleCat.{max u w} R) ℤ) (m : ℤ) :
    (IsPseudoCoherentFrom
        (DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u, v, max u w} f).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj K)) m →
      IsPseudoCoherentFrom (DerivedCategory.Q.obj K) m) ∧
    (IsPseudoCoherent
        (DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u, v, max u w} f).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj K)) →
      IsPseudoCoherent (DerivedCategory.Q.obj K))
```

## Tag 0DJE, a lemma

[Tag 0DJE](https://stacks.math.columbia.edu/tag/0DJE) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherent_derivedTensorProduct_largeUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Tensor.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Tensor.lean#L487).

> **Stacks 0DJE.** If `K` is `n`-pseudo-coherent and has no cohomology above `a`, and `L` is
> `m`-pseudo-coherent and has no cohomology above `b`, then their derived tensor product
> `K ⊗ᴸ L` is `max (m + a) (n + b)`-pseudo-coherent. Moreover, the derived tensor product of two
> pseudo-coherent objects is pseudo-coherent.
>
> The modules live in a universe `max u v` independent of the ring's universe `u`, as in the
> source, and the derived tensor product is the one of Stacks 064M,
> `CochainComplex.DerivedTensor.derivedTensorProduct`: one endofunctor
> `derivedTensorProduct L` of `D(R)` for each object `L`.

```lean
public theorem pseudoCoherent_derivedTensorProduct_largeUniverse
    (K L : DerivedCategory (ModuleCat.{max u v} R)) :
    (∀ n m a b : ℤ,
      IsPseudoCoherentFrom K n →
      (∀ i : ℤ, a < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K)) →
      IsPseudoCoherentFrom L m →
      (∀ j : ℤ, b < j →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) j).obj L)) →
      IsPseudoCoherentFrom
        ((CochainComplex.DerivedTensor.derivedTensorProduct L).obj K)
        (max (m + a) (n + b))) ∧
      (IsPseudoCoherent K → IsPseudoCoherent L →
        IsPseudoCoherent ((CochainComplex.DerivedTensor.derivedTensorProduct L).obj K))
```

## Tag 066E, a lemma

[Tag 066E](https://stacks.math.columbia.edu/tag/066E) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherent_iff_boundedAbove_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Coherent.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Coherent.lean#L238).

> **Stacks 066E.** Over a Noetherian ring, pseudo-coherence from degree `m` means
> bounded-above finite homology in degrees at least `m`; pseudo-coherence means bounded-above
> finite homology in all degrees; and pseudo-coherence of a module is equivalent to its
> finiteness.

```lean
theorem pseudoCoherent_iff_boundedAbove_finite_homology
    {R : Type u} [Ring R] [IsNoetherianRing R] [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R)) (m : ℤ)
    (M : Type v) [AddCommGroup M] [Module R M] :
    (IsPseudoCoherentFrom K m ↔
      (∃ b : ℤ, ∀ i : ℤ, b < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) ∧
      ∀ i : ℤ, m ≤ i →
        Module.Finite R ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) ∧
    (IsPseudoCoherent K ↔
      (∃ b : ℤ, ∀ i : ℤ, b < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) ∧
      ∀ i : ℤ,
        Module.Finite R ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) ∧
    (IsModulePseudoCoherent (R := R) M ↔ Module.Finite R M)
```

## Tag 0EWZ, a lemma

[Tag 0EWZ](https://stacks.math.columbia.edu/tag/0EWZ) in the Stacks Project.

**`StacksDraft.PseudoCoherence.pseudoCoherentFrom_iff_finite_and_coherent_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Coherent.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Coherent.lean#L410). References: SGA 6 I (3.5), “b), coherent ring”; SGA 6 I (2.11), “Part b), special case”.

> **Stacks 0EWZ.** Over a coherent ring, a bounded-above derived object is
> `m`-pseudo-coherent exactly when its degree-`m` cohomology is finite and its higher cohomology
> modules are coherent, equivalently finitely presented. It is pseudo-coherent exactly when all
> its cohomology modules are coherent.

```lean
theorem pseudoCoherentFrom_iff_finite_and_coherent_homology
    {R : Type u} [CommRing R] [IsCoherentRing R]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K))
    (m : ℤ) :
    let H := fun i : ℤ =>
      (DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K
    let finiteAndCoherent :=
      Module.Finite R (H m) ∧ ∀ i : ℤ, m < i → Module.IsCoherent R (H i)
    let finiteAndFinitePresentation :=
      Module.Finite R (H m) ∧ ∀ i : ℤ, m < i → Module.FinitePresentation R (H i)
    (IsPseudoCoherentFrom K m ↔ finiteAndCoherent) ∧
      (finiteAndCoherent ↔ finiteAndFinitePresentation) ∧
      (IsPseudoCoherent K ↔ ∀ i : ℤ, Module.IsCoherent R (H i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.66, Tag 064N](https://stacks.math.columbia.edu/tag/064N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
