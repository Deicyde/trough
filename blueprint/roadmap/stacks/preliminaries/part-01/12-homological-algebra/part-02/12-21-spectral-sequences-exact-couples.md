---
declaration: section
origin: cited
lean: CategoryTheory.ExactCouple, CategoryTheory.ExactCouple.Hom, CategoryTheory.ExactCouple.d_comp_d, CategoryTheory.ExactCouple.kernelSubobject_d_eq_pullback_kernelSubobject, CategoryTheory.ExactCouple.kernelSubobject_d_eq_pullback_imageSubobject, CategoryTheory.ExactCouple.imageSubobject_d_eq_exists_imageSubobject, CategoryTheory.ExactCouple.imageSubobject_d_eq_exists_kernelSubobject, CategoryTheory.ExactCouple.derived
statement: formalized
proof: formalized
---

# 12.21 Spectral sequences: exact couples

Section 12.21 of the Stacks Project, [Tag 011P](https://stacks.math.columbia.edu/tag/011P). 4 tags here are carried by 18 declarations of the repository (all in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 011Q, a definition

[Tag 011Q](https://stacks.math.columbia.edu/tag/011Q) in the Stacks Project.

**`CategoryTheory.ExactCouple`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L62). The attribute's comment: “(1) exact couple: `Ker α = Im f`, `Ker f = Im g`, `Ker g = Im α`”.

> An exact couple `(A, E, α, f, g)` in an abelian category: `Ker α = Im f`, `Ker f = Im g`
> and `Ker g = Im α`. The endomorphism is typed as `α : End A` so that `α ^ n` is the `n`-fold
> composite of `α`.

```lean
structure ExactCouple (C : Type*) [Category* C] [Abelian C]
```

**`CategoryTheory.ExactCouple.Hom`**, a structure in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L93). The attribute's comment: “(2) morphism `t = (t_A, t_E)` commuting with `α`, `f`, `g`”.

> A morphism of exact couples `t = (t_A, t_E) : X ⟶ Y`: a pair of morphisms commuting with
> `α`, `f` and `g`.

```lean
structure Hom (X Y : ExactCouple C)
```

## Tag 011R, a lemma

[Tag 011R](https://stacks.math.columbia.edu/tag/011R) in the Stacks Project.

**`CategoryTheory.ExactCouple.d_comp_d`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L144). The attribute's comment: “`d ∘ d = 0` for `d = g ∘ f`”.

> `d ∘ d = 0`, since `f ∘ g = 0`.

```lean
lemma d_comp_d : X.d ≫ X.d = 0
```

**`CategoryTheory.ExactCouple.kernelSubobject_d_eq_pullback_kernelSubobject`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L282). The attribute's comment: “(1) `Ker d = f⁻¹(Ker g)`”.

> `Ker d = f⁻¹(Ker g)`, as subobjects of `E`.

```lean
lemma kernelSubobject_d_eq_pullback_kernelSubobject :
    kernelSubobject X.d = (Subobject.pullback X.f).obj (kernelSubobject X.g)
```

**`CategoryTheory.ExactCouple.kernelSubobject_d_eq_pullback_imageSubobject`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L288). The attribute's comment: “(1) `Ker d = f⁻¹(Im α)`”.

> `Ker d = f⁻¹(Im α)`, as subobjects of `E`.

```lean
lemma kernelSubobject_d_eq_pullback_imageSubobject :
    kernelSubobject X.d = (Subobject.pullback X.f).obj (imageSubobject X.α.asHom)
```

**`CategoryTheory.ExactCouple.imageSubobject_d_eq_exists_imageSubobject`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L296). The attribute's comment: “(2) `Im d = g(Im f)`”.

> `Im d = g(Im f)`, as subobjects of `E`.

```lean
lemma imageSubobject_d_eq_exists_imageSubobject :
    imageSubobject X.d = (Subobject.exists X.g).obj (imageSubobject X.f)
```

**`CategoryTheory.ExactCouple.imageSubobject_d_eq_exists_kernelSubobject`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L302). The attribute's comment: “(2) `Im d = g(Ker α)`”.

> `Im d = g(Ker α)`, as subobjects of `E`.

```lean
lemma imageSubobject_d_eq_exists_kernelSubobject :
    imageSubobject X.d = (Subobject.exists X.g).obj (kernelSubobject X.α.asHom)
```

**`CategoryTheory.ExactCouple.derived`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple.lean#L397). The attribute's comment: “(3) the derived couple `(Im α, Ker d/Im d, α', f', g')` is exact”.

> The derived exact couple `(A', E', α', f', g') = (Im α, Ker d / Im d, α', f', g')` of
> Stacks 011R (3). An `abbrev` on purpose (load-bearing): the iterated derived couples need
> `X.derived.α` to reduce to `X.α'` (and likewise for `A`, `E`, `f`, `g`).

```lean
noncomputable abbrev derived : ExactCouple C
```

## Tag 011S, a definition

[Tag 011S](https://stacks.math.columbia.edu/tag/011S) in the Stacks Project.

**`CategoryTheory.ExactCouple.spectralSequence`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L194). The attribute's comment: “`(E_r, d_r)_{r ≥ 1}`: `E_1 = E`, `d_1 = d`, `E_{r+1} = E_r'`, `d_{r+1} = d_r'`”.

> The spectral sequence `(E_r, d_r)_{r ≥ 1}` of the exact couple `X`: `(E_{n+1}, d_{n+1})` is
> `(E^{(n)}, d^{(n)})`, the `E`-object and differential of the `n`-th derived couple, and
> `E_{n+2} ≅ Ker d^{(n)}/Im d^{(n)}` is `derivedIterSuccIso n`. An `abbrev` of `Ungraded.ofNat`
> on purpose (load-bearing): `X.spectralSequence.X r hr` must reduce to `(X.derivedIter _).E`.

```lean
noncomputable abbrev spectralSequence : Ungraded C 1
```

**`CategoryTheory.ExactCouple.spectralSequenceXIso`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L335). The attribute's comment: “`E_{n+1} ≅ E^{(n)}`, the `n`-th derived couple's `E`”.

> `E_{n+1} ≅ E^{(n)}`: the `(n + 1)`-st page of the spectral sequence of `X` is the `E` of
> the `n`-th derived couple. An `abbrev` on purpose (load-bearing): the 011T statements for
> `X.spectralSequence` must see through it.

```lean
noncomputable abbrev spectralSequenceXIso (n : ℕ) :
    X.spectralSequence.X (n + 1) ≅ (X.derivedIter n).E
```

**`CategoryTheory.ExactCouple.spectralSequence_d`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L341). The attribute's comment: “`d_{n+1} = d^{(n)}` under `E_{n+1} ≅ E^{(n)}`”.

> `d_{n+1} = d^{(n)}` under `E_{n+1} ≅ E^{(n)}`.

```lean
lemma spectralSequence_d (n : ℕ) :
    X.spectralSequence.d (n + 1) ≫ (X.spectralSequenceXIso n).hom =
      (X.spectralSequenceXIso n).hom ≫ (X.derivedIter n).d
```

**`CategoryTheory.ExactCouple.spectralSequenceXOneIso`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L349). The attribute's comment: “`E_1 = E`”.

> `E_1 ≅ E`. An `abbrev` on purpose (load-bearing): the 011T statements for
> `X.spectralSequence` must see through it.

```lean
noncomputable abbrev spectralSequenceXOneIso : X.spectralSequence.X 1 ≅ X.E
```

**`CategoryTheory.ExactCouple.spectralSequence_d_one`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L354). The attribute's comment: “`d_1 = d` under `E_1 ≅ E`”.

> `d_1 = d` under `E_1 ≅ E`.

```lean
lemma spectralSequence_d_one :
    X.spectralSequence.d 1 ≫ X.spectralSequenceXOneIso.hom = X.spectralSequenceXOneIso.hom ≫ X.d
```

**`CategoryTheory.ExactCouple.spectralSequenceXTwoIso`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L360). The attribute's comment: “`E_2 = E'`”.

> `E_2 ≅ E'`. An `abbrev` on purpose (load-bearing), as `spectralSequenceXOneIso`.

```lean
noncomputable abbrev spectralSequenceXTwoIso : X.spectralSequence.X 2 ≅ X.derived.E
```

**`CategoryTheory.ExactCouple.spectralSequence_d_two`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L365). The attribute's comment: “`d_2 = g' ∘ f'` under `E_2 ≅ E'`”.

> `d_2 = g' ∘ f'` under `E_2 ≅ E'`.

```lean
lemma spectralSequence_d_two :
    X.spectralSequence.d 2 ≫ X.spectralSequenceXTwoIso.hom =
      X.spectralSequenceXTwoIso.hom ≫ (X.f' ≫ X.g')
```

## Tag 011T, a lemma

[Tag 011T](https://stacks.math.columbia.edu/tag/011T) in the Stacks Project.

**`CategoryTheory.ExactCouple.DerivedPages.Z_succ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 708](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L708). The attribute's comment: “`Z_{r+1} = f⁻¹(Im α^r)` under `E_1 ≅ E`, for any `E` with derived-couple pages”.

> Stacks 011T: `Z_{r+1} = f⁻¹(Im α^r)` under `E_1 ≅ E`, for any ungraded spectral sequence
> `E` whose pages are the derived couples of `X`.

```lean
theorem Z_succ (r : ℕ) :
    E.Z () (r + 1) =
      (Subobject.pullback (D.pageOneIso.hom ≫ X.f)).obj (imageSubobject (X.α ^ r).asHom)
```

**`CategoryTheory.ExactCouple.DerivedPages.B_succ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L716). The attribute's comment: “`B_{r+1} = g(Ker α^r)` under `E_1 ≅ E`, for any `E` with derived-couple pages”.

> Stacks 011T: `B_{r+1} = g(Ker α^r)` under `E_1 ≅ E`, for any ungraded spectral sequence
> `E` whose pages are the derived couples of `X`.

```lean
theorem B_succ (r : ℕ) :
    E.B () (r + 1) =
      (Subobject.exists (X.g ≫ D.pageOneIso.inv)).obj (kernelSubobject (X.α ^ r).asHom)
```

**`CategoryTheory.ExactCouple.DerivedPages.d_succ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L740). The attribute's comment: “`d_{r+1}(x̄) = \overline{g y}` for `x ∈ Z_{r+1}`, `y ∈ A` with `f x = α^r y`”.

> Stacks 011T, the differential: for `x : T ⟶ Z_{r+1}` and `y : T ⟶ A` with `f x = α^r y`
> under `E_1 ≅ E`, `d_{r+1}(x̄) = \overline{g y}`: here `x̄ = x ≫ q_{r+1} : T ⟶ E_{r+1}` and
> `\overline{g y}` is the class of the lift of `y ≫ g` (Stacks' `g ∘ y`) to `Z_{r+1}` (which
> exists by `factors_g`).

```lean
theorem d_succ (r : ℕ) {T : C} (x : T ⟶ (E.Z () (r + 1) : C)) (y : T ⟶ X.A)
    (hxy : x ≫ (E.Z () (r + 1)).arrow ≫ D.pageOneIso.hom ≫ X.f = y ≫ (X.α ^ r).asHom) :
    x ≫ E.q () (r + 1) ≫ E.d (r + 1) =
      y ≫ (E.Z () (r + 1)).factorThru (X.g ≫ D.pageOneIso.inv) (D.factors_g r) ≫
        E.q () (r + 1)
```

Declarations registered for the tag:

- [`CategoryTheory.SpectralSequence.B_le_Z`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L512), declared in the repository, registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 776](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L776) (StacksCore): “the inclusions `B_r ⊆ Z_r` of the towers `0 = B_1 ⊆ … ⊆ Z_1 = E`”.
- [`CategoryTheory.SpectralSequence.B_monotone`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L636), declared in the repository, registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L778) (StacksCore): “the inclusions `B_r ⊆ B_{r+1}` of the tower `0 = B_1 ⊆ B_2 ⊆ …`”.
- [`CategoryTheory.SpectralSequence.Z_antitone`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L632), declared in the repository, registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean, line 780](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ExactCouple/SpectralSequence.lean#L780) (StacksCore): “the inclusions `Z_{r+1} ⊆ Z_r` of the tower `… ⊆ Z_2 ⊆ Z_1 = E`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.21, Tag 011P](https://stacks.math.columbia.edu/tag/011P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
