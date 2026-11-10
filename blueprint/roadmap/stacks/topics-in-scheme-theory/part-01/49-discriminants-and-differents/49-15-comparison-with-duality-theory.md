---
declaration: section
origin: cited
lean: Stacks.Duality.relativeDualizingModule_upperShriek_structureSheaf, Stacks.Duality.upperShriekRelativeDualizingModuleData, Stacks.Duality.existsUnique_upperShriekRelativeDualizingComparison, Stacks.Duality.upperShriekDualSection_pushforwardTrace
statement: formalized
proof: formalized
---

# 49.15 Comparison with duality theory

Section 49.15 of the Stacks Project, [Tag 0DWM](https://stacks.math.columbia.edu/tag/0DWM). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BUL, a lemma

[Tag 0BUL](https://stacks.math.columbia.edu/tag/0BUL) in the Stacks Project.

**`Stacks.Duality.relativeDualizingModule_upperShriek_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/RelativeDualizingModuleShriek.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/RelativeDualizingModuleShriek.lean#L62). The attribute's comment: “the whole lemma: H^0(V, f^! O) = omega_{B/A} compatibly with restriction, the canonical isomorphism H^0(f^! O) = omega_{Y/X}, and H^0(f_new^! O) = omega_{Y/X}”.

> **Stacks Project, Tag 0BUL.** (1) Let `S` be Noetherian, `f : X ⟶ Y` a locally quasi-finite
> morphism of schemes separated and of finite type over `S` and `j` any compactification computing
> `f^!` (Tag 0A9Y). Then `H⁰(f^!𝒪_Y)` is the sheaf of a relative dualizing module datum of `f`
> (Tag 0BVG): its sections over affine opens `V ⊆ f⁻¹U` are identified with `ω_{Γ(V)/Γ(U)}`,
> compatibly with restriction; and for every relative dualizing module `ω_{X/Y}` there is exactly
> one family of isomorphisms on sections, compatible with restriction, carrying these affine
> identifications to those of `ω_{X/Y}` — the canonical isomorphism `H⁰(f^!𝒪_Y) = ω_{X/Y}`.
> (2) Let `S` be a Noetherian scheme with a dualizing complex `ω_S^•`, `f : X ⟶ Y` a locally
> quasi-finite morphism of schemes of finite type over `S` (not necessarily separated), `ω_X^•`,
> `ω_Y^•` dualizing complexes normalized relative to `ω_S^•` and `f_new^! = D_X ∘ Lf^* ∘ D_Y`.
> Then `H⁰(f_new^!𝒪_Y)` is the sheaf of a relative dualizing module datum of `f`, i.e.
> `H⁰(f_new^!𝒪_Y) = ω_{X/Y}`.

```lean
theorem relativeDualizingModule_upperShriek_structureSheaf :
    (∀ {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S} (f : X ⟶ Y) [LocallyQuasiFinite f.left]
        (j : CompactificationOf (Over.mk f.left)),
        (∃ D : RelativeDualizingModuleData f.left, D.sheaf = upperShriekStructureSheafZeroth f j) ∧
        ∀ ω : RelativeDualizingModuleData f.left,
          ∃! E : ∀ W : X.left.Opens,
              Γ(upperShriekStructureSheafZeroth f j, W) ≃ₗ[Γ(X.left, W)] Γ(ω.sheaf, W),
            (∀ (W W' : X.left.Opens) (h : W' ≤ W) (s : Γ(upperShriekStructureSheafZeroth f j, W)),
                E W' (Stacks.AlgebraicGeometry.QuasicoherentBaseChange.restrictₗ _ h s) =
                  Stacks.AlgebraicGeometry.QuasicoherentBaseChange.restrictₗ ω.sheaf h (E W s)) ∧
              ∀ (U : Y.left.affineOpens) (V : X.left.affineOpens) (hVU : V.1 ≤ f.left ⁻¹ᵁ U.1),
                letI : Algebra Γ(Y.left, U.1) Γ(X.left, V.1) := (f.left.appLE U V hVU).hom.toAlgebra
                ∀ (F : FiniteOpenFactorization.{u, u, u} Γ(Y.left, U.1) Γ(X.left, V.1))
                  (s : Γ(upperShriekStructureSheafZeroth f j, V.1)),
                  ω.localEquiv U V hVU F (E V.1 s) =
                    (upperShriekRelativeDualizingModuleData f j).localEquiv U V hVU F s) ∧
    (∀ (c : ∀ {X Y : Scheme.{u}} (f : X ⟶ Y), IsShriekable f → CompactificationOf (Over.mk f))
        {X Y S : Scheme.{u}} (f : X ⟶ Y) {q : Y ⟶ S} {p : X ⟶ S}
        {hp : IsFiniteTypeOverNoetherian p} {hq : IsFiniteTypeOverNoetherian q}
        {ωS : quasiCoherentDerivedCategoryPlusOfModel S}
        (𝒦X : NormalizedOnOpens (UpperShriek.ofCompactifications c) hp ωS)
        (𝒦Y : NormalizedOnOpens (UpperShriek.ofCompactifications c) hq ωS)
        (_hpe : f ≫ q = p) (_hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
        [LocallyQuasiFinite f],
        haveI := hp.source_noetherian
        haveI := hq.source_noetherian
        ∃ D : RelativeDualizingModuleData f,
          D.sheaf = NormalizedOnOpens.newShriekStructureSheafZeroth c f 𝒦X 𝒦Y)
```

**`Stacks.Duality.upperShriekRelativeDualizingModuleData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizingModule.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizingModule.lean#L268). The attribute's comment: “first assertion: H^0(V, f^! O) = omega_{B/A}, compatible with restriction”.

> **Stacks Project, Tag 0BUL, first assertion.** Let `f : X ⟶ Y` be a quasi-finite morphism
> of schemes separated and of finite type over a Noetherian scheme `S`, and `f^!` the upper shriek
> of [Stacks, Tag 0A9Y] at any compactification `j`. Then `H⁰(f^!𝒪_Y)` is a relative dualizing
> module for `f` (Tag 0BVG): for affine opens `Spec(B) = V ⊆ X`, `Spec(A) = U ⊆ Y` with
> `f(V) ⊆ U` its sections over `V` are identified with `ω_{B/A}`, independently of the
> finite-open factorization computing `ω_{B/A}` and compatibly with the restriction maps.

```lean
def upperShriekRelativeDualizingModuleData (j : CompactificationOf (Over.mk f.left)) :
    RelativeDualizingModuleData f.left
```

**`Stacks.Duality.existsUnique_upperShriekRelativeDualizingComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizingModule.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizingModule.lean#L292). The attribute's comment: “first assertion: the canonical isomorphism H^0(f^! O) = omega_{Y/X}”.

> **Stacks Project, Tag 0BUL, first assertion (the canonical isomorphism).** The affine
> identifications of `upperShriekRelativeDualizingModuleData` define a canonical isomorphism
> `H⁰(f^!𝒪_Y) ≅ ω_{X/Y}` with any relative dualizing module `ω_{X/Y}` of Tag 0BVG: there is exactly
> one family of isomorphisms on sections, compatible with restriction, carrying the identification
> of `H⁰(V, f^!𝒪_Y)` with `ω_{B/A}` to that of `Γ(V, ω_{X/Y})`.

```lean
theorem existsUnique_upperShriekRelativeDualizingComparison
    (j : CompactificationOf (Over.mk f.left)) (ω : RelativeDualizingModuleData f.left) :
    ∃! E : ∀ W : X.left.Opens,
        Γ(upperShriekStructureSheafZeroth f j, W) ≃ₗ[Γ(X.left, W)] Γ(ω.sheaf, W),
      (∀ (W W' : X.left.Opens) (h : W' ≤ W) (s : Γ(upperShriekStructureSheafZeroth f j, W)),
          E W' (Stacks.AlgebraicGeometry.QuasicoherentBaseChange.restrictₗ _ h s) =
            Stacks.AlgebraicGeometry.QuasicoherentBaseChange.restrictₗ ω.sheaf h (E W s)) ∧
        ∀ (U : Y.left.affineOpens) (V : X.left.affineOpens) (hVU : V.1 ≤ f.left ⁻¹ᵁ U.1),
          letI : Algebra Γ(Y.left, U.1) Γ(X.left, V.1) := (f.left.appLE U V hVU).hom.toAlgebra
          ∀ (F : FiniteOpenFactorization.{u, u, u} Γ(Y.left, U.1) Γ(X.left, V.1))
            (s : Γ(upperShriekStructureSheafZeroth f j, V.1)),
            ω.localEquiv U V hVU F (E V.1 s) =
              (upperShriekRelativeDualizingModuleData f j).localEquiv U V hVU F s
```

## Tag 0BVI, a lemma

[Tag 0BVI](https://stacks.math.columbia.edu/tag/0BVI) in the Stacks Project.

**`Stacks.Duality.upperShriekDualSection_pushforwardTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekTraceSection.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekTraceSection.lean#L207).

> **Stacks Project, Tag 0BVI.** Let `f : X ⟶ Y` be a finite flat morphism of schemes separated
> and of finite type over a Noetherian scheme `S`, and `f^!` the upper shriek of Tag 0A9Y at any
> compactification `j`. The trace `Trace_f : f_*𝒪_X ⟶ 𝒪_Y` of Section 0BVH corresponds under
> duality to a global section of `H⁰(f^!𝒪_Y)`; via the identification `H⁰(f^!𝒪_Y) = ω_{X/Y}` of
> Tag 0BUL (`upperShriekRelativeDualizingModuleData`), this section is the trace element
> `τ_{X/Y}` of Tag 0BVJ.

```lean
theorem upperShriekDualSection_pushforwardTrace (j : CompactificationOf (Over.mk f.left)) :
    upperShriekDualSection f (pushforwardTrace f.left) j =
      relativeTraceSection (upperShriekRelativeDualizingModuleData f j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.15, Tag 0DWM](https://stacks.math.columbia.edu/tag/0DWM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
