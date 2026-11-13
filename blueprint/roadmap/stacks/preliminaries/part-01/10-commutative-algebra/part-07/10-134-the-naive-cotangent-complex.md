---
declaration: section
origin: cited
lean: Algebra.Generators.self, Algebra.Extension.cotangentComplex, Algebra.naiveCotangentComplex, Stacks.NaiveCotangent.RingSquare, Algebra.Generators.naiveCotangentComplex_functorial, Deformation.Artin.derivedNaiveCotangentComplexIso, NaiveCotangent.exists_hom, NaiveCotangent.nlMap_homotopic
statement: formalized
proof: formalized
---

# 10.134 The naive cotangent complex

Section 10.134 of the Stacks Project, [Tag 00S0](https://stacks.math.columbia.edu/tag/00S0). 19 tags here are carried by 38 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07BL, an equation

[Tag 07BL](https://stacks.math.columbia.edu/tag/07BL) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.Generators.self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Generators.self#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L262) (StacksFrontier): “the canonical surjection R[S] → S, [s] ↦ s: the generators of S indexed by S itself, whose map MvPolynomial S R → S is aeval id”.

## Tag 07BM, an equation

[Tag 07BM](https://stacks.math.columbia.edu/tag/07BM) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.Extension.cotangentComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Extension.cotangentComplex#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 569](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L569) (StacksFrontier): “the naive cotangent differential”. References: EGA IV (17.15.9); SGA 1 II (5.9), “more general”; SGA 6 0 (4.4), “special case”; SGA 6 VIII (2.1), “affine case”.

## Tag 07BN, a definition

[Tag 07BN](https://stacks.math.columbia.edu/tag/07BN) in the Stacks Project.

**`Algebra.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L161). The attribute's comment: “The complex itself; Mathlib has its differential (`Algebra.Extension.cotangentComplex` at `Algebra.Generators.self R S`) and its degree-`1` homology (`Algebra.H1Cotangent`), but not the two-term complex. See the module docstring.”. References: SGA 6 VIII (2.1), “affine case, R[S]”.

> **The naive cotangent complex** (Stacks 07BN): for a ring map `R → S`, the two-term chain
> complex of `S`-modules
> ```
> NL_{S/R} = (I/I² ⟶ Ω_{R[S]/R} ⊗_{R[S]} S)
> ```
> where `I` is the kernel of the canonical surjection `R[S] → S`, `[s] ↦ s`, with `I/I²` in
> homological degree `1`, `Ω_{R[S]/R} ⊗_{R[S]} S` in homological degree `0`, and the canonical
> map of Stacks 07BM, sending the class of `f ∈ I` to `df ⊗ 1`, as its differential. It is zero
> in all other degrees. Its degree-`0` homology is `Ω_{S/R}` and its degree-`1` homology is
> `H₁(L_{S/R}) = Algebra.H1Cotangent R S`.

```lean
public noncomputable def Algebra.naiveCotangentComplex (R : Type u) (S : Type v) [CommRing R]
    [CommRing S] [Algebra R S] : ChainComplex (ModuleCat.{max u v} S) ℕ
```

## Tag 06RQ, an equation

[Tag 06RQ](https://stacks.math.columbia.edu/tag/06RQ) in the Stacks Project.

**`Stacks.NaiveCotangent.RingSquare`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Functoriality.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Functoriality.lean#L279). The attribute's comment: “The commutative square of rings; the functoriality of the naive cotangent complex in it is `Algebra.Generators.naiveCotangentComplex_functorial`.”.

> **A commutative square of rings** (Stacks 06RQ): ring maps `R → S`, `R → R'`, `R' → S'` and
> `φ : S → S'` such that the two composites `R → S'` agree. It is the datum for which the naive
> cotangent complex is functorial, see `Algebra.Generators.naiveCotangentComplex_functorial`.

```lean
structure RingSquare (R S R' S' : Type*) [CommRing R] [CommRing S] [CommRing R'] [CommRing S']
```

**`Algebra.Generators.naiveCotangentComplex_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Functoriality.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Functoriality.lean#L353). The attribute's comment: “The functoriality of the naive cotangent complex in the square: kernels, the maps of complexes `NL(α) → NL(α')` and `NL(α) ⊗_S S' → NL(α')`, the canonical map of the canonical presentations, and its compatibility with composition.”.

> **Functoriality of the naive cotangent complex in a commutative square of rings**
> (Stacks 06RQ). Let `R → S`, `R' → S'`, `R → R'`, `φ : S → S'` be a commutative square of rings
> (as algebra structures with `IsScalarTower R S S'` and `IsScalarTower R R' S'`, see
> `Stacks.NaiveCotangent.RingSquare`), and let `α : P → S`, `α' : P' → S'` be presentations of `S`
> over `R` and of `S'` over `R'`. Then for every morphism of presentations `f : P → P'`:
> 1. `f` maps `I = ker α` into `I' = ker α'`;
> 2. the induced maps `I/I² → I'/(I')²` and `Ω_{P/R} ⊗_P S → Ω_{P'/R'} ⊗_{P'} S'` commute with the
>    differentials, so they form a map of complexes `NL(α) → NL(α')`;
> 3. the induced maps on `NL(α) ⊗_S S'` commute with the differentials, so they form a map of
>    complexes `NL(α) ⊗_S S' → NL(α')`.
> Moreover:
> 4. for the canonical presentations `R[S] → S` and `R'[S'] → S'`, the canonical morphism
>    `defaultHom (self R S) (self R' S')` is the ring map `[s] ↦ [φ(s)]`;
> 5. the construction is compatible with composition: for a second square
>    `R' → R''`, `S' → S''`, the composite of the canonical morphisms `R[S] → R'[S'] → R''[S'']` is
>    the canonical morphism `R[S] → R''[S'']` of the outer square, hence the canonical maps
>    `NL_{S/R} → NL_{S'/R'} → NL_{S''/R''}` compose to the map of the outer square.

```lean
theorem naiveCotangentComplex_functorial (P : Generators R S ι) (P' : Generators R' S' ι') :
    (∀ f : P.Hom P', P.ker.map f.toAlgHom ≤ P'.ker) ∧
    (∀ f : P.Hom P',
      Extension.CotangentSpace.map f.toExtensionHom ∘ₗ P.toExtension.cotangentComplex =
        P'.toExtension.cotangentComplex.restrictScalars S ∘ₗ
          Extension.Cotangent.map f.toExtensionHom) ∧
    (∀ f : P.Hom P',
      P'.toExtension.cotangentComplex ∘ₗ
          (Extension.Cotangent.map f.toExtensionHom).liftBaseChange S' =
        (Extension.CotangentSpace.map f.toExtensionHom).liftBaseChange S' ∘ₗ
          P.toExtension.cotangentComplex.baseChange S') ∧
    (∀ s : S, (defaultHom (self R S) (self R' S')).toAlgHom (.X s) = .X (algebraMap S S' s)) ∧
    (∀ (R'' S'' : Type _) [CommRing R''] [CommRing S''] [Algebra R'' S''] [Algebra R' R'']
      [Algebra R' S''] [Algebra S' S''] [Algebra S S''] [IsScalarTower R' R'' S'']
      [IsScalarTower R' S' S''] [IsScalarTower S S' S''],
      (defaultHom (self R' S') (self R'' S'')).comp (defaultHom (self R S) (self R' S')) =
        defaultHom (self R S) (self R'' S''))
```

## Tag 00S1, a lemma

[Tag 00S1](https://stacks.math.columbia.edu/tag/00S1) in the Stacks Project.

**`Deformation.Artin.derivedNaiveCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveCotangentPresentation.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Obstruction/NaiveCotangentPresentation.lean#L348). The attribute's comment: “presentation independence in the derived category: the comparison with the canonical presentation is an isomorphism in D(A)”. References: SGA 6 0 (4.3), “partial”; SGA 6 0 (4.4), “special case”; SGA 6 VIII (2.2), “special case”.

> For any presentation of `A` over `Λ`, the comparison with the canonical presentation is an
> isomorphism `NL(α) ≅ NL_{A/Λ}` in the derived category of `A`-modules.

```lean
public def derivedNaiveCotangentComplexIso (P : Algebra.Generators Λ A ι)
    (φ : P.Hom (canonicalGenerators Λ A)) :
    DerivedCategory.Q.obj (twoTermComplex (nlRestrict A P)) ≅
      derivedNaiveCotangentComplex Λ A
```

**`NaiveCotangent.exists_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L417). The attribute's comment: “(1)”.

> **Existence.** There exists a morphism of presentations `varphi` from `α` to `α'`
> covering the square.

```lean
theorem exists_hom (P : Generators R S ι) (P' : Generators R' S' ι') : Nonempty (P.Hom P')
```

**`NaiveCotangent.nlMap_homotopic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L427). The attribute's comment: “(2)”.

> **Homotopy uniqueness.** Any two morphisms of presentations `varphi, varphi'` from `α` to
> `α'` induce homotopic chain maps `NL(varphi), NL(varphi')` (over the source base `S`). The
> homotopy is the `S`-linear map `h : Ω_{P/R} ⊗_P S → I'/(I')²`
> (`= P.CotangentSpace →ₗ[S] P'.Cotangent`) given by `Algebra.Extension.Hom.sub` of the two
> extension homs; the two homotopy relations are `Cotangent.map_sub_map` and
> `CotangentSpace.map_sub_map`.

```lean
theorem nlMap_homotopic (P : Generators R S ι) (P' : Generators R' S' ι') (φ φ' : P.Hom P') :
    Homotopic (nlMap P P' φ) (nlMap P P' φ')
```

**`NaiveCotangent.nlMapBase_comp_nlMapBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L436). The attribute's comment: “(3)”.

> **Compatibility with composition.** Given a commutative diagram of two squares and
> compatible morphisms of presentations `varphi : P → P'`, `varphi' : P' → P''`, the composite
> `varphi' ∘ varphi` is a morphism of presentations from `α` to `α''` and, viewing everything
> over the base ring `S`, `NL(varphi') ∘ NL(varphi) = NL(varphi' ∘ varphi)`.

```lean
theorem nlMapBase_comp_nlMapBase {R'' S'' ι'' : Type*} [CommRing R''] [CommRing S'']
    [Algebra R'' S''] [Algebra R' R''] [Algebra R' S''] [Algebra S' S''] [Algebra S S'']
    [IsScalarTower R' R'' S''] [IsScalarTower R' S' S''] [IsScalarTower S S' S''] [Algebra R R'']
    [Algebra R S''] [IsScalarTower R R' R''] [IsScalarTower R R'' S''] [IsScalarTower R S S'']
    (P : Generators R S ι) (P' : Generators R' S' ι') (P'' : Generators R'' S'' ι'') (φ : P.Hom P')
    (φ' : P'.Hom P'') :
    (nlMapBase S P' P'' φ').comp (nlMapBase S P P' φ) = nlMapBase S P P'' (φ'.comp φ)
```

**`NaiveCotangent.nlMap_isHomotopyEquiv_and_isQuasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L516). The attribute's comment: “(4)”.

> **Isomorphism case.** If `R → R'` and `φ : S → S'` are isomorphisms, then for any morphism
> of presentations `varphi` from `α` to `α'` the induced chain map `NL(varphi)` (over `S`) is
> both a homotopy equivalence and a quasi-isomorphism.

```lean
theorem nlMap_isHomotopyEquiv_and_isQuasiIso (hR : Function.Bijective (algebraMap R R'))
    (hS : Function.Bijective (algebraMap S S')) (P : Generators R S ι) (P' : Generators R' S' ι')
    (φ : P.Hom P') : IsHomotopyEquiv (nlMap P P' φ) ∧ IsQuasiIso (nlMap P P' φ)
```

**`NaiveCotangent.nlMap_canonical_isQuasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Defs.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Defs.lean#L559).

> **Comparison with the canonical complex.** Any morphism of presentations `varphi` from a
> presentation `α` of `S/R` to the canonical presentation `α_can : R[S] → S` induces a
> quasi-isomorphism `NL(α) → NL_{S/R}`.

```lean
theorem nlMap_canonical_isQuasiIso (P : Generators R S ι) (φ : P.Hom (canonicalGenerators R S)) :
    IsQuasiIso (nlMap P (canonicalGenerators R S) φ)
```

## Tag 08Q1, a lemma

[Tag 08Q1](https://stacks.math.columbia.edu/tag/08Q1) in the Stacks Project.

**`NaiveCotangent.isHomotopyEquiv_toKaehlerChainMap_of_algEquiv_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/FormallySmoothExtensionQuasiIso.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/FormallySmoothExtensionQuasiIso.lean#L223). The attribute's comment: “the homotopy equivalence `NL_{S/R} → (0 → Ω_{S/R})`, for the canonical naive cotangent complex of any `R`-algebra `S` isomorphic to a polynomial algebra `R[x_i : i ∈ ι]`”.

> **The naive cotangent complex of a polynomial algebra** (Stacks 08Q1). Let `R → S` be a
> polynomial algebra, that is `S ≅ R[x_i : i ∈ ι]` as `R`-algebras for some set of variables `ι`.
> Then the canonical naive cotangent complex `NL_{S/R}` is homotopy equivalent to the complex
> `(0 → Ω_{S/R})` with `Ω_{S/R}` in degree `0`, the homotopy equivalence being the augmentation
> `toKaehlerChainMap R S`.

```lean
theorem isHomotopyEquiv_toKaehlerChainMap_of_algEquiv_mvPolynomial {ι : Type*}
    (e : MvPolynomial ι R ≃ₐ[R] S) : IsHomotopyEquiv (toKaehlerChainMap R S)
```

**`NaiveCotangent.isQuasiIso_toKaehlerChainMap_of_algEquiv_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/FormallySmoothExtensionQuasiIso.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/FormallySmoothExtensionQuasiIso.lean#L234). The attribute's comment: “the quasi-isomorphism `NL_{S/R} → (0 → Ω_{S/R})` deduced from the homotopy equivalence, for any `R`-algebra `S` isomorphic to a polynomial algebra `R[x_i : i ∈ ι]`”.

> **Homology of the naive cotangent complex of a polynomial algebra** (Stacks 08Q1). For an
> `R`-algebra `S` isomorphic to a polynomial algebra `R[x_i : i ∈ ι]`, the augmentation
> `NL_{S/R} → (0 → Ω_{S/R})` is a quasi-isomorphism: `H₁(NL_{S/R}) = 0` and `H₀(NL_{S/R}) = Ω_{S/R}`
> through it.

```lean
theorem isQuasiIso_toKaehlerChainMap_of_algEquiv_mvPolynomial {ι : Type*}
    (e : MvPolynomial ι R ≃ₐ[R] S) : IsQuasiIso (toKaehlerChainMap R S)
```

## Tag 00S2, a lemma

[Tag 00S2](https://stacks.math.columbia.edu/tag/00S2) in the Stacks Project.

**`Algebra.Generators.Cotangent.map_ker_baseChange_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/JacobiZariski.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Kaehler/JacobiZariski.lean#L144). The attribute's comment: “Exactness at `H₁(L_{C/A})`, the one node of the six term sequence that is not in Mathlib; the term on the left is the source's `H₁(NL_{B/A} ⊗_B C)`, so no `Tor` vanishing hypothesis is needed. See the module docstring.”.

> **The Jacobi-Zariski sequence is exact at `H₁(L_{C/A})`**: let `A → B → C` be ring maps, let
> `α : A[x_s, s ∈ S] → B` be a presentation with kernel `I`, let `β : B[y_t, t ∈ T] → C` be a
> presentation with kernel `J`, and let `γ : A[x_s, y_t] → C` be the induced presentation of `C`
> with kernel `K`. Then the image in `K/K²` of
> `H₁(NL_{B/A} ⊗_B C) = Ker(I/I² ⊗_B C → Ω_{A[x_s]/A} ⊗ C)`, under the map `I/I² ⊗_B C → K/K²`
> induced by `A[x_s] → A[x_s, y_t]`, is the intersection of
> `H₁(L_{C/A}) = Ker(K/K² → Ω_{A[x_s, y_t]/A} ⊗ C)` with the kernel of the map `K/K² → J/J²`
> induced by `A[x_s, y_t] → B[y_t]`, i.e. with the kernel of `H₁(L_{C/A}) → H₁(L_{C/B})`.

```lean
public theorem map_ker_baseChange_cotangentComplex (Q : Generators S T ι)
    (P : Generators R S σ) :
    Submodule.map ((Extension.Cotangent.map (Q.toComp P).toExtensionHom).liftBaseChange T)
        (LinearMap.ker (P.toExtension.cotangentComplex.baseChange T)) =
      LinearMap.ker (Q.comp P).toExtension.cotangentComplex ⊓
        LinearMap.ker (Extension.Cotangent.map (Q.ofComp P).toExtensionHom)
```

**`NaiveCotangent.jacobiZariski_sixTerm_exact_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiPresentations.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiPresentations.lean#L272). The attribute's comment: “the six-term exact sequence with its middle column an ARBITRARY presentation of `C` over `A`, rather than the presentation `Q.comp P` induced by the other two, which is what `NaiveCotangent.jacobiZariski_sixTerm_exact` gives; the two are compared by Stacks 00S1 (4), which this statement uses but does not state”.

> **The Jacobi-Zariski six-term exact sequence over three independently chosen
> presentations** (Stacks 00S2 together with Stacks 00S1).  Let `A → B → C` be ring maps, let
> `α : A[x_s] → B` be a presentation of `B` over `A`, let `β : B[y_t] → C` be a presentation of
> `C` over `B` and let `N` be *any* presentation of `C` over `A`.  Choose morphisms of extensions
> `varphi : α ⟶ N` over the square with vertical morphisms `id_A` and `B → C`, and
> `psi : N ⟶ β` over the square with vertical morphisms `A → B` and `id_C`.  Then
> ```
> H₁(NL(α) ⊗_B C) → H₁(NL(N)) → H₁(NL(β)) --δ--> H₀(NL(α) ⊗_B C) → H₀(NL(N)) → H₀(NL(β)) → 0
> ```
> is exact at each of its five interior nodes, `δ` being
> `NaiveCotangent.jacobiZariskiConnecting`.
>
> The two comparison maps do not depend on the choice of `varphi` and `psi`
> (`NaiveCotangent.homotopic_nlExtensionBaseChangeMap` and
> `NaiveCotangent.homotopic_nlExtensionOverMap`, which are Stacks 00S1 (2)), so the sequence is
> canonical.

```lean
theorem jacobiZariski_sixTerm_exact_extension (Q : Generators S T ι)
    (P : Generators R S σ) (N : Generators R T τ)
    (φ : P.toExtension.Hom N.toExtension) (ψ : N.toExtension.Hom Q.toExtension) :
    Exact (nlExtensionBaseChangeMap (T := T) φ).onH₁ (nlExtensionOverMap ψ).onH₁ ∧
      Exact (nlExtensionOverMap ψ).onH₁ (jacobiZariskiConnecting Q P) ∧
      Exact (jacobiZariskiConnecting Q P) (nlExtensionBaseChangeMap (T := T) φ).onH₀ ∧
      Exact (nlExtensionBaseChangeMap (T := T) φ).onH₀ (nlExtensionOverMap ψ).onH₀ ∧
      Surjective (nlExtensionOverMap ψ).onH₀
```

**`NaiveCotangent.jacobiZariski_sixTerm_exact_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiPresentations.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiPresentations.lean#L326). The attribute's comment: “the six-term exact sequence between the naive cotangent complexes of the three CANONICAL presentations of Stacks 07BL, rather than of the three presentations of the source's own proof”.

> **The Jacobi-Zariski six-term exact sequence over the canonical presentations** of Stacks
> 07BL.  For ring maps `A → B → C`,
> ```
> H₁(NL_{B/A} ⊗_B C) → H₁(NL_{C/A}) → H₁(NL_{C/B}) --δ--> C ⊗_B Ω_{B/A} → Ω_{C/A} → Ω_{C/B} → 0
> ```
> is exact at each of its five interior nodes, the three complexes being the naive cotangent
> complexes of the canonical presentations `A[B] → B`, `A[C] → C` and `B[C] → C`, and the two
> comparison maps those attached to any morphisms of extensions between them, on which they do
> not depend.
>
> This is `NaiveCotangent.jacobiZariski_sixTerm_exact_extension` at the canonical presentation of
> `C` over `A`; it is the form in which the stalkwise statements of Stacks 0E1Y need it, the stalk
> of the naive cotangent complex being the naive cotangent complex of the canonical presentation
> of the stalk (Stacks 0D09), and the stalk of the canonical map `c₁` of Stacks 0E1Y being
> `NaiveCotangent.nlExtensionBaseChangeMap` of a morphism of those canonical presentations
> (`Stacks.NaiveCotangentStalkBaseChange.stalkLegZeroLinear_baseChangeNaiveCotangentMap`).

```lean
theorem jacobiZariski_sixTerm_exact_canonical
    (φ : (canonicalGenerators R S).toExtension.Hom (canonicalGenerators R T).toExtension)
    (ψ : (canonicalGenerators R T).toExtension.Hom (canonicalGenerators S T).toExtension) :
    Exact (nlExtensionBaseChangeMap (T := T) φ).onH₁ (nlExtensionOverMap ψ).onH₁ ∧
      Exact (nlExtensionOverMap ψ).onH₁
        (jacobiZariskiConnecting (canonicalGenerators S T) (canonicalGenerators R S)) ∧
      Exact (jacobiZariskiConnecting (canonicalGenerators S T) (canonicalGenerators R S))
        (nlExtensionBaseChangeMap (T := T) φ).onH₀ ∧
      Exact (nlExtensionBaseChangeMap (T := T) φ).onH₀ (nlExtensionOverMap ψ).onH₀ ∧
      Surjective (nlExtensionOverMap ψ).onH₀
```

**`NaiveCotangent.jacobiZariski_diagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean#L159). The attribute's comment: “The canonical commutative diagram with exact rows: the top row is short exact, the bottom row is exact with a surjection at its right end.”.

> **The Jacobi-Zariski diagram** (Stacks 00S2, first assertion).  Let `A → B → C` be ring maps,
> let `α : A[x_s] → B` and `β : B[y_t] → C` be presentations with kernels `I` and `J`, and let
> `γ : A[x_s, y_t] → C` be the induced presentation, with kernel `K`.  In the canonical diagram
> ```
> 0 ⟶ C ⊗_B Ω_{A[x]/A} ⊗ B ⟶ Ω_{A[x,y]/A} ⊗ C ⟶ Ω_{B[y]/B} ⊗ C ⟶ 0
>           ▲                       ▲                  ▲
>      C ⊗_B I/I²       ⟶         K/K²       ⟶       J/J²        ⟶ 0
> ```
> the top row is short exact, the bottom row is exact, and both squares commute: the vertical
> maps are the differentials of `NL(α) ⊗_B C`, `NL(γ)` and `NL(β)`, and the horizontal ones are
> the components of `NaiveCotangent.nlToComp` and `NaiveCotangent.nlOfComp`.

```lean
public theorem jacobiZariski_diagram (Q : Generators S T ι) (P : Generators R S σ) :
    Injective (nlToComp Q P).f₀ ∧ Exact (nlToComp Q P).f₀ (nlOfComp Q P).f₀ ∧
      Surjective (nlOfComp Q P).f₀ ∧ Exact (nlToComp Q P).f₁ (nlOfComp Q P).f₁ ∧
      Surjective (nlOfComp Q P).f₁ ∧
      (NL (Q.comp P)).d ∘ₗ (nlToComp Q P).f₁ = (nlToComp Q P).f₀ ∘ₗ (nlBaseChange T P).d ∧
      (NL Q).d ∘ₗ (nlOfComp Q P).f₁ = (nlOfComp Q P).f₀ ∘ₗ (NL (Q.comp P)).d
```

**`NaiveCotangent.jacobiZariskiConnecting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean#L175). The attribute's comment: “The connecting map of the six-term sequence, for the naive cotangent complexes of three presentations as in the source's own proof.”.

> **The Jacobi-Zariski connecting map** (Stacks 00S2): for ring maps `A → B → C` and
> presentations `α : A[x_s] → B`, `β : B[y_t] → C` with induced presentation
> `γ : A[x_s, y_t] → C`, the snake-lemma map
> `δ : H₁(NL(β)) ⟶ H₀(NL(α) ⊗_B C)`, that is `H₁(L_{C/B}) → C ⊗_B Ω_{B/A}`.

```lean
public noncomputable def jacobiZariskiConnecting (Q : Generators S T ι) (P : Generators R S σ) :
    H₁ (NL Q) →ₗ[T] H₀ (nlBaseChange T P)
```

**`NaiveCotangent.jacobiZariski_sixTerm_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean#L196). The attribute's comment: “The six-term exact sequence for the naive cotangent complex, over the three presentations of the source's own proof; `Stacks.KaehlerDifferential.JacobiZariski` records only exactness at `H₁(L_{C/A})`, and for the full cotangent complex.”.

> **The Jacobi-Zariski six-term exact sequence** (Stacks 00S2) for the naive cotangent
> complex.  Let `A → B → C` be ring maps, let `α : A[x_s] → B` and `β : B[y_t] → C` be
> presentations and let `γ : A[x_s, y_t] → C` be the induced presentation of `C` over `A`.
> Then
> ```
> H₁(NL(α) ⊗_B C) → H₁(NL(γ)) → H₁(NL(β)) --δ--> H₀(NL(α) ⊗_B C) → H₀(NL(γ)) → H₀(NL(β)) → 0
> ```
> is exact at each of its five interior nodes, `δ` being
> `NaiveCotangent.jacobiZariskiConnecting`.  In the notation of the source this is
> `H₁(NL_{B/A} ⊗_B C) → H₁(L_{C/A}) → H₁(L_{C/B}) → C ⊗_B Ω_{B/A} → Ω_{C/A} → Ω_{C/B} → 0`.

```lean
public theorem jacobiZariski_sixTerm_exact (Q : Generators S T ι) (P : Generators R S σ) :
    Exact (nlToComp Q P).onH₁ (nlOfComp Q P).onH₁ ∧
      Exact (nlOfComp Q P).onH₁ (jacobiZariskiConnecting Q P) ∧
      Exact (jacobiZariskiConnecting Q P) (nlToComp Q P).onH₀ ∧
      Exact (nlToComp Q P).onH₀ (nlOfComp Q P).onH₀ ∧
      Surjective (nlOfComp Q P).onH₀
```

**`NaiveCotangent.exists_jacobiZariski_sixTerm_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiSixTerm.lean#L219). The attribute's comment: “The existential form of the six-term sequence for the naive cotangent complex.”.

> **Stacks 00S2** in the form in which the source states it: there *exists* a six-term
> exact sequence
> ```
> H₁(NL(α) ⊗_B C) → H₁(NL(γ)) → H₁(NL(β)) → H₀(NL(α) ⊗_B C) → H₀(NL(γ)) → H₀(NL(β)) → 0
> ```
> of `C`-modules, for ring maps `A → B → C`, presentations `α : A[x_s] → B`,
> `β : B[y_t] → C` and the induced presentation `γ : A[x_s, y_t] → C`.

```lean
public theorem exists_jacobiZariski_sixTerm_exact (Q : Generators S T ι)
    (P : Generators R S σ) :
    ∃ δ : H₁ (NL Q) →ₗ[T] H₀ (nlBaseChange T P),
      Exact (nlToComp Q P).onH₁ (nlOfComp Q P).onH₁ ∧
        Exact (nlOfComp Q P).onH₁ δ ∧
        Exact δ (nlToComp Q P).onH₀ ∧
        Exact (nlToComp Q P).onH₀ (nlOfComp Q P).onH₀ ∧
        Surjective (nlOfComp Q P).onH₀
```

**`NaiveCotangent.bijective_h1BaseChangeMap_of_tor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiTor.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/JacobiZariskiTor.lean#L85). The attribute's comment: “The final assertion: if `Tor₁^B(Ω_{B/A}, C)` and `Tor₂^B(Ω_{B/A}, C)` vanish then the canonical map `C ⊗_B H₁(NL_{B/A}) → H₁(NL_{B/A} ⊗_B C)` is an isomorphism; `Tor` is Mathlib's `Tor'` on `ModuleCat B`, with `B` and `C` in one universe as `Tor` requires.”.

> **The `Tor` clause of the Jacobi-Zariski sequence** (Stacks 00S2, final assertion).  Let
> `A → B → C` be ring maps and let `α : A[x_s] → B` be a presentation of `B` over `A`.  If
> `Tor₁^B(Ω_{B/A}, C) = 0` and `Tor₂^B(Ω_{B/A}, C) = 0`, then the canonical map
> `C ⊗_B H₁(NL(α)) → H₁(NL(α) ⊗_B C)` is bijective, that is
> `H₁(NL_{B/A} ⊗_B C) = H₁(L_{B/A}) ⊗_B C`.

```lean
theorem bijective_h1BaseChangeMap_of_tor {T : Type u} [CommRing T] [Algebra S T]
    (P : Generators R S σ)
    (h₁ : Limits.IsZero (((Tor' (ModuleCat.{u} S) 1).obj (ModuleCat.of S Ω[S⁄R])).obj
      (ModuleCat.of S T)))
    (h₂ : Limits.IsZero (((Tor' (ModuleCat.{u} S) 2).obj (ModuleCat.of S Ω[S⁄R])).obj
      (ModuleCat.of S T))) :
    Bijective (h1BaseChangeMap T P)
```

## Tag 07VC, a remark

[Tag 07VC](https://stacks.math.columbia.edu/tag/07VC) in the Stacks Project.

**`NaiveCotangent.towerChainMap_homotopic_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean#L216). The attribute's comment: “the composition is homotopy equivalent to zero”.

> **Stacks 07VC.** The composition `NL_{B/A} ⟶ NL_{C/A} ⟶ NL_{C/B}` of the two
> functoriality maps of the naive cotangent complex is homotopic to the zero chain map.

```lean
public theorem towerChainMap_homotopic_zero :
    Homotopic (towerChainMap A B C)
      (ChainMap.zero (nlRestrict B (Generators.self A B))
        (nlRestrict B (Generators.self B C)))
```

**`NaiveCotangent.towerNullHomotopy_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean#L227). The attribute's comment: “the displayed map is an explicit homotopy”.

> The two homotopy relations satisfied by `towerNullHomotopy`: it is a null homotopy of the
> composition `NL_{B/A} ⟶ NL_{C/A} ⟶ NL_{C/B}`.

```lean
public theorem towerNullHomotopy_spec :
    (towerChainMap A B C).f₁ = towerNullHomotopy A B C ∘ₗ
        (nlRestrict B (Generators.self A B)).d ∧
      (towerChainMap A B C).f₀ =
        (nlRestrict B (Generators.self B C)).d ∘ₗ towerNullHomotopy A B C
```

**`NaiveCotangent.towerNullHomotopy_cotangentSpaceBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/CompositionNullHomotopy.lean#L259). The attribute's comment: “the value of the homotopy on the basis element d[b]”.

> **Stacks 07VC.** The homotopy sends the basis element `d[b]` of
> `Ω_{A[B]/A} ⊗_{A[B]} B` to the class of `[φ(b)] - b` in `J/J²`.

```lean
public theorem towerNullHomotopy_cotangentSpaceBasis (b : B) :
    towerNullHomotopy A B C ((Generators.self A B).cotangentSpaceBasis b) =
      Extension.Cotangent.mk
        ⟨X (algebraMap B C b) - MvPolynomial.C b, X_sub_C_mem_ker B C b⟩
```

## Tag 07BP, a lemma

[Tag 07BP](https://stacks.math.columbia.edu/tag/07BP) in the Stacks Project.

**`h1Cotangent_equiv_cotangent_of_surjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/H1.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/H1.lean#L116).

> For a surjective ring map `A → B` with kernel `I := RingHom.ker (algebraMap A B)`, the
> `A`-linear isomorphism `Algebra.H1Cotangent A B ≃ₗ[A] I.Cotangent`.

```lean
noncomputable def h1Cotangent_equiv_cotangent_of_surjective
    (h : Function.Surjective (algebraMap A B)) :
    Algebra.H1Cotangent A B ≃ₗ[A] (RingHom.ker (algebraMap A B)).Cotangent
```

**`NaiveCotangent.nlToConormalOfSurjective_isHomotopyEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Surjective.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Surjective.lean#L108). The attribute's comment: “the homotopy equivalence `NL_{B/A} ≃ (I/I^2 → 0)`; the consequence `H_1(L_{B/A}) = I/I^2` is `h1Cotangent_equiv_cotangent_of_surjective`”.

> **Stacks 07BP.** Let `A → B` be a surjective ring map with kernel `I`. Then the naive
> cotangent complex `NL_{B/A}` is homotopy equivalent to the chain complex `(I/I² → 0)` with
> `I/I²` in degree `1`, via `nlToConormalOfSurjective`.

```lean
theorem nlToConormalOfSurjective_isHomotopyEquiv (h : Function.Surjective (algebraMap A B)) :
    IsHomotopyEquiv (nlToConormalOfSurjective h)
```

## Tag 065V, a lemma

[Tag 065V](https://stacks.math.columbia.edu/tag/065V) in the Stacks Project.

**`exact_mapCotangent_kerCotangentToTensor_and_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Conormal.lean, line 697](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Conormal.lean#L697). References: EGA 0 (20.5.12), “(i), special case”.

> **Stacks Tag 065V (Lemma 10.134.7).** Let `A → B → C` be ring maps with `A → C`
> surjective, and set `I = ker (A → C)` and `J = ker (B → C)`. Then the sequence
> `I/I² → J/J² → Ω[B⁄A] ⊗_B B/J → 0` is exact: the image of `Ideal.mapCotangent` is the
> kernel of `KaehlerDifferential.kerCotangentToTensor`, and the latter is surjective.

```lean
theorem exact_mapCotangent_kerCotangentToTensor_and_surjective
    (A B C : Type*) [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hAC : Function.Surjective (algebraMap A C))
    (hle : RingHom.ker (algebraMap A C) ≤
      Ideal.comap (Algebra.ofId A B) (RingHom.ker (algebraMap B C))) :
    Function.Exact
      (Ideal.mapCotangent (RingHom.ker (algebraMap A C)) (RingHom.ker (algebraMap B C))
        (Algebra.ofId A B) hle)
      (KaehlerDifferential.kerCotangentToTensor A B C) ∧
    Function.Surjective (KaehlerDifferential.kerCotangentToTensor A B C)
```

## Tag 00S4, a lemma

[Tag 00S4](https://stacks.math.columbia.edu/tag/00S4) in the Stacks Project.

**`FlatBaseChangeNL.statement2_complex_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/BaseChange.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/BaseChange.lean#L758). References: EGA IV (16.2.2), “(iii)”; EGA IV (16.2.4), “affine case”; SGA 3 I (6.8.5), “special case”; SGA 3 III (0.14), “partial”.

> **Statement 2, part (b): the canonical comparison is an isomorphism.**
>
> If `R → R'` is flat, the canonical comparison `NL(α) ⊗_S S' → NL(α')` is an isomorphism of
> two-term complexes of `S' = R' ⊗_R S`-modules, with degree-`1` component `cotComparison1`
> (bijective by flatness) and degree-`0` component `cotComparison0` (always bijective).

```lean
theorem statement2_complex_iso [Module.Flat R R'] (P : Algebra.Extension R S) :
    ∃ iso : TwoComplexEquiv (cotDiffBaseChangeS R' P)
        (P.baseChange (T := R')).cotangentComplex,
      (iso.e1 : _ →ₗ[R' ⊗[R] S] _) = cotComparison1 R' P ∧
        (iso.e0 : _ →ₗ[R' ⊗[R] S] _) = cotComparison0 R' P
```

**`FlatBaseChangeNL.statement3_homotopy_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/BaseChange.lean, line 1465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/BaseChange.lean#L1465).

> **Statement 3**: under flatness of `R → R'`, the canonical comparison chain map of
> naive cotangent complexes `NL_{S/R} ⊗_S S' → NL_{S'/R'}` (with `NL_{S'/R'}` the
> canonical presentation of `S' = R' ⊗_R S` over `R'`) is a homotopy equivalence of
> two-term complexes of `S'`-modules; in particular a quasi-isomorphism.
>
> The asserted homotopy equivalence has as its forward chain map the canonical comparison,
> i.e. the `ChainMap` whose degree-`1`/`0` components are the canonical comparisons
> `statement3_f1`/`statement3_f0` (the `S'`-linear lifts of `Cotangent.map (canHom)`,
> `CotangentSpace.map (canHom)`).

```lean
theorem statement3_homotopy_equiv [Module.Flat R R'] :
    ∃ he : HtpyEquiv (nlCanDiffBaseChange R')
        ((Algebra.Generators.self R' (R' ⊗[R] S)).toExtension).cotangentComplex,
      he.toFun.f1 = statement3_f1 R' ∧ he.toFun.f0 = statement3_f0 R'
```

## Tag 07BQ, a lemma

[Tag 07BQ](https://stacks.math.columbia.edu/tag/07BQ) in the Stacks Project.

**`RingMapSystemUnbundled.isIso_colim_NL`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Colimit.lean, line 1697](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Colimit.lean#L1697).

> **Stacks Tag 07BQ, Lemma 10.134.9 (packaged).**
> The canonical comparison morphism `colim_λ NL_{S_λ/R_λ} → NL_{S/R}` is an
> isomorphism of two-term complexes: it is a bijection in each homological degree
> (degree 1 and degree 0) and the two degreewise comparison maps commute with the
> differentials (the colimit differential `colimDifferential` and the differential
> `NL_{S/R}.cotangentComplex`).  This bundles the three theorems above.

```lean
theorem isIso_colim_NL [IsDirected Λ (· ≤ ·)] [Nonempty Λ] :
    Function.Bijective sys.comparisonCotangent ∧
    Function.Bijective sys.comparisonCotangentSpace ∧
    (∀ x : sys.colimCotangent,
      sys.comparisonCotangentSpace (sys.colimDifferential x)
        = sys.NLinf.cotangentComplex (sys.comparisonCotangent x))
```

## Tag 07BR, a lemma

[Tag 07BR](https://stacks.math.columbia.edu/tag/07BR) in the Stacks Project.

**`kaehlerDifferential_subsingleton_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L1151).

> `H₀(NL_{S⁻¹A/A}) = Ω_{S⁻¹A/A} = 0`: the module of Kähler differentials of a
> localization `S⁻¹A` over `A` vanishes.

```lean
theorem kaehlerDifferential_subsingleton_of_isLocalization
    [IsLocalization S B] :
    Subsingleton (Ω[B⁄A])
```

**`h1Cotangent_subsingleton_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 1160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L1160).

> `H₁(NL_{S⁻¹A/A}) = 0`: the first naive cotangent homology of a localization `S⁻¹A`
> over `A` vanishes.

```lean
theorem h1Cotangent_subsingleton_of_isLocalization
    [IsLocalization S B] :
    Subsingleton (Algebra.H1Cotangent A B)
```

## Tag 07BS, a lemma

[Tag 07BS](https://stacks.math.columbia.edu/tag/07BS) in the Stacks Project.

**`naiveCotangentComplex_localization_base_homotopyEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 1459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L1459).

> With `Aₘ` a localization of `A` at the multiplicative subset `M` and a ring map `Aₘ → B`, the
> canonical chain map `φ = (φ₁, φ₀) : NL_{B/A} → NL_{B/Aₘ}`, given by
> `Algebra.Extension.Cotangent.map h` and `Algebra.Extension.CotangentSpace.map h` for the morphism
> of extensions `h` induced by the tower `A → Aₘ → B`, is a homotopy equivalence of the two term
> naive cotangent complexes of `B`-modules.

```lean
theorem naiveCotangentComplex_localization_base_homotopyEquiv
    (A : Type*) (Aₘ : Type*) (B : Type*)
    [CommRing A] [CommRing Aₘ] [CommRing B]
    [Algebra A Aₘ] [Algebra A B] [Algebra Aₘ B]
    [IsScalarTower A Aₘ B]
    (M : Submonoid A) [IsLocalization M Aₘ] :
    let P := (Generators.self A B).toExtension
    let Q := (Generators.self Aₘ B).toExtension
    let h : P.Hom Q :=
      ((Generators.self A B).defaultHom (Generators.self Aₘ B)).toExtensionHom
    let φ₁ := Algebra.Extension.Cotangent.map h
    let φ₀ := Algebra.Extension.CotangentSpace.map h
    ∃ (ψ₁ : Q.Cotangent →ₗ[B] P.Cotangent)
      (ψ₀ : Q.CotangentSpace →ₗ[B] P.CotangentSpace)
      (s : P.CotangentSpace →ₗ[B] P.Cotangent)
      (t : Q.CotangentSpace →ₗ[B] Q.Cotangent),
      Q.cotangentComplex ∘ₗ φ₁ = φ₀ ∘ₗ P.cotangentComplex ∧
      P.cotangentComplex ∘ₗ ψ₁ = ψ₀ ∘ₗ Q.cotangentComplex ∧
      ψ₁ ∘ₗ φ₁ - LinearMap.id = s ∘ₗ P.cotangentComplex ∧
      ψ₀ ∘ₗ φ₀ - LinearMap.id = P.cotangentComplex ∘ₗ s ∧
      φ₁ ∘ₗ ψ₁ - LinearMap.id = t ∘ₗ Q.cotangentComplex ∧
      φ₀ ∘ₗ ψ₀ - LinearMap.id = Q.cotangentComplex ∘ₗ t
```

**`NaiveCotangent.isQuasiIso_nlExtensionOverMap_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/LocalizationBaseAndTarget.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/LocalizationBaseAndTarget.lean#L479). The attribute's comment: “the canonical map `NL_{T/R} ⟶ NL_{T/R'}` is bijective in both degrees, hence a quasi-isomorphism; the homotopy equivalence itself is `naiveCotangentComplex_localization_base_homotopyEquiv`.”.

> **Localizing the base**: for a localization `R' = N⁻¹R` of `R` at a multiplicative subset
> `N ⊆ R` and a ring map `R' → T`, the canonical map of two-term complexes `NL_{T/R} ⟶ NL_{T/R'}`
> is bijective in both degrees, hence a quasi-isomorphism.

```lean
theorem isQuasiIso_nlExtensionOverMap_of_isLocalization (N : Submonoid R) [IsLocalization N R'] :
    IsQuasiIso (nlExtensionOverMap
      ((Generators.self R T).defaultHom (Generators.self R' T)).toExtensionHom)
```

## Tag 08JZ, a lemma

[Tag 08JZ](https://stacks.math.columbia.edu/tag/08JZ) in the Stacks Project.

**`Algebra.Generators.naiveCotangentComplex_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 1014](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L1014). The attribute's comment: “The whole statement: the presentation `β` (its values on the variables), the generators `I`, `f x - 1` of its kernel (Mathlib's `Algebra.Generators.comp_localizationAway_ker`), items (1) (from Mathlib's `Algebra.Generators.cotangentCompLocalizationAwayEquiv` and `Algebra.Generators.basisCotangentAway`), (2) (from Mathlib's `Algebra.Generators.CotangentSpace.compEquiv`) and (3), and the homotopy equivalence `NL_{B/A} ⊗_B B_g → NL_{B_g/A}`, for the map induced by any morphism between any presentations.”.

> **Stacks 08JZ, the formation of the naive cotangent complex commutes with localization at an
> element.** Let `A → B` be a ring map, let `g ∈ B`, let `B_g` be a localization of `B` away from
> `g`, let `α : P = A[x_i, i ∈ ι] → B` be a presentation with kernel `I` and let `f ∈ P` be an
> element mapped to `g` by `α`. Then `β = (localizationAway T g).comp P : P[x] → B_g` is a
> presentation of `B_g` over `A` extending `α` and sending `x` to `1/g`, and
>
> * its kernel `J` is generated by `I` and `f x - 1`;
> * (1) `J/J² = (I/I²)_g ⊕ B_g (f x - 1)`: there is an isomorphism `J/J² ≅ (I/I²) ⊗_B B_g ⊕ B_g`
>   restricting to the canonical map on the first summand and sending `(0, 1)` to the class of
>   `f x - 1`;
> * (2) `Ω_{P[x]/A} ⊗ B_g = Ω_{P/A} ⊗ B_g ⊕ B_g dx`: there is an isomorphism
>   `Ω_{P[x]/A} ⊗ B_g ≅ (Ω_{P/A} ⊗_P B) ⊗_B B_g ⊕ B_g` restricting to the canonical map on the first
>   summand and sending `(0, 1)` to `dx`;
> * (3) `NL(β) ≅ NL(α) ⊗_B B_g ⊕ (B_g --g--> B_g)`: isomorphisms in both degrees which intertwine
>   the differential of `NL(β)` with the direct sum of the base changed differential of `NL(α)` and
>   multiplication by `g` on `B_g`, and restrict to the canonical maps on the first summands;
> * hence, for any presentations `P'` of `B` and `Q` of `B_g` over `A` (for example the canonical
>   ones, whose complexes are `NL_{B/A}` and `NL_{B_g/A}`) and any morphism `φ` of presentations,
>   the induced map `NL(P') ⊗_B B_g → NL(Q)` is a homotopy equivalence: a chain map with a chain
>   homotopy inverse `(ψ₁, ψ₀)` and homotopies `s`, `t`.

```lean
public theorem naiveCotangentComplex_localizationAway
    (g : S) [IsLocalization.Away g T] {ι : Type*} (P : Generators R S ι) (f : P.Ring)
    (hf : algebraMap P.Ring S f = g) :
    (∀ i, ((localizationAway T g).comp P).val (Sum.inr i) = algebraMap S T (P.val i)) ∧
      ((localizationAway T g).comp P).val (Sum.inl ()) = IsLocalization.Away.invSelf g ∧
      ((localizationAway T g).comp P).ker =
        Ideal.map ((localizationAway T g).toComp P).toAlgHom P.ker ⊔
          Ideal.span {rename Sum.inr f * X (Sum.inl ()) - 1} ∧
      (∃ e : ((localizationAway T g).comp P).toExtension.Cotangent ≃ₗ[T]
          T ⊗[S] P.toExtension.Cotangent × T,
        e.symm.toLinearMap ∘ₗ LinearMap.inl T _ _ =
            (Extension.Cotangent.map
              ((localizationAway T g).toComp P).toExtensionHom).liftBaseChange T ∧
          ∃ h : rename Sum.inr f * X (Sum.inl ()) - 1 ∈ ((localizationAway T g).comp P).ker,
            e.symm (0, 1) = Extension.Cotangent.mk ⟨_, h⟩) ∧
      (∃ e : ((localizationAway T g).comp P).toExtension.CotangentSpace ≃ₗ[T]
          T ⊗[S] P.toExtension.CotangentSpace × T,
        e.symm.toLinearMap ∘ₗ LinearMap.inl T _ _ =
            (Extension.CotangentSpace.map
              ((localizationAway T g).toComp P).toExtensionHom).liftBaseChange T ∧
          e.symm (0, 1) = ((1 : T) ⊗ₜ[((localizationAway T g).comp P).Ring]
            KaehlerDifferential.D R ((localizationAway T g).comp P).Ring (X (Sum.inl ())) :)) ∧
      (∃ (e₁ : ((localizationAway T g).comp P).toExtension.Cotangent ≃ₗ[T]
          T ⊗[S] P.toExtension.Cotangent × T)
        (e₀ : ((localizationAway T g).comp P).toExtension.CotangentSpace ≃ₗ[T]
          T ⊗[S] P.toExtension.CotangentSpace × T),
        e₀.toLinearMap ∘ₗ ((localizationAway T g).comp P).toExtension.cotangentComplex =
            (P.toExtension.cotangentComplex.baseChange T).prodMap
              (algebraMap S T g • LinearMap.id) ∘ₗ e₁.toLinearMap ∧
          e₁.symm.toLinearMap ∘ₗ LinearMap.inl T _ _ =
            (Extension.Cotangent.map
              ((localizationAway T g).toComp P).toExtensionHom).liftBaseChange T ∧
          e₀.symm.toLinearMap ∘ₗ LinearMap.inl T _ _ =
            (Extension.CotangentSpace.map
              ((localizationAway T g).toComp P).toExtensionHom).liftBaseChange T) ∧
      ∀ {ι' κ : Type*} (P' : Generators R S ι') (Q : Generators R T κ)
        (φ : P'.toExtension.Hom Q.toExtension),
        Q.toExtension.cotangentComplex ∘ₗ (Extension.Cotangent.map φ).liftBaseChange T =
            (Extension.CotangentSpace.map φ).liftBaseChange T ∘ₗ
              P'.toExtension.cotangentComplex.baseChange T ∧
          ∃ (ψ₁ : Q.toExtension.Cotangent →ₗ[T] T ⊗[S] P'.toExtension.Cotangent)
            (ψ₀ : Q.toExtension.CotangentSpace →ₗ[T] T ⊗[S] P'.toExtension.CotangentSpace)
            (s : T ⊗[S] P'.toExtension.CotangentSpace →ₗ[T] T ⊗[S] P'.toExtension.Cotangent)
            (t : Q.toExtension.CotangentSpace →ₗ[T] Q.toExtension.Cotangent),
            P'.toExtension.cotangentComplex.baseChange T ∘ₗ ψ₁ =
                ψ₀ ∘ₗ Q.toExtension.cotangentComplex ∧
              LinearMap.id - ψ₁ ∘ₗ (Extension.Cotangent.map φ).liftBaseChange T =
                s ∘ₗ P'.toExtension.cotangentComplex.baseChange T ∧
              LinearMap.id - ψ₀ ∘ₗ (Extension.CotangentSpace.map φ).liftBaseChange T =
                P'.toExtension.cotangentComplex.baseChange T ∘ₗ s ∧
              LinearMap.id - (Extension.Cotangent.map φ).liftBaseChange T ∘ₗ ψ₁ =
                t ∘ₗ Q.toExtension.cotangentComplex ∧
              LinearMap.id - (Extension.CotangentSpace.map φ).liftBaseChange T ∘ₗ ψ₀ =
                Q.toExtension.cotangentComplex ∘ₗ t
```

## Tag 00S7, a lemma

[Tag 00S7](https://stacks.math.columbia.edu/tag/00S7) in the Stacks Project.

**`Algebra.Extension.Cotangent.bijOn_ker_liftBaseChange_map_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L186). The attribute's comment: “The `H₁` half at the level of the complexes, where the homology is `ker (d ⊗ T)` rather than `T ⊗ ker d`. The `H₀` half is `KaehlerDifferential.isLocalizedModule_map` and the `H¹(L)`-level `H₁` half is `Algebra.H1Cotangent.isLocalizedModule`. See the module docstring.”.

> **The naive cotangent complex commutes with localization**, on `H₁`: let `A → B` be a ring
> map, let `M ⊆ B` be a multiplicative subset with localization `M⁻¹B`, and let `α`, `β` be
> presentations of `B` and of `M⁻¹B` over `A` with a compatible map `f` between them. Then the map
> `M⁻¹B ⊗_B I/I² → J/J²` induced by `f` carries the kernel of the base changed differential of
> `NL(α)` bijectively onto the kernel of the differential of `NL(β)`.

```lean
public theorem Algebra.Extension.Cotangent.bijOn_ker_liftBaseChange_map_of_isLocalization
    {R S T : Type*} [CommRing R] [CommRing S] [CommRing T]
    [Algebra R S] [Algebra R T] [Algebra S T] [IsScalarTower R S T]
    (M : Submonoid S) [IsLocalization M T] {ι κ : Type*} {P : Algebra.Generators R S ι}
    {Q : Algebra.Generators R T κ} (f : P.toExtension.Hom Q.toExtension) :
    Set.BijOn ((Algebra.Extension.Cotangent.map f).liftBaseChange T)
      (LinearMap.ker (P.toExtension.cotangentComplex.baseChange T))
      (LinearMap.ker Q.toExtension.cotangentComplex)
```

**`NaiveCotangent.isQuasiIso_nlExtensionBaseChangeMap_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/LocalizationBaseAndTarget.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/LocalizationBaseAndTarget.lean#L446). The attribute's comment: “the whole lemma at the level of the complexes: the canonical map `NL_{S/R} ⊗_S T ⟶ NL_{T/R}` is a quasi-isomorphism. The `H₁` half alone is `Algebra.Extension.Cotangent.bijOn_ker_liftBaseChange_map_of_isLocalization`.”.

> **Localizing the target**: for a localization `T = M⁻¹S` of `S` at a multiplicative subset
> `M ⊆ S`, the canonical map of two-term complexes `NL_{S/R} ⊗_S T ⟶ NL_{T/R}` is a
> quasi-isomorphism.

```lean
theorem isQuasiIso_nlExtensionBaseChangeMap_of_isLocalization (M : Submonoid S) [IsLocalization M T]
    (h : (Generators.self R S).toExtension.Hom (Generators.self R T).toExtension) :
    IsQuasiIso (nlExtensionBaseChangeMap (T := T) h)
```

## Tag 00S3, a lemma

[Tag 00S3](https://stacks.math.columbia.edu/tag/00S3) in the Stacks Project.

**`main_theorem_00s3`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/TwoTermComplex.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/TwoTermComplex.lean#L155).

> **Stacks Tag 00S3 (Lemma 10.134.14).** Let `R` be a ring and let
> `A_• : A_1 →[d_A] A_0` and `B_• : B_1 →[d_B] B_0` be two term complexes of
> `R`-modules. Suppose there are morphisms of complexes `φ : A_• → B_•` and
> `ψ : B_• → A_•` such that `φ ∘ ψ` is homotopic to `id_{B_•}` and `ψ ∘ φ` is
> homotopic to `id_{A_•}`. Then there is an isomorphism of `R`-modules
> `A_1 ⊕ B_0 ≅ B_1 ⊕ A_0`.

```lean
theorem main_theorem_00s3 (A B : TwoComplex R)
    (φ : ComplexHom A B) (ψ : ComplexHom B A)
    (hB : Homotopic (φ.comp ψ) (ComplexHom.id B))
    (hA : Homotopic (ψ.comp φ) (ComplexHom.id A)) :
    Nonempty ((A.A1 × B.A0) ≃ₗ[R] (B.A1 × A.A0))
```

## Tag 00S5, a lemma

[Tag 00S5](https://stacks.math.columbia.edu/tag/00S5) in the Stacks Project.

**`NaiveCotangent.Conormal.conormal_stable_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Conormal.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Conormal.lean#L269).

> **Stacks Tag 00S5 (Lemma 10.134.15).** Let `R → S` be a ring map of finite
> type, and let
>   `P : Algebra.Generators R S (Fin n)` (with kernel `I`) and
>   `Q : Algebra.Generators R S (Fin m)` (with kernel `J`)
> be two finite-type presentations of `S` over `R`. Then there is an isomorphism
> of `S`-modules
>   `I/I² ⊕ S^{⊕m} ≅ J/J² ⊕ S^{⊕n}`.

```lean
theorem conormal_stable_iso [Algebra.FiniteType R S]
    {n m : ℕ} (P : Algebra.Generators R S (Fin n)) (Q : Algebra.Generators R S (Fin m)) :
    Nonempty ((Conormal P × FreeModule S m) ≃ₗ[S] (Conormal Q × FreeModule S n))
```

## Tag 00S6, a lemma

[Tag 00S6](https://stacks.math.columbia.edu/tag/00S6) in the Stacks Project.

**`Algebra.Generators.nonempty_cotangent_baseChange_prod_linearEquiv_of_isLocalizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Localization.lean, line 819](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Localization.lean#L819). The attribute's comment: “The isomorphism is non-canonical: `Nonempty` of a linear equivalence is the whole statement. See the module docstring.”.

> **The conormal module up to free summands, after localizing at an element**: let `R → S` be
> a ring map, let `g ∈ S` and let `S_g` be a localization of `S` away from `g`. Let
> `α : R[x₁, …, xₙ] → S` be a presentation of `S` over `R` with kernel `I` and let
> `β : R[y₁, …, y_m] → S_g` be a presentation of `S_g` over `R` with kernel `J`. Then there is an
> isomorphism of `S_g`-modules `(I/I²)_g ⊕ S_g^{⊕m} ≅ J/J² ⊕ S_g^{⊕n}`.

```lean
public theorem nonempty_cotangent_baseChange_prod_linearEquiv_of_isLocalizationAway
    (g : S) [IsLocalization.Away g T] {n m : ℕ}
    (P : Generators R S (Fin n)) (Q : Generators R T (Fin m)) :
    Nonempty (((T ⊗[S] P.toExtension.Cotangent) × (Fin m → T)) ≃ₗ[T]
      (Q.toExtension.Cotangent × (Fin n → T)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.134, Tag 00S0](https://stacks.math.columbia.edu/tag/00S0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
