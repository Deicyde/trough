---
declaration: section
origin: cited
lean: DifferentialGradedModule.IsAdmissibleMono, DifferentialGradedModule.IsAdmissibleEpi, DifferentialGradedModule.IsAdmissibleShortExact, DifferentialGradedModule.isAdmissibleShortExact_gradedSplit, DifferentialGraded.LeftModule.IsAdmissibleMono, DifferentialGraded.LeftModule.IsAdmissibleEpi, DifferentialGraded.LeftModule.IsAdmissibleShortExact, DifferentialGradedModule.connectingHom
statement: formalized
proof: formalized
---

# 22.7 Admissible short exact sequences

Section 22.7 of the Stacks Project, [Tag 09JS](https://stacks.math.columbia.edu/tag/09JS). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09JT, a definition

[Tag 09JT](https://stacks.math.columbia.edu/tag/09JT) in the Stacks Project.

**`DifferentialGradedModule.IsAdmissibleMono`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean#L64). The attribute's comment: “part (1)”.

> A homomorphism of differential graded modules is an admissible monomorphism if it has a
> retraction by a map of graded right modules.

```lean
abbrev IsAdmissibleMono {K L : DifferentialGradedModule A} (f : Hom K L) : Prop
```

**`DifferentialGradedModule.IsAdmissibleEpi`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean#L75). The attribute's comment: “part (2)”.

> A homomorphism of differential graded modules is an admissible epimorphism if it has a
> section by a map of graded right modules.

```lean
abbrev IsAdmissibleEpi {L M : DifferentialGradedModule A} (g : Hom L M) : Prop
```

**`DifferentialGradedModule.IsAdmissibleShortExact`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Admissible.lean#L86). The attribute's comment: “part (3)”.

> A short exact sequence of differential graded modules that splits as a sequence of graded
> modules.

```lean
structure IsAdmissibleShortExact {K L M : DifferentialGradedModule A}
    (f : Hom K L) (g : Hom L M) : Prop
```

**`DifferentialGradedModule.isAdmissibleShortExact_gradedSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean#L106). The attribute's comment: “a graded splitting is an admissible short exact sequence”.

> **The two closed arrows of a graded-split short exact sequence are an admissible short exact
> sequence.** Injectivity, surjectivity and exactness are all consequences of the four identities
> of the graded splitting, and the splitting itself witnesses admissibility of the two arrows.

```lean
theorem isAdmissibleShortExact_gradedSplit :
    IsAdmissibleShortExact (homOfCocycle A E.a) (homOfCocycle A E.b)
```

**`DifferentialGraded.LeftModule.IsAdmissibleMono`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean#L185). The attribute's comment: “part (1)”.

> A homomorphism of left differential graded modules is an admissible monomorphism if it has a
> retraction by a map of graded left modules.

```lean
abbrev IsAdmissibleMono {K L : LeftModule A} (f : Hom K L) : Prop
```

**`DifferentialGraded.LeftModule.IsAdmissibleEpi`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean#L196). The attribute's comment: “part (2)”.

> A homomorphism of left differential graded modules is an admissible epimorphism if it has a
> section by a map of graded left modules.

```lean
abbrev IsAdmissibleEpi {L M : LeftModule A} (g : Hom L M) : Prop
```

**`DifferentialGraded.LeftModule.IsAdmissibleShortExact`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean#L207). The attribute's comment: “part (3)”.

> A short exact sequence of left differential graded modules that splits as a sequence of
> graded modules.

```lean
structure IsAdmissibleShortExact {K L M : LeftModule A} (f : Hom K L) (g : Hom L M) : Prop
```

## Tag 09JU, a lemma

[Tag 09JU](https://stacks.math.columbia.edu/tag/09JU) in the Stacks Project.

**`DifferentialGradedModule.connectingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/ConnectingHom.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/ConnectingHom.lean#L101). The attribute's comment: “clause (i): δ = π ∘ d\_L ∘ s is a morphism M ⟶ K[1] of differential graded A-modules”.

> The connecting homomorphism `M ⟶ K[1]` associated to graded splittings of an admissible short
> exact sequence of differential graded modules, bundled with the formula `δ x = π (d_L (s x))`.
>
> This is the first half of Stacks 09JU: the family `π ∘ d_L ∘ s` is a morphism of
> `Mod_{(A,d)}`, i.e. it is `A`-linear, of degree `0` as a map into the shift, and commutes with
> the differentials.

```lean
noncomputable def connectingHom (f : Hom K L) (g : Hom L M)
    (hfg : IsAdmissibleShortExact f g) (s : GradedHom M L) (π : GradedHom L K)
    (hs : ∀ x : M.M, g.toFun (s.toFun x) = x)
    (hπ : ∀ x : K.M, π.toFun (f.toFun x) = x)
    (hker : LinearMap.ker π.toFun = LinearMap.range s.toFun) :
    {δ : Hom M (shift K 1) // ∀ x : M.M, δ.toFun x = π.toFun (L.d (s.toFun x))}
```

**`DifferentialGradedModule.homologyMap_connectingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/ConnectingHomBoundary.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/ConnectingHomBoundary.lean#L158). The attribute's comment: “clause (ii): δ induces the boundary maps of the long exact cohomology sequence”.

> **Stacks 09JU**, second clause: the connecting homomorphism `δ = π ∘ d_L ∘ s : M ⟶ K[1]` of
> an admissible short exact sequence of differential graded modules induces the boundary maps of
> the long exact cohomology sequence of 09JK.
>
> The boundary map is the `δ` of the short exact sequence of underlying cochain complexes, i.e. the
> one appearing in `DifferentialGradedModule.longExactCohomology`; the cohomology of `K[1]` in
> degree `n` is identified with that of `K` in degree `n + 1` by the shift isomorphism of
> `HomologicalComplex.homologyFunctor`, as in 011H.
>
> The proof transports 011K, the same statement for a degreewise split short exact sequence of
> cochain complexes, along `forgetToCochainComplex`.

```lean
theorem homologyMap_connectingHom (hS : S.ShortExact)
    (hfg : IsAdmissibleShortExact S.f S.g)
    (sec : GradedHom S.X₃ S.X₂) (ret : GradedHom S.X₂ S.X₁)
    (hs : ∀ x : S.X₃.M, S.g.toFun (sec.toFun x) = x)
    (hret : ∀ x : S.X₁.M, ret.toFun (S.f.toFun x) = x)
    (hker : LinearMap.ker ret.toFun = LinearMap.range sec.toFun)
    (n m : ℤ) (hnm : (ComplexShape.up ℤ).Rel n m) (hm : 1 + n = m) :
    HomologicalComplex.homologyMap
        ((forgetToCochainComplex A).map
            (connectingHom S.f S.g hfg sec ret hs hret hker).val ≫
          (shiftToCochainComplexIso S.X₁).hom) n ≫
        ((HomologicalComplex.homologyFunctor (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).shiftIso
          1 n m hm).hom.app S.X₁.toCochainComplex =
      (shortExact_forgetToCochainComplex A S hS).δ n m hnm
```

## Tag 09JV, a lemma

[Tag 09JV](https://stacks.math.columbia.edu/tag/09JV) in the Stacks Project.

**`DifferentialGradedModule.AdmissibleSquare.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/AdmissibleSequence.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/AdmissibleSequence.lean#L296). The attribute's comment: “(1)”.

> **Statement 1** (Stacks Tag 09JV).  Consider a square of homomorphisms of
> differential graded `𝒜`-modules
> ```
> K --f--> L
> |a       |b
> v        v
> M --g--> N
> ```
> that commutes up to homotopy, i.e. `b ∘ f` is homotopic to `g ∘ a`.  If `f` is an
> admissible monomorphism, then `b` is homotopic to a homomorphism `b' : L → N`
> that makes the diagram commute strictly: `b' ∘ f = g ∘ a`.

```lean
theorem statement1 {K L M N : DGModule 𝒜}
    (f : Hom K L) (a : Hom K M) (b : Hom L N) (g : Hom M N)
    (hf : IsAdmissibleMono f)
    (hcomm : Homotopic (b.comp f) (g.comp a)) :
    ∃ b' : Hom L N, Homotopic b b' ∧
      ∀ x, b'.toLinearMap (f.toLinearMap x) = g.toLinearMap (a.toLinearMap x)
```

**`DifferentialGradedModule.AdmissibleSquare.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/AdmissibleSequence.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/AdmissibleSequence.lean#L323). The attribute's comment: “(2)”.

> **Statement 2** (Stacks Tag 09JV).  With the same setup as Statement 1, if
> `g` is an admissible epimorphism, then `a` is homotopic to a homomorphism
> `a' : K → M` that makes the diagram commute strictly: `g ∘ a' = b ∘ f`.

```lean
theorem statement2 {K L M N : DGModule 𝒜}
    (f : Hom K L) (a : Hom K M) (b : Hom L N) (g : Hom M N)
    (hg : IsAdmissibleEpi g)
    (hcomm : Homotopic (b.comp f) (g.comp a)) :
    ∃ a' : Hom K M, Homotopic a a' ∧
      ∀ x, g.toLinearMap (a'.toLinearMap x) = b.toLinearMap (f.toLinearMap x)
```

## Tag 09JW, a lemma

[Tag 09JW](https://stacks.math.columbia.edu/tag/09JW) in the Stacks Project.

**`DifferentialGradedModule.exists_factorization_isAdmissibleMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/AdmissibleFactorization.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/AdmissibleFactorization.lean#L65).

> A homomorphism of differential graded modules factors through an admissible monomorphism,
> followed by a homomorphism which is split and a homotopy equivalence.

```lean
theorem exists_factorization_isAdmissibleMono (α : K ⟶ L) :
    ∃ (L' : DifferentialGradedModule.{u, v, w} A) (α' : K ⟶ L')
      (π : L' ⟶ L) (s : L ⟶ L'),
      α' ≫ π = α ∧ IsAdmissibleMono α' ∧
        s ≫ π = 𝟙 L ∧ Homotopic (π ≫ s) (𝟙 L')
```

## Tag 09JX, a lemma

[Tag 09JX](https://stacks.math.columbia.edu/tag/09JX) in the Stacks Project.

**`DifferentialGradedModule.exists_admissibleMono_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/AdmissibleFactorization.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/AdmissibleFactorization.lean#L288).

> Replace a finite sequence of differential graded modules by one whose arrows are admissible
> monomorphisms, compatibly with homotopy equivalences to the original sequence.

```lean
theorem exists_admissibleMono_sequence (n : ℕ)
    (L : Fin (n + 1) → DifferentialGradedModule.{u, v, w} A)
    (f : ∀ i : Fin n, Hom (L i.castSucc) (L i.succ)) :
    ∃ (M : Fin (n + 1) → DifferentialGradedModule.{u, v, w} A)
      (g : ∀ i : Fin n, Hom (M i.castSucc) (M i.succ))
      (p : ∀ i : Fin (n + 1), Hom (M i) (L i)),
      (∀ i, IsAdmissibleMono (g i)) ∧
      (∀ i, IsHomotopyEquivalence (p i)) ∧
      (∀ i : Fin n, Hom.comp (p i.succ) (g i) = Hom.comp (f i) (p i.castSucc))
```

## Tag 09JY, a lemma

[Tag 09JY](https://stacks.math.columbia.edu/tag/09JY) in the Stacks Project.

**`DifferentialGradedModule.comp_homotopic_zero_of_isAdmissibleShortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyRectification.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/HomotopyRectification.lean#L302).

> A map which becomes null-homotopic after projection onto the quotient, followed by a map
> which is null-homotopic on the sub-object, has null-homotopic composite.

```lean
theorem comp_homotopic_zero_of_isAdmissibleShortExact
    (f₂ : Hom K₂ L₂) (g₂ : Hom L₂ M₂) (h₂ : IsAdmissibleShortExact f₂ g₂)
    (b : Hom L₁ L₂) (b' : Hom L₂ L₃)
    (hright₁ : Homotopic (Hom.comp g₂ b) 0)
    (hleft₂ : Homotopic (Hom.comp b' f₂) 0) :
    Homotopic (Hom.comp b' b) 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.7, Tag 09JS](https://stacks.math.columbia.edu/tag/09JS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
