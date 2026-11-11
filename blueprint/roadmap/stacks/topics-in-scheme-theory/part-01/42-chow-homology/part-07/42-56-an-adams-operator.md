---
declaration: section
origin: cited
lean: AlgebraicGeometry.VectorBundleKZero.exists_secondAdamsOperator, AlgebraicGeometry.VectorBundleKZero.exists_secondAdamsOperator_pullbackRingHom, Stacks.SecondAdamsPerfect.swapSquare_comp_swapSquare, Stacks.SecondAdamsPerfect.swapSquareAction, Stacks.SecondAdamsPerfect.invariantProjector_add_antiInvariantProjector, Stacks.SecondAdamsPerfect.cls_tensorObj_eq_add, Stacks.SecondAdamsPerfect.cls_sub_cls_eq, Stacks.SecondAdamsPerfect.derivedSwapSquare_comp_self
statement: formalized
proof: formalized
---

# 42.56 An Adams operator

Section 42.56 of the Stacks Project, [Tag 0FEI](https://stacks.math.columbia.edu/tag/0FEI). 12 tags here are carried by 62 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FEJ, a lemma

[Tag 0FEJ](https://stacks.math.columbia.edu/tag/0FEJ) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleKZero.exists_secondAdamsOperator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperator.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperator.lean#L555). The attribute's comment: “the ring map, its value on invertible modules and its compatibility with pullback, granted `SquarePowersData`: the filtration of `Sym²` and `⋀²` along a short exact sequence and the two short exact sequences for the squares of a tensor product”.

> **Stacks Project, Tag 0FEJ.** For a scheme `X` there is a ring map
> `ψ² : K₀(Vect(X)) → K₀(Vect(X))` which sends `[ℒ]` to `[ℒ^{⊗2}]` when `ℒ` is invertible and is
> compatible with pullbacks. It is given on the class of a finite locally free module `ℰ` by
> `ψ²([ℰ]) = [Sym² ℰ] - [⋀² ℰ]`.
>
> The three clauses of the source are present: `ψ²` is a `RingHom`, the second conjunct is its
> value on an invertible module, and the third is its commutation with any ring map of
> Grothendieck rings realising pullback of finite locally free modules. The first conjunct records
> the construction `ψ²([ℰ]) = [Sym² ℰ] - [⋀² ℰ]`.
>
> The hypothesis `SquarePowersData X` is the geometric input of the source's proof: the
> filtration of the two squares along a short exact sequence and the two short exact sequences
> computing the squares of a tensor product, neither of which is available in the library. The
> value on an invertible module is not assumed; it is proved.

```lean
theorem exists_secondAdamsOperator (X : Scheme.{u}) (h : SquarePowersData X) :
    ∃ ψ : VectorBundleKZero X →+* VectorBundleKZero X,
      (∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
          ψ (classOf X E) =
            classOf X (secondSymmetricPower X E) - classOf X (secondExteriorPower X E)) ∧
        (∀ L : X.Modules,
          ∀ _ : Stacks.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L,
            ψ (classOf X L) = classOf X (Scheme.Modules.tensorObjRingedSpace X L L)) ∧
        (∀ (Y : Scheme.{u}) (f : Y ⟶ X) (hY : SquarePowersData Y)
            (p : VectorBundleKZero X →+* VectorBundleKZero Y),
          (∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
              p (classOf X E) = classOf Y ((Scheme.Modules.pullback f).obj E)) →
            (∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
              IsFiniteLocallyFree.{u, u, u} (R := Y.ringCatSheaf)
                ((Scheme.Modules.pullback f).obj E)) →
              ∀ a : VectorBundleKZero X, secondAdamsAddHom hY (p a) = p (ψ a))
```

**`AlgebraicGeometry.VectorBundleKZero.exists_secondAdamsOperator_pullbackRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/VectorBundleKZeroPullback.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/VectorBundleKZeroPullback.lean#L211). The attribute's comment: “the family of ring maps `ψ²_X`, its value on finite locally free and on invertible modules, and its compatibility with pullback `ψ²_Y ∘ f^* = f^* ∘ ψ²_X` for the pullback ring map `f^*` of `K₀(Vect(-))` constructed here; no hypothesis”.

> For every scheme `X` there is a ring map `ψ²_X : K₀(Vect(X)) → K₀(Vect(X))` with
> `ψ²_X([ℰ]) = [Sym² ℰ] - [⋀² ℰ]` on finite locally free modules, `ψ²_X([ℒ]) = [ℒ ⊗ ℒ]` on
> invertible modules, and compatible with pullbacks: for every morphism `f : Y ⟶ X`,
> `ψ²_Y ∘ f^* = f^* ∘ ψ²_X`, where `f^*` is the pullback ring map `pullbackRingHom f`.

```lean
theorem exists_secondAdamsOperator_pullbackRingHom :
    ∃ ψ : ∀ X : Scheme.{u}, VectorBundleKZero X →+* VectorBundleKZero X,
      (∀ (X : Scheme.{u}) (E : X.Modules),
          IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
            ψ X (classOf X E) =
              classOf X (secondSymmetricPower X E) - classOf X (secondExteriorPower X E)) ∧
        (∀ (X : Scheme.{u}) (L : X.Modules),
          Stacks.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L →
            ψ X (classOf X L) = classOf X (Scheme.Modules.tensorObjRingedSpace X L L)) ∧
        (∀ {X Y : Scheme.{u}} (f : Y ⟶ X),
          (ψ Y).comp (pullbackRingHom f) = (pullbackRingHom f).comp (ψ X))
```

## Tag 0FEK, a remark

[Tag 0FEK](https://stacks.math.columbia.edu/tag/0FEK) in the Stacks Project.

**`Stacks.SecondAdamsPerfect.swapSquare_comp_swapSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L150). The attribute's comment: “the switch of the two factors of a tensor square is an involution”.

> **The switch is an involution.** This is the symmetry of the commutativity constraint, read
> at `(L, L)`, and it is what makes the group `{±1}` act on `L ⊗ L`.

```lean
theorem swapSquare_comp_swapSquare (L : C) : swapSquare L ≫ swapSquare L = 𝟙 (L ⊗ L)
```

**`Stacks.SecondAdamsPerfect.swapSquareAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L157). The attribute's comment: “the action of the group of units \{±1} on the tensor square by switching the two factors”.

> **The action of the group `{±1}` on `L ⊗ L` by switching the factors**: the unit `1` acts by
> the identity and the unit `-1` by the switch, which is an involution.

```lean
def swapSquareAction (L : C) : ℤˣ →* End (L ⊗ L)
```

**`Stacks.SecondAdamsPerfect.invariantProjector_add_antiInvariantProjector`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L198). The attribute's comment: “the invariant and anti-invariant projectors of the switch are complementary”.

> The two projectors are complementary: their sum is the identity of `L ⊗ L`.

```lean
theorem invariantProjector_add_antiInvariantProjector :
    invariantProjector R L + antiInvariantProjector R L = 𝟙 (L ⊗ L)
```

**`Stacks.SecondAdamsPerfect.cls_tensorObj_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L342). The attribute's comment: “the class of the tensor square is the sum of the classes of the invariants and of the anti-invariants of the switch”.

> **`[L ⊗ L] = [(L ⊗ L)^+] + [(L ⊗ L)^-]` in the `K`-group**: the invariants and the
> anti-invariants of the switch exhibit the tensor square as their biproduct, and the split
> triangle on a biproduct is distinguished.

```lean
theorem cls_tensorObj_eq_add (P : IdempotentSplitting (invariantProjector R L))
    (N : IdempotentSplitting (antiInvariantProjector R L)) :
    K0.cls (L ⊗ L) = K0.cls P.obj + K0.cls N.obj
```

**`Stacks.SecondAdamsPerfect.cls_sub_cls_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L368). The attribute's comment: “the difference of the classes of the invariants and of the anti-invariants of the switch on the tensor square is a well-defined element of the K-group attached to the object; its additivity along distinguished triangles is not proved”.

> **The difference `[(L ⊗ L)^+] - [(L ⊗ L)^-]` is independent of the chosen invariants and
> anti-invariants**, hence a well-defined element of the `K`-group attached to `L`. This is the
> value the second Adams operator of the source is to take on `L`.

```lean
theorem cls_sub_cls_eq (P P' : IdempotentSplitting (invariantProjector R L))
    (N N' : IdempotentSplitting (antiInvariantProjector R L)) :
    K0.cls P.obj - K0.cls N.obj = K0.cls P'.obj - K0.cls N'.obj
```

**`Stacks.SecondAdamsPerfect.derivedSwapSquare_comp_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L404). The attribute's comment: “the switch of the two factors of the derived tensor square on a ringed space is an involution”.

> **The switch of the two factors of `L ⊗^L_{O_X} L` is an involution.**

```lean
theorem derivedSwapSquare_comp_self (L : DerivedCategory (StructureSheafModules Rc)) :
    derivedSwapSquare Rc L ≫ derivedSwapSquare Rc L = 𝟙 (((derivedTensor Rc).obj L).obj L)
```

**`Stacks.SecondAdamsPerfect.derivedSwapSquareAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfect.lean#L412). The attribute's comment: “the action of the group \{±1} on the derived tensor square of an object of D(O\_X) by switching the two factors”.

> **The action of the group `{±1}` on `L ⊗^L_{O_X} L` by switching the factors**, in the
> derived category of a ringed space.

```lean
def derivedSwapSquareAction (L : DerivedCategory (StructureSheafModules Rc)) :
    ℤˣ →* End (((derivedTensor Rc).obj L).obj L)
```

**`AlgebraicGeometry.secondAdamsPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean#L148). The attribute's comment: “the second Adams operator ψ² on K₀(D\_perf(𝒪\_X)), for any model of D(𝒪\_X), as an additive endomorphism; its value on classes is `secondAdamsPerfect_cls`, and its well-definedness (additivity along distinguished triangles) is `secondAdamsPerfect_distinguished`”.

> The second Adams operator `ψ²` on `K₀(D_perf(𝒪_X))`, for a scheme `X` on which `2` is
> invertible: the additive endomorphism sending the class of a perfect object `L` to
> `[(L ⊗^L L)^+] - [(L ⊗^L L)^-]` (`secondAdamsPerfect_cls`).

```lean
def secondAdamsPerfect (h2 : IsUnit (2 : Γ(X, ⊤))) :
    K0 𝒟ₚ →+ K0 𝒟ₚ
```

**`AlgebraicGeometry.exists_switchSplittings_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean#L160). The attribute's comment: “the invariants (L ⊗^L L)^+ and the anti-invariants (L ⊗^L L)^- of the switch on the derived tensor square of a perfect object exist, and are perfect for every choice”.

> For a perfect object `L` of `D(𝒪_X)`, with `2` invertible on `X`, the idempotents `(𝟙 + σ)/2`
> and `(𝟙 - σ)/2` of the switch `σ` of `L ⊗^L L` split, and the objects splitting them — the
> invariants `(L ⊗^L L)^+` and the anti-invariants `(L ⊗^L L)^-` — are perfect, whichever splittings
> are taken.

```lean
theorem exists_switchSplittings_perfect (h2 : IsUnit (2 : Γ(X, ⊤))) (L : 𝒟ₚ) :
    letI := derivedMonoidal X.toRingedSpace.sheaf
    letI := derivedSymmetric X.toRingedSpace.sheaf
    haveI := isIso_two_smul_id X.toRingedSpace.sheaf (isUnit_two_presheaf_obj X h2)
    Nonempty (IdempotentSplitting
        (invariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _))) ∧
      Nonempty (IdempotentSplitting
        (antiInvariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _))) ∧
      (∀ s : IdempotentSplitting
        (invariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _)),
          IsPerfect (X := X.toRingedSpace) s.obj) ∧
      (∀ s : IdempotentSplitting
        (antiInvariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _)),
          IsPerfect (X := X.toRingedSpace) s.obj)
```

**`AlgebraicGeometry.secondAdamsPerfect_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean#L185). The attribute's comment: “ψ²([L]) = [(L ⊗^L L)^+] - [(L ⊗^L L)^-] for every perfect L and every choice of the invariants and the anti-invariants of the switch”.

> For a scheme `X` on which `2` is invertible and a perfect object `L` of `D(𝒪_X)`, the second
> Adams operator sends the class of `L` to the class of the invariants minus the class of the
> anti-invariants of the switch on `L ⊗^L L`, for any choice of the two (which exist and are perfect
> by `exists_switchSplittings_perfect`).

```lean
theorem secondAdamsPerfect_cls (h2 : IsUnit (2 : Γ(X, ⊤))) (L : 𝒟ₚ) :
    letI := derivedMonoidal X.toRingedSpace.sheaf
    letI := derivedSymmetric X.toRingedSpace.sheaf
    haveI := isIso_two_smul_id X.toRingedSpace.sheaf (isUnit_two_presheaf_obj X h2)
    ∀ (sp : IdempotentSplitting
        (invariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _)))
      (sm : IdempotentSplitting
        (antiInvariantIdempotent ((β_ L.obj L.obj).hom : L.obj ⊗ L.obj ⟶ _)))
      (hp : IsPerfect (X := X.toRingedSpace) sp.obj) (hm : IsPerfect (X := X.toRingedSpace) sm.obj),
      secondAdamsPerfect X h2 (K0.cls L) = K0.cls (⟨sp.obj, hp⟩ : 𝒟ₚ) -
        K0.cls (⟨sm.obj, hm⟩ : 𝒟ₚ)
```

**`AlgebraicGeometry.secondAdamsPerfect_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean#L210). The attribute's comment: “well-definedness on K₀: [(L ⊗^L L)^+] - [(L ⊗^L L)^-] is additive along distinguished triangles of D\_perf(𝒪\_X), for every choice of invariants and anti-invariants”.

> For a distinguished triangle `L₁ ⟶ L₂ ⟶ L₃ ⟶ L₁[1]` of `D_perf(𝒪_X)`, `2` being invertible on
> `X`, and for any choices `sᵢ^±` of the invariants and the anti-invariants of the switch on
> `Lᵢ ⊗^L Lᵢ`,
>
> `[s₂^+] - [s₂^-] = ([s₁^+] - [s₁^-]) + ([s₃^+] - [s₃^-])`
>
> in `K₀(D_perf(𝒪_X))`.

```lean
theorem secondAdamsPerfect_distinguished (h2 : IsUnit (2 : Γ(X, ⊤)))
    (T : Triangle 𝒟ₚ) (hT : T ∈ distTriang _) :
    letI := derivedMonoidal X.toRingedSpace.sheaf
    letI := derivedSymmetric X.toRingedSpace.sheaf
    haveI := isIso_two_smul_id X.toRingedSpace.sheaf (isUnit_two_presheaf_obj X h2)
    ∀ (sp₁ : IdempotentSplitting
        (invariantIdempotent ((β_ T.obj₁.obj T.obj₁.obj).hom : T.obj₁.obj ⊗ T.obj₁.obj ⟶ _)))
      (sm₁ : IdempotentSplitting
        (antiInvariantIdempotent ((β_ T.obj₁.obj T.obj₁.obj).hom : T.obj₁.obj ⊗ T.obj₁.obj ⟶ _)))
      (sp₂ : IdempotentSplitting
        (invariantIdempotent ((β_ T.obj₂.obj T.obj₂.obj).hom : T.obj₂.obj ⊗ T.obj₂.obj ⟶ _)))
      (sm₂ : IdempotentSplitting
        (antiInvariantIdempotent ((β_ T.obj₂.obj T.obj₂.obj).hom : T.obj₂.obj ⊗ T.obj₂.obj ⟶ _)))
      (sp₃ : IdempotentSplitting
        (invariantIdempotent ((β_ T.obj₃.obj T.obj₃.obj).hom : T.obj₃.obj ⊗ T.obj₃.obj ⟶ _)))
      (sm₃ : IdempotentSplitting
        (antiInvariantIdempotent ((β_ T.obj₃.obj T.obj₃.obj).hom : T.obj₃.obj ⊗ T.obj₃.obj ⟶ _)))
      (hp₁ : IsPerfect (X := X.toRingedSpace) sp₁.obj)
      (hm₁ : IsPerfect (X := X.toRingedSpace) sm₁.obj)
      (hp₂ : IsPerfect (X := X.toRingedSpace) sp₂.obj)
      (hm₂ : IsPerfect (X := X.toRingedSpace) sm₂.obj)
      (hp₃ : IsPerfect (X := X.toRingedSpace) sp₃.obj)
      (hm₃ : IsPerfect (X := X.toRingedSpace) sm₃.obj),
      K0.cls (⟨sp₂.obj, hp₂⟩ : 𝒟ₚ) -
          K0.cls (⟨sm₂.obj, hm₂⟩ : 𝒟ₚ) =
        (K0.cls (⟨sp₁.obj, hp₁⟩ : 𝒟ₚ) -
          K0.cls (⟨sm₁.obj, hm₁⟩ : 𝒟ₚ)) +
        (K0.cls (⟨sp₃.obj, hp₃⟩ : 𝒟ₚ) -
          K0.cls (⟨sm₃.obj, hm₃⟩ : 𝒟ₚ))
```

**`AlgebraicGeometry.perfectKZeroSecondAdams`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/SecondAdamsOperatorPerfectKZero.lean#L250). The attribute's comment: “ψ² on K₀(X) = PerfectKZero X of Tag 0FDG: `secondAdamsPerfect` at the standard model of D(𝒪\_X) that PerfectKZero is defined with”.

> The second Adams operator on the group `AlgebraicGeometry.PerfectKZero X = K₀(D_perf(𝒪_X))`
> of [Stacks, Tag 0FDG]: `secondAdamsPerfect` at the standard model of the derived category.

```lean
def perfectKZeroSecondAdams (h2 : IsUnit (2 : Γ(X, ⊤))) : PerfectKZero X →+ PerfectKZero X
```

## Tag 0FV8, a lemma

[Tag 0FV8](https://stacks.math.columbia.edu/tag/0FV8) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleKZero.exists_minusOneAdamsOperator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MinusAdamsOperator.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MinusAdamsOperator.lean#L411). The attribute's comment: “the ring map, its values on finite locally free modules and its compatibility with pullback”. References: SGA 6 VIII (3.4), “more general”.

> **The minus-one Adams operation.** There is a ring endomorphism `ψ^{-1}` of `K₀(Vect(X))`
> which sends the class of a finite locally free module to the class of its dual, and which
> commutes with duality along any ring map `p : K₀(Vect(X)) → K₀(Vect(Y))` sending the class of a
> finite locally free module `ℰ` to the class of `f^*ℰ`, for a morphism `f : Y ⟶ X`.

```lean
theorem exists_minusOneAdamsOperator (X : Scheme.{u}) :
    ∃ ψ : VectorBundleKZero X →+* VectorBundleKZero X,
      (∀ M : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M →
          ψ (classOf X M) = classOf X (dualSheaf X.toRingedSpace M)) ∧
        ∀ (Y : Scheme.{u}) (f : Y ⟶ X) (p : VectorBundleKZero X →+* VectorBundleKZero Y),
          (∀ M : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M →
              p (classOf X M) = classOf Y ((Scheme.Modules.pullback f).obj M)) →
            ∀ a : VectorBundleKZero X,
              dualAddHom (dualPreservesFiniteLocallyFree Y) (dualShortExact Y) (p a) = p (ψ a)
```

## Tag 0FEL, a remark

[Tag 0FEL](https://stacks.math.columbia.edu/tag/0FEL) in the Stacks Project.

**`Stacks.Chow.totalChernKGroupMap_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/KGroupChernClass.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/KGroupChernClass.lean#L251).

> **Stacks 0FEL.** Let `X` be locally of finite type over the base of chapter 42. The Chern
> class map `c : K_0(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X)`:
>
> 1. sends a generator `[ℰ]`, `ℰ` finite locally free of any rank, to
>    `c(ℰ) = 1 + c_1(ℰ) + c_2(ℰ) + …`, whose degree-`p` component is the Chern class `c_p(ℰ)` of
>    Stacks 0ESW and whose degree-`0` component is `1`;
> 2. is multiplicative, `c(α + β) = c(α) c(β)`;
> 3. sends `−[ℰ]` to the formal inverse of `c(ℰ)`, a two-sided inverse in `∏_{i ≥ 0} A^i(X)`;
> 4. is the only map with properties 1 and 2 (it is obtained "by extending multiplicatively").
>
> It is well defined by the Whitney sum formula, Stacks 02UI
> (`Stacks.Chow.totalChernClassOfModule_eq_mul_of_shortExact`).

```lean
theorem totalChernKGroupMap_spec :
    (∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
      totalChernKGroupMap C sX (VectorBundleKZero.classOf X E) = totalChernClassOfModule C sX E ∧
        totalChernClassOfModule C sX E 0 = (1 : TotalChowClass C sX) 0 ∧
        ∀ p : ℕ, totalChernClassOfModule C sX E p = chernClassOfModule C sX E p) ∧
    (∀ α β : VectorBundleKZero X,
      totalChernKGroupMap C sX (α + β) = totalChernKGroupMap C sX α * totalChernKGroupMap C sX β) ∧
    (∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
      totalChernKGroupMap C sX (-VectorBundleKZero.classOf X E) *
          totalChernClassOfModule C sX E = 1 ∧
        totalChernClassOfModule C sX E *
          totalChernKGroupMap C sX (-VectorBundleKZero.classOf X E) = 1) ∧
    (∀ c : VectorBundleKZero X → TotalChowClass C sX,
      (∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
        c (VectorBundleKZero.classOf X E) = totalChernClassOfModule C sX E) →
      (∀ α β, c (α + β) = c α * c β) → c = totalChernKGroupMap C sX)
```

**`Stacks.Chow.chowCohomologySeries`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean#L185). The attribute's comment: “the target: the product over i >= 0 of the Chow cohomology groups A^i(X), with A^i(X) the group Stacks.Chow.chowCohomologyComponent of Stacks 0B7E”.

> **The target of Stacks 0FEL.** The product `∏_{i ≥ 0} A^i(X)` of the nonnegative-degree Chow
> cohomology groups of a scheme `X` locally of finite type over the base: a family
> `(a_0, a_1, a_2, …)` with `a_i ∈ A^i(X)`, subject to **no** condition on its support.
>
> The product and not the direct sum, and not the completion `A^*(X)^∧` of Stacks 0FE0 either: the
> formal inverse of a total Chern class has a component in every degree in general, and that is the
> reason the source writes an infinite product.

```lean
abbrev chowCohomologySeries : Type (u + 1)
```

**`Stacks.Chow.chernClassKGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean#L665). The attribute's comment: “the map c : K\_0(Vect(X)) -> prod\_\{i >= 0} A^i(X) itself, with K\_0(Vect(X)) the Grothendieck group AlgebraicGeometry.VectorBundleKZero of Stacks 0FDK and A^i(X) the Chow cohomology Stacks.Chow.chowCohomologyComponent of Stacks 0B7E. CARRIED, as the two fields of the parameters R and D: (1) the ring structure of A^*(X)^∧, Stacks 0FE0 -- composition of bivariant classes, whose composite StacksDraft.AlgebraicGeometry.Chow.BivariantComposition .Class constructs as Stacks.Chow.bivariantComposite, though nothing here assembles the ring out of it -- namely a degreewise product A^i x A^j -> A^\{i+j}, additive in each variable, a unit series, and associativity, commutativity and the unit law for the Cauchy product it defines; (2) the total Chern class series c(E) of each module; Stacks 0B7H is constructed here, as Stacks.Chow.chernClass, but relative to the Chern cap products of Stacks 0B7G that the characterization is read against (the parameter Stacks.Chow.HigherChernCapRule), which rest on Stacks 02U5 and 02U7 and are not formalized here; and (3) the Whitney sum formula c(E\_2) = c(E\_1) c(E\_3) of Stacks 02UI in the source's product form, which is the well-definedness. The repository's Stacks 02UI, Stacks.Chow.chernCapOnChow\_eq\_sum\_of\_shortExact, is the relation read componentwise on Chow groups between cap products and does not give the product form: that deduction needs the bivariant Chern classes of Stacks 0B7H, the composition product of Stacks 0FE0 and the compatibility of the cap operation of a composite with the two cap operations; the first two are available, the degreewise product built from the composite and the last are not. NOT carried, and constructed here: the product prod\_\{i >= 0} A^i(X), the Cauchy product on it, the formal inverse of a series with constant term 1 and the proof that it inverts, the group of such series, and the map c with the three properties below”.

> **Stacks 0FEL.** The Chern class map
>
>   `c : K_0(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X)`,
>
> sending the generator `[ℰ]` to `c(ℰ) = 1 + c_1(ℰ) + c_2(ℰ) + …` and extended multiplicatively;
> so `−[ℰ]` goes to the formal inverse `c(ℰ)^{-1}`, which is why the target is the infinite product.
> It is well defined by the Whitney sum formula of Stacks 02UI.

```lean
def chernClassKGroup (D : TotalChernClassSeries C G sX R) :
    AlgebraicGeometry.VectorBundleKZero X → chowCohomologySeries C G sX
```

**`Stacks.Chow.chernClassKGroup_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean#L682). The attribute's comment: “the multiplicativity -- extending multiplicatively -- of the map, which is its well-definedness on K\_0(Vect(X)); the Whitney sum formula of Stacks 02UI is carried, see the attribute on Stacks.Chow.chernClassKGroup”.

> **The Chern class map is multiplicative**, which is what "extending multiplicatively" means:
> the sum in `K_0(Vect(X))` goes to the Cauchy product of series. This is the content Stacks 02UI
> supplies.

```lean
theorem chernClassKGroup_add (D : TotalChernClassSeries C G sX R)
    (α β : AlgebraicGeometry.VectorBundleKZero X) :
    chernClassKGroup D (α + β) =
      chowSeriesMul R.gradedMul (chernClassKGroup D α) (chernClassKGroup D β)
```

**`Stacks.Chow.chernClassKGroup_neg_classOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassKGroup.lean#L710). The attribute's comment: “the clause that -[E] is sent to the formal inverse c(E)^\{-1}, which is why the target is an infinite product; the formal inverse is constructed here by the recursion Stacks.Chow.ChowCohomologySeriesRing.formalInverse\_succ and is not carried”.

> **Stacks 0FEL, the last clause of the remark.** `−[ℰ]` is sent to the formal inverse
> `c(ℰ)^{-1}`: its coefficients are given by the recursion of
> `Stacks.Chow.ChowCohomologySeriesRing.formalInverse_succ`, which is not supported in finitely many
> degrees in general, and the Cauchy product of `c([ℰ])` with it is the unit series. This is why the
> target of the map is the infinite product `∏_{i ≥ 0} A^i(X)` rather than a finite sum.

```lean
theorem chernClassKGroup_neg_classOf (D : TotalChernClassSeries C G sX R) (E : X.Modules) :
    chernClassKGroup D (-AlgebraicGeometry.VectorBundleKZero.classOf X E) =
        R.formalInverse (D.ch E) ∧
      chowSeriesMul R.gradedMul (D.ch E)
        (chernClassKGroup D (-AlgebraicGeometry.VectorBundleKZero.classOf X E)) = R.one
```

## Tag 0FEM, a remark

[Tag 0FEM](https://stacks.math.columbia.edu/tag/0FEM) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleKZero.existsUnique_ringHom_of_tensorMultiplicative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCharacterKGroup.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCharacterKGroup.lean#L43). The attribute's comment: “the canonical ring map on `K₀(Vect(X))` that the Chern character defines, and its uniqueness; additivity along short exact sequences (Tag 0F9C), multiplicativity on tensor products (Tag 0F9D) and the value on `𝒪_X` are properties of the Chern character of a module and are hypotheses, and `∏_{i ≥ 0} A^i(X) ⊗ 𝐐` is read as an arbitrary ring, which it has no construction as in this repository”.

> An assignment `ℰ ↦ ch(ℰ)` of an element of a ring `R` to each `𝒪_X`-module which vanishes off
> the finite locally free modules, is additive along their short exact sequences and
> multiplicative on tensor products, and takes the value `1` on `𝒪_X`, extends to a ring
> homomorphism on `K₀(Vect(X))`, and to exactly one. For the Chern character with values in
> `∏_{i ≥ 0} A^i(X) ⊗ 𝐐` this is the ring map `ch : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X) ⊗ 𝐐`.

```lean
theorem existsUnique_ringHom_of_tensorMultiplicative
    (hzero : ∀ M : X.Modules,
      ¬ IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M → ch M = 0)
    (hadd : ∀ {E F G : X.Modules} (f : E ⟶ F) (g : F ⟶ G) (w : f ≫ g = 0),
      IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
        IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) F →
          IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) G →
            Mono f → Epi g → (ShortComplex.mk f g w).Exact → ch F = ch E + ch G)
    (hmul : ∀ M N : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M →
      IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) N →
        ch (Scheme.Modules.tensorObjRingedSpace X M N) = ch M * ch N)
    (hone : ch (SheafOfModules.unit X.ringCatSheaf) = 1) :
    ∃! φ : VectorBundleKZero X →+* R,
      ∀ M : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) M →
        φ (classOf X M) = ch M
```

**`Stacks.Chow.chernCharacterRingHom_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/KGroupChernCharacter.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/KGroupChernCharacter.lean#L346).

> Let `X` be locally of finite type over the base of chapter 42. The Chern character defines a
> canonical ring map
>
>   `ch : K_0(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X) ⊗ 𝐐`
>
> (`Stacks.Chow.chernCharacterRingHom`, a ring homomorphism into the ring
> `Stacks.Chow.instRingFullRationalChowCohomology`) which
>
> 1. sends a generator `[ℰ]`, `ℰ` finite locally free of any rank, to `ch(ℰ)`, whose degree-`p`
>    component is `ch_p(ℰ) = P_p(ℰ)/p!` (`Stacks.Chow.moduleChernCharacterComponent`);
> 2. is the only ring map with property 1 (it is obtained "by extending additively").
>
> It is well defined by Stacks 0F9C (`Stacks.Chow.moduleChernCharacter_eq_add_of_shortExact`) and a
> ring map by Stacks 0F9D (`Stacks.Chow.moduleChernCharacter_tensorObj`).

```lean
theorem chernCharacterRingHom_spec :
    (∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
      chernCharacterRingHom C sX (VectorBundleKZero.classOf X E) = moduleChernCharacter C sX E ∧
        ∀ p : ℕ, chernCharacterRingHom C sX (VectorBundleKZero.classOf X E) p =
          ((Nat.factorial p : ℚ)⁻¹) ⊗ₜ[ℤ] modulePowerSumComponentArbitraryRank C sX E p) ∧
    (∀ φ : VectorBundleKZero X →+* fullRationalChowCohomology C (gysinSystemOfInvertible C) sX,
      (∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
        φ (VectorBundleKZero.classOf X E) = moduleChernCharacter C sX E) →
      φ = chernCharacterRingHom C sX)
```

**`Stacks.Chow.existsUnique_ringHom_chernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChernCharacterMultiplicative.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChernCharacterMultiplicative.lean#L288). The attribute's comment: “the remark as stated: the unique ring map K\_0(Vect(X)) -> prod over i >= 0 of A^i(X) tensor Q sending [E] to ch(E), for every X locally of finite type over S, with no further hypothesis; the target is the ring Stacks.Chow.RationalTotalChowClass C sX (Cauchy product of the products A^i(X) x A^j(X) -> A^\{i+j}(X) of Stacks 0B75, tensored with Q), ch(E) is Stacks.Chow.rationalTotalChernCharacter (components P\_p(E)/p!, E of arbitrary rank), and the map is Stacks.Chow.rationalTotalChernCharacterRingHom; additivity is Stacks 0F9C and multiplicativity Stacks 0F9D, both proved”.

> **Stacks 0FEM.** The Chern character defines a canonical ring map
>
>   `ch : K_0(Vect(X)) ⟶ ∏_{i ≥ 0} A^i(X) ⊗ 𝐐`:
>
> there is a unique ring homomorphism sending the class of every finite locally free `𝒪_X`-module
> `ℰ`, of arbitrary rank, to its Chern character `ch(ℰ) = (P_p(ℰ)/p!)_{p ≥ 0}`. It is
> `Stacks.Chow.rationalTotalChernCharacterRingHom`.

```lean
theorem existsUnique_ringHom_chernCharacter :
    ∃! φ : VectorBundleKZero X →+* RationalTotalChowClass C sX,
      ∀ (E : X.Modules) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E],
        φ (VectorBundleKZero.classOf X E) = rationalTotalChernCharacter C sX E
```

## Tag 0FEN, a lemma

[Tag 0FEN](https://stacks.math.columbia.edu/tag/0FEN) in the Stacks Project.

**`Stacks.Chow.chernClassKGroup_secondAdams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperatorChernScaling.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperatorChernScaling.lean#L620). The attribute's comment: “the first equation, c\_i(psi^2(alpha)) = 2^i c\_i(alpha), for every alpha in K\_0(Vect(X)); psi^2 is AlgebraicGeometry.VectorBundleKZero.secondAdamsRingHom of Stacks 0FEJ and c is Stacks.Chow.chernClassKGroup of Stacks 0FEL, so the parameters R, D and hX are the data those two already carry. CARRIED in addition: (1) the splitting principle of Stacks 02UL, not formalized in this repository, as Stacks.Chow.HasSecondAdamsSplitting -- a family of morphisms p\_r : P\_r -> X, jointly injective on each A^i(X), along each of which [E] becomes a sum of classes of invertible modules, together with the restriction map of Stacks 0B7F and its multiplicativity and Chern class compatibility (which Stacks 0B7F does not formalize, needing the composition product of Stacks 0FE0) and the functoriality of K\_0(Vect(-)) (which this repository does not construct, as the notes of StacksFrontier.AlgebraicGeometry.Chow.SecondAdamsOperator record); the family rather than a single morphism is what keeps modules of non-constant rank in scope, since the source reduces to constant rank over the rank loci (Stacks 0ESW) before applying Stacks 02UL; and (2) Stacks 02U0 and Stacks 02SZ, the vanishing of c\_j of an invertible module above degree 1 and the additivity c\_1(L tensor L) = 2 c\_1(L), with Stacks 01CT (1), as Stacks.Chow.InvertibleChernClassData -- properties of the bivariant Chern classes of Stacks 0B7H, which this repository characterizes but does not construct. NOT carried, and proved here: that the 2^i-scaling of A^i(X) is a ring endomorphism of the product (the source's first step, which is what reduces the lemma to additive generators), the base case c(L tensor L) = 1 + 2 c\_1(L), the value psi^2([L]) = [L tensor L] (proved in Stacks 0FEJ), the computation of c(psi^2(alpha)) on a sum of classes of invertible modules, and the descent along the pullback”.

> **Stacks Project, Tag 0FEN, the first equation.** Let `(S, δ)` be as in Stacks 02QL, let `X`
> be locally of finite type over `S`, let `ψ²` be the second Adams operation of Stacks 0FEJ and let
> `c` be the Chern class map of Stacks 0FEL. Then
>
>   `c_i(ψ²(α)) = 2^i c_i(α)`
>
> for every `α ∈ K_0(Vect(X))` and every `i ≥ 0`.
>
> The parameters `R`, `D` and `hX` are the data Stacks 0FEL and Stacks 0FEJ already carry; `hsplit`
> is the splitting principle of Stacks 02UL, which the source's proof uses and which this
> repository does not have, in the shape `Stacks.Chow.SecondAdamsSplitting` records. The scaling
> map is not assumed to be a ring map, the base case is not assumed, and the descent is proved.

```lean
theorem chernClassKGroup_secondAdams {D : TotalChernClassSeries C G sX R}
    (hX : SquarePowersData X)
    (hsplit : ∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
      HasSecondAdamsSplitting C G sX R D hX E)
    (α : VectorBundleKZero X) (i : ℕ) :
    chernClassKGroup D (secondAdamsRingHom hX α) i =
      ((2 : ℕ) ^ i) • chernClassKGroup D α i
```

**`Stacks.Chow.chernCharacterKGroup_secondAdams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperatorChernScaling.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperatorChernScaling.lean#L704). The attribute's comment: “the second equation, ch\_i(psi^2(alpha)) = 2^i ch\_i(alpha), for every alpha in K\_0(Vect(X)); ch is Stacks.Chow.chernCharacterKGroup, the Chern character of Stacks 0FEM written out as ch\_p(alpha) = P\_p(c\_1(alpha), ..., c\_p(alpha))/p! in the product over p >= 0 of A^p(X) tensor Q, which is the library's Stacks.Chow.fullRationalChowCohomology. It is deduced from the first equation rather than proved by a second splitting argument. CARRIED in addition to what the first equation carries: the power sums P\_p themselves, as Stacks.Chow.NewtonPowerSums, with their additivity for the Cauchy product (Stacks 0F9C) and their weighted homogeneity of degree p -- Stacks.Chow.powerSumClassArbitraryRank of Stacks 0ESX assembles the power sums over the rank loci from a quantified family rather than from a polynomial expression, so neither property can be read off here. The weighted homogeneity is a combinatorial property of P\_p alone, with no geometry in it”.

> **Stacks Project, Tag 0FEN, the second equation.** In the situation of
> `Stacks.Chow.chernClassKGroup_secondAdams`, with `ch` the Chern character of Stacks 0FEM,
>
>   `ch_i(ψ²(α)) = 2^i ch_i(α)`
>
> for every `α ∈ K_0(Vect(X))` and every `i ≥ 0`.
>
> This is deduced from the first equation in its series form,
> `Stacks.Chow.chernClassKGroup_secondAdams_eq_chowSeriesScale`, together with the weighted
> homogeneity of the Newton power sums: `ch_i` is `P_i(c_1, …, c_i)/i!` and `P_i` is weighted
> homogeneous of degree `i`. No second splitting argument is needed.

```lean
theorem chernCharacterKGroup_secondAdams {D : TotalChernClassSeries C G sX R}
    (N : NewtonPowerSums C G sX R) (hX : SquarePowersData X)
    (hsplit : ∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
      HasSecondAdamsSplitting C G sX R D hX E)
    (α : VectorBundleKZero X) (i : ℕ) :
    chernCharacterKGroup (D := D) N (secondAdamsRingHom hX α) i =
      ((2 : ℕ) ^ i) • chernCharacterKGroup (D := D) N α i
```

**`Stacks.Chow.chernClass_chernCharacter_secondAdams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/SecondAdamsChernScaling.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/SecondAdamsChernScaling.lean#L513).

> Let `(S, δ)` be as in Situation 02QL and let `X` be locally of finite type over `S`. Let `ψ²`
> be the second Adams operator of Stacks 0FEJ
> (`AlgebraicGeometry.VectorBundleKZero.secondAdamsRingHom` at
> `AlgebraicGeometry.VectorBundleKZero.squarePowersData X`), and let `c` and `ch` be the maps of
> Stacks 0FEL and Stacks 0FEM (`Stacks.Chow.totalChernKGroupMap`, into `∏_{i ≥ 0} A^i(X)`, and
> `Stacks.Chow.chernCharacterRingHom`, into `∏_{i ≥ 0} A^i(X) ⊗ 𝐐`). Then for every
> `α ∈ K_0(Vect(X))` and every `i`
>
>   `c_i(ψ²(α)) = 2^i c_i(α)`  and  `ch_i(ψ²(α)) = 2^i ch_i(α)`,
>
> the subscript `i` being the component in `A^i(X)`, resp. `A^i(X) ⊗ 𝐐`.

```lean
theorem chernClass_chernCharacter_secondAdams (α : VectorBundleKZero X) (i : ℕ) :
    totalChernKGroupMap C sX
        (VectorBundleKZero.secondAdamsRingHom (VectorBundleKZero.squarePowersData X) α) i =
      (2 ^ i : ℤ) • totalChernKGroupMap C sX α i ∧
    chernCharacterRingHom C sX
        (VectorBundleKZero.secondAdamsRingHom (VectorBundleKZero.squarePowersData X) α) i =
      (2 ^ i : ℤ) • chernCharacterRingHom C sX α i
```

**`Stacks.Chow.chernCharacterVectorBundle_secondAdams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean#L245). The attribute's comment: “the ch\_i equation: ch\_p(ψ²(α)) = 2^p ch\_p(α), for every α ∈ K\_0(Vect(X)) and every X locally of finite type over S, with no further hypothesis: ψ² is AlgebraicGeometry.VectorBundleKZero.secondAdamsRingHom (Stacks 0FEJ) and ch is Stacks.Chow.chernCharacterVectorBundle (Stacks 0FEM), with values in A^p(X) ⊗ Q”.

> **Stacks Project, Tag 0FEN, the second equation.** Let `(S, δ)` be as in Situation 42.7.1 and
> let `X` be locally of finite type over `S`. For every `α ∈ K_0(Vect(X))` and every `p ≥ 0`,
>
>   `ch_p(ψ²(α)) = 2^p ch_p(α)`   in `A^p(X) ⊗ 𝐐`,
>
> where `ψ²` is the second Adams operation of Stacks 0FEJ and `ch` the Chern character of
> Stacks 0FEM.

```lean
theorem chernCharacterVectorBundle_secondAdams (a : VectorBundleKZero X) (p : ℕ) :
    chernCharacterVectorBundle C sX (secondAdamsRingHom (squarePowersData X) a) p =
      (2 ^ p : ℚ) • chernCharacterVectorBundle C sX a p
```

**`Stacks.Chow.totalChernKClass_secondAdams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsTotalChern.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsTotalChern.lean#L475). The attribute's comment: “the c\_i equation: c\_i(ψ²(α)) = 2^i c\_i(α) in A^i(X), for every α ∈ K\_0(Vect(X)) and every X locally of finite type over S, with no further hypothesis: ψ² is AlgebraicGeometry.VectorBundleKZero.secondAdamsRingHom (Stacks 0FEJ) and c is the total Chern class map of Remark 0FEL, Stacks.Chow.totalChernKClass, constructed here for modules of arbitrary rank”.

> **Stacks Project, Tag 0FEN, the first equation.** Let `(S, δ)` be as in Situation 42.7.1 and
> let `X` be locally of finite type over `S`. For every `α ∈ K_0(Vect(X))` and every `i ≥ 0`,
>
>   `c_i(ψ²(α)) = 2^i c_i(α)`   in `A^i(X)`,
>
> where `ψ²` is the second Adams operation of Stacks 0FEJ and `c` the total Chern class of
> Remark 0FEL (`Stacks.Chow.totalChernKClass`).

```lean
theorem totalChernKClass_secondAdams (a : VectorBundleKZero X) (i : ℕ) :
    totalChernKClass C sX (secondAdamsRingHom (squarePowersData X) a) i =
      (2 ^ i : ℤ) • totalChernKClass C sX a i
```

## Tag 0FEP, a remark

[Tag 0FEP](https://stacks.math.columbia.edu/tag/0FEP) in the Stacks Project.

**`AlgebraicGeometry.supportedPerfectEulerHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean#L166). The attribute's comment: “the homomorphism K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)). Two departures from the source, both recorded in the module docstring: the value on a class is the alternating sum ∑\_n (-1)^n [H^n(E)] rather than [⊕\_n H^\{2n}(E)] - [⊕\_n H^\{2n+1}(E)] (the same element of K\_0, but the identification of the two expressions is NOT proved here), and X is assumed Noetherian regular, the hypotheses of Stacks 0FER, rather than merely locally Noetherian, because the global coherence and boundedness of the cohomology sheaves used here come from the converse half of Stacks 0FDC. The identification K\_0(Coh\_Z(X)) = K'\_0(Z) is Stacks 0FDT and is NOT covered”.

> The homomorphism `K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))`. Let `X` be a Noetherian regular
> scheme and `Z ⊂ X` a closed subscheme. Taking the alternating sum of the cohomology sheaves of a
> perfect complex supported on `Z` defines a homomorphism from the `K`-group of `D_{Z, perf}(𝒪_X)`
> to the Grothendieck group of coherent `𝒪_X`-modules supported on `Z`.

```lean
def supportedPerfectEulerHom :
    Pretriangulated.K0 (supportedPerfectDerivedCategory i) →+ KZero (SupportedCoherentModules i)
```

**`AlgebraicGeometry.supportedPerfectEulerHom_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean#L174). The attribute's comment: “the defining property of the homomorphism, in the alternating-sum form”.

> The homomorphism `K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))` sends the
> class of a perfect complex `E` supported on `Z` to the alternating sum `∑_n (-1)^n [H^n(E)]` of
> the classes of its cohomology sheaves.

```lean
theorem supportedPerfectEulerHom_cls (E : supportedPerfectDerivedCategory i) :
    supportedPerfectEulerHom i hX (Pretriangulated.K0.cls E) =
      eulerClass (supportedPerfectDerivedCategory i) (SupportedCoherentModules i)
        (supportedPerfectHomology i hX) E
```

**`AlgebraicGeometry.SupportedCoherentModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherent.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherent.lean#L67). The attribute's comment: “supported\_coherent”.

> The full subcategory of coherent sheaves supported on `Z`.

```lean
abbrev SupportedCoherentModules {X Z : Scheme.{u}}
    (i : Z ⟶ X) [IsClosedImmersion i]
```

**`AlgebraicGeometry.supportedCoherentIsSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherent.lean#L98). The attribute's comment: “supported\_coherent”.

> Coherent sheaves supported on a closed subscheme form a Serre subcategory.

```lean
instance supportedCoherentIsSerreClass {X Z : Scheme.{u}}
    [IsLocallyNoetherian X] (i : Z ⟶ X) [IsClosedImmersion i] :
    (supportedCoherentProperty i).IsSerreClass
```

**`AlgebraicGeometry.supportedPerfectEulerHom'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean#L346). The attribute's comment: “the homomorphism K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)), with Coh\_Z(X) spelled as a weak Serre subcategory of all O\_X-modules. As for the nested spelling: the value on a class is the alternating sum ∑\_n (-1)^n [H^n(E)] rather than the source's [⊕\_n H^\{2n}(E)] - [⊕\_n H^\{2n+1}(E)], the same element of K\_0 but the identification of the two expressions is NOT proved; and X is Noetherian regular, the hypotheses of Stacks 0FER, rather than locally Noetherian. The identification K\_0(Coh\_Z(X)) = K'\_0(Z) is Stacks 0FDT and is NOT covered”.

> **The homomorphism `K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))` of [Stacks, Tag 0FEP]**, in the
> unnested spelling of `Coh_Z(X)`: the alternating sum of the classes of the cohomology sheaves of a
> perfect complex supported on `Z`.

```lean
def supportedPerfectEulerHom' :
    Pretriangulated.K0 (supportedPerfectDerivedCategory i) →+
      KZero (coherentSupportedProperty i).FullSubcategory
```

**`AlgebraicGeometry.supportedPerfectEulerHom'_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean#L355). The attribute's comment: “the defining property of the homomorphism, in the alternating-sum form”.

> **[Stacks, Tag 0FEP].** The homomorphism `K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))` sends the
> class of a perfect complex supported on `Z` to the alternating sum of the classes of its cohomology
> sheaves.

```lean
theorem supportedPerfectEulerHom'_cls (E : supportedPerfectDerivedCategory i) :
    supportedPerfectEulerHom' i hX (Pretriangulated.K0.cls E) =
      eulerClass (supportedPerfectDerivedCategory i)
        (coherentSupportedProperty i).FullSubcategory (supportedPerfectHomology' i hX) E
```

**`AlgebraicGeometry.supportedPerfectCohomologyHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean#L427). The attribute's comment: “the homomorphism K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)) for X locally Noetherian and Z ⊂ X a closed subscheme; its defining property is `supportedPerfectCohomologyHom_cls`”.

> **The homomorphism `K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))` of [Stacks, Tag 0FEP].**
> Let `X` be a locally Noetherian scheme and `Z ⊂ X` a closed subscheme. The rule
> `E ↦ [⊕_{i ∈ ℤ} H^{2i}(E)] - [⊕_{i ∈ ℤ} H^{2i + 1}(E)]` is additive on distinguished triangles of
> `D_{Z, perf}(𝒪_X)`, hence defines a homomorphism of groups; its value on the class of `E` is
> `supportedPerfectCohomologyHom_cls`.

```lean
def supportedPerfectCohomologyHom :
    Pretriangulated.K0 (supportedPerfectDerivedCategory.{u, d} i) →+
      KZero (SupportedCoherentModules i)
```

**`AlgebraicGeometry.supportedPerfectCohomologyHom_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean#L445). The attribute's comment: “the defining property: [E] ↦ [⊕\_\{i ∈ ℤ} H^\{2i}(E)] - [⊕\_\{i ∈ ℤ} H^\{2i+1}(E)], the direct sums taken in Mod(O\_X)”.

> **The defining property of the homomorphism of [Stacks, Tag 0FEP].** The class of a perfect
> complex `E` with cohomology sheaves supported on `Z` is sent to
> `[⊕_{i ∈ ℤ} H^{2i}(E)] - [⊕_{i ∈ ℤ} H^{2i + 1}(E)]`, the direct sums being taken in the category
> of `𝒪_X`-modules (`evenHomologySupported_obj_obj`, `oddHomologySupported_obj_obj`).

```lean
theorem supportedPerfectCohomologyHom_cls (E : supportedPerfectDerivedCategory.{u, d} i) :
    supportedPerfectCohomologyHom i (Pretriangulated.K0.cls E) =
      KZero.mk _ (evenHomologySupported i E) - KZero.mk _ (oddHomologySupported i E)
```

**`AlgebraicGeometry.supportedPerfectCohomologyHomToCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean#L454). The attribute's comment: “the same homomorphism with target K'\_0(Z) = K\_0(Coh(Z)), through the identification K\_0(Coh\_Z(X)) = K'\_0(Z) of Stacks 0FDT”.

> **The homomorphism of [Stacks, Tag 0FEP] with target `K'_0(Z) = K_0(Coh(𝒪_Z))`**, through
> the identification `K_0(Coh(𝒪_Z)) ≅ K_0(Coh_Z(X))` of [Stacks, Tag 0FDT].

```lean
def supportedPerfectCohomologyHomToCoherent :
    Pretriangulated.K0 (supportedPerfectDerivedCategory.{u, d} i) →+
      KZero (Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf)
```

**`AlgebraicGeometry.supportedPerfect_isStrictlyFull_isTriangulated_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectCohomologyHom.lean#L504). The attribute's comment: “D\_\{Z, perf}(O\_X) is a strictly full, saturated, triangulated subcategory of D(O\_X): closed under isomorphisms, triangulated, stable under retracts, hence saturated”. References: SGA 6 I (5.8.4), “5.8.4 a), special case”.

> **`D_{Z, perf}(𝒪_X)` is a strictly full, saturated, triangulated subcategory of
> `D(𝒪_X)`.** The perfect complexes of `𝒪_X`-modules whose cohomology sheaves are set-theoretically
> supported on `Z` form a property of objects which is closed under isomorphisms, triangulated, and
> stable under retracts, hence saturated (closed under direct summands).

```lean
theorem supportedPerfect_isStrictlyFull_isTriangulated_isSaturated :
    let P : ObjectProperty (DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)) :=
      fun K => RingedSpace.IsPerfect K ∧
        ∀ n : ℤ, SheafOfModules.supp
          ((DerivedCategory.homologyFunctor (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)
            n).obj K) ⊆ Set.range i.base
    P.IsClosedUnderIsomorphisms ∧ P.IsTriangulated ∧ P.IsStableUnderRetracts ∧
      P.IsSaturated
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.isCoherent_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/LocallyFiniteCohomology.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/LocallyFiniteCohomology.lean#L65). The attribute's comment: “locally\_finite\_cohomology”.

> Every cohomology module of a perfect object on a locally Noetherian scheme is coherent.

```lean
theorem isCoherent_homology (X : Scheme.{u}) [IsLocallyNoetherian X]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) (n : ℤ) :
    _root_.SheafOfModules.IsCoherent
      ((DerivedCategory.homologyFunctor
        (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace) n).obj K)
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.locally_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/LocallyFiniteCohomology.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/LocallyFiniteCohomology.lean#L80). The attribute's comment: “locally\_finite\_cohomology”.

> Near every point only finitely many cohomology modules of a perfect object have nonempty
> support.

```lean
theorem locally_finite_homology (X : Scheme.{u})
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) (x : X) :
    ∃ U : X.Opens, x ∈ U ∧
      {n : ℤ | ∃ y : X, y ∈ U ∧ y ∈ SheafOfModules.supp
        ((DerivedCategory.homologyFunctor
          (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace) n).obj K)}.Finite
```

Declarations registered for the tag:

- [`AlgebraicGeometry.supportedPerfectDerivedCategory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/KGroups/Basic.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectComplexes.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectComplexes.lean#L30) (StacksFrontier): “supported\_perfect\_complexes”.

## Tag 0FEQ, a remark

[Tag 0FEQ](https://stacks.math.columbia.edu/tag/0FEQ) in the Stacks Project.

**`AlgebraicGeometry.coherentToSupportedPerfectHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfect.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfect.lean#L259).

> **Stacks Project, Tag 0FEQ.** Let `i : Z ⟶ X` be a closed immersion of schemes with `X`
> regular. There is a canonical homomorphism `K₀(Coh(𝒪_Z)) → K₀(D_{Z, perf}(𝒪_X))` taking the class
> of a coherent `𝒪_Z`-module `ℱ` to the class of its direct image placed in degree zero.
>
> The source is the Grothendieck group of the abelian category of coherent `𝒪_Z`-modules and the
> target is the `K`-group of the triangulated category of perfect complexes on `X` supported on the
> closed subset underlying `Z`. The map is well defined because the direct image of a short exact
> sequence of coherent modules is short exact, hence gives a distinguished triangle of the three
> degree-zero complexes.

```lean
def coherentToSupportedPerfectHom :
    KZero (Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) →+
      Pretriangulated.K0 (supportedPerfectDerivedCategory i)
```

**`AlgebraicGeometry.coherentToSupportedPerfectHom_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfect.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfect.lean#L269).

> **Stacks Project, Tag 0FEQ.** The canonical homomorphism
> `K₀(Coh(𝒪_Z)) → K₀(D_{Z, perf}(𝒪_X))` takes the class of a coherent `𝒪_Z`-module `ℱ` to the class
> of the perfect complex `(i_*ℱ)[0]`.

```lean
theorem coherentToSupportedPerfectHom_mk
    (F : Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) :
    coherentToSupportedPerfectHom i hX (KZero.mk _ F) =
      Pretriangulated.K0.cls (singlePushforwardSupportedPerfect i hX F)
```

**`AlgebraicGeometry.coherentToSupportedPerfectHomGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfectGeneral.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfectGeneral.lean#L137).

> **Stacks Project, Tag 0FEQ.** Let `i : Z ⟶ X` be a closed immersion of schemes with `X`
> regular. There is a canonical homomorphism `K₀(Coh(𝒪_Z)) → K₀(D_{Z, perf}(𝒪_X))` taking the class
> of a coherent `𝒪_Z`-module `ℱ` to the class of its direct image placed in degree zero.
>
> The source is the Grothendieck group of the abelian category of coherent `𝒪_Z`-modules and the
> target is the `K`-group of the triangulated category of perfect complexes on `X` supported on the
> closed subset underlying `Z`. The map is well defined because the direct image of a short exact
> sequence of coherent modules is short exact, hence gives a distinguished triangle of the three
> degree-zero complexes.

```lean
def coherentToSupportedPerfectHomGeneral
    [HasDerivedCategory.{w} (OXMod.{u, u} X.toRingedSpace)] :
    KZero (Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) →+
      Pretriangulated.K0 (supportedPerfectDerivedCategory i)
```

**`AlgebraicGeometry.coherentToSupportedPerfectHomGeneral_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfectGeneral.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentToSupportedPerfectGeneral.lean#L148).

> **Stacks Project, Tag 0FEQ.** The canonical homomorphism
> `K₀(Coh(𝒪_Z)) → K₀(D_{Z, perf}(𝒪_X))` takes the class of a coherent `𝒪_Z`-module `ℱ` to the class
> of the perfect complex `(i_*ℱ)[0]`.

```lean
theorem coherentToSupportedPerfectHomGeneral_mk
    [HasDerivedCategory.{w} (OXMod.{u, u} X.toRingedSpace)]
    (F : Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) :
    coherentToSupportedPerfectHomGeneral i hX (KZero.mk _ F) =
      Pretriangulated.K0.cls (singlePushforwardSupportedPerfectGeneral i hX F)
```

## Tag 0FER, a lemma

[Tag 0FER](https://stacks.math.columbia.edu/tag/0FER) in the Stacks Project.

**`AlgebraicGeometry.coherentToSupportedPerfectHom_mutuallyInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentSupportedPerfectKGroupIso.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentSupportedPerfectKGroupIso.lean#L239).

> **Stacks Project, Tag 0FER.** Let `X` be a Noetherian regular scheme and `i : Z ⟶ X` a closed
> immersion. The homomorphism `K'_0(Z) = K_0(Coh(𝒪_Z)) → K_0(D_{Z, perf}(𝒪_X))`,
> `[ℱ] ↦ [(i_*ℱ)[0]]`, of [Stacks, Tag 0FEQ] and the homomorphism
> `K_0(D_{Z, perf}(𝒪_X)) → K'_0(Z)`, `[E] ↦ [⊕_n H^{2n}(E)] - [⊕_n H^{2n+1}(E)]`, of
> [Stacks, Tag 0FEP] are mutually inverse.

```lean
theorem coherentToSupportedPerfectHom_mutuallyInverse :
    (supportedPerfectCohomologyHomToCoherent i).comp (coherentToSupportedPerfectHom i hX) =
        AddMonoidHom.id _ ∧
      (coherentToSupportedPerfectHom i hX).comp (supportedPerfectCohomologyHomToCoherent i) =
        AddMonoidHom.id _
```

**`AlgebraicGeometry.coherentKZeroEquivSupportedPerfectKZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentSupportedPerfectKGroupIso.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/CoherentSupportedPerfectKGroupIso.lean#L255). The attribute's comment: “the resulting identification K'\_0(Z) = K\_0(D\_\{Z, perf}(O\_X))”.

> **Stacks Project, Tag 0FER**, as an isomorphism: `K'_0(Z) ≃+ K_0(D_{Z, perf}(𝒪_X))` for a
> closed subscheme `Z` of a Noetherian regular scheme `X`, given by the mutually inverse
> homomorphisms of [Stacks, Tag 0FEQ] and [Stacks, Tag 0FEP].

```lean
def coherentKZeroEquivSupportedPerfectKZero :
    KZero (Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) ≃+
      Pretriangulated.K0 (supportedPerfectDerivedCategory i)
```

**`AlgebraicGeometry.supportedPerfectEulerHom_comp_coherentToSupportedPerfectHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/PerfectToSupportedCoherent.lean#L210). The attribute's comment: “the round trip K\_0(Coh(Z)) → K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)) is the comparison homomorphism of Stacks 0FDT, which is step (1) of the source's proof ('the composite is the identity'), stated without the 0FDT identification because that identification is not available. What is NOT covered: step (2), surjectivity of K\_0(Coh(Z)) → K\_0(D\_\{Z, perf}(O\_X)), which the source gets from the truncation triangles together with the finite filtration of a coherent module supported on Z by O\_Z-modules; and therefore NOT the conclusion that the two maps are mutually inverse”.

> Let `X` be a Noetherian regular scheme and `Z ⊂ X` a closed subscheme. The composite of
> `coherentToSupportedPerfectHom : K_0(Coh(𝒪_Z)) → K_0(D_{Z, perf}(𝒪_X))` with
> `supportedPerfectEulerHom : K_0(D_{Z, perf}(𝒪_X)) → K_0(Coh_Z(X))` is the comparison
> homomorphism `coherentToSupportedCoherentKZeroHom : K_0(Coh(𝒪_Z)) → K_0(Coh_Z(X))` of direct
> image.

```lean
theorem supportedPerfectEulerHom_comp_coherentToSupportedPerfectHom :
    (supportedPerfectEulerHom i hX).comp (coherentToSupportedPerfectHom i hX) =
      coherentToSupportedCoherentKZeroHom i
```

**`AlgebraicGeometry.supportedPerfectEulerHom'_comp_supportedCoherentToPerfectHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean#L383). The attribute's comment: “the identity K\_0(Coh\_Z(X)) → K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)); the identification K\_0(Coh\_Z(X)) = K'\_0(Z) of Stacks 0FDT, under which this is the source's statement about K\_0(Coh(Z)), is NOT covered”.

> **The first of the two inverse identities of [Stacks, Tag 0FER].** Taking the alternating sum
> of the cohomology sheaves of a coherent module supported on `Z`, placed in degree zero, returns the
> class of that module: the only nonvanishing cohomology sheaf is the module itself, in degree zero.

```lean
theorem supportedPerfectEulerHom'_comp_supportedCoherentToPerfectHom :
    (supportedPerfectEulerHom' i hX).comp (supportedCoherentToPerfectHom i hX) =
      AddMonoidHom.id (KZero (coherentSupportedProperty i).FullSubcategory)
```

**`AlgebraicGeometry.supportedCoherentToPerfectHom_comp_supportedPerfectEulerHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentPerfectKGroup.lean#L425). The attribute's comment: “the identity K\_0(D\_\{Z, perf}(O\_X)) → K\_0(Coh\_Z(X)) → K\_0(D\_\{Z, perf}(O\_X)); with supportedPerfectEulerHom'\_comp\_supportedCoherentToPerfectHom this is the source's 'mutually inverse', EXCEPT that the source's left hand side is K'\_0(Z) = K\_0(Coh(Z)) and here it is K\_0(Coh\_Z(X)); the identification of the two is Stacks 0FDT and is NOT covered”.

> **The two homomorphisms of [Stacks, Tag 0FEP] and [Stacks, Tag 0FEQ] are mutually inverse**, so
> `K_0(Coh_Z(X)) = K_0(D_{Z, perf}(𝒪_X))`: the alternating sum of cohomology sheaves and the
> placement of a coherent module supported on `Z` in degree zero compose to the identity in this
> direction, and `supportedPerfectEulerHom'_comp_supportedCoherentToPerfectHom` is the other
> direction.

```lean
theorem supportedCoherentToPerfectHom_comp_supportedPerfectEulerHom' :
    (supportedCoherentToPerfectHom i hX).comp (supportedPerfectEulerHom' i hX) =
      AddMonoidHom.id (Pretriangulated.K0 (supportedPerfectDerivedCategory i))
```

## Tag 0FES, a remark

[Tag 0FES](https://stacks.math.columbia.edu/tag/0FES) in the Stacks Project.

**`Stacks.Chow.localizedChernClassKMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean#L232).

> **Stacks 0FES: the localized Chern class map**
> `c(Z ⟶ X, -) : K₀(D_{Z,perf}(𝒪_X)) ⟶ A⁰(X) × ∏_{i ≥ 1} Aⁱ(Z ⟶ X)`, for `X` locally of finite type
> over `S` with quasi-compact irreducible components (for instance `X` quasi-compact) and a closed
> immersion `i : Z ⟶ X`: the homomorphism from `K₀(D_{Z,perf}(𝒪_X))`, written multiplicatively, to
> the ring `A⁽¹⁾(Z ⟶ X)` with the product of Remark 0FA0, sending `[E]` to
> `c(Z ⟶ X, E) = 1 + c₁(Z ⟶ X, E) + c₂(Z ⟶ X, E) + ⋯`
> (`Stacks.Chow.localizedChernClassKMap_cls`), extended multiplicatively
> (`Stacks.Chow.localizedChernClassKMap_add`). It is well defined by Lemma 0FBD
> (`Stacks.Chow.supportedTotalLocalizedChern_triangle`).

```lean
def localizedChernClassKMap :
    Multiplicative (K0 (supportedPerfectDerivedCategory i)) →*
      localizedBivariantGrading C (gysinSystemOfInvertible C) (i ≫ a) a i rfl 1
```

**`Stacks.Chow.localizedChernClassKMap_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean#L240). The attribute's comment: “the value `c(Z → X, E) = 1 + c_1(Z → X, E) + ⋯` on a generator `[E]`”.

> **Stacks 0FES, the value on a generator**: `c(Z ⟶ X, [E]) = c(Z ⟶ X, E)`.

```lean
theorem localizedChernClassKMap_cls (E : supportedPerfectDerivedCategory i) :
    localizedChernClassKMap C a hX (Multiplicative.ofAdd (K0.cls E)) =
      supportedTotalLocalizedChern C a hX E
```

**`Stacks.Chow.localizedChernClassKMap_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernClassKMap.lean#L248). The attribute's comment: “the map is extended multiplicatively: `c(Z → X, α + β) = c(Z → X, α) c(Z → X, β)`”.

> **Stacks 0FES, multiplicativity**: `c(Z ⟶ X, α + β) = c(Z ⟶ X, α) c(Z ⟶ X, β)` in
> `A⁽¹⁾(Z ⟶ X)`.

```lean
theorem localizedChernClassKMap_add (α β : K0 (supportedPerfectDerivedCategory i)) :
    localizedChernClassKMap C a hX (Multiplicative.ofAdd (α + β)) =
      localizedChernClassKMap C a hX (Multiplicative.ofAdd α) *
        localizedChernClassKMap C a hX (Multiplicative.ofAdd β)
```

## Tag 0FET, a remark

[Tag 0FET](https://stacks.math.columbia.edu/tag/0FET) in the Stacks Project.

**`Stacks.Chow.localizedChernCharKMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean#L227).

> **The localized Chern character map of Stacks 0FET**
> `ch(Z ⟶ X, -) : K₀(D_{Z,perf}(𝒪_X)) ⟶ ∏_{p ≥ 0} A^p(Z ⟶ X) ⊗ 𝐐`, for `X` with quasi-compact
> irreducible components: `[E] ↦ ch(Z ⟶ X, E)`, extended additively. It is well defined because the
> localized Chern character is additive along distinguished triangles (Lemma 0FBE,
> `Stacks.Chow.supportedLocalizedChernChar_triangle`).

```lean
def localizedChernCharKMap :
    K0 (supportedPerfectDerivedCategory i) →+
      ∀ p : ℕ, TensorProduct ℤ ℚ (BivariantClass C (gysinSystemOfInvertible C) (i ≫ a) a i rfl
        (p : ℤ))
```

**`Stacks.Chow.localizedChernCharKMap_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean#L236). The attribute's comment: “localized\_chern\_character\_k\_map: the generator [E] is sent to ch(Z → X, E), and the map is the additive extension”.

> The localized Chern character map on a class: `[E] ↦ ch(Z ⟶ X, E)`.

```lean
theorem localizedChernCharKMap_cls (E : supportedPerfectDerivedCategory i) :
    localizedChernCharKMap C a hX (K0.cls E) = supportedLocalizedChernChar C a hX E
```

**`Stacks.Chow.exists_localizedChernCharKMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterKMap.lean#L329). The attribute's comment: “localized\_chern\_character\_k\_finite\_support: for X quasi-compact the image lies in A^*(Z → X) ⊗ Q, every value having finitely many nonzero components”.

> If `X` is quasi-compact, the localized Chern character map takes values in `A^*(Z ⟶ X) ⊗ 𝐐`:
> every value has only finitely many nonzero components.

```lean
theorem exists_localizedChernCharKMap_eq_zero (x : K0 (supportedPerfectDerivedCategory i)) :
    ∃ N, ∀ p ≥ N, localizedChernCharKMap C a hX x p = 0
```

**`Stacks.Chow.localizedChernCharKMap_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterRing.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedChernCharacterRing.lean#L249). The attribute's comment: “localized\_chern\_character\_k\_multiplicative: ch(Z → X, αβ) = ch(Z → X, α) ch(Z → X, β), the product on K\_0(D\_\{Z,perf}(O\_X)) being derived tensor product (0FDN) and that on ∏ A^p(Z → X) ⊗ Q the Cauchy product of the products res(c) ∘ c' of 0FA0”.

> **The localized Chern character map is multiplicative.** For `X` with quasi-compact
> irreducible components and `α, β ∈ K₀(D_{Z,perf}(𝒪_X))`, multiplied by the derived tensor product
> (Remark 0FDN),
>
>   `ch(Z ⟶ X, α β) = ch(Z ⟶ X, α) ch(Z ⟶ X, β)`
>
> in `∏_{p ≥ 0} A^p(Z ⟶ X) ⊗ 𝐐` (`Stacks.Chow.rationalSupportedProductMul`).

```lean
theorem localizedChernCharKMap_mul (x y : K0 (supportedPerfectDerivedCategory i)) :
    localizedChernCharKMap C a hX (x * y) =
      rationalSupportedProductMul C a i (localizedChernCharKMap C a hX x)
        (localizedChernCharKMap C a hX y)
```

## Tag 0FEU, a remark

[Tag 0FEU](https://stacks.math.columbia.edu/tag/0FEU) in the Stacks Project.

**`AlgebraicGeometry.supportedPerfectDerivedCategory_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean#L100). The attribute's comment: “supported\_perfect”.

> **Stacks 0FEU.** Perfect objects of the derived category supported on the whole scheme are
> exactly the perfect objects: `D_{X, perf}(O_X) = D_perf(O_X)`.

```lean
theorem supportedPerfectDerivedCategory_id (X : Scheme.{u}) :
    supportedPerfectDerivedCategory (𝟙 X) = PerfectDerivedCategory X
```

**`AlgebraicGeometry.supportedPerfectKZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean#L111). The attribute's comment: “k\_group”.

> **Stacks 0FEU.** The `K`-group of perfect complexes supported on the whole scheme is the
> Grothendieck group `K_0(X) = K_0(D_perf(O_X))` of the scheme.

```lean
noncomputable def supportedPerfectKZeroEquiv (X : Scheme.{u}) :
    Pretriangulated.K0 (supportedPerfectDerivedCategory (𝟙 X)) ≃+
      Pretriangulated.K0 (PerfectDerivedCategory X)
```

**`AlgebraicGeometry.supportedPerfectKZeroEquiv_cls`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedPerfectWholeScheme.lean#L163). The attribute's comment: “k\_group”.

> **Stacks 0FEU.** The identification of `K`-groups takes the class of a perfect complex
> supported on the whole scheme to the class of the same complex in `K_0(D_perf(O_X))`.

```lean
theorem supportedPerfectKZeroEquiv_cls (X : Scheme.{u})
    (K : supportedPerfectDerivedCategory (𝟙 X)) :
    supportedPerfectKZeroEquiv X (Pretriangulated.K0.cls K) =
      Pretriangulated.K0.cls (⟨K.obj, K.property.1⟩ : PerfectDerivedCategory X)
```

**`Stacks.Chow.perfectKZeroChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean#L417). The attribute's comment: “the map c : K\_0(X) -> prod A^i(X), [E] |-> c(E) extended multiplicatively, built directly from Definition 0F9E and Lemma 0F9F as the remark allows; X has quasi-compact irreducible components”.

> **Stacks 0FEU, the Chern class map `c : K_0(X) ⟶ ∏_{i ≥ 0} A^i(X)`**, sending `[E]` to the
> total Chern class `c(E)` of Stacks 0F9E and sums to products.

```lean
def perfectKZeroChernClass (α : K0 (PerfectDerivedCategory X)) : TotalChowClass C sX
```

**`Stacks.Chow.perfectKZeroChernCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean#L440). The attribute's comment: “the map ch : K\_0(X) -> prod A^i(X) tensor Q, [E] |-> ch(E) extended additively, built directly from Definition 0F9E and Lemma 0F9F as the remark allows”.

> **Stacks 0FEU, the Chern character `ch : K_0(X) ⟶ ∏_{i ≥ 0} A^i(X) ⊗ 𝐐`**, additive and
> sending `[E]` to `ch(E)`; well defined by Stacks 0F9F.

```lean
def perfectKZeroChernCharacter :
    K0 (PerfectDerivedCategory X) →+ fullRationalChowCohomology C (gysinSystemOfInvertible C) sX
```

**`Stacks.Chow.perfectKZero_chernMaps_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/WholeSchemeChernMaps.lean#L488). The attribute's comment: “the whole remark: D\_\{X,perf} = D\_perf, K\_0(D\_\{X,perf}) = K\_0(X), the maps c and ch on K\_0(X), and the commutativity of both triangles with K\_0(Vect(X)) -> K\_0(X)”.

> **Stacks 0FEU.** Let `X` be locally of finite type over the base of chapter 42, with
> quasi-compact irreducible components (e.g. `X` quasi-compact). Then
>
> 1. `D_{X, perf}(𝒪_X) = D_perf(𝒪_X)`, and `K_0(D_{X, perf}(𝒪_X)) ≅ K_0(D_perf(𝒪_X)) = K_0(X)`
>    compatibly with classes of objects;
> 2. the Chern classes give `c : K_0(X) ⟶ ∏ A^i(X)`, `[E] ↦ c(E)`, with `c(α + β) = c(α) c(β)`;
> 3. the Chern character gives the additive `ch : K_0(X) ⟶ ∏ A^i(X) ⊗ 𝐐`, `[E] ↦ ch(E)`;
> 4. `c` composed with `K_0(Vect(X)) ⟶ K_0(X)` is the map `c` of Stacks 0FEL; and
> 5. `ch` composed with `K_0(Vect(X)) ⟶ K_0(X)` is the map `ch` of Stacks 0FEM.

```lean
theorem perfectKZero_chernMaps_spec :
    AlgebraicGeometry.supportedPerfectDerivedCategory (𝟙 X) = PerfectDerivedCategory X ∧
    (∀ K : AlgebraicGeometry.supportedPerfectDerivedCategory (𝟙 X),
      AlgebraicGeometry.supportedPerfectKZeroEquiv X (K0.cls K) =
        K0.cls (⟨K.obj, K.property.1⟩ : PerfectDerivedCategory X)) ∧
    (∀ (E : PerfectDerivedCategory X) (hE : HasDefinedChernClasses E.obj),
      perfectKZeroChernClass C sX hqc (K0.cls E) = perfectChernClass C sX hE) ∧
    (∀ α β : K0 (PerfectDerivedCategory X), perfectKZeroChernClass C sX hqc (α + β) =
      perfectKZeroChernClass C sX hqc α * perfectKZeroChernClass C sX hqc β) ∧
    (∀ (E : PerfectDerivedCategory X) (hE : HasDefinedChernClasses E.obj),
      perfectKZeroChernCharacter C sX hqc (K0.cls E) = perfectChernCharacter C sX hE) ∧
    (∀ α : VectorBundleKZero X, perfectKZeroChernClass C sX hqc (vectorBundleKZeroToPerfect X α) =
      totalChernKGroupMap C sX α) ∧
    (perfectKZeroChernCharacter C sX hqc).comp (vectorBundleKZeroToPerfect X) =
      (chernCharacterRingHom C sX).toAddMonoidHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.56, Tag 0FEI](https://stacks.math.columbia.edu/tag/0FEI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
