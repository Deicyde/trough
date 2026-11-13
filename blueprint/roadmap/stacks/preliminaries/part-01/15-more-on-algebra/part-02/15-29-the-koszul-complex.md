---
declaration: section
origin: cited
lean: Koszul.differentialGradedAlgebra, Koszul.seqDual, Koszul.seqComplex, koszul_map_comm, Koszul.seqComplex_mulVec_iso, koszul_scalar_eq_homotopy, Koszul.koszulSeq_smul_nullHomotopic_and_span_le_annihilator, HomologicalComplex.homotopyCofiber.d_fstX
statement: formalized
proof: formalized
---

# 15.29 The Koszul complex

Section 15.29 of the Stacks Project, [Tag 0621](https://stacks.math.columbia.edu/tag/0621). 13 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0622, a definition

[Tag 0622](https://stacks.math.columbia.edu/tag/0622) in the Stacks Project.

**`Koszul.differentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/DifferentialGradedAlgebra.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/DifferentialGradedAlgebra.lean#L138). References: EGA III (1.1.1); SGA 3 III (4.6.1), “definition”; SGA 6 VII (1.1), “more general”.

> The Koszul differential graded algebra `K•(φ)`: its underlying graded algebra is
> the exterior algebra `⋀[R] E`, and its differential is contraction by `φ`.
>
> The chain complex obtained from its homogeneous pieces is `Koszul.complex φ`.

```lean
noncomputable def differentialGradedAlgebra (φ : E →ₗ[R] R) :
    HomologicalDifferentialGradedExteriorAlgebra φ
```

## Tag 0623, a definition

[Tag 0623](https://stacks.math.columbia.edu/tag/0623) in the Stacks Project.

**`Koszul.seqDual`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Defs.lean#L158).

> The functional `Rʳ →ₗ[R] R` attached to a sequence `f₁, …, f_r` of elements of `R`,
> namely `v ↦ ∑ i, vᵢ * fᵢ`; it sends the `i`-th standard basis vector to `fᵢ`.

```lean
noncomputable def seqDual (f : Fin r → R) : Module.Dual R (Fin r → R)
```

**`Koszul.seqComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Defs.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Defs.lean#L185). References: EGA III (1.1.1).

> The Koszul complex `K_•(f₁, …, f_r)` of a sequence of elements of `R`: the Koszul
> complex of the functional `Koszul.seqDual f` on `Rʳ`.

```lean
noncomputable def seqComplex (f : Fin r → R) : ChainComplex (ModuleCat.{u} R) ℕ
```

## Tag 0624, a lemma

[Tag 0624](https://stacks.math.columbia.edu/tag/0624) in the Stacks Project.

**`koszul_map_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Functoriality.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Functoriality.lean#L65). References: EGA III (1.1.5).

> **Functoriality of the Koszul complex.**
>
> Let `φ : E → R` and `φ' : E' → R` be `R`-module maps and let `ψ : E → E'` be an `R`-module
> map with `φ' ∘ ψ = φ`. Then the induced graded-algebra homomorphism `∧(ψ)` commutes with the
> Koszul differentials, i.e. `∧(ψ) ∘ d = d' ∘ ∧(ψ)`, where `d = Koszul.contraction φ` and
> `d' = Koszul.contraction φ'`. Together with the fact that `∧(ψ) = ExteriorAlgebra.map ψ` is
> automatically a unital graded `R`-algebra homomorphism, this exhibits `∧(ψ)` as a homomorphism
> of differential graded `R`-algebras `K_•(φ) → K_•(φ')`.

```lean
theorem koszul_map_comm (φ : Module.Dual R E) (φ' : Module.Dual R E') (ψ : E →ₗ[R] E')
    (h : φ'.comp ψ = φ) (x : ExteriorAlgebra R E) :
    exteriorMap ψ (Koszul.contraction φ x) = Koszul.contraction φ' (exteriorMap ψ x)
```

## Tag 0625, a lemma

[Tag 0625](https://stacks.math.columbia.edu/tag/0625) in the Stacks Project.

**`Koszul.seqComplex_mulVec_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Functoriality.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Functoriality.lean#L116).

> **Change of basis for a Koszul complex.** If `x` is an invertible `r × r` matrix over `R`, then
> the Koszul complex of `f` is isomorphic to the Koszul complex of the sequence
> `i ↦ ∑ j, x i j * f j`.

```lean
public theorem seqComplex_mulVec_iso {R : Type u} [CommRing R] {r : ℕ}
    (f : Fin r → R) (x : Matrix (Fin r) (Fin r) R)
    (hx : IsUnit x) :
    Nonempty (Koszul.seqComplex f ≅ Koszul.seqComplex (Matrix.mulVec x f))
```

## Tag 0626, a lemma

[Tag 0626](https://stacks.math.columbia.edu/tag/0626) in the Stacks Project.

**`koszul_scalar_eq_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Functoriality.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Functoriality.lean#L93). References: EGA III (1.1.7), “more general”.

> **Multiplication by `φ e` is null-homotopic on the Koszul complex.** Let `φ : E → R` be an
> `R`-module map, let `e ∈ E`, and set `f = φ e`. As `R`-linear endomorphisms of
> `K_•(φ) = ∧(E)`, `f = d ∘ e + e ∘ d`, i.e. for every `a`, `f • a = d (e ∧ a) + e ∧ d a`, where
> `e ∧ -` is left multiplication by `ι R e` in the exterior algebra.

```lean
theorem koszul_scalar_eq_homotopy (φ : Module.Dual R E) (e : E)
    (a : ExteriorAlgebra R E) :
    φ e • a =
      Koszul.contraction φ (ExteriorAlgebra.ι R e * a)
        + ExteriorAlgebra.ι R e * Koszul.contraction φ a
```

## Tag 0663, a lemma

[Tag 0663](https://stacks.math.columbia.edu/tag/0663) in the Stacks Project.

**`Koszul.koszulSeq_smul_nullHomotopic_and_span_le_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Homotopy.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Homotopy.lean#L149).

> Multiplication by each member of a finite sequence is null-homotopic on its Koszul complex,
> and the ideal generated by the sequence annihilates every Koszul homology module.

```lean
public theorem koszulSeq_smul_nullHomotopic_and_span_le_annihilator
    {R : Type*} [CommRing R] {r : ℕ} (f : Fin r → R) :
    (∀ i, Nonempty (Homotopy (f i • 𝟙 (Koszul.seqComplex f)) 0)) ∧
      ∀ n, Ideal.span (Set.range f) ≤
        Module.annihilator R ((Koszul.seqComplex f).homology n)
```

## Tag 0627, an equation

[Tag 0627](https://stacks.math.columbia.edu/tag/0627) in the Stacks Project.

Declarations registered for the tag:

- [`HomologicalComplex.homotopyCofiber.d_fstX`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homotopyCofiber.d_fstX#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 647](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L647) (StacksFrontier): “first projection of the mapping-cone differential”.
- [`HomologicalComplex.homotopyCofiber.d_sndX`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homotopyCofiber.d_sndX#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L649) (StacksFrontier): “second projection of the mapping-cone differential”.
- [`HomologicalComplex.homotopyCofiber.inlX_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homotopyCofiber.inlX_d#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L651) (StacksFrontier): “restriction to the first summand”.
- [`HomologicalComplex.homotopyCofiber.inrX_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homotopyCofiber.inrX_d#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L653) (StacksFrontier): “restriction to the second summand”.

## Tag 0628, a lemma

[Tag 0628](https://stacks.math.columbia.edu/tag/0628) in the Stacks Project.

**`Stacks.MappingCone.NatIndexed.koszulComplex_phiPrime_iso_cone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L613).

> The cone of multiplication by `f` on the Koszul complex of `phi` is isomorphic, as a chain
> complex of `R`-modules, to the Koszul complex of `phi' : E ⊕ R → R`, by an isomorphism with the
> prescribed components `Θₙ`: the inclusion on the `⋀ⁿ E` summand and wedging with `e₀ = (0,1)` on
> the `⋀^{n-1} E` summand.

```lean
theorem koszulComplex_phiPrime_iso_cone (φ : Module.Dual R E) (f : R) :
    ∃ Θ : coneComplex (Koszul.complex φ) (Koszul.complex φ) (mulByF (Koszul.complex φ) f) ≅
        Koszul.complex (phiPrime φ f),
      (∀ x : (⋀[R]^0 E),
        (Θ.hom.f 0).hom (show ((Koszul.complex φ).X 0 : Type (max u v)) from x) = inclPow 0 x) ∧
      (∀ (n : ℕ) (b : (⋀[R]^(n+1) E)) (a : (⋀[R]^n E)),
        (Θ.hom.f (n+1)).hom
            (show ((Koszul.complex φ).X (n+1) × (Koszul.complex φ).X n : Type (max u v))
              from (b, a))
          = inclPow (n+1) b + wedgeE0Pow (n+1) a)
```

## Tag 0629, a lemma

[Tag 0629](https://stacks.math.columbia.edu/tag/0629) in the Stacks Project.

**`Koszul.seqComplex_snoc_iso_cone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Cone.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Cone.lean#L742).

> The Koszul complex of a sequence obtained by appending `a` is isomorphic to the cone of
> multiplication by `a` on the Koszul complex of the original sequence.

```lean
public theorem seqComplex_snoc_iso_cone {R : Type u} [CommRing R] {r : ℕ}
    (f : Fin r → R) (a : R) :
    Nonempty
      (Koszul.seqComplex (Fin.snoc f a) ≅
        Stacks.MappingCone.NatIndexed.coneComplex (Koszul.seqComplex f) (Koszul.seqComplex f)
          (Stacks.MappingCone.NatIndexed.mulByF (Koszul.seqComplex f) a))
```

## Tag 062A, a lemma

[Tag 062A](https://stacks.math.columbia.edu/tag/062A) in the Stacks Project.

**`Koszul.exists_homotopyEquiv_mappingCone_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean#L81).

> The cone of a composite of two endomorphisms is homotopy equivalent to the cone of a map
> from the shifted cone of the first endomorphism to the cone of the second.

```lean
theorem exists_homotopyEquiv_mappingCone_comp
    {C : Type u} [Category.{v} C] [Preadditive C] [HasZeroObject C]
    [HasBinaryBiproducts C]
    (A : CochainComplex C ℤ) (f g : A ⟶ A) :
    ∃ (φ : (CochainComplex.mappingCone f)⟦(-1 : ℤ)⟧ ⟶
        CochainComplex.mappingCone g),
      Nonempty
        (HomotopyEquiv (CochainComplex.mappingCone (g ≫ f))
          (CochainComplex.mappingCone φ))
```

## Tag 062B, a lemma

[Tag 062B](https://stacks.math.columbia.edu/tag/062B) in the Stacks Project.

**`Koszul.exists_homotopyEquiv_koszulComplex_coprod_mul_mappingCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean#L529).

> After adjoining `f * g` to a linear functional, its Koszul complex is homotopy equivalent to
> the mapping cone of a map from the shifted complex obtained by adjoining `f` to the complex
> obtained by adjoining `g`.

```lean
theorem exists_homotopyEquiv_koszulComplex_coprod_mul_mappingCone
    {R : Type u} [CommRing R] {E : Type v} [AddCommGroup E] [Module R E]
    (φ : E →ₗ[R] R) (f g : R) :
    let K (a : R) : CochainComplex (ModuleCat.{max u v} R) ℤ :=
      (ComplexShape.embeddingDownNat.extendFunctor (ModuleCat.{max u v} R)).obj
        (Koszul.complex (φ.coprod (a • LinearMap.id)))
    ∃ ψ : (K f)⟦(-1 : ℤ)⟧ ⟶ K g,
      Nonempty (HomotopyEquiv (K (f * g)) (CochainComplex.mappingCone ψ))
```

## Tag 062C, a lemma

[Tag 062C](https://stacks.math.columbia.edu/tag/062C) in the Stacks Project.

**`Koszul.exists_homotopyEquiv_koszulComplex_snoc_mul_mappingCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean, line 597](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/HomotopyCofiber.lean#L597).

> The Koszul complex on a finite sequence ending in `f * g` is homotopy equivalent to the mapping
> cone of a map from the shifted complex ending in `f` to the complex ending in `g`.

```lean
theorem exists_homotopyEquiv_koszulComplex_snoc_mul_mappingCone
    {R : Type u} [CommRing R] {n : ℕ} (s : Fin n → R) (f g : R) :
    let K (a : R) : CochainComplex (ModuleCat.{u} R) ℤ :=
      (ComplexShape.embeddingDownNat.extendFunctor (ModuleCat.{u} R)).obj
        (Koszul.complex (Fintype.linearCombination R (Fin.snoc s a)))
    ∃ ψ : (K f)⟦(-1 : ℤ)⟧ ⟶ K g,
      Nonempty (HomotopyEquiv (K (f * g)) (CochainComplex.mappingCone ψ))
```

## Tag 0664, a lemma

[Tag 0664](https://stacks.math.columbia.edu/tag/0664) in the Stacks Project.

**`Koszul.seqComplex_append_iso_totTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Append.lean, line 606](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Append.lean#L606). References: EGA III (1.1.1), “(f)”.

> **Stacks Tag 0664.** The Koszul complex on the concatenation of two sequences
> `f_1, ..., f_r` and `g_1, ..., g_s` (length `r + s`) is isomorphic, as a chain
> complex of `R`-modules, to the total complex of the tensor product of the Koszul
> complexes on `f` and on `g`; see `seqComplexAppendIsoTotTensor` for the isomorphism
> itself.

```lean
theorem seqComplex_append_iso_totTensor {r s : ℕ} (f : Fin r → R) (g : Fin s → R) :
    Nonempty
      (seqComplex (Fin.append f g) ≅ totTensor (seqComplex f) (seqComplex g))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.29, Tag 0621](https://stacks.math.columbia.edu/tag/0621)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
