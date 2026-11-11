---
declaration: section
origin: cited
lean: HomotopyCategory.instIsHomologicalIntUpHomologyFunctor, CategoryTheory.Functor.homologySequenceComposableArrows₅_exact, HomotopyCategory.isSaturated_subcategoryAcyclic_and_quasiIso_and_kernel_eq, DerivedCategory.plus_iff, DerivedCategory.minus_iff, DerivedCategory.bounded_iff, DerivedCategory, DerivedCategory.homologyFunctor
statement: formalized
proof: formalized
---

# 13.11 Derived categories

Section 13.11 of the Stacks Project, [Tag 05RR](https://stacks.math.columbia.edu/tag/05RR). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05RS, a lemma

[Tag 05RS](https://stacks.math.columbia.edu/tag/05RS) in the Stacks Project.

Declarations registered for the tag:

- [`HomotopyCategory.instIsHomologicalIntUpHomologyFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.instIsHomologicalIntUpHomologyFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L159) (StacksFrontier): “Hⁿ : K(A) ⥤ A is homological”.

## Tag 05ST, an equation

[Tag 05ST](https://stacks.math.columbia.edu/tag/05ST) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.homologySequenceComposableArrows₅_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.homologySequenceComposableArrows₅_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L79) (StacksFrontier).

## Tag 05RT, a lemma

[Tag 05RT](https://stacks.math.columbia.edu/tag/05RT) in the Stacks Project.

**`HomotopyCategory.isSaturated_subcategoryAcyclic_and_quasiIso_and_kernel_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L255). References: SGA 4½ Etat 0 (2.4.1), “case D = K(A), H = H^0”; SGA 4½ Etat 0 (3.1.6), “H^i factors via D(A)”; SGA 4½ Etat 0 (1.2.3), “(A)”; SGA 4½ Etat 0 (4.2.3), “partial”.

> **Stacks 05RT.** Let `A` be an abelian category, let `K(A)` be the homotopy category of
> cochain complexes in `A` and let `L : K(A) ⥤ D` be a localization of `K(A)` at the class of
> quasi-isomorphisms. Then:
>
> * the subcategory `Ac(A)` of acyclic complexes is a strictly full saturated triangulated
>   subcategory of `K(A)`;
> * the saturated multiplicative system corresponding to it under [Stacks, Tag 05RL], namely the
>   class of morphisms whose cone is acyclic, is the class `Qis(A)` of quasi-isomorphisms;
> * the kernel of `L` is `Ac(A)`;
> * every cohomology functor `Hⁿ : K(A) ⥤ A` factors through `L`.

```lean
public theorem isSaturated_subcategoryAcyclic_and_quasiIso_and_kernel_eq
    (L : HomotopyCategory A (ComplexShape.up ℤ) ⥤ D)
    [L.IsLocalization (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))] :
    ((HomotopyCategory.subcategoryAcyclic A).IsClosedUnderIsomorphisms ∧
        (HomotopyCategory.subcategoryAcyclic A).IsTriangulated ∧
        (HomotopyCategory.subcategoryAcyclic A).IsSaturated) ∧
      ((HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).IsSaturated ∧
        (HomotopyCategory.subcategoryAcyclic A).trW =
          HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ∧
      L.kernel = HomotopyCategory.subcategoryAcyclic A ∧
      ∀ n : ℤ, ∃ H : D ⥤ A,
        Nonempty (L ⋙ H ≅ HomotopyCategory.homologyFunctor A (ComplexShape.up ℤ) n)
```

## Tag 05RU, a definition

[Tag 05RU](https://stacks.math.columbia.edu/tag/05RU) in the Stacks Project.

**`DerivedCategory.plus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L762). The attribute's comment: “Ob(D^+(A)) = \{X | H^n(X) = 0 for all n ≪ 0}”. References: SGA 6 I (1.1.5), “D^+ degree condition”.

> **Stacks 05RU.** The objects of the bounded below derived category `D^{+}(A)`, the full
> subcategory `DerivedCategory.Plus C` of `D(A)` on the object property `plus` of the canonical
> t-structure, are exactly the `X` with `H^n(X) = 0` for all `n ≪ 0`.

```lean
public theorem plus_iff (X : DerivedCategory C) :
    (TStructure.t (C := C)).plus X ↔
      ∃ N : ℤ, ∀ n ≤ N, IsZero ((homologyFunctor C n).obj X)
```

**`DerivedCategory.minus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 772](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L772). The attribute's comment: “Ob(D^-(A)) = \{X | H^n(X) = 0 for all n ≫ 0}”. References: SGA 6 I (1.1.5), “D^- degree condition”.

> **Stacks 05RU.** The objects of the bounded above derived category `D^{-}(A)`, the full
> subcategory `DerivedCategory.Minus C` of `D(A)` on the object property `minus` of the canonical
> t-structure, are exactly the `X` with `H^n(X) = 0` for all `n ≫ 0`.

```lean
public theorem minus_iff (X : DerivedCategory C) :
    (TStructure.t (C := C)).minus X ↔
      ∃ N : ℤ, ∀ n, N ≤ n → IsZero ((homologyFunctor C n).obj X)
```

**`DerivedCategory.bounded_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L784). The attribute's comment: “Ob(D^b(A)) = \{X | H^n(X) = 0 for all |n| ≫ 0}”. References: SGA 6 I (1.1.5), “D^b degree condition”.

> **Stacks 05RU.** The objects of the bounded derived category `D^b(A)`, the full subcategory
> `DerivedCategory.Bounded C` of `D(A)` on the object property `bounded` of the canonical
> t-structure, are exactly the `X` with `H^n(X) = 0` for all `|n| ≫ 0`: a single bound in the
> source's condition, against the two unrelated bounds of `bounded = plus ⊓ minus`.

```lean
public theorem bounded_iff (X : DerivedCategory C) :
    (TStructure.t (C := C)).bounded X ↔
      ∃ N : ℤ, ∀ n, N ≤ |n| → IsZero ((homologyFunctor C n).obj X)
```

Declarations registered for the tag:

- [`DerivedCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 803](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L803) (StacksFrontier): “D(A), the derived category of an abelian category”. References: SGA 4 XVII (2.1.1), “more general”; SGA 4½ Etat 0 (3.1.1); SGA 4½ Etat 0 (3.1.3); SGA 4½ Rapport (4.1); SGA 5 I (App.1.1); SGA 5 III (1.1), “more general”; SGA 5 IIIB (5.1); SGA 5 IIIB (6.1), “more general”; SGA 6 I (1.1.5), “the derived fiber D(C\_X)”; SGA 6 II (2.2.10); SGA 6 II (2.3.2); SGA 6 III (1.1); SGA 6 III (5.1); SGA 6 IV (2.1), “partial”.
- [`DerivedCategory.homologyFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.homologyFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 818](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L818) (StacksFrontier): “H^0 : D(A) ⥤ A, and its shifts H^n”. References: SGA 4½ Etat 0 (3.1.6).
- [`DerivedCategory.Plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.Plus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 820](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L820) (StacksFrontier): “D^+(A), the bounded below derived category”. References: SGA 4 Vbis (1.3.8); SGA 4 Vbis (2.4.1); SGA 4½ Etat 0 (3.1.1); SGA 4½ Etat 0 (3.1.3); SGA 4½ Rapport (4.1).
- [`DerivedCategory.Minus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.Minus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 826](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L826) (StacksFrontier): “D^-(A), the bounded above derived category”. References: SGA 4½ Etat 0 (3.1.2); SGA 4½ Etat 0 (3.1.3); SGA 4½ Rapport (4.1); SGA 6 I (1.1.5), “the fiber D⁻(C\_X)”.
- [`DerivedCategory.Bounded`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.Bounded#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L831) (StacksFrontier): “D^b(A), the bounded derived category”. References: SGA 4½ Etat 0 (3.1.2); SGA 4½ Etat 0 (3.1.3).

## Tag 05RV, a lemma

[Tag 05RV](https://stacks.math.columbia.edu/tag/05RV) in the Stacks Project.

**`CochainComplex.exists_quasiIso_square_of_isGE_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L313).

> **Stacks 05RV (3).** Let `K` be a cochain complex in an abelian category — or, as stated
> here, in any category with zero morphisms, a zero object and homology — whose cohomology
> vanishes in degrees `< a` and in degrees `> b`. Then there is a commutative square of
> quasi-isomorphisms
> ```
>   M ⟶ N
>   ↓    ↓
>   K ⟶ L
> ```
> with `L` concentrated in degrees `≥ a`, `M` in degrees `≤ b`, and `N` in degrees `a ≤ n ≤ b`,
> i.e. `N` bounded. Parts (1) and (2) of the source are the horizontal, resp. left vertical, map
> alone, and are the quasi-isomorphisms `K.πTruncGE a`, resp. `K.ιTruncLE b`.

```lean
public theorem exists_quasiIso_square_of_isGE_of_isLE
    (K : CochainComplex C ℤ) (a b : ℤ) [K.IsGE a] [K.IsLE b] :
    ∃ (L M N : CochainComplex C ℤ) (f : K ⟶ L) (g : M ⟶ K) (u : M ⟶ N) (v : N ⟶ L)
      (_ : QuasiIso f) (_ : QuasiIso g) (_ : QuasiIso u) (_ : QuasiIso v)
      (_ : L.IsStrictlyGE a) (_ : M.IsStrictlyLE b) (_ : N.IsStrictlyGE a)
      (_ : N.IsStrictlyLE b), g ≫ f = u ≫ v
```

## Tag 05RW, a lemma

[Tag 05RW](https://stacks.math.columbia.edu/tag/05RW) in the Stacks Project.

**`HomotopyCategory.isSaturated_subcategoryAcyclic_inverseImage_and_quasiIso_and_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Basic.lean#L706).

> **Stacks 05RW.** Let `A` be an abelian category. For every triangulated subcategory `P` of
> the homotopy category `K(A)` — in particular for `K⁺(A)`, `K⁻(A)` and `Kᵇ(A)` — the acyclic
> objects of `P` form a strictly full saturated triangulated subcategory `Ac_P` of `P`, the
> quasi-isomorphisms `Qis_P` of `P` form a saturated multiplicative system compatible with the
> triangulation which is the class `Ac_P.trW` corresponding to `Ac_P` under [Stacks, Tag 05RL],
> and the kernel of any localization `L` of `P` at `Qis_P` is `Ac_P`. Moreover:
>
> 1. `DerivedCategory.Plus.Qh : K⁺(A) ⥤ D⁺(A)` is a localization at `Qis⁺(A)`, so that
>    `K⁺(A)/Ac⁺(A) = Qis⁺(A)⁻¹K⁺(A) ⥤ D⁺(A)` is an equivalence;
> 2. the functor `K⁻(A) ⥤ D⁻(A)` induced by `Qh` is a localization at `Qis⁻(A)`;
> 3. the functor `Kᵇ(A) ⥤ Dᵇ(A)` induced by `Qh` is a localization at `Qisᵇ(A)`.

```lean
public theorem isSaturated_subcategoryAcyclic_inverseImage_and_quasiIso_and_isLocalization :
    (∀ (P : ObjectProperty (HomotopyCategory A (ComplexShape.up ℤ))) [P.IsTriangulated]
        (L : P.FullSubcategory ⥤ D)
        [L.IsLocalization ((HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).inverseImage P.ι)],
      (((HomotopyCategory.subcategoryAcyclic A).inverseImage P.ι).IsClosedUnderIsomorphisms ∧
          ((HomotopyCategory.subcategoryAcyclic A).inverseImage P.ι).IsTriangulated ∧
          ((HomotopyCategory.subcategoryAcyclic A).inverseImage P.ι).IsSaturated) ∧
        (((HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).inverseImage P.ι).IsSaturated ∧
          ((HomotopyCategory.quasiIso A
            (ComplexShape.up ℤ)).inverseImage P.ι).IsCompatibleWithTriangulation ∧
          ((HomotopyCategory.subcategoryAcyclic A).inverseImage P.ι).trW =
            (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).inverseImage P.ι) ∧
        L.kernel = (HomotopyCategory.subcategoryAcyclic A).inverseImage P.ι) ∧
    (DerivedCategory.Plus.Qh (C := A)).IsLocalization (HomotopyCategory.Plus.quasiIso A) ∧
    (∃ F : ((CochainComplex.minus A).strictMap
          (HomotopyCategory.quotient A (ComplexShape.up ℤ))).FullSubcategory ⥤
        DerivedCategory.Minus A,
      Nonempty (F ⋙ DerivedCategory.Minus.ι ≅
          ((CochainComplex.minus A).strictMap
            (HomotopyCategory.quotient A (ComplexShape.up ℤ))).ι ⋙ DerivedCategory.Qh) ∧
        F.IsLocalization ((HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).inverseImage
          ((CochainComplex.minus A).strictMap
            (HomotopyCategory.quotient A (ComplexShape.up ℤ))).ι)) ∧
    (∃ F : ((CochainComplex.plus A ⊓ CochainComplex.minus A).strictMap
          (HomotopyCategory.quotient A (ComplexShape.up ℤ))).FullSubcategory ⥤
        DerivedCategory.Bounded A,
      Nonempty (F ⋙ DerivedCategory.Bounded.ι ≅
          ((CochainComplex.plus A ⊓ CochainComplex.minus A).strictMap
            (HomotopyCategory.quotient A (ComplexShape.up ℤ))).ι ⋙ DerivedCategory.Qh) ∧
        F.IsLocalization ((HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).inverseImage
          ((CochainComplex.plus A ⊓ CochainComplex.minus A).strictMap
            (HomotopyCategory.quotient A (ComplexShape.up ℤ))).ι))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.11, Tag 05RR](https://stacks.math.columbia.edu/tag/05RR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
