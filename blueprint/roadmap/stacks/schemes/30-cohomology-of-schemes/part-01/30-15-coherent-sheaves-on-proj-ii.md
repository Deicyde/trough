---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjCoherentII.moduleFinite_truncation_of_isCoherent, Stacks.AlgebraicGeometry.Proj.isNoetherian_proj, Stacks.AlgebraicGeometry.ProjNoetherian.proj_isNoetherian_and_coherent, Stacks.AlgebraicGeometry.ProjCoherentII.truncatedTwistedToShifted, Stacks.AlgebraicGeometry.ProjCoherentII.moduleToTruncatedShiftedSections, Stacks.AlgebraicGeometry.ProjCoherentII.exists_pos_forall_bijective_twistedToShiftedComponent, Stacks.AlgebraicGeometry.ProjCoherentII.truncatedSections_finite_and_comparison, Stacks.AlgebraicGeometry.ProjSerreCorrespondence.exists_coherentIrrelevantQuotientEquivalence
statement: formalized
proof: formalized
---

# 30.15 Coherent sheaves on Proj, II

Section 30.15 of the Stacks Project, [Tag 0BXE](https://stacks.math.columbia.edu/tag/0BXE). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B5Q, a lemma

[Tag 0B5Q](https://stacks.math.columbia.edu/tag/0B5Q) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjCoherentII.moduleFinite_truncation_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentII/TwistedFiniteness.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentII/TwistedFiniteness.lean#L350). The attribute's comment: “clause (4)”. References: SGA 2 XII (5.3), “clause (a), special case”.

> Clause (4) of [Stacks, Tag 0B5Q], equivalently part (2) of [Stacks, Tag 0B5R]. For `S` a
> Noetherian graded ring, `X = Proj S`, `ℱ` a coherent `𝒪_X`-module and `k ∈ ℤ`, the graded
> `S`-module `⨁_{n ≥ k} Γ(X, ℱ(n))` is a finite `S`-module.
>
> No generation hypothesis on `S` is assumed. The proof is the source's Veronese reduction: a
> degree `d` is chosen by
> `Stacks.AlgebraicGeometry.ProjCoherentII.exists_reductionDegree`, the degrees are split into the
> `d` residue classes, each class is compared with the twisted global sections of a coherent sheaf
> on `X' = Proj S⁽ᵈ⁾` where [Stacks, Tag 0AG6] (4) applies, and the `d` resulting finite families
> are assembled over `S` by
> `Stacks.AlgebraicGeometry.ProjTwistedSections.moduleFinite_gradedActionTruncation_of_residues`.

```lean
public theorem moduleFinite_truncation_of_isCoherent [IsNoetherianRing S]
    (F : (AlgebraicGeometry.Proj 𝒮).Modules) (hF : _root_.SheafOfModules.IsCoherent F) (k : ℤ) :
    letI := (twistedGlobalSectionsModule 𝒮 F).moduleInst
    Module.Finite S ((twistedGlobalSectionsModule 𝒮 F).truncation 𝒮 F k)
```

**`Stacks.AlgebraicGeometry.Proj.isNoetherian_proj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjNoetherian/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjNoetherian/Basic.lean#L135). The attribute's comment: “proj\_noetherian”. References: EGA II (2.7.1), “(i)”.

> **Stacks Project, Tag 0B5Q.** The projective spectrum of a Noetherian graded ring is a
> Noetherian scheme.

```lean
public instance isNoetherian_proj
    {A : Type u} {σ : Type v} [CommRing A] [IsNoetherianRing A]
    [SetLike σ A] [AddSubgroupClass σ A] (𝒜 : ℕ → σ) [GradedRing 𝒜] :
    IsNoetherian (Proj 𝒜)
```

**`Stacks.AlgebraicGeometry.ProjNoetherian.proj_isNoetherian_and_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjNoetherian/CoherentSheaves.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjNoetherian/CoherentSheaves.lean#L51).

> **Stacks Project, Tag 0B5Q.** Let `A` be a Noetherian graded ring and `X = Proj A`. Then `X`
> is a Noetherian scheme, and every coherent `𝒪_X`-module `ℱ` satisfies the four assertions of the
> lemma: `ℱ` is a quotient of a finite direct sum of twisting sheaves, each `Hᵖ(X, ℱ)` is a finite
> `A₀`-module, the higher cohomology of the high twists vanishes, and each graded tail
> `⨁_{n ≥ k} H⁰(X, ℱ(n))` is a finite `A`-module.

```lean
theorem proj_isNoetherian_and_coherent :
    AlgebraicGeometry.IsNoetherian (AlgebraicGeometry.Proj 𝒜) ∧
      ∀ F : SheafOfModules.{u} (projRingSheaf 𝒜), _root_.SheafOfModules.IsCoherent F →
        (∃ (r : ℕ) (dj : Fin r → ℤ)
            (b : Bicone fun j : Fin r => twistingSheaf 𝒜 (dj j)) (_ : b.IsBilimit)
            (φ : b.pt ⟶ F), Epi φ) ∧
          (∀ p : ℕ, Module.Finite (𝒜 0)
            ((ModuleCat.restrictScalars
              (Stacks.AlgebraicGeometry.GradedProperCohomology.specAlgebraRingHom (𝒜 0)
                (AlgebraicGeometry.Proj.toSpecZero 𝒜))).obj
              (Stacks.AlgebraicGeometry.GradedProperCohomology.cohomologyOf
                (AlgebraicGeometry.Proj 𝒜) p F))) ∧
          (∀ p : ℕ, 0 < p → ∃ e₀ : ℤ, ∀ e : ℤ, e₀ ≤ e →
            IsZero (Hgroup (projRingSheaf 𝒜) ⊤ p (twistSheafOfModules 𝒜 F e))) ∧
          (∀ k : ℤ,
            letI := (ProjTwistedSections.twistedGlobalSectionsModule 𝒜 F).moduleInst
            Module.Finite A
              (TwistedGlobalSectionsModule.truncation 𝒜 F
                (ProjTwistedSections.twistedGlobalSectionsModule 𝒜 F) k))
```

## Tag 0B5R, a lemma

[Tag 0B5R](https://stacks.math.columbia.edu/tag/0B5R) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjCoherentII.truncatedTwistedToShifted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean#L227). The attribute's comment: “part (3), the canonical map N → N'”.

> **Tag 0B5R (3): the canonical map `N → N'`.** The comparison assembled from the global
> sections of Tag 01MQ's maps carries the degrees `≥ k` part of `⨁_n H⁰(X, M̃(n))` into the
> degrees `≥ k` part of `⨁_n H⁰(X, M(n)~)`, because it is degreewise.

```lean
def truncatedTwistedToShifted (k : ℤ) :
    twistedSectionsTruncation 𝒮 𝒨 k →+ shiftedSectionsTruncation 𝒮 𝒨 k
```

**`Stacks.AlgebraicGeometry.ProjCoherentII.moduleToTruncatedShiftedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean#L284). The attribute's comment: “part (4), the canonical map M → N'”.

> **Tag 0B5R (4): for `k` small enough there is a canonical map `M → N'`.** The map is Tag
> 01MR's `M → ⨁_{n ∈ ℤ} H⁰(X, M(n)~)`, and "`k` small enough" is the hypothesis
> `hlow : ∀ n < k, ∀ x ∈ 𝒨 n, x = 0` that `M` vanishes below degree `k`, which is what generators
> of `M` in degrees `≥ k` give.

```lean
def moduleToTruncatedShiftedSections (k : ℤ)
    (hlow : ∀ n : ℤ, n < k → ∀ x ∈ 𝒨 n, x = (0 : M)) :
    M →+ shiftedSectionsTruncation 𝒮 𝒨 k
```

**`Stacks.AlgebraicGeometry.ProjCoherentII.exists_pos_forall_bijective_twistedToShiftedComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentII/Basic.lean#L342). The attribute's comment: “part (6), N\_n ≅ N'\_n for d | n”.

> **Tag 0B5R (6).** For a Noetherian graded ring `A` and a graded `A`-module `M` there is a
> positive `d` such that `N_n = H⁰(X, M̃(n)) → H⁰(X, M(n)~) = N'_n` is bijective for every `n`
> divisible by `d`. The `d` is the common degree of a finite standard-open cover of `Proj(A)`,
> which is the property the source's `d = lcm(deg f_i)` is used for.

```lean
theorem exists_pos_forall_bijective_twistedToShiftedComponent [IsNoetherianRing S] :
    ∃ d : ℕ, 0 < d ∧ ∀ n : ℤ, (d : ℤ) ∣ n →
      Function.Bijective (twistedToShiftedComponent 𝒮 𝒨 n)
```

**`Stacks.AlgebraicGeometry.ProjCoherentII.truncatedSections_finite_and_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjCoherentII/FiniteGradedModuleSections.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjCoherentII/FiniteGradedModuleSections.lean#L163). The attribute's comment: “all six parts: (1) N' is a finite A-module; (2) N is a finite A-module; (3) the canonical map N → N'; (4) the canonical map M → N' for k small enough, i.e. for every k at most some k₀; (5) M\_n → N'\_n is an isomorphism in all sufficiently large degrees; (6) N\_n → N'\_n is an isomorphism for d | n, with d the lcm of the degrees of homogeneous generators of A over A\_0; (1), (2), (3), (5) and (6) for every k ∈ ℤ”.

> Let `A` be a Noetherian graded ring, `f_1, …, f_r` homogeneous generators of `A` over `A_0` of
> positive degrees `deg_1, …, deg_r`, and `d = lcm(deg_i)`. Let `M` be a finite graded `A`-module,
> `X = Proj(A)`, `M̃` the associated quasi-coherent `𝒪_X`-module and `k ∈ ℤ` arbitrary, and set
>
> `N' = ⨁_{n ≥ k} H⁰(X, M(n)~)`   and   `N = ⨁_{n ≥ k} H⁰(X, M̃(n))`.
>
> Then, in order:
>
> 1. `N'` is a finite `A`-module;
> 2. `N` is a finite `A`-module;
> 3. the comparison map `⨁_n H⁰(X, M̃(n)) → ⨁_n H⁰(X, M(n)~)` carries `N` into `N'`, giving the
>    canonical map `N → N'`;
> 4. for `k` small enough the canonical map `M → ⨁_n H⁰(X, M(n)~)` carries `M` into `N'`: there
>    is `k₀` such that for every `k' ≤ k₀` it lands in `⨁_{n ≥ k'} H⁰(X, M(n)~)`;
> 5. `M_n → N'_n` is an isomorphism for all sufficiently large `n`;
> 6. `N_n → N'_n` is an isomorphism whenever `d` divides `n`.

```lean
public theorem truncatedSections_finite_and_comparison [IsNoetherianRing S] [Module.Finite S M]
    {r : ℕ} (f : Fin r → S) (deg : Fin r → ℕ) (hdeg : ∀ i, 0 < deg i)
    (hf : ∀ i, f i ∈ 𝒮 (deg i))
    (hgen : Algebra.adjoin (Stacks.Veronese.gradeZero 𝒮) (Set.range f) = ⊤)
    (k : ℤ) :
    letI := (globalSectionsModuleMap 𝒮 𝒨).moduleInst
    letI := (twistedGlobalSectionsModule 𝒮 (associatedModuleSheaf 𝒮 𝒨)).moduleInst
    Module.Finite S ((globalSectionsModuleMap 𝒮 𝒨).truncation 𝒮 𝒨 k) ∧
      Module.Finite S ((twistedGlobalSectionsModule 𝒮
        (associatedModuleSheaf 𝒮 𝒨)).truncation 𝒮 (associatedModuleSheaf 𝒮 𝒨) k) ∧
      (∀ x ∈ twistedSectionsTruncation 𝒮 𝒨 k,
        twistedToShiftedSections 𝒮 𝒨 x ∈ shiftedSectionsTruncation 𝒮 𝒨 k) ∧
      (∃ k₀ : ℤ, ∀ k' ≤ k₀, ∀ m : M,
        (globalSectionsModuleMap 𝒮 𝒨).hom m ∈ shiftedSectionsTruncation 𝒮 𝒨 k') ∧
      (∃ n₀ : ℤ, ∀ n : ℤ, n₀ ≤ n → Function.Bijective (degreeNToGlobalSections 𝒮 𝒨 n)) ∧
      (∀ n : ℤ, ((Finset.univ.lcm deg : ℕ) : ℤ) ∣ n →
        Function.Bijective (twistedToShiftedComponent 𝒮 𝒨 n))
```

## Tag 0BXF, a proposition

[Tag 0BXF](https://stacks.math.columbia.edu/tag/0BXF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.exists_coherentIrrelevantQuotientEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/CoherentEquivalence.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/CoherentEquivalence.lean#L344). The attribute's comment: “the proposition: for A a Noetherian graded ring and X = Proj(A), the functor M ↦ M~ induces an equivalence Mod^fg\_A / Mod^fg\_\{A, irrelevant} ⟶ Coh(O\_X) whose quasi-inverse is F ↦ ⨁\_\{n ≥ 0} Γ(X, F(n)). The degree d of Tag 0BXE, the lcm of the degrees of a finite homogeneous generating set of A over A\_0, is produced here as the source produces it; the same statement for an arbitrary d divisible by those degrees is coherentIrrelevantQuotientEquivalence”. References: EGA II (2.7.7), “Coherent noetherian case”.

> **[Stacks, Tag 0BXF].** Let `A` be a Noetherian graded ring and `X = Proj(A)`. There is a
> degree `d` of the kind [Stacks, Tag 0BXE] asks for — the least common multiple of the degrees of a
> finite homogeneous generating set of `A` over `A₀` — and for it the functor `M ↦ M̃` induces an
> **equivalence**
>
> `Mod^fg_A / Mod^fg_{A, irrelevant} ⟶ Coh(𝒪_X)`
>
> whose quasi-inverse is `ℱ ↦ ⨁_{n ≥ 0} Γ(X, ℱ(n))`.
>
> The two equations say that the equivalence *is* the proposition's two functors: its `functor` is
> `coherentIrrelevantQuotientFunctor`, the arrow induced by `M ↦ M̃` on the quotient category, and
> its `inverse` is `coherentTruncatedTwistedSectionsFunctor 𝒮 0` followed by the quotient functor,
> which is `ℱ ↦ ⨁_{n ≥ 0} Γ(X, ℱ(n))`.
>
> The degree cannot be quantified away: for `A = k[x]` with `deg x = 2` the module `A(1)` has
> vanishing associated sheaf and is not irrelevant at `d = 1`, so the subcategory of [Stacks, Tag
> 0BXE], and with it the quotient category, genuinely depends on `d` being a multiple of the
> generators' degrees. `coherentIrrelevantQuotientEquivalence` is the same statement for every such
> `d`.

```lean
public theorem exists_coherentIrrelevantQuotientEquivalence :
    ∃ (d : ℕ) (hd : 0 < d) (e : IrrelevantQuotient 𝒮 hd ≌
        _root_.AlgebraicGeometry.SheafOfModules.CoherentModules (projRingSheaf 𝒮)),
      e.functor = coherentIrrelevantQuotientFunctor.{u, u} 𝒮 hd ∧
        e.inverse = coherentTruncatedTwistedSectionsFunctor.{u} 𝒮 0 ⋙
          toIrrelevantQuotient.{u, u, u} 𝒮 hd
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.irrelevantModules_prop_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/IrrelevantModules.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/IrrelevantModules.lean#L384). The attribute's comment: “only the step that the irrelevant finite graded modules satisfy the Serre-subcategory condition of Tag 02MO, which is what makes the quotient category in the statement exist; the equivalence with Coh(O\_X) and its twisted-section quasi-inverse are not formalized, and exactness is spelled elementwise because this library's category of graded modules has no abelian structure yet”.

> The irrelevant finitely generated graded modules satisfy the Serre-subcategory condition of
> Stacks 02MO inside `Mod^{fg}_A`: they contain every zero module, and they contain the middle term
> of every exact sequence whose outer terms belong to them.

```lean
public theorem irrelevantModules_prop_of_exact {d : ℕ} (hd : 0 < d)
    (M₀ : FiniteGradedModules.{u, v, w} 𝒮) (h₀ : Subsingleton M₀.obj.carrier) :
    irrelevantModules 𝒮 d M₀ ∧
      ∀ (L N P : FiniteGradedModules.{u, v, w} 𝒮) (f : L ⟶ N) (g : N ⟶ P),
        (∀ y : N.obj.carrier, g.hom.toLinearMap y = 0 →
          ∃ x : L.obj.carrier, f.hom.toLinearMap x = y) →
        irrelevantModules 𝒮 d L → irrelevantModules 𝒮 d P → irrelevantModules 𝒮 d N
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.irrelevantQuotientFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/IrrelevantQuotientFunctor.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/IrrelevantQuotientFunctor.lean#L134). The attribute's comment: “the arrow of the proposition: the functor out of the quotient category Mod^fg\_A / Mod^fg\_\{A, irrelevant} induced by M ↦ M~, obtained by factoring that functor's restriction to the finitely generated graded modules through the localization at the isomorphisms modulo the irrelevant ones. Its target is written as all sheaves of O\_X-modules; its corestriction to the proposition's own target Coh(O\_X) is coherentIrrelevantQuotientFunctor. Of the proposition's assertion that this functor is an equivalence, faithfulness is proved (faithful\_irrelevantQuotientFunctor), for the corestriction too (faithful\_coherentIrrelevantQuotientFunctor); the whole proposition is now proved, as exists\_coherentIrrelevantQuotientEquivalence of CoherentEquivalence.lean. The quasi-inverse F ↦ ⨁\_\{n ≥ 0} Γ(X, F(n)) is identified on objects, by truncatedTwistedSectionsIsoOfNoetherian, and assembled into a functor to all graded modules, truncatedTwistedSectionsFunctor”.

> **The functor `Mod^fg_A / Mod^fg_{A, irrelevant} ⟶ Mod(𝒪_X)` induced by `M ↦ M̃`.** This is
> the functor of which Stacks 0BXF asserts that it is an equivalence onto `Coh(𝒪_X)`.

```lean
public def irrelevantQuotientFunctor (hd : 0 < d) :
    IrrelevantQuotient 𝒮 hd ⥤ SheafOfModules.{u}
      ((sheafCompose (Opens.grothendieckTopology (ProjectiveSpectrum.top 𝒮))
        (forget₂ CommRingCat.{u} RingCat.{u})).obj
          (ProjectiveSpectrum.Proj.structureSheaf 𝒮))
```

**`Stacks.AlgebraicGeometry.ProjSerreCorrespondence.isSerreClass_irrelevantModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/SerreClass.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjSerreCorrespondence/SerreClass.lean#L213). The attribute's comment: “the Serre-subcategory step of the proposition: the irrelevant finitely generated graded modules are a Serre class in Mod^fg\_A, which is what makes the quotient category on the left of the arrow exist, and which this file turns into that quotient category. The equivalence with Coh(O\_X) and the identification of its quasi-inverse with F ↦ ⨁\_\{n ≥ 0} Γ(X, F(n)) are exists\_coherentIrrelevantQuotientEquivalence of CoherentEquivalence.lean”.

> The irrelevant finitely generated graded modules (Tag 0BXE) are a Serre class in `Mod^fg_A`:
> the subcategory contains a zero object and is closed under subobjects, quotients and
> extensions.

```lean
public theorem isSerreClass_irrelevantModules (hd : 0 < d) :
    ObjectProperty.IsSerreClass (irrelevantModules.{u, v, w} 𝒮 d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.15, Tag 0BXE](https://stacks.math.columbia.edu/tag/0BXE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
