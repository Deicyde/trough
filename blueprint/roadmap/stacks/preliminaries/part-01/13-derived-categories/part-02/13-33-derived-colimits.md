---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.IsHomotopyColimit, CategoryTheory.Pretriangulated.exists_iso_of_isHomotopyColimitWithCoprojections, CategoryTheory.Pretriangulated.exists_hom_of_isHomotopyColimit, CategoryTheory.Pretriangulated.exists_iso_of_isHomotopyColimit_of_strictMono, derivedCategory_termwiseDirectSum_isColimit, derivedCategory_hasCountableCoproducts, SheafOfModules.DifferentialGradedModule.shortExact_oneSubShift_piMap, DifferentialGradedModule.shortExact_oneSubShift_piMap
statement: formalized
proof: formalized
---

# 13.33 Derived colimits

Section 13.33 of the Stacks Project, [Tag 0A5K](https://stacks.math.columbia.edu/tag/0A5K). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 090Z, a definition

[Tag 090Z](https://stacks.math.columbia.edu/tag/090Z) in the Stacks Project.

**`CategoryTheory.Pretriangulated.IsHomotopyColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/HomotopyColimit.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/HomotopyColimit.lean#L88).

> An object `K` of a pre-triangulated category `D` is a **derived colimit**, or **homotopy
> colimit**, of a system of objects `F : ℕ ⥤ D` whose direct sum `∐ F.obj` exists — written
> `K = hocolim Kₙ` — if there is a distinguished triangle
> `∐ F.obj ⟶ ∐ F.obj ⟶ K ⟶ (∐ F.obj)⟦1⟧` whose first map is `1 - fₙ` on the `n`-th summand, i.e.
> `Sigma.ι F.obj n - fₙ ≫ Sigma.ι F.obj (n + 1)`, where `Kₙ = F.obj n` and
> `fₙ = F.map (homOfLE (Nat.le_succ n))` is the transition map `Kₙ ⟶ Kₙ₊₁`. Such a `K` is unique
> only up to non-unique isomorphism, which is why this is a predicate and not a construction.

```lean
public def IsHomotopyColimit (F : ℕ ⥤ D) [HasCoproduct F.obj] (K : D) : Prop
```

## Tag 0CRH, a remark

[Tag 0CRH](https://stacks.math.columbia.edu/tag/0CRH) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_of_isHomotopyColimitWithCoprojections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/HomotopyColimitCoprojections.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/HomotopyColimitCoprojections.lean#L180).

> **[Stacks, Tag 0CRH]: a derived colimit datum is unique up to a compatible isomorphism.**
> Let `(Kₙ, fₙ)` be a system of objects of a pre-triangulated category whose direct sum exists, and
> let `(K, iₙ, c)` and `(K', i'ₙ, c')` be two derived colimit data for it: objects endowed with
> coprojections satisfying `iₙ₊₁ ∘ fₙ = iₙ` and with a morphism to `(∐ Kₙ)⟦1⟧` completing
> `∐ Kₙ --(1 - fₙ)--> ∐ Kₙ --(iₙ)--> · --c-->` to a distinguished triangle. Then there is an
> isomorphism `φ : K ≅ K'` with `φ ∘ iₙ = i'ₙ` for every `n` and `c' ∘ φ = c`.
>
> The existence of a morphism `φ` completing the identity of the first two terms to a morphism of
> the two triangles is TR3, and that it is invertible is the five lemma for distinguished triangles
> (Lemma 13.4.3). The isomorphism is not unique: nothing pins the completion TR3 produces.

```lean
theorem exists_iso_of_isHomotopyColimitWithCoprojections {F : ℕ ⥤ D} [HasCoproduct F.obj]
    {K : D} {i : ∀ n : ℕ, F.obj n ⟶ K} {c : K ⟶ (∐ F.obj)⟦(1 : ℤ)⟧}
    (h : IsHomotopyColimitWithCoprojections F K i c)
    {K' : D} {i' : ∀ n : ℕ, F.obj n ⟶ K'} {c' : K' ⟶ (∐ F.obj)⟦(1 : ℤ)⟧}
    (h' : IsHomotopyColimitWithCoprojections F K' i' c') :
    ∃ φ : K ≅ K', (∀ n : ℕ, i n ≫ φ.hom = i' n) ∧ φ.hom ≫ c' = c
```

## Tag 0CRI, a remark

[Tag 0CRI](https://stacks.math.columbia.edu/tag/0CRI) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_hom_of_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean#L461).

> **Stacks 0CRI.** A morphism of sequential systems induces a morphism between chosen
> homotopy colimits. It commutes with every canonical coprojection and completes the morphism of
> the two defining distinguished triangles.

```lean
public theorem exists_hom_of_isHomotopyColimit {F G : ℕ ⥤ D} [HasCoproduct F.obj]
    [HasCoproduct G.obj] (a : F ⟶ G) {K L : D}
    (p : ∐ F.obj ⟶ K) (q : K ⟶ (∐ F.obj)⟦(1 : ℤ)⟧)
    (hK : Triangle.mk (Stacks.CountableCoproducts.oneSubShift F) p q ∈ distTriang D)
    (p' : ∐ G.obj ⟶ L) (q' : L ⟶ (∐ G.obj)⟦(1 : ℤ)⟧)
    (hL : Triangle.mk (Stacks.CountableCoproducts.oneSubShift G) p' q' ∈ distTriang D) :
    ∃ b : K ⟶ L,
      (∀ n : ℕ, Sigma.ι F.obj n ≫ p ≫ b = a.app n ≫ Sigma.ι G.obj n ≫ p') ∧
      b ≫ q' = q ≫ (Limits.Sigma.map (fun n ↦ a.app n))⟦(1 : ℤ)⟧'
```

## Tag 0CRJ, a lemma

[Tag 0CRJ](https://stacks.math.columbia.edu/tag/0CRJ) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_of_isHomotopyColimit_of_strictMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean, line 831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean#L831).

> **Stacks 0CRJ**. Let `F : ℕ ⥤ D` be a system of objects `K m = F.obj m` of a
> pre-triangulated category, let `n : ℕ → ℕ` be strictly increasing, and assume the direct sums
> `∐ K m` and `∐ K (n i)` exist. If `K` is a derived colimit of the system with structure map `p`
> and `K'` is a derived colimit of the subsystem `(K (n i))` with structure map `p'` (Definition
> 090Z), then there is an isomorphism `e : K' ≅ K`, i.e. `hocolim K (n i) ⟶ hocolim K m`, such
> that for every `i` the composition `K (n i) ⟶ K' ⟶ K` of the coprojection with `e` is the
> coprojection `K (n i) ⟶ K`.

```lean
public theorem exists_iso_of_isHomotopyColimit_of_strictMono
    (F : ℕ ⥤ D) [HasCoproduct F.obj] {n : ℕ → ℕ} (hn : StrictMono n)
    [HasCoproduct (hn.monotone.functor ⋙ F).obj]
    {K : D} (p : ∐ F.obj ⟶ K) (q : K ⟶ (∐ F.obj)⟦(1 : ℤ)⟧)
    (hK : Triangle.mk (Limits.Sigma.desc fun m ↦ Limits.Sigma.ι F.obj m -
        F.map (homOfLE (Nat.le_succ m)) ≫ Limits.Sigma.ι F.obj (m + 1)) p q ∈ distTriang D)
    {K' : D} (p' : ∐ (hn.monotone.functor ⋙ F).obj ⟶ K')
    (q' : K' ⟶ (∐ (hn.monotone.functor ⋙ F).obj)⟦(1 : ℤ)⟧)
    (hK' : Triangle.mk (Limits.Sigma.desc fun i ↦
      Limits.Sigma.ι (hn.monotone.functor ⋙ F).obj i -
        (hn.monotone.functor ⋙ F).map (homOfLE (Nat.le_succ i)) ≫
          Limits.Sigma.ι (hn.monotone.functor ⋙ F).obj (i + 1)) p' q' ∈ distTriang D) :
    ∃ e : K' ≅ K, ∀ i : ℕ,
      Limits.Sigma.ι (hn.monotone.functor ⋙ F).obj i ≫ p' ≫ e.hom =
        Limits.Sigma.ι F.obj (n i) ≫ p
```

## Tag 0A5L, a lemma

[Tag 0A5L](https://stacks.math.columbia.edu/tag/0A5L) in the Stacks Project.

**`derivedCategory_termwiseDirectSum_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Coproducts.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Coproducts.lean#L1015).

> **Stacks Tag 0A5L**, the concrete identification of the coproduct in `D(A)`: for a countable
> family `K : J → CochainComplex A ℤ`, the termwise direct sum `∐ K`, with the images under `Q` of
> the canonical injections `Sigma.ι K j`, is a coproduct of `(Q (K j))ⱼ` in `D(A)`.
>
> `[HasCoproduct K]` records that the termwise direct sum exists in `CochainComplex A ℤ`; it
> follows from `h.hasCoproducts` and `Countable J`, but is assumed so that `∐ K` and `Sigma.ι K`
> are well-formed in the statement.

```lean
theorem derivedCategory_termwiseDirectSum_isColimit
    (h : HasExactCountableDirectSums A) (J : Type) [Countable J]
    (K : J → CochainComplex A ℤ) [HasCoproduct K] :
    Nonempty (IsColimit
      ((DerivedCategory.Q (C := A)).mapCocone (Cofan.mk (∐ K) (Sigma.ι K))))
```

**`derivedCategory_hasCountableCoproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Coproducts.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Coproducts.lean#L1029).

> **Stacks Tag 0A5L**: if the abelian category `A` has exact countable direct sums then its
> derived category `D(A)` has countable direct sums.
>
> A countable family in `D(A)` is, up to isomorphism, the image under `Q` of a family of complexes,
> by essential surjectivity of `Q`; the termwise direct sum of the latter is its coproduct.

```lean
theorem derivedCategory_hasCountableCoproducts
    (h : HasExactCountableDirectSums A) :
    HasCountableCoproducts (DerivedCategory A)
```

## Tag 093W, a lemma

[Tag 093W](https://stacks.math.columbia.edu/tag/093W) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.shortExact_oneSubShift_piMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedColimits.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedColimits.lean#L157). The attribute's comment: “sheaf differential graded modules”.

> **Lemma 093W for sheaf differential graded modules.** For a system `M₀ → M₁ → ⋯` of right
> differential graded `A`-modules over a sheaf of differential graded algebras, the sequence
>
> `0 → ⊕ₙ Mₙ --(1 - f)--> ⊕ₙ Mₙ --π--> colim Mₙ → 0`
>
> is short exact, where `1 - f` is the morphism with `σₙ ≫ (1 - f) = σₙ - fₙ ≫ σₙ₊₁` on the `n`-th
> coprojection and `π` is the morphism with `σₙ ≫ π = ιₙ`.
>
> The general Lemma 093W applies verbatim: `Mod(A, d)` is abelian, it has colimits over `ℕ` and
> countable direct sums, and those colimits over `ℕ` are exact by Tag 0FRJ.

```lean
theorem shortExact_oneSubShift_piMap (F : ℕ ⥤ DifferentialGradedModule.{u, v, max u v w} A) :
    ∃ hw : oneSubShift F ≫ piMap F = 0,
      (ShortComplex.mk (oneSubShift F) (piMap F) hw).ShortExact
```

**`DifferentialGradedModule.shortExact_oneSubShift_piMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean#L255). The attribute's comment: “differential graded modules”.

> **Lemma 093W for differential graded modules.** For a system `M₀ → M₁ → ⋯` of right
> differential graded `A`-modules the sequence
> `0 → ⊕ₙ Mₙ --(1 - f)--> ⊕ₙ Mₙ --π--> colim Mₙ → 0` is short exact.

```lean
theorem shortExact_oneSubShift_piMap :
    ∃ w : oneSubShift F ≫ piMap F = 0,
      (ShortComplex.mk (oneSubShift F) (piMap F) w).ShortExact
```

**`Stacks.CountableCoproducts.hasColimitsOfShape_discrete_of_hasColimitsOfShape_nat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean#L182).

> **Countable direct sums exist.** If colimits over `ℕ` exist in `A`, then every countable
> family of objects has a coproduct, i.e. `A` has colimits of shape `Discrete ℕ`.

```lean
theorem hasColimitsOfShape_discrete_of_hasColimitsOfShape_nat
    [HasColimitsOfShape ℕ A] :
    HasColimitsOfShape (Discrete ℕ) A
```

**`Stacks.CountableCoproducts.preservesFiniteLimits_colim_discrete_of_hasColimitsOfShape_nat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean#L194).

> **Countable direct sums are exact.** If colimits over `ℕ` exist and are exact in `A`, then the
> countable-coproduct functor `colim : (Discrete ℕ ⥤ A) ⥤ A` preserves finite limits — which, for a
> right-exact additive left adjoint, is exactness: it carries short exact sequences to short exact
> sequences.

```lean
theorem preservesFiniteLimits_colim_discrete_of_hasColimitsOfShape_nat
    [HasColimitsOfShape ℕ A] [HasColimitsOfShape (Discrete ℕ) A]
    (hexact : PreservesFiniteLimits (colim : (ℕ ⥤ A) ⥤ A)) :
    PreservesFiniteLimits (colim : (Discrete ℕ ⥤ A) ⥤ A)
```

**`Stacks.CountableCoproducts.shortExact_oneSubShift_piMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/CountableCoproducts.lean#L546).

> **The presentation of the colimit: Lemma 093W(2).** For every system over `ℕ` in an abelian
> category with countable direct sums and colimits over `ℕ` that are exact, the sequence
> `0 ⟶ ∐ₙ Aₙ --(1 - f)--> ∐ₙ Aₙ --π--> colim Aₙ ⟶ 0` is short exact.

```lean
theorem shortExact_oneSubShift_piMap
    [HasColimitsOfShape ℕ A] [HasColimitsOfShape (Discrete ℕ) A]
    (hexact : PreservesFiniteLimits (colim : (ℕ ⥤ A) ⥤ A))
    (F : SystemOverNat A) :
    ∃ w : oneSubShift F ≫ piMap F = 0,
      (ShortComplex.mk (oneSubShift F) (piMap F) w).ShortExact
```

## Tag 0949, a lemma

[Tag 0949](https://stacks.math.columbia.edu/tag/0949) in the Stacks Project.

**`DerivedCategory.isHomotopyColimit_Q_obj_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean#L425).

> **Stacks 0949**. Let `A` be an abelian category in which colimits over `ℕ` exist and are
> exact, and let `L : ℕ ⥤ CochainComplex A ℤ` be a system of complexes of `A`. Then the image
> under `Q : CochainComplex A ℤ ⥤ D(A)` of the termwise colimit `colimit L` is a derived colimit
> (homotopy colimit, Definition 090Z) of the system `L ⋙ Q` in `D(A)`.

```lean
public theorem DerivedCategory.isHomotopyColimit_Q_obj_colimit {A : Type u} [Category.{v} A]
    [Abelian A] [HasDerivedCategory.{w} A] [HasColimitsOfShape ℕ A]
    [HasExactColimitsOfShape ℕ A] (L : ℕ ⥤ CochainComplex A ℤ)
    [HasCoproduct (L ⋙ DerivedCategory.Q).obj] :
    IsHomotopyColimit (L ⋙ DerivedCategory.Q) (DerivedCategory.Q.obj (colimit L))
```

## Tag 0CRK, a lemma

[Tag 0CRK](https://stacks.math.columbia.edu/tag/0CRK) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_colimit_of_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean#L243).

> **Stacks 0CRK**. Let `F : ℕ ⥤ D` be a system of objects `K n = F.obj n` of a pre-triangulated
> category whose direct sum `∐ K n` exists, let `A` be an abelian category in which colimits over
> `ℕ` exist and are exact, and let `H : D ⥤ A` be a homological functor commuting with countable
> direct sums. If `K` is a derived colimit of the system with structure map `p : ∐ K n ⟶ K`
> (Definition 090Z), then `H K = colim H (K n)`: there is an isomorphism
> `e : colim H (K n) ≅ H K` such that for every `n` the `n`-th coprojection of the colimit followed
> by `e` is `H` applied to the coprojection `K n ⟶ K` of the derived colimit.

```lean
public theorem exists_iso_colimit_of_isHomotopyColimit
    (F : ℕ ⥤ D) [HasCoproduct F.obj] (H : D ⥤ A) [H.IsHomological]
    [PreservesColimitsOfShape (Discrete ℕ) H]
    {K : D} (p : ∐ F.obj ⟶ K) (q : K ⟶ (∐ F.obj)⟦(1 : ℤ)⟧)
    (hK : Triangle.mk (Limits.Sigma.desc fun n ↦ Limits.Sigma.ι F.obj n -
        F.map (homOfLE (Nat.le_succ n)) ≫ Limits.Sigma.ι F.obj (n + 1)) p q ∈ distTriang D) :
    ∃ e : colimit (F ⋙ H) ≅ H.obj K, ∀ n : ℕ,
      colimit.ι (F ⋙ H) n ≫ e.hom = H.map (Limits.Sigma.ι F.obj n ≫ p)
```

## Tag 094A, a lemma

[Tag 094A](https://stacks.math.columbia.edu/tag/094A) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_colimit_preadditiveCoyoneda_of_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedColimits.lean#L327).

> **Stacks 094A**. Let `F : ℕ ⥤ D` be a system of objects `L n = F.obj n` of a pre-triangulated
> category whose direct sum `∐ L n` exists, and let `K` be an object of `D` such that
> `Hom(K, -) = preadditiveCoyoneda.obj (Opposite.op K)` commutes with countable direct sums, i.e.
> for every countable family `E : ℕ → D` the canonical map `⨁ (K ⟶ E n) ⟶ (K ⟶ ∐ E)` is bijective.
> If `L` is a derived colimit of the system with structure map `p : ∐ L n ⟶ L` (Definition 090Z),
> then `Hom(K, L) = colim Hom(K, L n)`: there is an isomorphism of abelian groups
> `e : colim Hom(K, L n) ≅ Hom(K, L)` such that for every `n` the `n`-th coprojection of the colimit
> followed by `e` is composition with the coprojection `L n ⟶ L` of the derived colimit.
>
> This is Lemma 0CRK for the homological functor `H = Hom(K, -)`.

```lean
public theorem exists_iso_colimit_preadditiveCoyoneda_of_isHomotopyColimit
    (F : ℕ ⥤ D) [HasCoproduct F.obj] (K : D)
    [PreservesColimitsOfShape (Discrete ℕ) (preadditiveCoyoneda.obj (Opposite.op K))]
    {L : D} (p : ∐ F.obj ⟶ L) (q : L ⟶ (∐ F.obj)⟦(1 : ℤ)⟧)
    (hL : Triangle.mk (Limits.Sigma.desc fun n ↦ Limits.Sigma.ι F.obj n -
        F.map (homOfLE (Nat.le_succ n)) ≫ Limits.Sigma.ι F.obj (n + 1)) p q ∈ distTriang D) :
    ∃ e : colimit (F ⋙ preadditiveCoyoneda.obj (Opposite.op K)) ≅
        (preadditiveCoyoneda.obj (Opposite.op K)).obj L, ∀ n : ℕ,
      colimit.ι (F ⋙ preadditiveCoyoneda.obj (Opposite.op K)) n ≫ e.hom =
        (preadditiveCoyoneda.obj (Opposite.op K)).map (Limits.Sigma.ι F.obj n ≫ p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.33, Tag 0A5K](https://stacks.math.columbia.edu/tag/0A5K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
