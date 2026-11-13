---
declaration: section
origin: cited
lean: SheafOfModules.LocalHom, SheafOfModules.LocalHom.comp, SheafOfModules.LocalHom.diffTo_comp, SheafOfModules.sheafHomComp, SheafOfModules.sheafHomComp_leibniz, SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv, SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_add, SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_smul
statement: formalized
proof: formalized
---

# 24.16 Internal hom for sheaves of differential graded modules

Section 24.16 of the Stacks Project, [Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN). 1 tag here is carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FRN, the section

[Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN) in the Stacks Project.

**`SheafOfModules.LocalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean#L168). The attribute's comment: “a local section of SheafHom^n\_A(M, L) over U: an A|\_U-linear map M|\_U → L|\_U homogeneous of degree n”.

> A local section of `SheafHom^n_A(M, L)` over `U`: a map `M|_U → L|_U` of right differential
> graded `A|_U`-modules homogeneous of degree `n`.

```lean
structure LocalHom (M : DifferentialGradedModule.{t, a, w} A)
    (L : DifferentialGradedModule.{t, a, z} A) (n : ℤ) (U : C)
    extends LocalGradedHom M L n U
```

**`SheafOfModules.LocalHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean#L234). The attribute's comment: “the composition map of the internal hom on local sections: composition of homogeneous A|\_U-linear maps, of degree n + m”.

> The composition of local homomorphisms of right differential graded `A|_U`-modules.

```lean
def LocalHom.comp {K : DifferentialGradedModule.{t, a, s} A}
    {M : DifferentialGradedModule.{t, a, w} A} {L : DifferentialGradedModule.{t, a, z} A}
    {n m nm : ℤ} {U : C} (g : LocalHom K M n U) (f : LocalHom M L m U) (h : n + m = nm) :
    LocalHom K L nm U
```

**`SheafOfModules.LocalHom.diffTo_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L116). The attribute's comment: “the Leibniz rule d(f ∘ g) = d(f) ∘ g + (-1)^m f ∘ d(g) on local sections”.

> **The Leibniz rule for the composition of the internal hom**, on local homomorphisms: for
> `g` of degree `n` and `f` of degree `m`, `d(f ∘ g) = d(f) ∘ g + (-1)^m f ∘ d(g)`. Here
> `f ∘ g` is `g.comp f`, and the degrees are free so that both sides are local homomorphisms of
> one and the same degree.

```lean
theorem diffTo_comp (g : LocalHom K L n U) (f : LocalHom L M m U) {k l : ℤ} (h : n + m = k)
    (hl : k + 1 = l) :
    (g.comp f h).diffTo l hl =
      g.comp f.diffAt (by omega) + (m.negOnePow : ℤ) • g.diffAt.comp f (by omega)
```

**`SheafOfModules.sheafHomComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L147). The attribute's comment: “the composition map SheafHom^m(L, M) × SheafHom^n(K, L) → SheafHom^\{n + m}(K, M), O-bilinear and compatible with restriction”.

> **The composition map of the internal hom**
> `SheafHom^m_A(L, M) × SheafHom^n_A(K, L) ⟶ SheafHom^{n + m}_A(K, M)`, `(f, g) ↦ f ∘ g`: an
> `O`-bilinear map of sheaves of `O`-modules, given on local sections by composition of local
> homomorphisms.

```lean
noncomputable def sheafHomComp (K : DifferentialGradedModule.{t, a, z} A)
    (L : DifferentialGradedModule.{t, a, s} A) (M : DifferentialGradedModule.{t, a, w} A)
    (m n : ℤ) :
    BilinearMap ((sheafHomComplex L M).X m) ((sheafHomComplex K L).X n)
      ((sheafHomComplex K M).X (n + m))
```

**`SheafOfModules.sheafHomComp_leibniz`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L177). The attribute's comment: “the composition map is a morphism of differential graded O-modules: d(f ∘ g) = d(f) ∘ g + (-1)^m f ∘ d(g)”.

> **The composition map of the internal hom is a morphism of differential graded
> `O`-modules**: `d(f ∘ g) = d(f) ∘ g + (-1)^m f ∘ d(g)` for a local section `f` of
> `SheafHom^m_A(L, M)` and a local section `g` of `SheafHom^n_A(K, L)`.

```lean
theorem sheafHomComp_leibniz (K : DifferentialGradedModule.{t, a, z} A)
    (L : DifferentialGradedModule.{t, a, s} A) (M : DifferentialGradedModule.{t, a, w} A)
    (m n : ℤ) (U : C) (f : ((sheafHomComplex L M).X m).val.obj (op U))
    (g : ((sheafHomComplex K L).X n).val.obj (op U)) :
    ((sheafHomComplex K M).d (n + m) (n + m + 1)).val.app (op U)
        ((sheafHomComp K L M m n).app (op U) f g) =
      gradedCast (fun q => ((sheafHomComplex K M).X q).val.obj (op U)) (add_assoc n m 1).symm
          ((sheafHomComp K L M (m + 1) n).app (op U)
            (((sheafHomComplex L M).d m (m + 1)).val.app (op U) f) g) +
        (m.negOnePow : ℤ) •
          gradedCast (fun q => ((sheafHomComplex K M).X q).val.obj (op U)) (add_right_comm n 1 m)
            ((sheafHomComp K L M m (n + 1)).app (op U) f
              (((sheafHomComplex K L).d n (n + 1)).val.app (op U) g))
```

**`SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L223). The attribute's comment: “Hom\_\{Mod^dg(A)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) in each degree”.

> **`Hom_{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg_A(K, L))`**, in degree `n`: a homogeneous
> right-linear map `K ⟶ L` of degree `n` is the same thing as a global section of
> `SheafHom^n_A(K, L)`, the section over `U` being the restriction of the map to `K|_U → L|_U`.

```lean
noncomputable def homogeneousMapSectionsEquiv (K L : DifferentialGradedModule.{u, a, w} A)
    (n : ℤ) : HomogeneousMap A K L n ≃ ((sheafHomComplex K L).X n).sections
```

**`SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L246). The attribute's comment: “Hom\_\{Mod^dg(A)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is additive”.

> The identification of homogeneous maps with global sections of the internal hom is
> additive: a homogeneous map `χ` with underlying cochain `φ + φ'` goes to the sum of the global
> sections of `φ` and `φ'`.

```lean
theorem homogeneousMapSectionsEquiv_add (φ φ' χ : HomogeneousMap A K L n)
    (hχ : χ.val = φ.val + φ'.val) (U : X.Cᵒᵖ) :
    (homogeneousMapSectionsEquiv K L n χ).eval U =
      (homogeneousMapSectionsEquiv K L n φ).eval U +
        (homogeneousMapSectionsEquiv K L n φ').eval U
```

**`SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L261). The attribute's comment: “Hom\_\{Mod^dg(A)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is linear over R = Γ(C, O)”.

> The identification of homogeneous maps with global sections of the internal hom is linear
> over `R = Γ(C, O)`: a homogeneous map `χ` which is `r • φ`, i.e. whose components are those of
> `φ` multiplied by the image of `r` in the ring of sections over every object, goes to the global
> section of `φ` multiplied by the image of `r` over every object.

```lean
theorem homogeneousMapSectionsEquiv_smul (r : (limit X.O.obj : CommRingCat.{u}))
    (φ χ : HomogeneousMap A K L n)
    (hχ : ∀ (i j : ℤ) (hij : i + n = j) (U : X.Cᵒᵖ) (x : (K.complex.X i).val.obj U),
      (χ.val.v i j hij).val.app U x =
        (show (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj U from
            ((forget₂ CommRingCat RingCat).map (limit.π X.O.obj U)).hom r) •
          (φ.val.v i j hij).val.app U x)
    (U : X.Cᵒᵖ) :
    (homogeneousMapSectionsEquiv K L n χ).eval U =
      (show (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj U from
          ((forget₂ CommRingCat RingCat).map (limit.π X.O.obj U)).hom r) •
        (homogeneousMapSectionsEquiv K L n φ).eval U
```

**`SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L283). The attribute's comment: “Hom\_\{Mod^dg(A)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is compatible with the differentials”.

> The identification of homogeneous maps with global sections of the internal hom is
> compatible with the differentials: the commutator `δ φ` of a homogeneous map goes to the
> differential of the global section of `φ`.

```lean
theorem homogeneousMapSectionsEquiv_delta (φ : HomogeneousMap A K L n)
    (χ : HomogeneousMap A K L (n + 1)) (hχ : χ.val = δ n (n + 1) φ.val) (U : X.C) :
    (homogeneousMapSectionsEquiv K L (n + 1) χ).eval (op U) =
      ((sheafHomComplex K L).d n (n + 1)).val.app (op U)
        ((homogeneousMapSectionsEquiv K L n φ).eval (op U))
```

**`SheafOfModules.DifferentialGradedModule.homogeneousMapSectionsEquiv_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L300). The attribute's comment: “Hom\_\{Mod^dg(A)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is compatible with composition”.

> The identification of homogeneous maps with global sections of the internal hom is
> compatible with composition: the composite `ψ ∘ φ` of homogeneous maps goes to the image of the
> global sections of `ψ` and `φ` under the composition map of the internal hom.

```lean
theorem homogeneousMapSectionsEquiv_comp (φ : HomogeneousMap A K L n)
    (ψ : HomogeneousMap A L M m) (χ : HomogeneousMap A K M (n + m))
    (hχ : χ.val = φ.val.comp ψ.val rfl) (U : X.Cᵒᵖ) :
    (homogeneousMapSectionsEquiv K M (n + m) χ).eval U =
      (sheafHomComp K L M m n).app U ((homogeneousMapSectionsEquiv L M m ψ).eval U)
        ((homogeneousMapSectionsEquiv K L n φ).eval U)
```

**`SheafOfModules.DifferentialGradedModule.dgHomSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L320). The attribute's comment: “Hom\_\{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)), in the differential graded category”.

> **`Hom_{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg_A(K, L))`** in degree `n`, read in the
> differential graded category `Mod^dg(A, d)` itself.

```lean
noncomputable def dgHomSectionsEquiv (K L : DifferentialGradedModule.{u, a, w} A) (n : ℤ) :
    D.category.Hom (moduleObject A D K) (moduleObject A D L) n ≃
      ((sheafHomComplex K L).X n).sections
```

**`SheafOfModules.DifferentialGradedModule.dgHomSectionsEquiv_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L328). The attribute's comment: “Hom\_\{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is additive”.

> The identification of the morphisms of `Mod^dg(A, d)` with global sections of the internal
> hom is additive.

```lean
theorem dgHomSectionsEquiv_add
    (f g : D.category.Hom (moduleObject A D K) (moduleObject A D L) n) (U : X.Cᵒᵖ) :
    (dgHomSectionsEquiv D K L n (f + g)).eval U =
      (dgHomSectionsEquiv D K L n f).eval U + (dgHomSectionsEquiv D K L n g).eval U
```

**`SheafOfModules.DifferentialGradedModule.dgHomSectionsEquiv_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L338). The attribute's comment: “Hom\_\{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is compatible with the differentials”.

> The identification of the morphisms of `Mod^dg(A, d)` with global sections of the internal
> hom is compatible with the differentials.

```lean
theorem dgHomSectionsEquiv_d
    (f : D.category.Hom (moduleObject A D K) (moduleObject A D L) n) (U : X.C) :
    (dgHomSectionsEquiv D K L (n + 1) (D.category.d f)).eval (op U) =
      ((sheafHomComplex K L).d n (n + 1)).val.app (op U)
        ((dgHomSectionsEquiv D K L n f).eval (op U))
```

**`SheafOfModules.DifferentialGradedModule.dgHomSectionsEquiv_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomComposition.lean#L350). The attribute's comment: “Hom\_\{Mod^dg(A, d)}(K, L) = Γ(C, SheafHom^dg\_A(K, L)) is compatible with composition”.

> The identification of the morphisms of `Mod^dg(A, d)` with global sections of the internal
> hom is compatible with composition: the composite `g ∘ f` goes to the image of the global
> sections of `g` and `f` under the composition map of the internal hom.

```lean
theorem dgHomSectionsEquiv_comp
    (g : D.category.Hom (moduleObject A D L) (moduleObject A D M) m)
    (f : D.category.Hom (moduleObject A D K) (moduleObject A D L) n) (U : X.Cᵒᵖ) :
    (dgHomSectionsEquiv D K M (n + m) (D.category.comp (add_comm m n) g f)).eval U =
      (sheafHomComp K L M m n).app U ((dgHomSectionsEquiv D L M m g).eval U)
        ((dgHomSectionsEquiv D K L n f).eval U)
```

**`SheafOfModules.LocalHom.diffAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean#L311). The attribute's comment: “the differential d(f) = d\_L ∘ f - (-1)^n f ∘ d\_K, homogeneous of degree n + 1 and A-linear”.

> The differential `d(f) = d_L ∘ f - (-1)^n f ∘ d_K` of a degree-`n` local homomorphism, a
> degree-`(n + 1)` local homomorphism.

```lean
def diffAt (f : LocalHom K L n U) : LocalHom K L (n + 1) U
```

**`SheafOfModules.LocalHom.diffAt_diffAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean#L394). The attribute's comment: “the differential of the internal hom squares to zero”.

> The differential of the internal hom squares to zero.

```lean
theorem diffAt_diffAt (f : LocalHom K L n U) : f.diffAt.diffAt = 0
```

**`SheafOfModules.localHomPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean#L625). The attribute's comment: “the local homomorphisms form a sheaf SheafHom^n\_A(K, L) of O-modules”.

> **The local homomorphisms form a sheaf**: the presheaf `U ↦ SheafHom^n_A(K, L)(U)` satisfies
> the sheaf condition.

```lean
theorem localHomPresheaf_isSheaf (K : DifferentialGradedModule.{t, a, z} A)
    (L : DifferentialGradedModule.{t, a, s} A) (n : ℤ) :
    Presheaf.IsSheaf J (localHomPresheaf K L n).presheaf
```

**`SheafOfModules.sheafHomComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean#L676). The attribute's comment: “the internal hom SheafHom^dg\_A(K, L) = ⨁\_n SheafHom^n\_A(K, L), a complex of O-modules”.

> **The internal hom `SheafHom^dg_A(K, L)`**, as a complex of sheaves of `R`-modules: in degree
> `n` the sheaf of degree-`n` local homomorphisms `K|_U → L|_U`, with differential
> `d(f) = d_L ∘ f - (-1)^n f ∘ d_K`.

```lean
noncomputable abbrev sheafHomComplex (K : DifferentialGradedModule.{t, a, z} A)
    (L : DifferentialGradedModule.{t, a, s} A) :
    CochainComplex (SheafOfModules.{max u v z s} R) ℤ
```

**`SheafOfModules.isInternalHom_sheafHomComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHomSheaf.lean#L707). The attribute's comment: “the sections of SheafHom^n\_A(K, L) over U are the A|\_U-linear maps K|\_U → L|\_U homogeneous of degree n, and its differential is d(f) = d\_L ∘ f - (-1)^n f ∘ d\_K”.

> **The constructed complex is the internal hom**: its sections are the local homomorphisms,
> additively, `R`-linearly and compatibly with restriction, and its differential is
> `SheafOfModules.localDiffApp`.

```lean
noncomputable def isInternalHom_sheafHomComplex (K : DifferentialGradedModule.{t, a, z} A)
    (L : DifferentialGradedModule.{t, a, s} A) :
    IsInternalHom K L (sheafHomComplex K L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.16, Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
