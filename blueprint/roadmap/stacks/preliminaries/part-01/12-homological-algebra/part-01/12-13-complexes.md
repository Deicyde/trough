---
declaration: section
origin: cited
lean: Homotopy.compLeft, Homotopy.compRight, HomotopyEquiv, HomologicalComplex.mono_iff_degreewise_mono, HomologicalComplex.epi_iff_degreewise_epi, HomologicalComplex.instAbelian, HomologicalComplex.exact_iff_degreewise_exact, quasiIso_iff_isIso_homologyMap
statement: formalized
proof: formalized
---

# 12.13 Complexes

Section 12.13 of the Stacks Project, [Tag 010V](https://stacks.math.columbia.edu/tag/010V). 12 tags here are carried by 10 declarations of the repository (all in StacksCore) and 21 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 010W, a lemma

[Tag 010W](https://stacks.math.columbia.edu/tag/010W) in the Stacks Project.

Declarations registered for the tag:

- [`Homotopy.compLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.compLeft#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L22) (StacksCore): “together with `Homotopy.compRight`. The Stacks family `c_{i+1} ∘ h_i ∘ a_i` is `(h.compRight c).compLeft a`, whose components are `a.f i ≫ h.hom i j ≫ c.f j` definitionally, so composing the two one-sided lemmas is the whole of the tag and needs no declaration of its own.”.
- [`Homotopy.compRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.compRight#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L27) (StacksCore): “together with `Homotopy.compLeft`; see the comment there.”.

## Tag 010X, a definition

[Tag 010X](https://stacks.math.columbia.edu/tag/010X) in the Stacks Project.

Declarations registered for the tag:

- [`HomotopyEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyEquiv#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L37) (StacksCore): “the morphism `a` together with a `b` and the two homotopies; `A` and `B` are *homotopy equivalent* when `Nonempty (HomotopyEquiv A B)`, which Mathlib does not name separately.”. References: EGA III (6.1.4).

## Tag 010Y, a lemma

[Tag 010Y](https://stacks.math.columbia.edu/tag/010Y) in the Stacks Project.

**`HomologicalComplex.mono_iff_degreewise_mono`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L34). The attribute's comment: “(2)”.

> **Stacks 010Y (2) and 0114 (2).** A morphism of complexes is a monomorphism if and only if it
> is one in each degree.

```lean
lemma mono_iff_degreewise_mono [HasFiniteLimits C] (φ : K ⟶ L) :
    Mono φ ↔ ∀ i, Mono (φ.f i)
```

**`HomologicalComplex.epi_iff_degreewise_epi`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L41). The attribute's comment: “(3)”.

> **Stacks 010Y (3) and 0114 (3).** A morphism of complexes is an epimorphism if and only if it
> is one in each degree.

```lean
lemma epi_iff_degreewise_epi [HasFiniteColimits C] (φ : K ⟶ L) :
    Epi φ ↔ ∀ i, Epi (φ.f i)
```

Declarations registered for the tag:

- [`HomologicalComplex.instAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.instAbelian#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L47) (StacksCore): “(1)”. References: EGA 0 (11.7.1), “more general”; SGA 4 XVII (2.2.7), “special case”; SGA 6 I (1.1.5), “partial”.
- [`HomologicalComplex.exact_iff_degreewise_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.exact_iff_degreewise_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L51) (StacksCore): “(4), for a short complex of complexes: exactness at the middle term is exactness at the middle term in every degree.”.

## Tag 010Z, a definition

[Tag 010Z](https://stacks.math.columbia.edu/tag/010Z) in the Stacks Project.

**`quasiIso_iff_isIso_homologyMap`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/QuasiIso.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L38). The attribute's comment: “(1), identified with the Stacks wording”. References: SGA 4½ Etat 0 (3.1.7).

> **Stacks 010Z (1) and 0115 (1).** A morphism of complexes is a quasi-isomorphism exactly when
> the induced map `Hᵢ(f) : Hᵢ(K) ⟶ Hᵢ(L)` is an isomorphism for every `i`.

```lean
lemma quasiIso_iff_isIso_homologyMap (f : K ⟶ L)
    [∀ i, K.HasHomology i] [∀ i, L.HasHomology i] :
    QuasiIso f ↔ ∀ i, IsIso (homologyMap f i)
```

**`HomologicalComplex.acyclic_iff_isZero_homology`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L36). The attribute's comment: “(2), identified with the Stacks wording”.

> **Stacks 010Z (2) and 0115 (2).** A complex is acyclic exactly when all of its homology
> objects vanish.

```lean
lemma acyclic_iff_isZero_homology (K : HomologicalComplex C c) [∀ i, K.HasHomology i] :
    K.Acyclic ↔ ∀ i, IsZero (K.homology i)
```

Declarations registered for the tag:

- [`QuasiIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiIso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/QuasiIso.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L28) (StacksCore): “(1), the definition”. References: SGA 4½ Etat 0 (3.1.7).
- [`HomologicalComplex.Acyclic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.Acyclic#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L22) (StacksCore): “(2), the definition”. References: SGA 4½ Etat 0 (1.2.3), “more general”.

## Tag 0110, a lemma

[Tag 0110](https://stacks.math.columbia.edu/tag/0110) in the Stacks Project.

Declarations registered for the tag:

- [`Homotopy.homologyMap_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.homologyMap_eq#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L45) (StacksCore): “part 1”. References: EGA 0 (11.2.3), “abutment clause”; SGA 4½ Etat 0 (1.3.2), “partial”.
- [`HomotopyEquiv.quasiIso_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyEquiv.quasiIso_hom#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/QuasiIso.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L43) (StacksCore): “part 2”. References: EGA III (6.1.4), “special case”; EGA III (6.2.1), “f = id\_X”.

## Tag 0111, a lemma

[Tag 0111](https://stacks.math.columbia.edu/tag/0111) in the Stacks Project.

Declarations registered for the tag:

- [`HomologicalComplex.HomologySequence.composableArrows₅_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.HomologySequence.composableArrows₅_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologySequenceLemmas.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologySequenceLemmas.lean#L45) (StacksCore): “the exact sequence itself, as a `ComposableArrows C 5` for one step of the complex shape; the doubly infinite sequence is the family of these over all steps.”.

## Tag 0112, a lemma

[Tag 0112](https://stacks.math.columbia.edu/tag/0112) in the Stacks Project.

Declarations registered for the tag:

- [`Homotopy.compLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.compLeft#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L30) (StacksCore): “the cochain-complex case of 010W, and the same two declarations: both are stated for an arbitrary `ComplexShape`.”.
- [`Homotopy.compRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.compRight#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L34) (StacksCore): “together with `Homotopy.compLeft`; see the comment there.”.

## Tag 0113, a definition

[Tag 0113](https://stacks.math.columbia.edu/tag/0113) in the Stacks Project.

Declarations registered for the tag:

- [`HomotopyEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyEquiv#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L41) (StacksCore): “the cochain-complex case of 010X; `HomotopyEquiv` is stated for an arbitrary `ComplexShape`, so it is the same declaration.”. References: EGA III (6.1.4).

## Tag 0114, a lemma

[Tag 0114](https://stacks.math.columbia.edu/tag/0114) in the Stacks Project.

**`HomologicalComplex.mono_iff_degreewise_mono`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L34). The attribute's comment: “(2)”.

> **Stacks 010Y (2) and 0114 (2).** A morphism of complexes is a monomorphism if and only if it
> is one in each degree.

```lean
lemma mono_iff_degreewise_mono [HasFiniteLimits C] (φ : K ⟶ L) :
    Mono φ ↔ ∀ i, Mono (φ.f i)
```

**`HomologicalComplex.epi_iff_degreewise_epi`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L41). The attribute's comment: “(3)”.

> **Stacks 010Y (3) and 0114 (3).** A morphism of complexes is an epimorphism if and only if it
> is one in each degree.

```lean
lemma epi_iff_degreewise_epi [HasFiniteColimits C] (φ : K ⟶ L) :
    Epi φ ↔ ∀ i, Epi (φ.f i)
```

Declarations registered for the tag:

- [`HomologicalComplex.instAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.instAbelian#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L49) (StacksCore): “(1)”. References: EGA 0 (11.7.1), “more general”; SGA 4 XVII (2.2.7), “special case”; SGA 6 I (1.1.5), “partial”.
- [`HomologicalComplex.exact_iff_degreewise_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.exact_iff_degreewise_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologicalComplexAbelian.lean#L55) (StacksCore): “(4)”.

## Tag 0115, a definition

[Tag 0115](https://stacks.math.columbia.edu/tag/0115) in the Stacks Project.

**`quasiIso_iff_isIso_homologyMap`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/QuasiIso.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L38). The attribute's comment: “(1), identified with the Stacks wording”. References: SGA 4½ Etat 0 (3.1.7).

> **Stacks 010Z (1) and 0115 (1).** A morphism of complexes is a quasi-isomorphism exactly when
> the induced map `Hᵢ(f) : Hᵢ(K) ⟶ Hᵢ(L)` is an isomorphism for every `i`.

```lean
lemma quasiIso_iff_isIso_homologyMap (f : K ⟶ L)
    [∀ i, K.HasHomology i] [∀ i, L.HasHomology i] :
    QuasiIso f ↔ ∀ i, IsIso (homologyMap f i)
```

**`HomologicalComplex.acyclic_iff_isZero_homology`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L36). The attribute's comment: “(2), identified with the Stacks wording”.

> **Stacks 010Z (2) and 0115 (2).** A complex is acyclic exactly when all of its homology
> objects vanish.

```lean
lemma acyclic_iff_isZero_homology (K : HomologicalComplex C c) [∀ i, K.HasHomology i] :
    K.Acyclic ↔ ∀ i, IsZero (K.homology i)
```

Declarations registered for the tag:

- [`QuasiIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiIso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/QuasiIso.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L30) (StacksCore): “(1), the definition; `QuasiIso` is stated for an arbitrary `ComplexShape`, so the chain- and cochain-complex tags are the same declaration.”. References: SGA 4½ Etat 0 (3.1.7).
- [`HomologicalComplex.Acyclic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.Acyclic#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L24) (StacksCore): “(2), the definition; `Acyclic` is stated for an arbitrary `ComplexShape`, so the chain- and cochain-complex tags are the same declaration.”. References: SGA 4½ Etat 0 (1.2.3), “more general”.

## Tag 0116, a lemma

[Tag 0116](https://stacks.math.columbia.edu/tag/0116) in the Stacks Project.

Declarations registered for the tag:

- [`Homotopy.homologyMap_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Homotopy.homologyMap_eq#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/Homotopy.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/Homotopy.lean#L47) (StacksCore): “part 1”. References: EGA 0 (11.2.3), “abutment clause”; SGA 4½ Etat 0 (1.3.2), “partial”.
- [`HomotopyEquiv.quasiIso_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyEquiv.quasiIso_hom#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/QuasiIso.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/QuasiIso.lean#L45) (StacksCore): “part 2”. References: EGA III (6.1.4), “special case”; EGA III (6.2.1), “f = id\_X”.

## Tag 0117, a lemma

[Tag 0117](https://stacks.math.columbia.edu/tag/0117) in the Stacks Project.

**`CochainComplex.shiftIso_hom_app_comp_δ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean#L160). The attribute's comment: “third clause, compatibility with shifts; note the `(-1)^k`, which the Stacks wording does not lead one to expect”.

> **Stacks 0117**, third clause: the long exact cohomology sequence is compatible with shifts,
> in the sense of the identification `H^{i+k}(A^•) = H^i(A[k]^•)` of Definition 12.14.8 (tag 011H).
>
> The two functorial maps of the sequence are unsigned, but the connecting map picks up `(-1)^k`.
> The Stacks project's proof says "compatibility with shifts is immediate from the definitions" and
> records no sign; with its own conventions there is one, because 011G shifts differentials by
> `(-1)^k` while the 011H identification is the plain unsigned re-indexing. `δ_eq_of_shift` is where
> that sign appears.
>
> `shiftIso_hom_app_comp_δ'` is the same statement with the short exactness of the shifted sequence
> derived rather than assumed.

```lean
theorem shiftIso_hom_app_comp_δ (S : ShortComplex (CochainComplex C ℤ)) (hS : S.ShortExact)
    (k i j i' j' : ℤ) (hij : (up ℤ).Rel i j) (hij' : (up ℤ).Rel i' j')
    (hi' : k + i = i') (hj' : k + j = j')
    (hS' : (S.map (CategoryTheory.shiftFunctor (CochainComplex C ℤ) k)).ShortExact) :
    ((homologyFunctor C (up ℤ) 0).shiftIso k i i' hi').hom.app S.X₃ ≫ hS.δ i' j' hij' =
      k.negOnePow • (hS'.δ i j hij ≫
        ((homologyFunctor C (up ℤ) 0).shiftIso k j j' hj').hom.app S.X₁)
```

**`CochainComplex.shiftIso_hom_app_comp_δ'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean#L208). The attribute's comment: “third clause, self-contained form”.

> **Stacks 0117**, third clause, with the short exactness of the shifted sequence produced
> internally rather than assumed.

```lean
lemma shiftIso_hom_app_comp_δ' (S : ShortComplex (CochainComplex C ℤ)) (hS : S.ShortExact)
    (k i j i' j' : ℤ) (hij : (up ℤ).Rel i j) (hij' : (up ℤ).Rel i' j')
    (hi' : k + i = i') (hj' : k + j = j') :
    ((homologyFunctor C (up ℤ) 0).shiftIso k i i' hi').hom.app S.X₃ ≫ hS.δ i' j' hij' =
      k.negOnePow •
        ((hS.map_of_exact (CategoryTheory.shiftFunctor (CochainComplex C ℤ) k)).δ i j hij ≫
          ((homologyFunctor C (up ℤ) 0).shiftIso k j j' hj').hom.app S.X₁)
```

Declarations registered for the tag:

- [`HomologicalComplex.HomologySequence.composableArrows₅_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.HomologySequence.composableArrows₅_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologySequenceLemmas.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologySequenceLemmas.lean#L49) (StacksCore): “the exact sequence itself”.
- [`HomologicalComplex.HomologySequence.mapComposableArrows₅`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.HomologySequence.mapComposableArrows₅#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomologySequenceLemmas.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/HomologySequenceLemmas.lean#L52) (StacksCore): “functorial in the short exact sequence; the shift-compatibility clause is `CochainComplex.shiftIso_hom_app_comp_δ`, which carries a `(-1)^k` on the connecting map that the Stacks wording does not lead you to expect — see the module docstring.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.13, Tag 010V](https://stacks.math.columbia.edu/tag/010V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
