---
declaration: section
origin: cited
lean: ExtendedAlternatingCech.cechd_comp_cechd, ExtendedCech.termTensorEquiv_comm_d, Stacks.CechBaseChange.exists_cechComplexBaseChange_iso, Stacks.CechContractible.cechComplex_nullHomotopic, Cech.cechComplex_homology_torsion_support_vanishes, Cech.cechComplex_isColimit_koszulPowerComplexes
statement: formalized
proof: formalized
---

# 15.30 The extended alternating Čech complex

Section 15.30 of the Stacks Project, [Tag 0G6F](https://stacks.math.columbia.edu/tag/0G6F). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G6G, a lemma

[Tag 0G6G](https://stacks.math.columbia.edu/tag/0G6G) in the Stacks Project.

**`ExtendedAlternatingCech.cechd_comp_cechd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/Extended.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/Extended.lean#L404).

> **Stacks 0G6G**.
> For consecutive integer degrees `i, j, k`, the composition `d_{j,k} ∘ d_{i,j}` of the
> differentials of the extended alternating Čech complex vanishes.

```lean
theorem cechd_comp_cechd (i j k : ℤ) (hij : (ComplexShape.up ℤ).Rel i j)
    (hjk : (ComplexShape.up ℤ).Rel j k) :
    CategoryStruct.comp (cechd f M i j) (cechd f M j k) = 0
```

## Tag 0G6H, a lemma

[Tag 0G6H](https://stacks.math.columbia.edu/tag/0G6H) in the Stacks Project.

**`ExtendedCech.termTensorEquiv_comm_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/Tensor.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/Tensor.lean#L198).

> **Stacks Lemma 15.30.2 (Tag 0G6H).** The degreewise canonical isomorphisms
> `termTensorEquiv` (induced by `M ⊗_R R_g ≅ M_g`) commute with the Čech
> differentials, the differential of `M ⊗_R Č•(R)` being
> `id_M ⊗ d_R = LinearMap.lTensor M (Cech.cechD f R p)`.  Together with
> `termTensorEquiv` this exhibits the extended alternating Čech complex of `M` as
> `M ⊗_R Č•(R)`, an isomorphism of cochain complexes of `R`-modules.

```lean
theorem termTensorEquiv_comm_d (p : ℕ) :
    (termTensorEquiv f M (p + 1)).toLinearMap.comp (cechD f M p)
      = (LinearMap.lTensor M (cechD f R p)).comp (termTensorEquiv f M p).toLinearMap
```

## Tag 0G6I, a lemma

[Tag 0G6I](https://stacks.math.columbia.edu/tag/0G6I) in the Stacks Project.

**`Stacks.CechBaseChange.exists_cechComplexBaseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/BaseChange.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/BaseChange.lean#L503).

> **Stacks 0G6I**.
> Let `R → S` be a ring map, `g_i` the image of `f_i` in `S` and `N = S ⊗_R M`. There is an
> isomorphism of cochain complexes of `S`-modules `e : C^•(f; M) ⊗_R S ≅ C^•(g; N)` (the
> target lifted to the universe of the source) whose degree-`p` component, after lowering
> the lift, is `termBaseChangeS f M S p`.

```lean
theorem exists_cechComplexBaseChange_iso :
    ∃ e : cechComplexBaseChange f M S ≅ cechComplexBaseChangeTarget f M S,
      ∀ p : ℕ, ULift.moduleEquiv.toLinearMap.comp (e.hom.f p).hom =
        termBaseChangeS f M S p
```

## Tag 0G6J, a lemma

[Tag 0G6J](https://stacks.math.columbia.edu/tag/0G6J) in the Stacks Project.

**`Stacks.CechContractible.cechComplex_nullHomotopic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/Contractible.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/Contractible.lean#L677).

> **Stacks 0G6J**.
> If some `f i` is a unit in `R`, then the extended alternating Čech complex of `M` is homotopy
> equivalent to `0`: the identity chain map is chain homotopic to the zero chain map.

```lean
theorem cechComplex_nullHomotopic
    (hunit : ∃ i : Fin r, IsUnit (f i)) :
    Nonempty (Homotopy (𝟙 (cechComplex f M)) 0)
```

## Tag 0G6K, a lemma

[Tag 0G6K](https://stacks.math.columbia.edu/tag/0G6K) in the Stacks Project.

**`Cech.cechComplex_homology_torsion_support_vanishes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/Cohomology.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/Cohomology.lean#L271).

> **Stacks 0G6K.** The cohomology of the extended alternating Čech complex is
> concentrated in degrees `0, …, r`; every chosen element acts locally nilpotently
> on every cohomology class; its support lies in the common zero locus of the chosen
> elements; and all cohomology vanishes when an element of their generated ideal
> acts invertibly on the coefficient module.

```lean
theorem cechComplex_homology_torsion_support_vanishes
    {R : Type u} [CommRing R] {r : ℕ} (f : Fin r → R)
    (M : Type v) [AddCommGroup M] [Module R M] (q : ℤ) :
    let K : CochainComplex (ModuleCat.{max u v} R) ℤ :=
      (Cech.cechComplex f M).extend ComplexShape.embeddingUpNat
    ((q < 0 ∨ (r : ℤ) < q) → Subsingleton (K.homology q)) ∧
      (∀ (i : Fin r) (x : K.homology q),
        ∃ n : ℕ, 0 < n ∧ f i ^ n • x = 0) ∧
      Module.support R (K.homology q) ⊆
        PrimeSpectrum.zeroLocus (Ideal.span (Set.range f) : Set R) ∧
      ((∃ g ∈ Ideal.span (Set.range f),
          IsUnit (algebraMap R (Module.End R M) g)) →
        Subsingleton (K.homology q))
```

## Tag 0913, a lemma

[Tag 0913](https://stacks.math.columbia.edu/tag/0913) in the Stacks Project.

**`Cech.cechComplex_isColimit_koszulPowerComplexes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/KoszulColimit.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/KoszulColimit.lean#L672).

> The extended alternating Čech complex of a finite sequence `f` is the colimit of the
> regraded Koszul complexes on its positive powers. The transition maps multiply each standard
> exterior-basis vector by the product of the entries of `f` indexed by its complement, and the
> colimit cocone sends the basis vector indexed by `s` to the localized generator indexed by the
> complement `t` of `s`, with sign `(-1) ^ (∑ i ∈ t, (i + 1) + p + r * p)`.

```lean
public theorem cechComplex_isColimit_koszulPowerComplexes
    {R : Type u} [CommRing R] {r : ℕ} (f : Fin r → R) :
    ∃ σ : ∀ n : ℕ,
        Koszul.seqComplex (fun i ↦ f i ^ (n + 1)) ⟶
          Koszul.seqComplex (fun i ↦ f i ^ (n + 2)),
      (∀ (n q : ℕ) (s : Finset (Fin r)) (hs : s.card = q),
        (σ n).f q
            ⟨ExteriorAlgebra.ιMulti R q
                (fun k ↦ Pi.single (s.orderEmbOfFin hs k) 1),
              Koszul.ιMulti_mem q _⟩ =
          (∏ i ∈ sᶜ, f i) •
            ⟨ExteriorAlgebra.ιMulti R q
                (fun k ↦ Pi.single (s.orderEmbOfFin hs k) 1),
              Koszul.ιMulti_mem q _⟩) ∧
      ∃ ι : ∀ n : ℕ, koszulPowerCochainComplex f n ⟶ Cech.cechComplex f R,
        ∃ hι : ∀ n : ℕ,
            (koszulPowerDiagram f σ).map (homOfLE (Nat.le_succ n)) ≫
              ι (n + 1) = ι n,
          (∀ (n p q : ℕ) (s t : Finset (Fin r)) (hs : s.card = q) (ht : t.card = p)
              (hcard : p + q = r) (_ : Disjoint s t) (_ : s ∪ t = Finset.univ),
            (ι n).f p
                (koszulRegradeHom f n p q hcard
                  ⟨ExteriorAlgebra.ιMulti R q
                      (fun k ↦ Pi.single (s.orderEmbOfFin hs k) 1),
                    Koszul.ιMulti_mem q _⟩) =
              DirectSum.lof R {w : Finset (Fin r) // w.card = p}
                (fun w ↦ Cech.cechMod f R w.1) ⟨t, ht⟩
                (LocalizedModule.mk
                  ((-1 : R) ^ ((∑ i ∈ t, (i.val + 1)) + p + r * p))
                  ⟨(∏ i ∈ t, f i) ^ (n + 1), n + 1, rfl⟩)) ∧
          Nonempty (IsColimit
            ({ pt := Cech.cechComplex f R
               ι := NatTrans.ofSequence
                 (F := koszulPowerDiagram f σ)
                 (G := (Functor.const ℕ).obj (Cech.cechComplex f R)) ι
                 (fun n ↦ (hι n).trans (Category.comp_id _).symm) } :
              Cocone (koszulPowerDiagram f σ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.30, Tag 0G6F](https://stacks.math.columbia.edu/tag/0G6F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
