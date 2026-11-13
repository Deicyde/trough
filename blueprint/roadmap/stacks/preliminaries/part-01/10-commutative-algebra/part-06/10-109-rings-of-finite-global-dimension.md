---
declaration: section
origin: cited
lean: schanuel, Module.projectiveDimension, pd_syzygy_projective_of_le, CategoryTheory.hasProjectiveDimensionLE_tfae_leftResolution, ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free, ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_projective_finite, ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free_finite, CategoryTheory.hasProjectiveDimensionLT_of_enoughProjectives
statement: formalized
proof: formalized
---

# 10.109 Rings of finite global dimension

Section 10.109 of the Stacks Project, [Tag 00O2](https://stacks.math.columbia.edu/tag/00O2). 13 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00O3, a lemma

[Tag 00O3](https://stacks.math.columbia.edu/tag/00O3) in the Stacks Project.

**`schanuel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 924](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L924).

> **Schanuel's Lemma (Stacks Tag 00O3).**
> Given two short exact sequences `0 → K → P₁ → M → 0` and `0 → L → P₂ → M → 0`
> with `P₁`, `P₂` projective, there are `R`-linear isomorphisms
> `φ : K × P₂ ≃ P₁ × L` and `ψ : P₁ × P₂ ≃ P₁ × P₂` fitting into a commutative
> diagram of short exact sequences whose right-hand vertical map is the identity
> on `M`.

```lean
theorem schanuel
    {R : Type*} [Ring R]
    {K L P₁ P₂ M : Type*}
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup P₁] [AddCommGroup P₂] [AddCommGroup M]
    [Module R K] [Module R L] [Module R P₁] [Module R P₂] [Module R M]
    (c₁ : K →ₗ[R] P₁) (p₁ : P₁ →ₗ[R] M) (c₂ : L →ₗ[R] P₂) (p₂ : P₂ →ₗ[R] M)
    (hP₁ : Module.Projective R P₁) (hP₂ : Module.Projective R P₂)
    -- first short exact sequence `0 → K → P₁ → M → 0`
    (hc₁ : Function.Injective c₁) (hp₁ : Function.Surjective p₁)
    (hex₁ : Function.Exact c₁ p₁)
    -- second short exact sequence `0 → L → P₂ → M → 0`
    (hc₂ : Function.Injective c₂) (hp₂ : Function.Surjective p₂)
    (hex₂ : Function.Exact c₂ p₂) :
    ∃ (φ : (K × P₂) ≃ₗ[R] (P₁ × L)) (ψ : (P₁ × P₂) ≃ₗ[R] (P₁ × P₂)),
      let topLeft : (K × P₂) →ₗ[R] (P₁ × P₂) := c₁.prodMap LinearMap.id
      let topRight : (P₁ × P₂) →ₗ[R] M := LinearMap.coprod p₁ 0
      let botLeft : (P₁ × L) →ₗ[R] (P₁ × P₂) := LinearMap.id.prodMap c₂
      let botRight : (P₁ × P₂) →ₗ[R] M := LinearMap.coprod 0 p₂
      -- (1) both rows are short exact sequences
      (Function.Injective topLeft ∧ Function.Surjective topRight ∧
        Function.Exact topLeft topRight) ∧
      (Function.Injective botLeft ∧ Function.Surjective botRight ∧
        Function.Exact botLeft botRight) ∧
      -- (3a) left square commutes: `(id, c₂) ∘ φ = ψ ∘ (c₁, id)`
      (botLeft.comp φ.toLinearMap = ψ.toLinearMap.comp topLeft) ∧
      -- (3b) right square commutes: `(0, p₂) ∘ ψ = (p₁, 0)`
      (botRight.comp ψ.toLinearMap = topRight)
```

## Tag 00O4, a definition

[Tag 00O4](https://stacks.math.columbia.edu/tag/00O4) in the Stacks Project.

**`Module.projectiveDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Defs.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension/Defs.lean#L142). References: EGA 0 (17.2.1), “dim.proj definition”.

> The **projective dimension** of an `R`-module `M`: the least `d` with `Ext^i(M, -) = 0` for
> all `i > d`. For `R` small in `M`'s universe this is the source's invariant, the least `d` for
> which there is an exact sequence `0 → P_d → ⋯ → P_0 → M → 0` with all `P_i` projective (00O5,
> 0CXC), and `M` then has *finite projective dimension* in the sense of the source exactly when
> this is `≠ ⊤` (`CategoryTheory.projectiveDimension_ne_top_iff`). It is `⊥` for the zero module,
> whose projective dimension in the source is `0`.

```lean
public noncomputable abbrev Module.projectiveDimension (R : Type u) [Ring R] (M : Type v)
    [AddCommGroup M] [Module R M] : WithBot ℕ∞
```

## Tag 00O5, a lemma

[Tag 00O5](https://stacks.math.columbia.edu/tag/00O5) in the Stacks Project.

**`pd_syzygy_projective_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 1499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L1499). The attribute's comment: “The source's hypothesis `pd(M) = d` is relaxed to `projectiveDimension M ≤ d`, which also covers the zero module, of projective dimension `0` in the source and `⊥` here.”. References: EGA 0 (17.2.1), “Necessity”.

> **Stacks Tag 00O5 / Lemma 10.109.3.** Let `M` have projective dimension at most `d` and let
> `F_e → ⋯ → F_0 → M → 0` be exact with every `F_i` projective and `d ≤ e + 1`. Then the
> leftmost syzygy `Ker(F_e → F_{e-1})`, or `Ker(F_0 → M)` when `e = 0`, is projective.
>
> The source assumes `pd(M) = d` for its minimal-resolution projective dimension (00O4), under
> which the zero module has projective dimension `0`; the library's projective dimension of the zero
> module is `⊥` instead. The hypothesis `projectiveDimension M ≤ d` covers the source's hypothesis
> in both cases (for `M ≠ 0` the two invariants coincide, and for `M = 0` the value `⊥` is `≤ d`),
> so this is the source's statement, in a slightly more general form.

```lean
theorem pd_syzygy_projective_of_le (d e : ℕ)
    -- the truncated sequence `F_e → ⋯ → F_0 → M → 0`
    (S : ComposableArrows (ModuleCat R) (e + 2))
    -- `M`, the object at position `e + 1`, has projective dimension at most `d`
    (hpd : projectiveDimension (S.obj ⟨e + 1, by omega⟩) ≤ (d : WithBot ℕ∞))
    -- the hypothesis `e ≥ d - 1`, equivalently `d ≤ e + 1`
    (hde : d ≤ e + 1)
    -- exactness at every internal object (in particular `F_0 → M` is surjective);
    -- note exactness is NOT imposed at the leftmost object `F_e`
    (hexact : S.Exact)
    -- the rightmost object (position `e + 2`) is the zero module
    (hzero : Limits.IsZero (S.obj (Fin.last (e + 2))))
    -- each `F_i` (positions `0, …, e`) is projective
    (hproj : ∀ i : Fin (e + 1), Projective (S.obj i.castSucc.castSucc)) :
    -- the leftmost syzygy `Ker(F_e → F_{e-1})` (or `Ker(F_0 → M)` when `e = 0`)
    -- is projective
    Projective (Limits.kernel (S.map' 0 1))
```

## Tag 0CXC, a lemma

[Tag 0CXC](https://stacks.math.columbia.edu/tag/0CXC) in the Stacks Project.

**`CategoryTheory.hasProjectiveDimensionLE_tfae_leftResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 660](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L660). The attribute's comment: “A resolution `⋯ → P₁ → P₀ → M → 0` is an `ObjectProperty.LeftResolution` by the class of projective objects (00LQ), the notion 00O7 uses; the source's `M`, `Ker(P₀ → M)` and `Ker(P_{d-1} → P_{d-2})` are the single syzygy `(F.complex.toSingle₀AsComplex X F.π).cycles d`, the `d`-th cycles of the augmentation `F.π` read as a complex; see the module docstring.”. References: EGA 0 (17.2.1), “dim.proj resolution char”.

> **Stacks 0CXC.** Let `X` be an object of an abelian category which admits a projective
> resolution, and let `d : ℕ`. The following are equivalent: (1) `X` has projective dimension
> at most `d`; (2) there is a resolution `0 → P_d → ⋯ → P₀ → X → 0` by projectives, that is, a
> left resolution `F` of `X` by projective objects with `F.complex.X i = 0` for `i > d`; (3) for
> some resolution `⋯ → P₁ → P₀ → X → 0` by projectives the `d`-th syzygy of `X`, the `d`-th cycles
> object of the augmented complex, is projective; (4) for every such resolution the `d`-th syzygy
> is projective.

```lean
public theorem CategoryTheory.hasProjectiveDimensionLE_tfae_leftResolution {C : Type u}
    [Category.{v} C] [Abelian C] (X : C) [HasProjectiveResolution X] (d : ℕ) :
    List.TFAE
      [HasProjectiveDimensionLE X d,
        ∃ F : ObjectProperty.LeftResolution (isProjective C) X,
          ∀ i, d < i → Limits.IsZero (F.complex.X i),
        ∃ F : ObjectProperty.LeftResolution (isProjective C) X,
          Projective ((F.complex.toSingle₀AsComplex X F.π).cycles d),
        ∀ F : ObjectProperty.LeftResolution (isProjective C) X,
          Projective ((F.complex.toSingle₀AsComplex X F.π).cycles d)]
```

## Tag 0CXD, a lemma

[Tag 0CXD](https://stacks.math.columbia.edu/tag/0CXD) in the Stacks Project.

**`ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/ProjectiveDimension.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/ProjectiveDimension.lean#L177). The attribute's comment: “Condition (5) is added to Lemma 0CXC by stating its equivalence with item 1 of that lemma's `TFAE`. A resolution `0 → P_d → ⋯ → P₀ → M → 0` by frees is an `ObjectProperty.LeftResolution` for the class of free modules (00LQ), the notion 0CXC and 00O7 use, vanishing in degrees `> d`; see the module docstring.”.

> **Stacks 0CXD.** Let `R` be a commutative local ring, let `M` be an `R`-module and let
> `d : ℕ`. Then `M` has projective dimension at most `d` — equivalently, by Stacks 0CXC, `M` has a
> resolution of length `d` by projectives — if and only if `M` has a resolution
> `0 → P_d → ⋯ → P₀ → M → 0` by *free* modules, that is, a left resolution `F` of `M` by free
> modules with `F.complex.X i = 0` for `i > d`.

```lean
public theorem ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free {R : Type u}
    [CommRing R] [IsLocalRing R] [Small.{v} R] (M : ModuleCat.{v} R) (d : ℕ) :
    HasProjectiveDimensionLE M d ↔
      ∃ F : ObjectProperty.LeftResolution (fun N : ModuleCat.{v} R => Module.Free R N) M,
        ∀ i, d < i → IsZero (F.complex.X i)
```

## Tag 0CXE, a lemma

[Tag 0CXE](https://stacks.math.columbia.edu/tag/0CXE) in the Stacks Project.

**`ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_projective_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/FiniteResolution.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension/FiniteResolution.lean#L332). The attribute's comment: “Condition (6) is added to Lemma 0CXC by stating its equivalence with item 1 of that lemma's `TFAE`. A resolution `0 → P_d → ⋯ → P₀ → M → 0` by finite projectives is an `ObjectProperty.LeftResolution` for the class of finite projective modules (00LQ), the notion 0CXC, 0CXD and 00O7 use, vanishing in degrees `> d`; stated for a not necessarily commutative ring. See the module docstring.”. References: EGA 0 (17.2.2).

> **Stacks 0CXE.** Let `R` be a Noetherian ring, let `M` be a finite `R`-module and let `d : ℕ`.
> Then `M` has projective dimension at most `d` — equivalently, by Stacks 0CXC, `M` has a resolution
> of length `d` by projectives — if and only if `M` has a resolution `0 → P_d → ⋯ → P₀ → M → 0` by
> *finite projective* modules, that is, a left resolution `F` of `M` by projective modules that are
> finite over `R`, with `F.complex.X i = 0` for `i > d`.

```lean
public theorem ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_projective_finite
    {R : Type u} [Ring R] [IsNoetherianRing R] [Small.{v} R] (M : ModuleCat.{v} R)
    [Module.Finite R M] (d : ℕ) :
    HasProjectiveDimensionLE M d ↔
      ∃ F : ObjectProperty.LeftResolution
          (fun N : ModuleCat.{v} R => Projective N ∧ Module.Finite R N) M,
        ∀ i, d < i → IsZero (F.complex.X i)
```

## Tag 0CXF, a lemma

[Tag 0CXF](https://stacks.math.columbia.edu/tag/0CXF) in the Stacks Project.

**`ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/ProjectiveDimension.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/ProjectiveDimension.lean#L379). The attribute's comment: “Condition (7) is added to Lemmas 0CXC, 0CXD and 0CXE by stating its equivalence with item 1 of 0CXC's `TFAE`. A resolution `0 → F_d → ⋯ → F₀ → M → 0` by finite frees is an `ObjectProperty.LeftResolution` for the class of finite free modules (00LQ), the notion 00O7 uses, vanishing in degrees `> d`; see the module docstring.”. References: EGA 0 (17.2.2).

> **Stacks 0CXF.** Let `R` be a local Noetherian ring, let `M` be a finite `R`-module and let
> `d : ℕ`. Then `M` has projective dimension at most `d` — equivalently, by Stacks 0CXC, 0CXD and
> 0CXE, `M` has a resolution of length `d` by projectives, by frees, or by finite projectives — if
> and only if `M` has a resolution `0 → F_d → ⋯ → F₀ → M → 0` by *finite free* modules, that is, a
> left resolution `F` of `M` by free modules that are finite over `R`, with `F.complex.X i = 0` for
> `i > d`.

```lean
public theorem ModuleCat.hasProjectiveDimensionLE_iff_exists_leftResolution_free_finite
    {R : Type u} [CommRing R] [IsLocalRing R] [IsNoetherianRing R] [Small.{v} R]
    (M : ModuleCat.{v} R) [Module.Finite R M] (d : ℕ) :
    HasProjectiveDimensionLE M d ↔
      ∃ F : ObjectProperty.LeftResolution
          (fun N : ModuleCat.{v} R => Module.Free R N ∧ Module.Finite R N) M,
        ∀ i, d < i → IsZero (F.complex.X i)
```

## Tag 065R, a lemma

[Tag 065R](https://stacks.math.columbia.edu/tag/065R) in the Stacks Project.

**`CategoryTheory.hasProjectiveDimensionLT_of_enoughProjectives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/Projective/Dimension.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/Projective/Dimension.lean#L103). The attribute's comment: “The implication `(3) ⇒ (1)`, proved the source's way: in an abelian category with enough projectives, indexed by `HasProjectiveDimensionLT X n`, so that the source's `R`-modules of projective dimension `≤ n` are the case `C = ModuleCat.{v} R` at `n + 1`. The converse `(1) ⇒ (2)` and, at a single degree, `(2) ⇒ (3)` are `hasProjectiveDimensionLT_iff`; the sibling under enough injectives is `hasProjectiveDimensionLT_of_enoughInjectives`. Projective dimension is Ext-measured here rather than defined by a finite projective resolution (Definition 00O4, Lemma 0CXC); see the module docstring.”.

> Let `X` be an object of an abelian category with enough projectives and let `n : ℕ`. If the
> single group `Extⁿ(X, Y)` vanishes for every object `Y`, then `X` has projective dimension `< n`.

```lean
public theorem CategoryTheory.hasProjectiveDimensionLT_of_enoughProjectives {C : Type u}
    [Category.{v} C] [Abelian C] [HasExt.{w} C] [EnoughProjectives C] (X : C) (n : ℕ)
    (hX : ∀ Y : C, Subsingleton (Ext.{w} X Y n)) : HasProjectiveDimensionLT X n
```

## Tag 065S, a lemma

[Tag 065S](https://stacks.math.columbia.edu/tag/065S) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₁`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₁#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 1821](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L1821) (StacksFrontier): “(1)”.
- [`CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₂#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 1822](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L1822) (StacksFrontier): “(2)”.
- [`CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₃`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ShortComplex.ShortExact.hasProjectiveDimensionLT_X₃#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/ProjectiveDimension.lean, line 1823](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension.lean#L1823) (StacksFrontier): “(3)”.

## Tag 00O6, a definition

[Tag 00O6](https://stacks.math.columbia.edu/tag/00O6) in the Stacks Project.

**`ringGlobalDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GlobalDimension/Defs.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GlobalDimension/Defs.lean#L128). The attribute's comment: “The global dimension is the supremum `⨆ M, projectiveDimension M` over the `R`-modules in `R`'s own universe; `R` has finite global dimension iff this is `≠ ⊤`. See the module docstring.”.

> The **global dimension** of a ring `R`: the supremum of the projective dimensions of all
> `R`-modules, an element of `WithBot ℕ∞`. It is `≤ n` exactly when every `R`-module admits a
> resolution of length `≤ n` by projective modules (00O5, 0CXC), so it is the source's minimal such
> `n`, and `R` has *finite global dimension* exactly when `ringGlobalDimension R ≠ ⊤`. It is `⊥`
> for the zero ring.

```lean
public noncomputable abbrev ringGlobalDimension (R : Type u) [Ring R] : WithBot ℕ∞
```

## Tag 0D1U, a lemma

[Tag 0D1U](https://stacks.math.columbia.edu/tag/0D1U) in the Stacks Project.

**`ModuleCat.hasProjectiveDimensionLT_of_monotone_of_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Filtration.lean, line 637](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension/Filtration.lean#L637). The attribute's comment: “Indexed by `HasProjectiveDimensionLT _ n`, so that the source's `≤ n` is the case `n + 1`; the source's well-ordered family of submodules is a `Monotone` family over a type with `[LinearOrder E] [WellFoundedLT E]`, its union is `⨆ e, N e = ⊤`, and the graded piece at `e` is `↥(N e) ⧸ (⨆ e' < e, N e').submoduleOf (N e)`. See the module docstring.”.

> **Stacks 0D1U.** Let `R` be a ring and let `M` be an `R`-module which is the union
> `⨆ e, N e = ⊤` of a monotone family of submodules `N` indexed by a well-ordered type `E`. If each
> graded piece `N e ⧸ ⨆ e' < e, N e'` has projective dimension `< n`, then so does `M`.

```lean
public theorem ModuleCat.hasProjectiveDimensionLT_of_monotone_of_iSup_eq_top {R : Type u} [Ring R]
    [Small.{v} R] {M : ModuleCat.{v} R} {E : Type w} [LinearOrder E] [WellFoundedLT E]
    (N : E → Submodule R M) (hN : Monotone N) (hNtop : ⨆ e, N e = ⊤) (n : ℕ)
    (hquot : ∀ e, HasProjectiveDimensionLT
      (ModuleCat.of R (↥(N e) ⧸ (⨆ e' < e, N e').submoduleOf (N e))) n) :
    HasProjectiveDimensionLT M n
```

## Tag 065T, a lemma

[Tag 065T](https://stacks.math.columbia.edu/tag/065T) in the Stacks Project.

**`ringGlobalDimension_lt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GlobalDimension/Cyclic.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GlobalDimension/Cyclic.lean#L273). The attribute's comment: “Indexed by `HasProjectiveDimensionLT _ n`, so that the source's `≤ n` is the case `n + 1`; item (1) is the global dimension `⨆ M, projectiveDimension M` of Tag 00O6, and the modules of items (2) and (3) range over an arbitrary universe `v` with `Small.{v} R`, of which the source is the case `v = u`. See the module docstring.”. References: EGA 0 (17.2.8), “a) <=> a')”.

> **Stacks 065T.** Let `R` be a ring and `n : ℕ`. The following are equivalent: the global
> dimension of `R` is `< n`; every `R`-module has projective dimension `< n`; every finite
> `R`-module has projective dimension `< n`; every cyclic `R`-module `R ⧸ I` has projective
> dimension `< n`. The source's bound `≤ n` is the case `n + 1`.

```lean
public theorem ringGlobalDimension_lt_tfae (R : Type u) [Ring R] [Small.{v} R] (n : ℕ) :
    List.TFAE
      [(⨆ M : ModuleCat.{u} R, projectiveDimension M) < n,
       ∀ M : ModuleCat.{v} R, HasProjectiveDimensionLT M n,
       ∀ M : ModuleCat.{v} R, Module.Finite R M → HasProjectiveDimensionLT M n,
       ∀ I : Ideal R, HasProjectiveDimensionLT (ModuleCat.of R (R ⧸ I)) n]
```

## Tag 00O8, a lemma

[Tag 00O8](https://stacks.math.columbia.edu/tag/00O8) in the Stacks Project.

**`Module.projectiveDimension_localizedModule_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Localization.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension/Localization.lean#L49). The attribute's comment: “(1)”.

> **Stacks 00O8 (1).** Let `R` be a ring, `M` an `R`-module and `S ⊆ R` a multiplicative
> subset. If `M` has projective dimension `≤ n`, then `S⁻¹M` has projective dimension `≤ n` over
> `S⁻¹R`. Projective dimension is the library's `Module.projectiveDimension` (Stacks 00O4); the
> module `M` lives in any universe in which `R` is small, the hypothesis under which that invariant
> is the source's minimal length of a projective resolution (00O5, 0CXC). The localization `S⁻¹M`
> is `LocalizedModule S M` itself, in its own universe.

```lean
theorem Module.projectiveDimension_localizedModule_le {R : Type u} [CommRing R] [Small.{v} R]
    (S : Submonoid R) (M : Type v) [AddCommGroup M] [Module R M] (n : ℕ)
    (hM : Module.projectiveDimension R M ≤ n) :
    Module.projectiveDimension (Localization S) (LocalizedModule S M) ≤ n
```

**`ringGlobalDimension_localization_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ProjectiveDimension/Localization.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/ProjectiveDimension/Localization.lean#L73). The attribute's comment: “(2)”.

> **Stacks 00O8 (2).** Let `R` be a ring and `S ⊆ R` a multiplicative subset. If `R` has
> finite global dimension `≤ n`, then so does `S⁻¹R`. Global dimension is the library's
> `ringGlobalDimension` (Stacks 00O6), the supremum of the projective dimensions of all modules,
> which is `≤ n` exactly when every module has a projective resolution of length `≤ n`. The proof
> is the source's: every `S⁻¹R`-module `M'` is its own localization `S⁻¹M'`, so (1) applies.

```lean
theorem ringGlobalDimension_localization_le {R : Type u} [CommRing R] (S : Submonoid R) (n : ℕ)
    (hR : ringGlobalDimension R ≤ n) : ringGlobalDimension (Localization S) ≤ n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.109, Tag 00O2](https://stacks.math.columbia.edu/tag/00O2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
