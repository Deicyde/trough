---
declaration: section
origin: cited
lean: AlgebraicGeometry.NoTraceOnOneForms.mem_A_iff_flip_eq, AlgebraicGeometry.NoTraceOnOneForms.A_normal, AlgebraicGeometry.NoTraceOnOneForms.A_finiteType, AlgebraicGeometry.NoTraceOnOneForms.x_dy_flip_invariant, AlgebraicGeometry.NoTraceOnOneForms.two_mul_x_dy_not_mem_span, AlgebraicGeometry.NoTraceOnOneForms.two_mul_x_dy_not_mem_range, AlgebraicGeometry.existsUnique_formsTraceRule, AlgebraicGeometry.Scheme.Hom.formsTrace_isComplexMap
statement: formalized
proof: formalized
---

# 50.19 Trace maps on de Rham complexes

Section 50.19 of the Stacks Project, [Tag 0FK6](https://stacks.math.columbia.edu/tag/0FK6). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FK7, an example

[Tag 0FK7](https://stacks.math.columbia.edu/tag/0FK7) in the Stacks Project.

**`AlgebraicGeometry.NoTraceOnOneForms.mem_A_iff_flip_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L199). The attribute's comment: “invariant ring”.

> The three quadratic monomials generate precisely the simultaneous-negation invariants.

```lean
theorem mem_A_iff_flip_eq (p : B) : p ∈ A ↔ flip p = p
```

**`AlgebraicGeometry.NoTraceOnOneForms.A_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L243). The attribute's comment: “normal domain”.

> The invariant ring is a normal domain.

```lean
theorem A_normal : IsNormalDomain A
```

**`AlgebraicGeometry.NoTraceOnOneForms.A_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L256). The attribute's comment: “finite type”.

> The invariant ring is of finite type over `ℂ`.

```lean
theorem A_finiteType : Algebra.FiniteType ℂ A
```

**`AlgebraicGeometry.NoTraceOnOneForms.x_dy_flip_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L261). The attribute's comment: “invariant one-form”.

> Simultaneously negating the variables fixes `x dy`.

```lean
theorem x_dy_flip_invariant :
    flip x • KaehlerDifferential.D ℂ B (flip y) =
      x • KaehlerDifferential.D ℂ B y
```

**`AlgebraicGeometry.NoTraceOnOneForms.two_mul_x_dy_not_mem_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L268). The attribute's comment: “failure of descent for one-forms”.

> The form `2 x dy` does not lie in the `B`-span of the differentials of `x²`, `xy` and `y²`.

```lean
theorem two_mul_x_dy_not_mem_span :
    (2 : B) • (x • KaehlerDifferential.D ℂ B y) ∉
      Submodule.span B
        ({KaehlerDifferential.D ℂ B (x * x),
          KaehlerDifferential.D ℂ B (x * y),
          KaehlerDifferential.D ℂ B (y * y)} : Set Ω[B⁄ℂ])
```

**`AlgebraicGeometry.NoTraceOnOneForms.two_mul_x_dy_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/TraceMapsDe/Basic.lean#L353). The attribute's comment: “failure of the differential map to capture the invariant form”.

> Twice the invariant one-form does not come from the invariant ring.

```lean
theorem two_mul_x_dy_not_mem_range :
    (2 : B) • (x • KaehlerDifferential.D ℂ B y) ∉
      LinearMap.range (KaehlerDifferential.map ℂ ℂ A B)
```

## Tag 0FLB, a lemma

[Tag 0FLB](https://stacks.math.columbia.edu/tag/0FLB) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_formsTraceRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormsTrace/Main.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormsTrace/Main.lean#L43).

> **Stacks, Lemma 0FLB.** There exists a unique rule that to every finite syntomic morphism of
> schemes `f : Y ⟶ X` assigns `𝒪_X`-module maps `Θ^p_{Y/X} : f_*Ω^p_{Y/ℤ} ⟶ Ω^p_{X/ℤ}` such that
> (1) the composition with `Ω^p_{X/ℤ} ⊗_{𝒪_X} f_*𝒪_Y → f_*Ω^p_{Y/ℤ}` is `id ⊗ Trace_f`
> (`FormsTraceRule.IsTrace`, on local sections `ω ⊗ b ↦ b · f^*ω`), and (2) the rule is compatible
> with base change (`FormsTraceRule.IsBaseChange`). The rule is `formsTraceRule`.

```lean
theorem existsUnique_formsTraceRule :
    ∃! Θ : FormsTraceRule.{u}, Θ.IsTrace ∧ Θ.IsBaseChange
```

## Tag 0FLC, a proposition

[Tag 0FLC](https://stacks.math.columbia.edu/tag/0FLC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.formsTrace_isComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormsTrace/Proposition.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormsTrace/Proposition.lean#L59).

> **Stacks, Proposition 0FLC.** Let `f : Y ⟶ X` be a finite syntomic morphism of schemes. The
> maps `Θ^p_{Y/X} : f_*Ω^p_{Y/ℤ} ⟶ Ω^p_{X/ℤ}` of Lemma 0FLB (`formsTrace`, the rule
> `formsTraceRule` of `existsUnique_formsTraceRule`) define a map of complexes
> `f_*Ω^•_{Y/ℤ} ⟶ Ω^•_{X/ℤ}`: on every open `U` of `X`, `Θ^{p+1}(dη) = d Θ^p(η)`. Moreover:
>
> 1. in degree `0` it is `Trace_f : f_*𝒪_Y ⟶ 𝒪_X`, through `Ω^0 ≅ 𝒪` on both sides;
> 2. `Θ(ω ∧ η) = ω ∧ Θ(η)` for local sections `ω` of `Ω^q_{X/ℤ}` and `η` of `f_*Ω^p_{Y/ℤ}`
>    (`ω` acting on `f_*Ω^•_{Y/ℤ}` through `f^*`);
> 3. if `f` is a morphism over a base scheme `S`, i.e. for every `g : X ⟶ S`, the maps `Θ^p_{Y/X}`
>    induce maps `f_*Ω^p_{Y/S} ⟶ Ω^p_{X/S}` (compatible with `Θ^p_{Y/X}` through the canonical
>    surjections `Ω^p_{·/ℤ} → Ω^p_{·/S}`) forming a map of complexes.

```lean
theorem formsTrace_isComplexMap :
    haveI := AlgebraicGeometry.flat hf
    haveI := AlgebraicGeometry.locallyOfFinitePresentation hf
    -- a map of complexes
    (∀ (p : ℕ) (U : X.Opens) (η : Γ(absoluteDifferentialForms Y p, f ⁻¹ᵁ U)),
      (f.formsTrace hf (p + 1)).app U
          ((Y.toSpecZ.deRhamComplex.d p (p + 1)).val.app (op (f ⁻¹ᵁ U)) η) =
        (X.toSpecZ.deRhamComplex.d p (p + 1)).val.app (op U) ((f.formsTrace hf p).app U η)) ∧
    -- (1) degree zero is the trace
    f.formsTrace hf 0 ≫ (relativeDifferentialFormsZeroIso X.toSpecZ).hom =
      (Scheme.Modules.pushforward f).map (relativeDifferentialFormsZeroIso Y.toSpecZ).hom ≫
        f.finiteTrace ∧
    -- (2) linearity over the forms of `X`
    (∀ (q p : ℕ) (U : X.Opens) (ω : Γ(absoluteDifferentialForms X q, U))
      (η : Γ(absoluteDifferentialForms Y p, f ⁻¹ᵁ U)),
      (f.formsTrace hf (q + p)).app U
          ((eqToHom (congrArg (absoluteDifferentialForms Y) (Nat.cast_add q p).symm)).val.app
            (op (f ⁻¹ᵁ U)) (((absoluteDifferentialFormsAlgebra Y).mul q p).app (op (f ⁻¹ᵁ U))
              (f.absoluteFormsPullback q U ω) η)) =
        (eqToHom (congrArg (absoluteDifferentialForms X) (Nat.cast_add q p).symm)).val.app (op U)
          (((absoluteDifferentialFormsAlgebra X).mul q p).app (op U) ω
            ((f.formsTrace hf p).app U η))) ∧
    -- (3) the relative version over a base
    (∀ {S : Scheme.{u}} (g : X ⟶ S), ∃ ΘS : ∀ p : ℕ,
        (Scheme.Modules.pushforward f).obj (relativeDifferentialForms (f ≫ g) p) ⟶
          relativeDifferentialForms g p,
      (∀ p : ℕ, (Scheme.Modules.pushforward f).map ((f ≫ g).absoluteToRelativeFormsMap p) ≫
          ΘS p = f.formsTrace hf p ≫ g.absoluteToRelativeFormsMap p) ∧
      ∀ (p : ℕ) (U : X.Opens) (η : Γ(relativeDifferentialForms (f ≫ g) p, f ⁻¹ᵁ U)),
        (ΘS (p + 1)).app U (((f ≫ g).deRhamComplex.d p (p + 1)).val.app (op (f ⁻¹ᵁ U)) η) =
          (g.deRhamComplex.d p (p + 1)).val.app (op U) ((ΘS p).app U η))
```

## Tag 0FLD, an example

[Tag 0FLD](https://stacks.math.columbia.edu/tag/0FLD) in the Stacks Project.

**`AlgebraicGeometry.formsTrace_app_top_eq_frameTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormsTrace/MonogenicExample.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormsTrace/MonogenicExample.lean#L124). The attribute's comment: “the map `Θ_{B/A} : Ω^•_B → Ω^•_A` of the example is the map of Proposition 0FLC for `Spec B → Spec A` on global sections”.

> **Stacks, Example 0FLD: the map `Θ_{B/A}` is the one of Proposition 0FLC.** Let `B` have a
> power basis of positive dimension over `A`, for instance `B = A[x]/(f)` with `f` monic of degree
> `d ≥ 1`. Then `Spec B → Spec A` is finite syntomic (`isFinite_specMap_of_powerBasis`,
> `syntomic_specMap_of_powerBasis`), and on global sections the map of de Rham complexes
> `Θ_{Spec B/Spec A}` given by `Scheme.Hom.formsTrace` is the trace map `Θ_{B/A} = frameTrace A B`
> on the forms of `B`: the global section of `Ω^p_{Spec B/ℤ}` corresponding to a `p`-form `x` of `B`
> goes to the global section of `Ω^p_{Spec A/ℤ}` corresponding to `Θ_{B/A}(x)` (with `A`, `B`
> identified with their rings of global sections by the canonical isomorphisms).

```lean
theorem formsTrace_app_top_eq_frameTrace (pb : PowerBasis A B) (hdim : 0 < pb.dim)
    [Algebra A Γ(Spec (.of A), ⊤)]
    [Algebra B Γ(Spec (.of B), Spec.map (CommRingCat.ofHom (algebraMap A B)) ⁻¹ᵁ ⊤)]
    (hA : algebraMap A Γ(Spec (.of A), ⊤) = (Scheme.ΓSpecIso (.of A)).inv.hom)
    (hB : algebraMap B Γ(Spec (.of B), Spec.map (CommRingCat.ofHom (algebraMap A B)) ⁻¹ᵁ ⊤) =
      (Scheme.ΓSpecIso (.of B)).inv.hom)
    (p : ℕ) (x : ⋀[B]^p Ω[B⁄ℤ]) :
    haveI := isFinite_specMap_of_powerBasis pb
    Scheme.absoluteFormsSectionsEquiv (Spec (.of A)) (isAffineOpen_top _) p
        (((Spec.map (CommRingCat.ofHom (algebraMap A B))).formsTrace
            (syntomic_specMap_of_powerBasis pb) p).app ⊤
          ((Scheme.absoluteFormsSectionsEquiv (Spec (.of B))
              ((isAffineOpen_top _).preimage (Spec.map (CommRingCat.ofHom (algebraMap A B))))
                p).symm
            (formsMap B Γ(Spec (.of B), Spec.map (CommRingCat.ofHom (algebraMap A B)) ⁻¹ᵁ ⊤) p
              x))) =
      formsMap A Γ(Spec (.of A), ⊤) p (frameTrace A B p x)
```

**`Stacks.FormsTrace.frameTrace_oneForm_D_root`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean#L179). The attribute's comment: “`Θ(dt) = -da₁`”.

> **Stacks, Example 0FLD: `Θ(dt) = -da₁`.** Let `f = x^d + ∑_{0 ≤ i < d} a_{d - i} x^i` with
> `d ≥ 1`, let `B ≅ A[x]/(f)` and let `t ∈ B` be the image of `x`. Then the trace map
> `Θ_{B/A} : Ω^•_B → Ω^•_A` of Proposition 0FLC sends `dt` to `-da₁`.

```lean
theorem frameTrace_oneForm_D_root (hd : 1 ≤ d)
    (e : AdjoinRoot (monicOfCoefficients d a) ≃ₐ[A] B) :
    frameTrace A B 1
        (oneForm B Ω[B⁄ℤ] (D ℤ B (e (AdjoinRoot.root (monicOfCoefficients d a))))) =
      oneForm A Ω[A⁄ℤ] (-D ℤ A (a 1))
```

**`Stacks.FormsTrace.frameTrace_root_smul_oneForm_D_root`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean#L199). The attribute's comment: “`Θ(t dt) = a₁ da₁ - da₂`”.

> **Stacks, Example 0FLD: `Θ(t dt) = a₁ da₁ - da₂`.** Let `f = x^d + ∑_{0 ≤ i < d} a_{d - i} x^i`
> with `d ≥ 2`, let `B ≅ A[x]/(f)` and let `t ∈ B` be the image of `x`. Then the trace map
> `Θ_{B/A}` of Proposition 0FLC sends `t dt` to `a₁ da₁ - da₂`.

```lean
theorem frameTrace_root_smul_oneForm_D_root (hd : 2 ≤ d)
    (e : AdjoinRoot (monicOfCoefficients d a) ≃ₐ[A] B) :
    frameTrace A B 1 (e (AdjoinRoot.root (monicOfCoefficients d a)) •
        oneForm B Ω[B⁄ℤ] (D ℤ B (e (AdjoinRoot.root (monicOfCoefficients d a))))) =
      oneForm A Ω[A⁄ℤ] (a 1 • D ℤ A (a 1) - D ℤ A (a 2))
```

**`Stacks.FormsTrace.frameTrace_root_sq_smul_oneForm_D_root`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean#L223). The attribute's comment: “`Θ(t² dt) = -a₁² da₁ + a₁ da₂ + a₂ da₁ - da₃`”.

> **Stacks, Example 0FLD: `Θ(t² dt) = -a₁² da₁ + a₁ da₂ + a₂ da₁ - da₃`.** Let
> `f = x^d + ∑_{0 ≤ i < d} a_{d - i} x^i` with `d ≥ 3`, let `B ≅ A[x]/(f)` and let `t ∈ B` be the
> image of `x`. Then the trace map `Θ_{B/A}` of Proposition 0FLC sends `t² dt` to
> `-a₁² da₁ + a₁ da₂ + a₂ da₁ - da₃` (and the source's "modulo calculation error" is not needed).

```lean
theorem frameTrace_root_sq_smul_oneForm_D_root (hd : 3 ≤ d)
    (e : AdjoinRoot (monicOfCoefficients d a) ≃ₐ[A] B) :
    frameTrace A B 1 (e (AdjoinRoot.root (monicOfCoefficients d a)) ^ 2 •
        oneForm B Ω[B⁄ℤ] (D ℤ B (e (AdjoinRoot.root (monicOfCoefficients d a))))) =
      oneForm A Ω[A⁄ℤ] (-(a 1 ^ 2 • D ℤ A (a 1)) + a 1 • D ℤ A (a 2) + a 2 • D ℤ A (a 1) -
        D ℤ A (a 3))
```

**`Stacks.FormsTrace.frameTrace_root_pow_smul_oneForm_D_root_X_pow_sub_C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean#L285). The attribute's comment: “for `f = x^d - a`: `Θ(t^i dt) = 0` for `i = 0, …, d - 2`”.

> **Stacks, Example 0FLD: for `f = x^d - a`, `Θ(t^i dt) = 0` for `i = 0, …, d - 2`.** Let
> `B ≅ A[x]/(x^d - a)` with `d ≥ 1` and let `t ∈ B` be the image of `x`. Then the trace map
> `Θ_{B/A}` of Proposition 0FLC kills `t^i dt` for `i + 1 < d`.

```lean
theorem frameTrace_root_pow_smul_oneForm_D_root_X_pow_sub_C
    (e : AdjoinRoot (Polynomial.X ^ d - C a) ≃ₐ[A] B) {i : ℕ} (hi : i + 1 < d) :
    frameTrace A B 1 (e (AdjoinRoot.root (Polynomial.X ^ d - C a)) ^ i •
        oneForm B Ω[B⁄ℤ] (D ℤ B (e (AdjoinRoot.root (Polynomial.X ^ d - C a))))) = 0
```

**`Stacks.FormsTrace.frameTrace_root_pow_pred_smul_oneForm_D_root_X_pow_sub_C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormsTrace/MonogenicExample.lean#L298). The attribute's comment: “for `f = x^d - a`: `Θ(t^{d-1} dt) = da`”.

> **Stacks, Example 0FLD: for `f = x^d - a`, `Θ(t^{d-1} dt) = da`.** Let `B ≅ A[x]/(x^d - a)`
> with `d ≥ 1` and let `t ∈ B` be the image of `x`. Then the trace map `Θ_{B/A}` of
> Proposition 0FLC sends `t^{d-1} dt` to `da`.

```lean
theorem frameTrace_root_pow_pred_smul_oneForm_D_root_X_pow_sub_C
    (e : AdjoinRoot (Polynomial.X ^ d - C a) ≃ₐ[A] B) :
    frameTrace A B 1 (e (AdjoinRoot.root (Polynomial.X ^ d - C a)) ^ (d - 1) •
        oneForm B Ω[B⁄ℤ] (D ℤ B (e (AdjoinRoot.root (Polynomial.X ^ d - C a))))) =
      oneForm A Ω[A⁄ℤ] (D ℤ A a)
```

## Tag 0FW2, a lemma

[Tag 0FW2](https://stacks.math.columbia.edu/tag/0FW2) in the Stacks Project.

**`AlgebraicGeometry.relativeFrobenius_relativeFormsTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormsTrace/RelativeFrobenius.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormsTrace/RelativeFrobenius.lean#L132). References: SGA 5 XV (1.Proposition2), “Clause a), special case”.

> **Stacks, Lemma 0FW2.** Let `p` be a prime number and let `X → S` be a smooth morphism of
> relative dimension `d` of schemes in characteristic `p`. Then:
>
> * the relative Frobenius `F = F_{X/S} : X → X^{(p)}` (Varieties, Definition 0CC9) is finite and
>   syntomic; it is a morphism over `S`, `F ≫ (X^{(p)} → S) = (X → S)`, so `F_*Ω^•_{F ≫ g}` is
>   `F_{X/S,*}Ω^•_{X/S}`;
> * the corresponding map `Θ_{X/X^{(p)}} : F_{X/S,*}Ω^•_{X/S} → Ω^•_{X^{(p)}/S}` of Proposition
>   0FLC (3) (`AlgebraicGeometry.Scheme.Hom.relativeFormsTrace`, a map of complexes by
>   `AlgebraicGeometry.Scheme.Hom.relativeFormsTrace_deRhamComplex_d`) is zero in every degree
>   `k ≠ d`;
> * in degree `d` it is a surjection (an epimorphism of sheaves of modules on `X^{(p)}`).

```lean
theorem relativeFrobenius_relativeFormsTrace :
    haveI := isFinite_relativeFrobenius S p hS X d
    IsFinite (relativeFrobenius S p hS X).left ∧ Syntomic (relativeFrobenius S p hS X).left ∧
      (relativeFrobenius S p hS X).left ≫ ((frobeniusTwist S p hS).obj X).hom = X.hom ∧
      (∀ k ≠ d, (relativeFrobenius S p hS X).left.relativeFormsTrace
          ((frobeniusTwist S p hS).obj X).hom (syntomic_relativeFrobenius S p hS X d) k = 0) ∧
      Epi ((relativeFrobenius S p hS X).left.relativeFormsTrace
          ((frobeniusTwist S p hS).obj X).hom (syntomic_relativeFrobenius S p hS X d) d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.19, Tag 0FK6](https://stacks.math.columbia.edu/tag/0FK6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
