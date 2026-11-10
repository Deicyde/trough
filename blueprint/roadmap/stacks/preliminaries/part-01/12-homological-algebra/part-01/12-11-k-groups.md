---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckGroup, CategoryTheory.GrothendieckGroup.additivity, KZero, CategoryTheory.GrothendieckGroup.map, CategoryTheory.GrothendieckGroup.map_of, exactFunctor_induces_kZeroHom, CategoryTheory.ObjectProperty.SerreClassLocalization.exact_map_iff, CategoryTheory.GrothendieckGroup.map_surjective
statement: formalized
proof: formalized
---

# 12.11 K-groups

Section 12.11 of the Stacks Project, [Tag 02MT](https://stacks.math.columbia.edu/tag/02MT). 3 tags here are carried by 17 declarations of the repository (11 in StacksCore and 6 in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02MU, a definition

[Tag 02MU](https://stacks.math.columbia.edu/tag/02MU) in the Stacks Project.

**`CategoryTheory.GrothendieckGroup`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean#L82). The attribute's comment: “free on the objects; for any category with zero morphisms”.

> The Grothendieck group `K₀(C)`: the free abelian group on the objects of `C` modulo
> `[S.X₂] = [S.X₁] + [S.X₃]` for every short exact sequence `S`.

```lean
def GrothendieckGroup : Type u
```

**`CategoryTheory.GrothendieckGroup.additivity`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean#L146). The attribute's comment: “the relation `[B] = [A] + [C]` of a short exact sequence”.

> The class of the middle term of a short exact sequence is the sum of the other two.

```lean
lemma additivity {S : ShortComplex C} (hS : S.ShortExact) : of S.X₂ = of S.X₁ + of S.X₃
```

**`KZero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckGroup.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckGroup.lean#L37). References: SGA 6 0 (3.1), “more general”.

> The zeroth K-group `K₀(𝒜)` of an abelian category `𝒜` (Stacks tag 02MU).
> It is the free abelian group on the objects of `𝒜`, modulo the relation
> `[B] - [A] - [C] = 0` for every short exact sequence `0 → A → B → C → 0`.

```lean
noncomputable abbrev KZero : Type _
```

## Tag 02MV, a lemma

[Tag 02MV](https://stacks.math.columbia.edu/tag/02MV) in the Stacks Project.

**`CategoryTheory.GrothendieckGroup.map`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean#L155). The attribute's comment: “for any functor preserving zero morphisms and short exact sequences”.

> The homomorphism `K₀(F) : K₀(C) → K₀(D)`, `[X] ↦ [F(X)]`, induced by a functor preserving
> zero morphisms and short exact sequences.

```lean
def map (F : C ⥤ D) [F.PreservesZeroMorphisms]
    (hF : ∀ ⦃S : ShortComplex C⦄, S.ShortExact → (S.map F).ShortExact) :
    GrothendieckGroup C →+ GrothendieckGroup D
```

**`CategoryTheory.GrothendieckGroup.map_of`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean#L258). The attribute's comment: “`K₀(F)[A] = [F(A)]`”.

> `K₀(F)` sends the class of `X` to the class of `F(X)`.

```lean
lemma map_of (F : C ⥤ D) [F.PreservesZeroMorphisms]
    (hF : ∀ ⦃S : ShortComplex C⦄, S.ShortExact → (S.map F).ShortExact) (X : C) :
    map F hF (of X) = of (F.obj X)
```

**`exactFunctor_induces_kZeroHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckGroup.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckGroup.lean#L128).

> **Stacks Tag 02MV.** An exact functor `F : C ⥤ D` between abelian categories
> induces a unique homomorphism of K-groups `K₀(F) : K₀(C) → K₀(D)` satisfying
> `K₀(F)([A]) = [F(A)]` for every object `A`.

```lean
theorem exactFunctor_induces_kZeroHom {C D : Type*} [Category C] [Abelian C] [Category D]
    [Abelian D] (F : C ⥤ D) [F.Additive] [PreservesFiniteLimits F] [PreservesFiniteColimits F] :
    ∃! (φ : KZero C →+ KZero D), ∀ A : C, φ (KZero.mk C A) = KZero.mk D (F.obj A)
```

## Tag 02MX, a lemma

[Tag 02MX](https://stacks.math.columbia.edu/tag/02MX) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.exact_map_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean#L176). The attribute's comment: “(2): `(M, φ, ψ)` becomes exact in `D` iff its homology satisfies `P`”.

> **Stacks 02MX (2)**, exactness in the quotient: a short complex `T` becomes exact after
> applying `L` if and only if its homology satisfies `P`.
>
> For a 2-periodic complex `(M, φ, ψ)` (Stacks 02MW), that is `φ ψ : M ⟶ M` with `φ ≫ ψ = 0` and
> `ψ ≫ φ = 0`, the homology objects of `ShortComplex.mk φ ψ _` and `ShortComplex.mk ψ φ _` are
> `H⁰(M, φ, ψ) = Ker ψ / Im φ` and `H¹(M, φ, ψ) = Ker φ / Im ψ`. Applied to these two short
> complexes, this lemma is the "in other words" of 02MX (2): `(M, φ, ψ)` becomes exact in the
> quotient if and only if `H⁰(M, φ, ψ)` and `H¹(M, φ, ψ)` satisfy `P`.

```lean
lemma exact_map_iff (T : ShortComplex C) : (T.map L).Exact ↔ P T.homology
```

**`CategoryTheory.GrothendieckGroup.map_surjective`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/Basic.lean#L301). The attribute's comment: “(1), surjectivity, for any essentially surjective `F` to a category with `0`”.

> An essentially surjective functor into a category with a zero object induces a surjection on
> `K₀`. For the quotient functor `𝒜 ⥤ 𝒜/𝒞` by a Serre subcategory `𝒞` this is the surjectivity of
> `K₀(𝒜) → K₀(𝒜/𝒞)` in Stacks 02MX (1).

```lean
lemma map_surjective [HasZeroObject D] (F : C ⥤ D) [F.PreservesZeroMorphisms] [F.EssSurj]
    (hF : ∀ ⦃S : ShortComplex C⦄, S.ShortExact → (S.map F).ShortExact) :
    Function.Surjective (map F hF)
```

**`CategoryTheory.GrothendieckGroup.of_eq_of_iff_exists_homology_iso`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/PeriodicComplex.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/PeriodicComplex.lean#L275). The attribute's comment: “(2), key step: `[X] = [Y]` iff `X ≅ H⁰`, `Y ≅ H¹` for some `(M, φ, ψ)`”.

> The realisation theorem, the key step of Stacks 02MX (2): two objects `X` and `Y` of `A`
> have the same class in `K₀(A)` if and only if there is a 2-periodic complex
> `M --φ--> M --ψ--> M` (Stacks 02MW) whose homology objects `H⁰ = Ker ψ / Im φ` and
> `H¹ = Ker φ / Im ψ` are isomorphic to `X` and to `Y`. Stacks 02SC uses it in this form.

```lean
theorem of_eq_of_iff_exists_homology_iso {X Y : A} :
    of X = of Y ↔ ∃ (M : A) (φ ψ : M ⟶ M) (hφψ : φ ≫ ψ = 0) (hψφ : ψ ≫ φ = 0),
      Nonempty ((ShortComplex.mk φ ψ hφψ).homology ≅ X) ∧
        Nonempty ((ShortComplex.mk ψ φ hψφ).homology ≅ Y)
```

**`CategoryTheory.GrothendieckGroup.map_ι_eq_zero_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/PeriodicComplex.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/PeriodicComplex.lean#L293). The attribute's comment: “(2), for any `P` containing `0` and closed under `⊞`”.

> Stacks 02MX (2): let `P` be a property of objects of `A` that contains `0` and is closed under
> binary products (hence under isomorphisms), and let `hι` say that the inclusion `P.ι` preserves
> short exact sequences. An element `x` of `K₀(P.FullSubcategory)` maps to `0` in `K₀(A)` if and
> only if `x = [H⁰] - [H¹]` for a 2-periodic complex `(M, φ, ψ)` in `A` (Stacks 02MW) whose
> homology objects `H⁰ = Ker ψ / Im φ` and `H¹ = Ker φ / Im ψ` satisfy `P`. Stacks states it for a
> Serre subcategory, where it reads `map_ι_eq_zero_iff P P.shortExact_map_ι x`; there, by
> `ObjectProperty.SerreClassLocalization.exact_map_iff`, the homology objects satisfy `P` if and
> only if the complex becomes exact in the Serre quotient of `A` by `P`.

```lean
theorem map_ι_eq_zero_iff (P : ObjectProperty A) [P.ContainsZero] [P.IsClosedUnderBinaryProducts]
    (hι : ∀ ⦃S : ShortComplex P.FullSubcategory⦄, S.ShortExact → (S.map P.ι).ShortExact)
    (x : GrothendieckGroup P.FullSubcategory) :
    map P.ι hι x = 0 ↔ ∃ (M : A) (φ ψ : M ⟶ M) (hφψ : φ ≫ ψ = 0) (hψφ : ψ ≫ φ = 0)
      (h₀ : P (ShortComplex.mk φ ψ hφψ).homology) (h₁ : P (ShortComplex.mk ψ φ hψφ).homology),
      x = of ⟨_, h₀⟩ - of ⟨_, h₁⟩
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.grothendieckGroupEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean#L145). The attribute's comment: “(1) as `K₀(A)/im K₀(C) ≃ K₀(A/C)`, for any localization `L`”.

> **Stacks 02MX (1)**, as an isomorphism: the map `K₀(A) → K₀(D)` induced by the localization
> functor `L` identifies `K₀(D)` with the quotient of `K₀(A)` by the image of
> `K₀(P.FullSubcategory)`.
>
> The inverse sends `[Y]` to the class of `[L.objPreimage Y]`. It respects the relations of `K₀(D)`
> because every short exact sequence of `D` is isomorphic to the image of a short exact sequence of
> `A` (`exists_shortExact_map_iso`), and any two preimages of an object have the same class
> (`mk_of_eq_mk_of_of_iso`).

```lean
noncomputable def grothendieckGroupEquiv :
    GrothendieckGroup A ⧸ (GrothendieckGroup.map P.ι hι).range ≃+ GrothendieckGroup D
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.exact_grothendieckGroup_map`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean#L217). The attribute's comment: “(1), exactness at `K₀(A)`”.

> **Stacks 02MX (1)**, exactness at `K₀(A)`: the kernel of the map `K₀(A) → K₀(D)` induced by
> `L` is the image of the map `K₀(P.FullSubcategory) → K₀(A)` induced by the inclusion. It is read
> off `grothendieckGroupEquiv_comp_mk'`.

```lean
theorem exact_grothendieckGroup_map :
    Function.Exact (GrothendieckGroup.map P.ι hι) (GrothendieckGroup.map L hL)
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.grothendieckGroup_map_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GrothendieckGroup/SerreClass.lean#L227). The attribute's comment: “(1), surjectivity of `K₀(A) → K₀(A/C)`”.

> **Stacks 02MX (1)**, surjectivity: the map `K₀(A) → K₀(D)` induced by `L` is surjective. This
> is `GrothendieckGroup.map_surjective`, since `L` is essentially surjective and `D` has a zero
> object.

```lean
theorem grothendieckGroup_map_surjective :
    Function.Surjective (GrothendieckGroup.map L hL)
```

**`KZero.mk_eq_mk_iff_exists_homology_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/KZeroRealisation.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/KZeroRealisation.lean#L95). The attribute's comment: “(2), key step, for `KZero`: `[X] = [Y]` iff `X ≅ H⁰`, `Y ≅ H¹` for some `(M, φ, ψ)`”.

> **[Stacks, Tag 02MX] part (2), the realisation theorem, for `KZero`.** Two objects `X` and `Y`
> of an abelian category have the same class in `K₀` if and only if there is a `(2, 1)`-periodic
> complex `M --φ--> M --ψ--> M` whose homology objects `H⁰ = Ker ψ / Im φ` and `H¹ = Ker φ / Im ψ`
> are isomorphic to `X` and to `Y`. [Stacks, Tag 02SC] uses 02MX (2) in this form.

```lean
theorem mk_eq_mk_iff_exists_homology_iso {X Y : 𝒜} :
    mk 𝒜 X = mk 𝒜 Y ↔ ∃ (M : 𝒜) (φ ψ : M ⟶ M) (hφψ : φ ≫ ψ = 0) (hψφ : ψ ≫ φ = 0),
      Nonempty ((ShortComplex.mk φ ψ hφψ).homology ≅ X) ∧
        Nonempty ((ShortComplex.mk ψ φ hψφ).homology ≅ Y)
```

**`KZero.surjective_map_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/SerreQuotient.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/SerreQuotient.lean#L175). The attribute's comment: “part (1): `K₀(C) → K₀(C/P)` is surjective”.

> **Stacks 02MX, part (1), surjectivity.** The quotient functor `L : C ⥤ C/P` induces a
> surjection `K₀(C) → K₀(C/P)`.

```lean
theorem surjective_map_localization : Function.Surjective (map L)
```

**`KZero.exact_map_ι_map_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/SerreQuotient.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/SerreQuotient.lean#L206). The attribute's comment: “part (1): exactness at `K₀(C)`”.

> **Stacks 02MX, part (1), exactness in the middle.** The sequence
> `K₀(P) → K₀(C) → K₀(C/P)` induced by the inclusion of `P` and the quotient functor is exact.

```lean
theorem exact_map_ι_map_localization : Function.Exact (map P.ι) (map L)
```

**`KZero.map_ι_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/KTheory/SerreQuotient.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/KTheory/SerreQuotient.lean#L462). The attribute's comment: “part (2)”.

> **Stacks 02MX, part (2).** An element of `K₀(P)` dies in `K₀(C)` if and only if it is
> `[H⁰(M, φ, ψ)] - [H¹(M, φ, ψ)]` for a complex `(M, φ, ψ)` (endomorphisms `φ, ψ` of an object `M`
> of `C` with `φ ∘ ψ = 0 = ψ ∘ φ`) whose homology `H⁰ = Ker(φ)/Im(ψ)` and `H¹ = Ker(ψ)/Im(φ)`
> lies in `P`, i.e. which becomes exact in `C/P`.

```lean
theorem map_ι_eq_zero_iff (x : KZero P.FullSubcategory) :
    map P.ι x = 0 ↔ ∃ (M : C) (φ ψ : M ⟶ M) (hφψ : φ ≫ ψ = 0) (hψφ : ψ ≫ φ = 0)
      (h₀ : P (ShortComplex.mk ψ φ hψφ).homology) (h₁ : P (ShortComplex.mk φ ψ hφψ).homology),
      x = mk _ ⟨_, h₀⟩ - mk _ ⟨_, h₁⟩
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.11, Tag 02MT](https://stacks.math.columbia.edu/tag/02MT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
